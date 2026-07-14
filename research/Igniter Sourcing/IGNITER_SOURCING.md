# Igniter Sourcing for a 20 kN·s Paraffin / N₂O Hybrid

**Purpose.** Explicit steps to **order** or **develop** an ignition system for this project’s ~**20 kN·s** (20,000 N·s) experimental paraffin + N₂O motor on the **static test stand**.  
**Audience.** Builder / adult mentor planning a **full-scale static fire** (campaign end goal — not flight).  
**Companion docs.**  
- [`../N2O_paraffin_burn_rate/SAFETY_PROCEDURES_N2O_PARAFFIN.md`](../N2O_paraffin_burn_rate/SAFETY_PROCEDURES_N2O_PARAFFIN.md)  
- [`../../STATIC_FIRE_WEEKLY_CHECKLIST.md`](../../STATIC_FIRE_WEEKLY_CHECKLIST.md)  
- [`../../Hybrid Motor Static Fire Project.md`](../../Hybrid%20Motor%20Static%20Fire%20Project.md)

**Disclaimer.** Guidance for research planning—not legal advice, not a certified motor procedure, and not a substitute for your site SOP / adult mentor / AHJ rules. Pyrotechnic work by a minor must be adult-supervised; custody of N₂O has age and account gates (adult/parent as custodian).

---

## 1. What you are actually buying or building

A paraffin/N₂O hybrid does **not** light like an APCP solid. You need:

1. **Initiator** — something that starts when GSE applies current (e-match, resistor heater, or spark).  
2. **Energy source / preheater** — enough sustained heat to melt/vaporize paraffin at the grain face (or in a pre-chamber) **before** full oxidizer flow. Typical forms: Pyrodex pellets heated by a resistor, a small APCP or sugar–KNO₃ “puck,” or a commercial hybrid igniter stack.  
3. **Sequencing** — igniter on → confirm flame/heat → open N₂O (often soft-start) → main burn. Hard oxidizer slam onto a cold grain is a common hard-start / grain-crack path.  
4. **Redundancy** — dual initiators preferred for a 20 kN·s research motor.  
5. **Mechanical fit** — leads, support, and preheater geometry that fit **your** injector, pre-chamber, fill line, and nozzle throat.

**Hard truth for 20 kN·s custom paraffin motors:** there is **no** catalog SKU labeled “igniter for 20 kN·s paraffin/N₂O, drop-in.” You either:

- **Order** commercial hybrid ignition hardware (Contrail / HyperTEK class) and **prove** it on *your* grain and injector on a static stand, or  
- **Develop** a custom pyrogen/preheater and qualify it through a staged test campaign.

Both paths end with the same gate: **repeatable ignition on the stand at the fill/fire sequence you will use for the full-scale static fire.**

---

## 2. Decision: order vs develop

| Path | Choose when | You must still do |
|------|-------------|-------------------|
| **A — Order commercial hybrid ignition** | You can use Contrail-style monotube/bolted hardware, or adapt their resistor + Pyrodex method; you want non-hazmat shippable heaters + off-the-shelf pellets | Buy correct voltage igniter + pellets + matching GSE; run subscale → full-scale statics; rewrite SOP for *your* motor |
| **B — Develop custom igniter** | Custom 152 mm-class paraffin grain / pre-chamber that commercial pellets alone will not heat; university-style pyrogen puck | Design puck mass/geometry; source initiators legally; machine holders; instrumented ignition tests; then full motor statics |
| **A then B** (recommended for this project) | Likely best for 20 kN·s | Start with Contrail 24 V igniter + pellet method on a **smaller** motor or cold-flow/mock pre-chamber, measure what energy is required, then size a custom puck if pellets are insufficient |

---

## 3. Path A — Order a commercial hybrid igniter system

### 3.1 What Contrail sells (orderable today)

Contrail’s method: **non-hazmat resistor igniter** + **Pyrodex pellets** (added by the user; not shipped as a live reload).

