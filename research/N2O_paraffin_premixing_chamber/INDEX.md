# Index: Pre-Mixing / Pre-Combustion Chamber Length for N₂O–Paraffin Hybrids

**Topic.** Selection of **pre-mixing (pre-combustion) chamber length** `L_pc` (also called `L_pre`) upstream of the solid fuel grain in hybrid rocket motors using **nitrous oxide (N₂O)** oxidizer and **paraffin-based** fuels.

**Compiled.** 2026-07-11  
**Scope.** Peer-reviewed journals (*JPP*, *Energies*, *AST*, *AKTT*), AIAA/EUCASS conference papers, theses, and textbook design rules. Local copies are under `downloads/` where legally obtainable without paywall.

**Terminology.** Literature uses *pre-combustion chamber*, *prechamber*, *pre-chamber*, *prevaporized zone*, and *pre-mixing chamber* for the head-end dump volume between the oxidizer injector and the fuel-grain entrance. This library treats them as the same geometric feature unless a source distinguishes dump recirculation from a pure prevaporization length.

**Primary design parameter:**

```text
  L_pc / D_pc     (same as L_pc / d_pc in some papers)

  L_pc  = axial length from injector exit to grain head-end
  D_pc  = prechamber diameter (often set by final grain OD)
          (written d_pc in some sources)
```

[HUM95; GON24; GON25]

---

## How to use this index

| Column | Meaning |
|--------|---------|
| **ID** | Short cite key used in `RESEARCH_BRIEF.md` |
| **Local file** | Path under `downloads/` (blank = paywalled / not downloaded) |
| **Relevance** | Why it matters for N₂O–paraffin prechamber length selection |

---

## A. Foundational design rules and vaporization theory

