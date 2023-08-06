# coding=utf-8
# Copyright 2022 The Pax Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Checkpointing-related utilities to handle TrainState instances."""

import enum
import re
from typing import Any, Mapping, Optional, Sequence, Tuple, cast

from absl import flags
from absl import logging
from etils import epath
import flax.serialization
import jax
from jax.experimental import multihost_utils
import numpy as np
import optax
import orbax.checkpoint
from paxml import base_task
from paxml import checkpoint_version
from paxml import train_states
from praxis import py_utils
from praxis import pytypes


CHECKPOINT_PREFIX = 'checkpoint_'
STATE_ITEM_NAME = 'state'
INPUT_ITEM_NAME = 'train_input'
METADATA_ITEM_NAME = orbax.checkpoint.checkpoint_manager.METADATA_ITEM_NAME
TMP_PREFIX = 'tmp_'
CHECKPOINT_PATTERN_RE = re.compile(rf'{CHECKPOINT_PREFIX}[\d]+$')
TMP_CHECKPOINT_PATTERN_RE = re.compile(
    rf'{TMP_PREFIX}[\d]+.{CHECKPOINT_PREFIX}[\d]+$')
# Large value to disable flax-specific checkpoint management.
_MAX_CHECKPOINT_FLAX = 1000000
get_version_key = checkpoint_version.get_version_key
get_version = checkpoint_version.get_version

JTensorOrPartitionSpec = pytypes.JTensorOrPartitionSpec
PyTree = Any
AsyncCheckpointer = orbax.checkpoint.AsyncCheckpointer
Checkpointer = orbax.checkpoint.Checkpointer
COMMIT_SUCCESS_FILE = 'commit_success.txt'


@enum.unique
class CheckpointType(str, enum.Enum):
  """The type of the checkpointing format."""

  UNSPECIFIED = 'unspecified'
  FLAX = 'flax'
  GDA = 'gda'
  PERSISTENCE = 'persistence'
  GDA_VERSION_SUBDIR = 'gda_version_subdir'


def _is_gda_version_subdir(checkpoint_path_with_step: epath.Path) -> bool:
  return checkpoint_path_with_step.name.isdigit()


def is_checkpoint_asset(x: epath.Path) -> bool:
  """Determines whether path is a checkpoint."""
  return bool(CHECKPOINT_PATTERN_RE.match(x.name))


def is_tmp_checkpoint_asset(x: epath.Path) -> bool:
  """Determines whether a checkpoint is temporary."""
  # Would only match v0.0 checkpoints, without state/metadata subdirs.
  # This case should trigger very rarely.
  if bool(TMP_CHECKPOINT_PATTERN_RE.match(x.name)):
    return True
  # Very old format Flax checkpoint.
  if x.is_file():
    return False
  return orbax.checkpoint.utils.is_tmp_checkpoint(x)


def make_metadata(version: Optional[float] = None) -> Mapping[str, Any]:
  if version is None:
    version = get_version()
  return {get_version_key(): version}


def metadata_exists(directory: epath.Path) -> bool:
  path = directory / METADATA_ITEM_NAME
  return path.is_dir() and path.exists()


def save_metadata(directory: epath.Path, metadata: Mapping[str, Any]):
  checkpointer = Checkpointer(orbax.checkpoint.JsonCheckpointHandler())
  path = directory / METADATA_ITEM_NAME
  checkpointer.save(path, metadata)


def restore_metadata(directory: epath.Path) -> Mapping[str, Any]:
  checkpointer = Checkpointer(orbax.checkpoint.JsonCheckpointHandler())
  path = directory / METADATA_ITEM_NAME
  return checkpointer.restore(path)


def get_version_and_save_dir(
    checkpoint_step_dir: epath.Path,
) -> Tuple[float, epath.Path]:
  return get_version(), checkpoint_step_dir / STATE_ITEM_NAME


