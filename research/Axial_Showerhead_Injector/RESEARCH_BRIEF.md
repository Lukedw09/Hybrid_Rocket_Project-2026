# Research Brief: Axial Showerhead Injector Plate Design for Hybrid Rockets

**Author role.** Propulsion research synthesis for hybrid motor design.  
**Companion index.** [`INDEX.md`](INDEX.md) — full bibliographic inventory and local file map.  
**Date.** 2026-07-11

**Notation (plain text).**  
`m_dot_ox` = oxidizer mass flow rate · `N` = number of orifices · `A_inj` = single-orifice geometric area · `d_inj` = orifice diameter · `L_inj` = orifice length (plate thickness through-hole) · `Cd` = discharge coefficient · `DeltaP` = injector pressure drop · `P_c` = chamber pressure · `rho_ox` = liquid oxidizer density · `u_ox` = axial injection velocity · `SMD` = Sauter mean diameter · `Re`, `Oh`, `We` = Reynolds, Ohnesorge, Weber numbers · `eta_c*` = characteristic-velocity efficiency · `G_ox` = oxidizer mass flux in the fuel port.

---

## 1. Executive finding

An **axial showerhead injector plate** is the simplest and most common liquid-oxidizer injector in hybrid rockets: a flat faceplate with many **parallel, axial orifices** that meter and distribute oxidizer into the prechamber / grain port [BOU21; BOU17]. It is chosen for **manufacturability, mechanical robustness, and relatively quiet chamber-pressure traces**, not for best-in-class atomization [BOU19E; BOU21].

Design is **not** “drill enough holes to pass the mass flow.” Reputable practice is:

1. Freeze **`m_dot_ox`**, target **`DeltaP / P_c`**, and a realistic **`Cd`** (often much lower for flashing N₂O than for water) [BOU17; BOU19E; HUM95; ULB].  
2. Choose **`N` and `d_inj`** so total geometric area satisfies the orifice equation **and** atomization criteria (`Re`, `We`, SMD) [GAM13; BOU21].  
3. Lay orifices on **concentric rings** sized to the **grain port**, not only the chamber ID [GAM13; BOU21].  
4. Couple the plate to **prechamber length**: coarser jets need more vaporization length [GON25; BOU17].  
5. Prove the design with **water Cd calibration → N₂O cold-flow → hot-fire** [BOU17; BOU21].

On a well-documented 1 kN paraffin/N₂O motor, reducing orifice diameter at fixed `m_dot_ox` (more, smaller holes) cut SMD and raised average regression rate by about **5%**, with a more stable exhaust plume [BOU19E; BOU21].

---

## 2. What the showerhead does (and does not)

Upstream of the solid fuel, liquid oxidizer must be **metered**, **distributed**, and **atomized** so droplets can vaporize in the prechamber and mix with fuel vapor in the port [BOU17; ULB]. The showerhead does this by discharging many high-speed axial jets through a common faceplate [BOU21].

| Strength | Limitation | Sources |
|----------|------------|---------|
| Easy to CAD/machine; few parts | Relatively **poor atomization** vs pressure-swirl or vortex | [BOU21; BOU19A] |
| Predictable axial jets; often **stable `P_c` signal** | Jets can **gouge / channel** the grain face if too coarse or misaligned | [BOU19E; BOU21] |
| Straightforward orifice-equation sizing | N₂O **flashes** at the exit — water cold-flow is only a partial analog | [BOU17] |
| Easy to swap plates for parametric tests | Does not by itself fix a too-short prechamber | [GON25; LEE20] |

Compared with swirl / hollow-cone / vortex injectors on the **same** ULB 1 kN paraffin/N₂O motor, showerheads trade some regression and efficiency for simplicity and axial-flow behavior [BOU19A]. Use a showerhead when development speed and stability margin matter more than squeezing the last percent of `eta_c*`; upgrade atomization later if vaporization length or efficiency is the bottleneck [BOU19A; GON25].

---

## 3. Core sizing equation

Oxidizer mass flow through a multi-orifice plate is written [BOU17; BOU19E]:

```text
  m_dot_ox  =  Cd * N * A_inj * sqrt( 2 * rho_ox * DeltaP )

  where:
    A_inj   =  pi * d_inj^2 / 4     (one orifice)
    DeltaP  =  P_upstream - P_c
```

**Design loop:**