| ID | Citation | Format | Local file | DOI / URL | Relevance |
|----|----------|--------|------------|-----------|-----------|
| **HUM95** | Humble, R. W.; Henry, G. N.; Larson, W. J. *Space Propulsion Analysis and Design.* McGraw-Hill, 1995. | Textbook (copyrighted) | `06_Humble_1995_Lpc_Dpc_rule_of_thumb_NOTE.txt` | Library / McGraw-Hill | Widely cited **rule of thumb** `L_pc / D_pc ≈ 0.5` for hybrid prechambers [GON24; GON25]. |
| **PRI57** | Priem, R. J. “Propellant vaporization as a criterion for rocket engine design…” NACA TN 3985, 1957. | Technical note | — | [NTRS](https://ntrs.nasa.gov/citations/19930084614) | Classical single-droplet vaporization → chamber-length criterion later adapted to hybrid PCs [GON23; GON25]. |
| **SUM51** | Summerfield, M. “A Theory of Unstable Combustion in Liquid Propellant Rocket Systems.” *ARS Journal*, 21(5), 108–114, 1951. | Journal | — | [10.2514/8.4374](https://doi.org/10.2514/8.4374) | L* / feed-coupled instability foundation adapted to hybrids by Lee/Bertoldi and Gontijo [LEE20; GON25]. |
| **SUT10** | Sutton, G. P.; Biblarz, O. *Rocket Propulsion Elements*, 8th ed. Wiley, 2010. | Textbook | — | Wiley | Background on characteristic length, residence time, and combustion-chamber sizing. |

---

## B. Core length-selection methods (N₂O hybrid focus)

| ID | Citation | Format | Local file | DOI / URL | Relevance |
|----|----------|--------|------------|-----------|-----------|
| **GON25** | Gontijo, M. S.; Shynkarenko, O.; Bertoldi, A. E. M. “Droplet Vaporization/Combustion Stability-Based Design of Pre-Combustion Chambers for Hybrid Propellant Rocket Motors.” *Energies*, 18(12), 3123, 2025. | PDF (OA) | `01_Gontijo_2025_Energies_Prechamber_Vaporization.pdf` | [10.3390/en18123123](https://doi.org/10.3390/en18123123) | **Best current OA design paper:** Priem-adapted vaporization + Summerfield-type stability; validated on SARA & ULBHRE N₂O/paraffin ~1 kN motors; recommends `0.24 ≤ L_pc / d_pc ≤ 0.81` (mean near 0.5). |
| **GON23** | Gontijo, M. S.; Filho, R. B. N.; Domingos, C. H. F. L. “Design of Pre-Combustion Chambers for Hybrid Propellant Rocket Motors and Related Aspects.” AIAA 2023-2183. | Conference (paywall); abstract TXT | `10_Gontijo_2023_AIAA_2183_ABSTRACT.txt` | [10.2514/6.2023-2183](https://doi.org/10.2514/6.2023-2183) | Conference precursor to GON25; proposed `0.26 – 0.66` for complete vaporization. |
| **GON24** | Gontijo, M. S. “Investigation of the existing methods for designing pre-combustion chambers in hybrid rocket engines.” *Aerospace Technic and Technology*, 4sup1, 2024. | Abstract TXT (publisher PDF intermittent) | `02_Gontijo_2024_AKTT_Prechamber_Design_Methods_ABSTRACT.txt` | [10.32620/aktt.2024.4sup1.07](https://doi.org/10.32620/aktt.2024.4sup1.07) | Survey of seven design methods + recommended development workflow; cites `L/D = 0.5` and N₂O/paraffin oxidizer mass flux ~650 kg/(m²·s) limit. |
| **LEE20** | Lee, J.; Bertoldi, A. E. M.; Andrianov, A.; Borges, R. A.; Veras, C. A. G.; Battistini, S.; Morita, T.; Hendrick, P. “Role of Precombustion Chamber Design in Feed-System Coupled Instabilities of Hybrid Rockets.” *JPP*, 36(6), 796–805, 2020. | Abstract TXT; AAM at SHURA | `03_Lee_2020_JPP_Prechamber_Instabilities_ABSTRACT.txt` | [10.2514/1.B37706](https://doi.org/10.2514/1.B37706); [SHURA](https://shura.shu.ac.uk/27601/) | **Primary experimental N₂O evidence:** UnB exchangeable `L_pre = 56.6 – 177.6 mm` vs ULB `102.5 mm`; longer PC can stabilize; frequency correlated to `tau_pre`. |

---

## C. Direct N₂O + paraffin motors reporting prechamber geometry / role

| ID | Citation | Format | Local file | DOI / URL | Relevance |
|----|----------|--------|------------|-----------|-----------|
| **BER07** | Bertoldi, A. E. M. *Avaliação experimental da queima de parafina e óxido nitroso em motores híbridos.* M.Sc. thesis, UnB, 2007. | PDF (thesis) | `07_Bertoldi_2007_UnB_Thesis_Paraffin_N2O.pdf` | [UnB](https://repositorio.unb.br/handle/10482/2497) | Pressure-swirl + **100 mm mixing prechamber** changes regression law (`a`, `n`) vs no long prechamber—length is not ballistically neutral. |
| **ULB** | ULB team. “Regression rate study in a small Hybrid Rocket Engine using N₂O/Paraffin propellants.” EUCASS. | PDF | `05_ULB_EUCASS_Regression_N2O_Paraffin.pdf` | [EUCASS](https://www.eucass.eu/component/docindexer/?id=4050&task=download) | Prechamber described as permitting **N₂O vaporization and dissociation** before paraffin reaction; instrumentation and DeltaP guidance. |
| **EUC19** | “Numerical and Experimental Study of a 230 N Paraffin/N₂O Hybrid Rocket Motor.” EUCASS 2019-0866. | PDF | `04_EUCASS2019_0866_Paraffin_N2O_230N.pdf` | [EUCASS PDF](https://www.eucass.eu/doi/EUCASS2019-0866.pdf) | Explicit pre- and post-combustion chamber lengths in a 230 N class paraffin/N₂O design; CFD on port-diameter / head-end pressure. |
| **AND15** | Andrianov, A.; Shynkarenko, O.; Bertoldi, A. E. M.; Barcelos, M. N. D.; Veras, C. A. G. “Concept and design of the hybrid test-motor…” AIAA 2015-3941. | Conference (paywall) | — | [10.2514/6.2015-3941](https://doi.org/10.2514/6.2015-3941) | SARA decelerator hybrid test-motor (UnB) used as validation hardware in GON25. |
| **BOU17** | Bouziane, M.; Bertoldi, A. E. M.; et al. “Design and Experimental Evaluation of Liquid Oxidizer Injection System for Hybrid Rocket Motors.” EUCASS 2017-133. | PDF | `09_Bouziane_EUCASS2017_133_Injectors.pdf` | [10.13009/eucass2017-133](https://doi.org/10.13009/eucass2017-133) | Spray characterization: droplets vaporize in prechamber/port; injector sets required vaporization length. |
| **BOU19** | Bouziane, M.; Bertoldi, A. E. M.; Milova, P.; Hendrick, P.; Lefèbvre, M. “Performance comparison of oxidizer injectors in a 1-kN paraffin-fueled hybrid rocket motor.” *AST*, 89, 392–406, 2019. | Journal (paywall) | — | [10.1016/j.ast.2019.04.009](https://doi.org/10.1016/j.ast.2019.04.009) | Same-motor SH/HC/PSW/VOR comparison (N₂O/paraffin); injector choice trades regression, specific impulse, and stability—feeds PC length via SMD / `v_i`. |

---

## D. Instability, recirculation, and length trade-offs (supporting)

| ID | Citation | Format | Local file | DOI / URL | Relevance |
|----|----------|--------|------------|-----------|-----------|
| **BER18** | Bertoldi, A. E. M. *Estudo de instabilidade de combustão em motor foguete a propelente híbrido.* Ph.D. thesis, UnB, 2018. | Thesis | — | UnB repository | Doctorate underlying LEE20 / UnB instability campaigns. |
| **BER19** | Bertoldi, A. E. M.; Bouziane, M.; Lee, J.; Veras, C. A. G.; Hendrick, P.; Simone, D. “Theoretical and Experimental Study of Combustion Instability in Hybrid Rocket Motors.” EUCASS 2019-538. | Conference | — | [10.13009/EUCASS2019-538](https://doi.org/10.13009/EUCASS2019-538) | Companion instability theory/experiment for hybrid motors. |
| **LIN13** | Lin, J. L. “Hybrid rocket combustion with prevaporized zone.” *Aircraft Engineering and Aerospace Technology*, 85(5), 406–414, 2013. | Journal (paywall) | — | [10.1108/AEAT-07-2012-0106](https://doi.org/10.1108/AEAT-07-2012-0106) | Numerical study: prevaporized zone ~**24% of combustor length** maximized completeness; longer hurts reaction space. |
| **CAR09** | Carmicino, C. “Acoustics, Vortex Shedding, and Low-Frequency Dynamics Interaction in an Unstable Hybrid Rocket.” *JPP*, 25(6), 1322–1335, 2009. | Journal (paywall) | — | [10.2514/1.42869](https://doi.org/10.2514/1.42869) | Vortex shedding in **pre- and post-combustion** chambers; injector topology (axial vs radial) dominates stability. |
| **CAR06** | Carmicino, C.; Russo Sorge, A. “The Effects of Oxidizer Injector Design on Hybrid Rockets Combustion Stability.” AIAA 2006-4677. | Conference (paywall) | — | [10.2514/6.2006-4677](https://doi.org/10.2514/6.2006-4677) | Injector–stability coupling relevant when shortening PC via better atomization. |
| **WHI10** | Whitmore, S. A.; Chandler, S. N. “Engineering Model for Self-Pressurizing Saturated-N₂O-Propellant Feed Systems.” *JPP*, 26(4), 706–714, 2010. | Journal (paywall) | — | [10.2514/1.47131](https://doi.org/10.2514/1.47131) | Two-phase N₂O mass-flow model used in GON25 feed/residence-time calculations. |

---

## E. Paywalled / not locally archived (cited; obtain via library)

| ID | Citation | DOI / URL |
|----|----------|-----------|
| **GON23** | AIAA 2023-2183 (full text) | [10.2514/6.2023-2183](https://doi.org/10.2514/6.2023-2183) |
| **LEE20** | *JPP* archival PDF (AAM free at SHURA) | [10.2514/1.B37706](https://doi.org/10.2514/1.B37706) |
| **BOU19** | *Aerospace Science and Technology* 89 | [10.1016/j.ast.2019.04.009](https://doi.org/10.1016/j.ast.2019.04.009) |
| **LIN13** | *AEAT* 85(5) | [10.1108/AEAT-07-2012-0106](https://doi.org/10.1108/AEAT-07-2012-0106) |
| **CAR09** | *JPP* 25(6) | [10.2514/1.42869](https://doi.org/10.2514/1.42869) |
| **AND15** | AIAA 2015-3941 | [10.2514/6.2015-3941](https://doi.org/10.2514/6.2015-3941) |
| **HUM95** / **SUT10** | Textbooks | Library |

---

## Local download inventory

Path: `research/N2O_paraffin_premixing_chamber/downloads/`

| File | Type | Notes |
|------|------|-------|
| `01_Gontijo_2025_Energies_Prechamber_Vaporization.pdf` | PDF (OA) | Primary design algorithm + L/D window |
| `02_Gontijo_2024_AKTT_Prechamber_Design_Methods_ABSTRACT.txt` | TXT | Survey methods / workflow |
| `03_Lee_2020_JPP_Prechamber_Instabilities_ABSTRACT.txt` | TXT | Experimental `L_pre` campaign summary |
| `04_EUCASS2019_0866_Paraffin_N2O_230N.pdf` | PDF | 230 N motor pre/post chambers |
| `05_ULB_EUCASS_Regression_N2O_Paraffin.pdf` | PDF | ULB prechamber function description |
| `06_Humble_1995_Lpc_Dpc_rule_of_thumb_NOTE.txt` | TXT | `L/D ≈ 0.5` citation note |
| `07_Bertoldi_2007_UnB_Thesis_Paraffin_N2O.pdf` | PDF | 100 mm prechamber vs `a`, `n` |
| `09_Bouziane_EUCASS2017_133_Injectors.pdf` | PDF | Injector spray → vaporization length |
| `10_Gontijo_2023_AIAA_2183_ABSTRACT.txt` | TXT | Conference precursor abstract |

Companion documents in this folder:

- `RESEARCH_BRIEF.md` — technical synthesis with **inline citations**
- `references.bib` — BibTeX entries
- `sources/citation_keys.md` — short key → full citation map

---

## Recommended reading order (design engineer)

1. **HUM95** (via GON24/GON25 quotes) — know the `L/D ≈ 0.5` starting guess  
2. **GON24** — map of methods (empirical → vaporization → instability → CFD → test)  
3. **GON25** — quantitative vaporization + stability algorithm for N₂O hybrids  
4. **LEE20** — what changing `L_pre` actually did on UnB/ULB N₂O motors  
5. **BER07** + **BOU17/BOU19** — length couples to regression and injector atomization  
6. **ULB** + **EUC19** — practical motor layouts with stated prechamber roles  
7. **LIN13** / **CAR09** — completeness and vortex-shedding trade-offs if lengthening further  

---

## Quick reference: published `L_pc / D_pc` guidance

| Source | Guidance | Context |
|--------|----------|---------|
| HUM95 (via GON24/GON25) | ≈ 0.5 | Textbook rule of thumb |
| GON23 | 0.26 – 0.66 | Complete vaporization (algorithm) |
| GON25 | 0.24 – 0.81 (use ≈ 0.5 ± 0.25 only early) | Vaporization + stability, N₂O motors |
| LEE20 (geometry) | UnB `L_pre / D_pre ≈ 0.47 – 1.48` tested | `D_pre = 120 mm`; `L_pre = 56.6 – 177.6 mm` |
| LIN13 | Prevaporized zone ~24% of combustor length | Numerical completeness optimum (generic hybrid) |