def get_version_and_restore_dir(
    checkpoint_step_dir: epath.Path,
) -> Tuple[float, epath.Path]:
  version = 0.
  if metadata_exists(checkpoint_step_dir):
    version = restore_metadata(checkpoint_step_dir)[get_version_key()]
  if version > 0:
    restore_dir = checkpoint_step_dir / STATE_ITEM_NAME
  else:
    restore_dir = checkpoint_step_dir
  return version, restore_dir


def checkpoint_name(
    step: int,
    checkpoint_type: CheckpointType = CheckpointType.UNSPECIFIED,
) -> str:
  if checkpoint_type == CheckpointType.FLAX:
    return f'{CHECKPOINT_PREFIX}{step}'
  elif checkpoint_type == CheckpointType.GDA_VERSION_SUBDIR:
    return str(step)
  else:
    return f'{CHECKPOINT_PREFIX}{step:08d}'


def make_checkpoint_step_dir(
    checkpoint_dir: epath.Path,
    step: int,
    checkpoint_type: CheckpointType = CheckpointType.UNSPECIFIED,
) -> epath.Path:
  return checkpoint_dir / checkpoint_name(step, checkpoint_type=checkpoint_type)


def get_step_from_checkpoint_asset(checkpoint_dir: epath.PathLike) -> int:
  checkpoint_dir = epath.Path(checkpoint_dir)
  if _is_gda_version_subdir(checkpoint_dir):
    return int(checkpoint_dir.name)
  if is_tmp_checkpoint_asset(checkpoint_dir):
    return int(checkpoint_dir.suffix[len(CHECKPOINT_PREFIX):])
  return int(checkpoint_dir.stem[len(CHECKPOINT_PREFIX):])


def maybe_update_checkpoint_type(
    user_specified_type: CheckpointType,
    checkpoint_path_with_step: epath.Path,
) -> CheckpointType:
  """Returns the GDA checkpoint type that matches the provided path.

  Args:
    user_specified_type: CheckpointType of the checkpoint provided by the user.
    checkpoint_path_with_step: Absolute path to the checkpoint directory that
      includes the step number e.g. "/some/path/checkpoints/checkpoint_001".

  Returns:
    The updated CheckpointType matching the provided absolute path.
  """
  if user_specified_type != CheckpointType.GDA:
    return user_specified_type
  if _is_gda_version_subdir(checkpoint_path_with_step):
    return CheckpointType.GDA_VERSION_SUBDIR
  return CheckpointType.GDA


def retrieve_checkpoint_type(
    maybe_use_persistence_checkpointing,
    task_p: base_task.BaseTask.HParams) -> CheckpointType:
  """Retrieves the CheckpointType given the input arguments."""
  using_pjit = task_p.model.mesh_shape is not None  # pytype: disable=attribute-error
  if using_pjit or py_utils.pmap_use_tensorstore():
    if maybe_use_persistence_checkpointing:
      return CheckpointType.PERSISTENCE
    else:
      return CheckpointType.GDA
  else:
    # pmap uses FLAX, Persistence-based or not.
    return CheckpointType.FLAX


