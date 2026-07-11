# Research Brief: Pre-Mixing Chamber Length Selection in N₂O–Paraffin Hybrid Rockets

**Author role.** Propulsion research synthesis for hybrid motor design.  
**Companion index.** [`INDEX.md`](INDEX.md) — full bibliographic inventory and local file map.  
**Date.** 2026-07-11

**Notation (plain text).**  
`L_pc` or `L_pre` = prechamber length · `D_pc` or `d_pc` = prechamber diameter · `v_i` = injection velocity · `v_p` = port velocity · `tau_pc` / `tau_pre` = prechamber residence time · `DeltaP` = injector pressure drop · `P_c` = chamber pressure · `eta_c*` = characteristic-velocity efficiency · `a`, `n` = regression-rate constants.

---

## 1. Executive finding

For liquid-N₂O / paraffin hybrids, **pre-mixing (pre-combustion) chamber length is a first-order design variable**, not a free packaging leftover. It must be long enough for **atomization + vaporization (and some N₂O dissociation)** and for **acceptable low-frequency / feed-system-coupled stability**, yet short enough to limit **inert mass, heat loss, and packaging cost** [GON24; GON25; LEE20; ULB].

There is **no single universal millimetre value**. Reputable practice is:

1. Size `D_pc` from grain final OD / motor envelope [GON24].  
2. Start from an empirical ratio near **`L_pc / D_pc ≈ 0.5`** [HUM95; GON24].  
3. Refine with a **droplet-vaporization length** and a **feed-coupled stability check** (preferably both) [GON23; GON25; LEE20].  
4. Confirm with cold-flow spray / hot-fire `eta_c*` and pressure-oscillation data [GON24].

Recent open design work validated against UnB (SARA) and ULB (~1 kN N₂O/paraffin) motors recommends an engineering window:

```text
  0.24  ≤  L_pc / d_pc  ≤  0.81
```

with early-phase use of **`0.5 ± 0.25`** only as a preliminary band [GON25].

---

## 2. What the pre-mixing chamber does

Upstream of the paraffin grain, the prechamber provides volume for the liquid oxidizer to be **injected, atomized, and vaporized (or partially vaporized)** and for the gas to **preheat / recirculate** before entering the port [GON24; GON25; ULB]. ULB’s N₂O/paraffin motor explicitly cites the precombustion chamber as allowing **N₂O vaporization and dissociation** before reaction with melting paraffin [ULB].

Design consequences:

| If too short | If too long | Sources |
|--------------|-------------|---------|
| Incomplete vaporization; nonuniform head-end burn | Extra inert mass and heat-transfer losses | [GON25; GON24] |
| Feed-system-coupled / low-frequency pressure oscillations | Diminishing returns on `eta_c*`; can steal length from the reaction zone | [LEE20; GON25; LIN13] |
| Liquid N₂O quenching / endothermic penalty at grain face | Higher cost and packaging difficulty | [LIN13; GON24] |

Gaseous oxidizer can tolerate a **shorter** prechamber because atomization/vaporization are absent [GON24]. Liquid N₂O (two-phase, self-pressurizing) is the harder case and drives most published length models [WHI10; GON25].

---

## 3. Quantitative length-selection guidance

### 3.1 Empirical L/D rules

The most cited textbook starting point is:

```text
  L_pc / D_pc  ≈  0.5
```

[HUM95], reiterated as the common rule of thumb in recent surveys [GON24; GON25]. Gontijo’s vaporization-based calculations produced a **mean ~0.53**, close to that rule [GON24].

Updated windows from the vaporization + stability algorithm:

| Reference | Recommended `L_pc / d_pc` | Basis |
|-----------|---------------------------|--------|
| GON23 | 0.26 – 0.66 | Complete vaporization vs real motors |
| GON25 | 0.24 – 0.81 | Vaporization + FSC stability; SARA/ULBHRE N₂O data |
| GON25 (early only) | 0.5 ± 0.25 | Preliminary sizing band |

These ratios are **not** substitutes for injector-specific droplet size and port velocity; they are condensed results of those physics for the motors studied [GON25].

### 3.2 Physics-based sizing (preferred)

