# Static Fire Weekly Checklist

**Project.** Full-scale **152 mm paraffin / N₂O** hybrid motor on an instrumented portable stand.  
**Final goal.** One **safe, documented, full-scale static fire** using the stand-mounted **Amazon / GCS 20 lb Al + CGA-326** tank (~9.1 kg N₂O). No flight attempt in this plan.  
**Roles.** Adult/parent = N₂O custodian, fill account, final go/no-go, pad supervision. Builder = design, fabrication, procedures, data. Never solo N₂O or hot-fire work.  
**Companions.** [`Hybrid Motor Static Fire Project.md`](Hybrid%20Motor%20Static%20Fire%20Project.md) · [`research/N2O_paraffin_burn_rate/SAFETY_PROCEDURES_N2O_PARAFFIN.md`](research/N2O_paraffin_burn_rate/SAFETY_PROCEDURES_N2O_PARAFFIN.md) · [`research/Igniter Sourcing/IGNITER_SOURCING.md`](research/Igniter%20Sourcing/IGNITER_SOURCING.md)

**Assumption.** Work starts **mid-July 2026**. Target full-scale static in **late October / early November 2026** (adjust only with written gate slips). Weeks are Monday-start.

**Not legal advice.** Confirm fill rules, site permission, and local AHJ / fire-code constraints before any N₂O or hot-fire activity.

---

## Success criteria (end of campaign)

Check **all** before calling the campaign complete:

- [ ] Chamber **hydro-proofed** ≥ 1.5× MEOP and documented  
- [ ] Feed system **oxidizer-clean**, leak-checked, and remote MAIN/bleed proven  
- [ ] **20 lb CGA-326** tank on stand cradle; whip-check installed; fill account working  
- [ ] Instrumentation (load cell ≥500 kg, Pc transducer, video, timeline log) recording  
- [ ] Ignition sequence demonstrated (igniter → heat soak → MAIN open)  
- [ ] At least one **hot fire** with acceptable Pc / thrust traces and no uncontrolled event  
- [ ] Prefer: one **full-fill** (or planned full-duration) fire matching the 20 lb budget  
- [ ] Post-test inspection notes + data archived; abort/depressurize SOP exercised  

If any safety gate fails, **scrub and fix** — do not “push through” to hit a calendar date.

---

## Week 0 — Jul 13–19, 2026 · Freeze the plan & place long-lead orders

### Goals
Lock the static-only configuration, order the tank and long-lead hardware, start the written safety plan.

