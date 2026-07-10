# Index: N₂O–Paraffin Hybrid Rocket Burn / Regression Rate Literature

**Topic.** Variation of solid-fuel regression rate (burn rate) in hybrid rocket motors using nitrous oxide (N₂O) oxidizer and paraffin-based fuels.

**Compiled.** 2026-07-10  
**Scope.** Peer-reviewed journals, conference papers (AIAA, EUCASS, COBEM), theses, open-access chapters, patents, and secondary reference pages. Local copies are under `downloads/` where legally obtainable without paywall.

**Primary correlation form used throughout the literature:**

\[
\dot{r} = a\, G_{\mathrm{ox}}^{n}
\]

where \(\dot{r}\) is space–time-averaged regression rate, \(G_{\mathrm{ox}}\) is oxidizer mass flux, and \(a,n\) are empirical constants for a given propellant pair, injector, and averaging method ([Karabeyoglu et al., 2004](https://doi.org/10.2514/1.3340); [Karabeyoglu et al., 2007](https://doi.org/10.2514/1.19226)).

---

## How to use this index

| Column | Meaning |
|--------|---------|
| **ID** | Short cite key used in `RESEARCH_BRIEF.md` |
| **Local file** | Path under `downloads/` (blank = paywalled / not downloaded) |
| **Relevance** | Why it matters for N₂O–paraffin burn-rate variation |

---

## A. Foundational theory (liquefying / entrainment fuels)

| ID | Citation | Format | Local file | DOI / URL | Relevance |
|----|----------|--------|------------|-----------|-----------|
| **KAC02** | Karabeyoglu, M. A.; Altman, D.; Cantwell, B. J. “Combustion of Liquefying Hybrid Propellants: Part 1, General Theory.” *Journal of Propulsion and Power*, 18(3), 610–620, 2002. | PDF (open Stanford mirror) | `12_Karabeyoglu_2002_Liquefying_Part1_Theory.pdf` | [10.2514/2.5975](https://doi.org/10.2514/2.5975) | Establishes melt-layer hydrodynamic instability and droplet entrainment as the mechanism that raises paraffin regression rates ~3–4× vs HTPB. |
| **KAC02b** | Karabeyoglu, M. A.; Cantwell, B. J. “Combustion of Liquefying Hybrid Propellants: Part 2, Stability of Liquid Films.” *JPP*, 18(3), 621–630, 2002. | Journal (paywall) | — | [10.2514/2.5976](https://doi.org/10.2514/2.5976) | Film stability / entrainment criteria (viscosity, surface tension). |
| **PAT03** | Karabeyoglu, M. A. et al. “High Regression Rate Hybrid Rocket Propellants and Method of Selecting.” U.S. Patent Appl. US2003/0098107. | HTML/TXT | `16_Karabeyoglu_Patent_US20030098107.txt` | [freepatentsonline](https://www.freepatentsonline.com/y2003/0098107.html) | Patent disclosure of liquefying-fuel selection and predicted 3–5× regression vs classical fuels. |

---

## B. Scale-up and scalable averaging (paraffin; GOX primary, N₂O context)

| ID | Citation | Format | Local file | DOI / URL | Relevance |
|----|----------|--------|------------|-----------|-----------|
| **KZC03** | Karabeyoglu, A.; Zilliac, G.; Cantwell, B.; De Zilwa, S.; Castellucci, P. “Scale-up Tests of High Regression Rate Liquefying Hybrid Rocket Fuels.” AIAA 2003-1162. | PDF | `01_Karabeyoglu_2003_Scaleup_Paraffin_AIAA-2003-1162.pdf` | [10.2514/6.2003-1162](https://doi.org/10.2514/6.2003-1162) | Classic SP-1a law \(\dot{r}=0.488\,G_{\mathrm{ox}}^{0.62}\) (mm/s, \(G\) in g/cm²·s) for paraffin/GOX; framework reused for N₂O motors. |
| **KZC04** | Karabeyoglu, A.; Zilliac, G.; Cantwell, B.; DeZilwa, S.; Castellucci, P. “Scale-Up Tests of High Regression Rate Paraffin-Based Hybrid Rocket Fuels.” *JPP*, 20(6), 1037–1045, 2004. | PDF | `13_Karabeyoglu_2004_Scaleup_JPP.pdf` | [10.2514/1.3340](https://doi.org/10.2514/1.3340) | Archival journal version; confirms weak length/pressure dependence and 3–4× HTPB rates at operational fluxes. |
| **KCZ07** | Karabeyoglu, M. A.; Cantwell, B. J.; Zilliac, G. “Development of Scalable Space-Time Averaged Regression Rate Expressions for Hybrid Rockets.” *JPP*, 23(4), 737–747, 2007. | PDF | `02_Karabeyoglu_2007_Scalable_Regression_Rate_JPP.pdf` | [10.2514/1.19226](https://doi.org/10.2514/1.19226) | Correct averaging of \(\dot{r}\) and \(G\); essential when comparing N₂O–paraffin datasets across scales. |

---

## C. Direct N₂O + paraffin experimental characterization (core set)

| ID | Citation | Format | Local file | DOI / URL | Relevance |
|----|----------|--------|------------|-----------|-----------|
| **BV05** | Bertoldi, A. E. M.; Veras, C. A. G. “Experimental Evaluation of Paraffin–Nitrous Oxide Hybrid Rocket Motors.” COBEM 2005, Paper COBEM2005-2529. | PDF | `03_Bertoldi_Veras_2005_COBEM_Paraffin_N2O.pdf` | [ABCM](https://abcm.org.br/anais/cobem/2005/PDF/COBEM2005-2529.pdf) | Early UnB 500 N motor: paraffin/N₂O rates up to ~4.5 mm/s; notes difficulty fitting \(a,n\) without accurate \(G_{\mathrm{ox}}\). |
| **BER07** | Bertoldi, A. E. M. *Avaliação experimental da queima de parafina e óxido nitroso em motores híbridos.* M.Sc. thesis, Universidade de Brasília, 2007. | PDF (thesis) | `04_Bertoldi_2007_UnB_Thesis_Paraffin_N2O.pdf` | [UnB repository](https://repositorio.unb.br/handle/10482/2497) | **Primary N₂O–paraffin laws:** pressure-swirl \(\dot{r}=0.7197\,G^{0.67}\); with prechamber \(\dot{r}=1.2301\,G^{0.47}\) (\(G\) in g/cm²·s, \(\dot{r}\) in mm/s). Swirl injectors → rates >9 mm/s at ~150 g/cm²·s. |
| **ULB** | Université Libre de Bruxelles team. “Regression rate study in a small Hybrid Rocket Engine using N₂O/Paraffin propellants.” EUCASS paper. | PDF | `06_ULB_EUCASS_Regression_N2O_Paraffin.pdf` | [EUCASS download](https://www.eucass.eu/component/docindexer/?id=4050&task=download) | Mean \(\dot{r}\approx 4\)–\(5\) mm/s for pure paraffin/N₂O; higher than some prior N₂O–paraffin literature (~3 mm/s) and comparable to Stanford SP-1a/GOX. |
| **CAR13** | Scaramuzzino, F.; Carmicino, C.; Festa, G.; Viviani, A.; Russo Sorge, A. “Fuel regression-rate characterization on a lab-scale hybrid rocket burning N₂O and paraffin-based propellants.” AIAA 2013-4039. | Conference (paywall) | — | [10.2514/6.2013-4039](https://doi.org/10.2514/6.2013-4039) | Lab-scale GN₂O with HTPB, Al-HTPB, and paraffin; paraffin gives the largest regression gain; scale effects examined. |
| **CAR_EUC** | Carmicino, C. et al. “Paraffin-based and metal-loaded HTPB fuel regression rates study in a lab-scale hybrid rocket fed with N₂O.” EUCASS. | PDF | `07_Carmicino_EUCASS_Paraffin_HTPB_N2O.pdf` | [EUCASS](https://www.eucass.eu/component/docindexer/?id=4157&task=download) | Open companion to CAR13: Al-HTPB ~+25% at 100 kg/m²·s; paraffin larger gain; manufacturing strongly affects paraffin results. |
| **CAR14** | Carmicino, C.; Scaramuzzino, F.; Russo Sorge, A. “Trade-off between paraffin-based and aluminium-loaded HTPB fuels to improve performance of hybrid rocket fed with N₂O.” *Aerospace Science and Technology*, 37, 81–92, 2014. | Journal (paywall) | — | [10.1016/j.ast.2014.05.010](https://doi.org/10.1016/j.ast.2014.05.010) | Archival trade-off study: paraffin vs Al-HTPB with N₂O. |
| **GRO09** | Grosse, M. “Effect of a Diaphragm on Performance and Fuel Regression of a Laboratory Scale Hybrid Rocket Motor Using Nitrous Oxide and Paraffin.” AIAA 2009-5113. | Conference (paywall) | — | [10.2514/6.2009-5113](https://doi.org/10.2514/6.2009-5113) | Liquid N₂O + microcrystalline paraffin; diaphragm raises local \(\dot{r}\) ~40–80% downstream; \(I_{\mathrm{sp}}\) gain ~12%. |
| **MOR** | Moreira, J. “Design, testing and analysis of a N₂O/paraffin wax hybrid rocket combustion system…” Extended abstract, Instituto Superior Técnico. | PDF | `08_Moreira_IST_N2O_Paraffin_Slab_Burner.pdf` | [IST](https://fenix.tecnico.ulisboa.pt/downloadFile/1407770020547671/JOAOMOREIRA_EXTENDED_ABSTRACT.pdf) | Optical slab burner: local \(\dot{r}\) vs axial position; **weak flux dependence** at 5–15 kg/(m²·s); liquid layer visualized. |
| **EUC19** | “Numerical and Experimental Study of a 230 N Paraffin/N₂O Hybrid Rocket Motor.” EUCASS 2019-0866. | PDF | `05_EUCASS2019_0866_Paraffin_N2O_230N.pdf` | [EUCASS PDF](https://www.eucass.eu/doi/EUCASS2019-0866.pdf) | 230 N class motor; cites paraffin 3–4× HTPB and rates up to ~4.7 mm/s; CFD + experiment on port-diameter effects. |

---

## D. Injection, mixing devices, and additives (N₂O–paraffin or closely related)

| ID | Citation | Format | Local file | DOI / URL | Relevance |
|----|----------|--------|------------|-----------|-----------|
| **BEL12n** | Bellomo, N. et al. “The ‘Vortex Reloaded’ project: numerical investigation on fully tangential vortex injection in N₂O–paraffin hybrid motors.” AIAA 2012-3903. | Conference (paywall) | — | [10.2514/6.2012-3903](https://doi.org/10.2514/6.2012-3903) | Vortex injection CFD for N₂O–paraffin. |
| **BEL12e** | Bellomo, N. et al. “The ‘Vortex Reloaded’ project: experimental investigation…” AIAA 2012-4304. | Conference (paywall) | — | [10.2514/6.2012-4304](https://doi.org/10.2514/6.2012-4304) | Experimental vortex injection; regression/efficiency effects. |
| **BOR11** | Boronowsky, K. *Non-homogeneous Hybrid Rocket Fuel for Enhanced Regression Rates Utilizing Partial Entrainment.* M.S. thesis, San José State University, 2011. | PDF | `10_Boronowsky_SJSU_Partial_Entrainment_Thesis.pdf` | [SJSU ScholarWorks](https://scholarworks.sjsu.edu/etd_theses/4036/) | Paraffin nodules in HTPB; documents entrainment concept and 3–4× paraffin advantage (GOX tests; mechanism transferable). |
| **INT11** | Dziubinski, A. (ed. context) / InTech chapter material on hybrid propulsion citing N₂O ballistic tables and paraffin. | PDF (OA chapter) | `22_InTech_Hybrid_Rocket_Propulsion_chapter.pdf` | [InTech](https://cdn.intechopen.com/pdfs/18671.pdf) | Survey tables of N₂O polymer ballistic coefficients; paraffin as liquefying high-\(\dot{r}\) option. |

---

## E. Numerical / CFD studies including N₂O–paraffin

| ID | Citation | Format | Local file | DOI / URL | Relevance |
|----|----------|--------|------------|-----------|-----------|
| **CFD21** | CFD Letters article comparing GOX/paraffin vs N₂O/paraffin regression via ANSYS. | PDF | `09_CFD_Letters_GOX_N2O_Paraffin_Regression.pdf` | [Semarak Ilmu](https://semarakilmu.com.my/journals/index.php/CFD_Letters/article/download/461/558/4791) | Numerical \(\dot{r}\) up to ~1.8 mm/s (GOX/P) vs ~1.2 mm/s (N₂O/P) in studied cases; flux and BC sensitivity. |
| **ACT20** | “Numerical simulation of low-melting temperature solid fuel regression in hybrid rocket engines.” *Acta Astronautica*, 2020. | Abstract TXT | `15_Acta_Astronautica_2020_LowMelting_abstract.txt` | [10.1016/j.actaastro.2020.05.001](https://doi.org/10.1016/j.actaastro.2020.05.001) | CFD of paraffin + gaseous N₂O melt-layer regression (full text paywalled). |

---

## F. Supporting N₂O hybrid regression baselines (non-paraffin fuels)

| ID | Citation | Format | Local file | DOI / URL | Relevance |
|----|----------|--------|------------|-----------|-----------|
| **LOH06** | Lohner, K.; Dyer, J.; Doran, E.; Dunn, Z.; Zilliac, G. “Fuel Regression Rate Characterization Using a Laboratory Scale Nitrous Oxide Hybrid Propulsion System.” AIAA 2006-4671. | Conference (paywall) | — | [10.2514/6.2006-4671](https://doi.org/10.2514/6.2006-4671) | HTPB/PMMA/HDPE/sorbitol with N₂O; ULB cites HTPB/N₂O ~1 mm/s as baseline vs paraffin ~5 mm/s. |
| **WIKI** | “Hybrid rocket fuel regression.” *Wikipedia*. | HTML | `17_Wikipedia_Hybrid_rocket_fuel_regression.html` | [Wikipedia](https://en.wikipedia.org/wiki/Hybrid_rocket_fuel_regression) | Secondary table of \(a,n\) including N₂O/HTPB; use only as a pointer to primary sources. |

---

## G. Paywalled / not locally archived (cited; obtain via library)

| ID | Citation | DOI |
|----|----------|-----|
| **CAR14** | Carmicino et al., *Aerospace Science and Technology* 37 (2014) | [10.1016/j.ast.2014.05.010](https://doi.org/10.1016/j.ast.2014.05.010) |
| **CAR13** | AIAA 2013-4039 | [10.2514/6.2013-4039](https://doi.org/10.2514/6.2013-4039) |
| **GRO09** | AIAA 2009-5113 | [10.2514/6.2009-5113](https://doi.org/10.2514/6.2009-5113) |
| **LOH06** | AIAA 2006-4671 | [10.2514/6.2006-4671](https://doi.org/10.2514/6.2006-4671) |
| **BEL12n/e** | AIAA 2012-3903 / 2012-4304 | see Section D |
| **ACT20** | *Acta Astronautica* full text | [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0094576520302861) |
| **PREP20** | “Regression Rate Characterization of HTPB‐Paraffin Based Solid Fuels…” *Propellants Explos. Pyrotech.* | [10.1002/prep.202000051](https://doi.org/10.1002/prep.202000051) |
| **B37017** | “Two-Hundred-Newton Laboratory-Scale Hybrid Rocket Testing for Paraffin Fuel-Performance Characterization.” *JPP* | [10.2514/1.B37017](https://doi.org/10.2514/1.B37017) |

---

## Local download inventory

Path: `research/N2O_paraffin_burn_rate/downloads/`

| File | Type | Approx. size |
|------|------|--------------|
| `01_Karabeyoglu_2003_Scaleup_Paraffin_AIAA-2003-1162.pdf` | PDF | 2.0 MB |
| `02_Karabeyoglu_2007_Scalable_Regression_Rate_JPP.pdf` | PDF | 0.4 MB |
| `03_Bertoldi_Veras_2005_COBEM_Paraffin_N2O.pdf` | PDF | 1.2 MB |
| `04_Bertoldi_2007_UnB_Thesis_Paraffin_N2O.pdf` | PDF | 2.1 MB |
| `05_EUCASS2019_0866_Paraffin_N2O_230N.pdf` | PDF | 1.5 MB |
| `06_ULB_EUCASS_Regression_N2O_Paraffin.pdf` | PDF | 0.7 MB |
| `07_Carmicino_EUCASS_Paraffin_HTPB_N2O.pdf` | PDF | 1.1 MB |
| `08_Moreira_IST_N2O_Paraffin_Slab_Burner.pdf` | PDF | 2.8 MB |
| `09_CFD_Letters_GOX_N2O_Paraffin_Regression.pdf` | PDF | 1.4 MB |
| `10_Boronowsky_SJSU_Partial_Entrainment_Thesis.pdf` | PDF | 3.0 MB |
| `12_Karabeyoglu_2002_Liquefying_Part1_Theory.pdf` | PDF | 0.3 MB |
| `13_Karabeyoglu_2004_Scaleup_JPP.pdf` | PDF | 0.7 MB |
| `15_Acta_Astronautica_2020_LowMelting_abstract.txt` | TXT | abstract |
| `16_Karabeyoglu_Patent_US20030098107.txt` | TXT | patent text |
| `17_Wikipedia_Hybrid_rocket_fuel_regression.html` | HTML | secondary |
| `22_InTech_Hybrid_Rocket_Propulsion_chapter.pdf` | PDF | 0.6 MB |

Companion documents in this folder:

- `RESEARCH_BRIEF.md` — technical synthesis with **inline citations**
- `REGRESSION_CONSTANT_CLARIFICATION.md` — project uses Bertoldi pressure-swirl `a=0.1531`, `n=0.67` (SI); unit conversion
- `EXPERIMENTAL_MEASUREMENT_OF_A_AND_N.md` — lab procedure to measure `a` and `n` from hot-fire data
- `references.bib` — BibTeX entries for the sources above
- `sources/citation_keys.md` — short key → full citation map

---

## Recommended reading order (design engineer)

1. **KAC02** — understand *why* paraffin burns fast  
2. **KZC04** / **KCZ07** — how to average and scale \(\dot{r}(G)\)  
3. **BER07** — N₂O–paraffin \(a,n\) and injector effects (best open experimental law set)  
4. **CAR_EUC** / **CAR14** — paraffin vs Al-HTPB with N₂O  
5. **GRO09** — diaphragm / mixing-device \(\dot{r}\) variation  
6. **MOR** — spatial variation and weak flux dependence at low \(G\)  
7. **ULB** + **EUC19** — independent lab confirmation of multi-mm/s rates  

---

## Notes on units (critical for design)

| Source | \(a\) | \(n\) | \(G_{\mathrm{ox}}\) units | \(\dot{r}\) units |
|--------|-------|-------|---------------------------|-------------------|
| KZC03 SP-1a / GOX | 0.488 | 0.62 | g/(cm²·s) | mm/s |
| BER07 pressure-swirl / N₂O | 0.7197 | 0.67 | g/(cm²·s) | mm/s |
| BER07 same, SI flux | 0.1531 | 0.67 | kg/(m²·s) | mm/s |
| BER07 + prechamber / N₂O | 1.2301 | 0.47 | g/(cm²·s) | mm/s |
| This repo `model.py` | **0.1531** | **0.67** | kg/(m²·s) | mm/s |

**Unit check:** \(1\,\mathrm{g\,cm^{-2}\,s^{-1}} = 10\,\mathrm{kg\,m^{-2}\,s^{-1}}\). Converting BER07’s \(a=0.7197\) from cgs flux to SI flux yields \(a\approx 0.153\) mm/s·(kg/m²·s)\(^{-n}\), which is what `model.py` uses. See `REGRESSION_CONSTANT_CLARIFICATION.md` and `EXPERIMENTAL_MEASUREMENT_OF_A_AND_N.md`.
