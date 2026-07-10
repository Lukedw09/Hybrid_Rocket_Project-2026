"""
Time-dependent 1D hybrid rocket burn model for N2O / plain paraffin.

================================================================================
WHAT THIS MODULE DOES
================================================================================
Given motor design targets (case size, fuel mass, burn time, O/F, chamber
pressure, total impulse), this module:

  1. Sizes the fuel grain (outer diameter, initial port, length).
  2. Solves for the initial port diameter so the fuel "web" burns through in
     exactly the target burn time.
  3. Reports oxidizer mass flux G_ox as an *output* (not an input).
  4. Runs a frozen-equilibrium nozzle analysis (gamma = 1.25, P_e = 1 atm)
     to size the throat, compute theoretical c*, and report chamber and
     sea-level specific impulse (see nozzle.py).
  5. Integrates a simple time-dependent burn to produce thrust, port growth,
     and regression-rate histories.

================================================================================
PHYSICAL MODEL (1D, circular port)
================================================================================
- Solid paraffin fuel grain with a single circular port down the center.
- Liquid/gaseous N2O oxidizer flows through the port at a constant mass flow
  rate m_dot_ox (set by injector / tank blowdown assumptions here).
- Fuel regresses radially outward. The regression rate depends on the local
  oxidizer mass flux:

      r_dot [mm/s] = 0.104 * G_ox ** 0.67

  where G_ox = m_dot_ox / A_port  [kg/(s·m^2)].

- As the port grows, A_port increases, so G_ox and r_dot fall over time.
- Grain length does NOT affect port growth for a given m_dot_ox; it only
  affects how much fuel mass is vaporized per second (burning surface area).

================================================================================
UNITS
================================================================================
Internal calculations use SI (meters, kilograms, seconds, pascals).
The GUI/CLI accept mm and bar for convenience and convert on the way in.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ParaffinN2O_dimensioncalc.nozzle import NozzleAnalysis, analyze_nozzle

# ---------------------------------------------------------------------------
# Empirical regression correlation (plain paraffin + N2O)
# Source: Table 3 comparison of N2O-based hybrid fuels.
# Correlation returns r_dot in mm/s when G_ox is in kg/(s·m^2).
# ---------------------------------------------------------------------------
REGRESSION_A = 0.104
REGRESSION_N = 0.67

# Default solid paraffin density used for grain volume <-> mass conversion.
PARAFFIN_DENSITY = 834.0  # kg/m^3

# Standard gravity — used when converting thrust <-> I_sp in seconds.
G0 = 9.80665  # m/s^2

# Lower bound on port diameter when searching for a burn-time match.
# Prevents division by zero / infinite G_ox in the integral.
_MIN_PORT_M = 1e-4  # 0.1 mm


# =============================================================================
# Data containers
# =============================================================================
# dataclasses generate __init__, etc. automatically. They are plain bundles of
# related numbers — no behavior beyond storing fields.


@dataclass
class MotorInputs:
    """
    Design targets supplied by the user (all SI).

    case_od_m            : Outer diameter of the motor case [m]
    wall_thickness_m     : Case wall + thermal liner thickness [m]
                           Grain OD = case_od - 2 * wall_thickness
    fuel_mass_kg         : Mass of solid paraffin to load [kg]
    burn_time_s          : Desired burn duration [s]
                           Also used to set m_dot_ox = m_ox / burn_time
    chamber_pressure_pa  : Design chamber pressure [Pa]
    of_ratio             : Oxidizer-to-fuel mass ratio m_ox / m_fuel [-]
    total_impulse_n_s    : Design total impulse I_total [N·s]
                           Sets average thrust F_avg = I_total / t_burn
                           (used to size the nozzle throat)
    dt_s                 : Integration time step for the burn simulation [s]
    fuel_density_kg_m3   : Solid fuel density [kg/m^3]

    Note: c* is NOT an input. It is computed in the nozzle analysis from
    P_c, A_t, and m_dot (see nozzle.analyze_nozzle).
    """

    case_od_m: float
    wall_thickness_m: float
    fuel_mass_kg: float
    burn_time_s: float
    chamber_pressure_pa: float
    of_ratio: float
    total_impulse_n_s: float
    dt_s: float = 0.01
    fuel_density_kg_m3: float = PARAFFIN_DENSITY


@dataclass
class MotorGeometry:
    """
    Sized grain / oxidizer quantities (outputs of size_motor).

    grain_od_m             : Fuel grain outer diameter [m]
    port_diameter_m        : Initial circular port diameter [m] (solved)
    grain_length_m         : Grain length needed to hold fuel_mass [m]
    web_thickness_m        : Radial fuel thickness = (OD - port) / 2 [m]
    m_dot_ox_kg_s          : Constant oxidizer mass flow [kg/s]
    oxidizer_mass_kg       : Total oxidizer mass for the burn [kg]
    fuel_volume_m3         : Fuel volume = m_fuel / density [m^3]
    gox_initial_kg_s_m2    : Initial oxidizer mass flux [kg/(s·m^2)] (output)
    """

    grain_od_m: float
    port_diameter_m: float
    grain_length_m: float
    web_thickness_m: float
    m_dot_ox_kg_s: float
    oxidizer_mass_kg: float
    fuel_volume_m3: float
    gox_initial_kg_s_m2: float


@dataclass
class DesignPerformance:
    """
    Propulsion figures from propellant budget + frozen nozzle analysis.

    total_propellant_kg  : m_fuel + m_ox [kg]
    m_dot_avg_kg_s       : Average total propellant flow m_prop / t_burn [kg/s]
    thrust_avg_n         : F_avg = I_total / t_burn [N]
    nozzle               : Full frozen-equilibrium nozzle result (c*, Isp, ...)

    Convenience mirrors of nozzle fields (so burn sim code stays short):
      c_star_m_s, throat_area_m2, throat_diameter_m,
      isp_sea_level_s, isp_chamber_s
    """

    total_propellant_kg: float
    m_dot_avg_kg_s: float
    thrust_avg_n: float
    nozzle: NozzleAnalysis
    c_star_m_s: float
    throat_area_m2: float
    throat_diameter_m: float
    isp_sea_level_s: float
    isp_chamber_s: float


@dataclass
class BurnHistory:
    """
    Time series from the 1D burn integration.

    Each array is the same length. Index i is the state at time_s[i].
    burnout_reason explains why the loop stopped (web burned through,
    fuel depleted, oxidizer schedule ended, etc.).
    """

    time_s: np.ndarray
    port_diameter_m: np.ndarray
    regression_rate_m_s: np.ndarray
    gox_kg_s_m2: np.ndarray
    m_dot_fuel_kg_s: np.ndarray
    m_dot_total_kg_s: np.ndarray
    of_ratio: np.ndarray
    thrust_n: np.ndarray
    chamber_pressure_pa: np.ndarray
    fuel_consumed_kg: np.ndarray
    burnout_reason: str


@dataclass
class MotorResult:
    """Complete package returned by run_motor: geometry + performance + history."""

    geometry: MotorGeometry
    performance: DesignPerformance
    history: BurnHistory


# =============================================================================
# Regression / port-growth helpers
# =============================================================================


def regression_rate_m_s(gox: float | np.ndarray) -> float | np.ndarray:
    """
    Convert oxidizer mass flux to fuel regression rate.

    Correlation:  r_dot_mm = a * G_ox^n
    We return meters/second for use in SI geometry updates.

    Accepts a scalar or a NumPy array (useful when integrating over many
    diameters at once in web_burn_time_s).
    """
    gox = np.asarray(gox, dtype=float)
    # Clamp negative fluxes (should not occur physically) so **n is safe.
    r_mm_s = REGRESSION_A * np.power(np.maximum(gox, 0.0), REGRESSION_N)
    return r_mm_s * 1e-3  # mm/s -> m/s


def _port_growth_rate_m_s(d_port_m: float | np.ndarray, m_dot_ox: float) -> float | np.ndarray:
    """
    Rate of change of port *diameter* [m/s].

    Fuel regresses on the radius at r_dot, so diameter grows at 2 * r_dot.
    G_ox is evaluated at the current port area A = pi D^2 / 4.
    """
    a_port = 0.25 * np.pi * np.asarray(d_port_m, dtype=float) ** 2
    # Tiny floor avoids divide-by-zero if D is numerically ~0.
    gox = m_dot_ox / np.maximum(a_port, 1e-18)
    return 2.0 * regression_rate_m_s(gox)


def web_burn_time_s(
    port_diameter_m: float,
    grain_od_m: float,
    m_dot_ox: float,
    n_pts: int = 4000,
) -> float:
    """
    Time required for the port to grow from D0 to the grain OD.

    We integrate:

        t = ∫_{D0}^{D_od}  dD / (dD/dt)

    where dD/dt = 2 * r_dot(G_ox(D)) and G_ox(D) = m_dot_ox / (pi D^2 / 4).

    Important: this time does *not* depend on grain length. Length scales the
    fuel mass-flow, but the radial burn-through of a circular port is only a
    function of local G_ox (hence of m_dot_ox and D).
    """
    if port_diameter_m >= grain_od_m:
        return 0.0

    # Sample diameters from initial port to outer grain diameter.
    d = np.linspace(port_diameter_m, grain_od_m, n_pts)
    dD_dt = _port_growth_rate_m_s(d, m_dot_ox)

    # Trapezoidal rule on dt = dD / (dD/dt).
    integrand = 1.0 / np.maximum(dD_dt, 1e-18)
    if hasattr(np, "trapezoid"):
        return float(np.trapezoid(integrand, d))
    # Older NumPy used the name trapz.
    return float(np.trapz(integrand, d))  # type: ignore[attr-defined]


def solve_initial_port_diameter(
    grain_od_m: float,
    m_dot_ox: float,
    burn_time_s: float,
    tol_s: float = 1e-4,
    max_iter: int = 80,
) -> float:
    """
    Invert web_burn_time_s: find D0 such that burn-through time == burn_time_s.

    Monotonicity used by the search:
      - Smaller D0  => thicker web => longer burn-through time
      - Larger D0   => thinner web => shorter burn-through time

    Algorithm: bisection on D0 between a tiny port and nearly the grain OD.
    """
    # Upper end of search: port almost as large as the grain (very thin web).
    d_hi = grain_od_m * (1.0 - 1e-6)
    # Lower end: smallest practical port.
    d_lo = min(_MIN_PORT_M, grain_od_m * 0.01)
    d_lo = max(d_lo, _MIN_PORT_M)
    if d_lo >= d_hi:
        raise ValueError("Grain OD is too small to place a circular port.")

    # Feasibility check: can this grain OD + oxidizer flow support the burn time?
    t_max = web_burn_time_s(d_lo, grain_od_m, m_dot_ox)  # thickest web
    t_min = web_burn_time_s(d_hi, grain_od_m, m_dot_ox)  # thinnest web

    if burn_time_s > t_max:
        # Even the thickest web burns out too fast (or rather: cannot last that long).
        raise ValueError(
            f"Cannot reach burn time {burn_time_s:.3f} s: maximum web burn time "
            f"with this oxidizer flow and grain OD is {t_max:.3f} s. "
            "Increase case OD, reduce O/F or fuel mass, or shorten burn time."
        )
    if burn_time_s < t_min:
        # Target is shorter than even a vanishingly thin web — return near-OD port.
        return float(d_hi)

    # Bisection: drive t(D0) toward burn_time_s.
    a, b = d_lo, d_hi
    for _ in range(max_iter):
        mid = 0.5 * (a + b)
        t_mid = web_burn_time_s(mid, grain_od_m, m_dot_ox)
        if abs(t_mid - burn_time_s) < tol_s:
            return float(mid)
        if t_mid > burn_time_s:
            # Burn lasts too long => web too thick => enlarge the port.
            a = mid
        else:
            # Burn too short => web too thin => shrink the port.
            b = mid
    return float(0.5 * (a + b))


# =============================================================================
# Sizing
# =============================================================================


def size_motor(inp: MotorInputs) -> tuple[MotorGeometry, DesignPerformance]:
    """
    Compute grain geometry and nozzle design point from MotorInputs.

    Steps:
      1. Grain OD from case OD and wall/liner thickness.
      2. Oxidizer mass from O/F; constant m_dot_ox = m_ox / t_burn.
      3. Solve initial port so web burns through in t_burn.
      4. Grain length from fuel volume and annular cross-section.
      5. Frozen nozzle analysis (P_e = 1 atm): throat, c*, chamber & SL Isp.
    """
    # --- Input validation (fail early with clear messages) ---
    if inp.wall_thickness_m <= 0:
        raise ValueError("wall_thickness_m must be > 0")
    if inp.case_od_m <= 2 * inp.wall_thickness_m:
        raise ValueError("case_od_m must be larger than 2 * wall_thickness_m")
    if inp.fuel_mass_kg <= 0 or inp.burn_time_s <= 0:
        raise ValueError("fuel_mass_kg and burn_time_s must be > 0")
    if inp.of_ratio <= 0:
        raise ValueError("of_ratio must be > 0")
    if inp.chamber_pressure_pa <= 0:
        raise ValueError("chamber_pressure_pa must be > 0")
    if inp.total_impulse_n_s <= 0:
        raise ValueError("total_impulse_n_s must be > 0")

    # Fuel grain sits inside the case; subtract wall+liner on both sides of diameter.
    grain_od = inp.case_od_m - 2.0 * inp.wall_thickness_m

    # Design O/F defines how much oxidizer accompanies the fuel load.
    oxidizer_mass = inp.of_ratio * inp.fuel_mass_kg
    # Assume a constant oxidizer flow that empties the oxidizer in burn_time.
    m_dot_ox = oxidizer_mass / inp.burn_time_s

    # Core solve: choose D_port so radial burn-through matches burn_time.
    port_diameter = solve_initial_port_diameter(grain_od, m_dot_ox, inp.burn_time_s)
    port_area = 0.25 * np.pi * port_diameter**2
    gox_initial = m_dot_ox / port_area  # reported as an output

    # Annular grain: volume = (pi/4)(OD^2 - ID^2) * L  =>  L = V / annular_area
    fuel_volume = inp.fuel_mass_kg / inp.fuel_density_kg_m3
    annular_area = 0.25 * np.pi * (grain_od**2 - port_diameter**2)
    if annular_area <= 0:
        raise ValueError("Invalid annular grain area after port solve")

    grain_length = fuel_volume / annular_area
    web = 0.5 * (grain_od - port_diameter)

    # --- Average propellant flow and thrust (design point for the nozzle) ---
    total_propellant = inp.fuel_mass_kg + oxidizer_mass
    m_dot_avg = total_propellant / inp.burn_time_s
    thrust_avg = inp.total_impulse_n_s / inp.burn_time_s  # F_avg = I / t

    # Frozen nozzle: P_e = P_a = 1 atm, gamma = 1.25.
    # Returns A_t, theoretical c* = P_c A_t / m_dot, and both Isp values.
    nozzle = analyze_nozzle(
        of_ratio=inp.of_ratio,
        chamber_pressure_pa=inp.chamber_pressure_pa,
        m_dot_avg_kg_s=m_dot_avg,
        thrust_avg_n=thrust_avg,
    )

    geometry = MotorGeometry(
        grain_od_m=float(grain_od),
        port_diameter_m=float(port_diameter),
        grain_length_m=float(grain_length),
        web_thickness_m=float(web),
        m_dot_ox_kg_s=float(m_dot_ox),
        oxidizer_mass_kg=float(oxidizer_mass),
        fuel_volume_m3=float(fuel_volume),
        gox_initial_kg_s_m2=float(gox_initial),
    )
    performance = DesignPerformance(
        total_propellant_kg=float(total_propellant),
        m_dot_avg_kg_s=float(m_dot_avg),
        thrust_avg_n=float(thrust_avg),
        nozzle=nozzle,
        c_star_m_s=nozzle.c_star_m_s,
        throat_area_m2=nozzle.throat_area_m2,
        throat_diameter_m=nozzle.throat_diameter_m,
        isp_sea_level_s=nozzle.isp_sea_level_s,
        isp_chamber_s=nozzle.isp_chamber_s,
    )
    return geometry, performance


# =============================================================================
# Time-dependent burn simulation
# =============================================================================


def _state_at(
    d_port: float,
    length: float,
    m_dot_ox: float,
    rho: float,
    isp_sea_level: float,
    c_star: float,
    a_t: float,
) -> tuple[float, float, float, float, float, float, float]:
    """
    Evaluate instantaneous motor state at a given port diameter.

    Returns:
      gox, r_dot, m_dot_fuel, m_dot_total, of_ratio, thrust, chamber_pressure

    Fuel mass flow uses the cylindrical burning surface:
      A_burn = pi * D_port * L
      m_dot_fuel = rho * A_burn * r_dot

    Thrust uses the design *sea-level* I_sp held fixed:
      F = I_sp,sl * m_dot_total * g0

    Instantaneous chamber pressure assumes the design throat stays choked:
      P_c = m_dot_total * c* / A_t
    with c* from the nozzle analysis (not a user guess).
    """
    a_port = max(0.25 * np.pi * d_port**2, 1e-18)
    g = m_dot_ox / a_port
    r = float(regression_rate_m_s(g))
    m_f = rho * (np.pi * d_port * length) * r
    m_tot = m_dot_ox + m_f
    of = m_dot_ox / m_f if m_f > 0 else np.inf
    thrust = isp_sea_level * m_tot * G0
    pc = m_tot * c_star / a_t
    return g, r, m_f, m_tot, of, thrust, pc


def simulate_burn(
    inp: MotorInputs,
    geometry: MotorGeometry,
    performance: DesignPerformance,
) -> BurnHistory:
    """
    March forward in time until the web, fuel, or oxidizer schedule ends.

    Assumptions:
      - Circular port remains circular (1D radial burn).
      - Oxidizer mass flow is constant until t = burn_time.
      - Sea-level I_sp is held at the nozzle design value.
      - Throat area and c* are fixed at the nozzle design values.

    Each step:
      1. Record current state.
      2. Check stop conditions.
      3. Choose a time step that will not overshoot burnout events.
      4. Grow the port by 2 * r_dot * dt and consume fuel.
    """
    dt = inp.dt_s
    if dt <= 0:
        raise ValueError("dt_s must be > 0")

    # Local copies of geometry / performance used inside the loop.
    d_port = geometry.port_diameter_m
    d_grain = geometry.grain_od_m
    length = geometry.grain_length_m
    m_dot_ox = geometry.m_dot_ox_kg_s
    rho = inp.fuel_density_kg_m3
    isp_sl = performance.isp_sea_level_s
    c_star = performance.c_star_m_s
    a_t = performance.throat_area_m2
    t_ox_end = inp.burn_time_s

    # Pre-allocate arrays (slightly longer than burn_time / dt for safety).
    max_steps = int(t_ox_end / dt) + 10
    t = np.zeros(max_steps)
    port = np.zeros(max_steps)
    rdot = np.zeros(max_steps)
    gox = np.zeros(max_steps)
    mdot_f = np.zeros(max_steps)
    mdot_tot = np.zeros(max_steps)
    of_arr = np.zeros(max_steps)
    thrust = np.zeros(max_steps)
    pc = np.zeros(max_steps)
    fuel_used = np.zeros(max_steps)

    fuel_remaining = inp.fuel_mass_kg
    time = 0.0
    reason = "oxidizer_depleted"
    i = 0

    while i < max_steps:
        # --- Current state ---
        g, r, m_f, m_tot, of, f, p = _state_at(
            d_port, length, m_dot_ox, rho, isp_sl, c_star, a_t
        )
        t[i] = time
        port[i] = d_port
        rdot[i] = r
        gox[i] = g
        mdot_f[i] = m_f
        mdot_tot[i] = m_tot
        of_arr[i] = of
        thrust[i] = f
        pc[i] = p
        fuel_used[i] = inp.fuel_mass_kg - fuel_remaining

        # --- Stop conditions (checked after recording so the final point is kept) ---
        if d_port >= d_grain - 1e-12:
            reason = "web_burned_through"
            i += 1
            break
        if fuel_remaining <= 1e-12:
            reason = "fuel_depleted"
            i += 1
            break
        if time >= t_ox_end - 1e-15:
            reason = "oxidizer_depleted"
            i += 1
            break

        # --- Adaptive step: never jump past oxidizer end, fuel end, or web end ---
        dt_step = min(dt, t_ox_end - time)
        if m_f > 0:
            dt_step = min(dt_step, fuel_remaining / m_f)
        if r > 0:
            # Diameter grows at 2*r; time to hit grain OD is (D_od - D) / (2r).
            dt_step = min(dt_step, (d_grain - d_port) / (2.0 * r))

        # Explicit Euler update of port diameter and fuel mass.
        d_port = min(d_port + 2.0 * r * dt_step, d_grain)
        fuel_remaining = max(0.0, fuel_remaining - m_f * dt_step)
        time += dt_step
        i += 1
    else:
        # while-else in Python: runs if the loop did *not* break.
        reason = "max_steps"

    # Trim unused pre-allocated entries.
    n = max(i, 1)
    return BurnHistory(
        time_s=t[:n],
        port_diameter_m=port[:n],
        regression_rate_m_s=rdot[:n],
        gox_kg_s_m2=gox[:n],
        m_dot_fuel_kg_s=mdot_f[:n],
        m_dot_total_kg_s=mdot_tot[:n],
        of_ratio=of_arr[:n],
        thrust_n=thrust[:n],
        chamber_pressure_pa=pc[:n],
        fuel_consumed_kg=fuel_used[:n],
        burnout_reason=reason,
    )


def run_motor(inp: MotorInputs) -> MotorResult:
    """
    Convenience entry point: size the motor (grain + nozzle), then simulate.

    This is what the GUI and CLI call.
    """
    geometry, performance = size_motor(inp)
    history = simulate_burn(inp, geometry, performance)
    return MotorResult(geometry=geometry, performance=performance, history=history)
