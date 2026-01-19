# Comprehensive Mechanical Drawing Review Checklist

## Overview

This comprehensive checklist provides 80+ review items for mechanical construction documents (HVAC, plumbing, gas piping, and controls), organized by system and drawing type. Each item includes check description, applicable code references (IMC, IPC, ASHRAE), common mistakes, and pass/fail criteria.

**Integration with QA Workflow:**
This checklist directly maps to automated QA rules in the SKILL.md workflow (QA-401-MECH through QA-415-MECH series). Use this for manual review or as validation criteria for automated checks.

**How to Use This Checklist:**
- [ ] Mark each item as Pass, Fail, or N/A
- Document failures with specific drawing references
- Prioritize failures by severity (Critical, Major, Minor)
- Track corrections and re-review

---

## Section 1: Title Block and General Requirements (10 Items)

### Item 1.1: Project Information Complete
**Check:** Title block contains complete project name, address, owner information
**Code Reference:** Local jurisdiction requirements
**Common Mistakes:** Project address incomplete, owner contact outdated
**Pass Criteria:** All title block fields populated and current
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.2: Professional Seal Present
**Check:** Professional Engineer (PE) seal present on all required sheets
**Code Reference:** State licensing board requirements
**Common Mistakes:** Seal on cover sheet only, unsigned seal, expired license
**Pass Criteria:** Seal on all engineering sheets, signed, current date
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.3: Drawing Scale and Index
**Check:** Scale clearly shown, sheet index matches actual sheets
**Code Reference:** Best practice
**Common Mistakes:** Scale "NTS" overused, index outdated
**Pass Criteria:** Scales accurate, index complete and current
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.4: Code and Standards References
**Check:** IMC/IPC version, ASHRAE standards, local amendments noted
**Code Reference:** IMC 102, IPC 102
**Common Mistakes:** Code version not stated, ASHRAE 62.1 version unclear
**Pass Criteria:** All applicable codes/standards listed with versions
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.5: General Notes Complete
**Check:** General mechanical notes sheet complete and project-specific
**Code Reference:** IMC Chapter 3 (general requirements)
**Common Mistakes:** Generic notes copied from previous project
**Pass Criteria:** Notes tailored to project, no outdated information
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.6: Legend and Symbols
**Check:** Mechanical symbol legend complete and consistent with drawings
**Code Reference:** Best practice
**Common Mistakes:** Symbols on plans not in legend, unused symbols in legend
**Pass Criteria:** All plan symbols in legend, all legend symbols used
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.7: Abbreviations List
**Check:** Abbreviations list provided and consistent throughout
**Code Reference:** Best practice
**Common Mistakes:** Common abbreviations used but not defined
**Pass Criteria:** All abbreviations defined, usage consistent
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.8: Specification References
**Check:** Drawing notes reference applicable CSI Division 23 sections
**Code Reference:** Best practice
**Common Mistakes:** Spec references not updated with spec revisions
**Pass Criteria:** All spec references accurate and current
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.9: Discipline Coordination Notes
**Check:** Coordination notes reference electrical, plumbing, fire protection
**Code Reference:** Best practice
**Common Mistakes:** No cross-references to other disciplines
**Pass Criteria:** Coordination clearly noted where required
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.10: Energy Code Compliance Statement
**Check:** Energy code compliance statement shown (IECC/ASHRAE 90.1)
**Code Reference:** IECC 103.2, ASHRAE 90.1 Section 4.2.1
**Common Mistakes:** Energy code version not stated, compliance path unclear
**Pass Criteria:** Energy code version and compliance method clearly stated
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

---

## Section 2: HVAC Load Calculations (15 Items)