def save_checkpoint(
    train_state: train_states.TrainState,
    checkpoint_dir: epath.PathLike,
    overwrite: bool = False,
    checkpoint_type: CheckpointType = CheckpointType.FLAX,
    state_specs: Optional[train_states.TrainState] = None,
    async_checkpointer: Optional[AsyncCheckpointer] = None,
) -> None:
  """Saves a checkpoint into the provided base directory.

  This is typically called on a replicated TrainState instance.

  Args:
    train_state: The TrainState instance to save.
    checkpoint_dir: The base directory from where to retrieve checkpoints.
    overwrite: Whether to overwrite existing checkpoints files if a checkpoint
      at the current or a later step already exists.
    checkpoint_type: The checkpoint type (implementation) to save. Either
      `FLAX`, `GDA` or `PERSISTENCE`.
    state_specs: Currently unused.
    async_checkpointer: When async checkpointing and Orbax are enabled, allows
      training to continue when checkpointing is going on as checkpointing
      happens in a different thread.

  Raises:
    ValueError: If the global step has an unexpected shape, if `state_specs`
    is not specified for persistence-based checkpointing or if
    `checkpoint_type` is invalid.
  """
  del state_specs

  checkpoint_dir = epath.Path(checkpoint_dir)
  step = int(py_utils.maybe_unreplicate_for_fully_replicated(train_state.step))

  checkpoint_step_dir = make_checkpoint_step_dir(
      checkpoint_dir, step, checkpoint_type=checkpoint_type
  )
  version, checkpoint_save_dir = get_version_and_save_dir(checkpoint_step_dir)
  if checkpoint_type == CheckpointType.GDA:
    if async_checkpointer is not None:
      async_checkpointer.save(checkpoint_save_dir, train_state, version=version)
    else:
      checkpointer = orbax.checkpoint.Checkpointer(
          PaxCheckpointHandler())
      checkpointer.save(checkpoint_save_dir, train_state, version=version)
  elif checkpoint_type == CheckpointType.FLAX:
    checkpointer = FlaxCheckpointer(FlaxCheckpointHandler())
    checkpointer.save(
        checkpoint_save_dir, train_state, force=overwrite, version=version
    )
  else:
    raise ValueError(f'Unexpected checkpoint_type `{checkpoint_type}`.')

  # Save metadata.
  save_metadata(checkpoint_step_dir, make_metadata())


def latest_checkpoint(checkpoint_dir: epath.PathLike) -> Optional[epath.Path]:
  """Gets the path to the latest checkpoint.

  Args:
    checkpoint_dir: The base directory from where to retrieve checkpoints.

  Returns:
    Path to latest checkpoint or None if there is no checkpoint.
  """
  checkpoint_dir = epath.Path(checkpoint_dir)
  if not checkpoint_dir.exists():
    return None
  checkpoint_assets = [
      v
      for v in checkpoint_dir.iterdir()
      if is_checkpoint_asset(v) and not is_tmp_checkpoint_asset(v)
  ]
  if not checkpoint_assets:
    return None
  checkpoint_assets = sorted(
      checkpoint_assets, key=get_step_from_checkpoint_asset)
  return checkpoint_dir / checkpoint_assets[-1]


def retrieve_latest_checkpoint_step(
    checkpoint_dir: epath.Path) -> Optional[int]:
  """Retrieves the latest checkpoint step if any.

  Note that this broadcasts the checkpoint step from host 0 to ensure that all
  processes get the exact same checkpoint step.

  Args:
    checkpoint_dir: The base directory from where to retrieve checkpoints.

  Returns:
    The latest checkpoint step as an integer or None if no checkpoint is found.
  """
  if not checkpoint_dir.exists():
    checkpoint_step = -1
  else:
    latest_checkpoint_path = latest_checkpoint(checkpoint_dir)
    if latest_checkpoint_path is None:
      checkpoint_step = -1
    else:
      checkpoint_step = get_step_from_checkpoint_asset(latest_checkpoint_path)
  np_checkpoint_step = multihost_utils.broadcast_one_to_all(
      np.array(checkpoint_step))
  multihost_utils.assert_equal(np_checkpoint_step,
                               "checkpoint_steps across hosts don't match.")
  step = int(np_checkpoint_step.item())
  if step == -1:
    return None
  return step


