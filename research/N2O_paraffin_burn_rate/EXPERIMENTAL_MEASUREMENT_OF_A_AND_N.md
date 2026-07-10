# Experimental Measurement of Regression Constants a and n

**Purpose.** Step-by-step procedure to measure the empirical constants in

```text
  r_dot  =  a  *  G_ox ^ n
```

for a hybrid propellant pair (here: paraffin + N₂O), so you can replace or validate literature values such as Bertoldi’s pressure-swirl law used in this project.

**Audience.** Lab / student rocketry teams sizing motors from hot-fire data.  
**Companion docs.** `REGRESSION_CONSTANT_CLARIFICATION.md`, `INDEX.md` (BER07, KCZ07, KZC04).

---

## 0. What you are fitting

| Symbol | Name | Typical units in this project |
|--------|------|-------------------------------|
| `r_dot` | Space–time-averaged fuel regression rate | mm/s |
| `G_ox` | Space–time-averaged oxidizer mass flux | kg/(m²·s) or g/(cm²·s) |
| `a` | Regression coefficient | same as `r_dot` when `G_ox = 1` in chosen units |
| `n` | Flux exponent | dimensionless |

**Important:** `a` depends on the **units of G_ox**. Always state units with the fit. This project’s SI form is:

```text
  r_dot [mm/s]  =  a_SI  *  G_ox[kg/(m²·s)] ^ n
```

Bertoldi pressure-swirl reference: `a_SI = 0.1531`, `n = 0.67`.

---

## 1. Experimental goal and test philosophy

You need **many firings** that span a useful range of oxidizer mass flux, then plot:

```text
  log(r_dot)  vs  log(G_ox)
```

A straight line gives:

```text
  log(r_dot)  =  log(a)  +  n * log(G_ox)

  slope     →  n
  intercept →  log(a)  →  a = 10^(intercept)   (if log is base 10)
```

**Design rules of thumb**
- Aim for **≥ 8–12 good firings** after discarding ignition failures and web burn-throughs.
- Span at least a **factor of ~2–3 in G_ox** (wider is better for a stable `n`).
- Hold **injector type, fuel formulation, and grain length** fixed while varying flux (change `m_dot_ox` and/or initial port diameter).
- Do **not** mix swirl and axial-injector data into one fit unless that is intentional.

---

## 2. Hardware and instrumentation checklist

### 2.1 Motor / grain

| Item | Why it matters |
|------|----------------|
| Single circular port grain (known initial ID, OD, length) | Simple geometry for averaging |
| Repeatable paraffin casting / machining | Manufacturing scatter dominates paraffin data |
| Fixed injector (e.g. pressure-swirl) | `a` and `n` are hardware-specific |
| Nozzle sized so chamber pressure is measurable and stable | Burn-time definition from Pc trace |

### 2.2 Measurements you must record every firing

| Measurement | Typical sensor | Used for |
|-------------|----------------|----------|
| Oxidizer mass flow vs time, `m_dot_ox(t)` | Coriolis, turbine + density, or Δm_tank / Δt with care | `G_ox` |
| Chamber pressure vs time, `Pc(t)` | Pressure transducer | Burn time `t_b` |
| Optional: thrust vs time | Load cell | Cross-check; not required for `a`,`n` |
| Pre-fire grain mass `m_i` | Scale | Fuel consumed |
| Post-fire grain mass `m_f` | Scale | Fuel consumed |
| Pre-fire port diameter `D_i` (or radius `R_i`) | Calipers / CMM, several axial stations | Geometry |
| Post-fire port diameter `D_f` (or `R_f`) | Same, several stations | Geometry |
| Grain length `L` | Calipers | Port volume / O/F checks |
| Fuel density `rho_f` | From mass/volume of a cast sample | Mass ↔ volume consistency |

**Critical:** Without a trustworthy `m_dot_ox`, you cannot get a trustworthy `G_ox`. Early UnB work failed to close `a`,`n` for that reason (see INDEX **BV05**).

