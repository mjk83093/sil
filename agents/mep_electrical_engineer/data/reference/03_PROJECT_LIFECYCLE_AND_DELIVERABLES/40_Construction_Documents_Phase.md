# Construction Documents (CD) Phase - Complete Requirements

## Overview

The Construction Documents (CD) phase represents 100% design completion and produces the final contract documents used for bidding, permitting, and construction. This document outlines complete requirements, coordination standards, and quality control procedures for CD phase deliverables.

**Phase Characteristics:**
- Design completion: 100%
- Typical duration: 6-10 weeks
- Drawing accuracy requirement: ±0.5% of actual
- Cost estimate accuracy: ±5-10%
- Specification completeness: 100%
- Code compliance: Fully documented

**Integration with QA Workflow:**
This document directly supports the SKILL.md QA validation workflow by defining completeness standards that automated rules (QA-001 through QA-901 series) validate against.

---

## 1. CD Phase Objectives

### Primary Deliverables
1. **Complete drawing sets** for all disciplines (architectural, structural, MEP, civil, landscape)
2. **Technical specifications** (CSI MasterFormat divisions)
3. **Cost estimates** (detailed quantity takeoffs)
4. **Permit application packages** (jurisdiction-specific)
5. **Bid documents** (instructions, forms, agreements)

### Quality Standards
- All design decisions finalized and documented
- All disciplines fully coordinated
- All code requirements identified and addressed
- All engineering calculations complete and sealed
- All details drawn at construction-ready scale
- All notes clear, complete, and constructible

---

## 2. Drawing Completeness Standards

### 2.1 Title Block Requirements (100% Complete)

**Required Information:**
```
Project name and address
Owner name and contact
Design firm name, address, license numbers
Sheet title and number
Drawing scale(s)
Revision dates and descriptions
Professional seal and signature (wet or digital)
Project number
Issue date
Phase designation (e.g., "FOR CONSTRUCTION")
Sheet index reference
Consultant information (if applicable)
Jurisdictional approval stamps (space for)
```

**Validation:** QA-001-GENERAL: Title block completeness check

### 2.2 General Notes and Legends

**Architectural:**
- Complete material legend with manufacturer specifications
- Construction assembly notes with referenced details
- Accessibility compliance notes (ADA/ANSI A117.1)
- Fire-rated assembly notes with UL listings
- Quality assurance and testing requirements

**Structural:**
- Material specifications (concrete strength, rebar grade, steel grade)
- Welding standards and inspection requirements
- Special inspection requirements per IBC Chapter 17
- Load test requirements
- Foundation notes (soil bearing, frost depth, water table)

**Electrical:**
- Voltage and phase designation
- Wire and conduit sizing standards
- Equipment service and maintenance access requirements
- Grounding and bonding notes per NEC Article 250
- Arc flash warning label requirements per NFPA 70E
- Panel schedule legend and load calculation summary
- Emergency power transfer sequence

**Mechanical:**
- Equipment specifications and performance requirements
- Duct and pipe sizing standards
- Insulation requirements by system
- Testing, adjusting, and balancing (TAB) requirements
- Sequence of operations for all systems
- Fire damper and smoke damper schedule
- Refrigerant piping requirements per ASHRAE 15

**Plumbing:**
- Fixture unit calculations
- Water pressure requirements
- Backflow prevention requirements
- Pipe sizing standards
- Insulation and heat trace requirements
- Testing and inspection requirements

### 2.3 Drawing Accuracy Requirements

| Discipline | Dimensional Tolerance | Coordination Accuracy |
|------------|----------------------|----------------------|
| Architectural | ±1/8" on dimensions | ±3" in space |
| Structural | ±1/4" on member size | ±6" in space |
| Electrical | ±6" on device location | ±12" on routing |
| Mechanical | ±3" on equipment | ±6" on ductwork |
| Plumbing | ±3" on fixture | ±6" on piping |