1. From motor ballistics, pick **`m_dot_ox`** (and thus roughly thrust / O/F) [BOU17].  
2. Pick a target **`DeltaP`**. Hybrid / liquid practice clusters near **`DeltaP ≈ (0.20 – 0.30) * P_c`** (≥ ~20% of chamber pressure is commonly cited to limit hot-gas backflow and feed coupling) [HUM95; ULB; GON25].  
3. Assume a **`Cd`**, solve for **`N * A_inj`**, then pick an integer **`N`** and **`d_inj`** that also meet atomization and layout rules (§4–5).  
4. **Measure `Cd`** on the finished plate — design guesses are often wrong for N₂O (§3.1).

Injection velocity for a plain orifice (useful for Re / We / SMD) [BOU21]:

```text
  u_ox  =  m_dot_ox / ( rho_ox * N * A_inj )
```

(Equivalently, from Bernoulli with losses: `u_ox ≈ Cd * sqrt(2 * DeltaP / rho_ox)`.)

### 3.1 Discharge coefficient — water vs N₂O

Textbook / preliminary designs often take **`Cd ≈ 0.6`** for sharp-edged orifices [BOU17; BOU19E]. On ULB’s benchmark showerhead (11 × 1.4 mm, `L_inj = 7` mm):

- Water cold-flow `Cd` already fell **below** the 0.6 design value [BOU17; BOU19E].  
- Hot-fire / N₂O operation implied a real **`Cd ≈ 0.32`** — about half the initial assumption — so later plates (SH2–SH4) were resized with **`Cd ≈ 0.33`** to hit 550 g/s [BOU19E; BOU21].

**Lesson:** size with a conservative N₂O `Cd` (start ~0.3–0.4 if you lack data), then calibrate. Do not freeze hole count from water-only `Cd = 0.6` if the flight oxidizer is saturated N₂O [BOU17; WHI10].

N₂O jets also **expand / flash** at ambient backpressure differently from water: cold-flow photos show a cone-like gas–liquid plume at each orifice rather than a clean liquid column [BOU17]. Density and quality (vapor fraction) therefore enter both `m_dot_ox` and atomization — Whitmore’s self-pressurizing feed model is the usual engineering frame for the upstream state [WHI10].

---

## 4. Orifice diameter, count, and atomization

### 4.1 Dimensionless checks (Gamper & Hink)

Before freezing `d_inj`, check the three classical orifice numbers [GAM13; BOU21]:

```text
  Re  =  rho_L * u_ox * d_inj / mu_L     →  want  Re  >  ~2300  (turbulent orifice flow)
  Oh  =  mu_L / sqrt( rho_L * sigma * d_inj )
  We  =  rho_G * u_ox^2 * d_inj / sigma  →  want  We  >  ~50   (inertial breakup into fine drops)
```

(`rho_L`, `mu_L`, `sigma` = liquid density, viscosity, surface tension; `rho_G` = surrounding gas density.)

Gamper & Hink place N₂O injector designs on an **Ohnesorge–Reynolds** map so atomization occurs promptly at the orifice exit and droplet sizes stay in a useful band for homogeneous combustion [GAM13]. Bouziane’s four showerheads all satisfied Re ≫ 2300 and We ≫ 50 for their N₂O property set [BOU21].

### 4.2 Sauter mean diameter (plain orifice)

For axial showerheads, Bouziane uses the Tanasawa–Toyoda plain-orifice SMD estimate [TAN55; BOU21]:

```text
  SMD  ≈  47 * (d_inj / u_ox) * (sigma / rho_G)^0.25
          * [ 1 + 331 * mu_L / sqrt( rho_L * sigma * d_inj ) ]
```

**At fixed `m_dot_ox`**, smaller `d_inj` (more orifices) → lower SMD [BOU19E]. ULB calculated SMDs for the 550 g/s family [BOU21]:

| Injector | `d_inj` | `N` | `u_ox` (m/s) | SMD (μm) |
|----------|---------|-----|--------------|----------|
| SH2 | 1.9 mm | 11 | 22.8 | ~2780 |
| SH3 | 1.4 mm | 21 | 24.4 | ~1970 |
| SH4 | 0.8 mm | 71 | 20.0 | ~1450 |
| SH1 (benchmark, ~400 g/s) | 1.4 mm | 11 | 30.6 | ~1570 |

Smaller drops vaporize faster → shorter required prechamber and better mixing for a given residence time [GON25; BOU17]. Raising `DeltaP` also shrinks drops but **raises** `u_ox`, which can increase the axial distance needed for vaporization — a real trade the prechamber designer must close [GON24; GON25].

### 4.3 Orifice length (plate thickness)

