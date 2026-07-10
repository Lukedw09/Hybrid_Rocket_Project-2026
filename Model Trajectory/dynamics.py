"""
9-state rigid-body flight dynamics for near-vertical hybrid rocket flight.

================================================================================
WHAT THIS MODULE DOES
================================================================================
Defines the equations of motion used by simulate.py:

  State (9 numbers, y-up, launch at origin):
      [x, y, z,  vx, vy, vz,  phi, theta, psi]

  Plus a separate propellant mass m_prop that depletes with motor m_dot(t).

Each RK4 step:
  1. Look up sea-level thrust and m_dot from MotorData.
  2. Correct thrust for ambient pressure at current altitude.
  3. Apply drag opposite velocity (Cd at AoA ≈ 0).
  4. Apply constant gravity in −y.
  5. Point thrust along the body +nose axis (no gimbal).
  6. Advance position/velocity; snap attitude to the prescribed hold law.

================================================================================
"9DOF" vs 9-STATE
================================================================================
This is a *9-component state vector*, not nine independent free degrees of
freedom. Attitude is *prescribed* (actuators hold near-vertical), so the
rotational dynamics are not free 6DOF. Translation in x,y,z is free.

Tip from world +y is held within ±2% of 90° → about ±1.8°. We implement that
as small deterministic pitch/yaw sinusoids (not random noise), so the path
drifts slightly off pure vertical in a repeatable way.

================================================================================
FORCES (world frame)
================================================================================
  F_thrust = F(h,t) * body_axis(φ,θ,ψ)     # along +nose
  F_drag   = −½ ρ |V| Cd A * V             # opposite velocity
  F_grav   = (0, −m g0, 0)

  a = (F_thrust + F_drag + F_grav) / m
  m = m_dry + m_prop

Altitude thrust correction (motor tables are sea-level):
  F(h) = F_sl(t) + (P_sl − P_a(h)) * A_e

================================================================================
COORDINATES
================================================================================
  y  — vertical (up)
  x,z — horizontal ground plane
  Body +nose aligns with +y when tip angles are zero.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from atmosphere import P_SL, G0, density, pressure
from motor_import import MotorData

# Tip-angle hold: ±2% of 90° → 1.8° from vertical
TIP_MAX_RAD = np.deg2rad(0.02 * 90.0)  # ≈ 1.8°
# Split the tip budget across pitch & yaw so combined tip stays ≤ TIP_MAX
_ATT_AMP = TIP_MAX_RAD / np.sqrt(2.0)
_OMEGA_THETA = 0.35  # rad/s — slow wander frequencies
_OMEGA_PSI = 0.27
_PSI_PHASE = 1.1


# =============================================================================
# Vehicle parameters
# =============================================================================


@dataclass(frozen=True)
class VehicleParams:
    """
    Vehicle / aero parameters for the force model.

    mass_dry_kg is inert mass *excluding* propellant. Instantaneous mass is
    mass_dry_kg + remaining propellant.
    """

    diameter_m: float
    length_m: float
    mass_dry_kg: float
    mass_propellant_kg: float
    cd: float

    @property
    def area_m2(self) -> float:
        """Reference cross-section A = π D²/4 used in the drag equation."""
        return float(np.pi * self.diameter_m**2 / 4.0)


# =============================================================================
# Attitude hold (prescribed, not free dynamics)
# =============================================================================


def attitude_angles(t: float) -> tuple[float, float, float]:
    """
    Prescribed Euler attitude (φ, θ, ψ) [rad] at time t.

    θ and ψ are small tip angles from vertical; φ = 0 (no roll command).
    Combined tip from +y stays within ≈ ±1.8° by construction of _ATT_AMP.
    """
    theta = _ATT_AMP * np.sin(_OMEGA_THETA * t)
    psi = _ATT_AMP * np.sin(_OMEGA_PSI * t + _PSI_PHASE)
    phi = 0.0
    return float(phi), float(theta), float(psi)


def attitude_rates(t: float) -> tuple[float, float, float]:
    """
    Time derivatives of the prescribed Euler angles [rad/s].

    Used as d(attitude)/dt in the state derivative so RK4 stays consistent
    with the analytic hold law (we also snap angles after each step).
    """
    dtheta = _ATT_AMP * _OMEGA_THETA * np.cos(_OMEGA_THETA * t)
    dpsi = _ATT_AMP * _OMEGA_PSI * np.cos(_OMEGA_PSI * t + _PSI_PHASE)
    return 0.0, float(dtheta), float(dpsi)


def body_axis(phi: float, theta: float, psi: float) -> np.ndarray:
    """
    Unit vector along body longitudinal (+nose) in the world frame.

    Vertical reference is +y. Small θ (pitch about world x) and ψ (yaw about
    world z) tip the nose off vertical. φ is unused for the thrust axis
    (axisymmetric for this model) but kept in the signature for the 9-state.

        x = sin(ψ) cos(θ)
        y = cos(ψ) cos(θ)
        z = sin(θ)
    """
    _ = phi  # roll does not change the longitudinal axis direction here
    ct, st = np.cos(theta), np.sin(theta)
    cp, sp = np.cos(psi), np.sin(psi)
    axis = np.array([sp * ct, cp * ct, st], dtype=float)
    n = np.linalg.norm(axis)
    if n < 1e-15:
        return np.array([0.0, 1.0, 0.0])
    return axis / n


def tip_angle_from_vertical(phi: float, theta: float, psi: float) -> float:
    """Angle [rad] between body +nose and world +y (0 = perfectly vertical)."""
    axis = body_axis(phi, theta, psi)
    # axis[1] is the y-component = cos(tip); clamp for numerical safety
    c = float(np.clip(axis[1], -1.0, 1.0))
    return float(np.arccos(c))


# =============================================================================
# Forces
# =============================================================================


def thrust_at_altitude(f_sl: float, altitude_m: float, exit_area_m2: float) -> float:
    """
    Altitude-corrected thrust from a sea-level table value.

        F(h) = F_sl + (P_a,sl − P_a(h)) · A_e

    As ambient pressure falls with altitude, the pressure term grows and
    thrust increases slightly above the sea-level motor table.
    """
    if f_sl <= 0.0 or exit_area_m2 <= 0.0:
        return max(f_sl, 0.0)
    p_amb = pressure(altitude_m)
    return float(f_sl + (P_SL - p_amb) * exit_area_m2)


def drag_force(velocity: np.ndarray, rho: float, cd: float, area: float) -> np.ndarray:
    """
    Quadratic drag opposite the velocity vector.

        D_vec = −½ ρ V² Cd A * (V / |V|)
              = −½ ρ |V| Cd A * V

    Returns the zero vector when speed is negligible (avoids divide-by-zero).
    """
    speed = float(np.linalg.norm(velocity))
    if speed < 1e-9 or rho <= 0.0 or cd <= 0.0 or area <= 0.0:
        return np.zeros(3)
    return -0.5 * rho * speed * cd * area * velocity


# =============================================================================
# State packing
# =============================================================================


def unpack_state(state: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Split the 9-vector into position[3], velocity[3], Euler angles[3]."""
    pos = state[0:3]
    vel = state[3:6]
    att = state[6:9]
    return pos, vel, att