**Vaporization length.** Adapt Priem-type single-droplet mass/energy balances in an oxidizer-rich prechamber atmosphere; integrate until the droplet is consumed (or vaporized fraction target, e.g. 90–100%) [PRI57; GON25]. Required `L_pc` rises with **larger SMD** and **higher injection velocity**, and falls with higher chamber pressure / droplet temperature [GON25]. Injector orifice diameter and `DeltaP` therefore **set** the length budget [BOU17; BOU19; GON25].

**Stability length.** Feed-system-coupled (Summerfield / L*-family) models for hybrids introduce a prechamber residence time:

```text
  tau_pc  ∝  2 * L_pc / (v_i + v_p)

  where:
    tau_pc  = prechamber residence time
    L_pc    = prechamber length
    v_i     = oxidizer injection velocity
    v_p     = gas velocity at the grain-port entrance
```

This is coupled to injector pressure drop through:

```text
  beta  =  P_c_avg / (2 * DeltaP)
```

and to bulk gas residence time [SUM51; LEE20; GON25]. Lee et al. showed experimentally on N₂O hybrids that **`L_pre` and injection velocity** control the **period** of pressure oscillations, and proposed a frequency correlation based on `tau_pre` [LEE20].

**Both criteria.** GON25’s algorithm takes the length needed for vaporization **and** checks the stability map; a vaporization-optimal length can still be unstable, forcing redesign (e.g. via port radius) [GON25].

### 3.3 Experimental N₂O geometries (anchors)

UnB exchangeable-prechamber campaign (paraffin/HDPE + liquid N₂O) [LEE20]:

| Parameter | UnB | ULB (companion) |
|-----------|-----|-----------------|
| `L_pre` tested | 56.6, 76.6, 157.6, 177.6 mm | 102.5 mm |
| `D_pre` | 120 mm | 99 & 130 mm |
| Port diameter | 34 / 51 mm | 30 mm |

Comparing short vs long UnB cases (e.g. showerhead at 56.6 mm vs 157.6 mm), the **longer prechamber ran much more stably**, but lengthening also raised bulk gas residence time `theta_g`, which itself widens the stability locus—so length and volume effects are **coupled** [LEE20]. Practically, a very long PC that “fixes” stability can be undesirable for mass [LEE20; GON25].

Bertoldi’s earlier UnB paraffin/N₂O work fitted different regression laws **without** vs **with** a **100 mm mixing prechamber** (`a` and `n` both changed), proving head-end length alters ballistics, not only stability [BER07].

ULB’s small motor documents the prechamber’s vaporization/dissociation role and recommends **≥20% injector pressure drop** relative to chamber pressure to limit backflow [ULB]. GON25 likewise cites typical injector `DeltaP` of **~20–30% of `P_c`** [GON25; HUM95].

---

## 4. Drivers that change the required length

### 4.1 Injector atomization (strong)

Smaller SMD and moderate `v_i` shorten the vaporization length [GON25]. Pressure-swirl sprays can achieve very small SMD; vortex/hollow-cone change regression and plume behavior on the same 1 kN paraffin/N₂O motor [BOU19; BOU17]. **Changing injector type can justify shortening the PC**—or demand lengthening it if droplets coarsen.

### 4.2 Port diameter / mass flux

Port radius enters both `tau_pc` (via `v_p`) and stability maps; GON25 shows `L_pc` and `tau_pc` fall as port radius rises for fixed burn-time constraints [GON25]. Grain design also sets `D_pc` (usually tied to final grain OD) [GON24]. For N₂O/paraffin, literature cited in GON24 warns that initial oxidizer mass flux above ~**650 kg/(m²·s)** risks blowoff / instability [GON24].

### 4.3 Completeness vs length fraction

Lin’s numerical prevaporized-zone study found completeness peaking near **~24% of combustor length**; beyond ~one-fourth, completeness fell as reaction space shrank [LIN13]. That fraction is configuration-specific but warns against “longer is always better.”

### 4.4 Recirculation and vortex shedding