### Item 2.1: Load Calculation Method Stated
**Check:** Load calculation method clearly stated (ASHRAE, Manual J, other)
**Code Reference:** IMC 312.1
**Common Mistakes:** Method not documented, multiple methods mixed
**Pass Criteria:** Method clearly stated (e.g., "ASHRAE Fundamentals")
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.2: Design Conditions Documented
**Check:** Indoor and outdoor design conditions clearly documented
**Code Reference:** ASHRAE 90.1 Section 6.1.1, ASHRAE Handbook Fundamentals
**Common Mistakes:** Summer/winter outdoor conditions not stated
**Pass Criteria:** Indoor (72°F/50% RH typical) and outdoor temps shown
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.3: Calculation Sealed by PE
**Check:** Load calculation signed and sealed by PE
**Code Reference:** State licensing requirements
**Common Mistakes:** Calculation provided but not sealed
**Pass Criteria:** PE seal and signature on calculation
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.4: Building Envelope Data
**Check:** Wall, roof, window U-values and R-values documented
**Code Reference:** ASHRAE 90.1 Section 5, IECC Chapter 4
**Common Mistakes:** Generic values used instead of actual assembly values
**Pass Criteria:** Actual U/R-values from architectural specs used
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.5: Internal Load Assumptions
**Check:** Occupancy density, lighting, and equipment loads documented
**Code Reference:** ASHRAE 90.1 Table G3.1, ASHRAE Fundamentals
**Common Mistakes:** Unrealistic occupancy assumptions, plug loads omitted
**Pass Criteria:** Loads appropriate for occupancy type and use
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.6: Ventilation Load Included
**Check:** Outdoor air ventilation load included in calculation
**Code Reference:** IMC 403, ASHRAE 62.1
**Common Mistakes:** Ventilation load omitted or undersized
**Pass Criteria:** Ventilation load calculated and included
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.7: Zone-by-Zone Calculation
**Check:** Heating and cooling loads calculated for each zone/room
**Code Reference:** Best practice, ASHRAE Fundamentals
**Common Mistakes:** Whole-building load only, no zone breakdown
**Pass Criteria:** Individual zone loads calculated and documented
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.8: Peak Block Load Calculated
**Check:** Peak block (simultaneous) load calculated for equipment sizing
**Code Reference:** ASHRAE Fundamentals Chapter 18
**Common Mistakes:** Equipment sized on sum of zones (oversizing)
**Pass Criteria:** Peak block load calculated, not sum of zones
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.9: Safety Factors Appropriate
**Check:** Safety factors applied appropriately (10-20% typical)
**Code Reference:** Best practice
**Common Mistakes:** Excessive safety factors (>25%), compounding factors
**Pass Criteria:** Safety factors documented and reasonable (<20%)
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.10: Heating Load Calculation
**Check:** Heating load calculated for design winter conditions
**Code Reference:** ASHRAE Fundamentals Chapter 18
**Common Mistakes:** Heating load omitted in mild climates
**Pass Criteria:** Heating load calculated even in mild climates
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.11: Cooling Load Calculation
**Check:** Cooling load calculated for design summer conditions
**Code Reference:** ASHRAE Fundamentals Chapter 18
**Common Mistakes:** Solar heat gain not calculated correctly
**Pass Criteria:** Cooling load includes all components (sensible, latent, solar)
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.12: Humidity Load (Latent) Calculated
**Check:** Latent (humidity) load calculated and equipment selected accordingly
**Code Reference:** ASHRAE Fundamentals Chapter 18
**Common Mistakes:** Latent load omitted, equipment can't handle latent load
**Pass Criteria:** Latent load calculated, equipment adequate
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.13: Equipment Capacity vs. Load
**Check:** Selected equipment capacity matches calculated load
**Code Reference:** IMC 312.1
**Common Mistakes:** Equipment undersized or grossly oversized (>25%)
**Pass Criteria:** Equipment capacity 100-120% of calculated load
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.14: Load Summary Sheet Provided
**Check:** Load summary sheet showing total heating/cooling by zone and total
**Code Reference:** Best practice
**Common Mistakes:** Detailed calc provided but no summary
**Pass Criteria:** Summary sheet with zone and total loads clearly shown
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.15: Calculation Matches Equipment Schedule
**Check:** Equipment on plans matches equipment in load calculation
**Code Reference:** Best practice
**Common Mistakes:** Calculation shows different equipment than plans
**Pass Criteria:** Perfect match between calculation and plan equipment
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

---

## Section 3: Equipment Schedules (15 Items)