ULB’s reference SH elements used **`L_inj = 7` mm** with `d_inj = 1.4` mm (`L/d ≈ 5`) [BOU17; BOU19E]. Length affects entrance losses, `Cd`, and jet coherence; keep `L/d` consistent across a plate family when comparing orifice diameters, and re-measure `Cd` if you change plate thickness [BOU17].

---

## 5. Faceplate layout and grain-port alignment

**Pattern.** Spread orifices on **concentric rings plus a center hole** so the spray footprint is uniform across the prechamber / port entrance [BOU17; BOU19E]. SH1/SH2 used 11 holes on two radii + center; SH3 densified to 21 holes; SH4 to 71 holes of 0.8 mm [BOU21].

**Align to the port, not only the chamber wall.** Homogeneous combustion wants orifice placement matched to the **solid-fuel port shape**; too much oxidizer stuck outside a small port (or all jammed into a large port) changes local O/F and plume behavior [GAM13; BOU21]. On the ULB SH4 plate vs initial port diameter [BOU21]:

| Initial port Ø | Approx. fraction of `m_dot_ox` aimed into the port |
|----------------|-----------------------------------------------------|
| 20 mm | 23% |
| 30 mm | 37% |
| 40 mm | 51% |
| 50 mm | 65% |

Larger ports admitted more oxidizer **into** the grain and shifted O/F, `G_ox`, regression, and `eta_c*` [BOU21]. After burns, coarse few-hole plates left **smooth longitudinal channels**; the fine 71-hole plate left **pits / scratches** but the highest regression — surface finish is a forensic clue for jet–grain interaction, not a free aesthetic choice [BOU19E; BOU21].

**Practical rule:** sketch the orifice circle diameters against **initial and final** port diameters for your burn time. Prefer a pattern that keeps a large fraction of jets inside the port early in the burn without permanently drilling the grain face with a few oversized jets [BOU21; GAM13].

---

## 6. Pressure drop, stability, and the prechamber

### 6.1 Why `DeltaP` is a stability control

Adequate injector pressure drop helps **decouple** the feed system from chamber-pressure oscillations and reduces reverse flow of hot gas into the manifold [ULB; HUM95; LEE20]. ULB explicitly recommends **≥ ~20% of `P_c`**; Gontijo cites the common **~20–30% of `P_c`** band for hybrid injectors [ULB; GON25; HUM95]. ULB’s 1 kN design targeted **`DeltaP ≈ 25` bar** with `P_c` in the **20–30 bar** class [BOU17; BOU19E].

Feed-system-coupled (FSC) instability models used for hybrid prechambers include a term proportional to `P_c / (2 * DeltaP)` together with prechamber residence time — so **injector `DeltaP` and `L_pc` are co-design variables**, not sequential afterthoughts [LEE20; GON25].

### 6.2 Injection velocity and vaporization length

Higher `u_ox` and larger SMD both stretch the distance needed to vaporize droplets in the oxidizer-rich prechamber [GON25]. Axial showerheads with millimeter-class orifices produce **millimeter-scale** SMDs in the ULB correlations — far coarser than a well-designed pressure-swirl element — so a showerhead motor often needs a **longer** prechamber (or accepts incomplete vaporization into the port) [BOU17; GON25; BOU19A]. See the companion brief on prechamber length [`../N2O_paraffin_premixing_chamber/RESEARCH_BRIEF.md`](../N2O_paraffin_premixing_chamber/RESEARCH_BRIEF.md).

### 6.3 Axial topology and acoustics

Injector **topology** (axial vs radial / wall-impinging) strongly affects low-frequency stability and head-end recirculation [CAR06; CAR09]. Axial showerheads are often described as producing a **stable chamber-pressure signal** during combustion [BOU19E], but that does not exempt the designer from FSC checks when `DeltaP` is soft or the prechamber is short [LEE20].

---

## 7. Experimental anchors (ULB 1 kN paraffin / N₂O)

Design targets for the ULB-HRM motor [BOU17; BOU21]:

| Parameter | Value |
|-----------|--------|
| Thrust (nominal) | ~1 kN |
| `m_dot_ox` (design) | 550 g/s (SH1 benchmark ~400 g/s) |
| Fuel | Paraffin |
| `P_c` | ~20–30 bar |
| Feed / tank pressure (tests) | 60 bar (N₂ pressurant) |
| Design `DeltaP` | 25 bar |
| Prechamber length | 100 mm |

Hot-fire comparison at matched ~550 g/s [BOU19E; BOU21]:

