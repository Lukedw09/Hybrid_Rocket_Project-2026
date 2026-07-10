# Research Brief: Burn-Rate Variation in N₂O–Paraffin Hybrid Rockets

**Author role.** Propulsion research synthesis for hybrid motor design.  
**Companion index.** [`INDEX.md`](INDEX.md) — full bibliographic inventory and local file map.  
**Date.** 2026-07-10

---

## 1. Executive finding

In N₂O–paraffin hybrids, **fuel regression rate \(\dot{r}\) is not a fixed “burn rate.”** It varies primarily with **oxidizer mass flux** \(G_{\mathrm{ox}}\), and secondarily with **injector topology**, **mixing devices**, **grain length / port diameter**, **fuel formulation / manufacturing**, and (weakly) **chamber pressure** [KAC02; KZC04; BER07; CAR_EUC; GRO09; MOR]. Measured space–time-averaged rates for paraffin with N₂O typically fall in the **~2–5 mm/s** band at moderate fluxes, with **>9 mm/s** reported under high-flux swirl injection [BER07; ULB; BV05]. That is roughly **3–5×** classical HTPB/N₂O rates (~1 mm/s class) [ULB; LOH06].

The governing design correlation remains Marxman-derived power law form:

\[
\dot{r} = a\, G_{\mathrm{ox}}^{n}
\]

with \(a,n\) **propellant- and hardware-specific** [KZC04; KCZ07].

---

## 2. Physical mechanism of elevated (and variable) burn rate

Classical polymeric hybrids are diffusion-flame limited: heat transfer to the wall drives pyrolysis, and blowing reduces convective heat flux (blocking) [KAC02]. Paraffin-class fuels form a **thin, low-viscosity melt layer**. Under port shear, the layer is **hydrodynamically unstable**, shedding droplets into the core flow (**entrainment**). Entrained mass transfer is **not** subject to the same blocking penalty as vaporization, so total fuel mass flux—and thus surface regression—rises sharply [KAC02; KZC04; PAT03].

Design consequences of the mechanism:

| Effect | Implication for \(\dot{r}\) variation | Sources |
|--------|----------------------------------------|---------|
| Entrainment ∝ dynamic pressure / layer properties | Strong sensitivity to local velocity / \(G\) and melt viscosity | [KAC02; MOR] |
| Weaker flux exponent \(n\) than classical hybrids | Smaller O/F swing over the burn (desirable) | [BER07; KZC04] |
| Weak chamber-pressure dependence (typical) | Throttling mainly via \(\dot{m}_{\mathrm{ox}}\) | [KZC04; BER07; MOR] |
| Grain mechanical integrity / slumping | Apparent \(\dot{r}\) can include mass loss not from surface regression | [CAR_EUC; EUC19] |

---

## 3. Quantitative N₂O–paraffin regression laws and measured ranges

### 3.1 Empirical laws (direct N₂O–paraffin)

**Bertoldi (UnB) — pressure-swirl injector, no long prechamber** [BER07]:

\[
\dot{r}\;[\mathrm{mm/s}] = 0.7197\, G_{\mathrm{ox}}^{0.67},\quad G_{\mathrm{ox}}\ \mathrm{in}\ \mathrm{g\,cm^{-2}\,s^{-1}}
\]

Equivalent SI-flux form reported in the same thesis: \(a = 0.1531\) when \(G_{\mathrm{ox}}\) is in \(\mathrm{kg\,m^{-2}\,s^{-1}}\) [BER07].

**Bertoldi — pressure-swirl + 100 mm mixing prechamber** [BER07]:

\[
\dot{r}\;[\mathrm{mm/s}] = 1.2301\, G_{\mathrm{ox}}^{0.47},\quad G_{\mathrm{ox}}\ \mathrm{in}\ \mathrm{g\,cm^{-2}\,s^{-1}}
\]

Interpretation: adding a long prechamber **changes both \(a\) and \(n\)**—i.e., burn-rate variation is **configuration-dependent**, not a universal propellant constant [BER07].

**Stanford SP-1a / GOX reference** (often used as a paraffin baseline; oxidizer differs) [KZC03; KZC04]:

\[
\dot{r}\;[\mathrm{mm/s}] = 0.488\, G_{\mathrm{ox}}^{0.62},\quad G_{\mathrm{ox}}\ \mathrm{in}\ \mathrm{g\,cm^{-2}\,s^{-1}}
\]

ULB reports paraffin/N₂O mean rates **~4–5 mm/s**, higher than some prior N₂O–paraffin literature (~3 mm/s) and comparable to Stanford SP-1a/GOX behavior [ULB].

