"""
9-state rigid-body flight dynamics for near-vertical hybrid rocket flight.

State vector (y-up, launch at origin):
  [x, y, z, vx, vy, vz, phi, theta, psi]

Attitude is constrained (no gimbal): tip from +y held within ±2% of 90°
(≈ ±1.8°) via deterministic pitch/yaw sinusoids. Thrust along body +nose.
Mass propellant is tracked alongside the 9-state for depletion.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from atmosphere import P_SL, G0, density, pressure
from motor_import import MotorData

# Tip-angle hold: ±2% of 90° → 1.8° from vertical
TIP_MAX_RAD = np.deg2rad(0.02 * 90.0)  # ≈ 1.8°
# Split budget across pitch & yaw so combined tip ≤ TIP_MAX
_ATT_AMP = TIP_MAX_RAD / np.sqrt(2.0)
_OMEGA_THETA = 0.35  # rad/s — slow wander
_OMEGA_PSI = 0.27
_PSI_PHASE = 1.1


@dataclass(frozen=True)
class VehicleParams:
    """Vehicle / aero parameters for the force model."""

    diameter_m: float
    length_m: float
    mass_dry_kg: float
    mass_propellant_kg: float
    cd: float

    @property
    def area_m2(self) -> float:
        """Reference cross-section A = π D²/4."""
        return float(np.pi * self.diameter_m**2 / 4.0)


def attitude_angles(t: float) -> tuple[float, float, float]:
    """
    Prescribed Euler attitude (φ, θ, ψ) [rad] at time t.

    θ, ψ are small tip angles from vertical; φ = 0 (no roll).
    Combined tip from +y stays within ≈ ±1.8°.
    """
    theta = _ATT_AMP * np.sin(_OMEGA_THETA * t)
    psi = _ATT_AMP * np.sin(_OMEGA_PSI * t + _PSI_PHASE)
    phi = 0.0
    return float(phi), float(theta), float(psi)


def attitude_rates(t: float) -> tuple[float, float, float]:
    """Time derivatives of prescribed Euler angles [rad/s]."""
    dtheta = _ATT_AMP * _OMEGA_THETA * np.cos(_OMEGA_THETA * t)
    dpsi = _ATT_AMP * _OMEGA_PSI * np.cos(_OMEGA_PSI * t + _PSI_PHASE)
    return 0.0, float(dtheta), float(dpsi)


def body_axis(phi: float, theta: float, psi: float) -> np.ndarray:
    """
    Unit vector along body longitudinal (+nose) in world frame.

    Vertical reference is +y. Small θ (about world x) and ψ (about world z)
    tip the nose off vertical; φ unused (axisymmetric for thrust).
    """
    _ = phi
    # Apply yaw-about-z then pitch-about-x to (0, 1, 0):
    #   x = sin(ψ) cos(θ)
    #   y = cos(ψ) cos(θ)
    #   z = sin(θ)
    ct, st = np.cos(theta), np.sin(theta)
    cp, sp = np.cos(psi), np.sin(psi)
    axis = np.array([sp * ct, cp * ct, st], dtype=float)
    n = np.linalg.norm(axis)
    if n < 1e-15:
        return np.array([0.0, 1.0, 0.0])
    return axis / n


def tip_angle_from_vertical(phi: float, theta: float, psi: float) -> float:
    """Angle [rad] between body +nose and world +y."""
    axis = body_axis(phi, theta, psi)
    c = float(np.clip(axis[1], -1.0, 1.0))
    return float(np.arccos(c))


def thrust_at_altitude(f_sl: float, altitude_m: float, exit_area_m2: float) -> float:
    """
    Altitude-corrected thrust:
      F(h) = F_sl + (P_a,sl − P_a(h)) · A_e
    """
    if f_sl <= 0.0 or exit_area_m2 <= 0.0:
        return max(f_sl, 0.0)
    p_amb = pressure(altitude_m)
    return float(f_sl + (P_SL - p_amb) * exit_area_m2)


def drag_force(velocity: np.ndarray, rho: float, cd: float, area: float) -> np.ndarray:
    """Drag D = ½ ρ V² Cd A opposite velocity. Zero at rest."""
    speed = float(np.linalg.norm(velocity))
    if speed < 1e-9 or rho <= 0.0 or cd <= 0.0 or area <= 0.0:
        return np.zeros(3)
    return -0.5 * rho * speed * cd * area * velocity  # (½ρV²CdA) * (−V̂) = −½ρV CdA V


def unpack_state(state: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Split 9-vector into position, velocity, Euler angles."""
    pos = state[0:3]
    vel = state[3:6]
    att = state[6:9]
    return pos, vel, att


def pack_state(pos: np.ndarray, vel: np.ndarray, att: np.ndarray) -> np.ndarray:
    """Assemble 9-vector from position, velocity, Euler angles."""
    out = np.empty(9, dtype=float)
    out[0:3] = pos
    out[3:6] = vel
    out[6:9] = att
    return out


def derivatives(
    t: float,
    state: np.ndarray,
    m_prop: float,
    vehicle: VehicleParams,
    motor: MotorData,
) -> tuple[np.ndarray, float]:
    """
    State derivative d(state)/dt and dm_prop/dt.

    Boost while m_prop > 0 and motor history still supplies thrust/m_dot;
    otherwise coast (thrust = 0, m_dot = 0).
    """
    pos, vel, _att = unpack_state(state)
    altitude = float(pos[1])
    rho = density(max(altitude, 0.0))

    # Prescribed attitude (overwrite integrated angles' rates from law)
    phi, theta, psi = attitude_angles(t)
    dphi, dtheta, dpsi = attitude_rates(t)
    axis = body_axis(phi, theta, psi)

    thrusting = m_prop > 1e-9 and t <= motor.burn_time_s + 1e-12
    if thrusting:
        f_sl = motor.thrust_sl(t)
        m_dot = motor.m_dot(t)
        # Don't consume more propellant than remains this step conceptually;
        # continuous derivative uses full m_dot; integrator clamps mass.
        thrust_mag = thrust_at_altitude(f_sl, max(altitude, 0.0), motor.exit_area_m2)
        if m_dot < 0.0:
            m_dot = 0.0
    else:
        thrust_mag = 0.0
        m_dot = 0.0

    mass = vehicle.mass_dry_kg + max(m_prop, 0.0)
    if mass < 1e-9:
        mass = 1e-9

    f_thrust = thrust_mag * axis
    f_drag = drag_force(vel, rho, vehicle.cd, vehicle.area_m2)
    f_grav = np.array([0.0, -mass * G0, 0.0])
    accel = (f_thrust + f_drag + f_grav) / mass

    dstate = np.empty(9, dtype=float)
    dstate[0:3] = vel
    dstate[3:6] = accel
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
    Fixed-step RK4 for the 9-state + propellant mass.

    After the step, Euler angles are snapped to the prescribed attitude law
    (keeps tip-hold exact despite numerical drift). Propellant is clamped ≥ 0.
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

    # Snap attitude to prescribed hold at t+dt
    phi, theta, psi = attitude_angles(t + dt)
    s1[6:9] = (phi, theta, psi)
    return s1, m1