def restore_checkpoint(
    state_global_shapes: train_states.TrainState,
    checkpoint_dir: epath.PathLike,
    global_mesh: Optional[jax.sharding.Mesh] = None,
    checkpoint_type: CheckpointType = CheckpointType.FLAX,
    state_specs: Optional[train_states.TrainState] = None,
    step: Optional[int] = None,
    enforce_restore_shape_check: bool = False,
) -> Optional[train_states.TrainState]:
  """Restores a checkpoint from the provided base directory.

  This is typically called on an unreplicated TrainState instance.

  Args:
    state_global_shapes: The TrainState with variable names and corresponding
      ShapeDtypeStruct.
    checkpoint_dir: The base directory from where to retrieve checkpoints.
    global_mesh: The global mesh representing devices across multiple processes.
    checkpoint_type: The checkpoint type (implementation) to restore. Either
      `FLAX`, `GDA` or `PERSISTENCE`.
    state_specs: If using a GDA-based checkpoint, the partition specs
      corresponding to this TrainState instance to restore.
    step: Step number to load a checkpoint from or None to load the latest.
    enforce_restore_shape_check: Raises an error if restore shapes do not match
      checkpoint shapes.

  Returns:
    A restored `TrainState` instance. If no step specified and no checkpoint
    files present, return None.

  Raises:
    ValueError: When a mismatch between the current checkpoint structure and
    the saved checkpoint one is detected.
  """
  checkpoint_dir = epath.Path(checkpoint_dir)
  if step is None:
    step = retrieve_latest_checkpoint_step(checkpoint_dir)
    if step is None:
      logging.info('No checkpoint found for restore in %s.', checkpoint_dir)
      return None
  checkpoint_step_dir = make_checkpoint_step_dir(
      checkpoint_dir, step, checkpoint_type=checkpoint_type
  )
  version, checkpoint_restore_dir = get_version_and_restore_dir(
      checkpoint_step_dir
  )
  if checkpoint_type in {CheckpointType.GDA, CheckpointType.GDA_VERSION_SUBDIR}:
    checkpointer = orbax.checkpoint.Checkpointer(
        PaxCheckpointHandler(
            enforce_restore_shape_check=enforce_restore_shape_check
        )
    )
    restored_train_state = checkpointer.restore(
        checkpoint_restore_dir,
        item=state_global_shapes,
        specs=state_specs,
        mesh=global_mesh,
        version=version,
    )
    return restored_train_state
  elif checkpoint_type == CheckpointType.FLAX:
    checkpointer = FlaxCheckpointer(FlaxCheckpointHandler())
    return checkpointer.restore(
        checkpoint_restore_dir, item=state_global_shapes, version=version
    )
  else:
    raise ValueError(f'Unexpected checkpoint_type `{checkpoint_type}`.')


def reregister_type_handlers(tensorstore_metadata_key: Optional[str] = None):
  """Registers overrides to Orbax TypeHandlers to set Pax-specific properties."""
  if tensorstore_metadata_key is None:
    return
  orbax.checkpoint.type_handlers.register_standard_handlers_with_options(
      metadata_key=tensorstore_metadata_key
  )


def _extract_nested_prefix_names(
    state: train_states.TrainState) -> train_states.TrainState:
  """Extracts prefix names from a TrainState data structure."""
  # CNS doesn't support square bracket in filenames.
  key_separator = '.'
  left_separator = '_'
  right_separator = ''
  return train_states.TrainState(
      step=py_utils.extract_prefixed_keys_from_nested_map(
          state.step,
          'step',
          key_separator=key_separator,
          left_separator=left_separator,
          right_separator=right_separator),
      mdl_vars=py_utils.extract_prefixed_keys_from_nested_map(
          state.mdl_vars,
          'mdl_vars',
          key_separator=key_separator,
          left_separator=left_separator,
          right_separator=right_separator),
      opt_states=py_utils.extract_prefixed_keys_from_nested_map(
          state.opt_states,
          'opt_states',
          key_separator=key_separator,
          left_separator=left_separator,
          right_separator=right_separator,
          is_leaf=py_utils.is_optax_masked_node))


def _masked_node_to_none(mask: Any, value: Any) -> Any:
  """Return value when `mask` is not a MaskedNode, or MaskedNode otherwise."""
  if py_utils.is_optax_masked_node(mask):
    return optax.MaskedNode()
  return value


