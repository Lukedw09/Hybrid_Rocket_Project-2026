# Index: Axial Showerhead Injector Plate Design for Hybrid Rockets

**Topic.** Design of **axial showerhead (SH) oxidizer injector plates** for hybrid rocket motors — orifice sizing, discharge coefficient, atomization criteria, faceplate layout, and coupling to prechamber / stability — with emphasis on **liquid nitrous oxide (N₂O) + paraffin**.

**Compiled.** 2026-07-11  
**Scope.** Peer-reviewed journals (*FirePhysChem*, *AST*, *JPP*), EUCASS / DLRK conference papers, and textbook pressure-drop practice. Local copies are under `downloads/` where legally obtainable.

**Primary design equation:**

```text
  m_dot_ox  =  Cd * N * A_inj * sqrt( 2 * rho_ox * DeltaP )

  DeltaP / P_c  ≈  0.20 – 0.30     (typical hybrid practice)
```

[BOU17; BOU19E; HUM95; ULB]

---

## How to use this index

| Column | Meaning |
|--------|---------|
| **ID** | Short cite key used in `RESEARCH_BRIEF.md` |
| **Local file** | Path under `downloads/` (blank = paywalled / not downloaded) |
| **Relevance** | Why it matters for axial showerhead design |

---

## A. Core showerhead design and experiment (N₂O / paraffin)