### 3.2 Observed magnitude bands

| Condition | Typical \(\dot{r}\) | Source |
|-----------|---------------------|--------|
| UnB early 500 N motor, paraffin/N₂O | up to ~4.5 mm/s | [BV05] |
| UnB pressure-swirl campaign (table data ~10–16 g/cm²·s) | ~2.6–4.7 mm/s | [BER07] |
| UnB nine-swirl-atomizer, high flux (~150 g/cm²·s) | **>9 mm/s** | [BER07] |
| ULB small motor, pure paraffin/N₂O | **~4–5 mm/s** mean | [ULB] |
| Literature HTPB/N₂O baseline (for contrast) | ~1 mm/s | [ULB; LOH06] |
| EUCASS 230 N design discussion | cites up to ~4.7 mm/s class for paraffin | [EUC19] |
| IST slab burner, low flux (5–15 kg/m²·s) | weak flux dependence; spatially varying local \(\dot{r}\) | [MOR] |
| CFD Letters N₂O/paraffin cases | ~1.2 mm/s (case-dependent; GOX higher) | [CFD21] |

### 3.3 Relation to this repository’s motor model

`ParaffinN2O_dimensioncalc/model.py` uses Bertoldi’s pressure-swirl SI law [BER07]:

```text
  r_dot [mm/s] = 0.1531 * G_ox[kg/(m²·s)] ^ 0.67
```

(Equivalent cgs form: `r_dot = 0.7197 * G^0.67` with G in g/(cm²·s).)

Unit conversion, history of the previous `a = 0.104` constant, and design impact: see [`REGRESSION_CONSTANT_CLARIFICATION.md`](REGRESSION_CONSTANT_CLARIFICATION.md).  
How to measure your own `a` and `n`: see [`EXPERIMENTAL_MEASUREMENT_OF_A_AND_N.md`](EXPERIMENTAL_MEASUREMENT_OF_A_AND_N.md).

---

## 4. Drivers of burn-rate *variation* (what changes \(\dot{r}\))

### 4.1 Oxidizer mass flux \(G_{\mathrm{ox}}\) (primary)

As the port opens, \(G_{\mathrm{ox}}=\dot{m}_{\mathrm{ox}}/A_{\mathrm{port}}\) falls, so \(\dot{r}\) falls as \(G^{n}\) [KZC04; KCZ07]. Because paraffin \(n\) is often **~0.5–0.7** (lower than many classical hybrids), O/F drift is milder—but still first-order for ballistics [BER07; KZC04].

**Averaging caveat:** published \(a,n\) depend on whether \(G\) and \(\dot{r}\) are diameter-averaged, length-averaged, or O/F-corrected. Cross-paper comparisons without [KCZ07] methodology are unreliable.

### 4.2 Injector and swirl

- **Pressure-swirl / vortex injection** increases regression and can stabilize chamber pressure enough to shorten or eliminate a prechamber [BER07; BEL12e].  
- **Axial shower-head** vs swirl changes head-end recirculation and thus local \(\dot{r}\) near the grain entrance [CAR_EUC].  
- UnB orifice-plate (furos passantes) tests at ~15–16.5 g/cm²·s gave \(\dot{r}\approx 2.9\)–\(3.1\) mm/s—lower than swirl at similar flux [BER07].

### 4.3 Diaphragms / mixers

Grosse’s liquid-N₂O / microcrystalline-paraffin motor showed **~40%** (1-hole) to **~80%** (4-hole) higher regression **downstream of a diaphragm** at mid-grain positions, plus ~12% \(I_{\mathrm{sp}}\) gain vs no diaphragm [GRO09]. Burn-rate variation along the grain can therefore be **engineered**, not only accepted.

### 4.4 Axial / spatial variation

Slab-burner optical data show local \(\dot{r}\) **highest near ignition / leading edge**, then steadier downstream; both optical and mass methods showed **low dependency on oxidizer flux** in the tested low-\(G\) window [MOR]. Motor-averaged laws can hide this structure.

### 4.5 Grain length and scale

Bertoldi reports ~17% length change associated with ~22% \(\dot{r}\) change in one comparison—large enough to demand scale-aware testing [BER07]. Karabeyoglu’s GOX scale-up found **weak length dependence** for SP-1a under their conditions [KZC04]; N₂O datasets are less unanimous, so **do not assume length-independence without your own firings**.

### 4.6 Fuel formulation and manufacturing