def _tensorstore_prepare(
    train_state: train_states.TrainState,
    state_specs: Optional[train_states.TrainState] = None
) -> Tuple[Sequence[JTensorOrPartitionSpec], Sequence[str],
           Optional[Sequence[JTensorOrPartitionSpec]]]:
  """Prepares data prior to saving/restoring it from/to TensorStore.

  Args:
    train_state: A partitioned train_state that is a Pytree of
      GlobalDeviceArray.
    state_specs: [optional] The partition specs corresponding to this TrainState
      instance, when it is used for checkpoint restoring.

  Returns:
    A 3-tuple (flattened_traine_state, flattened_nested_names, out), where:
    - flattened_traine_state: A flattened version of the train state, where all
      MaskedNode instances have been filtered out.
    - flattened_nested_names: A flattened version of the nested names, where all
      entries corresponding to MaskedNode have been filtered out.
    - out: Either None when the input state_specs is None or the flattened
      version of the state_specs, where all entries corresponding to MaskedNode
      instances have been filtered out.
  """
  # This replaces MaskedNode instances by None values ...
  train_state_none = jax.tree_map(
      _masked_node_to_none,
      train_state,
      train_state,
      is_leaf=py_utils.is_optax_masked_node,
  )
  if state_specs is not None:
    state_specs_none = jax.tree_map(
        _masked_node_to_none,
        train_state,
        state_specs,
        is_leaf=py_utils.is_optax_masked_node)
  # ... that are filtered out when calling jax.tree_util.tree_flatten() here.
  flattened_train_state, _ = jax.tree_util.tree_flatten(train_state_none)
  if state_specs is not None:
    flattened_state_specs, _ = jax.tree_util.tree_flatten(state_specs_none)
  else:
    flattened_state_specs = None

  # _extract_nested_prefix_names() also replaces MaskedNode instances by None
  # values ...
  nested_names = _extract_nested_prefix_names(train_state)
  # ... that are filtered out when calling jax.tree_util.tree_flatten() here.
  flattened_nested_names, _ = jax.tree_util.tree_flatten(nested_names)
  return flattened_train_state, flattened_nested_names, flattened_state_specs


def _tensorstore_reconstruct(
    state_global_shapes: train_states.TrainState,
    restored_train_state: Sequence[JTensorOrPartitionSpec]
) -> train_states.TrainState:
  """Reconstructs a nested train state including MaskedNode.

  Args:
    state_global_shapes: The original nested train state with GDAs, which
      includes MaskedNode entries.
    restored_train_state: A flattened version of the restored train state, which
      does not include any MaskedNode entry.

  Returns:
    A nested version of `restored_train_state` after adding back the MaskedNode
    instances, based on the original structure of `state_global_shapes`.
  """
  c = 0
  restored_flattened_train_state = []
  flattened_state_global_shapes, treedef = jax.tree_util.tree_flatten(
      state_global_shapes)
  for l in flattened_state_global_shapes:
    if py_utils.is_optax_masked_node(l):
      restored_flattened_train_state.append(optax.MaskedNode())
    else:
      restored_flattened_train_state.append(restored_train_state[c])
      c += 1
  assert c == len(restored_train_state)
  return jax.tree_util.tree_unflatten(treedef, restored_flattened_train_state)


def _check_restored_shapes(
    restored: Sequence[JTensorOrPartitionSpec],
    expected: Sequence[JTensorOrPartitionSpec],
):
  def _check(a, b):
    if a.shape != b.shape:
      raise ValueError(
          f'Restored parameter shape mismatch: {a.shape} (checkpoint) vs.'
          f' {b.shape} (expected).'
      )

  jax.tree_util.tree_map(_check, restored, expected)


