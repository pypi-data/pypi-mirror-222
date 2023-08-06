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

"""Learning rate schedule."""

from __future__ import annotations

import abc
import dataclasses
import math
from typing import Any, Optional, Sequence, Tuple

import jax
from jax import numpy as jnp
import optax
from praxis import base_hyperparams
from praxis import pax_fiddle
from praxis import pytypes

JTensor = pytypes.JTensor
InstantiableHyperParams = base_hyperparams.InstantiableHyperParams
instantiate = base_hyperparams.instantiate


class BaseSchedule(base_hyperparams.FiddleBaseParameterizable, abc.ABC):
  """Base class for all schedules."""

  @abc.abstractmethod
  def value_at(self, step: JTensor) -> JTensor:  # pylint:disable=invalid-name
    """Returns the value of schedule at step 'step'.

    Args:
      step: A scalar uint32 array.

    Returns:
      A float32 value of the schedule at step 'step' as a scalar array.
    """
    raise NotImplementedError()


class Constant(BaseSchedule):
  """A schedule whose value is a constant.

  Attributes:
    value: The constant value.
  """
  value: float = 1.0

  def value_at(self, step: JTensor) -> JTensor:
    del step
    return jnp.array(self.hparams.value, dtype=jnp.float32)


class Polynomial(BaseSchedule):
  """Polynomial learning rate schedule.

  If x < x0, returns y0. If x >= x1, returns y1. Otherwise, interpolate with
  a polynomial between (x0, y0) and (x1, y1).

  Attributes:
    power: Polynomial power.
    start: (x0, y0)
    limit: (x1, y1)
    origin: Origin of the polynomial. Can be "start" or "limit".
  """
  power: int = 1
  start: Tuple[int, float] = (0, 1.0)
  limit: Tuple[int, float] = (1, 1.0)
  origin: str = 'start'

  def __post_init__(self):
    super().__post_init__()
    p = self.hparams
    if len(p.start) != 2:
      raise ValueError(f'{p.start} must be of length 2.')
    if len(p.limit) != 2:
      raise ValueError(f'{p.limit} must be of length 2.')
    x0, _ = p.start
    x1, _ = p.limit
    if x0 >= x1:
      raise ValueError(f'{x0} must be < {x1}')
    if p.origin not in {'start', 'limit'}:
      raise ValueError('Invalid parameter origin: %s' % p.origin)

  def value_at(self, step: JTensor) -> JTensor:
    p = self.hparams
    x = jnp.array(step).astype(jnp.float32)
    x0, y0 = p.start
    x1, y1 = p.limit
    ratio = (x - x0) / (x1 - x0)
    if p.origin == 'start':
      f_x = ratio**p.power
    elif p.origin == 'limit':
      f_x = 1 - (1 - ratio)**p.power
    y = y0 + f_x * (y1 - y0)
    return jnp.where(x < x0, y0, jnp.where(x >= x1, y1, y))


class Linear(Polynomial):
  """Linear learning rate schedule.

  If x < x0, returns y0. If x >= x1, returns y1. Otherwise, interpolate
  linearly between (x0, y0) and (x1, y1).

  Attributes:
    value: The constant value.
  """
  power: int = 1


class Exponential(BaseSchedule):
  """Exponential learning rate schedule.

  Attributes:
    start: (x0, y0)
    limit: (x1, y1)
  """
  start: Tuple[int, float] = (0, 1.0)
  limit: Tuple[int, float] = (1, 0.5)
  linear: Any = dataclasses.field(init=False, repr=False)

  def __post_init__(self):
    super().__post_init__()
    p = self.hparams
    x0, y0 = p.start
    x1, y1 = p.limit
    assert x0 < x1, '%s must be < %s' % (x0, x1)
    assert y0 > 0, '%s must be > 0' % y0
    assert y1 > 0, '%s must be > 0' % y1
    self.linear = instantiate(
        Linear.HParams(start=(x0, math.log(y0)), limit=(x1, math.log(y1))))

  def value_at(self, step: JTensor) -> JTensor:
    return jnp.exp(self.linear.value_at(step))


class Cosine(BaseSchedule):
  """Cosine learning rate schedule.

  Attributes:
    initial_value: Initial decay value.
    final_value: Final decay value.
    total_steps: Number of steps to reach full decay.
  """
  initial_value: float = 1.0
  final_value: float = 0.0
  total_steps: int = 0

  def value_at(self, step: JTensor) -> JTensor:
    p = self.hparams
    decay_gap = p.initial_value - p.final_value
    return p.final_value + 0.5 * decay_gap * (
        1
        + jnp.cos(
            math.pi
            * jnp.minimum(
                1.0, jnp.array(step, dtype=jnp.float32) / p.total_steps
            )
        )
    )


