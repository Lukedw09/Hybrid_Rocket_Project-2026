# **Hybrid Motor Static Fire Project**

*Full-Scale Paraffin + N₂O Hybrid (152 mm) · Instrumented Static Fire Stand · Component List*

Luke de Wet  •  Phase 0 – July 2026  •  Experimental Hybrid Rocket Project

## **Locked Targets**

* **Motor / chamber OD:** 152.4 mm (6″) nominal. Do **not** shrink below ~6″.  
* **Chamber path (preferred):** Custom **6061-T6** tube sized by `ParaffinN2O_dimensioncalc` (Sutton hoop + margins below). Contrail 152 mm is a heavy backup / reference only.  
* **Oxidizer tank (locked):** **Amazon / GCS 20 lb Al + CGA-326** (~**9.1 kg** N₂O, **~8″ OD**). Tank lives **outside the motor**, fixed to the **static test stand**, and feeds the chamber through the CGA-326 plumbing in Section 1.  
* **Full-scale static motor:** **4 MPa** chamber pressure. Oxidizer from locked **20 lb** fill ≈ **9.1 kg N₂O** (calculator at O/F ~6 → **~1.5 kg** paraffin; total propellant ≈ **10.6 kg**). Impulse class ≈ **~20 kN·s** if delivered Isp ≈ 194 s (stretch depends on usable fill and delivered Isp).  
* **Early / reduced-load statics (optional):** Same ~152 mm OD hardware with a **partial fill** or shorter grain for first hot fires before a full 20 lb burn.  
* **Primary Goal:** Complete a **safe, instrumented full-scale static fire** of this motor. There is **no flight / airframe goal** in this repository phase. Trajectory tools (`Run Trajectory GUI.bat`) remain available for analysis only.

## **Prioritized Ordering & Research Sequence**

1. **Now – July 15:** **Order Amazon/GCS 20 lb Al + CGA-326** (Section 1). Price **3× ≥500 kg** load cells (not 150–200 kg) + **3× HX711** + Arduino + pressure transducer. **Source custom 6061-T6 chamber tube** (material certs); keep Contrail only if custom lead time slips. Start safety plan draft. Confirm local **fill** account for customer-owned CGA-326 cylinder (parent/adult).  
2. **By July 20:** Finalize injector concept and lathe drawings for injector plate + closures. **RFQ/order short cuts of 6″ 6061 round bar** (Section 2.1). Order long-lead items (load cells, HX711s, transducer). Order oxidizer feed-system kit (Section 1) as one batch (plumbing unchanged — still CGA-326). Design **stand tank cradle** for the 8″ × ~27″ bottle.  
3. **By July 25:** Design nozzle and **stand motor cradle / thrust path** in SolidWorks. Order graphite nozzle blank for the nozzle carrier. Plan chamber hydro-proof.  
4. **Late July – August:** Order igniter materials; cold-flow / leak-check oxidizer plumbing before any hot fire. Begin casting test grains. Integrate tank mount + feed line on the portable stand.

**Week-by-week execution:** see [`STATIC_FIRE_WEEKLY_CHECKLIST.md`](STATIC_FIRE_WEEKLY_CHECKLIST.md).

## **1. Oxidizer System (N₂O)**

**Operating model:** Fill / prep the **stand-mounted** cylinder elsewhere (or at a controlled fill site), then attach it to this fixed feed plumbing on the static stand for the hot fire. No remote pad-fill loop. Tank is **not** packaged inside an airframe.

**Static tank (locked — add-to-cart path):** Medical/industrial **DOT aluminum** N₂O cylinder with **CGA-326** valve — **20 lb / ~9.1 kg N₂O**, **~8″ OD × ~27″** with handle.