class PaxCheckpointHandler(orbax.checkpoint.PyTreeCheckpointHandler):
  """PaxCheckpointHandler override for Pax GDA checkpointing.

  Allows setting parameter names manually, which would normally be extracted
  from the train state itself. This is somewhat hacky, and we will aim to remove
  it eventually (see below).

  TODO(cpgaffney) Rework _extract_nested_prefix_names to allow extracting names
  from a state dict.
  """

  def __init__(
      self, *args, enforce_restore_shape_check: bool = False, **kwargs
  ):
    self._enforce_restore_shape_check = enforce_restore_shape_check
    super().__init__(*args, **kwargs)

  _param_names: PyTree = None

  def _set_param_names(self, param_names: PyTree):
    self._param_names = param_names

  def _get_param_names(self, item: PyTree) -> PyTree:
    return self._param_names

  async def _write_aggregate_file(self, directory: epath.Path, item: PyTree,
                                  param_infos: PyTree, save_args: PyTree):
    """Skip writing msgpack file for Pax since this file would be unused."""
    pass

  async def async_save(
      self,
      directory: epath.Path,
      item: PyTree,
      save_args: Optional[PyTree] = None,
      version: Optional[float] = None,
  ) -> Any:
    """Filters optax.MaskedNode before calling superclass async_save."""
    if version is None:
      raise ValueError('Expected version for saving.')
    flattened_train_state, flattened_nested_names, _ = _tensorstore_prepare(
        item)
    # At that point, the flattened entries do not contain any reference to
    # MaskedNode's.
    self._set_param_names(flattened_nested_names)
    return await super().async_save(
        directory, flattened_train_state, save_args=save_args)

  def restore(
      self,
      directory: epath.Path,
      item: Optional[PyTree] = None,
      specs: Optional[PyTree] = None,
      mesh: Optional[jax.sharding.Mesh] = None,
      version: Optional[float] = None,
  ) -> PyTree:
    """Restores by filtering optax.MaskedNode and adding it back after calling superclass restore."""
    if version is None:
      raise ValueError('Expected version for restoration.')
    flattened_train_state, flattened_nested_names, flattened_state_specs = (
        _tensorstore_prepare(item, specs))
    # At that point, the flattened entries do not contain any reference to
    # MaskedNode's.
    self._set_param_names(flattened_nested_names)

    def create_restore_args(pspec, shape_struct):
      # Providing `None` indicates that the shape should be restored exactly as
      # saved.
      restore_shape = (
          None if self._enforce_restore_shape_check else shape_struct.shape
      )
      return orbax.checkpoint.ArrayRestoreArgs(
          restore_type=jax.Array,
          mesh=mesh,
          mesh_axes=pspec,
          global_shape=restore_shape,
          dtype=shape_struct.dtype,
      )

    restore_args = jax.tree_map(create_restore_args, flattened_state_specs,
                                flattened_train_state)

    # Consequently, we restore the checkpoint that does not contain any
    # reference to MaskedNode's.
    restored_train_state = super().restore(
        directory, item=flattened_train_state, restore_args=restore_args)
    if self._enforce_restore_shape_check:
      _check_restored_shapes(restored_train_state, flattened_train_state)

    # We add back the MaskedNode entries into the pytree.
    restored_train_state = _tensorstore_reconstruct(item, restored_train_state)

    return restored_train_state

  def structure(self, directory: epath.Path) -> PyTree:
    return jax.tree_util.tree_map(
        orbax.checkpoint.utils.leaf_placeholder,
        flax.serialization.to_state_dict(self._param_names))


class FlaxCheckpointHandler(orbax.checkpoint.PyTreeCheckpointHandler):
  """Override to process checkpoints in Flax format.

  Should only be used in conjunction with FlaxCheckpointer.
  """

  async def async_save(
      self,
      directory: epath.Path,
      item: PyTree,
      save_args: Optional[PyTree] = None,
      version: Optional[float] = None,
  ) -> Any:
    if version is None:
      raise ValueError('Expected version for saving.')
    # Extract/flatten data structure to store to disk. Flax requires a flattened
    # data structure to be passed to the checkpointer.
    flattened_state, pytree_state = jax.tree_util.tree_flatten(
        jax.device_get(item)
    )
    checkpoint_target = {
        'flattened_state': flattened_state,
        # Saves a serialized version of the pytree structure to detect potential
        # mismatch caused by different versions of saver/restorer.
        'str_pytree_state': str(pytree_state),
    }
    assert save_args is None
    save_args = jax.tree_util.tree_map(
        lambda _: orbax.checkpoint.SaveArgs(aggregate=True), checkpoint_target
    )
    return await super().async_save(
        directory, checkpoint_target, save_args=save_args
    )

  def restore(
      self,
      directory: epath.Path,
      item: Optional[PyTree] = None,
      restore_args: Optional[PyTree] = None,
      transforms: Optional[PyTree] = None,
      transforms_default_to_original: bool = True,
      version: Optional[float] = None,
  ) -> PyTree:
    if version is None:
      raise ValueError('Expected version for restoration.')
    # Input the same data structure as in save_checkpoint().
    flattened_state, pytree_state = jax.tree_util.tree_flatten(item)
    str_pytree_state = str(pytree_state)
    input_target = {
        'flattened_state': flattened_state,
        'str_pytree_state': str_pytree_state,
    }
    restored_target = super().restore(directory, input_target)
    # Flax restore_checkpoint returned input_target unchanged if
    # no step specified and no checkpoint files present.
    if restored_target is input_target:
      return None
    restored_state = restored_target['flattened_state']
    restored_str_pytree_state = restored_target['str_pytree_state']
    if restored_str_pytree_state != str_pytree_state:
      # Could be spurious due to abbreviation of treedef printing added in
      # https://github.com/tensorflow/tensorflow/commit/aa21adc148c98c76f54ba5932ce34cf59da538c4
      logging.warning(
          (
              'A possible mismatch (could be spurious) between the saved '
              'checkpoint structure and the current one has been detected '
              '(%s vs %s).'
          ),
          restored_str_pytree_state,
          str_pytree_state,
      )
    return jax.tree_util.tree_unflatten(pytree_state, restored_state)