### Item 3.1: Equipment Schedule Complete
**Check:** Equipment schedule includes all required information columns
**Code Reference:** Best practice
**Common Mistakes:** Incomplete schedules missing key data
**Pass Criteria:** Schedule includes: tag, location, model, capacity, electrical, weight
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.2: Equipment Tags Match Plans
**Check:** Equipment tag designations on schedule match floor plans
**Code Reference:** Best practice
**Common Mistakes:** Tags on schedule don't match tags on plans
**Pass Criteria:** Perfect tag match between schedule and plans
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.3: Manufacturer and Model Number
**Check:** Equipment manufacturer and model number specified
**Code Reference:** Best practice, specification requirements
**Common Mistakes:** Generic "by manufacturer" or "TBD" in CD phase
**Pass Criteria:** Specific manufacturer and model number shown
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.4: Equipment Capacity Shown
**Check:** Heating/cooling capacity shown in appropriate units (tons, Btu/h, MBH)
**Code Reference:** IMC 312.1
**Common Mistakes:** Capacity missing or in unclear units
**Pass Criteria:** Capacity clearly shown in standard units
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.5: Airflow (CFM) Shown
**Check:** Airflow in CFM shown for all air-handling equipment
**Code Reference:** IMC 403.3
**Common Mistakes:** CFM not shown, or shown only as "see duct layout"
**Pass Criteria:** CFM clearly shown on equipment schedule
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.6: External Static Pressure Shown
**Check:** External static pressure (ESP) shown for fans and air handlers
**Code Reference:** Best practice, SMACNA
**Common Mistakes:** ESP not calculated or shown
**Pass Criteria:** ESP shown in inches w.g. (typical 0.5" to 2.0")
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.7: Electrical Characteristics
**Check:** Electrical characteristics shown (voltage, phase, MCA, MOCP)
**Code Reference:** NEC 440.4 (HVAC equipment)
**Common Mistakes:** MCA (Minimum Circuit Ampacity) or MOCP (Max OCPD) missing
**Pass Criteria:** Voltage, phase, MCA, and MOCP all shown
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.8: Equipment Weight Shown
**Check:** Operating weight shown for all equipment
**Code Reference:** IBC 1607 (structural loading)
**Common Mistakes:** Weight not shown, or shipping weight instead of operating
**Pass Criteria:** Operating weight (including fluids) shown in pounds
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.9: Equipment Dimensions
**Check:** Equipment dimensions (L x W x H) shown
**Code Reference:** Best practice
**Common Mistakes:** Dimensions not shown, causing rigging/access issues
**Pass Criteria:** Dimensions shown, verified to fit through access routes
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.10: Equipment Efficiency Ratings
**Check:** Efficiency ratings shown (SEER, EER, COP, AFUE, thermal efficiency)
**Code Reference:** ASHRAE 90.1 Tables 6.8.1-A through 6.8.1-K
**Common Mistakes:** Efficiency not shown, or doesn't meet code minimum
**Pass Criteria:** Efficiency shown and meets/exceeds code minimum
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.11: Sound Ratings Shown
**Check:** Equipment sound ratings shown in dBA or NC rating
**Code Reference:** Best practice, owner requirements
**Common Mistakes:** Sound ratings not specified for noise-sensitive areas
**Pass Criteria:** Sound ratings shown where required by owner or code
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.12: Coil Data (If Applicable)
**Check:** Heating/cooling coil data shown (entering/leaving air temps, rows)
**Code Reference:** Best practice
**Common Mistakes:** Coil data missing, causing inadequate heat transfer
**Pass Criteria:** Coil entering/leaving temps and performance shown
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.13: Equipment Location Shown
**Check:** Equipment location clearly indicated (room name or grid reference)
**Code Reference:** Best practice
**Common Mistakes:** Location shown as "TBD" or generic "roof"
**Pass Criteria:** Specific location shown, references floor plan
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.14: Accessories and Options Listed
**Check:** Required accessories listed (economizers, VFDs, filters, etc.)
**Code Reference:** ASHRAE 90.1 Section 6 (various requirements)
**Common Mistakes:** Code-required accessories not specified
**Pass Criteria:** All required accessories specifically listed
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.15: Coordinated with Electrical Schedule
**Check:** Equipment on mechanical schedule matches electrical load schedule
**Code Reference:** Best practice
**Common Mistakes:** Electrical characteristics don't match electrical drawings
**Pass Criteria:** Perfect coordination with electrical equipment schedule
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