| ID | Citation | Format | Local file | DOI / URL | Relevance |
|----|----------|--------|------------|-----------|-----------|
| **BOU17** | Bouziane, M.; Bertoldi, A. E. M.; et al. “Design and Experimental Evaluation of Liquid Oxidizer Injection System for Hybrid Rocket Motors.” EUCASS 2017-133. | PDF | `01_Bouziane_2017_EUCASS_Injectors.pdf` | [10.13009/eucass2017-133](https://doi.org/10.13009/eucass2017-133) | Cold-flow design of SH baseline (11 × 1.4 mm, `L = 7` mm); orifice mass-flow equation; water/`Cd` vs N₂O spray; comparison to HC/PSW/VOR. |
| **BOU19E** | Bouziane, M.; Bertoldi, A. E. M.; Milova, P.; Hendrick, P.; Lefèbvre, M. “Experimental Investigation of Showerhead Injectors on Performance of a 1-kN Paraffin-Fueled Hybrid Rocket Motor.” EUCASS 2019-473. | PDF | `03_Bouziane_2019_EUCASS_473_Showerhead.pdf` | [10.13009/EUCASS2019-473](https://doi.org/10.13009/EUCASS2019-473) | Hot-fire SH1–SH4; N₂O `Cd ≈ 0.32`; SMD vs `d_inj`; **~5%** regression gain for smallest orifices (SH4). |
| **BOU21** | Bouziane, M.; Bertoldi, A. E. M.; Hendrick, P.; Lefèbvre, M. “Experimental investigation of the axial oxidizer injectors geometry on a 1-kN paraffin-fueled hybrid rocket motor.” *FirePhysChem*, 1, 231–243, 2021. | PDF (OA) | `02_Bouziane_2021_FirePhysChem_Axial_SH.pdf` | [10.1016/j.fpc.2021.11.012](https://doi.org/10.1016/j.fpc.2021.11.012); [UnB](https://repositorio.unb.br/bitstream/10482/43599/1/ARTIGO_ExperimentalInvestigationAxial.pdf) | **Best single archival paper:** Re/Oh/We criteria, SMD table, port–orifice alignment fractions, regression law for SH4 family. |
| **BOU19A** | Bouziane, M.; Bertoldi, A. E. M.; Milova, P.; Hendrick, P.; Lefèbvre, M. “Performance comparison of oxidizer injectors in a 1-kN paraffin-fueled hybrid rocket motor.” *Aerospace Science and Technology*, 89, 392–406, 2019. | Journal (paywall) | — | [10.1016/j.ast.2019.04.009](https://doi.org/10.1016/j.ast.2019.04.009) | Same-motor SH vs hollow-cone / pressure-swirl / vortex — places showerhead in the injector trade space. |

---

## B. Atomization criteria and textbook pressure drop

| ID | Citation | Format | Local file | DOI / URL | Relevance |
|----|----------|--------|------------|-----------|-----------|
| **GAM13** | Gamper, E.; Hink, R. “Design and Test of Nitrous Oxide Injectors for a Hybrid Rocket Engine.” Deutscher Luft- und Raumfahrtkongress, 2013. | PDF | `04_Gamper_Hink_2013_N2O_Injectors.pdf` | [DGLR](https://www.dglr.de/publikationen/2013/301266.pdf) | Source of Bouziane’s **`Re > 2300`**, **`We > 50`**, Ohnesorge–Reynolds atomization map; orifice layout vs propellant grain shape. |
| **HUM95** | Humble, R. W.; Henry, G. N.; Larson, W. J. *Space Propulsion Analysis and Design.* McGraw-Hill, 1995. | Textbook (copyrighted) | `05_Humble_Sutton_DeltaP_NOTE.txt` | Library / McGraw-Hill | Widely cited hybrid practice: injector **`DeltaP / P_c ≈ 20–30%`**. |
| **SUT10** | Sutton, G. P.; Biblarz, O. *Rocket Propulsion Elements*, 8th ed. Wiley, 2010. | Textbook | (same note) | Wiley | Background on injectors, chamber pressure, and combustion efficiency. |
| **TAN55** | Tanasawa, Y.; Toyoda, S. “On the Atomization of a Liquid Jet Issuing from a Cylindrical Nozzle.” *Tech. Rep. Tohoku Univ.*, 1955. | Classic correlation | — | Library / as cited in BOU21 | Plain-orifice **SMD** formula used for ULB showerheads. |

---

## C. System coupling — prechamber, feed, stability

| ID | Citation | Format | Local file | DOI / URL | Relevance |
|----|----------|--------|------------|-----------|-----------|
| **GON25** | Gontijo, M. S.; Shynkarenko, O.; Bertoldi, A. E. M. “Droplet Vaporization/Combustion Stability-Based Design of Pre-Combustion Chambers…” *Energies*, 18(12), 3123, 2025. | OA PDF in sister library | See `../N2O_paraffin_premixing_chamber/downloads/` | [10.3390/en18123123](https://doi.org/10.3390/en18123123) | Injector SMD and `DeltaP` **set** required prechamber length; `DeltaP ~ 20–30% P_c`. |
| **GON24** | Gontijo, M. S. “Investigation of the existing methods for designing pre-combustion chambers…” *AKTT*, 2024. | Abstract in sister library | — | [10.32620/aktt.2024.4sup1.07](https://doi.org/10.32620/aktt.2024.4sup1.07) | Droplet Weber / collision outcomes vs injector `DeltaP`. |
| **LEE20** | Lee, J.; et al. “Role of Precombustion Chamber Design in Feed-System Coupled Instabilities of Hybrid Rockets.” *JPP*, 36(6), 796–805, 2020. | Abstract in sister library | — | [10.2514/1.B37706](https://doi.org/10.2514/1.B37706) | Injection velocity + `L_pre` control FSC oscillation period. |
| **ULB** | ULB team. “Regression rate study in a small Hybrid Rocket Engine using N₂O/Paraffin propellants.” EUCASS. | PDF in sister library | — | [EUCASS](https://www.eucass.eu/component/docindexer/?id=4050&task=download) | Prechamber vaporization role; **≥20%** injector `DeltaP` vs `P_c`. |
| **WHI10** | Whitmore, S. A.; Chandler, S. N. “Engineering Model for Self-Pressurizing Saturated-N₂O-Propellant Feed Systems.” *JPP*, 26(4), 706–714, 2010. | Journal (paywall) | — | [10.2514/1.47131](https://doi.org/10.2514/1.47131) | Two-phase N₂O feed / density state for `m_dot_ox` and flashing injectors. |
| **CAR06** | Carmicino, C.; Russo Sorge, A. “The Effects of Oxidizer Injector Design on Hybrid Rockets Combustion Stability.” AIAA 2006-4677. | Conference (paywall) | — | [10.2514/6.2006-4677](https://doi.org/10.2514/6.2006-4677) | Injector design ↔ hybrid combustion stability. |
| **CAR09** | Carmicino, C. “Acoustics, Vortex Shedding, and Low-Frequency Dynamics Interaction in an Unstable Hybrid Rocket.” *JPP*, 25(6), 1322–1335, 2009. | Journal (paywall) | — | [10.2514/1.42869](https://doi.org/10.2514/1.42869) | Axial vs radial injector topology and head-end vortex coupling. |

---

## D. Paywalled / obtain via library (cited; full text not always local)

| ID | Citation | DOI / URL |
|----|----------|-----------|
| **BOU19A** | *AST* 89 (2019) | [10.1016/j.ast.2019.04.009](https://doi.org/10.1016/j.ast.2019.04.009) |
| **LEE20** | *JPP* 36(6) | [10.2514/1.B37706](https://doi.org/10.2514/1.B37706) |
| **CAR09** | *JPP* 25(6) | [10.2514/1.42869](https://doi.org/10.2514/1.42869) |
| **WHI10** | *JPP* 26(4) | [10.2514/1.47131](https://doi.org/10.2514/1.47131) |
| **HUM95** / **SUT10** | Textbooks | Library |

---

## Local download inventory

Path: `research/Axial_Showerhead_Injector/downloads/`

| File | Type | Notes |
|------|------|-------|
| `01_Bouziane_2017_EUCASS_Injectors.pdf` | PDF | Cold-flow SH + Cd + spray |
| `02_Bouziane_2021_FirePhysChem_Axial_SH.pdf` | PDF (OA) | Archival axial-SH hot-fire study |
| `03_Bouziane_2019_EUCASS_473_Showerhead.pdf` | PDF | EUCASS showerhead orifice campaign |
| `04_Gamper_Hink_2013_N2O_Injectors.pdf` | PDF | Re / Oh / We design guidance |
| `05_Humble_Sutton_DeltaP_NOTE.txt` | TXT | `DeltaP / P_c ≈ 20–30%` citation note |

Companion documents in this folder:

- `RESEARCH_BRIEF.md` — technical synthesis with **inline citations**
- `references.bib` — BibTeX entries
- `sources/citation_keys.md` — short key → full citation map

---

## Recommended reading order (design engineer)

1. **BOU21** — full axial-SH geometry story (equations + tables + port alignment)  
2. **BOU17** — how to cold-flow calibrate `Cd` and visualize N₂O jets  
3. **BOU19E** — orifice-diameter parametric hot-fire results  
4. **GAM13** — Re / We / Oh atomization gates before machining  
5. **BOU19A** — when to leave showerhead for swirl/vortex  
6. **GON25** + **LEE20** + **ULB** — close `DeltaP` and prechamber length with the plate  
7. **CAR06** / **CAR09** — if low-frequency stability appears after the plate is “correct”  

---

## Quick reference: ULB showerhead family (paraffin / N₂O, ~1 kN)

| ID | `d_inj` | `N` | Design `m_dot_ox` | Notes |
|----|---------|-----|-------------------|--------|
| SH1 | 1.4 mm | 11 | ~400 g/s | Benchmark; water design `Cd = 0.6`, N₂O `Cd ≈ 0.32` |
| SH2 | 1.9 mm | 11 | 550 g/s | Coarsest SMD |
| SH3 | 1.4 mm | 21 | 550 g/s | Similar overall performance to SH2 |
| SH4 | 0.8 mm | 71 | 550 g/s | Finest SMD; ~5% higher `r_dot`; preferred for port study |

Design `DeltaP = 25` bar; feed tank ~60 bar; `L_inj = 7` mm on SH1 [BOU17; BOU19E; BOU21].