class DelayedCosine(BaseSchedule):
  """Cosine learning rate schedule that can be delayed before it starts.

  Attributes:
    start: (x0, y0)
    limit: (x1, y1)
  """
  start: Tuple[int, float] = (0, 1.0)
  limit: Tuple[int, float] = (1, 0.5)
  max: Any = dataclasses.field(init=False, repr=False)
  min: Any = dataclasses.field(init=False, repr=False)
  linear: Any = dataclasses.field(init=False, repr=False)

  def __post_init__(self):
    super().__post_init__()
    p = self.hparams
    x0, y0 = p.start
    x1, y1 = p.limit
    assert x0 < x1, '%s must be < %s' % (x0, x1)
    assert y0 > 0, '%s must be > 0' % y0
    assert y1 > 0, '%s must be > 0' % y1
    self.max = y0
    self.min = y1
    self.linear = instantiate(
        Linear.HParams(start=(x0, 0), limit=(x1, math.pi)))

  def value_at(self, step: JTensor) -> JTensor:
    decay_gap = self.max - self.min
    return self.min + 0.5 * decay_gap * (
        1 + jnp.cos(jnp.array(self.linear.value_at(step), dtype=jnp.float32))
    )


class LinearRampupPolynomialDecay(BaseSchedule):
  """Learning rate that linearly ramps up to max and then polynomial decays.

  Attributes:
    warmup_steps: Increases the learning rate linearly before warmup steps.
    decay_start: Starts the learning rate decay at decay_start-th step.
    decay_end: Ends the learning rate decay at decay_end-th step.
    power: Polynomial power.
    min_ratio: After decay_end, the multiplier stays at min.
    max: The schedule is never larger than this value.
  """

  warmup_steps: int = 0
  decay_start: int = 0
  decay_end: int = 0
  power: int = 1
  min_ratio: float = 0.01
  max: float = 0.0
  _schedules: Any = dataclasses.field(init=False, repr=False)
  _boundaries: Any = dataclasses.field(init=False, repr=False)

  def __post_init__(self):
    super().__post_init__()

    p = self.hparams

    assert (
        p.decay_start >= p.warmup_steps
    ), 'decay_start must greater than warmup_steps.'
    assert (
        p.decay_end >= p.decay_start
    ), 'decay_end must be greater than decay_start'
    assert p.max > 0, 'Must set max.'

    self._schedules = []
    self._boundaries = []
    if p.warmup_steps > 0:
      self._schedules.append(
          instantiate(
              Linear.HParams(start=(0, 0.0), limit=(p.warmup_steps, p.max))
          )
      )
      self._boundaries.append(p.warmup_steps)
    if p.decay_start > p.warmup_steps:
      self._schedules.append(
          instantiate(
              Linear.HParams(
                  start=(0, p.max),
                  limit=(p.decay_start - p.warmup_steps, p.max),
              )
          )
      )
      self._boundaries.append(p.decay_start)
    self._schedules.append(
        instantiate(
            Polynomial.HParams(
                start=(0, p.max),
                limit=(p.decay_end - p.decay_start, p.max * p.min_ratio),
                power=p.power,
            )
        )
    )

  def value_at(self, step: JTensor) -> JTensor:
    return jnp.array(
        optax.join_schedules(
            [s.value_at for s in self._schedules], self._boundaries
        )(step),
        jnp.float32,
    )


class LinearRampupCosineDecay(BaseSchedule):
  """Learning rate that first linearly ramps up to max and then cos decays.

  Attributes:
    warmup_steps: Increases the learning rate linearly before warmup steps.
    decay_start: Starts the learning rate decay at decay_start-th step.
    decay_end: Ends the learning rate decay at decay_end-th step.
    min_ratio: After decay_end, the multiplier stays at min.
    max: The schedule is never larger than this value.
  """
  warmup_steps: int = 0
  decay_start: int = 0
  decay_end: int = 0
  min_ratio: float = 0.01
  max: float = 0.0
  _schedules: Any = dataclasses.field(init=False, repr=False)
  _boundaries: Any = dataclasses.field(init=False, repr=False)

  def __post_init__(self):
    super().__post_init__()

    p = self.hparams

    assert p.decay_start >= p.warmup_steps, (
        f'decay_start ({p.decay_start}) must greater than warmup_steps'
        f' ({p.warmup_steps}).'
    )
    assert p.decay_end >= p.decay_start, (
        f'decay_end ({p.decay_end}) must be greater than decay_start'
        f' ({p.decay_start})'
    )
    assert p.max > 0, 'Must set max.'

    self._schedules = []
    self._boundaries = []
    if p.warmup_steps > 0:
      self._schedules.append(
          instantiate(
              Linear.HParams(start=(0, 0.0), limit=(p.warmup_steps, p.max))))
      self._boundaries.append(p.warmup_steps)
    if p.decay_start > p.warmup_steps:
      self._schedules.append(
          instantiate(
              Linear.HParams(
                  start=(0, p.max),
                  limit=(p.decay_start - p.warmup_steps, p.max))))
      self._boundaries.append(p.decay_start)
    self._schedules.append(
        instantiate(
            DelayedCosine.HParams(
                start=(0, p.max),
                limit=(p.decay_end - p.decay_start, p.max * p.min_ratio))))

  def value_at(self, step: JTensor) -> JTensor:
    return jnp.array(
        optax.join_schedules(
            [s.value_at for s in self._schedules], self._boundaries
        )(step),
        jnp.float32,
    )