---

## Section 4: Duct Layout and Sizing (15 Items)

### Item 4.1: Duct Sizes Shown on All Runs
**Check:** Duct width and height (or diameter) shown on all duct runs
**Code Reference:** Best practice
**Common Mistakes:** Duct sizes missing on return ducts, or "see schedule"
**Pass Criteria:** All supply and return ducts sized and labeled
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.2: Duct Sizing Method Documented
**Check:** Duct sizing method documented (equal friction, static regain, etc.)
**Code Reference:** ASHRAE Fundamentals Chapter 21
**Common Mistakes:** Method not stated, inconsistent sizing
**Pass Criteria:** Method clearly stated in general notes
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.3: Duct Velocity Limits Met
**Check:** Duct velocities within acceptable limits (supply: 1000-2500 fpm)
**Code Reference:** ASHRAE Fundamentals Chapter 21, SMACNA
**Common Mistakes:** Velocities too high (noise) or too low (space waste)
**Pass Criteria:** Velocities documented and within acceptable range
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.4: Diffuser/Register CFM Shown
**Check:** CFM shown at each supply diffuser and return grille
**Code Reference:** IMC 403.3
**Common Mistakes:** CFM not shown, or only shown on supply
**Pass Criteria:** CFM shown on all supply and return devices
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.5: Fire Dampers at Rated Penetrations
**Check:** Fire dampers shown at all duct penetrations through fire-rated assemblies
**Code Reference:** IMC 607.5.1
**Common Mistakes:** Fire dampers missing, or not UL-rated for application
**Pass Criteria:** Fire dampers shown at all required locations per IMC 607
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.6: Smoke Dampers (If Required)
**Check:** Smoke dampers shown where required by IBC (smoke control systems)
**Code Reference:** IBC 909, IMC 607.5.3
**Common Mistakes:** Smoke dampers confused with fire dampers
**Pass Criteria:** Smoke dampers shown if required by smoke control design
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.7: Volume Dampers Shown
**Check:** Volume (balancing) dampers shown on all branch runs
**Code Reference:** Best practice, SMACNA
**Common Mistakes:** No volume dampers, making TAB impossible
**Pass Criteria:** Volume damper shown on each branch for balancing
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.8: Access Doors for Dampers
**Check:** Access doors shown for all dampers requiring adjustment
**Code Reference:** IMC 306.5
**Common Mistakes:** Dampers inaccessible above ceiling
**Pass Criteria:** Access door within 10 feet of all adjustable dampers
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.9: Duct Insulation Specified
**Check:** Duct insulation type and thickness specified
**Code Reference:** IECC/ASHRAE 90.1 Section 6.4.4, IMC 604
**Common Mistakes:** Insulation not specified, R-value not shown
**Pass Criteria:** Insulation type, thickness, and R-value specified
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.10: Duct Construction Class Noted
**Check:** Duct construction class noted per SMACNA
**Code Reference:** IMC 603.2, SMACNA HVAC Duct Construction Standards
**Common Mistakes:** Duct gauge not specified, causing over/under-building
**Pass Criteria:** SMACNA class specified (typically Class 1 or 2)
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.11: Duct Support and Hanger Spacing
**Check:** Duct support requirements noted (typically 10 ft spacing)
**Code Reference:** SMACNA HVAC Duct Construction Standards
**Common Mistakes:** Support spacing not specified
**Pass Criteria:** Support/hanger spacing specified in general notes
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.12: Flexible Duct Limitations
**Check:** Flexible duct use limited (typically max 5 ft from rigid duct)
**Code Reference:** IMC 603.6
**Common Mistakes:** Excessive flexible duct use (high pressure drop)
**Pass Criteria:** Flexible duct limited to final connections, max length noted
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.13: Duct Routing Coordination
**Check:** Duct routing coordinated with structure, piping, and electrical
**Code Reference:** Best practice
**Common Mistakes:** Duct conflicts with beams, piping, or lights
**Pass Criteria:** Duct routing shown clear of all conflicts
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.14: Seismic Bracing Requirements
**Check:** Seismic bracing requirements noted for ductwork
**Code Reference:** IBC 1613, ASCE 7, SMACNA Seismic Restraint Manual
**Common Mistakes:** Seismic requirements not addressed in seismic zones
**Pass Criteria:** Seismic bracing requirements specified per local seismic zone
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.15: Return Air Plenum (If Used)
**Check:** Return air plenum clearly identified with CFM requirements
**Code Reference:** IMC 602.2
**Common Mistakes:** Plenum return not documented, combustibles not prohibited
**Pass Criteria:** Plenum return clearly shown, IMC 602.2 requirements noted
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