### 2.3 Safety (minimum)

N₂O and hybrid firings are hazardous (asphyxiation, pressure vessels, fire, possible N₂O decomposition). Use a written procedure, remote firing, blast/fragment protection, and trained personnel. This document is a **measurement method**, not a safety manual.

---

## 3. How to run one firing (data you need)

1. **Weigh and measure** the grain: `m_i`, `D_i` (average of several axial cuts or ends), `L`.
2. Install grain; leak-check feed system.
3. Record ambient conditions if you care about N₂O density / two-phase feed.
4. Fire with commanded oxidizer flow (or blowdown schedule you can reconstruct).
5. Log `Pc(t)`, `m_dot_ox(t)` (or tank mass), and optional thrust at ≥ 100–1000 Hz as appropriate.
6. After cool-down: **weigh** `m_f`, **measure** `D_f` at multiple stations (paraffin can be uneven).
7. Discard the firing if: ignition failed, grain slumped/fragmented badly, nozzle plugged, or web burned through early.

---

## 4. Reduce each firing to one (G_ox, r_dot) point

This is the core of the method. Use a **consistent averaging definition** for every test (Karabeyoglu / Stanford practice; INDEX **KCZ07**).

### 4.1 Burn time `t_b`

Define burn time from the pressure trace with a written rule, for example:

```text
  t_start  =  time when Pc rises through X% of steady (or ignition spike end)
  t_end    =  time when main oxidizer valve closes
              OR when Pc falls through Y% of the burn average
  t_b      =  t_end - t_start
```

Do **not** include long post-valve “tail” burning unless you correct for it. Bertoldi compared video time vs pressure time and found good agreement when the thrust-decay tail was excluded from paraffin regression.

### 4.2 Space–time-averaged regression rate

**Preferred (diameter-based), circular port:**

```text
  r_dot  =  (R_f - R_i) / t_b
         =  (D_f - D_i) / (2 * t_b)
```

Units: if D in mm and `t_b` in s → `r_dot` in mm/s.

**Mass-based cross-check:**

```text
  m_fuel_burned  =  m_i - m_f

  Average burn area (approx, circular port):
    A_burn_avg  ≈  pi * D_avg * L
    D_avg       =  (D_i + D_f) / 2

  r_dot_mass  ≈  m_fuel_burned / (rho_f * A_burn_avg * t_b)
```

If `r_dot` from diameter and from mass disagree by more than ~10–15%, investigate: uneven burn, slumping, measurement error, or wrong density.

**Multi-station ports:** average `D_f` along the length (or use several local `r_dot` values and report both local and average).

### 4.3 Space–time-averaged oxidizer mass flux

Instantaneous flux:

```text
  G_ox(t)  =  m_dot_ox(t) / A_port(t)
  A_port(t) =  pi * D(t)^2 / 4
```

You usually do **not** know `D(t)` continuously. Use a standard average.

**Recommended simple average (port-diameter average), widely used:**

```text
  D_avg  =  (D_i + D_f) / 2
  A_avg  =  pi * D_avg^2 / 4

  m_ox_total  =  integral of m_dot_ox over t_b
  m_dot_ox_avg  =  m_ox_total / t_b

  G_ox  =  m_dot_ox_avg / A_avg
```

**Better (physics-based) averages** exist when `n` is known or iterated (Karabeyoglu et al., JPP 2007 — INDEX **KCZ07**). Practical workflow:

1. First pass: use `D_avg = (D_i + D_f)/2` as above → get provisional `a`,`n`.
2. Optional second pass: recompute time-averaged G with the analytic port-growth average consistent with that `n`, then refit.
3. Optional O/F correction if your facility reports total mass flux instead of oxidizer flux (see KZC04 / KCZ07).

**Unit conversion reminder:**

```text
  1 g/(cm²·s)  =  10 kg/(m²·s)
```

### 4.4 One row per firing

Store a table like:

