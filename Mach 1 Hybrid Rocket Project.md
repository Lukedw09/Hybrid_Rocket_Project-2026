# **Hybrid Motor Component List**

*Flight-Size Paraffin \+ N₂O Hybrid (152 mm) \+ Instrumented Static Test Stand*

Luke de Wet  •  Phase 0 – July 2026  •  Experimental Hybrid Rocket Project

## **Locked Targets**

* **Motor / chamber OD:** 152.4 mm (6″) nominal — **not** the tank diameter. Do **not** shrink below ~6″ for packaging.  
* **Chamber path (preferred):** Custom **6061-T6** tube sized by `ParaffinN2O_dimensioncalc` (Sutton hoop \+ margins below). Contrail 152 mm is a heavy backup / reference only.  
* **Airframe:** **Madcow 8″ G12** (**ID 7.825″ / OD 8.000″**) — fits the **≤7″ OD** flight bottle. Motor mounts via centering rings \+ thrust bulkhead \+ aft retention (Section 2.2).  
* **Flight Motor Target:** \~**15 kN·s** class from locked oxidizer budget (Isp ≈ 194 s); **~20 kN·s** remains a stretch only if delivered Isp / usable fill are better than budget. **4 MPa** chamber pressure. Oxidizer from locked **Catalina NO15** ≈ **6.8 kg N₂O** (calculator at O/F ~6 → **~1.13 kg** paraffin; total propellant ≈ **7.9 kg**).  
* **First Static Test Motor:** Same ~152 mm OD, \~10–12 kN·s impulse, shorter grain (easier/safer early testing)  
* **Primary Goal:** Get the rocket flying by December 2026 (performance targets are secondary on first flight). Mach 1 / 5 km still needs more oxidizer or a later motor class — NO15 is the max that fits Madcow 8″ without a 9″ airframe.

## **Prioritized Ordering & Research Sequence**

1. **Now – July 15:** **RFQ Catalina NO15** (Section 1) via GCS special-order, Catalina sales, and local Airgas fill path; do **not** lock a 10 lb bottle as flight ox. Price **≥500 kg** load cell (not 150–200 kg), pressure transducer. **Source custom 6061-T6 chamber tube** (material certs); keep Contrail only if custom lead time slips. Start safety plan draft.  
2. **By July 20:** Finalize injector concept and lathe drawings for injector plate \+ closures. **RFQ/order short cuts of 6″ 6061 round bar** (Section 2.1). Order long-lead items (load cell, transducer). Order oxidizer feed-system kit (Section 1) as one batch (plumbing unchanged — still CGA-326).  
3. **By July 25:** Design nozzle, **centering rings, thrust bulkhead, and aft motor retention** in SolidWorks. Order **8″ 6061 round** (or G10 via SendCutSend) for airframe discs; graphite nozzle blank for the nozzle carrier. Plan chamber hydro-proof. Size tank bay for **~23.1″** NO15 length (+ valve/handle).  
4. **Late July – August:** Order igniter materials; cold-flow / leak-check oxidizer plumbing before any hot fire. Begin casting test grains. Confirm local **fill** account for customer-owned CGA-326 cylinder (parent/adult).

## **1\. Oxidizer System (N₂O)**

**Operating model:** Fill / prep the flight or static cylinder elsewhere, then attach it to this fixed feed plumbing for static test. No remote pad-fill loop.

**Flight / static tank (locked — RFQ path):** Medical/industrial **DOT aluminum** N₂O cylinder with **CGA-326** valve, **OD ≤ 7″** — **Catalina NO15** (15 lb / ~6.8 kg N₂O).

