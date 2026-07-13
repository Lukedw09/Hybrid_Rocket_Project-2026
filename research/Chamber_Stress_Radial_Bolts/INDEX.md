# Index: Chamber Stress Analysis & Radial Closure Bolts

**Topic.** Structural analysis of hybrid / solid **combustion chambers** with **radially bolted** forward bulkheads and aft nozzle carriers — hoop/axial stress, bolt shear, tear-out, bearing, net-section tension — applied to this project’s **152 mm 6061-T6** tube and **45 bar** hydroproof.

**Compiled.** 2026-07-13  
**Scope.** Amateur/university rocketry design guides, peer-reviewed SRM bolted-joint case study, NASA MSFC structural standard excerpts, commercial 152 mm bolt-count anchors. Local copies under `downloads/` where obtainable.

**Primary closure force:**

```text
  F  =  P * (pi/4) * Di^2
```

At project `Di = 5.75″` and `P = 45 bar`: **`F ≈ 75.4 kN`**.  

**Project finding (see RESEARCH_BRIEF):** with `t = 0.125″` and `1/4-28` Grade 8, **`N ≥ 20` per end** for all-mode `FS ≥ 2` at 45 bar (**`N ≥ 26`** if proof = 60 bar).

---

## How to use this index

| Column | Meaning |
|--------|---------|
| **ID** | Short cite key used in `RESEARCH_BRIEF.md` |
| **Local file** | Path under `downloads/` (blank = paywalled / not downloaded) |
| **Relevance** | Why it matters for chamber stress / radial bolts |

---

## A. Bolted closure design equations (core)

