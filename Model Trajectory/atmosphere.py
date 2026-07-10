"""
1976 International Standard Atmosphere (ISA).

================================================================================
WHAT THIS MODULE DOES
================================================================================
Given geometric altitude h [m] above the launch pad (treated as sea level),
return ambient temperature, pressure, density, and speed of sound.

The flight model needs these every RK4 step:
  - density ρ  → drag force
  - pressure P → altitude correction on thrust
  - speed of sound a → Mach number M = |V| / a

================================================================================
PHYSICAL MODEL
================================================================================
ISA is layered. Inside each layer temperature follows a constant lapse rate
L = dT/dh (K per meter). Pressure follows the barometric formulas:

  Isothermal (L ≈ 0):
      P = P0 * exp( -g0 * Δh / (R * T0) )

  Gradient layer (L ≠ 0):
      T = T0 + L * Δh
      P = P0 * (T / T0) ** ( -g0 / (R * L) )

Then:
  ρ = P / (R * T)
  a = sqrt(γ * R * T)     with γ = 1.4 for air

Layers implemented here cover 0 → ~47 km, which is enough for this sounding-
rocket style coast. Negative altitudes clamp to sea level.

================================================================================
API SHAPE
================================================================================
isa(h) accepts a scalar or a NumPy array:
  - scalar → AtmosState dataclass
  - array  → tuple of (T, P, rho, a) arrays

Convenience wrappers pressure / density / speed_of_sound / mach_number call
isa() for the common single-altitude case used by dynamics.py.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# ---------------------------------------------------------------------------
# Sea-level / gas constants (1976 ISA)
# ---------------------------------------------------------------------------
G0 = 9.80665  # m/s^2 — also used as constant gravity in dynamics.py
R_AIR = 287.05287  # J/(kg·K) specific gas constant for dry air
GAMMA_AIR = 1.4
P_SL = 101325.0  # Pa
T_SL = 288.15  # K
RHO_SL = P_SL / (R_AIR * T_SL)

# Each tuple: (h_base_m, T_base_K, P_base_Pa, lapse_K_per_m)
# Lapse L = dT/dh; isothermal layers use L = 0.
_LAYERS: tuple[tuple[float, float, float, float], ...] = (
    (0.0, 288.15, 101325.0, -0.0065),  # troposphere → 11 km
    (11000.0, 216.65, 22632.06, 0.0),  # lower stratosphere → 20 km
    (20000.0, 216.65, 5474.89, 0.001),  # upper stratosphere → 32 km
    (32000.0, 228.65, 868.02, 0.0028),  # → 47 km (guard for high coasts)
)


@dataclass(frozen=True)
class AtmosState:
    """Atmospheric state at one altitude (all SI)."""

    altitude_m: float
    temperature_k: float
    pressure_pa: float
    density_kg_m3: float
    speed_of_sound_m_s: float


def _layer_pressure(t: float, t_base: float, p_base: float, lapse: float, dh: float) -> float:
    """
    Barometric formula within one ISA layer.

    `t` is the temperature at the evaluation altitude; `t_base` / `p_base` are
    the values at the bottom of the layer; `dh` is height above that base.
    """
    if abs(lapse) < 1e-12:
        # Isothermal: exponential hydrostatic balance
        return float(p_base * np.exp(-G0 * dh / (R_AIR * t_base)))
    # Gradient layer: power-law form of the hydrostatic equation
    exponent = -G0 / (R_AIR * lapse)
    return float(p_base * (t / t_base) ** exponent)


def isa(altitude_m: float | np.ndarray) -> AtmosState | tuple[np.ndarray, ...]:
    """
    Evaluate 1976 ISA at geometric altitude h (m above MSL / launch pad).

    Negative altitudes clamp to sea level. Above the top tabulated layer the
    last lapse rate is continued (good enough for this simulator).

    Scalar input → AtmosState. Array input → (T, P, rho, a) arrays.
    """
    h_arr = np.asarray(altitude_m, dtype=float)
    scalar = h_arr.ndim == 0
    h = np.atleast_1d(np.maximum(h_arr, 0.0))

    t = np.empty_like(h)
    p = np.empty_like(h)

    for i, hi in enumerate(h):
        # Find the layer that contains hi, then apply that layer's formulas.
        t_val = T_SL
        p_val = P_SL
        for j, (h0, t0, p0, lapse) in enumerate(_LAYERS):
            h1 = _LAYERS[j + 1][0] if j + 1 < len(_LAYERS) else None
            # Still above this layer's top → keep walking upward
            if h1 is not None and hi > h1:
                continue
            dh = hi - h0
            t_val = t0 + lapse * dh
            p_val = _layer_pressure(t_val, t0, p0, lapse, dh)
            break
        else:
            # Above final base: extend the last layer's lapse rate
            h0, t0, p0, lapse = _LAYERS[-1]
            dh = hi - h0
            t_val = t0 + lapse * dh
            p_val = _layer_pressure(t_val, t0, p0, lapse, dh)
        t[i] = t_val
        p[i] = p_val

    rho = p / (R_AIR * t)
    a = np.sqrt(GAMMA_AIR * R_AIR * t)

    if scalar:
        return AtmosState(
            altitude_m=float(h[0]),
            temperature_k=float(t[0]),
            pressure_pa=float(p[0]),
            density_kg_m3=float(rho[0]),
            speed_of_sound_m_s=float(a[0]),
        )
    return t, p, rho, a


def pressure(altitude_m: float) -> float:
    """Ambient pressure [Pa] at altitude."""
    return isa(altitude_m).pressure_pa


def density(altitude_m: float) -> float:
    """Ambient density [kg/m³] at altitude."""
    return isa(altitude_m).density_kg_m3


def speed_of_sound(altitude_m: float) -> float:
    """Speed of sound [m/s] at altitude."""
    return isa(altitude_m).speed_of_sound_m_s


def mach_number(speed_m_s: float, altitude_m: float) -> float:
    """Mach number M = |V| / a(h)."""
    a = speed_of_sound(altitude_m)
    if a <= 0.0:
        return 0.0
    return float(abs(speed_m_s) / a)