class PiecewiseConstant(BaseSchedule):
  """A schedule with piecewise constants rate decay.

  Attributes:
    boundaries: Boundaries at which learning rate drops.
    values: Values in each interval. The number of values must be equal to the
      the number of boundaries plus 1.
  """
  boundaries: Optional[Sequence[int]] = None
  values: Optional[Sequence[int]] = None

  def __post_init__(self):
    super().__post_init__()
    p = self.hparams
    if p.boundaries is None or p.values is None:
      raise ValueError(
          'The parameters `boundaries` and `values` must not be None.')
    if len(p.values) != len(p.boundaries) + 1:
      raise ValueError(
          f'The number of values ({len(p.values)}) is expected to be equal '
          f'to the number of boundaries plus 1 ({len(p.boundaries) + 1}).')
    if sorted(p.boundaries) != list(p.boundaries):
      raise ValueError(f'The boundaries ({p.boundaries}) must be sorted.')

  def value_at(self, step: JTensor) -> JTensor:
    p = self.hparams
    # Map the step/boundaries to jnp.float32.
    boundaries = [jnp.array(v, dtype=jnp.float32) for v in p.boundaries]
    values = [jnp.array(v, dtype=jnp.float32) for v in p.values]
    step = step.astype(jnp.float32)
    if not boundaries:
      assert len(values) == 1
      return values[0]
    v = 0
    for i, threshold in enumerate(boundaries):
      indicator = jnp.maximum(0.0, jnp.sign(threshold - step))
      v = jnp.where(v > 0, v, indicator * values[i])
    # Check if step is greater equal to the last value.
    indicator = jnp.maximum(0.0, jnp.sign(1 + step - boundaries[-1]))
    v = jnp.where(v > 0, v, indicator * values[-1])
    return v


class Transformer(BaseSchedule):
  """Inverse-decay learning rate until warmup_steps, then decay.

  Attributes:
    warmup_steps: Increase the learning rate linearly for the first warmup_steps
      training steps.
    model_dim: Model dimension that applies to embedding layers and all
      Transformer layers.
    worker_replicas: Number of worker replicas.
    decay_end: Ends the learning rate decay at decay_end-th step.
  """
  warmup_steps: int = 4000
  model_dim: int = 512
  worker_replicas: int = 1
  decay_end: Optional[int] = None

  def value_at(self, step: JTensor) -> JTensor:
    """Returns the current learning rate decay."""
    p = self.hparams
    current_step = step.astype(jnp.float32)
    model_dim = jnp.array(p.model_dim, dtype=jnp.float32)
    warmup_steps = jnp.array(
        p.warmup_steps * p.worker_replicas, dtype=jnp.float32)
    if p.decay_end is not None:
      decay_end = jnp.array(p.decay_end, dtype=jnp.float32)
      current_step = jnp.where(current_step < decay_end, current_step,
                               decay_end)
    return model_dim**-0.5 * jnp.minimum(
        (current_step + 1) * warmup_steps**-1.5, (current_step + 1)**-0.5)


class SqrtDecay(BaseSchedule):
  """Square root decay learning rate after decay_start steps.

  Attributes:
    decay_start: Keep the learning rate constant till this step, and begin
      decaying using inverse square root after this step.
    multiplier: Multiplier for the loss.
    offset: Offset for computing when to start decaying the learning rate.
  """
  decay_start: int = 10000
  multiplier: float = 1.0
  offset: float = 0.0

  def value_at(self, step: JTensor) -> JTensor:
    """Returns the current learning rate decay."""
    p = self.hparams
    current_step = step.astype(jnp.float32)
    offset = jnp.array(p.offset, dtype=jnp.float32)
    decay_start = jnp.array(p.decay_start, dtype=jnp.float32)
    multiplier = jnp.array(p.multiplier, dtype=jnp.float32)
    return jax.lax.rsqrt(jnp.maximum(current_step - offset,
                                     decay_start)) * multiplier


