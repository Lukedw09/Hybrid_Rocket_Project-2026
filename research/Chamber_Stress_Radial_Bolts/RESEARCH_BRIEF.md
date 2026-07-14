# Research Brief: Chamber Stress Analysis & Radial Bolts for 45 bar Hydroproof

**Author role.** Structural research synthesis for the project’s ~152 mm paraffin/N₂O static motor.  
**Companion index.** [`INDEX.md`](INDEX.md) — full bibliographic inventory and local file map.  
**Date.** 2026-07-13

**Notation (plain text).**  
`P` = internal pressure · `MEOP` = maximum expected operating pressure · `Di`, `Do` = casing inside / outside diameter · `t` = casing wall thickness · `N` = number of radial bolts **per end** · `d_maj`, `d_min` = bolt major / minor diameter · `E` = edge distance (case end → hole center) · `Emin` = `E − d_maj/2` · `F` = axial closure force · `FS` = factor of safety = strength / stress · `YTS`, `UTS` = yield / ultimate tensile strength · `BYS` = bearing yield strength.

**Geometry locked to project hardware** [`Hybrid Motor Static Fire Project.md`](../../Hybrid%20Motor%20Static%20Fire%20Project.md):

| Parameter | Value |
|-----------|--------|
| Preferred tube | 6061-T6, **6.0″ OD × 0.125″ wall × 5.75″ ID** |
| MEOP (chamber) | **4 MPa = 40 bar** |
| Hydroproof asked here | **45 bar** (1.125× MEOP) |
| Project / SA Cup-style proof | **≥ 1.5× MEOP = 60 bar** (also tabulated) |
| Closure architecture | Radial bolts through casing into **forward bulkhead** and **aft nozzle carrier** (CAD half-section) |

**Disclaimer.** Hand calculations and literature synthesis for design planning — not a certified pressure-vessel stamp, not FEA, and not a substitute for an adult mentor / site SOP. Always hydro-proof remotely behind exclusion.

---

## 1. Executive finding

Internal pressure tries to **eject** the forward bulkhead and aft nozzle carrier axially. With **radial** fasteners through the thin casing into those closures, the bolts are loaded primarily in **single shear**, while the aluminum wall can fail by **tear-out**, **bearing**, or **net-section tension** between holes [HC25; MIT20; NAK; IOP26].

For this project’s preferred **0.125″ 6061-T6** tube at **45 bar**:

1. **Barrel hoop** is comfortable (`FS_yield ≈ 2.7` room-temp YTS) — the plain cylinder is **not** the weak link [HC25; SUT; MIT20].  
2. **Bearing** in the thin wall is the **first** closure failure mode for practical bolt sizes [HC25].  
3. With **1/4-28 Grade 8** radial screws, edge distance `E = 2 d_maj`, and HalfCat elevated-temperature Al allowables:  
   - **`N ≥ 20` bolts per end** → all four closure modes have **`FS ≥ 2.0` at 45 bar**.  
   - **`N ≥ 26` bolts per end** → same bar if you hydro-proof at the project’s **1.5× MEOP = 60 bar**.  
4. Commercial Contrail **152 mm** hardware uses only **6 bolts per end**, but on a **~0.25″** certified wall — **do not copy that count** onto the 0.125″ custom tube [CON152].

Reproduce numbers with [`downloads/06_project_bolt_count_calc.py`](downloads/06_project_bolt_count_calc.py).

---

## 2. Load path (what the bolts actually do)

```text
  F  =  P * A_i  =  P * (pi/4) * Di^2
```

At **45 bar** on `Di = 5.75″` (146.05 mm): **`F ≈ 75.4 kN` (~17,000 lbf)** acting **outward** on each closure. The same `F` appears at the **forward** and **aft** ends (same pressure × same free area, ignoring nozzle throat area relief which is **not** credited for hydroproof with blanked ends) [HC25; NAK].

Radial bolts through the casing into the bulkhead / nozzle carrier put each fastener in **single shear** at the casing–closure interface [HC25]. Preload and friction help in reality but are **neglected** in design equations (conservative) [HC25].

---

## 3. Barrel stresses (Sutton / thin-wall)

Thin-wall cylinder [MIT20; HC25; SUT]:

```text
  sigma_hoop   =  P * Di / (2 * t)     (or P * r / t with r ≈ Di/2)
  sigma_axial  =  P * Di / (4 * t)
```

| Pressure | Hoop (MPa) | Axial (MPa) | FS vs room-temp YTS 276 MPa (hoop) |
|----------|------------|-------------|-------------------------------------|
| 40 bar (MEOP) | 92 | 46 | **3.00** |
| **45 bar (this hydro)** | **103.5** | **52** | **2.67** |
| 60 bar (1.5× MEOP) | 138 | 69 | **2.00** |

