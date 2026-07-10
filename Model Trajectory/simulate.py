"""
Full boost + coast trajectory integration.

================================================================================
WHAT THIS MODULE DOES
================================================================================
simulate(inputs) is the high-level entry point for the physics:

  1. Load MotorData (or accept one already loaded by the GUI).
  2. Start at the origin, at rest, with the prescribed attitude at t = 0.
  3. March fixed-step RK4 (dynamics.rk4_step) until the rocket has left the
     pad and then returned to y ≤ 0 (impact). No parachute — ballistic fall.
  4. Record time histories and summary metrics into TrajectoryResult.

The animation layer (animate.py) only *reads* TrajectoryResult; it does not
recompute forces.

================================================================================
BOOST VS COAST
================================================================================
A sample is "thrusting" when remaining propellant > 0 *and* t is still inside
the motor burn table. The animation draws that segment red; after burnout the
path is green.

================================================================================
OUTPUTS OF INTEREST
================================================================================
  max_altitude_m, max_mach, boost_time_s, apogee_index, impact_time_s
  plus per-sample altitude_m[] and mach[] aligned with position_m[] for the HUD.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from atmosphere import mach_number, speed_of_sound
from dynamics import (
    VehicleParams,
    attitude_angles,
    body_axis,
    pack_state,
    rk4_step,
    thrust_at_altitude,
    tip_angle_from_vertical,
    unpack_state,
)
from motor_import import MotorData, load_motor


# =============================================================================
# Input / output containers
# =============================================================================


@dataclass
class SimInputs:
    """
    User-facing simulation inputs (SI).

    The GUI converts mm → m before building this. altitude_goal_m and mach_goal
    are comparison targets only — they do not change the physics.
    """

    diameter_m: float
    length_m: float
    mass_dry_kg: float
    mass_propellant_kg: float
    cd: float
    altitude_goal_m: float = 0.0
    mach_goal: float = 0.0
    motor_folder: str = "motorsim_output"
    dt_s: float = 0.01


@dataclass
class TrajectoryResult:
    """
    Time histories and summary metrics from one flight.

    Array lengths all match time_s. position_m[i] is (x, y, z) at time_s[i]
    with y vertical. thrusting[i] is True during boost (red path segment).
    """

    time_s: np.ndarray
    position_m: np.ndarray  # (N, 3) x, y, z
    velocity_m_s: np.ndarray  # (N, 3)
    attitude_rad: np.ndarray  # (N, 3) phi, theta, psi
    mass_prop_kg: np.ndarray
    mass_total_kg: np.ndarray
    thrust_n: np.ndarray
    altitude_m: np.ndarray
    mach: np.ndarray
    thrusting: np.ndarray  # bool
    # Summary scalars
    max_altitude_m: float
    max_mach: float
    boost_time_s: float
    apogee_index: int
    impact_time_s: float
    altitude_goal_m: float
    mach_goal: float
    vehicle: VehicleParams
    motor: MotorData

    @property
    def apogee_position_m(self) -> np.ndarray:
        """World-frame (x,y,z) at maximum altitude — used for the apogee marker."""
        return self.position_m[self.apogee_index]


# =============================================================================
# Integrator
# =============================================================================


def simulate(inputs: SimInputs, motor: MotorData | None = None) -> TrajectoryResult:
    """
    Integrate boost + coast from y = 0 until ground impact.

    Parameters
    ----------
    inputs :
        Vehicle geometry, masses, Cd, goals, motor folder, time step.
    motor :
        Optional pre-loaded MotorData. If None, loads from inputs.motor_folder
        (requires burn_history.csv + motor_export.json).

    Returns
    -------
    TrajectoryResult
        Full time history plus max altitude / Mach / boost time / apogee index.
    """
    if motor is None:
        motor = load_motor(inputs.motor_folder)

    vehicle = VehicleParams(
        diameter_m=inputs.diameter_m,
        length_m=inputs.length_m,
        mass_dry_kg=inputs.mass_dry_kg,
        mass_propellant_kg=inputs.mass_propellant_kg,
        cd=inputs.cd,
    )

    dt = float(inputs.dt_s)
    if dt <= 0.0:
        raise ValueError("dt_s must be > 0")

    # Initial state: on the pad, at rest, attitude from the hold law at t = 0
    phi0, theta0, psi0 = attitude_angles(0.0)
    state = pack_state(
        np.array([0.0, 0.0, 0.0]),
        np.array([0.0, 0.0, 0.0]),
        np.array([phi0, theta0, psi0]),
    )
    m_prop = float(max(inputs.mass_propellant_kg, 0.0))

    # Grow Python lists during the loop, then convert to NumPy once at the end
    # (cheaper than resizing arrays every step for unknown flight duration).
    times: list[float] = [0.0]
    positions: list[np.ndarray] = [state[0:3].copy()]
    velocities: list[np.ndarray] = [state[3:6].copy()]
    attitudes: list[np.ndarray] = [state[6:9].copy()]
    props: list[float] = [m_prop]
    thrusts: list[float] = [0.0]
    alts: list[float] = [0.0]
    machs: list[float] = [0.0]
    thrusting_flags: list[bool] = [False]

    t = 0.0
    left_pad = False
    max_steps = int(1e6)  # safety cap (~2.7 h at dt = 0.01 s)
    boost_time = 0.0

    for _ in range(max_steps):
        thrusting_now = m_prop > 1e-9 and t <= motor.burn_time_s + 1e-12
        if thrusting_now:
            boost_time = t + dt

        state, m_prop = rk4_step(t, state, m_prop, dt, vehicle, motor)
        t += dt

        pos, vel, att = unpack_state(state)
        # Re-assert attitude law (rk4_step already snaps; this keeps lists honest)
        phi, theta, psi = attitude_angles(t)
        state[6:9] = (phi, theta, psi)
        att = state[6:9]

        alt = float(pos[1])
        speed = float(np.linalg.norm(vel))
        a_sound = speed_of_sound(max(alt, 0.0))
        mach = speed / a_sound if a_sound > 0.0 else 0.0

        still_thrusting = m_prop > 1e-9 and t <= motor.burn_time_s + 1e-12
        if still_thrusting:
            f_sl = motor.thrust_sl(t)
            thrust_mag = thrust_at_altitude(f_sl, max(alt, 0.0), motor.exit_area_m2)
            boost_time = t
        else:
            thrust_mag = 0.0

        times.append(t)
        positions.append(pos.copy())
        velocities.append(vel.copy())
        attitudes.append(att.copy())
        props.append(m_prop)
        thrusts.append(thrust_mag)
        alts.append(alt)
        machs.append(mach)
        thrusting_flags.append(still_thrusting)

        # Impact detection: must climb off the pad first, then hit y ≤ 0
        if alt > 1.0:
            left_pad = True
        if left_pad and alt <= 0.0:
            break
    else:
        # for-else: loop finished without break → something went wrong
        raise RuntimeError("Trajectory integration exceeded max steps without impact.")

    # --- Pack arrays and compute summary metrics ---
    time_arr = np.asarray(times, dtype=float)
    pos_arr = np.vstack(positions)
    vel_arr = np.vstack(velocities)
    att_arr = np.vstack(attitudes)
    prop_arr = np.asarray(props, dtype=float)
    thrust_arr = np.asarray(thrusts, dtype=float)
    alt_arr = np.asarray(alts, dtype=float)
    mach_arr = np.asarray(machs, dtype=float)
    thrust_flag = np.asarray(thrusting_flags, dtype=bool)

    apogee_index = int(np.argmax(alt_arr))
    max_alt = float(alt_arr[apogee_index])
    max_mach = float(np.max(mach_arr)) if len(mach_arr) else 0.0

    # Last sample where the engine was still thrusting
    if np.any(thrust_flag):
        boost_time = float(time_arr[thrust_flag][-1])
    else:
        boost_time = 0.0

    return TrajectoryResult(
        time_s=time_arr,
        position_m=pos_arr,
        velocity_m_s=vel_arr,
        attitude_rad=att_arr,
        mass_prop_kg=prop_arr,
        mass_total_kg=vehicle.mass_dry_kg + prop_arr,
        thrust_n=thrust_arr,
        altitude_m=alt_arr,
        mach=mach_arr,
        thrusting=thrust_flag,
        max_altitude_m=max_alt,
        max_mach=max_mach,
        boost_time_s=boost_time,
        apogee_index=apogee_index,
        impact_time_s=float(time_arr[-1]),
        altitude_goal_m=float(inputs.altitude_goal_m),
        mach_goal=float(inputs.mach_goal),
        vehicle=vehicle,
        motor=motor,
    )


# Re-exports used by animation / HUD / callers that import from simulate
__all__ = [
    "SimInputs",
    "TrajectoryResult",
    "simulate",
    "load_motor",
    "VehicleParams",
    "body_axis",
    "tip_angle_from_vertical",
    "mach_number",
]