def pack_state(pos: np.ndarray, vel: np.ndarray, att: np.ndarray) -> np.ndarray:
    """Assemble a 9-vector from position, velocity, and Euler angles."""
    out = np.empty(9, dtype=float)
    out[0:3] = pos
    out[3:6] = vel
    out[6:9] = att
    return out


# =============================================================================
# Derivatives + RK4
# =============================================================================


def derivatives(
    t: float,
    state: np.ndarray,
    m_prop: float,
    vehicle: VehicleParams,
    motor: MotorData,
) -> tuple[np.ndarray, float]:
    """
    Continuous-time derivatives: d(state)/dt and dm_prop/dt.

    Boost while propellant remains *and* motor history still covers time t;
    otherwise coast (thrust = 0, m_dot = 0).

    Returns
    -------
    dstate : ndarray, shape (9,)
        [vx,vy,vz, ax,ay,az, dφ,dθ,dψ]
    dm_prop : float
        Negative of mass flow (propellant leaving the vehicle).
    """
    pos, vel, _att = unpack_state(state)
    altitude = float(pos[1])
    rho = density(max(altitude, 0.0))

    # Attitude comes from the hold law, not from integrating free rotational EOM
    phi, theta, psi = attitude_angles(t)
    dphi, dtheta, dpsi = attitude_rates(t)
    axis = body_axis(phi, theta, psi)

    thrusting = m_prop > 1e-9 and t <= motor.burn_time_s + 1e-12
    if thrusting:
        f_sl = motor.thrust_sl(t)
        m_dot = motor.m_dot(t)
        thrust_mag = thrust_at_altitude(f_sl, max(altitude, 0.0), motor.exit_area_m2)
        if m_dot < 0.0:
            m_dot = 0.0
    else:
        thrust_mag = 0.0
        m_dot = 0.0

    mass = vehicle.mass_dry_kg + max(m_prop, 0.0)
    if mass < 1e-9:
        mass = 1e-9  # numerical floor — should never hit with sane inputs

    f_thrust = thrust_mag * axis
    f_drag = drag_force(vel, rho, vehicle.cd, vehicle.area_m2)
    f_grav = np.array([0.0, -mass * G0, 0.0])
    accel = (f_thrust + f_drag + f_grav) / mass

    # Kinematic + dynamic state derivative
    dstate = np.empty(9, dtype=float)
    dstate[0:3] = vel  # dx/dt = v
    dstate[3:6] = accel  # dv/dt = a
    dstate[6:9] = (dphi, dtheta, dpsi)
    dm_prop = -m_dot
    return dstate, dm_prop


def rk4_step(
    t: float,
    state: np.ndarray,
    m_prop: float,
    dt: float,
    vehicle: VehicleParams,
    motor: MotorData,
) -> tuple[np.ndarray, float]:
    """
    One fixed-step classical RK4 update for the 9-state + propellant mass.

    Classic RK4 evaluates the derivative four times per step and blends them:

        y_{n+1} = y_n + (dt/6) * (k1 + 2 k2 + 2 k3 + k4)

    After the step we *snap* Euler angles to attitude_angles(t+dt) so the tip
    hold stays exact despite floating-point drift. Propellant is clamped ≥ 0.
    """
    s0 = np.asarray(state, dtype=float).copy()
    m0 = float(m_prop)

    k1, km1 = derivatives(t, s0, m0, vehicle, motor)
    k2, km2 = derivatives(t + 0.5 * dt, s0 + 0.5 * dt * k1, m0 + 0.5 * dt * km1, vehicle, motor)
    k3, km3 = derivatives(t + 0.5 * dt, s0 + 0.5 * dt * k2, m0 + 0.5 * dt * km2, vehicle, motor)
    k4, km4 = derivatives(t + dt, s0 + dt * k3, m0 + dt * km3, vehicle, motor)

    s1 = s0 + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
    m1 = m0 + (dt / 6.0) * (km1 + 2.0 * km2 + 2.0 * km3 + km4)
    m1 = max(m1, 0.0)

    # Snap attitude to the prescribed hold at the end of the step
    phi, theta, psi = attitude_angles(t + dt)
    s1[6:9] = (phi, theta, psi)
    return s1, m1