- Pure paraffin vs blended / Al-loaded HTPB: paraffin dominates regression gain; Al-HTPB ~+25% at 100 kg/m²·s in Carmicino’s N₂O tests [CAR_EUC; CAR14].  
- Paraffin grain **manufacturing** strongly affects firing results (fragmentation, voids) [CAR_EUC].  
- Viscosity of the melt layer inversely affects entrainment; IST tested low- vs high-viscosity waxes for that reason [MOR; KAC02].

### 4.7 Chamber pressure

For liquefying paraffin, pressure effect on \(\dot{r}\) is generally **weak** over typical hybrid ranges [KZC04; BER07]. Treat pressure as a second-order correction unless your flux regime enters radiation- or kinetics-dominated behavior.

---

## 5. Design guidance (researcher’s recommendations)

1. **Pick one reference law and stick to its averaging definition** [KCZ07]. For N₂O–paraffin with swirl-like injection, **BER07** (\(a=0.7197\), \(n=0.67\) in cgs) is the strongest open experimental fit.  
2. **Budget injector effects separately.** Changing from axial to swirl or adding a diaphragm can move \(\dot{r}\) by tens of percent [BER07; GRO09; BEL12e].  
3. **Expect multi-mm/s rates** and design single-port grains accordingly; do not use HTPB/N₂O \(a,n\) for paraffin [ULB; KZC04].  
4. **Validate at your scale.** UnB early work could not close \(a,n\) until mass-flow measurement improved [BV05]; flux uncertainty dominates regression uncertainty.  
5. **Use Bertoldi pressure-swirl constants in the project model** (`a=0.1531`, `n=0.67` SI), or replace them after fitting your own firings ([`EXPERIMENTAL_MEASUREMENT_OF_A_AND_N.md`](EXPERIMENTAL_MEASUREMENT_OF_A_AND_N.md)).  
6. **Stoichiometry reminder:** N₂O/paraffin stoichiometric O/F is high (~9–9.5), so motors run at **high \(G_{\mathrm{ox}}\)** relative to LOX/HTPB—amplifying absolute \(\dot{r}\) [BV05; EUC19].

---

## 6. Source quality map

| Tier | Role | Keys |
|------|------|------|
| **A — Theory** | Mechanism | KAC02, KAC02b, PAT03 |
| **A — Method** | Scalable averaging | KCZ07, KZC04 |
| **A — N₂O–paraffin data** | Primary experimental | BER07, BV05, ULB, CAR_EUC, CAR14, GRO09, MOR |
| **B — Supporting** | CFD / survey / related fuels | EUC19, CFD21, ACT20, LOH06, BOR11, INT11 |
| **C — Secondary** | Pointers only | WIKI |

Full bibliographic details, DOIs, and local download paths: **[`INDEX.md`](INDEX.md)**. BibTeX: **[`references.bib`](references.bib)**.

---

## 7. Inline citation key list

- **[KAC02]** Karabeyoglu, Altman & Cantwell, *JPP* 2002 — liquefying theory  
- **[KZC03]** / **[KZC04]** Karabeyoglu et al., AIAA 2003-1162 / *JPP* 2004 — paraffin scale-up  
- **[KCZ07]** Karabeyoglu, Cantwell & Zilliac, *JPP* 2007 — scalable averaging  
- **[PAT03]** Karabeyoglu et al., US2003/0098107 — patent  
- **[BV05]** Bertoldi & Veras, COBEM 2005 — early N₂O–paraffin rates  
- **[BER07]** Bertoldi, UnB M.Sc. 2007 — N₂O–paraffin \(a,n\) laws  
- **[ULB]** ULB EUCASS — ~4–5 mm/s paraffin/N₂O  
- **[CAR_EUC]** / **[CAR13]** / **[CAR14]** Carmicino et al. — N₂O lab motors, paraffin vs Al-HTPB  
- **[GRO09]** Grosse, AIAA 2009-5113 — diaphragm \(\dot{r}\) boost  
- **[MOR]** Moreira, IST — slab optical \(\dot{r}(x,G)\)  
- **[EUC19]** EUCASS 2019-0866 — 230 N paraffin/N₂O  
- **[CFD21]** CFD Letters — GOX vs N₂O paraffin CFD  
- **[ACT20]** *Acta Astronautica* 2020 — melt-layer CFD with N₂O  
- **[LOH06]** Lohner et al., AIAA 2006-4671 — N₂O polymer baselines  
- **[BEL12n]** / **[BEL12e]** Bellomo et al. — vortex N₂O–paraffin  
- **[BOR11]** Boronowsky thesis — partial entrainment  
- **[INT11]** InTech hybrid chapter — survey tables  