* **Order this (RFQ — not add-to-cart):** Catalina **NO15** — **6.89″ OD × ~23.1″**, empty mass ~16.2 lb, DOT-3AL / TC-3ALM, neck **1.125-12 UNF**, **CGA-326** valve required. Specs: [Catalina N₂O table](https://www.catalinacylinders.com/markets/nitrous-oxide/) · [NO15](https://www.catalinacylinders.com/product/no15/) · buy path: [catalinacylinders.com/buy](https://www.catalinacylinders.com/buy) · email [sales@catalinacylinders.com](mailto:sales@catalinacylinders.com).  
* **Parallel RFQ contacts (adult/parent buyer):**  
  1. **Gas Cylinder Source** (online, Wyoming MN — not a local chain): **866-395-5049**, [contact](https://gascylindersource.com/contact-gas-cylinder-source/), ask for special-order **NO15 / 15 lb Al + CGA-326** empty.  
  2. **Catalina sales** — nearest distributor + lead time for NO15 + CGA-326 (prefer removable/low-profile handle; quote siphon/dip tube as option).  
  3. **Local filler** (e.g. Airgas Tallahassee **850-576-2192**, 945 Yulee St) — customer-owned **CGA-326** fill (industrial/specialty/food-grade preferred over USP medical Rx path).  
* **Interim / backup only:** [GCS 10 lb Al + CGA-326](https://gascylindersource.com/shop/nitrous-oxide-cylinders/new-10-lb-aluminum-n2o-cylinder/) (~4.5 kg) if NO15 lead time blocks static-test schedule — **not** the flight oxidizer budget.  
* **Do not buy:** NX 11151 / NOS Hi-Flo (CGA-660 / AN, not CGA-326).

Everything below is sized to that **CGA-326** outlet and a **1/4″ NPT, 316 stainless + PTFE** feed standard (≥3000 psi / ≥20 MPa working class; exceeds the project ≥10 MPa floor).

### **1.0 Tank diameter survey (DOT)**

**Finding:** **20 lb Al = ~8″ OD** (won’t fit Madcow 8″ ID). **Largest CGA-326 bottle that fits Madcow 8″** is **Catalina NO15** (~6.89″ OD) via RFQ. Retail add-to-cart for CGA-326 stops at **10 lb** (GCS/Amazon) or jumps to **20 lb** (too wide).

| Part / class | N₂O capacity | OD | Buyable? | Link | Fits Madcow 8″ ID? |
| ----- | ----- | ----- | ----- | ----- | ----- |
| **Locked — Catalina NO15 + CGA-326** | **15 lb / 6.8 kg** | **6.89″** | **OEM / distributor RFQ** | [Specs](https://www.catalinacylinders.com/markets/nitrous-oxide/) · [NO15](https://www.catalinacylinders.com/product/no15/) · [Buy via distributor](https://www.catalinacylinders.com/buy) · valve [Sherwood CGA326](https://gascylindersource.com/shop/nitrous-oxide-valves/sherwood-nitrous-oxide-valve-cga326-1-125-12-unf/) | **Yes** (~0.47″ radial clearance) |
| GCS / Amazon 10 lb + CGA-326 | 10 lb / 4.5 kg | 7.0″ | Yes — add to cart | [GCS 10 lb](https://gascylindersource.com/shop/nitrous-oxide-cylinders/new-10-lb-aluminum-n2o-cylinder/) · [Amazon B09PFDKQ9G](https://www.amazon.com/dp/B09PFDKQ9G) | Yes — **backup / interim only** |
| GCS 5 lb + CGA-326 | 5 lb / 2.3 kg | 5.25″ | Yes | [GCS 5 lb](https://gascylindersource.com/shop/nitrous-oxide-cylinders/new-5-lb-aluminum-n2o-cylinder/) · [Amazon B09PFG4NGL](https://www.amazon.com/dp/B09PFG4NGL) | Yes (short on ox) |
| GCS / Amazon 20 lb + CGA-326 | 20 lb / 9.1 kg | **8.0″** | Yes | [GCS 20 lb](https://gascylindersource.com/shop/nitrous-oxide-cylinders/20-lb-aluminum-n2o-cylinder-with-handle/) | **No** |
| Racing NX / NOS 15 lb (e.g. **11151**) | 15 lb | 6.89–7″ | Yes | [NX 11151](https://www.tickperformance.com/nitrous-express-15lb-bottle-w-standard-45-valve-6-89-dia-x-26-69-tall-with-gauge-11151/) | Body yes — **wrong valve** |

**Design rules (compatibility & safety)**

* Wetted metals: **316 / 316L SS only** (no brass, bronze, zinc-plated, or carbon-steel fittings in the N₂O path).  
* Seals / hose liner: **PTFE** (or FEP/PCTFE). No silicone. No hydrocarbon grease — use PFPE (Krytox-type) only if lubricant is required.  
* **CGA-326 bullet nose = metal-to-metal seal** — no PTFE tape on the CGA interface. Tape only on NPT threads; leave 1–2 male threads bare so shreds cannot enter the stream.  
* **One remote MAIN valve** (NOS 18045NOS) opens/closes oxidizer to the chamber. **One manual bleed** on a tee vents to atmosphere after the cylinder hand valve is closed.  
* Note: 18045NOS has a **0.125″ orifice** and **1/8″ NPT outlet** — fine for early / lower-flow static tests; with **NO15** (~50% more ox than 10 lb) expect possible flow starvation on long burns — plan to upgrade MAIN to a larger N₂O solenoid or a remote-actuated 316SS ball valve if ṁ_ox is limited.  
* Whip-check every pressurized flex hose. Degrease / solvent-clean all wetted parts before assembly; **cap/plug open ports** when disconnected so dust and oil cannot enter the oxidizer path. Use **PFPE grease (Krytox)** only sparingly on O-rings / thread backs if a lubricant is needed — never hydrocarbon grease.

**Feed-system topology (attach filled tank → fire)**

Gender key: **MNPT** = male NPT, **FNPT** = female NPT. Hex nipples join two FNPT ports.

```
[Filled NO15 tank · CGA-326 valve]           ← Catalina NO15 (RFQ); 10 lb GCS = backup only
        │
        │  (#1) CGA-326 → 1/4″ MNPT 316SS adapter
        │       CGA bullet nose: metal-to-metal, NO tape
        │       free end: 1/4″ MNPT
        ▼
(#2) PTFE/SS braid hose  1/4″ FNPT  ×  1/4″ MNPT     +  (#3) whip check
        │                 ▲ screws onto adapter          across hose ends
        │                 └──────────────┘
        │  hose MNPT end
        ▼
(#9) optional 316SS inline filter  (1/4″ FNPT × 1/4″ FNPT typical)
        │  if used: hose MNPT → filter FNPT;
        │  then (#7) 1/4″ MNPT×MNPT hex nipple → filter FNPT out → next FNPT
        │  if omitted: hose MNPT screws straight into solenoid IN
        ▼
(#5) NOS 18045NOS MAIN solenoid
        │  IN  = 1/4″ FNPT  ← hose MNPT (or nipple from filter)
        │  OUT = 1/8″ FNPT
        ▼
(#8) 1/8″ MNPT close nipple  →  screws into solenoid OUT
        ▼
(#8) reducing hex bushing  1/4″ MNPT × 1/8″ FNPT
        │  1/8″ FNPT ← nipple;  free end = 1/4″ MNPT
        ▼
(#4) FITOK SS-PT-NS4 tee  (all three ports 1/4″ FNPT)
        │
        │  bushing 1/4″ MNPT → tee run/inlet FNPT
        │
        ├──── (#7) 1/4″ MNPT×MNPT hex nipple ────► chamber / injector line
        │         (tee FNPT ← nipple → injector FNPT or adapter)
        │
        └──── (#7) 1/4″ MNPT×MNPT hex nipple ────► (#6) NOSHOK 402-FFS bleed
                  (tee FNPT ← nipple → bleed FNPT)
                        │
                        │  other bleed port = 1/4″ FNPT
                        ▼
                  vent to atmosphere
                  (open, or short tube on another 1/4″ MNPT nipple)
```

**Nipple / adapter count for this diagram:** (3–4)× 1/4″ MNPT×MNPT hex nipples (#7); (1)× 1/8″ MNPT close nipple + (1)× 1/4″×1/8″ reducing bushing (#8). Extra 1/4″ nipple needed only if the filter is FNPT×FNPT.

### **1.1 Shopping list — order these (direct add-to-cart)**

| # | Role | Exact part / what to select | Qty | Est. $ | Where to order (direct link) |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 0 | **Tank (locked)** | **Catalina NO15** — **15 lb** Al N₂O, **CGA-326**, **6.89″ OD × ~23.1″**, DOT-3AL, ships empty | 1 | RFQ | **RFQ:** [Catalina sales](mailto:sales@catalinacylinders.com) · [how to buy](https://www.catalinacylinders.com/buy) · [specs](https://www.catalinacylinders.com/markets/nitrous-oxide/) · GCS special-order **866-395-5049**. Valve: [Sherwood CGA326 1.125-12](https://gascylindersource.com/shop/nitrous-oxide-valves/sherwood-nitrous-oxide-valve-cga326-1-125-12-unf/). **Backup:** [GCS 10 lb](https://gascylindersource.com/shop/nitrous-oxide-cylinders/new-10-lb-aluminum-n2o-cylinder/). **Do not buy** NX 11151. |
| 1 | Cylinder adapter | **CGA-326 → 1/4″ MNPT**, **316/316L SS**, bullet-nose (not brass) | 1 | **~63** | **Preferred:** [ASG CGA326SS](https://www.asgequipment.com/stainless-steel-cga-cylinder-connection-326-cga-x-1-4-npt-male-model-cga326ss/) ($63). Budget/verify: [Amazon B0CKQTRLR4](https://www.amazon.com/CGA326-SUS316L-Stainless-Fitting-Connector/dp/B0CKQTRLR4) (confirm 316L + CGA-326→1/4 MNPT before checkout). Premium: [Ideal Vac SEQ3264SSL](https://www.idealvac.com/CGA-326-Gas-Regulator-Inlet-to-14-Male-NPT-Fitting-Stainless-Steel-Long-PN:-SEQ3264SSL/pp/P109510) (~$227). **Do not buy brass / chrome-plated brass CGA-326 kits.** |
| 2 | Flex hose | FITOK PTFE-lined SS braid, **1/4″ nom.**, **1/4″ FNPT × 1/4″ MNPT**, **3000 psi**, ~18″ | 1 | ~80 | [Amazon B0F1XCWJKM](https://www.amazon.com/FITOK-PTFE-Lined-Connections-Chemically-Compatible/dp/B0F1XCWJKM) — select **18″** and **FNPT × MNPT** |
| 3 | Whip check | Hose-to-hose safety cable for ~1/2–1-1/4″ OD flex | 1 | ~15 | [Becker Safety MI-178-WB1](https://beckersafety.com/products/whip-check-1-2-1-1-4-safety-cable-1-8-x-20) |
| 4 | Tee | **FITOK SS-PT-NS4** — **1/4″ F-NPT ×3**, 316SS (not 1/8″ SS-PT-NS2) | 1 | ~25–40 | [Amazon B0B6D7MQJH](https://www.amazon.com/FITOK-Stainless-Female-Fitting-SS-PT-NS4-10K/dp/B0B6D7MQJH) — **confirm title says 1/4″ and SS-PT-NS4 before checkout** |
| 5 | Remote MAIN valve | **NOS 18045NOS** — SS body, PTFE plunger, **1/4″ NPT in / 1/8″ NPT out**, NC | 1 | ~275–290 | [Summit Racing NOS-18045NOS](https://www.summitracing.com/parts/nos-18045nos) or [AutoZone 18045NOS](https://www.autozone.com/p/nos-nitrous-oxide-system-nitrous-oxide-solenoid-18045nos/694392) |
| 6 | Manual bleed | **NOSHOK 402-FFS** — 1/4″ F-NPT × F-NPT, **316SS**, hard seat | 1 | list | [MassMeasure 402-FFS](https://massmeasure.com/product/noshok-402-ffs-1-4-npt-female-x-female-316-ss-hard-seat-needle-valve/) (FKM stem O-ring is N₂O-compatible; optional PTFE packing if preferred) |
| 7 | 1/4″ hex nipples | **316SS** 1/4″ MNPT × 1/4″ MNPT | 3–4 | ~7 ea | [BFO 4027-N-HEX](https://www.buyfittingsonline.com/stainless-steel-fittings-high-pressure-hex-nipple-4500-psi-316ss-psig-75001-4-in-x-1-4-in-npt-threads-4027-n-hex/) (~$6.97, 8100 psi). Alt: [Ideal Spectroscopy Swagelok SS-4-HN](https://www.idealspectroscopy.com/Swagelok-Male-NPT-Hex-Nipple/pp/P1012990) |
| 8 | 1/8→1/4 adapter | **316SS** reducing hex bushing **1/4″ MNPT × 1/8″ FNPT** + **1/8″ MNPT close nipple** | 1 set | ~12 | Bushing: [BFO 4026-NM](https://www.buyfittingsonline.com/stainless-steel-fittings-high-pressure-bushing-4500-psi-316ss-1-4-in-male-x-1-8-in-female-npt-threads-4026-nm/) (~$6.56). Close nipple: [BFO 4027-M-CLOSE](https://www.buyfittingsonline.com/stainless-steel-fittings-high-pressure-close-nipple-316ss-psig-91001-8-in-x-1-8-in-npt-threads-4027-m-close/). **BFO $40 order minimum** — order #7+#8+#10 together. |
| 9 | Inline filter (recommended) | **316SS** inline particulate filter, **1/4″ FNPT**, **≥3000 psi** | 1 | ~120+ | Preferred NPT: [Swagelok SS-4F4-7](https://products.swagelok.com/en/c/inline-filters/p/SS-4F4-7) via local distributor (~7 µm). Alt: [McMaster sintered filters](https://www.mcmaster.com/products/sintered-filters/) → filter **1/4″ NPT**, **316 stainless**, **≥3000 psi** |
| 10 | Thread seal, lube & port covers | Oxygen-compatible **PTFE tape** + **Krytox GPL-205** + **316SS 1/4″ NPT caps/plugs** | 1 kit | ~30–50 | Grease: [Amazon Krytox GPL-205 B00MWLDALQ](https://www.amazon.com/Krytox-Grease-Pure-PFPE-PTFE/dp/B00MWLDALQ) or [McMaster 10195K19](https://www.mcmaster.com/10195K19/). Caps (FNPT): [BFO 4028-N](https://www.buyfittingsonline.com/stainless-steel-fittings-high-pressure-pipe-cap-4500-psi-316ss-1-4-in-npt-threads-4028-n/) ×2–4. Plugs (MNPT): [BFO 3025-N](https://www.buyfittingsonline.com/pipe-fittings-stainless-steel-3000-lb-forged-1-4-in-threaded-npt-hex-head-plug-316-ss-3025-n/) ×2–4. PTFE tape: [McMaster PTFE tape (oxygen-compatible)](https://www.mcmaster.com/products/ptfe-tape/) |

**Rough feed-system hardware total (ex-tank, preferred path):** ~$520–650 (ASG CGA + BFO fittings batch). Ideal Vac CGA alone adds ~$164 vs ASG.

### **1.2 Operating / assembly notes**

1. Verify cylinder valve is stamped **CGA-326** (not CGA-660).  
2. Install whip check **fully extended (no slack)** across the hose ends.  
3. Wire MAIN solenoid through a **remote pad relay** and a heavy 12 V battery at the pad (~11.5 A draw). Keep open time short; coil heats on long duty.  
4. **Safe depressurize:** close cylinder hand valve → open MAIN remotely if needed → open manual bleed to atmosphere → approach only when gauge/feel confirms lines are empty. Never walk up with the cylinder valve open.  
5. Point bleed outlet away from people, motor, and ignition. Do not trap liquid N₂O between two closed valves without a bleed path.  
6. Cold nitrogen or empty-system leak check before first N₂O load; first N₂O ops are remote-only.

## **2\. Motor Hardware – 152 mm Diameter**

### **2.1 Chamber tube – custom Al (preferred) vs Contrail (backup)**

**Do not use Madcow G12 as a pressure vessel.** The airframe is structural for aero loads only.

**Contrail 152 mm reference (vendor-stated):** ID **5.5″ (139.7 mm)**, wall **0.25″ (6.35 mm)** → OD **6.0″ (152.4 mm)**. Convenient and overbuilt for 4 MPa; tube mass is roughly **3×** a hoop-sized custom wall. Keep as schedule backup only.

**Preferred flight chamber:** seamless **6061-T6** tube, **OD ≈ 152.4 mm**, wall from `ParaffinN2O_dimensioncalc` at MEOP = **4 MPa**:

| Layer | Policy | Approx. at 152.4 mm OD / 4 MPa |
| ----- | ----- | ----- |
| Sutton Al minimum | Eq. 15-3 hoop: \(d = p D / (2 \sigma_\mathrm{allow})\), \(\sigma_\mathrm{allow} = 276\,\mathrm{MPa}/1.5\) (yield SF) | **~1.66 mm** metal |
| Design Al metal | **1.50 ×** Sutton minimum (`CASE_WALL_DESIGN_MARGIN`) | **~2.5 mm** metal |
| Thermal liner | Fixed **3.0 mm**, non-structural (radial stack only) | **3.0 mm** |
| Design radial stack | 1.50×Al \+ liner (sets grain OD) | **~5.5 mm** → grain OD **~141 mm** |

**Effective hoop SF on yield** with the 1.50 metal margin ≈ **2.25** at MEOP (still hoop-only). Rough burst vs 6061-T6 UTS is on the order of **~2.5× MEOP** for a plain cylinder — closures, bolt holes, and welds often govern before the barrel does.

**Custom-tube rules**

* Buy tube with **material certs**; machine OD/ID for concentricity if stock is rough.  
* Target metal **~2.5 mm** (calculator design Al); do not fly the bare Sutton 1.66 mm value.  
* Always use a **thermal liner**; thin Al fails thermally before it yields if the liner is wrong.  
* Analyze **forward/aft closures, bolt circles, and nozzle carrier** separately (not covered by Sutton barrel sizing).  
* **Hydro-proof** every chamber before hot fire (typical target: proof ≥ **1.5× MEOP**; document the exact procedure in the safety plan).  
* Stay near **6″ OD** so centering rings stay simple; larger ID than Contrail’s 5.5″ is a free grain-volume win. Shrinking below 6″ is not required for tank packaging and loses the simple mount geometry.

***Flight Motor (\~15 kN·s budget / 4 MPa chamber pressure)***

| Component | Metric Spec / Notes | Est. Price (USD) | Supplier / Status | Notes |
| ----- | ----- | ----- | ----- | ----- |
| **Chamber tube (preferred)** | 6061-T6 extruded, **6.0″ OD × 0.125″ (3.18 mm) wall × 5.75″ ID**; cut to grain \+ prechamber \+ closures; \+ **3 mm** liner. Request **MTR / material cert**. | ~$37/ft (12″) · ~$122 (48″) | **Preferred:** [OnlineMetals 6″×0.125″ 6061-T6, pid 9559](https://www.onlinemetals.com/en/buy/aluminum/6-od-x-0-125-wall-x-5-75-id-aluminum-round-tube-6061-t6-extruded/pid/9559) (MTR available). Alt: [Speedy Metals same size](https://www.speedymetals.com/p-4648-6-od-x-0125-wall-tube-6061-t6-aluminum.aspx) | Stock wall is **~0.7 mm thicker** than calculator ~2.5 mm design Al — acceptable mass trade for COTS availability. Hydro-proof before hot fire. |
| **Thermal liner (phenolic)** | **Non-structural** ablative sleeve inside Al chamber. Target **OD ≈ 5.75″** (slip into chamber ID), **wall ≈ 3.0 mm (0.118″)**, length = grain \+ prechamber. Prefer **convolute-wound paper phenolic (NEMA XX)** for short burns; **canvas phenolic (NEMA CE)** if burn is longer / more heat soak. | RFQ (custom) · stock CE tube varies | **Preferred (custom rocket liner):** [Franklin Fibre / Lamitex — rocket motor tubes & liners](https://www.lamitex.com/munition-rocket-tubes) — RFQ **XX or CE**, OD/ID/wall to match 5.75″ chamber ID ([propulsion blog](https://www.franklinfibre.com/blog/phenolic-tubes-for-rocket-propulsion); [info@franklinfibre.com](mailto:info@franklinfibre.com) · 800-233-9739). **Industrial stock tube:** [K-Mac Plastics CE canvas phenolic tubes](https://k-mac-plastics.net/ce-tubes.htm) · [LE linen phenolic tubes](https://kmac-plastics.net/le-tubes.htm) (machine OD/ID if needed). **Retail sheet/tube:** [McMaster Garolite / canvas phenolic](https://www.mcmaster.com/products/canvas-phenolic-laminate/) (CE tubes or sheet rolled as backup). **Hobby 152 mm sets (wrong OD for this chamber):** [Loki Research phenolic liners](https://lokiresearch.com/secure/store.asp?groupid=6112003225363) — sized for ~5.5″-ID / ¼″-wall cases (e.g. ARR ~5.47″ OD), **not** a drop-in for **5.75″ ID** custom tube. | Liner is thermal only — Al takes hoop. Do **not** use LOC/PML **airframe** phenolic as a pressure wall. Confirm slip fit + grain OD after ordering. Expect NRE/setup on Franklin custom quotes. |
| **Chamber tube (backup)** | Contrail 152 mm: **ID 5.5″ / wall 0.25″ / OD 6.0″** | ~400 | [Contrail 152 mm 26″ chamber](https://contrailrockets.com/product/152mm-26-inch-combustion-chamber) | Heavy vs custom; will **not** fit a standard 6″ MMT. Use only if custom tube slips. With Contrail, Loki/ARR **152 mm phenolic liner sets** become size-compatible. |
| **Airframe (preferred)** | Madcow **8″ G12**: **ID 7.825″ / OD 8.000″**, 48″ | ~602 | **[Madcow 8″ G12](https://www.madcowrocketry.com/8-g12-airframe/)** | Clears **NO15 6.89″** (and 7″ 10 lb backup) with margin. Airframe only — not a pressure vessel. Size tank bay for **~23.1″** NO15 length. |
| **Airframe (optional / demoted)** | Wildman **9″ G12**: ID 8.78″ / OD 9.005″ | ~280 (30″) / ~560 (60″) | [Wildman G12-9.0](https://wildmanrocketry.com/products/g12-9-0) | Only if stepping up to an **8″ OD** 20 lb bottle. Extra drag — avoid while NO15 is locked. |
| Centering rings (×2–3) | Custom: **OD = Madcow 8″ ID (7.825″)**; **ID = chamber OD (6.0″)**; **G10/FR4** 0.125″–0.187″ **or** lathe from **8″** 6061 round. Qty 2–3 | G10 ~$15–40 ea · Al slug ~$50–80 (≤1.5″ of 8″ bar) | **G10:** [SendCutSend G10/FR4](https://sendcutsend.com/materials/g10-fr4/) (DXF annulus). **Al stock (needs 8″ OD, not 6″):** [Speedy Metals 8″ 6061-T6511](https://www.speedymetals.com/p-2488-8-rd-6061-t6511-aluminum-extruded.aspx) (~$53/in). | **No stock 6″-in-8″ ring exists.** Do **not** buy Apogee 75/98 mm–in–8″ rings. **6″ solid bar is too small** for the ring OD — use **8″** bar or G10. Radial centering only — does **not** take thrust. |
| Thrust bulkhead | Forward stop: motor/injector face bears here; load into airframe or glued coupler. Machine from **8″** 6061 round (turn OD to 7.825″; lathe pilots/O-ring grooves; mill holes). | Slug ~$30–80 (0.5–1.5″ of 8″ bar) | **Preferred stock:** [Speedy Metals 8″ 6061-T6511](https://www.speedymetals.com/p-2488-8-rd-6061-t6511-aluminum-extruded.aspx). Alt catalog: [MetalsDepot 6061 round](https://www.metalsdepot.com/aluminum-products/aluminum-round-bar). | Needs **~7.825″ OD** — buy **8″** cylinder, not 6″. Sized for **peak** thrust \+ margin. |
| Aft motor retention | Bolted flange, screw retainer, or through-bolts into nozzle carrier / aft ring. Lathe from **6″** (chamber-side) and/or **8″** (airframe ring) 6061 round. | Slug ~$30–60 of 6″ · more if 8″ flange | **6″ chamber-class:** [Speedy Metals 6″ 6061-T6511](https://www.speedymetals.com/p-2482-6-rd-6061-t6511-aluminum-extruded.aspx) (~$30/in) · [MSP Metals 6″](https://www.mspmetals.com/product/6061-t6-aluminum-round-bar-6-dia/) (~$27/in) · [Metals4U 6″](https://www.metals4uonline.com/aluminum-round-bar-6061-6in/). **8″ airframe ring:** [Speedy 8″](https://www.speedymetals.com/p-2488-8-rd-6061-t6511-aluminum-extruded.aspx). | Prevents motor sliding aft out the boat-tail. Cut short discs; do not buy full 12″ unless making many parts. |
| Injector Plate | ~chamber ID / flange OD, showerhead or simple impinging pattern, sized for 4 MPa. Lathe blank from **6″** 6061 round; drill orifice pattern on mill. | Slug ~$30–90 (1–3″ of 6″ bar) | **Preferred:** [Speedy Metals 6″ 6061-T6511](https://www.speedymetals.com/p-2482-6-rd-6061-t6511-aluminum-extruded.aspx). Alt: [MSP 6″](https://www.mspmetals.com/product/6061-t6-aluminum-round-bar-6-dia/) · [Metals4U 6″](https://www.metals4uonline.com/aluminum-round-bar-6061-6in/) · [MetalsDepot R36 / 6061 round](https://www.metalsdepot.com/aluminum-products/aluminum-round-bar). | Design in SolidWorks → lathe \+ mill (or 3D print prototype). One short cut of 6″ bar can yield injector \+ closure blanks. |
| Fuel Grain (Flight) | Paraffin, length from calculator for **~1.13 kg** at O/F 6 (grain OD from wall stack) | ~72 | [Amazon AM Wax 25 lb B0DL6HLNQ4](https://www.amazon.com/dp/B0DL6HLNQ4) | Cast yourself. Run `ParaffinN2O_dimensioncalc` defaults (NO15 class). Grain OD ≈ case OD − 2×(Al \+ liner), **not** full 152 mm. |
| Nozzle Insert | Graphite blank large enough to machine throat + exit for nozzle carrier | ~95+ | [GraphiteStore 1.5″ OD × 24″ rod NC001370](https://www.graphitestore.com/fine-extruded-graphite-rod-1-5od-x-24l-nc001370) or larger OD from [fine-extruded catalog](https://www.graphitestore.com/Graphite/Plates-rods-and-tubes/Graphite-fine-extruded) | **Do not buy the $98 0.75″ OD tube** — too small. Size blank to nozzle-carrier ID. |
| Forward & Aft Closures | Aluminum flanges with O-ring grooves / pilot steps, matched to custom tube ID/OD. Lathe from **6″** 6061-T6/T6511 solid round. | Slug ~$30–90 ea blank (1–3″ of 6″ bar) | **Preferred:** [Speedy Metals 6″ 6061-T6511](https://www.speedymetals.com/p-2482-6-rd-6061-t6511-aluminum-extruded.aspx) (~$30/in; 12″ ≈ $333). Alt: [MSP Metals 6″ @ ~$27/in](https://www.mspmetals.com/product/6061-t6-aluminum-round-bar-6-dia/) · [Metals4U 6″ cut-to-length](https://www.metals4uonline.com/aluminum-round-bar-6061-6in/) · [MetalsDepot 6061 round (R36)](https://www.metalsdepot.com/aluminum-products/aluminum-round-bar). | Confirm O-ring dash numbers after final ID. Order **short cuts** (e.g. 2–6″ total length), not a full 4 ft stick, unless sharing stock across all lathe parts. |
| O-rings & Seals | High-temperature Viton; size to final groove (AS568-258 is ~5.984″ ID — Contrail-class; re-pick for custom ID) | ~50 | [Marco V1000-258](https://www.marcorubber.com/product/V1000-258) | Buy after closure drawings freeze. |

### **2.2 Motor mount in 8″ airframe (centering \+ axial lock)**

**Fit check:**

| Part | Typical OD | Fits Madcow 8″ (ID 7.825″)? |
| ----- | ----- | ----- |
| Chamber (preferred) | **6.0″** | Yes (~0.9″ radial gap) |
| Locked N₂O bottle (**Catalina NO15**) | **6.89″** | **Yes** (~0.47″ radial clearance) |
| Backup GCS 10 lb | **7.0″** | Yes (~0.4″ radial clearance) |
| 20 lb Al bottle | **8.0″** | **No** — do not use in this airframe |

Radial gap between **6″ chamber** and **8″** tube is intentional. Fill it with structure:

```
[nozzle] → chamber → [aft centering ring + aft retainer]
                  → [optional mid centering ring]
                  → [forward centering ring]
                  → [thrust bulkhead — takes forward thrust]
                  → tank / avionics bay
```

* **Centering rings:** stop side-to-side motion; epoxy into airframe (or into a removable coupler bay). Size OD to **7.825″** (Madcow 8″ ID), ID to **6.0″** chamber.  
* **Thrust bulkhead:** hard forward stop — do **not** rely on friction or epoxy on the chamber OD for thrust.  
* **Aft retainer:** positive lock so the motor cannot fall out aft under handling or recovery loads.  
* Tank OD drives **airframe** size; **do not** match chamber OD to the N₂O bottle.

***First Static Test Motor (\~10–12 kN·s) – Same ~152 mm OD***

| Component | Metric Spec / Notes | Est. Price (USD) | Supplier / Status | Notes |
| ----- | ----- | ----- | ----- | ----- |
| Chamber Tube | Same custom 6061-T6 path (shorter length OK); Contrail backup if needed | See §2.1 | Custom preferred | Prove hydro-proof \+ hot-fire on this article before flight length |
| Fuel Grain (Test) | Shorter paraffin grain, \~0.6–0.8 kg (partial NO15 fill or shorter burn) | From 25 lb wax | Same wax | Cast shorter version for first hot fires; full **~1.13 kg** for flight article |
| Injector Plate (Test) | Same plate as flight motor (or simpler test version) | From 6″ bar (above) | [Speedy 6″](https://www.speedymetals.com/p-2482-6-rd-6061-t6511-aluminum-extruded.aspx) / 3D print prototype | Use flight injector blank from 6″ Al round, or quick 3D printed test version |

## **3\. Instrumentation & Portable Static Test Stand**

| Component | Metric Spec / Notes | Est. Price (USD) | Supplier / Status | Notes |
| ----- | ----- | ----- | ----- | ----- |
| Load Cell | **≥500 kg** for early static; **≥1000 kg** for flight-class peaks. S-type or pancake, tension/compression | ~80–150 | Example S-type 200 kg only for cold-flow: [Amazon B0D2D5Z37T](https://www.amazon.com/Bolisila-Compression-Weighing-Transducer-Capacaity/dp/B0D2D5Z37T) — **upsell to ≥500 kg before hot fire**. Prior link [ATO 300 kg B08CKDPKZS](https://www.amazon.com/dp/B08CKDPKZS) is marginal | Spec of 150–200 kg is **undersized** for ~10–20 kN·s motors (avg thrust can exceed 250–400+ kgf; peaks higher) |
| Pressure Transducer | 0–10 MPa (0–1500 psi), **1/4″ NPT**, 0.5–4.5 V (or 0–5 V) on 5 V supply | ~79 | [DATAQ 2000500-1500H](https://www.dataq.com/products/accessories/pressure-sensor/2000361-hs-1500.html) — select **1/4-18 NPT** | 316SS wetted; 4 MPa chamber ≈ 580 psi sits mid-range. Avoid G1/4 (BSPP) Amazon sensors unless you add the correct adapter. |
| **T-slot frame rails (locked)** | European **2020** (20×20 mm) **T-slot** extrusion, **6063-T5**, anodized black, **400 mm / 15.75″** lengths — **4 pcs/pack** | ~15–25 / pack | **[Amazon B08Y8N7FD1](https://www.amazon.com/dp/B08Y8N7FD1)** (IXGNIJ) | Order **≥2 packs** for a portable box frame; M5 T-nuts \+ corner brackets for joints. 2020 is light — use triangulation / short spans; step up to **4040** if hot-fire peaks flex the frame. |
| Portable Test Stand Frame | Bolted **2020 T-slot** frame (above), load cell in-line, portable; motor cradle on rails | — | T-slot \+ 3D print cradle (reinforce with Al plate scrap from 6″ bar cuts if needed) | Keep lightweight and movable. Do **not** buy 6″ round bar just for the cradle — use leftover plate/disc scrap or 3D print. |
| Sensor Mounting Hardware | Custom plates/brackets for load cell and pressure transducer (T-slot compatible) | — | 3D print / thin Al plate scrap | Mount with M5 T-nuts into 2020 slots. Flat brackets ≠ 6″ round stock. |

## **4\. Ignition & Safety Equipment**

| Component | Metric Spec / Notes | Est. Price (USD) | Supplier / Status | Notes |
| ----- | ----- | ----- | ----- | ----- |
| Igniter | Contrail 24 V resistor igniter (Pyrodex pellet method) or Nakka KNO₃ + sugar | $1.50 ea | [Contrail 24 V igniter](https://contrailrockets.com/product/24-volt-igniter-48-inches-long-designed-for-75-mm-or-larger-motors) | Order Pyrodex pellets separately (local sporting goods / online — hazmat rules apply). Student KNO₃/sugar recipe is fine for first tests. |
| Remote Firing System | Long wires \+ relay or wireless trigger with safety interlock | $450 | [Contrail GSE single-pad 12/24 V](https://contrailrockets.com/product/gse-ground-support-equipment-single-pad-12-24-volt-system) | Non-negotiable for safety. Extension cords not included. |
| PPE & Fire Suppression | Face shield, FR clothing, ABC extinguisher \+ water source; chemical gloves | $100+ | Gloves: [Amazon LANON nitrile B07ZRM6SZN](https://www.amazon.com/dp/B07ZRM6SZN) (~$13). Face shield + extinguisher: local hardware. | Start collecting early |

---

### **Review summary (Jul 2026)**

* **Updated (Jul 2026):** Tank locked to **Catalina NO15** (~**6.8 kg** N₂O, **6.89″ OD**) via RFQ (GCS special-order / Catalina sales / local fill). GCS **10 lb** demoted to interim/backup. Calculator defaults: **1.13 kg** fuel, **15 kN·s**, O/F 6. NX 11151 still rejected.  
* **Updated:** Flight airframe **[Madcow 8″ G12](https://www.madcowrocketry.com/8-g12-airframe/)**; Wildman 9″ demoted. Centering rings **7.825″ × 6.0″**.  
* **Fixed:** CGA adapter preferred to **ASG $63** (vs Ideal Vac $227). Hex nipples / bushings consolidated on **BFO** direct SKUs.  
* **Fixed:** Graphite and load-cell links were wrong size / capacity.  
* **Fixed:** Pressure transducer given a direct **1/4″ NPT** DATAQ product page.  
* **Fixed:** Locked chamber diameter was incorrectly listed as 203.2 mm; motor is **152 mm** inside **8″** airframe.  
* **Fixed:** Madcow 8″ G12 moved to **airframe**; chamber is **not** a pressure vessel.  
* **Updated:** Chamber path preference flipped to **custom 6061-T6** via **[OnlineMetals 6″×0.125″ pid 9559](https://www.onlinemetals.com/en/buy/aluminum/6-od-x-0-125-wall-x-5-75-id-aluminum-round-tube-6061-t6-extruded/pid/9559)**; Contrail demoted to heavy backup.  
* **Updated:** Portable test-stand frame locked to **2020 T-slot** rails — **[Amazon B08Y8N7FD1](https://www.amazon.com/dp/B08Y8N7FD1)** (4× 400 mm / 15.75″, 6063-T5).  
* **Updated:** Motor Al parts (injector, closures, retention) sourced as **6″ 6061 solid round** ([Speedy](https://www.speedymetals.com/p-2482-6-rd-6061-t6511-aluminum-extruded.aspx) / [MSP](https://www.mspmetals.com/product/6061-t6-aluminum-round-bar-6-dia/) / [Metals4U](https://www.metals4uonline.com/aluminum-round-bar-6061-6in/)); airframe discs (bulkhead / Al rings) need **[8″ Speedy](https://www.speedymetals.com/p-2488-8-rd-6061-t6511-aluminum-extruded.aspx)** — 6″ stock is undersize for Madcow ID.  
* **Updated:** **Thermal liner** locked to phenolic — prefer custom **[Franklin Fibre / Lamitex XX or CE](https://www.lamitex.com/munition-rocket-tubes)** to **OD ≈ 5.75″ / wall ≈ 3 mm**; stock [K-Mac CE/LE tube](https://k-mac-plastics.net/ce-tubes.htm) or [McMaster Garolite](https://www.mcmaster.com/products/canvas-phenolic-laminate/) as alts. Hobby 152 mm Loki liners fit Contrail-class **5.5″ ID**, not this chamber.