### Checklist
- [x] Read `Hybrid Motor Static Fire Project.md` end-to-end; confirm **20 lb Amazon/GCS + CGA-326** on stand (not in an airframe)  
- [x] Read `SAFETY_PROCEDURES_N2O_PARAFFIN.md`; list open questions for adult mentor  
- [x] Create a project binder (paper or drive): drawings, RFQs, certs, test logs, photos  
- [x] Order **[Amazon B09PFCV1QK](https://www.amazon.com/Aluminum-Nitrous-Cylinder-CGA326-Handle/dp/B09PFCV1QK)** or [GCS 20 lb](https://gascylindersource.com/shop/nitrous-oxide-cylinders/20-lb-aluminum-n2o-cylinder-with-handle/) (empty)  
- [x] Call local filler (e.g. Airgas Tallahassee) — confirm **customer-owned CGA-326** fill path in adult name  
- [x] Order **≥500 kg** load cell + **1/4″ NPT** 0–1500 psi transducer (DATAQ path in component list)  
- [x] Order / RFQ **6061-T6** chamber tube with MTR ([OnlineMetals pid 9559](https://www.onlinemetals.com/en/buy/aluminum/6-od-x-0-125-wall-x-5-75-id-aluminum-round-tube-6061-t6-extruded/pid/9559) or equivalent)  
- [x] Order **2020 T-slot** packs ([Amazon B08Y8N7FD1](https://www.amazon.com/dp/B08Y8N7FD1)) × ≥2 + M5 T-nuts / brackets  
- [x] Draft 1-page **safety plan outline**: site, standoff, PPE, abort, fire watch, emergency contacts  
- [x] Run `ParaffinN2O_dimensioncalc` with **~9.1 kg N₂O / O/F ~6** → freeze grain mass (~1.5 kg) and chamber length sketch  

### Gate to Week 1
Orders placed (or documented RFQ dates) for tank, chamber tube, load cell, transducer. Safety outline exists.

---

## Week 1 — Jul 20–26 · Injector / closures design + feed BOM

### Goals
Freeze injector and closure drawings; order all CGA-326 feed parts as one batch; start tank-cradle concept.

### Checklist
- [x] SolidWorks: injector plate (showerhead or simple pattern) for **4 MPa**, matched to chamber ID  
- [x] SolidWorks: forward + aft closures with O-ring grooves / pilots  
- [x] Order **6″ 6061** short cuts for injector + closures ([Speedy / MSP / Metals4U](https://www.speedymetals.com/p-2482-6-rd-6061-t6511-aluminum-extruded.aspx))  
- [ ] Place **feed-system cart** from Section 1.1 of the component list (CGA adapter, hose, whip-check, tee, NOS 18045NOS, bleed, nipples, Krytox, caps)  
- [ ] Sketch **stand layout**: motor rails + separate **8″ tank cradle** bay + load-cell thrust line  
- [ ] Quote/order phenolic liner from **Plastic-Craft** ([CE tube](https://plastic-craft.com/product/phenolic-ce-round-tube/) — **5.75″ OD × ~0.125″ wall**; call **(845) 358-3010** or quote form; sells to individuals). Fallback: Contrail chamber + [ARR 152 mm liner](https://alwaysreadyrocketry.com/product/standard-casting-tubes/)  
- [ ] Order graphite nozzle blank sized to carrier ID  
- [ ] Collect PPE: face shield, FR layer, gloves, ABC extinguisher, water source plan  
- [ ] Decide remote firing path (**preferred:** DIY dual-channel pad relays ~$50–150 or Half Cat RC ~$50–120; Contrail $450 GSE optional/overkill) and order parts  

### Gate to Week 2
Injector/closure drawings frozen enough to machine; feed-system parts ordered; stand layout sketched.

---

## Week 2 — Jul 27 – Aug 2 · Stand frame + tank cradle

### Goals
Build a rigid portable stand skeleton and a secure cradle for the 20 lb bottle.

### Checklist
- [ ] Assemble **2020** box frame; triangulate spans that will see thrust  
- [ ] Mount provisional motor cradle (print or scrap Al) for **6.0″** chamber  
- [ ] Build **tank cradle** for **8″ OD × ~27″** bottle: upright, strapped, tip-resistant, clear of plume  
- [ ] Route planned hose path so kick cannot tip the cylinder; leave room for whip-check  
- [ ] Mount load-cell brackets (even if cell not yet installed)  
- [ ] Confirm adult can physically move stand + empty tank without unsafe lifts  
- [ ] Write **site criteria**: hardstand or cleared ground, firebreak, wind, neighbors, no dry grass under plume  
- [ ] Identify test site landowner permission / date windows  

### Gate to Week 3
Stand holds motor mockup and empty tank without tipping; site criteria written.

---

## Week 3 — Aug 3–9 · Chamber receive / cut / liner path

### Goals
Receive chamber stock, cut to length, progress liner, start hydro-proof planning.

### Checklist
- [ ] Receive chamber tube; verify OD/ID/wall vs drawing; file MTR in binder  
- [ ] Cut chamber to grain + prechamber + closure stack length; deburr  
- [ ] Confirm liner ID/OD or machine phenolic to slip fit  
- [ ] Write **hydro-proof procedure**: fluid, proof pressure (≥1.5× MEOP), hold time, exclusion, dump  
- [ ] Source hydro pump / fittings / plugs for closures (or temporary proof ends)  
- [ ] Order O-rings only after final groove dash numbers freeze  
- [ ] Cast a **practice paraffin slug** (small) to validate melt/pour/cool process — adult present  
- [ ] Update safety plan with hydro-proof day roles  

### Gate to Week 4
Chamber cut; liner path real; hydro-proof procedure written; practice cast done or scheduled.

---

## Week 4 — Aug 10–16 · Machine injector, closures, nozzle carrier

### Goals
Machine critical pressure parts; keep chips/oil out of future N₂O path.

### Checklist
- [ ] Lathe / mill injector plate; record orifice count, diameter, Cd assumption  
- [ ] Machine forward and aft closures; trial-fit O-rings dry  
- [ ] Machine nozzle carrier + graphite insert (or schedule shop time)  
- [ ] Degrease all parts destined for oxidizer contact; bag/cap ports  
- [ ] Dry-assemble chamber + liner + closures (no grain yet); check concentricity  
- [ ] Install pressure-tap port for transducer (1/4″ NPT) if designed  
- [ ] Photograph as-built stack for binder  

### Gate to Week 5
Dry motor stack fits; injector orifices documented; parts cleaned and capped.

---

## Week 5 — Aug 17–23 · Hydro-proof + instrumentation wire-up

### Goals
Prove the chamber; get sensors talking before any propellant.

### Checklist
- [ ] Hydro-proof chamber assembly per written procedure; **pass** and document pressure/time  
- [ ] If fail: stop hot-fire planning; repair/re-machine; re-proof  
- [ ] Install load cell; verify polarity and calibration with known weights  
- [ ] Install Pc transducer; confirm excitation and DAQ scale (psi or MPa)  
- [ ] Sync video camera view of nozzle + stand clock / clap sync method  
- [ ] Build remote MAIN solenoid power path (12 V battery + relay + kill switch at observer)  
- [ ] Continuity-check igniter leads with **shunted** igniter; verify GSE arm/safe lamps  
- [ ] Print **depressurize card**: close cylinder → MAIN open if needed → bleed → approach  

### Gate to Week 6
Hydro-proof pass on file; load cell + Pc recording a dry “tap test”; remote power path works.

---

## Week 6 — Aug 24–30 · Feed-system assembly (inert)

### Goals
Build the full CGA-326 → MAIN → tee → injector / bleed tree **without** N₂O.

### Checklist
- [ ] Verify adapter and tank valve are both stamped **CGA-326**  
- [ ] Assemble feed tree per component-list diagram; PTFE tape on NPT only (not CGA nose)  
- [ ] Install whip-check **fully extended**  
- [ ] Cap open ports when work pauses  
- [ ] **Inert leak check** (GN₂ or shop air within fitting ratings — never exceed component limits); soap all joints  
- [ ] Cycle MAIN remotely; verify NC when power removed  
- [ ] Cycle bleed valve; confirm vent points away from operators and motor  
- [ ] Strap empty 20 lb tank into cradle; attach CGA adapter hand-tight then wrench to metal-to-metal seat per vendor practice  
- [ ] Walk the **approach ban**: nobody near stand while any pressure is planned  

### Gate to Week 7
Inert leak check clean; remote MAIN/bleed demonstrated; tank cradle fit verified with empty bottle.

---

## Week 7 — Aug 31 – Sep 6 · Grain casting (full-scale blank)

### Goals
Cast the full-scale paraffin grain (and a spare shorter grain if planning a reduced first fire).

### Checklist
- [ ] Freeze grain OD/ID/length from calculator + as-built liner ID  
- [ ] Build or verify mold; release agent compatible with paraffin  
- [ ] Cast **~1.5 kg** full-scale grain under adult supervision; controlled cool  
- [ ] Optional: cast **reduced** grain (~0.7–1.0 kg) for first hot fire  
- [ ] Inspect for cracks, voids, unbonds; reject bad grains — do not patch for hot fire  
- [ ] Weigh and photograph grains; log batch ID  
- [ ] Order / receive igniters + Pyrodex (or approved preheater materials) per igniter doc  
- [ ] Dry-fit grain in liner; confirm injector face clearance / prechamber length  

### Gate to Week 8
At least one inspection-passed grain ready; igniter materials on hand.

---

## Week 8 — Sep 7–13 · Ignition path + cold sequencing

### Goals
Prove ignition energy and GSE sequencing **without** a full oxidizer burn.

### Checklist
- [ ] Bench-test igniter continuity and all-fire on scrap (safe area, adult present)  
- [ ] Install igniter/preheater in motor mock or real stack per SOP  
- [ ] Time the sequence: **arm → igniter on → hold → MAIN open → MAIN close → safe**  
- [ ] Write final **countdown script** and abort words (“ABORT”, “SAFE”, “BLEED”)  
- [ ] Assign day-of roles: Firing Officer, Safety Officer, Data, Video, Runner (no spectators in zone)  
- [ ] Confirm standoff distance and radio/phone plan  
- [ ] Re-read hard-start / grain-crack notes in safety procedures  
- [ ] If using reduced first fire: document partial-fill target mass and scale method  

### Gate to Week 9
Written countdown + abort script; igniter path proven on scrap; roles assigned.

---

## Week 9 — Sep 14–20 · First N₂O fill practice (no hot fire)

### Goals
Adult-led fill, attach, depressurize, and dump/bleed practice with **no ignition**.

### Checklist
- [ ] Adult completes first **fill** of the 20 lb cylinder at supplier; transport upright/secured  
- [ ] At test site (or controlled area): attach filled tank to stand plumbing  
- [ ] Leak-check under N₂O with remote observation; **no approach while pressurized** if leak is suspected until depressurized  
- [ ] Practice **safe depressurize** card until it is muscle memory  
- [ ] Practice abort: power kill MAIN, close cylinder (when approach allowed post-depress), bleed  
- [ ] Log tank tare / gross / net if scale available  
- [ ] Return or store cylinder per supplier and safety rules (vented? secure? labeled?)  
- [ ] Debrief: what felt rushed? Update SOP  

### Gate to Week 10
Successful fill → attach → depressurize cycle with zero improvisation. No hot fire yet.

---

## Week 10 — Sep 21–27 · Motor load + dress rehearsal (inert / empty)

### Goals
Full dress rehearsal of the static day with everything except live N₂O burn.

### Checklist
- [ ] Load liner + grain + igniter into chamber; torque closures to recorded values  
- [ ] Mount motor on stand; verify thrust path into load cell  
- [ ] Connect feed to injector; whip-check on; tank empty or inert only for this week if preferred  
- [ ] Run **full countdown** with GSE, cameras, DAQ recording (no N₂O or with empty system only)  
- [ ] Verify data files save and are named with date/test ID  
- [ ] Walk exclusion zone; place extinguishers and water; clear combustibles  
- [ ] Final go/no-go checklist printed and laminated for pad box  
- [ ] Weather scrub criteria written (wind toward people/fuel, lightning, extreme heat, etc.)  

### Gate to Week 11
Dress rehearsal completes without missing steps; data path works; pad box stocked.

---

## Week 11 — Sep 28 – Oct 4 · Optional reduced-load hot fire

### Goals
First flame on the real article at **reduced** N₂O / shorter grain if you chose that path. Skip to Week 12 only if team and mentor agree to go straight to full-scale **and** all prior gates are green.

### Checklist
- [ ] Pre-test: grain inspection, hydro already passed, inert leak already passed this build  
- [ ] Partial fill or short MAIN open time as planned; log target  
- [ ] Exclusion zone set; roles briefed; weather OK  
- [ ] Arm → ignite → MAIN → burn → MAIN close → depressurize → approach only when safe  
- [ ] Save thrust, Pc, video; note anomalies (hard start, chuff, leak, flame attachment)  
- [ ] Post-test: inspect chamber, liner, injector, nozzle, stand, tank cradle  
- [ ] Go/no-go for full-scale: fix any findings before Week 12  

### Gate to Week 12
Either reduced fire acceptable **or** documented decision + risk acceptance to proceed to full-scale with mentor/adult sign-off.

---

## Week 12 — Oct 5–11 · Full-scale static fire prep

### Goals
Configure for the **20 lb / ~1.5 kg** class burn; freeze the test card.

### Checklist
- [ ] Install full-scale grain (inspection-passed)  
- [ ] Fresh igniter lot; dual initiator if planned  
- [ ] Confirm MAIN orifice adequate or accept shorter burn / note flow limit  
- [ ] Cal-check load cell and Pc the day before  
- [ ] Full tank fill scheduled; transport plan locked  
- [ ] Notify landowner / neighbors as required by site rules  
- [ ] Print test card: predicted Pc, predicted burn time, abort limits (e.g. Pc overshoot)  
- [ ] Sleep / fatigue check — scrub if team is exhausted  

### Gate to Fire Week
Adult and builder both willing to scrub; hardware and paperwork complete.

---

## Week 13 — Oct 12–18 · Full-scale static fire (primary window)

### Goals
Execute the campaign goal: instrumented full-scale static fire.

### Day-of checklist (in order)
- [ ] Weather / wind / fire danger OK  
- [ ] PPE on; extinguishers placed; phones charged; emergency contacts known  
- [ ] Stand inspection: bolts, cradle straps, whip-check, plume clear  
- [ ] Motor inspection: grain, seals, igniter shunt until arm  
- [ ] Instrumentation rolling; video rolling; clocks synced  
- [ ] Attach filled tank; leak scan from standoff; no approach if hissing  
- [ ] Zone clear; Firing Officer reads countdown script  
- [ ] **FIRE** per sequence  
- [ ] MAIN close; cylinder close when safe; bleed; confirm depressurized  
- [ ] Approach only on Safety Officer call  
- [ ] Photograph hardware; bag failed parts if any  
- [ ] Secure remaining N₂O per SOP  

### Immediate post-test
- [ ] Archive raw data + video with test ID  
- [ ] Rough impulse / burn-time estimate same day  
- [ ] Write anomaly list while memory is fresh  

### Gate
Hot fire complete **or** scrub documented with reason. Either outcome is success if safety held.

---

## Week 14 — Oct 19–25 · Contingency re-fire / data closeout

### Goals
If Week 13 scrubbed or data were incomplete, re-fire once. Otherwise close the binder.

### Checklist
- [ ] If re-fire needed: complete root-cause fixes; re-hydro or re-leak-check if seals disturbed  
- [ ] If success: integrate thrust curve; compare to `ParaffinN2O_dimensioncalc` / trajectory tools as desired  
- [ ] Update component list notes with as-flown (as-fired) reality (orifice Cd, burn time, usable ox)  
- [ ] Restock consumables; clean and cap oxidizer fittings  
- [ ] Final lessons-learned page in binder  
- [ ] Declare campaign **complete** when success criteria at top of this doc are checked  

---

## Standing rules (every week)

1. **Adult present** for casting, N₂O, hydro-proof at pressure, and any hot fire.  
2. **No hydrocarbon grease** on N₂O wetted parts — Krytox/PFPE only if needed.  
3. **Never approach** a pressurized system to “just check” a fitting. Depressurize first.  
4. **One remote MAIN**, one manual bleed, whip-check on every pressurized hose.  
5. **Scrub early** for weather, fatigue, missing parts, or gut-feel unease.  
6. Keep `Run Trajectory GUI.bat` / Model Trajectory for analysis if useful — it is **not** a go/no-go for static day.

---

## Quick reference links

| Item | Link / path |
|------|-------------|
| Component list | `Hybrid Motor Static Fire Project.md` |
| 20 lb tank (Amazon) | https://www.amazon.com/Aluminum-Nitrous-Cylinder-CGA326-Handle/dp/B09PFCV1QK |
| 20 lb tank (GCS) | https://gascylindersource.com/shop/nitrous-oxide-cylinders/20-lb-aluminum-n2o-cylinder-with-handle/ |
| Safety procedures | `research/N2O_paraffin_burn_rate/SAFETY_PROCEDURES_N2O_PARAFFIN.md` |
| Igniter sourcing | `research/Igniter Sourcing/IGNITER_SOURCING.md` |
| Motor GUI | `Run Motor GUI.bat` |
| Trajectory GUI (analysis only) | `Run Trajectory GUI.bat` |

---

## Document control

| Field | Value |
|-------|--------|
| Path | Repository root |
| Campaign end state | Full-scale static fire complete + data archived |
| Oxidizer | Amazon/GCS 20 lb Al + CGA-326 on stand |
| Start | Mid-July 2026 |
| Primary fire window | Mid-October 2026 |

*End of checklist.*