| Item | Spec / note | Order link |
|------|-------------|------------|
| 12 V resistor igniter, 24″ | ~0.250 (listed as mW on site; treat as 12 V heater element); OK for 38 mm+; **24 V preferred on larger motors** | [12 V igniter](https://contrailrockets.com/product/12-volt-igniter-24-inches-long-designed-for-use-on-38-mm-motors-or-larger) |
| 24 V resistor igniter, 24″ | Dual-heater style lineage; recommended for larger motors | [24 V igniter](https://contrailrockets.com/product/24-volt-igniter-24-inches-long-designed-for-38-mm-or-larger-motors) |
| Motor / 152 mm hardware | Contrail lists **152 mm** bolted systems and reloads—closest commercial diameter to this project’s ~152 mm interfaces | [Contrail catalog](https://contrailrockets.com/) → categories **152mm** |
| GSE (fill / purge / arm / fire) | Must match igniter voltage and solenoid load; longer-range GSE for N-class standoff | [12 V GSE (~300 ft)](https://contrailrockets.com/product/gse-ground-support-equipment-single-pad-12-volt-system-300-feet-maximum-distance) · [12/24 V GSE (~1000 ft)](https://contrailrockets.com/product/gse-ground-support-equipment-single-pad-12-24-volt-system) |
| Large N₂O fill manifold | Explicitly for larger / high-volume hybrids | [3/8″ fill + purge manifold](https://contrailrockets.com/product/nitrous-oxide-fill-manifold-system-3-8-inch-fill-valve-and-1-4-inch-purge-solenoid-valves) |

**Dealer / overview PDF (pellet method explained):**  
[Contrail Hybrid Motors (Pratt Hobbies PDF)](https://pratt-hobbies.com/wpdpratt/wp-content/uploads/2025/09/Contrail-Rockets-Hybrid-Motors.pdf) · [Pratt Contrail page](https://pratthobbies.com/contrail.htm)

**Vendor contact (ordering / consulting):**  
Contrail Rockets LLC — [contrailrockets.com](https://contrailrockets.com/) · info@ContrailRockets.com · (928) 208-5580  
(Also see [12 V ignition notes](https://contrailrockets.com/12-volt-ignition).)

**Alternate commercial hybrid lineage:** [HyperTEK](http://www.hypertekhybrids.com/mainpage.html) (CTI) — modular N₂O/thermoplastic system with remote fill/fire; historically marketed with pyrotechnic-free ignition. Useful if you can stay inside their fuel/injector architecture; not a drop-in for a custom paraffin grain.

### 3.2 Exact steps to **order** (Path A)

Do these in order.

1. **Freeze motor interface dimensions**  
   - Chamber ID / grain OD (~152 mm if that is your case).  
   - Pre-chamber length, injector type, fill-line OD, vent-tube OD (Contrail igniters often slide onto a **1/8″** vent tube—confirm against *your* drawing).  
   - Nozzle throat diameter (igniter must pass through or be installed from the head end).

2. **Email Contrail (or call) with a written RFQ** — copy/paste and fill blanks:

   ```text
   Subject: Ignition + GSE RFQ — experimental paraffin/N2O, ~20 kN·s, ~152 mm

   We are developing an experimental N2O + paraffin hybrid (~20,000 N·s class).
   Please advise:
   1) Recommended igniter (12 V vs 24 V) and quantity of Pyrodex pellets for a
      motor near 152 mm with [pre-chamber length ___ mm] and [injector type ___].
   2) Whether your 152 mm bolted system / reloads can be used as a reference
      ignition stack, or consulting for adapting your resistor+pellet method
      to a custom paraffin grain.
   3) Matching GSE (voltage, cable length for ≥1000 ft standoff), fill manifold,
      and lead times / age-of-buyer or Shipper-of-Record requirements.
   4) Owner’s manual section on ignition for the closest motor to our size.

   Attachments: section drawing of pre-chamber/injector; estimated m_dot_ox;
   burn time; chamber pressure target.
   ```

3. **Create a web account and purchase** from [contrailrockets.com](https://contrailrockets.com/) (or via Pratt if directed):  
   - Recommended: **24 V igniter** for large motors (buy **spares**—plan ≥6 for development).  
   - Matching **GSE** and **fill manifold** if you do not already have remote fill/fire.  
   - If evaluating commercial architecture: relevant **152 mm** hardware/reload kit as a **reference motor**, not as your flight paraffin motor unless that is an explicit design choice.

4. **Buy Pyrodex pellets separately** (not hazmat rocket motors; common muzzleloader product).  
   - **Exact product:** Hodgdon **Pyrodex 50/50** pellets — **.50 caliber / 50 grain** (SKU **BP5050**). Center hole is what lets you stack them on a heater or thread an e-match.  
   - **Order / buy:** [Hodgdon shop](https://shop.hodgdon.com/pyrodex-50-50-pellets/) · [Muzzle-Loaders.com](https://muzzle-loaders.com/products/hodgdon-pyrodex-50-50-pellets-black-powder-substitute-50-cal-50-grains) · [MidwayUSA](https://www.midwayusa.com/product/1009299634) · local Bass Pro / outdoor / gun shops (adult purchaser). Online powder orders often add UPS hazmat fees.  
   - **Quantity and pellet size:** use **only** the count/size in the Contrail manual for the motor class you are mimicking; do **not** invent a “20 kN·s pellet count” without vendor advice + static-fire proof. Do **not** substitute Triple Seven or other BP substitutes without a new ignition qualification.  
   - Adult purchaser if local age rules apply to black-powder substitutes.

### 3.4 If Contrail’s website is down — initiator alternatives

The Contrail 24 V part is a **dual resistor heater** (~$1.50, non-hazmat) that lights Pyrodex pellets. It is **not** the only workable initiator for this static campaign.

| Alternative | Replaces | Source | Notes |
|-------------|----------|--------|-------|
| Call / email Contrail | Web cart | (928) 208-5580 · info@ContrailRockets.com · [Pratt overview](https://pratthobbies.com/contrail.htm) | Prefer before cloning |
| **E-match or AeroTech FirstFire** + Pyrodex 50/50 | Resistor | HPR dealers; [Apogee igniter overview](http://www.apogeerockets.com/Peak-of-Flight/Newsletter527); [AeroTech FirstFire](https://aerotech-rocketry.com/) | Thread through pellet hole; dual preferred; all-fire test at cable length |
| **DIY nichrome / power resistor** + Pyrodex | Resistor | Electronics suppliers | Closest clone of Contrail method; qualify heat on a dry pellet stack |
| **Sugar–KNO₃ puck** + nichrome | Pellets + heater | [UCLA HyPE PDF](https://www.soundingrocket.org/uploads/9/0/6/4/9064598/technical_paper_ucla.pdf) | Path B Lane 2 |
| **Short APCP slug** + e-match | Pellets | Commercial 18–29 mm grain segment; mentor/range rules | Common when pellets are unavailable ([TRF thread](https://www.rocketryforum.com/threads/contrail-hybrid-alternatives-to-pyrodex-pellets-for-ignition.159470/)) |
| HyperTEK GOX + HV spark | Entire ignition stack | [HyperTEK](http://www.hypertekhybrids.com/mainpage.html) | Different architecture — not a drop-in |

**Do not** expect a bare Estes / low-current starter alone to heat a large paraffin grain. You still need a **preheater** (pellets or puck).

5. **Buy / verify GSE electrical capability**  
   - Battery and cable sized for the **heater current** at pad distance (voltage drop matters at 1000 ft).  
   - Spark-check procedure, arm key, and separate fill vs fire channels.  
   - For N-class personnel distance, prefer the **12/24 V long-range GSE** or an equivalent RC/Ethernet system (see Half Cat / Waterloo notes in prior sourcing notes).

6. **Receive, inspect, log**  
   - Photograph packing list; measure igniter resistance cold; label lots.  
   - Store pellets dry, per manufacturer; keep initiators **shunted** until connect.

7. **Do not skip to full 20 kN·s** — enter the validation ladder in §5.

### 3.3 What Path A does *not* automatically give you

- Guaranteed ignition of a **custom paraffin** grain with a different injector or cold chamber.  
- Permission to fly a homemade hybrid at a sport launch.  
- Correct pellet count for 20 kN·s without testing.  

Ordering gets you **qualified building blocks**. Your team still owns the **ignition sequence proof**.

---

## 4. Path B — Develop your own igniter

Use this when commercial pellets/heaters cannot establish a stable flame before main N₂O flow, or when geometry (152 mm pre-chamber, head-end fill, custom injector) requires a shaped **pyrogen / preheater**.

### 4.1 Architecture you must design (block diagram)

```text
  GSE fire channel
        │
        ├─► Initiator A (e-match or resistor)  ─┐
        └─► Initiator B (redundant)            ─┼─► Preheater / pyrogen puck
                                                │         │
                                                │         ▼
                                                │   Heat paraffin surface /
                                                │   pre-chamber gases
                                                │         │
                                         open N₂O (soft) ─► Main hybrid burn
```

**Deliverables before any N₂O hot-fire with a new design:**

| # | Deliverable | Pass criterion |
|---|-------------|----------------|
| D1 | Initiator datasheet + measured all-fire current | GSE can supply ≥2× all-fire at pad cable length |
| D2 | Preheater mass, composition, geometry drawing | Fits pre-chamber; clearance to injector spray; does not block port |
| D3 | Hold-down / bonding method | Survives transport + fill vibration; ejects or burns clean |
| D4 | Electrical schematic (dual fire, shunts, arm) | Two inhibits + spark-check written in SOP |
| D5 | Open-air / atmospheric burn of puck alone | Both initiators light puck; burn time ≥ target preheat window |
| D6 | Motor dry-fire (no N₂O): puck in chamber | No chamber damage; leads clear nozzle; debris acceptable |
| D7 | Subscale N₂O hot-fire | Ignition delay within window; no hard start; grain intact |
| D8 | Full-scale static at campaign sequence | ≥1 (prefer ≥3) consecutive successes at full or planned load |

### 4.2 Exact steps to **develop** (Path B)

#### Step 1 — Set ignition requirements from motor numbers

Write these into the ignition ICD (interface control) before buying powder:

| Parameter | How to get it | Example use |
|-----------|---------------|-------------|
| Target \(\dot{m}_{ox}\) at start | Injector sizing / fill model | Sets how fast you must have flame before full flow |
| Preheat time \(t_{pre}\) | Goal: melt a surface layer without cracking grain | Often 0.5–3 s class—**measure**, do not guess |
| Chamber volume / pre-chamber volume | Drawing | Sets how much hot gas you need |
| Max allowable ignition overpressure | Structural analysis | Caps pyrogen mass |
| Grain temp at fire | Instrumentation plan | Cold paraffin cracks more easily (see safety doc §6.5) |

#### Step 2 — Choose initiator type (order list)

| Initiator | When to use | Where to source | What you must do |
|-----------|-------------|-----------------|------------------|
| **Contrail 24 V resistor** | Prefer non-hazmat heater under pellets or against a puck | [Contrail 24 V](https://contrailrockets.com/product/24-volt-igniter-24-inches-long-designed-for-38-mm-or-larger-motors) | Measure R; size battery/cable; follow pellet or puck seating |
| **Commercial e-match** (Oxral / similar) | Low-current fire under a pyrogen coat or APCP puck | Supplied with many CTI reloads; HPR dealers; see [Cesaroni FAQ](https://cesaroni-aerospace.com/frequently-asked-questions/) and [Apogee igniter overview](http://www.apogeerockets.com/Peak-of-Flight/Newsletter527) | Adult purchase if required; keep shunted; dual matches; all-fire test on scrap |
| **Nichrome + pyrogen coat** | University-style (e.g. UCLA HyPE) | Nichrome wire + approved pyrogen process under mentor | Document resistance, coating mass, and dual-bridge layout |

Reference paper (sugar–KNO₃ ring + dual nichrome):  
[UCLA HyPE technical paper (PDF)](https://www.soundingrocket.org/uploads/9/0/6/4/9064598/technical_paper_ucla.pdf)

Field example (APCP ring + e-match on Contrail-class hybrid static):  
[RRS / FAR hybrid static write-up](https://rrs.org/2021/04/24/static-fire-test-of-hybrid-motor-at-far-2021-04-17/)

#### Step 3 — Choose preheater chemistry (pick one lane and stick to it)

| Lane | Composition (conceptual) | Pros | Cons / controls |
|------|--------------------------|------|-----------------|
| **Lane 1 — Contrail method** | Pyrodex pellets + resistor | Shippable heater; documented for commercial hybrids | May under-heat large paraffin surface; pellet count must be proven |
| **Lane 2 — Sugar–KNO₃ pyrogen** | Cast ring/puck (UCLA-style) | Controllable geometry; common in student papers | Hygroscopic; must be dry; still a pyrotechnic mixture—adult SOP |
| **Lane 3 — Small APCP / composite puck** | Commercial APCP slug or mentor-mixed grain segment | High energy density; proven on hybrids in the field | Explosives/regulatory and range rules; **not** a DIY first project for a minor without licensed adult |

**Explicit rule for this project:** If the primary builder is a **minor**, Lane 3 materials and mixing stay under a **qualified adult**; do not improvise APCP formulas from the internet. Prefer Lane 1 first; escalate to Lane 2/3 only with mentor + range approval.

#### Step 4 — Size the preheater (engineering loop)

1. Start from a **known-good small motor** ignition (Contrail 38/54 mm class or a subscale paraffin motor).  
2. Record: time from fire to visible flame, time to stable \(P_c\) after N₂O open, peak \(P_c\) spike.  
3. Scale **preheater mass** roughly with **pre-chamber free volume** and **grain exposed area facing the igniter**, not with total impulse alone.  
   - 20 kN·s means a large grain and long burn—but ignition cares about **initial heat soak**, not total propellant mass.  
4. Increase energy in **small steps** (e.g. +25% pellet/puck mass) between statics.  
5. Stop increasing when: ignition delay is repeatable **and** ignition overpressure / grain inspection stay acceptable.

#### Step 5 — Design the mechanical package

You must produce a drawing that answers:

- How does the igniter enter (nozzle vs head-end)?  
- How is the puck located axially relative to the injector spray?  
- Where do wires run so they eject or burn without plugging the throat?  
- How does the **fill line** (if nylon head-end fill) clear the igniter (see RRS article for fill-line + e-match practice)?  
- Retention: tape, phenolic holder, press-fit ring, snap ring—**named** in the traveler.

#### Step 6 — Electrical / GSE requirements you must implement

- Dual initiators on **one** fire command (or dual channels fired together).  
- Continuity check **without** enough current to fire.  
- Spark-check of leads **before** connecting initiators.  
- Arm key / enable separate from fire.  
- Failsafe: lost link does **not** fire; N₂O dump opens if filled.  
- Document all-fire / no-fire currents at the **end of the actual pad cable**.

Build references:  
[Half Cat remote firing](https://www.halfcatrocketry.com/rcfs) · [Waterloo RLCS](https://docs.waterloorocketry.com/electrical-gse/rlcs-v4/index.html)

#### Step 7 — Legal / safety gates before mixing or firing

- Read and follow [`SAFETY_PROCEDURES_N2O_PARAFFIN.md`](../N2O_paraffin_burn_rate/SAFETY_PROCEDURES_N2O_PARAFFIN.md) §6.5 (ignition shock) and oxidizer cleanliness.  
- Confirm with mentor whether your pyrogen is allowed at your **static site** (FAR, RRS, university, private land + AHJ).  
- Age 17: adult/parent as **N₂O custodian** and final go/no-go for static ops (see weekly checklist).  
- Never approach a motor with N₂O aboard to “fix” an igniter.

---

## 5. Validation ladder (required for both Path A and Path B)

Do **not** jump straight to a full 20 lb / ~20 kN·s static without the early stages.

| Stage | Configuration | N₂O? | Success = |
|-------|---------------|------|-----------|
| **V0** | Initiator only (bench) | No | Fires at measured current; both bridges OK |
| **V1** | Preheater in open air / sand pit | No | Full puck/pellets consumed; burn time logged |
| **V2** | Igniter installed in **inert** chamber (or empty case) | No | Lead routing OK; no mechanical interference |
| **V3** | Subscale paraffin motor or shortened grain | Yes, remote | Soft start; \(P_c\) rise without spike; grain post-inspect OK |
| **V4** | Full-diameter grain, reduced N₂O load | Yes, remote | Same as V3 at stand injector |
| **V5** | Full 20 kN·s / 20 lb-class propellant load static | Yes, remote | Nominal ignition; campaign complete when data archived |

Instrument every N₂O stage: chamber pressure, fire-command time stamp, valve-open time stamp, video of plume/vent.

---

## 6. Bill of materials checklist (print and tick)

### 6.1 Ordering Path A

- [ ] Interface drawing (pre-chamber, vent tube, throat) frozen  
- [ ] RFQ email sent to Contrail (or HyperTEK if that architecture)  
- [ ] 24 V igniters × ___ (recommend ≥6) ordered  
- [ ] Pyrodex pellets (correct size) × ___ ordered by eligible adult  
- [ ] GSE ordered / verified for voltage and ≥1000 ft standoff  
- [ ] Fill/dump valves + manifold compatible with N₂O  
- [ ] Owner’s manual ignition section on file  
- [ ] V0–V5 test plan signed by mentor  

### 6.2 Developing Path B

- [ ] Ignition ICD with \(t_{pre}\), max \(P_c\) spike, geometry  
- [ ] Initiator type chosen + all-fire data measured  
- [ ] Preheater lane chosen (1 / 2 / 3) with adult approval  
- [ ] Puck/pellet drawing + mass target  
- [ ] Holder / bonding method drawn  
- [ ] Dual-init wiring diagram + arm/fire SOP  
- [ ] V0–V2 complete before any N₂O  
- [ ] V3–V5 complete before declaring the static campaign done  
 

---

## 7. Recommended project plan (this repo)

1. **Week 0–1:** Try Contrail RFQ (§3.2); if the site is down, call/email or use §3.4 initiator alts. Order heaters/initiators + **Pyrodex 50/50** + DIY remote fire (not the $450 GSE unless needed).  
2. **Week 1–2:** V0–V2 on the bench; measure heater/e-match current and pellet burn time.  
3. **Week 2–4:** V3 on a subscale paraffin/N₂O motor or shortened grain (same injector family if possible).  
4. **Decision gate:** If ignition is marginal → design Lane 2/3 puck (Path B Steps 3–5) under mentor; do **not** only “add more pellets” without pressure/grain inspection data.  
5. **Week 4+:** V4–V5 on the 20 kN·s article at an approved static site; freeze the ignition kit lot used for the successful full-scale fire. Follow [`STATIC_FIRE_WEEKLY_CHECKLIST.md`](../../STATIC_FIRE_WEEKLY_CHECKLIST.md) for the calendar.

---

## 8. Link index

| Topic | URL |
|-------|-----|
| Contrail home / 152 mm catalog | https://contrailrockets.com/ |
| Contrail 12 V igniter | https://contrailrockets.com/product/12-volt-igniter-24-inches-long-designed-for-use-on-38-mm-motors-or-larger |
| Contrail 24 V igniter | https://contrailrockets.com/product/24-volt-igniter-24-inches-long-designed-for-38-mm-or-larger-motors |
| Contrail 12 V ignition notes | https://contrailrockets.com/12-volt-ignition |
| Contrail long-range GSE | https://contrailrockets.com/product/gse-ground-support-equipment-single-pad-12-24-volt-system |
| Contrail large fill manifold | https://contrailrockets.com/product/nitrous-oxide-fill-manifold-system-3-8-inch-fill-valve-and-1-4-inch-purge-solenoid-valves |
| Pratt Contrail overview | https://pratthobbies.com/contrail.htm |
| Pratt Contrail overview PDF | https://pratt-hobbies.com/wpdpratt/wp-content/uploads/2025/09/Contrail-Rockets-Hybrid-Motors.pdf |
| **Pyrodex 50/50 pellets (Hodgdon BP5050)** | https://shop.hodgdon.com/pyrodex-50-50-pellets/ |
| Pyrodex 50/50 (Muzzle-Loaders.com) | https://muzzle-loaders.com/products/hodgdon-pyrodex-50-50-pellets-black-powder-substitute-50-cal-50-grains |
| Pyrodex 50/50 (MidwayUSA) | https://www.midwayusa.com/product/1009299634 |
| HyperTEK | http://www.hypertekhybrids.com/mainpage.html |
| Cesaroni igniter FAQ | https://cesaroni-aerospace.com/frequently-asked-questions/ |
| Apogee igniter types | http://www.apogeerockets.com/Peak-of-Flight/Newsletter527 |
| UCLA HyPE ignition paper | https://www.soundingrocket.org/uploads/9/0/6/4/9064598/technical_paper_ucla.pdf |
| RRS FAR hybrid static (APCP puck practice) | https://rrs.org/2021/04/24/static-fire-test-of-hybrid-motor-at-far-2021-04-17/ |
| Half Cat remote fire | https://www.halfcatrocketry.com/rcfs |
| Waterloo RLCS | https://docs.waterloorocketry.com/electrical-gse/rlcs-v4/index.html |
| NAR HPR distance table (N-class = 1000 ft) | https://www.nar.org/HighPowerRocketSafetyCode |
| TRA safety code (hybrid remote fill/dump) | https://www.tripoli.org/safetycode |

---

## 9. Document control

| Field | Value |
|-------|-------|
| Title | Igniter Sourcing |
| Location | `research/Igniter Sourcing/IGNITER_SOURCING.md` |
| Motor class | ~20 kN·s (20,000 N·s) paraffin / N₂O research hybrid |
| Status | Living sourcing + development procedure |
| Last updated | 2026-07-11 |