class LinearRampupSqrtDecay(BaseSchedule):
  """Linearly increases the schedule value in warmup_steps, then sqrt decay.

  Same as the Transformer schedule, except that this one is explicitly
  parameterized by the peak value (instead of model_dim).

  For the original Transformer schedule, the peak value is
    1.0 / sqrt(model_dim * warmup_steps).

  Attributes:
    decay_start: Keep the learning rate constant till this step, and begin
      decaying using inverse square root after this step.
    multiplier: Multiplier for the loss.
    offset: Offset for computing when to start decaying the learning rate.
  """
  peak: float = 1.0
  warmup_steps: int = 4000

  def value_at(self, step: JTensor) -> JTensor:
    """Returns the current schedule value."""
    p = self.hparams
    current_step = jnp.maximum(step.astype(jnp.float32), 1)
    warmup_steps = jnp.array(p.warmup_steps, dtype=jnp.float32)
    return p.peak * jnp.minimum(current_step / warmup_steps,
                                jnp.sqrt(warmup_steps / current_step))


class LinearRampupExponentialDecay(BaseSchedule):
  """Learning rate that first linearly ramps up to max and exponentially decays.

  Attributes:
    warmup_steps: Increases the learning rate linearly  before warmup_steps *
      num_splits steps.
    decay_start: Starts the learning rate decay at decay_start-th step.
    decay_end: Ends the learning rate decay at decay_end-th step.
    min_ratio: After decay_end, the multiplier stays at min.
    max: The schedule is never larger than this value.
  """
  warmup_steps: int = 0
  decay_start: int = 0
  decay_end: int = 0
  min_ratio: float = 0.01
  max: float = 0.0
  _schedules: Any = dataclasses.field(init=False, repr=False)
  _boundaries: Any = dataclasses.field(init=False, repr=False)

  def __post_init__(self):
    super().__post_init__()

    p = self.hparams

    assert p.decay_start >= p.warmup_steps, (
        'decay_start must greater than warmup_steps.')
    assert p.decay_end >= p.decay_start, (
        'decay_end must be greater than decay_start')
    assert p.max > 0, 'Must set max.'

    # Offset the boundaries, since each schedule passed to
    # optax.join_schedules() will receive a step step indicating the number
    # of steps since the previous boundary transition.
    self._schedules = []
    self._boundaries = []
    if p.warmup_steps > 0:
      self._schedules.append(
          instantiate(
              Linear.HParams(start=(0, 0.0), limit=(p.warmup_steps, p.max))))
      self._boundaries.append(p.warmup_steps)
    if p.decay_start > p.warmup_steps:
      self._schedules.append(
          instantiate(
              Linear.HParams(
                  start=(0, p.max),
                  limit=(p.decay_start - p.warmup_steps, p.max))))
      self._boundaries.append(p.decay_start)
    self._schedules.append(
        instantiate(
            Exponential.HParams(
                start=(0, p.max),
                limit=(p.decay_end - p.decay_start, p.max * p.min_ratio))))

  def value_at(self, step: JTensor) -> JTensor:
    return jnp.array(
        optax.join_schedules(
            [s.value_at for s in self._schedules], self._boundaries
        )(step),
        jnp.float32,
    )


class LinearRampupPiecewiseConstant(BaseSchedule):
  """A learning rate schedule that does the following.

  1. The multiplier ramps up linearly from 0 to the peak(lrs[0]) at
     boundaries[0].
  2. After peak, the multiplier stays values[i] when step falls into
     [boundaries[i], boundaries[i+1]).
  3. When step is more than boundaries[-1], then the multiplier is values[-1].

  Attributes:
    boundaries: Boundaries at which learning rate changes.
    values: The learning rate values for the PiecewiseConstant schedule and if
      the step is between boundaries[i] and boundaries[i + 1] then values[i] is
      returned, except when it is linearly ramping up from to values[0].
  """
  boundaries: Optional[Sequence[int]] = None
  values: Optional[Sequence[float]] = None
  p0: Any = dataclasses.field(init=False, repr=False)
  p1: Any = dataclasses.field(init=False, repr=False)

  def __post_init__(self):
    super().__post_init__()
    p = self.hparams
    assert len(p.boundaries) >= 1 and len(p.boundaries) == len(p.values)
    self.p0 = instantiate(
        Linear.HParams(start=(0, 0.0), limit=(p.boundaries[0], p.values[0])))
    # Offset the boundaries, since each schedule passed to
    # optax.join_schedules() will receive a step count indicating the number
    # of steps since the previous boundary transition.
    boundaries_pc = [b - p.boundaries[0] for b in p.boundaries[1:]]
    self.p1 = instantiate(
        PiecewiseConstant.HParams(boundaries=boundaries_pc, values=p.values))

  def value_at(self, step: JTensor) -> JTensor:
    p = self.hparams
    return jnp.array(
        optax.join_schedules(
            [self.p0.value_at, self.p1.value_at], p.boundaries[:1]
        )(step),
        jnp.float32,
    )


