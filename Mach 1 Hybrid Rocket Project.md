# **Hybrid Motor Component List**

*Flight-Size Paraffin \+ N₂O Hybrid (152 mm) \+ Instrumented Static Test Stand*

Luke de Wet  •  Phase 0 – July 2026  •  Experimental Hybrid Rocket Project

## **Locked Targets**

* **Motor / chamber OD:** 152 mm (6") nominal — **not** 203.2 mm  
* **Airframe:** 203.2 mm (8") G12 — motor mounts inside 8" airframe  
* **Flight Motor Target:** \~20 kN·s total impulse, \~10 kg total propellant (≈ 8.2 kg N₂O \+ 1.8 kg paraffin), 4 MPa chamber pressure  
* **First Static Test Motor:** Same 152 mm diameter, \~10 kN·s impulse, shorter grain (easier/safer early testing)  
* **Primary Goal:** Get the rocket flying by December 2026 (performance targets are secondary on first flight)

## **Prioritized Ordering & Research Sequence**

1. **Now – July 15:** Order fixed N₂O tank (below) if not already purchased; price **≥500 kg** load cell (not 150–200 kg), pressure transducer, and decide chamber path (Contrail 152 mm vs custom Al tube). Start safety plan draft.  
2. **By July 20:** Finalize injector concept and SendCutSend drawings for injector plate \+ closures. Order long-lead items (load cell, transducer). Order oxidizer feed-system kit (Section 1) as one batch.  
3. **By July 25:** Design nozzle and motor retention in SolidWorks. Order chamber (Contrail or tube stock) and graphite nozzle blank sized for the nozzle carrier.  
4. **Late July – August:** Order igniter materials; cold-flow / leak-check oxidizer plumbing before any hot fire. Begin casting test grains.

## **1\. Oxidizer System (N₂O)**

**Operating model:** Fill / prep the **20 lb** cylinder elsewhere, then attach it to this fixed feed plumbing for static test. No remote pad-fill loop.

**Fixed tank (do not change):** 20 lb aluminum DOT N₂O cylinder with **CGA-326** valve — [Amazon B09PFCV1QK](https://www.amazon.com/dp/B09PFCV1QK) (~$175). Everything below is sized to that CGA-326 outlet and a **1/4″ NPT, 316 stainless + PTFE** feed standard (≥3000 psi / ≥20 MPa working class; exceeds the project ≥10 MPa floor).

**Design rules (compatibility & safety)**

* Wetted metals: **316 / 316L SS only** (no brass, bronze, zinc-plated, or carbon-steel fittings in the N₂O path).  
* Seals / hose liner: **PTFE** (or FEP/PCTFE). No silicone. No hydrocarbon grease — use PFPE (Krytox-type) only if lubricant is required.  
* **CGA-326 bullet nose = metal-to-metal seal** — no PTFE tape on the CGA interface. Tape only on NPT threads; leave 1–2 male threads bare so shreds cannot enter the stream.  
* **One remote MAIN valve** (NOS 18045NOS) opens/closes oxidizer to the chamber. **One manual bleed** on a tee vents to atmosphere after the cylinder hand valve is closed.  
* Note: 18045NOS has a **0.125″ orifice** and **1/8″ NPT outlet** — fine for early / lower-flow static tests; if the motor is flow-starved later, upgrade MAIN to a larger N₂O solenoid or a remote-actuated 316SS ball valve.  
* Whip-check every pressurized flex hose. Degrease / solvent-clean all wetted parts before assembly; **cap/plug open ports** when disconnected so dust and oil cannot enter the oxidizer path. Use **PFPE grease (Krytox)** only sparingly on O-rings / thread backs if a lubricant is needed — never hydrocarbon grease.

**Feed-system topology (attach filled tank → fire)**

Gender key: **MNPT** = male NPT, **FNPT** = female NPT. Hex nipples join two FNPT ports.

```
[Filled 20 lb tank · CGA-326 valve]          ← filled elsewhere, then attached
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
| 0 | **Tank (fixed)** | 20 lb Al N₂O cylinder, **CGA-326** valve, DOT | 1 | ~175 | [Amazon B09PFCV1QK](https://www.amazon.com/dp/B09PFCV1QK) |
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

***Flight Motor (\~20 kN·s, 4 MPa chamber pressure)***

| Component | Metric Spec / Notes | Est. Price (USD) | Supplier / Status | Notes |
| ----- | ----- | ----- | ----- | ----- |
| **Chamber tube** | Certified 152 mm combustion chamber (true 6″ OD; will **not** fit a standard 6″ motor-mount tube) | ~400 | [Contrail 152 mm 26″ chamber](https://contrailrockets.com/product/152mm-26-inch-combustion-chamber) | **Do not use Madcow G12 as chamber.** Alt: custom 6061-T6 tube only after pressure / wall-thickness analysis. |
| **8″ airframe** (flight vehicle) | 8″ G12 filament-wound tube, 48″ | ~765 | [Madcow 8″ G12 airframe](https://www.madcowrocketry.com/8-g12-airframe/) | Airframe only — mounts the 152 mm motor; not a pressure vessel. |
| Injector Plate | 152 mm diameter, showerhead or simple impinging pattern, sized for 4 MPa | — | SendCutSend | Design in SolidWorks → SendCutSend (aluminum) or 3D print prototype |
| Fuel Grain (Flight) | Paraffin, \~350–450 mm long × 152 mm diameter (≈ 1.8 kg) | ~72 | [Amazon AM Wax 25 lb B0DL6HLNQ4](https://www.amazon.com/dp/B0DL6HLNQ4) | Cast yourself. Start with simple cylindrical grain. |
| Nozzle Insert | Graphite blank large enough to machine throat + exit for 152 mm carrier | ~95+ | [GraphiteStore 1.5″ OD × 24″ rod NC001370](https://www.graphitestore.com/fine-extruded-graphite-rod-1-5od-x-24l-nc001370) or larger OD from [fine-extruded catalog](https://www.graphitestore.com/Graphite/Plates-rods-and-tubes/Graphite-fine-extruded) | **Do not buy the $98 0.75″ OD tube** — too small for this motor. Size blank to nozzle-carrier ID. |
| Forward & Aft Closures | 152 mm aluminum plates with O-ring grooves | — | SendCutSend | SendCutSend aluminum plates \+ machine O-ring grooves if needed |
| Motor Retention Hardware | Retention rings, bolts, or quick-release system for 152 mm motor | — | SendCutSend | SendCutSend aluminum \+ 3D printed parts where possible |
| O-rings & Seals | High-temperature Viton AS568-258 (~5.984″ ID) for ~6″ interfaces | ~50 | [Marco V1000-258](https://www.marcorubber.com/product/V1000-258) | Buy standard sizes in bulk; confirm groove sizes before ordering other dash numbers |

***First Static Test Motor (\~10 kN·s) – Same 152 mm Diameter***

| Component | Metric Spec / Notes | Est. Price (USD) | Supplier / Status | Notes |
| ----- | ----- | ----- | ----- | ----- |
| Chamber Tube | Same 152 mm chamber (reuse or shorter custom section) | See above | Contrail or custom | Use same chamber path as flight motor |
| Fuel Grain (Test) | Shorter paraffin grain, \~200–250 mm long (≈ 0.9–1.1 kg) | From 25 lb wax | Same wax | Cast shorter version for first hot fires |
| Injector Plate (Test) | Same 152 mm plate as flight motor (or simpler test version) | — | SendCutSend / 3D print | Use flight injector or quick 3D printed test version |

## **3\. Instrumentation & Portable Static Test Stand**

| Component | Metric Spec / Notes | Est. Price (USD) | Supplier / Status | Notes |
| ----- | ----- | ----- | ----- | ----- |
| Load Cell | **≥500 kg** for early static; **≥1000 kg** for flight-class peaks. S-type or pancake, tension/compression | ~80–150 | Example S-type 200 kg only for cold-flow: [Amazon B0D2D5Z37T](https://www.amazon.com/Bolisila-Compression-Weighing-Transducer-Capacaity/dp/B0D2D5Z37T) — **upsell to ≥500 kg before hot fire**. Prior link [ATO 300 kg B08CKDPKZS](https://www.amazon.com/dp/B08CKDPKZS) is marginal | Spec of 150–200 kg is **undersized** for ~10–20 kN·s motors (avg thrust can exceed 250–400+ kgf; peaks higher) |
| Pressure Transducer | 0–10 MPa (0–1500 psi), **1/4″ NPT**, 0.5–4.5 V (or 0–5 V) on 5 V supply | ~79 | [DATAQ 2000500-1500H](https://www.dataq.com/products/accessories/pressure-sensor/2000361-hs-1500.html) — select **1/4-18 NPT** | 316SS wetted; 4 MPa chamber ≈ 580 psi sits mid-range. Avoid G1/4 (BSPP) Amazon sensors unless you add the correct adapter. |
| Portable Test Stand Frame | Simple bolted steel/aluminum frame, load cell in-line, portable | — | SendCutSend | Keep lightweight and movable. Motor cradle: 3D print \+ metal reinforcement or SendCutSend |
| Sensor Mounting Hardware | Custom plates/brackets for load cell and pressure transducer | — | SendCutSend | Design for SendCutSend or 3D print |

## **4\. Ignition & Safety Equipment**

| Component | Metric Spec / Notes | Est. Price (USD) | Supplier / Status | Notes |
| ----- | ----- | ----- | ----- | ----- |
| Igniter | Contrail 24 V resistor igniter (Pyrodex pellet method) or Nakka KNO₃ + sugar | $1.50 ea | [Contrail 24 V igniter](https://contrailrockets.com/product/24-volt-igniter-48-inches-long-designed-for-75-mm-or-larger-motors) | Order Pyrodex pellets separately (local sporting goods / online — hazmat rules apply). Student KNO₃/sugar recipe is fine for first tests. |
| Remote Firing System | Long wires \+ relay or wireless trigger with safety interlock | $450 | [Contrail GSE single-pad 12/24 V](https://contrailrockets.com/product/gse-ground-support-equipment-single-pad-12-24-volt-system) | Non-negotiable for safety. Extension cords not included. |
| PPE & Fire Suppression | Face shield, FR clothing, ABC extinguisher \+ water source; chemical gloves | $100+ | Gloves: [Amazon LANON nitrile B07ZRM6SZN](https://www.amazon.com/dp/B07ZRM6SZN) (~$13). Face shield + extinguisher: local hardware. | Start collecting early |

---

### **Review summary (Jul 2026)**

* **Fixed:** Locked chamber diameter was incorrectly listed as 203.2 mm; motor is **152 mm** inside **8″** airframe.  
* **Fixed:** Madcow 8″ G12 moved to **airframe**; chamber is Contrail (or analyzed Al tube).  
* **Fixed:** CGA adapter preferred to **ASG $63** (vs Ideal Vac $227). Hex nipples / bushings consolidated on **BFO** direct SKUs.  
* **Fixed:** Graphite and load-cell links were wrong size / capacity.  
* **Fixed:** Pressure transducer given a direct **1/4″ NPT** DATAQ product page.