Project docs already size the barrel with Sutton + a **1.50×** metal design margin at MEOP; the table above shows the **stock 0.125″** wall itself is fine for 45 bar hydro. Closures and bolt holes still govern [project notes; HC25].

NASA MSFC solid-motor structural practice uses hydro-proof floors as low as **1.05× MEOP** for some SRM acceptances, with separate burst / joint tests [MSFC]. University / SA Cup amateur practice commonly targets **1.5× MEOP** hold [HC25; WAT18]. This brief sizes fasteners to the **user-requested 45 bar** and also shows **60 bar**.

---

## 4. Four bolted-closure failure modes (must all pass)

HalfCat’s bolted-casing checklist (same physics as Nakka’s bolted nozzle joint and the IOP SRM redesign) [HC25; NAK; IOP26]:

| Mode | What fails | Stress (HalfCat form) | Strength used |
|------|------------|------------------------|---------------|
| **Bolt shear** | Fastener shears between casing & closure | `σ = F / (N * A_min)` with `A_min = π d_min²/4` | `0.75 × UTS_bolt` (steel) |
| **Tear-out** | Bolt rips through case end | `σ = F_bolt / (Emin · 2 · t)` | Al shear ≈ **30 ksi** (6061-T6, HalfCat) |
| **Net tension** | Ligament between holes yields | `σ = F / {[(Do−t)π − N d_maj] t}` | Al **YTS** (38 ksi @ ~200 °F in HalfCat) |
| **Bearing** | Hole wall crushes | `σ = F_bolt / (d_maj · t)` | Al **BYS** ≈ **56 ksi** |

Edge-distance practice: **`E ≥ 1.5–2.0 × d`** (HalfCat strongly prefers **2.0×**; IOP redesign used **2.5×**) [HC25; IOP26; MIT20]. Fine threads preferred (`1/4-28` over `1/4-20`) — larger `d_min` → better bolt-shear FS [HC25].

For thin walls and/or diameters **> ~6″**, a **second staggered bolt circle** may be required so tear-out / bearing FS recover without eating the entire net section [HC25; IOP26; MIT20].

---

## 5. Project bolt-count tables (1/4-28 Grade 8, E = 2d)

Assumptions match HalfCat Appendix A diameters and allowables [HC25; `09_6061T6_Strength_Values_NOTE.txt`]:

- Casing: `Do = 6.0″`, `Di = 5.75″`, `t = 0.125″`, 6061-T6  
- Bolts: `d_maj = 0.250″`, `d_min = 0.2052″`, steel UTS = 150 ksi, shear = `0.75×UTS`  
- Edge: `E = 2.0 × d_maj` → `Emin = 1.5 × d_maj`

### 5.1 Hydroproof = **45 bar** (requested)

| `N` per end | FS bolt shear | FS tear-out | FS net tension | FS bearing | **Min FS** |
|-------------|---------------|-------------|----------------|------------|------------|
| 6 (Contrail count) | 1.32 | 1.00 | 4.75 | 0.62 | **0.62 — fail** |
| 12 | 2.63 | 1.99 | 4.33 | 1.24 | **1.24 — fail** |
| 16 | 3.51 | 2.66 | 4.05 | 1.65 | **1.65** |
| 18 | 3.95 | 2.99 | 3.91 | 1.86 | **1.86** |
| **20** | **4.39** | **3.32** | **3.77** | **2.07** | **2.07 — pass FS≥2** |
| 24 | 5.27 | 3.98 | 3.49 | 2.48 | **2.48** |

**Recommendation at 45 bar:** use **≥ 20 × 1/4-28 Grade 8 (or equivalent)** radial fasteners **on the forward end** and **≥ 20** on the aft end (40 total for the chamber), with `E ≥ 2d`, close-fit clearance holes in the tube, and tapped holes (or helicoils) in thick Al closures. Bearing remains the limiting mode.

### 5.2 If hydroproof rises to **1.5× MEOP = 60 bar**

| `N` per end | Min FS (bearing-limited) |
|-------------|---------------------------|
| 20 | 1.55 |
| 24 | 1.86 |
| **26** | **≈ 2.01** |

Prefer designing the bolt circle for **60 bar** even if the first hydro day is only 45 bar — matches the project checklist and SA Cup-style proof philosophy [HC25; project docs].

### 5.3 Why Contrail’s 6 bolts are not a counter-example

Contrail’s certified 152 mm chamber advertises **6 holes per end** on a **~0.25″** wall [CON152]. Bearing/tear-out capacity scales ≈ linearly with `t`. At half the wall thickness, the same `N` yields roughly **half** the bearing FS — consistent with the table above (`N = 6` → `FS_bearing ≈ 0.62` at 45 bar).