* **Order this:** [Amazon 20 lb Al + CGA-326 + handle](https://www.amazon.com/Aluminum-Nitrous-Cylinder-CGA326-Handle/dp/B09PFCV1QK) (ASIN **B09PFCV1QK**) — same class as [GCS 20 lb Al + CGA-326](https://gascylindersource.com/shop/nitrous-oxide-cylinders/20-lb-aluminum-n2o-cylinder-with-handle/) (**SKU 20LBALVLV-326**): ~**8″ OD × 27.25″** (with valve/handle), empty ~23–25.5 lb, DOT/TC, neck **1.125-12 UNF**, **CGA-326**, ships empty.  
* **Fill path (adult/parent buyer):** Local filler (e.g. Airgas Tallahassee **850-576-2192**, 945 Yulee St) — customer-owned **CGA-326** fill (industrial/specialty/food-grade preferred over USP medical Rx path).  
* **Interim / backup only if 20 lb is delayed:** [GCS 10 lb Al + CGA-326](https://gascylindersource.com/shop/nitrous-oxide-cylinders/new-10-lb-aluminum-n2o-cylinder/) (~4.5 kg) or [Amazon 10 lb B09PFDKQ9G](https://www.amazon.com/dp/B09PFDKQ9G) — shorter burns / reduced impulse only.  
* **Do not buy:** NX 11151 / NOS Hi-Flo (CGA-660 / AN, not CGA-326).  
* **Do not pursue Catalina NO15 for packaging** — in-airframe fit no longer matters; the **20 lb** bottle is preferred capacity for the full-scale static.

Everything below is sized to that **CGA-326** outlet and a **1/4″ NPT, 316 stainless + PTFE** feed standard (≥3000 psi / ≥20 MPa working class; exceeds the project ≥10 MPa floor).

### **1.0 Tank diameter survey (DOT) — stand-mounted**

**Finding:** With the tank **on the stand** (not in an airframe), **8″ OD is fine**. Prefer the **20 lb** bottle for full-scale static impulse.

| Part / class | N₂O capacity | OD | Buyable? | Link | Stand OK? |
| ----- | ----- | ----- | ----- | ----- | ----- |
| **Locked — Amazon/GCS 20 lb + CGA-326** | **20 lb / 9.1 kg** | **8.0″** | Yes — add to cart | [Amazon B09PFCV1QK](https://www.amazon.com/Aluminum-Nitrous-Cylinder-CGA326-Handle/dp/B09PFCV1QK) · [GCS 20 lb](https://gascylindersource.com/shop/nitrous-oxide-cylinders/20-lb-aluminum-n2o-cylinder-with-handle/) | **Yes** — cradle on stand |
| GCS / Amazon 10 lb + CGA-326 | 10 lb / 4.5 kg | 7.0″ | Yes | [GCS 10 lb](https://gascylindersource.com/shop/nitrous-oxide-cylinders/new-10-lb-aluminum-n2o-cylinder/) · [Amazon B09PFDKQ9G](https://www.amazon.com/dp/B09PFDKQ9G) | Yes — **reduced-load backup** |
| GCS 5 lb + CGA-326 | 5 lb / 2.3 kg | 5.25″ | Yes | [GCS 5 lb](https://gascylindersource.com/shop/nitrous-oxide-cylinders/new-5-lb-aluminum-n2o-cylinder/) | Yes (short on ox) |
| Catalina NO15 + CGA-326 | 15 lb / 6.8 kg | 6.89″ | OEM RFQ only | [NO15](https://www.catalinacylinders.com/product/no15/) | Yes — unused; 20 lb preferred |
| Racing NX / NOS 15 lb (e.g. **11151**) | 15 lb | 6.89–7″ | Yes | [NX 11151](https://www.tickperformance.com/nitrous-express-15lb-bottle-w-standard-45-valve-6-89-dia-x-26-69-tall-with-gauge-11151/) | Body OK — **wrong valve** |

**Design rules (compatibility & safety)**

* Wetted metals: **316 / 316L SS only** (no brass, bronze, zinc-plated, or carbon-steel fittings in the N₂O path).  
* Seals / hose liner: **PTFE** (or FEP/PCTFE). No silicone. No hydrocarbon grease — use PFPE (Krytox-type) only if lubricant is required.  
* **CGA-326 bullet nose = metal-to-metal seal** — no PTFE tape on the CGA interface. Tape only on NPT threads; leave 1–2 male threads bare so shreds cannot enter the stream.  
* **One remote MAIN valve** (NOS 18045NOS) opens/closes oxidizer to the chamber. **One manual bleed** on a tee vents to atmosphere after the cylinder hand valve is closed.  
* Note: 18045NOS has a **0.125″ orifice** and **1/8″ NPT outlet** — fine for early / lower-flow static tests; with a **full 20 lb** burn expect possible flow starvation on long burns — plan to upgrade MAIN to a larger N₂O solenoid or a remote-actuated 316SS ball valve if ṁ_ox is limited.  
* Whip-check every pressurized flex hose. Degrease / solvent-clean all wetted parts before assembly; **cap/plug open ports** when disconnected so dust and oil cannot enter the oxidizer path. Use **PFPE grease (Krytox)** only sparingly on O-rings / thread backs if a lubricant is needed — never hydrocarbon grease.  
* **Stand tank integration:** Secure the 20 lb bottle upright (or vendor-approved orientation) in a **non-combustible cradle** bolted to the stand frame; strain-relieve the CGA adapter and flex hose so thrust / hose kick cannot tip the cylinder; keep cylinder valve accessible for emergency shutoff from a safe approach path only after depressurization SOP.

**Feed-system topology (attach filled tank → fire)**

Gender key: **MNPT** = male NPT, **FNPT** = female NPT. Hex nipples join two FNPT ports.

```
[Filled 20 lb tank · CGA-326 valve]        ← Amazon/GCS 20 lb on stand cradle
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
| 0 | **Tank (locked)** | **20 lb** Al N₂O, **CGA-326**, **~8″ OD × ~27″**, DOT, ships empty, with handle | 1 | Retail | **Preferred:** [Amazon B09PFCV1QK](https://www.amazon.com/Aluminum-Nitrous-Cylinder-CGA326-Handle/dp/B09PFCV1QK) · [GCS 20 lb](https://gascylindersource.com/shop/nitrous-oxide-cylinders/20-lb-aluminum-n2o-cylinder-with-handle/). **Backup:** [GCS 10 lb](https://gascylindersource.com/shop/nitrous-oxide-cylinders/new-10-lb-aluminum-n2o-cylinder/). **Do not buy** NX 11151. |
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
3. Wire MAIN solenoid through a **remote pad relay** and a heavy 12 V battery at the stand (~11.5 A draw). Keep open time short; coil heats on long duty.  
4. **Safe depressurize:** close cylinder hand valve → open MAIN remotely if needed → open manual bleed to atmosphere → approach only when gauge/feel confirms lines are empty. Never walk up with the cylinder valve open.  
5. Point bleed outlet away from people, motor, and ignition. Do not trap liquid N₂O between two closed valves without a bleed path.  
6. Cold nitrogen or empty-system leak check before first N₂O load; first N₂O ops are remote-only.  
7. Confirm tank cradle bolts and whip-check before every pressurization.

## **2. Motor Hardware – 152 mm Diameter**

### **2.1 Chamber tube – custom Al (preferred) vs Contrail (backup)**

**Preferred static chamber:** seamless **6061-T6** tube, **OD ≈ 152.4 mm**, wall from `ParaffinN2O_dimensioncalc` at MEOP = **4 MPa**:

| Layer | Policy | Approx. at 152.4 mm OD / 4 MPa |
| ----- | ----- | ----- |
| Sutton Al minimum | Eq. 15-3 hoop: \(d = p D / (2 \sigma_\mathrm{allow})\), \(\sigma_\mathrm{allow} = 276\,\mathrm{MPa}/1.5\) (yield SF) | **~1.66 mm** metal |
| Design Al metal | **1.50 ×** Sutton minimum (`CASE_WALL_DESIGN_MARGIN`) | **~2.5 mm** metal |
| Thermal liner | Fixed **3.0 mm**, non-structural (radial stack only) | **3.0 mm** |
| Design radial stack | 1.50×Al + liner (sets grain OD) | **~5.5 mm** → grain OD **~141 mm** |

**Effective hoop SF on yield** with the 1.50 metal margin ≈ **2.25** at MEOP (still hoop-only). Rough burst vs 6061-T6 UTS is on the order of **~2.5× MEOP** for a plain cylinder — closures, bolt holes, and welds often govern before the barrel does.

**Custom-tube rules**

* Buy tube with **material certs**; machine OD/ID for concentricity if stock is rough.  
* Target metal **~2.5 mm** (calculator design Al); do not hot-fire the bare Sutton 1.66 mm value.  
* Always use a **thermal liner**; thin Al fails thermally before it yields if the liner is wrong.  
* Analyze **forward/aft closures, bolt circles, and nozzle carrier** separately (not covered by Sutton barrel sizing).  
* **Hydro-proof** every chamber before hot fire (typical target: proof ≥ **1.5× MEOP**; document the exact procedure in the safety plan).  
* Stay near **6″ OD** so the stand cradle stays simple.

***Full-Scale Static Motor (~20 kN·s budget / 4 MPa chamber pressure)***

| Component | Metric Spec / Notes | Est. Price (USD) | Supplier / Status | Notes |
| ----- | ----- | ----- | ----- | ----- |
| **Chamber tube (preferred)** | 6061-T6 extruded, **6.0″ OD × 0.125″ (3.18 mm) wall × 5.75″ ID**; cut to grain + prechamber + closures; + **3 mm** liner. Request **MTR / material cert**. | ~$37/ft (12″) · ~$122 (48″) | **Preferred:** [OnlineMetals 6″×0.125″ 6061-T6, pid 9559](https://www.onlinemetals.com/en/buy/aluminum/6-od-x-0-125-wall-x-5-75-id-aluminum-round-tube-6061-t6-extruded/pid/9559) (MTR available). Alt: [Speedy Metals same size](https://www.speedymetals.com/p-4648-6-od-x-0125-wall-tube-6061-t6-aluminum.aspx) | Stock wall is **~0.7 mm thicker** than calculator ~2.5 mm design Al — acceptable mass trade for COTS availability. Hydro-proof before hot fire. |
| **Thermal liner (phenolic)** | **Non-structural** ablative sleeve inside Al chamber. Target **OD ≈ 5.75″** (slip into chamber ID), **wall ≈ 3.0 mm (0.118″)**, length = grain + prechamber. Prefer **NEMA CE** (or **XX**) tube; machine OD/ID if stock is close. | Quote (cut-to-length) | **Preferred (sells to individuals / hobbyists, no min order):** [Plastic-Craft Products — Phenolic CE round tube](https://plastic-craft.com/product/phenolic-ce-round-tube/) — use their **quote form** or call **(845) 358-3010** / [ecom@plastic-craft.com](mailto:ecom@plastic-craft.com) for **5.75″ OD × ~0.125″ wall × length** (stock menu is smaller OD; this size is special-order). Also [CE / LE / XX phenolic category](https://plastic-craft.com/product-category/phenolic/). **Alt RFQ:** [Professional Plastics CE tubes](https://www.professionalplastics.com/PHENOLICCETUBE). **Working web cart (wrong OD for 5.75″ chamber):** [ARR 152 mm phenolic liner set](https://alwaysreadyrocketry.com/product/standard-casting-tubes/) (~**5.45″ OD**, for Contrail-class **5.5″ ID** only). **Sheet only:** [McMaster Garolite CE](https://www.mcmaster.com/products/canvas-phenolic-laminate/). *K-Mac “Add to Order” cart is broken/dead. Franklin Fibre declined — B2B-only.* | Liner is thermal only — Al takes hoop. Confirm slip fit + grain OD after ordering. If Plastic-Craft cannot source ~5.75″ OD, fall back to Contrail chamber + ARR liner. |
| **Chamber tube (backup)** | Contrail 152 mm: **ID 5.5″ / wall 0.25″ / OD 6.0″** | ~400 | [Contrail 152 mm 26″ chamber](https://contrailrockets.com/product/152mm-26-inch-combustion-chamber) | Heavy vs custom. Use only if custom tube slips. With Contrail, Loki/ARR **152 mm phenolic liner sets** become size-compatible. |
| Injector Plate | ~chamber ID / flange OD, showerhead or simple impinging pattern, sized for 4 MPa. Lathe blank from **6″** 6061 round; drill orifice pattern on mill. | Slug ~$30–90 (1–3″ of 6″ bar) | **Preferred:** [Speedy Metals 6″ 6061-T6511](https://www.speedymetals.com/p-2482-6-rd-6061-t6511-aluminum-extruded.aspx). Alt: [MSP 6″](https://www.mspmetals.com/product/6061-t6-aluminum-round-bar-6-dia/) · [Metals4U 6″](https://www.metals4uonline.com/aluminum-round-bar-6061-6in/) · [MetalsDepot R36 / 6061 round](https://www.metalsdepot.com/aluminum-products/aluminum-round-bar). | Design in SolidWorks → lathe + mill (or 3D print prototype). One short cut of 6″ bar can yield injector + closure blanks. |
| Fuel Grain (Full-scale) | Paraffin, length from calculator for **~1.5 kg** at O/F 6 (grain OD from wall stack; sized to **20 lb / 9.1 kg** ox) | ~72 | [Amazon AM Wax 25 lb B0DL6HLNQ4](https://www.amazon.com/dp/B0DL6HLNQ4) | Cast yourself. Run `ParaffinN2O_dimensioncalc` with **20 lb** ox budget. Grain OD ≈ case OD − 2×(Al + liner), **not** full 152 mm. |
| Fuel Grain (Reduced first fire) | Shorter paraffin grain, ~0.7–1.0 kg with **partial 20 lb fill** or shorter MAIN open time | From 25 lb wax | Same wax | Optional first hot fire before full fill |
| Nozzle Insert | Graphite blank large enough to machine throat + exit for nozzle carrier | ~95+ | [GraphiteStore 1.5″ OD × 24″ rod NC001370](https://www.graphitestore.com/fine-extruded-graphite-rod-1-5od-x-24l-nc001370) or larger OD from [fine-extruded catalog](https://www.graphitestore.com/Graphite/Plates-rods-and-tubes/Graphite-fine-extruded) | **Do not buy the $98 0.75″ OD tube** — too small. Size blank to nozzle-carrier ID. |
| Forward & Aft Closures | Aluminum flanges with O-ring grooves / pilot steps, matched to custom tube ID/OD. Lathe from **6″** 6061-T6/T6511 solid round. | Slug ~$30–90 ea blank (1–3″ of 6″ bar) | **Preferred:** [Speedy Metals 6″ 6061-T6511](https://www.speedymetals.com/p-2482-6-rd-6061-t6511-aluminum-extruded.aspx) (~$30/in; 12″ ≈ $333). Alt: [MSP Metals 6″ @ ~$27/in](https://www.mspmetals.com/product/6061-t6-aluminum-round-bar-6-dia/) · [Metals4U 6″ cut-to-length](https://www.metals4uonline.com/aluminum-round-bar-6061-6in/) · [MetalsDepot 6061 round (R36)](https://www.metalsdepot.com/aluminum-products/aluminum-round-bar). | Confirm O-ring dash numbers after final ID. Order **short cuts** (e.g. 2–6″ total length), not a full 4 ft stick, unless sharing stock across all lathe parts. |
| Stand motor cradle / thrust lock | Clamps or rings that hold the **6.0″** chamber on the stand rails and take forward thrust into the load cell path | Scrap Al / 3D print + plate | Leftover 6″ bar discs or printed cradle + Al plate | **Not** an airframe mount — design for static axial load + thermal soak |
| O-rings & Seals | High-temperature Viton; size to final groove (AS568-258 is ~5.984″ ID — Contrail-class; re-pick for custom ID) | ~50 | [Marco V1000-258](https://www.marcorubber.com/product/V1000-258) | Buy after closure drawings freeze. |

### **2.2 Stand mounting (motor + tank)**

Radial packaging against an airframe is **out of scope**. On the portable stand:

```
[20 lb N₂O tank cradle] — CGA-326 → feed hose → MAIN → injector
                │
[load cell] ← [thrust bulkhead / forward stop] ← chamber ← [aft clamp] ← [nozzle]
```

* **Motor cradle:** Centers the 6″ chamber; positive aft stop so the motor cannot leave the rails under thrust or hose loads.  
* **Thrust path:** Forward stop into load cell (or load-cell inline link) — do **not** rely on friction alone.  
* **Tank cradle:** Separate from the motor; sized for **8″ OD × ~27″** bottle; straps/bolts rated for tip-over and hose kick. Keep flex hose short enough to limit whip energy, with whip-check installed.  
* Tank OD does **not** drive chamber OD.

## **3. Instrumentation & Portable Static Test Stand**

| Component | Metric Spec / Notes | Est. Price (USD) | Supplier / Status | Notes |
| ----- | ----- | ----- | ----- | ----- |
| Load Cell (**qty 3**) | **≥500 kg each** for early static; **≥1000 kg** preferred for full-scale peaks. S-type, tension/compression. Sum \(F_1+F_2+F_3\) for total thrust | ~80–150 **ea** | Example S-type 200 kg only for cold-flow wire-up: [Amazon B0D2D5Z37T](https://www.amazon.com/Bolisila-Compression-Weighing-Transducer-Capacaity/dp/B0D2D5Z37T) — **upsell to ≥500 kg ×3 before hot fire**. Prior [ATO 300 kg B08CKDPKZS](https://www.amazon.com/dp/B08CKDPKZS) is marginal | 150–200 kg is **undersized** for ~10–20 kN·s motors. Wiring / DAQ: [`docs/LOAD_CELL_ARDUINO.md`](docs/LOAD_CELL_ARDUINO.md) |
| HX711 amp (**qty 3**) | One amp per load cell; shared SCK + separate DT → Arduino | ~5–10 **ea** | **Preferred:** [SparkFun SEN-13879](https://www.sparkfun.com/sparkfun-load-cell-amplifier-hx711.html) ×3 · [Amazon SparkFun](https://www.amazon.com/dp/B079LVMC6X). Alt: [Adafruit #5974](https://www.adafruit.com/product/5974). Budget: [DIYmall 2-pack](https://www.amazon.com/dp/B010FG9RXO) ×2 | Set **80 SPS**. Full pin map + sketch in [`docs/LOAD_CELL_ARDUINO.md`](docs/LOAD_CELL_ARDUINO.md) |
| Arduino DAQ | Uno / Nano / Mega; log CSV over USB (3× thrust + Pc) | ~10–25 | Any 5 V Arduino with ≥4 free digital pins + `A0` | Library: [bogde/HX711](https://github.com/bogde/HX711) |
| Pressure Transducer | 0–10 MPa (0–1500 psi), **1/4″ NPT**, 0.5–4.5 V (or 0–5 V) on 5 V supply | ~79 | [DATAQ 2000500-1500H](https://www.dataq.com/products/accessories/pressure-sensor/2000361-hs-1500.html) — select **1/4-18 NPT** | 316SS wetted; 4 MPa chamber ≈ 580 psi sits mid-range. Wire Vout → Arduino `A0`. Avoid G1/4 (BSPP) Amazon sensors unless you add the correct adapter. |
| **T-slot frame rails (locked)** | European **2020** (20×20 mm) **T-slot** extrusion, **6063-T5**, anodized black, **400 mm / 15.75″** lengths — **4 pcs/pack** | ~15–25 / pack | **[Amazon B08Y8N7FD1](https://www.amazon.com/dp/B08Y8N7FD1)** (IXGNIJ) | Order **≥2 packs** for a portable box frame; M5 T-nuts + corner brackets for joints. 2020 is light — use triangulation / short spans; step up to **4040** if hot-fire peaks flex the frame. Extra rail length for **tank cradle** bay. |
| Portable Test Stand Frame | Bolted **2020 T-slot** frame (above), load cell in-line, portable; motor cradle on rails; **separate bay for 20 lb tank** | — | T-slot + 3D print cradle (reinforce with Al plate scrap from 6″ bar cuts if needed) | Keep lightweight and movable. Integrate tank cradle so cylinder cannot tip into the plume. |
| Sensor Mounting Hardware | Custom plates/brackets for load cell and pressure transducer (T-slot compatible) | — | 3D print / thin Al plate scrap | Mount with M5 T-nuts into 2020 slots. |

## **4. Ignition & Safety Equipment**

| Component | Metric Spec / Notes | Est. Price (USD) | Supplier / Status | Notes |
| ----- | ----- | ----- | ----- | ----- |
| Igniter (heater / initiator) | Prefer **Contrail 24 V resistor** + Pyrodex if site is up; else use alternatives in §4.2 | $1.50 ea (Contrail) · ~$3–15 (e-match / FirstFire packs) | Contrail: [24 V / 48″](https://contrailrockets.com/product/24-volt-igniter-48-inches-long-designed-for-75-mm-or-larger-motors) (site intermittent — call **928-208-5580** / info@ContrailRockets.com). Alts: [AeroTech FirstFire](https://aerotech-rocketry.com/) · [MJG Firewire via Apogee](http://www.apogeerockets.com/Peak-of-Flight/Newsletter527) · DIY nichrome / power-resistor heater | Resistor heaters are non-hazmat. E-matches / FirstFire light **pellets or a puck**, not paraffin alone. Dual initiators preferred. |
| Pyrodex pellets (preheater) | **Hodgdon Pyrodex 50/50** — **.50 cal / 50 grain** muzzleloader pellets (center hole for stacking on heater or e-match). **Not** Triple Seven unless you re-qualify. | ~$15 (24-card) · hazmat ship fee if online | **Preferred:** [Hodgdon BP5050](https://shop.hodgdon.com/pyrodex-50-50-pellets/) · [Muzzle-Loaders.com](https://muzzle-loaders.com/products/hodgdon-pyrodex-50-50-pellets-black-powder-substitute-50-cal-50-grains) · [MidwayUSA](https://www.midwayusa.com/product/1009299634). Local: Bass Pro / outdoor / gun shops (adult buyer). | Same class Pratt/Contrail call out for hybrid boosters. Prove pellet **count** on stand — do not invent a 20 kN·s recipe. |
| **Remote firing (preferred)** | **DIY dual-channel pad box:** arm key + continuity + FIRE (igniter) + MAIN (NOS solenoid); 12 V battery **at the stand**; long control cable (or RC) only switches low-current relay coils | **~$50–150** | Automotive relays (30 A), key switch, momentary FIRE, continuity LED, fuse, project box + 100–300 ft control cable. Build refs: [Half Cat RCFS](https://www.halfcatrocketry.com/rcfs) · [Waterloo RLCS](https://docs.waterloorocketry.com/electrical-gse/rlcs-v4/index.html) · common NAR-style relay launchers | **Fits this project.** You already need a pad-side relay for the ~11.5 A MAIN coil (§1.2). Remote **fire** is mandatory; the $450 flight GSE is not. |
| Remote firing (wireless alt) | Flysky FS-i6 / FS-i6X + 2.4 GHz RX + high-current RC switch relays for igniter + MAIN | **~$50–120** | [Half Cat Remote Control Firing System](https://www.halfcatrocketry.com/rcfs) (open build guide; ~$50 radio bundle) | Set RX **failsafe** so lost link **does not** fire and **closes** MAIN. Prove range and failsafe on the ground before any N₂O. |
| Remote firing (optional COTS) | Contrail single-pad hybrid GSE (fill / purge / arm / fire) | $450 (12/24 V, ~1000 ft) · ~$200 (12 V, ~300 ft sale) | [Contrail 12/24 V GSE](https://contrailrockets.com/product/gse-ground-support-equipment-single-pad-12-24-volt-system) · [Contrail 12 V GSE 300 ft](https://contrailrockets.com/product/gse-ground-support-equipment-single-pad-12-volt-system-300-feet-maximum-distance) | **Overkill for this static.** Built for **remote pad-fill** flight hybrids; this repo has **no remote fill** (tank pre-filled on the stand). The cheap 12 V unit is rated only for Contrail’s **8–22 W** solenoids + **10 A** fuse — **not** verified for NOS **18045NOS** (~11.5 A). Skip unless you later add Contrail-style fill/purge. |
| PPE & Fire Suppression | Face shield, FR clothing, ABC extinguisher + water source; chemical gloves | $100+ | Gloves: [Amazon LANON nitrile B07ZRM6SZN](https://www.amazon.com/dp/B07ZRM6SZN) (~$13). Face shield + extinguisher: local hardware. | Start collecting early |

### **4.1 Remote firing — why cheaper is enough**

**Finding (Jul 2026):** The listed **$450** Contrail 12/24 V GSE is real flight-hybrid ground support (fill + purge + arm + fire, long wired run). This campaign only needs:

1. **Remote IGNITER** (arm key, continuity check that cannot fire, momentary FIRE).  
2. **Remote MAIN** open/close for the NOS solenoid (heavy current at the **stand battery**, not through a long skinny cable).  
3. Adequate standoff for a static site (typically **100–300+ ft**, not necessarily 1000 ft).

Do **not** buy low-current model-rocket wireless boxes (e.g. Apogee ~$55 9 V systems) for Contrail 24 V resistor igniters or the MAIN solenoid — they cannot supply the current.

**Minimum safety features (any build):** removable arm key; continuity only; separate FIRE vs MAIN; fuse on pad power; lost-link / power-loss leaves MAIN **closed** and FIRE **open**; dry rehearsal of the countdown before any N₂O.

### **4.2 Contrail 24 V igniter — alternatives if the site is down**

Contrail’s store has been **intermittent**. The product itself is a cheap **non-hazmat dual-heater resistor** (~$1.50) that slides on a **1/8″** vent tube and lights **Pyrodex pellets** — not a unique chemistry. If you cannot order:

| Alt | What it replaces | How to use | Caveat |
| ----- | ----- | ----- | ----- |
| **Phone / email Contrail** | Ordering path | **(928) 208-5580** · info@ContrailRockets.com · overview: [Pratt Contrail page](https://pratthobbies.com/contrail.htm) | Prefer this before reinventing their heater |
| **E-match or AeroTech FirstFire + Pyrodex 50/50** | Resistor heater | Thread initiator through pellet center hole(s); tape stack; head-end or nozzle install per drawing | Common field practice; prove all-fire current on **your** pad cable; keep shunted until connect |
| **DIY nichrome / power-resistor heater + Pyrodex** | Contrail resistor | Same pellet stack; size for ~12–24 V pad battery; measure cold R and current | Closest functional clone; must qualify heat soak on a dry stack before N₂O |
| **Sugar–KNO₃ puck + nichrome** (Nakka / UCLA-style) | Pellets + heater | Cast preheater ring/puck sized to pre-chamber | Already in igniter research doc; hygroscopic — keep dry |
| **Short APCP slug + e-match** | Pellets | ~2 cm of 18–29 mm AP grain (range/mentor rules) | Used by Contrail flyers when pellets are scarce; **not** DIY APCP for a minor |
| **HyperTEK GOX + HV spark** | Whole ignition architecture | CTI HyperTEK fill/ignition module | **Not** a drop-in for custom paraffin / stand-mounted tank |

**Igniter deep-dive:** [`research/Igniter Sourcing/IGNITER_SOURCING.md`](research/Igniter%20Sourcing/IGNITER_SOURCING.md)  
**N₂O / paraffin safety:** [`research/N2O_paraffin_burn_rate/SAFETY_PROCEDURES_N2O_PARAFFIN.md`](research/N2O_paraffin_burn_rate/SAFETY_PROCEDURES_N2O_PARAFFIN.md)

---

### **Review summary (Jul 2026)**

* **Goal change:** Primary goal is **full-scale static fire** (not flight). Airframe / Madcow / Wildman / launch-site certification docs removed. Trajectory GUI retained for analysis only.  
* **Tank locked:** **Amazon/GCS 20 lb Al + CGA-326** (~**9.1 kg** N₂O, **8″ OD**), **stand-mounted outside the motor**. Catalina NO15 / in-airframe packaging demoted. Calculator defaults: **~1.5 kg** fuel, **~20 kN·s** class, O/F 6. NX 11151 still rejected.  
* **Fixed:** CGA adapter preferred to **ASG $63** (vs Ideal Vac $227). Hex nipples / bushings consolidated on **BFO** direct SKUs.  
* **Fixed:** Graphite and load-cell links were wrong size / capacity.  
* **Fixed:** Pressure transducer given a direct **1/4″ NPT** DATAQ product page.  
* **Fixed:** Locked chamber diameter was incorrectly listed as 203.2 mm; motor is **152 mm**.  
* **Updated:** Chamber path preference flipped to **custom 6061-T6** via **[OnlineMetals 6″×0.125″ pid 9559](https://www.onlinemetals.com/en/buy/aluminum/6-od-x-0-125-wall-x-5-75-id-aluminum-round-tube-6061-t6-extruded/pid/9559)**; Contrail demoted to heavy backup.  
* **Updated:** Portable test-stand frame locked to **2020 T-slot** rails — **[Amazon B08Y8N7FD1](https://www.amazon.com/dp/B08Y8N7FD1)** (4× 400 mm / 15.75″, 6063-T5), with **tank cradle bay** for the 20 lb bottle.  
* **Updated:** Motor Al parts (injector, closures, cradle discs) sourced as **6″ 6061 solid round** ([Speedy](https://www.speedymetals.com/p-2482-6-rd-6061-t6511-aluminum-extruded.aspx) / [MSP](https://www.mspmetals.com/product/6061-t6-aluminum-round-bar-6-dia/) / [Metals4U](https://www.metals4uonline.com/aluminum-round-bar-6061-6in/)).  
* **Updated:** **Thermal liner** preferred via **[Plastic-Craft CE tube](https://plastic-craft.com/product/phenolic-ce-round-tube/)** (individuals OK, no min — quote/call for **~5.75″ OD × 0.125″ wall**). *K-Mac web cart dead; Franklin Fibre B2B-only.* Working cart for Contrail path only: [ARR 152 mm](https://alwaysreadyrocketry.com/product/standard-casting-tubes/).  
* **Updated:** Remote firing preference flipped from **Contrail $450 GSE** (flight fill/purge overkill) to **DIY dual-channel pad relays ~$50–150** or **Half Cat RC ~$50–120**; COTS Contrail GSE optional only.  
* **Updated:** Igniter path documents **Contrail website outages** + alternatives (e-match/FirstFire, DIY resistor, sugar–KNO₃, APCP slug) and locks Pyrodex to **Hodgdon 50/50 (.50 cal / 50 gr)** with buy links.  
* **Renamed:** this document from *Mach 1 Hybrid Rocket Project* → **Hybrid Motor Static Fire Project**.  
* **Execution plan:** [`STATIC_FIRE_WEEKLY_CHECKLIST.md`](STATIC_FIRE_WEEKLY_CHECKLIST.md).