class PiecewiseSchedule(BaseSchedule):
  """Piecewise schedule composed of sub-schedules.

  Attributes:
    boundaries: Boundaries between subschedules.
    schedules: A list of sub-schedules. The length must be len(boundaries) + 1.
      schedules[i] starts at boundaries[i-1] (inclusive) and ends at
      boundaries[i] (exclusive). The *relative* step in each interval will be
      passed to the sub-schedule for Value.
  """
  boundaries: Optional[Sequence[int]] = None
  schedules: Optional[Sequence[pax_fiddle.Config[BaseSchedule]]] = None
  _schedules_inst: Any = dataclasses.field(init=False, repr=False)

  def __post_init__(self):
    super().__post_init__()
    p = self.hparams
    prev_boundary = 0
    for boundary in p.boundaries:
      if boundary < prev_boundary:
        raise ValueError('Invalid boundary %s < %s' % (boundary, prev_boundary))
      prev_boundary = boundary
    if len(p.schedules) != len(p.boundaries) + 1:
      raise ValueError('len(schedules) != len(boundaries) + 1: %s vs %s' %
                       (len(p.schedules), len(p.boundaries)))
    self._schedules_inst = [instantiate(s) for s in p.schedules]

  def value_at(self, step: JTensor) -> JTensor:
    p = self.hparams
    return jnp.array(
        optax.join_schedules(
            [s.value_at for s in self._schedules_inst], p.boundaries
        )(step),
        jnp.float32,
    )


class CycleSchedule(BaseSchedule):
  """Piecewise schedule composed of sub-schedules in a cycle.

  Attributes:
    schedules: A list of sub-schedules. Unlike PiecewiseSchedule, the absolute
      step is passed to the sub-schedule.
    steps: The number of steps to run each sub-schedule.
  """
  schedules: Optional[Sequence[pax_fiddle.Config[BaseSchedule]]] = None
  steps: Optional[Sequence[int]] = None
  _schedules_inst: Any = dataclasses.field(init=False, repr=False)
  _period: Any = dataclasses.field(init=False, repr=False)
  _boundaries: Any = dataclasses.field(init=False, repr=False)

  def __post_init__(self):
    super().__post_init__()
    p = self.hparams
    if len(p.schedules) != len(p.steps):
      raise ValueError('len(schedules) != len(steps): %s vs %s' %
                       (len(p.schedules), len(p.steps)))
    self._schedules_inst = [instantiate(s) for s in p.schedules]
    boundaries = [0]
    for step in p.steps:
      boundaries.append(boundaries[-1] + step)
    self._period = boundaries[-1]
    self._boundaries = boundaries[1:-1]

  def value_at(self, step: JTensor) -> JTensor:
    relative_step = jnp.mod(step, self._period)
    output = self._schedules_inst[0].value_at(step)
    for boundary, schedule in zip(self._boundaries, self._schedules_inst[1:]):
      output = jnp.where(
          relative_step < boundary, output, schedule.value_at(step)
      )
    return output


class ContinuousSchedule(BaseSchedule):
  """Continuous learning rate decay.

  Attributes:
    initial_value: Initial decay value.
    start_step: Starts to decay the learning rate from this step.
    half_life_steps: Halve the learning rate every this many steps after
      start_step.
    min: Minimum relative learning rate.
  """
  initial_value: float = 1.0
  start_step: int = 400_000
  half_life_steps: int = 100_000
  min: float = 0.01
  exp: Exponential = dataclasses.field(init=False, repr=False)

  def __post_init__(self):
    super().__post_init__()
    p: self.HParams = self.hparams
    limit = p.start_step + p.half_life_steps * math.log(p.min) / math.log(0.5)
    self.exp: Exponential = instantiate(
        Exponential.HParams(start=(p.start_step, 1.0), limit=(limit, p.min))
    )

  def value_at(self, step: JTensor) -> JTensor:
    return self.hparams.initial_value * self.exp.value_at(step)