| Test ID | D_i | D_f | t_b | m_dot_ox_avg | G_ox | r_dot | Pc_avg | notes |
|---------|-----|-----|-----|--------------|------|-------|--------|-------|

Example (illustrative numbers only):

```text
  Test 12:  D_i=35 mm, D_f=48 mm, t_b=4.3 s
  r_dot = (48 - 35) / (2 * 4.3) = 1.51 mm/s     ← wait, check arithmetic:
          (13 mm) / (8.6 s) = 1.51 mm/s

  Better example matching multi-mm/s paraffin:
  D_i=25.4 mm, D_f=55 mm, t_b=4.0 s
  r_dot = (55 - 25.4) / (2*4.0) = 29.6/8 = 3.70 mm/s
```

---

## 5. Fit a and n from the campaign

### 5.1 Log–log linear regression

For N valid firings with pairs `(G_j, r_j)`:

```text
  x_j  =  ln(G_j)      (natural log is fine; any base works if consistent)
  y_j  =  ln(r_j)

  Fit:  y  =  c  +  n * x
```

Then:

```text
  n  =  slope
  a  =  exp(c)     if using natural log
  a  =  10^c       if using log10
```

**Spreadsheet / Python sketch:**

```python
import numpy as np

G = np.array([...])      # kg/(m^2·s)
r = np.array([...])      # mm/s

n, log_a = np.polyfit(np.log(G), np.log(r), 1)
a = np.exp(log_a)

print(f"a = {a:.4f}, n = {n:.3f}")  # a for G in kg/(m^2·s), r in mm/s
```

### 5.2 Report the fit properly

Always publish:

```text
  r_dot [mm/s] = a * G_ox^n
  G_ox units: kg/(m²·s)   [or g/(cm²·s)]
  Averaging: diameter average D_avg=(D_i+D_f)/2, burn time from Pc rule ___
  Injector: pressure-swirl (or describe)
  Fuel: paraffin grade, additives, density
  N firings, G_ox range, R^2 or residual scatter
```

### 5.3 Convert between SI and cgs a (same n)

```text
  a_SI   =  a_cgs / 10^n
  a_cgs  =  a_SI  * 10^n
```

Bertoldi check: `0.7197 / 10^0.67 ≈ 0.153`.

---

## 6. Recommended test matrix (practical)

Vary flux without changing the regression physics you care about:

| Knob | Effect on G_ox | Notes |
|------|----------------|-------|
| Initial port diameter `D_i` | Smaller D → higher G | Keep web thick enough for planned `t_b` |
| Oxidizer feed pressure / orifice | Changes `m_dot_ox` | Prefer measured flow, not assumed Cd alone |
| Burn time | Longer burn → more port growth → lower time-averaged G | Useful but couples to averaging |

**Example matrix (8+ shots):**

| Shot group | Target | How |
|------------|--------|-----|
| Low G | ~50–80 kg/(m²·s) | Larger D_i and/or lower m_dot_ox |
| Mid G | ~100–150 kg/(m²·s) | Nominal design point |
| High G | ~180–250 kg/(m²·s) | Smaller D_i and/or higher m_dot_ox |

Repeat 2–3 firings near each target to estimate scatter.

**Hold fixed:** fuel batch, injector, nozzle throat (or note Pc changes), grain length (unless you are studying length effect separately).

---

## 7. Quality checks and common failure modes

| Symptom | Likely cause | What to do |
|---------|--------------|------------|
| Huge scatter in log–log plot | Bad `m_dot_ox` or inconsistent `t_b` | Calibrate flow; freeze Pc-based time rule |
| `r_dot` from mass >> from diameter | Slumping / fuel loss not from surface regression | Improve grain strength; discard shot |
| `n` near 0 or > 1 with few points | Insufficient G span | Widen matrix |
| Systematic offset vs Bertoldi | Different injector / wax / averaging | Expected; publish your own `a`,`n` |
| Long grains give lower `r_dot` at same G | Length / entrance effects | Fit separate laws or include length study |
| Pressure strongly correlates with `r_dot` | Radiation / kinetics / facility artifact | Check if G and Pc are confounded |