**Critical Coordination Zones:**
- Ceiling spaces (2'-6" minimum clear height for access)
- Mechanical rooms (equipment access and maintenance clearance)
- Electrical rooms (NEC 110.26 working space)
- Vertical shafts (MEP stacking and access)
- Exterior wall penetrations (weather sealing details)

---

## 3. Detail Level Requirements by System

### 3.1 Electrical Systems

**Service and Distribution (Required Details):**
- Service entrance details showing:
  * Utility connection point
  * Meter location and mounting
  * Service equipment location
  * Main disconnect and OCPD
  * Grounding electrode system per NEC 250.50
  * Service conductor routing and protection
  * Clearances per NEC 110.26

- Panel details showing:
  * Panel mounting height and backing
  * Conduit entry locations (top/bottom/side)
  * Working space clearances (36" min depth)
  * Door swing clearances
  * Seismic bracing if required
  * Panel directory format

**Branch Circuiting:**
- Minimum detail level:
  * All receptacle and switch locations dimensioned
  * Circuit home run designations
  * Voltage and phase designation
  * GFCI and AFCI protection noted
  * Dedicated equipment circuits identified
  * Emergency power circuits identified (red color)

**Lighting:**
- Fixture schedule with complete specifications
- Switching and control logic diagrams
- Photometric analysis for critical areas
- Emergency lighting calculations per NFPA 101
- Lighting control system programming logic

**Fire Alarm:**
- Device spacing calculations per NFPA 72
- Initiating device circuit (IDC) wiring diagrams
- Notification appliance circuit (NAC) wiring diagrams
- Voltage drop calculations for all circuits
- Battery backup calculations
- Riser diagram with all circuits labeled

### 3.2 Mechanical Systems

**HVAC Equipment (Required Details):**
- Rooftop unit details:
  * Equipment dimensions and weights
  * Curb details with flashing
  * Duct connection details
  * Refrigerant line routing
  * Condensate drain routing and trap
  * Electrical disconnect location
  * Service access and clearances
  * Seismic restraint details

- Air handling unit details:
  * Equipment dimensions and access panels
  * Coil connections and drains
  * Filter access and sizes
  * Fan motor and drive details
  * Duct connections with flexible connectors
  * Vibration isolation details
  * Control damper locations

**Ductwork:**
- Minimum detail level:
  * Duct sizes on all runs (supply and return)
  * Duct material and construction class
  * Insulation type and thickness
  * Fire damper locations with UL rating
  * Volume damper locations
  * Access door locations (one per run)
  * Support and hanger spacing
  * Seismic bracing per SMACNA

**Piping Systems:**
- Hydronic piping:
  * Pipe sizes on all runs
  * Insulation specifications
  * Valve types and locations
  * Expansion compensation details
  * Air separator and expansion tank sizing
  * Pressure test requirements
  * Flow balancing valve locations
  * Hanger and support details

### 3.3 Plumbing Systems

**Domestic Water:**
- Service entrance detail with:
  * Meter location and bypass
  * Backflow preventer (type and size)
  * Main shut-off valve
  * Water pressure reducing valve if needed
  * Expansion tank sizing and location
  * Branch piping to all fixtures

- Fixture connection details:
  * Rough-in dimensions (specific to manufacturer)
  * Shut-off valve locations
  * Trap primer connections
  * ADA-compliant fixture mounting details

**Drainage Systems:**
- Isometric riser diagrams showing:
  * All fixture connections with fixture units
  * Pipe sizes calculated per IPC Table 710.1(2)
  * Vent sizing per IPC Table 916.1
  * Cleanout locations per IPC 708.3
  * Slope requirements (1/4" per foot minimum)
  * Building drain to building sewer connection

**Gas Piping:**
- Complete layout showing:
  * Service entrance and meter location
  * Main shut-off valve (seismic if required)
  * Branch piping sizes (calculated per IFGC)
  * Individual appliance shut-off valves
  * Drip legs at all vertical risers
  * Support and hanger requirements
  * Testing pressure and duration

---

## 4. Coordination Requirements Between Disciplines

### 4.1 Architectural-Structural Coordination

**Critical Coordination Points:**
1. Floor-to-floor heights and ceiling heights
2. Column and beam locations vs. partition locations
3. Structural opening sizes vs. door/window sizes
4. Roof slopes and drainage vs. rooftop equipment locations
5. Foundation walls vs. below-grade mechanical rooms
6. Expansion joints in structure vs. building envelope

**Coordination Process:**
- Weekly coordination meetings during CD phase
- Overlay review sessions (architectural plans over structural plans)
- 3D BIM clash detection (if BIM is being used)
- Shared coordination drawing set
- Issue log with resolution tracking

### 4.2 Architectural-MEP Coordination

**Space Allocation Verification:**

| Space Type | Required for MEP | Typical % of Floor Area |
|------------|------------------|-------------------------|
| Electrical room | Main distribution, panels, telecom | 0.3-0.5% |
| Mechanical room | HVAC equipment, pumps, controls | 2-4% |
| Plumbing room | Water heaters, RPZ, expansion tanks | 0.2-0.4% |
| Vertical shafts | MEP risers, access | 1-2% per floor |
| Ceiling plenum | Ductwork, piping, cable tray | 2'-6" to 4'-0" depth |

**Penetration Coordination:**
- All floor penetrations located and sized on architectural plans
- All wall penetrations located and fire-rated if required
- All roof penetrations located with waterproofing details
- All exterior wall penetrations with weather sealing details

**Equipment Access:**
- Door sizes verified for equipment delivery (add 6" to largest dimension)
- Corridor widths adequate for equipment rigging
- Elevator capacity verified for rooftop equipment access
- Stairs verified for access to roof and mechanical rooms

### 4.3 MEP Interdisciplinary Coordination

**Ceiling Space Coordination:**

Vertical stacking priority (from ceiling down):
1. Structural (beams, joists, decking)
2. Fire protection (sprinkler mains)
3. HVAC supply ductwork (largest runs)
4. Plumbing (above ductwork to allow drainage)
5. Electrical (conduit and cable tray)
6. HVAC return ductwork (lowest allowable)
7. Lighting fixtures (finished ceiling)

**Mechanical Room Coordination:**
- Equipment layout with maintenance access (36" min)
- Electrical panel locations with NEC 110.26 clearances
- Pipe and duct routing avoiding electrical panels
- Floor drain locations at low points
- Equipment vibration isolation not compromising structure

**Shaft Coordination:**
- Vertical riser locations on all floors aligned
- Riser sizes adequate for future capacity (20% spare)
- Access panels provided on each floor
- Fire stopping at each floor penetration
- Separation between incompatible systems (power vs. data)

---

## 5. Specification Coordination with Drawings

### 5.1 Drawing-Specification Integration

**Division 26 - Electrical Specifications:**

| Spec Section | Drawing Reference | Required Coordination |
|--------------|-------------------|----------------------|
| 26 05 00 - Common Work Results | General notes on E-000 | Material standards, testing |
| 26 05 26 - Grounding and Bonding | Grounding details on E-001 | Electrode sizing, connections |
| 26 05 33 - Raceways and Boxes | Conduit schedules on plans | Conduit types, fill, support |
| 26 24 00 - Switchboards and Panelboards | Panel schedules on plans | Manufacturer, ratings, config |
| 26 27 00 - Low-Voltage Distribution | One-line diagram on E-100 | Equipment ratings, protection |
| 26 50 00 - Lighting | Fixture schedule on E-200 series | Fixture types, controls, dimming |

**Drawing Callout Format:**
```
Example: "PANEL LP-2 - SEE SPEC SECTION 26 24 13 FOR PANEL REQUIREMENTS"
Example: "GROUNDING ELECTRODE - SEE DETAIL 5/E-001 AND SPEC 26 05 26.13"
```

### 5.2 Technical Specification Requirements (NEC Compliance)

**Electrical Specifications Must Include:**
1. **26 05 26 - Grounding and Bonding**
   - Electrode types per NEC 250.52
   - Conductor sizing per NEC 250.66
   - Bonding jumper sizing per NEC 250.102
   - Testing requirements (25 ohms or less)

2. **26 24 00 - Switchboards and Panelboards**
   - Short circuit current rating (SCCR) requirements
   - UL listing requirements (UL 891 for switchboards, UL 67 for panelboards)
   - Bus bar material and ampacity
   - Main and branch breaker types
   - Series rating restrictions per NEC 240.86

3. **26 27 00 - Low-Voltage Distribution**
   - Wire sizing standards per NEC 310.15
   - Conduit fill per NEC Chapter 9, Table 4
   - Conductor ampacity adjustment per NEC 310.15(C)
   - Voltage drop limitations (3% branch, 2% feeder recommended)

**Mechanical Specifications Must Include:**
1. **23 05 00 - Common Work Results**
   - Pipe and duct material standards
   - Support and hanger requirements per SMACNA
   - Vibration isolation requirements
   - Testing and balancing requirements

2. **23 09 00 - Instrumentation and Control**
   - BAS points list coordinated with sequence of operations
   - Control valve and damper specifications
   - Sensor specifications and locations
   - Network architecture and protocols

---

## 6. Code Compliance Documentation Requirements

### 6.1 Code Summary Sheet (Required on Cover Sheet)

**Format:**
```markdown
PROJECT CODE COMPLIANCE SUMMARY

Occupancy Classification: [IBC Chapter 3]
- Primary occupancy: _________________ (Use Group: ___)
- Secondary occupancies: _____________ (Use Group: ___)
- Mixed occupancy: Separated / Non-separated [IBC 508.3 / 508.4]

Construction Type: [IBC Chapter 6]
- Type: ______ (IA, IB, IIA, IIB, IIIA, IIIB, IV, VA, VB)
- Fire-resistance ratings verified: Yes / No

Height and Area: [IBC Chapter 5]
- Building height: _____ feet, _____ stories
- Building area per floor: _______ sq ft
- Allowable area: _______ sq ft (with increases noted)
- Area modification factors applied: Frontage ___ / Sprinkler ___

Fire Protection Systems: [IBC Chapter 9]
- Automatic sprinkler system: Yes / No [NFPA 13 / 13R / 13D]
- Fire alarm system: Yes / No [NFPA 72]
- Standpipe system: Yes / No [NFPA 14]
- Smoke control: Yes / No [IBC 909]

Means of Egress: [IBC Chapter 10]
- Occupant load: _______ persons
- Exit stairway quantity: _____ (Required: _____)
- Egress width: _______ inches (Required: _____ inches)
- Travel distance: _____ feet (Max allowed: _____ feet)
- Dead-end corridor: _____ feet (Max allowed: _____ feet)

Accessibility: [IBC Chapter 11 / ADA / ANSI A117.1]
- Accessible route provided: Yes / No
- Accessible parking spaces: _____ (Required: _____)
- Accessible plumbing fixtures: _____ (Required: _____)
- Elevator required: Yes / No

Energy Code: [IECC / ASHRAE 90.1]
- Code version: _________________
- Compliance path: Prescriptive / Performance / ERI
- Building envelope compliance documented: Yes / No
- Mechanical system efficiency documented: Yes / No
- Lighting power density documented: Yes / No

Electrical Code: [NFPA 70 - NEC]
- Code version: NEC ______
- Service size: _______ amperes at _____ volts, _____ phase
- Load calculation method: Standard / Optional [NEC Article 220]
- Emergency power required: Yes / No [NEC Article 700]
- Legally required standby: Yes / No [NEC Article 701]

Mechanical Code: [IMC / IECC]
- Code version: _________________
- Ventilation design standard: IMC / ASHRAE 62.1
- Minimum ventilation rate: _____ CFM
- Duct leakage class: _____

Plumbing Code: [IPC]
- Code version: _________________
- Water service size: _____ inches
- Sewer service size: _____ inches
- Fixture unit count: _____
- Backflow protection provided: Yes / No
```

### 6.2 Code Compliance Matrix

Create a matrix showing each code requirement and where it is addressed:

| Code Requirement | Code Section | Drawing Reference | Spec Reference | Calculation Reference |
|-----------------|--------------|-------------------|----------------|----------------------|
| Service entrance working space | NEC 110.26(A) | E-101, Detail 1 | 26 27 00 | - |
| Grounding electrode | NEC 250.50 | E-001, Detail 3 | 26 05 26 | Calc E-2.1 |
| Emergency lighting | IBC 1008.3 | E-201, E-202 | 26 51 00 | Calc E-4.3 |
| Fire alarm device spacing | NFPA 72 | E-301 | 28 31 00 | Calc E-5.1 |
| HVAC ventilation rate | IMC 403 / ASHRAE 62.1 | M-101 | 23 05 00 | Calc M-1.2 |
| Duct fire dampers | IMC 607.5 | M-101, Detail 8 | 23 33 00 | - |
| Sprinkler coverage | NFPA 13 | FP-101 | 21 13 00 | Hydraulic calc |
| Plumbing fixture units | IPC 709 | P-101 | 22 40 00 | Calc P-1.1 |

---

## 7. Professional Stamping and Sealing Requirements

### 7.1 Licensing Requirements by Discipline

**Electrical Engineering:**
- Professional Engineer (PE) license required in jurisdiction
- Electrical specialty or power engineering designation
- Stamp must include: Name, license number, jurisdiction, expiration date
- Signature required: Wet ink or approved digital signature
- Date of seal: Must match issue date or revision date

**Mechanical Engineering:**
- PE license with HVAC/mechanical specialty
- Additional certifications may enhance but not replace PE:
  * Certified Energy Manager (CEM)
  * LEED AP BD+C
  * Commissioning authority certifications

**Structural Engineering:**
- PE license with structural specialty required
- Seismic design certification may be required in high seismic zones
- Wind design certification may be required in coastal areas

**Fire Protection Engineering:**
- PE license or NICET Level III/IV certification
- May be required by AHJ depending on project scope
- Sprinkler system hydraulic calculations must be sealed

### 7.2 Sealing Requirements by Drawing Type

**Must Be Sealed:**
- All construction documents submitted for permit
- All sheets containing calculations or engineering design
- All sheets used for bidding and construction
- Cover sheet with code summary
- All detail sheets

**May Be Unsealed (verify with AHJ):**
- Interior design layouts (non-structural, non-MEP)
- Signage and wayfinding plans
- Furniture plans
- Key plans and vicinity maps

### 7.3 Seal Placement Standards

**Location on Sheet:**
- Typical: Lower right corner near title block
- Alternative: Adjacent to title block if space constraints
- Must not obscure drawing content or title block information
- Digital seal: Same location, embedded in PDF with certificate

**Seal Format:**
```
[Professional Seal/Stamp - Circular or Rectangular]
Includes:
- Engineer name
- License number
- State/province
- Expiration date
- "Professional Engineer" designation

[Signature - Written across seal]
Date: [Must match sheet issue/revision date]
```

---

## 8. CD Submittal Review Checklist (Complete 40-Item List)

### General Requirements (Items 1-5)

- [ ] **1. Cover sheet complete** with project data, code summary, sheet index, professional seals
- [ ] **2. Drawing set complete** - all disciplines included, all sheets in index present
- [ ] **3. Revisions tracked** - revision clouds, triangle markers, dates in title block
- [ ] **4. Professional seals** - all required sheets sealed by licensed professionals
- [ ] **5. Issue designation** - clearly marked "FOR CONSTRUCTION" or "FOR PERMIT"

### Architectural Coordination (Items 6-10)

- [ ] **6. Floor plans coordinated** - dimensions match, grid lines align, partitions consistent
- [ ] **7. Ceiling heights verified** - adequate for MEP systems (min 2'-6" plenum)
- [ ] **8. Door schedules complete** - hardware, fire ratings, accessibility features noted
- [ ] **9. Room names consistent** - same nomenclature across all discipline drawings
- [ ] **10. Penetration details** - floor, wall, roof penetrations detailed and fire-rated

### Electrical Drawings (Items 11-20)

- [ ] **11. One-line diagram complete** - service size, main disconnect, distribution equipment, short circuit ratings
- [ ] **12. Panel schedules accurate** - sum of breakers ≤ panel rating, balanced loads, spare space noted
- [ ] **13. Load calculations sealed** - service load calc per NEC Article 220, PE sealed
- [ ] **14. Grounding details** - electrode system per NEC 250.50, conductor sizing per 250.66
- [ ] **15. Branch circuit home runs** - all devices show panel and circuit number
- [ ] **16. Voltage drop verified** - 3% max branch circuit, 5% total recommended
- [ ] **17. Arc flash labels noted** - "Arc Flash Warning" labels noted on all panels per NFPA 70E
- [ ] **18. Emergency power** - generator, ATS, emergency circuits shown in red
- [ ] **19. Fire alarm complete** - device spacing calcs, battery calc, voltage drop calc
- [ ] **20. Low voltage systems** - telecom, data, AV, security systems shown with separate home runs

### Mechanical Drawings (Items 21-30)

- [ ] **21. Load calculations sealed** - heating/cooling loads per ASHRAE, PE sealed
- [ ] **22. Equipment schedules complete** - model numbers, capacities, electrical characteristics, weights
- [ ] **23. Duct sizing shown** - all supply and return ducts sized and labeled
- [ ] **24. Fire damper locations** - at all rated wall/floor penetrations per IMC 607.5
- [ ] **25. Outdoor air ventilation** - minimum ventilation rates per ASHRAE 62.1 documented
- [ ] **26. Piping sizes shown** - all hydronic piping, refrigerant piping, gas piping sized
- [ ] **27. Insulation specified** - all ductwork and piping insulation types and thicknesses noted
- [ ] **28. Vibration isolation** - isolation springs/pads specified for all rotating equipment
- [ ] **29. Sequence of operations** - complete control sequences for all HVAC systems
- [ ] **30. TAB requirements** - testing, adjusting, balancing requirements noted in general notes

### Plumbing Drawings (Items 31-35)

- [ ] **31. Fixture unit calculation** - drainage system sized per IPC Table 710.1(2)
- [ ] **32. Domestic water sizing** - water service and branches sized per IPC Chapter 6
- [ ] **33. Isometric risers** - all drainage and vent risers shown isometrically with sizes
- [ ] **34. Backflow prevention** - RPZ or other backflow preventers located per IPC 608
- [ ] **35. Gas piping sized** - natural gas or propane piping sized per IFGC Chapter 4

### Coordination and Details (Items 36-40)

- [ ] **36. MEP coordination** - ceiling space coordination verified, no conflicts
- [ ] **37. Details complete** - all callouts reference existing details, no "TYP" without precedent
- [ ] **38. Specifications coordinated** - all drawing callouts reference spec sections
- [ ] **39. Accessibility verified** - ADA/ANSI A117.1 compliance for all spaces and systems
- [ ] **40. Constructability review** - drawings reviewed by contractor or construction manager

---

## 9. Common CD Phase Errors and How to Avoid Them

### 9.1 Electrical Common Errors

**Error 1: Panel schedule loads don't sum correctly**
- Symptom: Total calculated load ≠ sum of breaker loads
- Cause: Manual arithmetic errors, outdated schedule after design changes
- Prevention: Use Excel or software templates that auto-calculate sums
- Fix: Recalculate all panel loads, verify against one-line diagram

**Error 2: Missing NEC clearances at electrical equipment**
- Symptom: Panel located too close to door, corner, or other equipment
- Cause: Equipment placed without checking NEC 110.26 requirements
- Prevention: Show 36" clear working space (depth) on plans, verify door swing
- Fix: Relocate panel or equipment, coordinate with architectural team

**Error 3: Inadequate conduit space for home runs**
- Symptom: Too many circuits home running to same panel location
- Cause: Not considering conduit bundling, fill limitations, or space constraints
- Prevention: Count circuits, group into conduits per NEC Chapter 9 fill
- Fix: Add additional conduit runs or reroute circuits

**Error 4: Voltage drop exceeds recommendations**
- Symptom: Long circuit runs with small wire sizes
- Cause: Voltage drop not calculated, or calculated incorrectly
- Prevention: Calculate VD for all circuits >50 feet, upsize if needed
- Fix: Increase wire size or reduce circuit length

**Error 5: Emergency circuits not clearly identified**
- Symptom: Emergency lighting/exit signs not on emergency power circuits
- Cause: Circuit designation not clearly shown on plans
- Prevention: Use red color for emergency circuits, call out in panel schedule
- Fix: Revise plans to show correct circuit designations

### 9.2 Mechanical Common Errors

**Error 6: Inadequate ceiling height for ductwork**
- Symptom: Duct sizes shown that don't fit in available ceiling space
- Cause: Coordination not done with architectural ceiling heights
- Prevention: Verify ceiling heights before finalizing duct sizes
- Fix: Reduce duct size (increase velocity), relocate ducts, or lower ceiling

**Error 7: Missing fire dampers at rated penetrations**
- Symptom: Ductwork penetrates fire-rated wall without fire damper
- Cause: Fire-rated walls not identified on mechanical drawings
- Prevention: Overlay mechanical plans on architectural plans showing fire walls
- Fix: Add fire dampers at all required locations, coordinate with architectural

**Error 8: Equipment not accessible for maintenance**
- Symptom: Equipment placed against wall or in corner without access
- Cause: Equipment layout not considering maintenance clearance requirements
- Prevention: Provide 36" minimum clearance on service side of all equipment
- Fix: Relocate equipment or enlarge mechanical room

**Error 9: Outdoor air intake too close to exhaust**
- Symptom: Outdoor air intake within 10 feet of exhaust outlet
- Cause: Equipment placement without considering airflow paths
- Prevention: Locate intakes upwind of exhausts, minimum 10' separation
- Fix: Relocate intake or exhaust, or increase separation distance

**Error 10: Incomplete sequence of operations**
- Symptom: Control sequence missing startup, shutdown, or failure modes
- Cause: Sequence written only for normal operation
- Prevention: Use standard template covering all operating modes
- Fix: Revise sequence to include all modes: startup, normal, shutdown, unoccupied, failure

### 9.3 Coordination Common Errors

**Error 11: Structural beam conflicts with ductwork**
- Symptom: Large duct passes through beam location
- Cause: MEP not coordinated with structural drawings
- Prevention: Weekly coordination meetings, overlay reviews, BIM clash detection
- Fix: Reroute duct around beam, resize duct, or coordinate structural opening

**Error 12: Plumbing vent through middle of HVAC unit**
- Symptom: Roof-mounted plumbing vent conflicts with rooftop unit location
- Cause: Plumbing and mechanical drawings not coordinated
- Prevention: Coordinate all rooftop penetrations and equipment locations
- Fix: Relocate plumbing vent or HVAC unit

**Error 13: Electrical panel door blocked by piping**
- Symptom: Pipe routed in front of electrical panel, blocking access
- Cause: Electrical and plumbing not coordinated in mechanical room
- Prevention: Show NEC 110.26 clear working space on all discipline drawings
- Fix: Reroute piping to maintain electrical clearances

---

## 10. CD Phase Schedule and Milestones

### Typical 8-Week CD Phase Schedule

**Week 1-2: Design Completion**
- Finalize all design decisions
- Complete all calculations
- Finalize equipment selections
- Coordinate major equipment locations

**Week 3-4: Drawing Production**
- Complete all plan drawings
- Complete all detail drawings
- Complete all schedules
- Begin specification writing

**Week 5: Internal QA Review**
- Discipline lead review (2 days per discipline)
- Interdisciplinary coordination review (1 day)
- Principal review (1 day)
- Corrections and revisions (1 day)

**Week 6: External Coordination Review**
- Architect review (if separate MEP firm)
- Owner review
- Contractor constructability review (if CM on board)
- Consultant responses to comments

**Week 7: Final QA and Stamping**
- Final QA checklist completion (use Section 8 checklist)
- Professional sealing and signing
- Specification proofreading and coordination
- Cost estimate finalization

**Week 8: Permit Submittal and Bid Preparation**
- Permit package assembly
- Permit application submittal
- Bid document assembly (drawings + specs + forms)
- Bid document distribution

---

## 11. Coordination Drawing Best Practices

### 11.1 Composite Overlay Drawings

Create composite drawings showing all disciplines in one view:

**Ceiling Coordination Plan:**
- Structural elements (beams, joists) - black
- HVAC supply ductwork - blue
- HVAC return ductwork - light blue
- Plumbing piping - green
- Electrical conduit/cable tray - red
- Fire protection piping - orange
- Lighting fixtures - yellow

**Mechanical Room Plan:**
- Equipment footprints with maintenance clearances
- Electrical panel locations with NEC clearances
- Piping routing shown in elevation view (inline)
- Duct routing shown in elevation view (inline)
- Floor drains and trenches
- Access doors and hatches

### 11.2 3D BIM Coordination (If Applicable)

If using BIM, perform clash detection at 95% CD:
- Hard clashes: Physical interference (red flag - must fix)
- Soft clashes: Clearance violations (yellow flag - review)
- Workflow clashes: Installation sequence conflicts (review)

Generate clash reports by discipline and coordinate resolution:
- Architect-structural clashes: Highest priority
- MEP-structural clashes: Second priority
- MEP-MEP clashes: Third priority
- Spatial clearance clashes: Final priority

---

## 12. Permit Package Preparation

### 12.1 Required Permit Drawings

**Electrical Permit Package:**
- E-000: Cover sheet with code summary and load calculation
- E-100: One-line diagram
- E-101 to E-10X: Power plans (all floors)
- E-200 to E-20X: Lighting plans (all floors)
- E-300 to E-30X: Fire alarm plans (all floors) - if required
- E-400: Site electrical plan (if applicable)
- E-500 to E-5XX: Electrical details
- E-600: Panel schedules
- E-700: Equipment schedules and diagrams

**Mechanical Permit Package:**
- M-000: Cover sheet with load calculation summary
- M-100 to M-10X: HVAC plans (all floors)
- M-200 to M-20X: Plumbing plans (all floors)
- M-300: Gas piping plan (if applicable)
- M-400 to M-4XX: Mechanical details
- M-500: Equipment schedules and specifications
- M-600: Sequence of operations and control diagrams

**Plumbing Permit Package:**
- P-100 to P-10X: Plumbing plans (all floors)
- P-200: Plumbing isometric riser diagrams
- P-300 to P-3XX: Plumbing details
- P-400: Fixture schedule and specifications

### 12.2 Permit Application Forms (Jurisdiction-Specific)

Typical application requirements:
- Building permit application form
- Electrical permit application form
- Mechanical permit application form
- Plumbing permit application form
- Fire sprinkler permit application (if separate)
- Fire alarm permit application (if separate)
- Fees (typically based on valuation or square footage)
- Professional license verification
- Energy code compliance forms (COMcheck, REScheck, etc.)

---

## 13. Post-CD Phase: Addenda and RFI Management

### 13.1 Addendum Process

During bidding phase, track and respond to contractor questions:

**Addendum Format:**
```
ADDENDUM NO. [Number]
Date: [Issue Date]
Project: [Project Name]
To: All Plan Holders

This addendum modifies the Construction Documents dated [Date] as follows:

ELECTRICAL:
1. Question: [Contractor question]
   Response: [Engineer response]
   Drawing change: [Specific drawing(s) affected]
   Specification change: [Specific spec section(s) affected]

[Attached: Revised drawing sheets]

By: [Engineer name and signature]
```

### 13.2 RFI Process (During Construction)

Track and respond to contractor RFIs during construction:

**RFI Log Format:**

| RFI No. | Date Received | Subject | Discipline | Response Due | Status | Date Closed |
|---------|---------------|---------|------------|--------------|--------|-------------|
| 001 | 3/15/24 | Panel LP-2 mounting height | Electrical | 3/22/24 | Closed | 3/20/24 |
| 002 | 3/16/24 | Fire damper at Grid C-5 | Mechanical | 3/23/24 | Open | - |

**RFI Response Template:**
```
RFI No.: [Number]
Date: [Response Date]
Subject: [RFI Subject]
Contractor Question: [Question as submitted]

Engineer Response:
[Detailed response referencing drawings, specifications, and code]

Action Required:
- [ ] Proceed as shown on drawings
- [ ] Proceed per this RFI response
- [ ] Proceed per attached sketch
- [ ] Stop work and await clarification

By: [Engineer name and signature]
```

---

## 14. CD Phase Quality Metrics

Track these metrics to assess CD quality:

| Metric | Target | Industry Average | Measurement |
|--------|--------|------------------|-------------|
| Drawing errors per sheet | <2 | 3-5 | RFIs + ASIs per sheet count |
| Permit review cycle | <3 weeks | 4-6 weeks | Date submitted to approval |
| Bid addenda count | <5 | 5-10 | Total addenda issued |
| RFI count (construction) | <1 per $100k | 1.5-2 per $100k | Total RFIs / contract value |
| Change order rate | <3% | 5-8% | CO value / contract value |

---

## Conclusion

The Construction Documents phase is the culmination of the design process and requires meticulous attention to detail, thorough coordination, and rigorous quality control. Following the standards and checklists in this document will help ensure:

1. **Complete and coordinated drawing sets** ready for permitting and construction
2. **Code-compliant designs** with documentation of all requirements
3. **Constructible details** that contractors can build from
4. **Minimal RFIs and change orders** during construction
5. **Professional delivery** that protects the engineer's license and liability

**Integration with QA Workflow:**
These CD phase requirements directly feed into the automated QA validation rules defined in SKILL.md. Each checklist item corresponds to one or more QA rules (e.g., QA-201-ELEC through QA-215-ELEC for electrical systems) that can be validated programmatically against drawing files.

---

**Document Version:** 1.0
**Last Updated:** 2025-01-22
**Next Review:** 2026-01-22
**Owner:** Engineering Standards Committee