---

## Section 5: Piping Layout and Sizing (10 Items)

### Item 5.1: Pipe Sizes Shown on All Runs
**Check:** Pipe size (diameter) shown on all piping runs
**Code Reference:** Best practice
**Common Mistakes:** Pipe sizes missing on return/drain lines
**Pass Criteria:** All supply, return, and drain pipes sized and labeled
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.2: Pipe Material Specified
**Check:** Pipe material specified for each system (copper, steel, PVC, etc.)
**Code Reference:** IMC 605, IPC 605
**Common Mistakes:** Material not specified, generic "pipe"
**Pass Criteria:** Material clearly specified (e.g., "Type L copper")
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.3: Insulation Specified
**Check:** Pipe insulation type and thickness specified
**Code Reference:** IECC/ASHRAE 90.1 Section 6.4.4, IMC 604
**Common Mistakes:** Insulation not specified on chilled water pipes
**Pass Criteria:** Insulation type, thickness shown for all systems requiring it
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.4: Valves Located
**Check:** Isolation valves, balancing valves, and control valves located
**Code Reference:** Best practice
**Common Mistakes:** Insufficient isolation valves for equipment service
**Pass Criteria:** Valves shown at all equipment and branch locations
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.5: Expansion Compensation
**Check:** Expansion loops or expansion joints shown where required
**Code Reference:** ASHRAE Fundamentals, manufacturer requirements
**Common Mistakes:** No expansion compensation on long runs
**Pass Criteria:** Expansion compensation shown on runs >100 ft
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.6: Pipe Slope Shown
**Check:** Pipe slope shown for drainage and condensate lines
**Code Reference:** IMC 307.2, IPC 704
**Common Mistakes:** Slope not shown, pipes pitched wrong direction
**Pass Criteria:** Slope shown (1/4" per foot min) and direction indicated
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.7: Air Separator/Vents
**Check:** Air separator or air vents shown on closed-loop systems
**Code Reference:** ASHRAE Handbook HVAC Systems and Equipment
**Common Mistakes:** No air elimination on hydronic systems
**Pass Criteria:** Air separator shown at high point with drain
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.8: Expansion Tank Sized
**Check:** Expansion tank shown and sized for system volume
**Code Reference:** ASHRAE Handbook HVAC Systems and Equipment Chapter 13
**Common Mistakes:** Expansion tank undersized or omitted
**Pass Criteria:** Expansion tank sized per system volume calculation
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.9: Pipe Support Requirements
**Check:** Pipe support and hanger spacing requirements noted
**Code Reference:** IMC 305, MSS SP-58
**Common Mistakes:** Support spacing not specified
**Pass Criteria:** Support spacing specified (typically 10 ft for copper)
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.10: Pressure Test Requirements
**Check:** Hydrostatic pressure test requirements noted
**Code Reference:** IMC 312.6, IPC 312.4
**Common Mistakes:** Test pressure or duration not specified
**Pass Criteria:** Test pressure and duration specified (typically 1.5x operating, 2 hrs)
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

---

## Section 6: Controls and BAS Sequences (10 Items)

### Item 6.1: Sequence of Operations Provided
**Check:** Complete sequence of operations provided for all HVAC systems
**Code Reference:** ASHRAE 90.1 Section 6.4.3.1, best practice
**Common Mistakes:** Generic sequences, modes missing (startup, shutdown, failure)
**Pass Criteria:** Complete sequences covering all operating modes
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 6.2: Normal Operation Mode
**Check:** Normal occupied operation mode fully described
**Code Reference:** Best practice
**Common Mistakes:** Sequence describes only one aspect (e.g., temperature control only)
**Pass Criteria:** Normal mode includes: temp, humidity, ventilation, economizer control
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 6.3: Unoccupied Mode
**Check:** Unoccupied operation mode described with setback temps
**Code Reference:** ASHRAE 90.1 Section 6.4.3.3
**Common Mistakes:** No unoccupied mode or setbacks insufficient
**Pass Criteria:** Unoccupied mode with setback/setup temps specified
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 6.4: Startup/Warm-up Mode
**Check:** Startup or warm-up mode described for occupied preparation
**Code Reference:** Best practice
**Common Mistakes:** Building brought to occupied temp immediately, wasting energy
**Pass Criteria:** Optimal start/warm-up routine specified
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 6.5: Shutdown Mode
**Check:** Shutdown sequence described (safe shutdown of equipment)
**Code Reference:** Best practice
**Common Mistakes:** Equipment just turned off without proper shutdown
**Pass Criteria:** Proper shutdown sequence (e.g., fans run after compressor stops)
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 6.6: Emergency/Failure Mode
**Check:** Failure mode operation described (loss of power, sensor failure)
**Code Reference:** Best practice, life safety
**Common Mistakes:** No failure mode planning, building unsafe without BAS
**Pass Criteria:** Failure modes described with safe default positions
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 6.7: Economizer Control Sequence
**Check:** Economizer control sequence described (if economizer required)
**Code Reference:** ASHRAE 90.1 Section 6.5.1
**Common Mistakes:** Economizer required but sequence not provided
**Pass Criteria:** Economizer lockout and control sequence fully described
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 6.8: Interlocks Described
**Check:** All safety and operational interlocks described
**Code Reference:** IMC 304, best practice
**Common Mistakes:** Critical interlocks missing (e.g., fan proof, freeze stat)
**Pass Criteria:** All interlocks identified (fan proof, safeties, alarms)
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 6.9: BAS Points List
**Check:** Building automation system points list provided
**Code Reference:** Best practice, specification requirements
**Common Mistakes:** Generic points list, doesn't match actual system
**Pass Criteria:** Detailed points list matches sequence and equipment
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 6.10: Control Diagrams Provided
**Check:** Control diagrams or schematics provided showing control logic
**Code Reference:** Best practice
**Common Mistakes:** Text sequences only, no visual diagrams
**Pass Criteria:** Diagrams show control loops, sensors, actuators, logic
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

---

## Section 7: Ventilation and Code Compliance (15 Items)

### Item 7.1: Ventilation Rates Calculated
**Check:** Outdoor air ventilation rates calculated per ASHRAE 62.1
**Code Reference:** IMC 403, ASHRAE 62.1 Section 6
**Common Mistakes:** Ventilation not calculated, generic rates used
**Pass Criteria:** Calculation per ASHRAE 62.1 (area + people) provided
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.2: Occupancy Density Used
**Check:** Occupancy density matches actual or design use
**Code Reference:** ASHRAE 62.1 Table 6-1
**Common Mistakes:** Default occupancy used instead of actual
**Pass Criteria:** Occupancy density appropriate for space type
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.3: Outdoor Air Intake Location
**Check:** Outdoor air intake location shown and meets separation requirements
**Code Reference:** IMC 401.4, 401.5
**Common Mistakes:** Intake too close to exhaust or contamination source
**Pass Criteria:** Intake location meets IMC separation requirements
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.4: Kitchen Exhaust and Makeup Air
**Check:** Kitchen exhaust and makeup air coordinated (makeup = 80-100% of exhaust)
**Code Reference:** IMC 508
**Common Mistakes:** Makeup air insufficient or not provided
**Pass Criteria:** Makeup air shown, sized at 80-100% of exhaust
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.5: Bathroom/Toilet Room Exhaust
**Check:** Bathroom exhaust rates meet code minimums (50 cfm/toilet, 20 cfm/urinal)
**Code Reference:** IMC 403.2.1
**Common Mistakes:** Exhaust undersized or intermittent when required continuous
**Pass Criteria:** Exhaust meets IMC minimums, continuous if no operable windows
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.6: Hazardous Exhaust Separation
**Check:** Hazardous exhaust systems separated from general exhaust
**Code Reference:** IMC 510
**Common Mistakes:** Lab exhaust connected to general building exhaust
**Pass Criteria:** Hazardous exhaust separate per IMC 510
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.7: Ventilation for Parking Garages
**Check:** Parking garage ventilation meets code (typically 1.5 cfm/sf or CO monitoring)
**Code Reference:** IMC 404
**Common Mistakes:** Ventilation undersized, no CO monitoring
**Pass Criteria:** Ventilation meets IMC 404 or CO monitoring system provided
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.8: High Ceilings Ventilation
**Check:** Ventilation design considers ceiling height >15 ft
**Code Reference:** ASHRAE 62.1 Informational Note to Section 6.2.6.2
**Common Mistakes:** Standard diffusers in high spaces (poor mixing)
**Pass Criteria:** High ceiling spaces have appropriate air distribution
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.9: Demand Control Ventilation (If Applicable)
**Check:** Demand control ventilation (DCV) provided where required by energy code
**Code Reference:** ASHRAE 90.1 Section 6.4.3.8
**Common Mistakes:** DCV required but not shown
**Pass Criteria:** DCV shown in spaces >500 sf and >25 people/1000 sf
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.10: Energy Recovery (If Applicable)
**Check:** Energy recovery provided where required by energy code
**Code Reference:** ASHRAE 90.1 Section 6.5.6.1
**Common Mistakes:** ERV required by code but not provided
**Pass Criteria:** ERV shown if outdoor air >specified code threshold
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.11: Refrigerant Monitoring (If Applicable)
**Check:** Refrigerant monitoring and alarm provided for large systems
**Code Reference:** IMC 1105, ASHRAE 15
**Common Mistakes:** No refrigerant detection in occupied machinery rooms
**Pass Criteria:** Refrigerant detection provided per IMC 1105/ASHRAE 15
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.12: Smoke Control (If Applicable)
**Check:** Smoke control system designed per IBC 909 if required
**Code Reference:** IBC 909
**Common Mistakes:** Smoke control required but not designed by qualified engineer
**Pass Criteria:** Smoke control system designed and sealed by qualified PE
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.13: Combustion Air for Fuel-Burning Equipment
**Check:** Combustion air provided per IFGC for fuel-burning equipment
**Code Reference:** IFGC 304
**Common Mistakes:** Combustion air undersized or not provided
**Pass Criteria:** Combustion air sized per IFGC 304 (50 cfm/1000 Btu typical)
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.14: Equipment Room Ventilation
**Check:** Equipment rooms (mechanical, electrical) have adequate ventilation
**Code Reference:** IMC 304
**Common Mistakes:** Equipment rooms inadequately ventilated, overheating
**Pass Criteria:** Equipment room ventilation per IMC 304 and equipment heat gain
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.15: Building Pressurization
**Check:** Building pressurization noted (typically +0.02" to +0.05" w.g.)
**Code Reference:** ASHRAE 62.1 Informational Note to Section 5.16
**Common Mistakes:** Building pressure not controlled, causing infiltration/exfiltration
**Pass Criteria:** Building pressurization strategy documented
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

---

## Section 8: Details and Specifications (10 Items)

### Item 8.1: Details Match Plans
**Check:** All detail callouts on plans reference existing details
**Code Reference:** Best practice
**Common Mistakes:** Detail callouts with no corresponding detail
**Pass Criteria:** Every callout references a real detail
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 8.2: Rooftop Equipment Curb Detail
**Check:** Rooftop equipment curb detail shows flashing, waterproofing, and support
**Code Reference:** SMACNA Architectural Sheet Metal Manual
**Common Mistakes:** Curb detail inadequate, causing leaks
**Pass Criteria:** Complete curb detail with flashing and sealing
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 8.3: Duct Penetration Detail
**Check:** Duct fire-rated penetration detail shows UL-listed firestop
**Code Reference:** IBC 714.3
**Common Mistakes:** Generic "firestop" without UL system reference
**Pass Criteria:** Specific UL firestop system number referenced
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 8.4: Pipe Penetration Detail
**Check:** Pipe penetration details show firestopping and sealing
**Code Reference:** IBC 714.3, IMC 603.8
**Common Mistakes:** Pipe sleeves not fire-rated through rated assemblies
**Pass Criteria:** Fire-rated pipe penetrations per IBC 714
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 8.5: Duct Support Detail
**Check:** Duct support and hanger details provided
**Code Reference:** SMACNA HVAC Duct Construction Standards
**Common Mistakes:** Support details inadequate, causing sagging or collapse
**Pass Criteria:** Support details per SMACNA with spacing requirements
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 8.6: Pipe Support Detail
**Check:** Pipe support and hanger details provided
**Code Reference:** MSS SP-58
**Common Mistakes:** Pipe supports inadequate for insulated pipe weight
**Pass Criteria:** Pipe supports per MSS SP-58 with insulation protection
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 8.7: Vibration Isolation Detail
**Check:** Vibration isolation details for equipment shown
**Code Reference:** ASHRAE Handbook HVAC Applications Chapter 48
**Common Mistakes:** Vibration isolators not specified or improperly selected
**Pass Criteria:** Isolator type and deflection specified per equipment
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 8.8: Flexible Connection Detail
**Check:** Flexible connections shown at equipment to prevent vibration transmission
**Code Reference:** SMACNA, best practice
**Common Mistakes:** Rigid connections causing noise and vibration
**Pass Criteria:** Flexible connections shown at all rotating equipment
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 8.9: Drain and Trap Details
**Check:** Condensate drain and trap details provided
**Code Reference:** IMC 307.2
**Common Mistakes:** Trap not properly sized, causing air leakage
**Pass Criteria:** Trap depth calculated for equipment static pressure
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 8.10: Seismic Restraint Details
**Check:** Seismic restraint details provided for equipment and piping
**Code Reference:** IBC 1613, ASCE 7, SMACNA Seismic Restraint Manual
**Common Mistakes:** Seismic requirements not detailed in seismic zones
**Pass Criteria:** Seismic restraints detailed per local seismic zone
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

---

## Critical Issues Summary

At the end of review, summarize critical issues that must be resolved before issuance:

**Critical Issues (Must Fix Before Permit/Bid):**
1. _______________________________________________________________
2. _______________________________________________________________
3. _______________________________________________________________

**Major Issues (Should Fix, May Impact Construction):**
1. _______________________________________________________________
2. _______________________________________________________________
3. _______________________________________________________________

**Minor Issues (Best Practice, Low Impact):**
1. _______________________________________________________________
2. _______________________________________________________________
3. _______________________________________________________________

---

## Reviewer Sign-Off

**Reviewed By:** _______________________________ **Date:** ______________
**PE License #:** ______________________________ **State:** _____________
**Review Phase:** [ ] SD  [ ] DD  [ ] CD  [ ] Permit  [ ] Construction

**Overall Assessment:**
[ ] Approved for issuance
[ ] Approved with noted corrections
[ ] Not approved - major revisions required

**Comments:**
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________

---

## Integration with Automated QA Rules

This checklist maps to the following automated QA rule series:
- **QA-401-MECH through QA-415-MECH**: Mechanical system validation rules
- **QA-001-GENERAL**: Title block and general drawing requirements
- **QA-101-COORD**: Interdisciplinary coordination rules

When automated QA tools are available, this checklist serves as validation criteria for automated checks and manual review of items that cannot be automated (e.g., engineering judgment, system performance analysis).

---

**Document Version:** 1.0
**Last Updated:** 2025-01-22
**Next Review:** 2026-01-22
**Owner:** Mechanical Engineering Standards Committee