| ID | Citation | Format | Local file | DOI / URL | Relevance |
|----|----------|--------|------------|-----------|-----------|
| **HC25** | Sennott, A.; Sharp, C. *How to Design Pressure Vessels, Propellant Tanks, and Rocket Motor Casings.* Half Cat Rocketry Technical Resources. | PDF | `01_HalfCat_Pressure_Vessels_Motor_Casings.pdf` | [HalfCat PDF](https://pentagon-turbot-cnlj.squarespace.com/s/How-to-Design-Pressure-Vessels-Propellant-Tanks-and-Rocket-Motor-Casings.pdf) | **Primary reference:** single-shear bolt stress, tear-out, net tension, bearing; SA Cup **1.5× MEOP** proof discussion; Appendix A worked example (12×1/4-28 on 4″ case). |
| **MIT20** | MIT Rocket Team. “Radial Bolted Case Design.” MIT Wiki Service (last meaningful edit ~2020). | Wiki / note | `07_MIT_Radial_Bolted_Case_NOTE.txt` | [MIT wiki](https://wikis.mit.edu/confluence/display/RocketTeam/Radial+Bolted+Case+Design) | Hoop / longitudinal stress; conservative tear-out area; edge-distance guidance (AISC J3.4); Phoenix dual-row example. |
| **NAK** | Motordesign article hosted on Richard Nakka’s Experimental Rocketry site (bolted nozzle / closure joints). | PDF | `02_Nakka_Motor_Design_Bolted_Joints.pdf` | [nakka-rocketry.net/articles/Motordesign.pdf](https://www.nakka-rocketry.net/articles/Motordesign.pdf) | Classical balance of bearing, plate tension, and bolt shear for aft (and forward) bolted retainers; SF ≈ 1.5 framing. |

---

## B. Case studies, hydroproof practice, standards

| ID | Citation | Format | Local file | DOI / URL | Relevance |
|----|----------|--------|------------|-----------|-----------|
| **IOP26** | “Structural design evolution of a high-power solid rocket motor for sounding rockets: a case study on bolted connections, testing, and validation.” *Engineering Research Express*, 2026. | PDF (OA) | `03_IOP_SRM_Bolted_Connections_2026.pdf` | [10.1088/2631-8695/ae7014](https://doi.org/10.1088/2631-8695/ae7014) | Documented **bolt shear failure** of forward closure (8×M5); FEA; redesign with staggered circles, **2.5d** edge distance, Class 12.9 fasteners. |
| **WAT18** | University of Waterloo IDEAs Design Analysis Competition. “Hybrid Rocket Engine” structural presentation, 2018. | PDF | `04_Waterloo_Hybrid_Structural_Analysis.pdf` | [uwaterloo.ca … presentation PDF](https://uwaterloo.ca/engineering-ideas-clinic/sites/default/files/uploads/documents/hybrid_rocket_engine_-_design_analysis_competition_presentation_1.pdf) | Hybrid chamber: **24×1/4-28**, FS table for shear/tear-out/bearing/tension; hydro to **1.5×** operating pressure. |
| **MSFC** | NASA Marshall Space Flight Center. *MSFC-STD-3744* — Solid Rocket Motor Structures / related structural requirements (hydro-proof language). | PDF | `05_MSFC_STD_3744_SRM_Structures.pdf` | [standards.nasa.gov … msfc-std-3744.pdf](https://standards.nasa.gov/sites/default/files/standards/MSFC/Baseline/0/msfc-std-3744.pdf) | Aerospace hydro-proof floors (e.g. **≥1.05× MEOP** acceptance language), joint testing context — contrast with amateur **1.5×** practice. |

---

## C. Commercial / material / project calculation anchors

| ID | Citation | Format | Local file | DOI / URL | Relevance |
|----|----------|--------|------------|-----------|-----------|
| **CON152** | Contrail Rockets — 152 mm combustion chamber & bolt packs (product pages). | Vendor note | `08_Contrail_152mm_Bolt_Count_NOTE.txt` | [Chamber](https://contrailrockets.com/product/152mm-26-inch-combustion-chamber) · [12-pack bolts](https://contrailrockets.com/product/152mm-combustion-chamber-bolts) | **6 bolts/end** on thick certified case — OD reference only; not transferable to 0.125″ custom tube. |
| **MAT** | 6061-T6 allowables as used in HalfCat FS tables (+ Grade 8 shear rule). | Note | `09_6061T6_Strength_Values_NOTE.txt` | (from HC25) | YTS 38 ksi, shear 30 ksi, BYS 56 ksi @ ~200 °F; bolt shear = 0.75×UTS. |
| **CALC** | Project bolt-count script for `Di=5.75″`, `t=0.125″`, 1/4-28 Gr8. | Python | `06_project_bolt_count_calc.py` | (local) | Reproduces RESEARCH_BRIEF FS tables at 40 / 45 / 60 bar. |
| **SUT** | Sutton, G. P.; Biblarz, O. *Rocket Propulsion Elements* (chamber hoop / structural background). | Textbook | — | Wiley | Barrel hoop sizing context already used in project chamber wall policy. |

---

## Local download inventory

Path: `research/Chamber_Stress_Radial_Bolts/downloads/`

| File | Type | Notes |
|------|------|-------|
| `01_HalfCat_Pressure_Vessels_Motor_Casings.pdf` | PDF | Full bolted-closure chapter + Appendix A |
| `02_Nakka_Motor_Design_Bolted_Joints.pdf` | PDF | Bolted nozzle / retainer theory |
| `03_IOP_SRM_Bolted_Connections_2026.pdf` | PDF (OA) | Failure investigation + multi-row redesign |
| `04_Waterloo_Hybrid_Structural_Analysis.pdf` | PDF | Hybrid FS + 1.5× hydro example |
| `05_MSFC_STD_3744_SRM_Structures.pdf` | PDF | NASA SRM structural / proof language |
| `06_project_bolt_count_calc.py` | PY | Project-specific FS calculator |
| `07_MIT_Radial_Bolted_Case_NOTE.txt` | TXT | Captured wiki equations |
| `08_Contrail_152mm_Bolt_Count_NOTE.txt` | TXT | 6 bolts/end commercial anchor |
| `09_6061T6_Strength_Values_NOTE.txt` | TXT | Allowables used in tables |

Companion documents in this folder:

- `RESEARCH_BRIEF.md` — synthesis + **bolt-count recommendations**
- `references.bib` — BibTeX entries
- `sources/citation_keys.md` — short key → full citation map

---

## Recommended reading order (design engineer)

1. **HC25** §§ thin-wall + bolted closures + Appendix A — learn the four modes  
2. **RESEARCH_BRIEF §5** — apply to *this* 152 mm / 45 bar geometry  
3. **CALC** — change `N`, bolt size, or proof pressure and re-check  
4. **IOP26** — why under-bolted Al cases fail; when to add a second circle  
5. **MIT20** / **NAK** — tear-out & classical joint balance  
6. **WAT18** — hydroproof process template  
7. **CON152** — only after you understand why 6≠20 on a thin wall  
8. **MSFC** — if comparing amateur 1.5× proof to aerospace floors  

---

## Quick reference: project recommendation

| End | Hydro pressure | Minimum radial fasteners (1/4-28 Gr8, E=2d, t=0.125″) |
|-----|----------------|------------------------------------------------------|
| Forward bulkhead | **45 bar** | **≥ 20** |
| Aft nozzle carrier | **45 bar** | **≥ 20** |
| Either end (design for project 1.5× MEOP) | **60 bar** | **≥ 26** |

Limiting mode: **casing bearing**. Barrel hoop alone is **not** limiting at these pressures.