Dump-style prechambers create head-end recirculation that can preheat oxidizer and aid flame holding [GON24]. Carmicino’s work shows vortex shedding in **pre- and post-chambers** and strong injector (axial vs radial) effects on low-frequency stability [CAR09; CAR06]. Length changes that alter the dump aspect ratio can therefore move acoustic/vortex coupling, not only vaporization.

### 4.5 Feed isolation hardware

Cavitating venturis or choked injectors can decouple feed and chamber dynamics, reducing reliance on PC volume for FSC control—but **cavitating venturis are discouraged for N₂O** due to decomposition risk; choked injectors are the usual alternative [GON25; LEE20].

---

## 5. Design guidance (researcher’s recommendations)

1. **Do not freeze `L_pc` from packaging alone.** Treat it as a stability + vaporization requirement [GON24; LEE20].  
2. **Preliminary:** `L_pc / D_pc ≈ 0.5` with `D_pc` from grain OD [HUM95; GON24].  
3. **Refine:** run (or approximate) GON25-style vaporization length using your injector SMD and `DeltaP`, then check FSC stability with `tau_pc` [GON25; LEE20]. Aim inside **0.24 – 0.81** unless your data say otherwise [GON25].  
4. **Couple injector and PC.** Better atomization → shorter PC possible; coarse showerhead jets → longer PC or swirl upgrade [BOU17; BOU19; BER07].  
5. **Expect ballistic coupling.** A long mixing prechamber can change paraffin/N₂O `a` and `n` [BER07]—re-fit regression if you change head-end length.  
6. **Validate:** cold-flow spray / coalescence, then hot-fire `eta_c*` and pressure oscillation ratio `P'_c / P_c_avg` (stable often taken as oscillations ≲ 5%) [GON24; GON25].  
7. **Workflow (GON24):** collision/outcome check → empirical L/D → vaporization + instability models → CFD → cold/hot tests.

---

## 6. Source quality map

| Tier | Role | Keys |
|------|------|------|
| **A — Design methods** | Length selection algorithms & surveys | GON25, GON23, GON24, HUM95 |
| **A — N₂O experiment** | Measured `L_pre` effects | LEE20, BER07, ULB, BOU17, BOU19, EUC19 |
| **B — Supporting physics** | Instability / completeness / feed models | SUM51, PRI57, LIN13, CAR09, CAR06, WHI10, AND15, BER18, BER19 |
| **C — Background** | Textbook chamber sizing | SUT10 |

Full bibliographic details, DOIs, and local download paths: **[`INDEX.md`](INDEX.md)**. BibTeX: **[`references.bib`](references.bib)**.

---

## 7. Inline citation key list

- **[HUM95]** Humble, Henry & Larson — `L_pc / D_pc ≈ 0.5`  
- **[GON25]** Gontijo, Shynkarenko & Bertoldi, *Energies* 2025 — vaporization + stability design  
- **[GON23]** Gontijo et al., AIAA 2023-2183 — conference precursor  
- **[GON24]** Gontijo, *AKTT* 2024 — methods survey + workflow  
- **[LEE20]** Lee et al., *JPP* 2020 — UnB/ULB N₂O prechamber instability tests  
- **[BER07]** Bertoldi UnB M.Sc. 2007 — 100 mm prechamber changes `a`, `n`  
- **[BER18]** / **[BER19]** Bertoldi Ph.D. / EUCASS instability studies  
- **[BOU17]** / **[BOU19]** Bouziane et al. — N₂O injector spray & 1 kN motor  
- **[ULB]** ULB EUCASS — prechamber vaporization/dissociation role  
- **[EUC19]** EUCASS 2019-0866 — 230 N pre/post chamber layout  
- **[LIN13]** Lin, *AEAT* 2013 — ~24% prevaporized-zone optimum  
- **[CAR09]** / **[CAR06]** Carmicino — prechamber vortex / injector stability  
- **[PRI57]** Priem NACA TN 3985 — droplet vaporization length  
- **[SUM51]** Summerfield 1951 — L* instability foundation  
- **[WHI10]** Whitmore & Chandler — N₂O self-pressurizing feed model  
- **[AND15]** Andrianov et al. — SARA hybrid test motor  
- **[SUT10]** Sutton & Biblarz — chamber characteristic length background  