- **SH2 vs SH3** (11 × 1.9 mm vs 21 × 1.4 mm): **no major** overall performance difference.  
- **SH4** (71 × 0.8 mm): **~5% higher** average regression rate at the same average `G_ox`, higher `eta_c*`, more stable plume intensity.  
- **SH1** (~400 g/s, high `u_ox`): hard starts / blow-out features in the plume; undersized `m_dot_ox` relative to the motor’s O/F target.

Cold-flow program (water then N₂O) measured `Cd`, spray angle, and laser-scattering SMD before committing to hot-fire [BOU17]. That sequence is the model workflow for a new plate.

---

## 8. Design guidance (researcher’s checklist)

1. **Set ballistics first:** `m_dot_ox`, `P_c`, burn time, initial/final port diameters.  
2. **Set `DeltaP / P_c ≈ 0.20 – 0.30`** (floor ~0.20) unless a cavitating/choked feed element intentionally owns isolation — noting cavitating venturis are **discouraged for N₂O** [HUM95; ULB; GON25; LEE20].  
3. **Assume `Cd` cautiously for N₂O** (~0.3–0.4 until measured); solve `N * A_inj` from the orifice equation [BOU19E].  
4. **Prefer more, smaller orifices** over few large ones at fixed area — lower SMD, better regression / plume stability in ULB data — subject to machining limits and clogging risk [BOU19E; BOU21].  
5. **Check `Re > ~2300` and `We > ~50`**; estimate SMD and feed it to the prechamber vaporization length [GAM13; BOU21; GON25].  
6. **Lay out concentric rings** sized to the **port**, and quantify what fraction of jets enter the port at `t = 0` and mid-burn [GAM13; BOU21].  
7. **Keep `L_inj / d_inj` consistent** across variants; ULB’s reference was `L_inj = 7` mm [BOU17].  
8. **Validate:** water `Cd` map → N₂O cold-flow visualization → instrumented hot-fire (`P_c`, `DeltaP`, thrust, mass accounting, plume) [BOU17; BOU21].  
9. **If atomization or `eta_c*` is insufficient**, consider pressure-swirl / vortex upgrades on the **same** motor before abandoning the chamber geometry [BOU19A; BOU17].  
10. **Re-fit regression `a`, `n`** if you change injector family — injector pattern is ballistically first-order for paraffin/N₂O [BOU21; BOU19A].

---

## 9. Source quality map

| Tier | Role | Keys |
|------|------|------|
| **A — Showerhead experiment** | Geometry, Cd, SMD, hot-fire | BOU21, BOU19E, BOU17 |
| **A — Injector comparison** | SH vs swirl / vortex on one motor | BOU19A |
| **A — Atomization criteria** | Re / Oh / We design rules for N₂O | GAM13 |
| **B — System coupling** | `DeltaP`, prechamber, FSC stability | GON25, GON24, LEE20, ULB, HUM95 |
| **B — Topology / acoustics** | Axial vs radial injector effects | CAR06, CAR09 |
| **C — Background** | Feed modeling, SMD correlation, textbooks | WHI10, TAN55, SUT10 |

Full bibliographic details, DOIs, and local download paths: **[`INDEX.md`](INDEX.md)**. BibTeX: **[`references.bib`](references.bib)**.

---

## 10. Inline citation key list

- **[BOU17]** Bouziane et al., EUCASS 2017-133 — cold-flow injector design & Cd  
- **[BOU19E]** Bouziane et al., EUCASS 2019-473 — showerhead hot-fire orifice study  
- **[BOU21]** Bouziane et al., *FirePhysChem* 2021 — archival axial-SH geometry paper  
- **[BOU19A]** Bouziane et al., *AST* 2019 — SH / HC / PSW / VOR comparison  
- **[GAM13]** Gamper & Hink, DLRK 2013 — N₂O injector Re / Oh / We guidance  
- **[HUM95]** Humble, Henry & Larson — `DeltaP / P_c` textbook practice  
- **[SUT10]** Sutton & Biblarz — rocket injector / chamber background  
- **[GON25]** / **[GON24]** Gontijo — vaporization length & `DeltaP`–droplet coupling  
- **[LEE20]** Lee et al., *JPP* 2020 — injection velocity / prechamber FSC tests  
- **[CAR06]** / **[CAR09]** Carmicino — injector topology & hybrid stability  
- **[WHI10]** Whitmore & Chandler — self-pressurizing N₂O feed model  
- **[ULB]** ULB EUCASS — ≥20% `DeltaP`; prechamber vaporization role  
- **[TAN55]** Tanasawa & Toyoda — plain-orifice SMD correlation  
