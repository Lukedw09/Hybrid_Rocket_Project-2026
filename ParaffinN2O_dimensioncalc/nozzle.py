"""
Frozen-equilibrium nozzle analysis for the hybrid motor design point.

================================================================================
PURPOSE
================================================================================
Given chamber pressure P_c, mixture ratio (O/F, for reporting / design context),
average mass flow, and average thrust, size a nozzle that is *optimally expanded
at sea level* (exit pressure P_e = ambient P_a = 1 atm) under frozen flow with
a constant specific-heat ratio gamma.

Then back-calculate the theoretical characteristic velocity:

    c* = P_c * A_t / m_dot

and report:

    I_sp,sea-level  = c* * C_F,sl / g0
    I_sp,chamber    = c* * C_F,chamber / g0

where "chamber" Isp uses the same nozzle geometry but with ambient pressure
removed (P_a = 0), i.e. the vacuum / no-backpressure thrust coefficient. That
is the usual academic pairing with sea-level Isp for a fixed expansion ratio.

================================================================================
ASSUMPTIONS (frozen equilibrium)
================================================================================
- Constant gamma = 1.25 (user-specified; composition does not shift in the nozzle).
- Isentropic, one-dimensional, ideal-gas expansion from chamber to exit.
- Design exit pressure equals sea-level ambient: P_e = P_a = 101325 Pa.
- Throat is sonic (choked). Average thrust and average m_dot define the design
  point ("on average" in the problem statement).

Mixture ratio does not enter the gamma=const formulas directly; it is carried
so the report shows which O/F the design point corresponds to.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# Standard gravity [m/s^2] — duplicated here to avoid a circular import with model.py
G0 = 9.80665

# Frozen specific-heat ratio (constant through the nozzle).
GAMMA_FROZEN = 1.25

# Sea-level ambient / design exit pressure.
P_ATM_PA = 101325.0  # 1 atm [Pa]


@dataclass
class NozzleAnalysis:
    """
    Results of the frozen nozzle design at the motor average operating point.

    of_ratio           : Design oxidizer/fuel mass ratio used for this point [-]
    gamma              : Frozen specific-heat ratio [-]
    chamber_pressure_pa: Design chamber pressure P_c [Pa]
    exit_pressure_pa   : Design exit pressure P_e (= 1 atm) [Pa]
    ambient_pressure_pa: Sea-level ambient P_a (= 1 atm) [Pa]
    exit_mach          : Exit Mach number M_e [-]
    expansion_ratio    : A_e / A_t [-]
    throat_area_m2     : Throat area A_t [m^2]
    throat_diameter_m  : Circular throat diameter [m]
    exit_area_m2       : Exit area A_e [m^2]
    exit_diameter_m    : Circular exit diameter [m]
    cf_sea_level       : Thrust coefficient at P_a = 1 atm [-]
    cf_chamber         : Thrust coefficient with P_a = 0 (vacuum / "chamber") [-]
    c_star_m_s         : Characteristic velocity c* = P_c A_t / m_dot [m/s]
    isp_sea_level_s    : Sea-level specific impulse [s]
    isp_chamber_s      : Chamber/vacuum specific impulse [s]
    thrust_avg_n       : Design average thrust F_avg = I_total / t_burn [N]
    m_dot_avg_kg_s     : Design average propellant flow [kg/s]
    """

    of_ratio: float
    gamma: float
    chamber_pressure_pa: float
    exit_pressure_pa: float
    ambient_pressure_pa: float
    exit_mach: float
    expansion_ratio: float
    throat_area_m2: float
    throat_diameter_m: float
    exit_area_m2: float
    exit_diameter_m: float
    cf_sea_level: float
    cf_chamber: float
    c_star_m_s: float
    isp_sea_level_s: float
    isp_chamber_s: float
    thrust_avg_n: float
    m_dot_avg_kg_s: float


def exit_mach_from_pressure_ratio(pc_pa: float, pe_pa: float, gamma: float = GAMMA_FROZEN) -> float:
    """
    Isentropic relation inverted for exit Mach number:

        P_c / P_e = (1 + (gamma-1)/2 * M_e^2) ** (gamma / (gamma-1))

    =>  M_e^2 = 2/(gamma-1) * [ (P_c/P_e)^((gamma-1)/gamma) - 1 ]
    """
    if pe_pa <= 0 or pc_pa <= pe_pa:
        raise ValueError("Need P_c > P_e > 0 for a supersonic nozzle design.")
    pr = pc_pa / pe_pa
    gm1 = gamma - 1.0
    me2 = (2.0 / gm1) * (pr ** (gm1 / gamma) - 1.0)
    if me2 <= 0:
        raise ValueError("Pressure ratio too small for supersonic exit Mach.")
    return float(np.sqrt(me2))


def area_ratio_from_mach(mach: float, gamma: float = GAMMA_FROZEN) -> float:
    """
    Isentropic area-Mach relation (A / A* = A_e / A_t for exit Mach):

        A/A* = (1/M) * [ (1 + (g-1)/2 M^2) / ((g+1)/2) ] ** ((g+1)/(2(g-1)))
    """
    if mach <= 0:
        raise ValueError("Mach number must be > 0")
    g = gamma
    term = (1.0 + 0.5 * (g - 1.0) * mach**2) / (0.5 * (g + 1.0))
    return float((1.0 / mach) * term ** ((g + 1.0) / (2.0 * (g - 1.0))))


def thrust_coefficient(
    pe_over_pc: float,
    expansion_ratio: float,
    pa_over_pc: float,
    gamma: float = GAMMA_FROZEN,
) -> float:
    """
    Ideal thrust coefficient:

        C_F = sqrt{
                (2 g^2 /(g-1)) * (2/(g+1))^((g+1)/(g-1)) * (1 - (Pe/Pc)^((g-1)/g))
              }
              + (Pe - Pa)/Pc * (Ae/At)

    The first term is the momentum thrust; the second is pressure thrust.
    For optimum sea-level design Pe = Pa, so the pressure term is zero.
    For "chamber" / vacuum performance of the *same* nozzle, set Pa = 0.
    """
    g = gamma
    # Prefactor under the square root (standard ideal-rocket identity).
    inside = (
        (2.0 * g**2 / (g - 1.0))
        * (2.0 / (g + 1.0)) ** ((g + 1.0) / (g - 1.0))
        * (1.0 - pe_over_pc ** ((g - 1.0) / g))
    )
    if inside < 0:
        raise ValueError("Invalid pressure ratio for thrust coefficient.")
    cf_mom = np.sqrt(inside)
    cf_pressure = (pe_over_pc - pa_over_pc) * expansion_ratio
    return float(cf_mom + cf_pressure)


def analyze_nozzle(
    of_ratio: float,
    chamber_pressure_pa: float,
    m_dot_avg_kg_s: float,
    thrust_avg_n: float,
    gamma: float = GAMMA_FROZEN,
    exit_pressure_pa: float = P_ATM_PA,
    ambient_pressure_pa: float = P_ATM_PA,
) -> NozzleAnalysis:
    """
    Full design-point nozzle analysis.

    Procedure
    ---------
    1. Fix P_e = P_a = 1 atm (optimum expansion at sea level "on average").
    2. From P_c / P_e and frozen gamma, get M_e and expansion ratio epsilon.
    3. Compute C_F,sea-level (Pe = Pa) and C_F,chamber (Pa = 0, same epsilon).
    4. Size throat from average thrust:
           F_avg = C_F,sl * P_c * A_t
           A_t   = F_avg / (C_F,sl * P_c)
    5. Theoretical c* from continuity at the design point:
           c* = P_c * A_t / m_dot_avg
    6. Specific impulses:
           I_sp,sl      = c* * C_F,sl / g0
           I_sp,chamber = c* * C_F,chamber / g0
    """
    if chamber_pressure_pa <= exit_pressure_pa:
        raise ValueError(
            f"Chamber pressure ({chamber_pressure_pa/1e5:.2f} bar) must exceed "
            f"exit/ambient pressure ({exit_pressure_pa/1e5:.2f} bar)."
        )
    if m_dot_avg_kg_s <= 0 or thrust_avg_n <= 0:
        raise ValueError("m_dot_avg and thrust_avg must be > 0")
    if of_ratio <= 0:
        raise ValueError("of_ratio must be > 0")

    # --- Isentropic exit state (frozen gamma) ---
    me = exit_mach_from_pressure_ratio(chamber_pressure_pa, exit_pressure_pa, gamma)
    eps = area_ratio_from_mach(me, gamma)

    pe_over_pc = exit_pressure_pa / chamber_pressure_pa
    pa_over_pc_sl = ambient_pressure_pa / chamber_pressure_pa

    # Sea level: design ambient. Chamber/vacuum: no back pressure.
    cf_sl = thrust_coefficient(pe_over_pc, eps, pa_over_pc_sl, gamma)
    cf_ch = thrust_coefficient(pe_over_pc, eps, 0.0, gamma)

    # --- Throat from average thrust at sea-level C_F ---
    # F = C_F * P_c * A_t  =>  A_t = F / (C_F * P_c)
    throat_area = thrust_avg_n / (cf_sl * chamber_pressure_pa)
    throat_diameter = float(np.sqrt(4.0 * throat_area / np.pi))
    exit_area = eps * throat_area
    exit_diameter = float(np.sqrt(4.0 * exit_area / np.pi))

    # --- c* from definition / continuity (NOT a user input) ---
    c_star = chamber_pressure_pa * throat_area / m_dot_avg_kg_s

    isp_sl = c_star * cf_sl / G0
    isp_ch = c_star * cf_ch / G0

    return NozzleAnalysis(
        of_ratio=float(of_ratio),
        gamma=float(gamma),
        chamber_pressure_pa=float(chamber_pressure_pa),
        exit_pressure_pa=float(exit_pressure_pa),
        ambient_pressure_pa=float(ambient_pressure_pa),
        exit_mach=float(me),
        expansion_ratio=float(eps),
        throat_area_m2=float(throat_area),
        throat_diameter_m=float(throat_diameter),
        exit_area_m2=float(exit_area),
        exit_diameter_m=float(exit_diameter),
        cf_sea_level=float(cf_sl),
        cf_chamber=float(cf_ch),
        c_star_m_s=float(c_star),
        isp_sea_level_s=float(isp_sl),
        isp_chamber_s=float(isp_ch),
        thrust_avg_n=float(thrust_avg_n),
        m_dot_avg_kg_s=float(m_dot_avg_kg_s),
    )