---

## 8. Worked outline: from raw data to constants

**Given three cleaned firings (toy numbers for teaching):**

```text
  Test A:  G =  80 kg/(m²·s),  r = 2.10 mm/s
  Test B:  G = 120 kg/(m²·s),  r = 2.85 mm/s
  Test C:  G = 180 kg/(m²·s),  r = 3.80 mm/s
```

1. Take ln:

```text
  ln(G):  4.382,  4.787,  5.193
  ln(r):  0.742,  1.047,  1.335
```

2. Linear fit → suppose you get `n ≈ 0.67`, `a ≈ 0.15`.

3. Write the law:

```text
  r_dot [mm/s] = 0.15 * G_ox[kg/(m²·s)] ^ 0.67
```

4. Drop into `model.py`:

```python
REGRESSION_A = 0.15
REGRESSION_N = 0.67
```

(Real campaigns use more points and report uncertainty.)

---

## 9. Uncertainty (minimum reporting)

Even a simple analysis should include:

```text
  δr_dot / r_dot  ≈  sqrt( (δΔR/ΔR)^2 + (δt_b/t_b)^2 )
  δG / G          ≈  sqrt( (δm_dot/m_dot)^2 + (2 δD/D)^2 )
```

Propagate to `a` and `n` via the log–log fit (or bootstrap: refit leaving one test out).

If diameter uncertainty is ±0.5 mm on a 10 mm web growth, that alone is ~5% on `r_dot`.

---

## 10. How this maps to Bertoldi’s pressure-swirl result

Bertoldi (2007) did essentially this procedure on an N₂O–paraffin motor with a **pressure-swirl** injector, applied Stanford-style corrections, and reported:

```text
  r_dot [mm/s] = 0.7197 * G[g/(cm²·s)] ^ 0.67
  r_dot [mm/s] = 0.1531 * G[kg/(m²·s)] ^ 0.67
```

This project’s `model.py` now uses that SI form (`REGRESSION_A = 0.1531`, `REGRESSION_N = 0.67`).

When **your** injector, wax, or scale differs, re-run Sections 3–5 and replace those constants. Do not assume Bertoldi’s `a` transfers unchanged to axial shower-head or diaphragm motors (his own prechamber series changed both `a` and `n`).

---

## 11. Procedure checklist (print and use)

- [ ] Freeze injector, fuel formula, grain length, and averaging definitions in writing  
- [ ] Calibrate oxidizer mass-flow measurement  
- [ ] Define burn-time rule from `Pc(t)`  
- [ ] Build a test matrix spanning ≥ 2× in `G_ox`  
- [ ] For each shot: measure `D_i`, `D_f`, `m_i`, `m_f`, `t_b`, `m_dot_ox`  
- [ ] Compute one `(G_ox, r_dot)` pair per shot  
- [ ] Cross-check mass-based vs diameter-based `r_dot`  
- [ ] Fit `log r` vs `log G` → `a`, `n`  
- [ ] State units of `G_ox` next to `a`  
- [ ] Report range of G, N, scatter, and hardware description  
- [ ] Update `REGRESSION_A` / `REGRESSION_N` in code only after review  

---

## 12. References (primary methods)

| Key | Why read it |
|-----|-------------|
| **KCZ07** Karabeyoglu, Cantwell & Zilliac, *JPP* 2007 | Scalable space–time averaging of `r` and `G` |
| **KZC04** Karabeyoglu et al., *JPP* 2004 | Paraffin scale-up; power-law practice |
| **BER07** Bertoldi thesis 2007 | Worked N₂O–paraffin example; pressure-swirl `a`,`n` |
| **BV05** Bertoldi & Veras, COBEM 2005 | Cautionary: bad flux data → no usable fit |

Local PDFs and DOIs: see `INDEX.md`.
