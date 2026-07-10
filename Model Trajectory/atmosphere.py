"""
1976 International Standard Atmosphere (ISA) — piecewise troposphere / stratosphere.

Returns pressure, temperature, density, and speed of sound vs geometric altitude.
Sufficient for sounding-rocket altitudes (implemented through 32 km).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# Sea-level / layer constants (1976 ISA)
G0 = 9.80665  # m/s^2
R_AIR = 287.05287  # J/(kg·K) specific gas constant for dry air
GAMMA_AIR = 1.4
P_SL = 101325.0  # Pa
T_SL = 288.15  # K
RHO_SL = P_SL / (R_AIR * T_SL)

# Layer bases: [h_base_m, T_base_K, P_base_Pa, lapse_K_per_m]
# Lapse L = dT/dh; isothermal layers use L = 0.
_LAYERS: tuple[tuple[float, float, float, float], ...] = (
    (0.0, 288.15, 101325.0, -0.0065),  # troposphere → 11 km
    (11000.0, 216.65, 22632.06, 0.0),  # lower stratosphere → 20 km
    (20000.0, 216.65, 5474.89, 0.001),  # upper stratosphere → 32 km
    (32000.0, 228.65, 868.02, 0.0028),  # → 47 km (cap for extrapolation guard)
)


@dataclass(frozen=True)
class AtmosState:
    """Atmospheric state at one altitude."""

    altitude_m: float
    temperature_k: float
    pressure_pa: float
    density_kg_m3: float
    speed_of_sound_m_s: float


def _layer_pressure(t: float, t_base: float, p_base: float, lapse: float, dh: float) -> float:
    """Barometric formula within one ISA layer."""
    if abs(lapse) < 1e-12:
        return float(p_base * np.exp(-G0 * dh / (R_AIR * t_base)))
    exponent = -G0 / (R_AIR * lapse)
    return float(p_base * (t / t_base) ** exponent)


def isa(altitude_m: float | np.ndarray) -> AtmosState | tuple[np.ndarray, ...]:
    """
    Evaluate 1976 ISA at geometric altitude h (m above MSL / launch pad ≈ sea level).

    Negative altitudes clamp to sea level. Above the top tabulated layer the last
    lapse rate is continued (adequate for this simulator's coast altitudes).

    Scalar input → AtmosState. Array input → (T, P, rho, a) arrays.
    """
    h_arr = np.asarray(altitude_m, dtype=float)
    scalar = h_arr.ndim == 0
    h = np.atleast_1d(np.maximum(h_arr, 0.0))

    t = np.empty_like(h)
    p = np.empty_like(h)

    for i, hi in enumerate(h):
        # Walk layers; continue last lapse above 32 km.
        t_val = T_SL
        p_val = P_SL
        for j, (h0, t0, p0, lapse) in enumerate(_LAYERS):
            h1 = _LAYERS[j + 1][0] if j + 1 < len(_LAYERS) else None
            if h1 is not None and hi > h1:
                continue
            dh = hi - h0
            t_val = t0 + lapse * dh
            p_val = _layer_pressure(t_val, t0, p0, lapse, dh)
            break
        else:
            # Above final base: extend last layer.
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