---

## 6. Lessons from published motor failures / redesigns

**IOP 2026 SRM case study [IOP26].** An early design with **8 × M5** radial bolts on an Al 6061-T6 case failed in test: overpressure + grain crack → **forward-closure bolts sheared** and O-ring loss. FEA showed casing hole-region von Mises ~**344 MPa** (above yield) and bolt shear ~**402 MPa**. Redesign used **staggered multi-row bolts**, **2.5d** edge distance, Class **12.9** fasteners, and retainers that change the load path — peak local stress dropped **>30%**.

**Takeaway for this motor:** under-bolting a thin Al case is a documented failure path; verify **all four** modes; consider a **second bolt row** if a single circle cannot hit FS≥2 without crowding ligaments.

**Waterloo hybrid DAC [WAT18].** Hybrid chamber end caps with **24 × 1/4-28** fasteners; closed-form FS ≥ 2 on shear / tear-out / bearing / tension; hydroproof at **1.5×** operating pressure with no measurable plastic set — good process template (analysis → hydro → hot fire).

**Nakka [NAK].** Classic amateur treatment of bolted nozzle joints: balance **bearing**, **plate tension**, and **bolt shear**; same formulas apply to a bolted forward retainer. Prefer failure that **ejects the aft closure** rather than fragmenting the barrel [HC25 Appendix A philosophy].

---

## 7. Design checklist (closures)

1. Freeze `Di`, `t`, MEOP, and **proof pressure** (45 bar minimum for this brief; prefer **60 bar** design).  
2. Compute `F = P × π Di²/4` at **proof**, not only MEOP [HC25].  
3. Pick fastener (prefer fine thread, Grade 8 / Class 12.9; **headed** screws so preload exists; avoid set-screws unless shear area at the socket is explicitly derated) [HC25].  
4. Size `N` so **bolt shear, tear-out, net tension, and bearing** all have **`FS ≥ 2` at proof** (HalfCat: prefer ~3 at MEOP when practical) [HC25].  
5. Enforce `E ≥ 2d` (or 2.5d); keep pitch ≥ ~2–3d so ligaments survive [HC25; IOP26; MIT20].  
6. Machine **thick** bulkhead / nozzle-carrier engagement (tear-out/bearing of the **closure** must also pass — usually OK if thicker than the tube) [HC25].  
7. If single-circle `N` is huge or ligaments vanish → **dual staggered circles** [HC25; IOP26].  
8. O-ring / face seal independent of the bolts (bolts are structure; seals are seals) [NAK O-ring practice; HC25].  
9. Hydro-proof remotely; pass/fail on leak, yield, and fastener inspection; document P–t hold [MSFC; WAT18; project Week 5].  
10. Re-check FS if you change tube wall, bolt diameter, or proof pressure — re-run `06_project_bolt_count_calc.py`.

---

## 8. Source quality map

| Tier | Role | Keys |
|------|------|------|
| **A — Bolted casing equations** | Four failure modes + worked example | HC25 |
| **A — Thin-wall + tear-out wiki** | Hoop/axial + radial tear-out | MIT20 |
| **A — Amateur bolted nozzle** | Bearing / tension / shear balance | NAK |
| **A — Failure + redesign** | Under-bolted Al case → shear failure; multi-row fix | IOP26 |
| **B — Hybrid hydro process** | 24×1/4-28 example; 1.5× hydro | WAT18 |
| **B — Proof / SRM structural std** | Hydro floors, joint testing | MSFC |
| **C — Commercial OD anchor** | Contrail 6 bolts/end on thick 152 mm case | CON152 |
| **C — Textbook chamber** | Hoop sizing context | SUT |

Full bibliographic details: **[`INDEX.md`](INDEX.md)**. BibTeX: **[`references.bib`](references.bib)**.

---

## 9. Inline citation key list

- **[HC25]** Half Cat Rocketry — pressure vessels / motor casings (bolted closures)  
- **[MIT20]** MIT Rocket Team wiki — radial bolted case design  
- **[NAK]** Nakka / Motordesign.pdf — bolted nozzle & closure joints  
- **[IOP26]** IOP *Eng. Res. Express* 2026 — SRM bolted-connection redesign  
- **[WAT18]** University of Waterloo hybrid DAC — structural + hydro  
- **[MSFC]** NASA MSFC-STD-3744 — SRM structures / hydro-proof  
- **[CON152]** Contrail Rockets 152 mm chamber & bolt packs  
- **[SUT]** Sutton & Biblarz — chamber hoop / structural background  