class FlaxCheckpointer(orbax.checkpoint.Checkpointer):
  """Allows restoring legacy Flax checkpoints, which are not directories.

  Should only be used in conjunction with FlaxCheckpointHandler.
  """

  def restore(
      self,
      directory: epath.PathLike,
      *args,
      item: Optional[Any] = None,
      **kwargs,
  ) -> Any:
    if not isinstance(self._handler, FlaxCheckpointHandler):
      raise ValueError('Unsupported handler for FlaxCheckpointer.')
    self._handler = cast(FlaxCheckpointHandler, self._handler)
    directory = epath.Path(directory)
    original_aggregate_filename = self._handler._aggregate_filename  # pylint: disable=protected-access
    # If is_file, then the checkpoint is in legacy format, not saved with orbax.
    # Orbax checkpoints are directories containing a file called 'checkpoint'.
    if directory.is_file():
      # The msgpack file is actually the "directory".
      self._handler._aggregate_filename = directory.name  # pylint: disable=protected-access
      directory = directory.parent
    result = super().restore(directory, *args, item=item, **kwargs)
    # Reset aggregate_filename back to normal.
    self._handler._aggregate_filename = (  # pylint: disable=protected-access
        original_aggregate_filename
    )
    return result


class BaseInputCheckpointHandler(orbax.checkpoint.CheckpointHandler):
  """A CheckpointHandler implementation that handles a tf.data BaseInput (sub)class.

  Useful for distributed input where the data iterator on the server cannot be
  accessed from the client, and thus we cannot call .save() and .restore() with
  input._iter like other implementations of DatasetCheckpointHandler.
  """

  def save(self, directory: epath.Path, item: Any):
    """Saves the given item.

    Args:
      directory: save location directory.
      item: a BaseInput to be saved, which must have save() implemented.
    """
    checkpoint_path = (
        directory / f'process_{jax.process_index()}-of-{jax.process_count()}'
    )
    item.save(checkpoint_path)

  def restore(
      self, directory: epath.Path, item: Any = None
  ) -> None:
    """Restores the given item.

    Args:
      directory: restore location directory.
      item: a BaseInput to be restored, which must have restore() implemented.
        Not Optional (declared as optional to conform to
        orbax.checkpoint.CheckpointHandler superclass)
    """
    if item is None:
      raise ValueError('Must provide item to restore')
    if not directory.exists():
      raise ValueError(f'Checkpoint dir {directory} does not exist.')
    checkpoint_path = (
        directory / f'process_{jax.process_index()}-of-{jax.process_count()}'
    )
    item.restore(checkpoint_path)

  def structure(self, directory: epath.Path) -> Any:
    """Unimplemented. See parent class."""
    return NotImplementedError
