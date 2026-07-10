# Clarification: Project Regression Constants vs Bertoldi

**Status (current).** `ParaffinN2O_dimensioncalc/model.py` uses Bertoldi’s **pressure-swirl** paraffin/N₂O law in SI units:

```text
  REGRESSION_A = 0.1531
  REGRESSION_N = 0.67

  r_dot [mm/s]  =  0.1531  *  G_ox[kg/(m²·s)] ^ 0.67
```

**Related files**
- Code: `ParaffinN2O_dimensioncalc/model.py`
- Source: Bertoldi (2007) thesis — `downloads/04_Bertoldi_2007_UnB_Thesis_Paraffin_N2O.pdf` (Eq. 4.1)
- How to measure your own `a`,`n`: `EXPERIMENTAL_MEASUREMENT_OF_A_AND_N.md`
- Broader context: `RESEARCH_BRIEF.md`

---

## 1. The law in both unit systems

Both forms use the same exponent `n = 0.67`:

```text
  r_dot  =  a  *  G_ox ^ n
```

| Form | a | G_ox units | r_dot units |
|------|---|------------|-------------|
| Bertoldi Eq. (4.1) / cgs | **0.7197** | g/(cm²·s) | mm/s |
| Project / Bertoldi SI | **0.1531** | kg/(m²·s) | mm/s |

These are the **same physical correlation**, not two different motors.

---

## 2. Unit conversion (why 0.7197 ↔ 0.1531)

### Flux identity

```text
  1 g/(cm²·s)  =  10 kg/(m²·s)

  G_cgs  =  G_SI / 10
  G_SI   =  G_cgs * 10
```

### Converting a at fixed n

```text
  r_dot  =  a_cgs * G_cgs^n
         =  a_cgs * (G_SI / 10)^n
         =  (a_cgs / 10^n) * G_SI^n

  a_SI   =  a_cgs / 10^n
  a_cgs  =  a_SI  * 10^n
```

With `a_cgs = 0.7197` and `n = 0.67`:

```text
  10^0.67  ≈  4.677
  a_SI     =  0.7197 / 4.677  ≈  0.1539
```

Bertoldi states **a = 0.1531** for kg/(m²·s). The project uses that stated SI value.

Inverse check:

```text
  0.1531 * 10^0.67  ≈  0.1531 * 4.677  ≈  0.716
```

(Close to 0.7197; small rounding between thesis statements.)

---

## 3. Historical note: previous project constant

Before this update, the code used:

```text
  REGRESSION_A = 0.104   (same n = 0.67, SI flux)
```

Comparison to Bertoldi SI:

```text
  0.104 / 0.1531  ≈  0.68
```

So the old constant predicted about **32% lower** regression rate at every `G_ox`. That was a more cautious ballistics estimate, but it was **not** Bertoldi’s pressure-swirl law.

| G_ox [kg/(m²·s)] | Old a=0.104 | Current a=0.1531 (Bertoldi) |
|------------------|-------------|------------------------------|
| 50 | 1.55 mm/s | 2.28 mm/s |
| 100 | 2.42 mm/s | 3.56 mm/s |
| 150 | 3.15 mm/s | 4.64 mm/s |
| 200 | 3.81 mm/s | 5.61 mm/s |

(Formula: `r_dot = a * G_ox^0.67`.)

---

## 4. What this means for sizing

Relative to the old `a = 0.104`, the Bertoldi constant implies:

| Quantity | Direction of change |
|----------|---------------------|
| Predicted `r_dot` at fixed G | Higher (~+47% relative to old, since 0.1531/0.104 ≈ 1.47) |
| Fuel mass flow at fixed geometry | Higher |
| Instantaneous O/F at fixed m_dot_ox | Lower (more fuel-rich) |
| Web burn-through time at fixed m_dot_ox | Shorter |

**Caveat:** Bertoldi’s `a`,`n` are for a **pressure-swirl** UnB motor. Axial injectors, diaphragms, different wax grades, or different averaging methods can shift both constants. Measure your own with `EXPERIMENTAL_MEASUREMENT_OF_A_AND_N.md` when hardware differs.

Bertoldi’s own prechamber series used a different fit (`a = 1.2301`, `n = 0.47` in cgs) — proof that configuration matters.

---

## 5. One-line summary

The project now uses Bertoldi 2007 pressure-swirl paraffin/N₂O: **a = 0.1531**, **n = 0.67** with G_ox in kg/(m²·s), equivalent to **a = 0.7197** with G_ox in g/(cm²·s).
