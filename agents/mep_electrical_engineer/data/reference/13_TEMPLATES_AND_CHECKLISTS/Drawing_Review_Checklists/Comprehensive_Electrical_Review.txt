# Comprehensive Electrical Drawing Review Checklist

## Overview

This comprehensive checklist provides 100+ review items for electrical construction documents, organized by drawing type and system. Each item includes check description, applicable code references, common mistakes, and pass/fail criteria.

**Integration with QA Workflow:**
This checklist directly maps to automated QA rules in the SKILL.md workflow (QA-201-ELEC through QA-215-ELEC series). Use this for manual review or as validation criteria for automated checks.

**How to Use This Checklist:**
- [ ] Mark each item as Pass, Fail, or N/A
- Document failures with specific drawing references
- Prioritize failures by severity (Critical, Major, Minor)
- Track corrections and re-review

---

## Section 1: Title Block and General Requirements (15 Items)

### Item 1.1: Project Information Complete
**Check:** Title block contains complete project name, address, owner name, and contact information
**Code Reference:** Local jurisdiction requirements
**Common Mistakes:** Abbreviated addresses, missing suite numbers, owner name outdated
**Pass Criteria:** All fields populated and current
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.2: Design Firm Information
**Check:** Design firm name, address, license number, and contact clearly shown
**Code Reference:** Professional licensing board requirements
**Common Mistakes:** License number missing or expired, contact info outdated
**Pass Criteria:** Current license number shown, contact info accurate
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.3: Professional Seal Present
**Check:** Professional Engineer (PE) seal present on all required sheets
**Code Reference:** State licensing board requirements
**Common Mistakes:** Seal on cover sheet only, unsigned seal, expired seal
**Pass Criteria:** Seal on all engineering sheets, signed, current date
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.4: Sheet Numbers and Index
**Check:** Sheet numbers unique and sequential, sheet index matches actual sheets
**Code Reference:** Best practice
**Common Mistakes:** Duplicate sheet numbers, index outdated after revisions
**Pass Criteria:** All sheets numbered correctly, index accurate
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.5: Drawing Scale Shown
**Check:** Scale clearly indicated for all plans, details, and diagrams
**Code Reference:** Best practice
**Common Mistakes:** "NTS" overused, scale not updated after resizing
**Pass Criteria:** Scale shown and accurate on all views
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.6: Revision History
**Check:** Revision clouds, triangles, dates, and descriptions shown
**Code Reference:** Best practice, AIA standards
**Common Mistakes:** Revision clouds without description, dates inconsistent
**Pass Criteria:** All revisions tracked with date and description
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.7: Issue/Phase Designation
**Check:** Drawing issue clearly marked (e.g., "FOR CONSTRUCTION", "FOR PERMIT")
**Code Reference:** Best practice
**Common Mistakes:** Generic "ISSUED" without purpose, phase unclear
**Pass Criteria:** Clear designation of drawing purpose
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.8: Code and Standards References
**Check:** NEC version, local amendments, and standards clearly noted
**Code Reference:** NEC 90.2, local jurisdiction
**Common Mistakes:** NEC version not stated, local amendments not noted
**Pass Criteria:** NEC version and all applicable codes listed
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.9: General Notes Complete
**Check:** General electrical notes sheet complete with all standard requirements
**Code Reference:** NEC 110.3, jurisdiction requirements
**Common Mistakes:** Notes copied from previous project without updating
**Pass Criteria:** Project-specific notes, no generic placeholders
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.10: Legend and Symbols
**Check:** Electrical symbol legend complete and consistent with drawings
**Code Reference:** Best practice
**Common Mistakes:** Symbols on plans not in legend, legend has unused symbols
**Pass Criteria:** All symbols on plans appear in legend, all legend symbols used
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.11: Abbreviations List
**Check:** Abbreviations list provided and consistent throughout drawings
**Code Reference:** Best practice
**Common Mistakes:** Abbreviations used but not defined, inconsistent usage
**Pass Criteria:** All abbreviations defined, usage consistent
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.12: Specification References
**Check:** Drawing notes reference applicable specification sections
**Code Reference:** Best practice, CSI format
**Common Mistakes:** Spec sections not updated after spec revision
**Pass Criteria:** All spec references accurate and current
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.13: Consultant Coordination
**Check:** Other disciplines' drawings referenced (architectural, mechanical, plumbing)
**Code Reference:** Best practice
**Common Mistakes:** No cross-references, references outdated
**Pass Criteria:** Current references to coordinated disciplines
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.14: Drawing Matchlines
**Check:** Matchlines clearly shown with sheet references on multi-sheet plans
**Code Reference:** Best practice
**Common Mistakes:** Matchline references incorrect, matchlines don't align
**Pass Criteria:** Matchlines align perfectly, references accurate
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 1.15: North Arrow and Grid
**Check:** North arrow on all plans, grid lines match architectural
**Code Reference:** Best practice
**Common Mistakes:** North arrow rotated incorrectly, grid lines off by inches
**Pass Criteria:** North arrow consistent, grids align with architectural ±1/8"
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

---

## Section 2: One-Line Diagram Review (20 Items)

### Item 2.1: Service Entrance Shown
**Check:** Utility service entrance point clearly shown with connection details
**Code Reference:** NEC 230.70, 230.91
**Common Mistakes:** Service entrance location unclear, meter not shown
**Pass Criteria:** Service entry point, meter, disconnect all clearly shown
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.2: Service Voltage and Phase
**Check:** Service voltage (120/208V, 120/240V, 277/480V) and phase (1Ø or 3Ø) noted
**Code Reference:** NEC 220.5
**Common Mistakes:** Voltage shown but not phase, or vice versa
**Pass Criteria:** Voltage and phase clearly noted at service entrance
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.3: Service Conductor Size
**Check:** Service conductor size shown and referenced to calculation
**Code Reference:** NEC 230.42, Table 310.15(B)(16)
**Common Mistakes:** Conductor size missing, calculation reference missing
**Pass Criteria:** Conductor size shown with calculation reference
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.4: Main Disconnect Rating
**Check:** Main disconnect type and amp rating shown
**Code Reference:** NEC 230.70, 230.79
**Common Mistakes:** Breaker vs. fused disconnect not specified, rating unclear
**Pass Criteria:** Disconnect type and amp rating clearly shown
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.5: Service OCPD Rating
**Check:** Main overcurrent protective device (OCPD) rating shown
**Code Reference:** NEC 230.90
**Common Mistakes:** OCPD rating different from disconnect rating without explanation
**Pass Criteria:** OCPD rating shown and appropriate for service conductor
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.6: Grounding Electrode System
**Check:** Grounding electrode system shown with conductor sizing
**Code Reference:** NEC 250.50, 250.52, 250.66
**Common Mistakes:** Electrode type not specified, GEC size not shown
**Pass Criteria:** Electrode type and GEC size shown per NEC 250.66
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.7: Main Bonding Jumper
**Check:** Main bonding jumper shown and sized
**Code Reference:** NEC 250.28, 250.102(C)
**Common Mistakes:** MBJ not shown, size not specified
**Pass Criteria:** MBJ shown with size per NEC 250.102(C)
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.8: Downstream Panelboards Shown
**Check:** All downstream panelboards shown with designations and ratings
**Code Reference:** NEC 408.4
**Common Mistakes:** Panel designations don't match panel schedules
**Pass Criteria:** All panels shown, designations match schedules
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.9: Feeder Conductor Sizes
**Check:** Feeder conductor sizes shown for all feeders
**Code Reference:** NEC 215.2, Table 310.15(B)(16)
**Common Mistakes:** Conductor size shown but not raceway size
**Pass Criteria:** Conductor size and raceway size shown for all feeders
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.10: Feeder OCPD Ratings
**Check:** Feeder overcurrent protection ratings shown
**Code Reference:** NEC 215.3, 240.4
**Common Mistakes:** OCPD rating larger than feeder conductor ampacity
**Pass Criteria:** OCPD ratings appropriate for conductor sizes
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.11: Equipment Grounding Conductors
**Check:** Equipment grounding conductor (EGC) sizes shown
**Code Reference:** NEC 250.122, Table 250.122
**Common Mistakes:** EGC size not shown, undersized per Table 250.122
**Pass Criteria:** EGC sizes shown and meet NEC 250.122 minimum
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.12: Short Circuit Current Rating (SCCR)
**Check:** Available fault current at service and SCCR of equipment noted
**Code Reference:** NEC 110.9, 110.10
**Common Mistakes:** Fault current not calculated, SCCR not verified
**Pass Criteria:** Fault current calculated, all equipment SCCR adequate
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.13: Transformer Shown (If Applicable)
**Check:** Transformers shown with kVA rating, primary/secondary voltages
**Code Reference:** NEC 450.3
**Common Mistakes:** Transformer primary OCPD not shown, secondary OCPD missing
**Pass Criteria:** Transformer fully detailed with primary and secondary protection
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.14: Emergency Power Source (If Applicable)
**Check:** Generator or other emergency power source shown
**Code Reference:** NEC Article 700, 701, 702
**Common Mistakes:** Generator size not justified by load, ATS not shown
**Pass Criteria:** Generator sized per load calc, ATS shown and rated
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.15: Automatic Transfer Switch (If Applicable)
**Check:** ATS shown with rating and transfer time
**Code Reference:** NEC 700.5(A), 700.12
**Common Mistakes:** ATS rating smaller than emergency load, transfer time >10 sec
**Pass Criteria:** ATS rated for emergency load, transfer time noted
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.16: Metering Shown
**Check:** Utility metering location and type shown
**Code Reference:** Utility requirements
**Common Mistakes:** Meter location conflicts with other equipment
**Pass Criteria:** Meter shown per utility requirements, accessible location
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.17: Surge Protection (If Applicable)
**Check:** Surge protective device (SPD) shown if required
**Code Reference:** NEC 230.67 (dwelling), 242.5 (commercial if required)
**Common Mistakes:** SPD not shown when required, not coordinated with service
**Pass Criteria:** SPD shown if required by code or owner, properly rated
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.18: Busway Systems (If Applicable)
**Check:** Busway shown with amp rating and plug-in unit locations
**Code Reference:** NEC Article 368
**Common Mistakes:** Busway amp rating not shown, plug locations unclear
**Pass Criteria:** Busway fully specified with ratings and connections
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.19: Equipment Nomenclature Consistent
**Check:** Equipment names/designations consistent across one-line and other drawings
**Code Reference:** Best practice
**Common Mistakes:** Panel called "LP-1" on one-line but "LP1" on schedules
**Pass Criteria:** Nomenclature exactly consistent across all drawings
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 2.20: Legend for One-Line Diagram
**Check:** Symbols and abbreviations used on one-line diagram defined
**Code Reference:** Best practice
**Common Mistakes:** Symbols used without legend, abbreviations undefined
**Pass Criteria:** All symbols and abbreviations defined on sheet or reference legend
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

---

## Section 3: Panel Schedules and Load Calculations (25 Items)

### Item 3.1: Panel Schedule Format
**Check:** Panel schedules use standard format with all required columns
**Code Reference:** NEC 408.4
**Common Mistakes:** Columns missing (wire size, breaker type, etc.)
**Pass Criteria:** Schedule includes: circuit #, description, breaker rating, wire size, conduit, load
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.2: Panel Designation Matches One-Line
**Check:** Panel names on schedules match one-line diagram exactly
**Code Reference:** Best practice
**Common Mistakes:** Minor variations in naming (LP-1 vs LP1 vs Lighting Panel 1)
**Pass Criteria:** Exact match between schedule and one-line
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.3: Panel Voltage and Phase
**Check:** Panel voltage and phase clearly shown on schedule header
**Code Reference:** NEC 408.4
**Common Mistakes:** Voltage shown but not phase configuration
**Pass Criteria:** Voltage and phase (e.g., "120/208V, 3Ø, 4W") clearly shown
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.4: Panel Main Breaker Rating
**Check:** Main breaker or main lugs rating shown and appropriate
**Code Reference:** NEC 408.36
**Common Mistakes:** Main breaker smaller than sum of loads
**Pass Criteria:** Main rating adequate for calculated panel load
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.5: Panel Bus Rating
**Check:** Panel bus amp rating shown
**Code Reference:** NEC 408.30
**Common Mistakes:** Bus rating not shown, confused with main breaker rating
**Pass Criteria:** Bus rating shown (typically 100A, 225A, or 400A)
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.6: Panel Short Circuit Rating
**Check:** Panel AIC (ampere interrupting capacity) or SCCR shown
**Code Reference:** NEC 110.9
**Common Mistakes:** AIC rating not specified, inadequate for available fault current
**Pass Criteria:** AIC rating shown and adequate per fault current study
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.7: Feeder to Panel
**Check:** Feeder conductor size and OCPD rating shown in schedule header
**Code Reference:** NEC 215.2
**Common Mistakes:** Feeder info missing, doesn't match one-line diagram
**Pass Criteria:** Feeder size matches one-line, properly protected
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.8: Circuit Numbering Sequential
**Check:** Circuit numbers sequential with no gaps (odd on left, even on right)
**Code Reference:** Best practice, NEC 408.3(E)
**Common Mistakes:** Circuit numbers skipped, not alternating odd/even
**Pass Criteria:** Sequential numbering, odd on left phase, even on right
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.9: Circuit Descriptions Accurate
**Check:** Circuit descriptions clearly identify load served
**Code Reference:** NEC 408.4
**Common Mistakes:** Generic descriptions ("Recepts", "Lights"), room numbers missing
**Pass Criteria:** Specific descriptions with room numbers or equipment names
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.10: Breaker Ratings Shown
**Check:** Breaker amp rating shown for every circuit
**Code Reference:** NEC 240.4, 240.6
**Common Mistakes:** Blanks in breaker column, non-standard ratings
**Pass Criteria:** All breaker ratings shown, standard ratings per NEC 240.6
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.11: Breaker Pole Count Shown
**Check:** Number of poles shown (1P, 2P, 3P) for each breaker
**Code Reference:** Best practice
**Common Mistakes:** Pole count assumed rather than explicitly shown
**Pass Criteria:** Pole count clearly indicated for all breakers
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.12: Wire Size Shown
**Check:** Conductor size (AWG or kcmil) shown for all circuits
**Code Reference:** NEC 110.14, 240.4
**Common Mistakes:** Wire size missing, undersized for load or OCPD
**Pass Criteria:** Wire sizes shown, adequate for load and properly protected
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.13: Conductor Count Shown
**Check:** Number of conductors shown (e.g., "#12-2/G", "12-3/G")
**Code Reference:** Best practice
**Common Mistakes:** Conductor count missing, neutral/ground not indicated
**Pass Criteria:** Conductor count shown including ground (e.g., 12-2/G)
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.14: Raceway Size and Type Shown
**Check:** Conduit or raceway size and type shown for each circuit
**Code Reference:** NEC Chapter 9, Table 4
**Common Mistakes:** Raceway size missing, undersized per fill requirements
**Pass Criteria:** Raceway type (EMT, PVC, etc.) and size shown
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.15: Circuit Load Shown (VA or Amps)
**Check:** Connected load shown for each circuit in VA or amperes
**Code Reference:** NEC 220.14
**Common Mistakes:** Load column blank, loads don't match actual devices on plan
**Pass Criteria:** Loads shown and match devices on plan
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.16: Load Balance Verified
**Check:** Loads balanced across phases within 10%
**Code Reference:** NEC 220.61 (for neutral calc), best practice for balance
**Common Mistakes:** All loads on one phase, imbalance >20%
**Pass Criteria:** Phase loads within 10% of each other
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.17: Sum of Breakers ≤ Panel Rating
**Check:** Total amp rating of all breakers does not exceed panel bus rating
**Code Reference:** NEC 408.36
**Common Mistakes:** Sum of breakers exceeds bus rating without calculation
**Pass Criteria:** Sum of breakers ≤ bus rating, or calc shows diversity
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.18: Calculated Panel Load Shown
**Check:** Total calculated load shown (considering demand factors)
**Code Reference:** NEC Article 220
**Common Mistakes:** Total load = sum of breakers without demand factors
**Pass Criteria:** Calculated load shown with demand factors applied
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.19: Spare Circuits Provided
**Check:** Spare circuits provided (10-20% typical)
**Code Reference:** Best practice, owner requirements
**Common Mistakes:** No spares, spares not clearly labeled
**Pass Criteria:** Adequate spares provided and clearly labeled "SPARE"
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.20: Space for Future Breakers
**Check:** Physical space in panel for future breakers noted
**Code Reference:** Best practice
**Common Mistakes:** Panel fully populated with no room for expansion
**Pass Criteria:** Space available noted in schedule
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.21: GFCI Protection Identified
**Check:** GFCI-protected circuits clearly identified
**Code Reference:** NEC 210.8
**Common Mistakes:** GFCI required by code but not shown on schedule
**Pass Criteria:** GFCI shown where required (bathrooms, kitchens, exteriors, etc.)
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.22: AFCI Protection Identified
**Check:** AFCI-protected circuits clearly identified
**Code Reference:** NEC 210.12
**Common Mistakes:** AFCI required for dwelling bedrooms but not shown
**Pass Criteria:** AFCI shown where required (dwelling units per NEC 210.12)
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.23: Emergency Circuits Identified
**Check:** Emergency power circuits clearly identified (typically red text)
**Code Reference:** NEC Article 700
**Common Mistakes:** Emergency circuits not differentiated from normal
**Pass Criteria:** Emergency circuits clearly identified with color or note
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.24: Service Load Calculation Attached
**Check:** Service load calculation per NEC Article 220 attached and sealed
**Code Reference:** NEC 220.40 (standard) or 220.82 (optional for dwellings)
**Common Mistakes:** Calc not sealed, method not identified, outdated
**Pass Criteria:** Current calculation, PE sealed, method clearly shown
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 3.25: Panel Directory Specified
**Check:** Note requires panel directory to be typed or neatly printed
**Code Reference:** NEC 408.4
**Common Mistakes:** No requirement for directory, handwritten directories allowed
**Pass Criteria:** Note requires legible typed directory
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

---

## Section 4: Power Plan Review (20 Items)

### Item 4.1: Receptacles Located and Dimensioned
**Check:** All receptacles shown on plan with dimensions to walls
**Code Reference:** NEC 210.52 (spacing requirements)
**Common Mistakes:** Receptacles shown but not dimensioned
**Pass Criteria:** Receptacles located with dimensions from nearest wall or reference
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.2: Receptacle Spacing Meets Code
**Check:** Receptacle spacing meets NEC 210.52 requirements
**Code Reference:** NEC 210.52(A) - 12 ft / 6 ft rule for dwellings
**Common Mistakes:** Receptacles >12 ft apart, wall spaces >2 ft without receptacle
**Pass Criteria:** Spacing meets NEC 210.52 for occupancy type
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.3: Receptacle Heights Specified
**Check:** Receptacle mounting heights specified
**Code Reference:** ADA/ANSI A117.1 (15"-48" AFF), NEC 406.5(E) (countertops)
**Common Mistakes:** Heights not shown, conflict with accessibility requirements
**Pass Criteria:** Heights shown and meet accessibility requirements
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.4: GFCI Receptacles Identified
**Check:** GFCI receptacles clearly identified where required
**Code Reference:** NEC 210.8 (bathrooms, kitchens, outdoors, crawl spaces, etc.)
**Common Mistakes:** GFCI required locations without GFCI shown
**Pass Criteria:** GFCI identified in all required locations per NEC 210.8
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.5: Dedicated Equipment Circuits
**Check:** Dedicated circuits provided for required equipment
**Code Reference:** NEC 210.11(C) - laundry, 210.52(B) - small appliance
**Common Mistakes:** Equipment sharing circuit with general receptacles
**Pass Criteria:** Dedicated circuits shown for all required equipment
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.6: Circuit Home Runs Shown
**Check:** Home run arrows clearly show panel and circuit number for all devices
**Code Reference:** Best practice
**Common Mistakes:** Home runs missing, illegible, or ambiguous
**Pass Criteria:** Every device shows clear home run with panel and circuit #
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.7: Switch Locations and Heights
**Check:** Switches located and dimensioned, heights specified
**Code Reference:** ADA/ANSI A117.1 (15"-48" AFF)
**Common Mistakes:** Switches behind doors, not at entry side of room
**Pass Criteria:** Switches located at latch side of door, heights shown
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.8: 3-Way and 4-Way Switching Shown
**Check:** Multi-location switching clearly shown with designations
**Code Reference:** Best practice
**Common Mistakes:** 3-way/4-way not identified, switching logic unclear
**Pass Criteria:** 3-way, 4-way clearly labeled with switching logic shown
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.9: Floor Boxes and Poke-Throughs
**Check:** Floor boxes/poke-throughs shown with fire rating if required
**Code Reference:** NEC 314.27, fire rating per IBC
**Common Mistakes:** Floor penetrations without fire rating through rated floor
**Pass Criteria:** Floor devices shown, fire rating noted if required
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.10: Equipment Connections Shown
**Check:** All equipment requiring power shown with connection details
**Code Reference:** NEC 422, 424, 430 (various equipment)
**Common Mistakes:** Equipment on architectural plans but no electrical connection shown
**Pass Criteria:** All equipment has electrical connection shown
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.11: Disconnect Switches for Equipment
**Check:** Disconnect switches provided per NEC requirements
**Code Reference:** NEC 422.31 (appliances), 424.19 (HVAC), 430.102 (motors)
**Common Mistakes:** No disconnect for HVAC equipment, disconnect not within sight
**Pass Criteria:** Disconnects provided per NEC, within sight or lockable
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.12: Motor Circuit Sizing
**Check:** Motor circuits sized per NEC Article 430
**Code Reference:** NEC 430.22 (conductor), 430.52 (OCPD), 430.6 (FLA tables)
**Common Mistakes:** Motor circuits sized on nameplate instead of NEC tables
**Pass Criteria:** Motor circuits sized per NEC 430, not nameplate
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.13: Outdoor Receptacles
**Check:** Outdoor receptacles shown with GFCI protection and weather-resistant/WP covers
**Code Reference:** NEC 210.8(A)(3), 406.9(A) & (B)
**Common Mistakes:** Outdoor receptacles without GFCI, non-WR rated
**Pass Criteria:** Outdoor receptacles GFCI protected, WR/WP per NEC 406.9
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.14: Elevator Power Shown
**Check:** Elevator power supply shown with disconnect at hoistway
**Code Reference:** NEC Article 620
**Common Mistakes:** Elevator power not coordinated with elevator drawings
**Pass Criteria:** Elevator power shown, disconnect per NEC 620.51
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.15: Kitchen Equipment Circuits
**Check:** Kitchen equipment circuits sized appropriately for loads
**Code Reference:** NEC 220.55 (ranges), 210.19(A)(3) (continuous loads)
**Common Mistakes:** Undersized circuits, inadequate receptacles for equipment
**Pass Criteria:** All kitchen equipment properly circuited per NEC 220
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.16: Tamper-Resistant Receptacles
**Check:** Tamper-resistant receptacles specified where required
**Code Reference:** NEC 406.12 (dwelling units, child care, education, health care)
**Common Mistakes:** TR not specified in required occupancies
**Pass Criteria:** TR receptacles noted in all required locations
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.17: Isolated Ground Receptacles (If Applicable)
**Check:** Isolated ground receptacles identified with insulated EGC
**Code Reference:** NEC 250.96(B), 250.146(D)
**Common Mistakes:** IG receptacles without insulated EGC to panel
**Pass Criteria:** IG receptacles shown with separate insulated EGC
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.18: Panelboard Locations and Clearances
**Check:** Panel locations shown on plan with NEC clearances
**Code Reference:** NEC 110.26 (36"x30" clear space min)
**Common Mistakes:** Panels in closets, behind doors, clearances obstructed
**Pass Criteria:** Panels accessible, clearances maintained per NEC 110.26
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.19: Conduit Routing Coordination
**Check:** Conduit routing coordinated with structure and other trades
**Code Reference:** Best practice
**Common Mistakes:** Conduits through structural members, conflicts with ductwork
**Pass Criteria:** Conduit routing clear of conflicts, structurally sound
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 4.20: Voltage Drop Verified for Long Runs
**Check:** Voltage drop calculated for branch circuits >50 feet
**Code Reference:** NEC 210.19(A) Informational Note No. 4 (3% recommended)
**Common Mistakes:** Long runs with minimum wire size, VD not calculated
**Pass Criteria:** VD calculated, wire upsized if needed to meet 3% recommendation
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

---

## Section 5: Lighting Plan Review (15 Items)

### Item 5.1: Fixture Schedule Complete
**Check:** Lighting fixture schedule includes all required information
**Code Reference:** Best practice, energy code documentation
**Common Mistakes:** Fixture types on plan not in schedule, specs incomplete
**Pass Criteria:** Schedule includes: type, manufacturer, catalog #, lamp, watts, mounting
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.2: Fixture Locations Shown
**Check:** All light fixtures shown on plan in correct locations
**Code Reference:** Best practice, IBC 1006 for means of egress
**Common Mistakes:** Fixtures not centered in rooms, missing in critical areas
**Pass Criteria:** Fixtures logically located for uniform illumination
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.3: Switching Logic Clear
**Check:** Switching clearly shown with 3-way/4-way designations
**Code Reference:** NEC 210.70 (lighting outlet requirements)
**Common Mistakes:** Switching unclear, no way to turn lights on at entry
**Pass Criteria:** Switching logic clear, accessible at all entries
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.4: Lighting Control Systems (If Applicable)
**Check:** Lighting control system (occupancy sensors, daylight harvesting) shown
**Code Reference:** IECC / ASHRAE 90.1 Section 9
**Common Mistakes:** Control requirements not met, control zones unclear
**Pass Criteria:** Control system fully detailed, meets energy code
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.5: Emergency Lighting Provided
**Check:** Emergency lighting provided per IBC requirements
**Code Reference:** IBC 1008.3, NFPA 101 7.9
**Common Mistakes:** Emergency lighting missing at exits, insufficient levels
**Pass Criteria:** Emergency lighting at all exits and egress paths
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.6: Emergency Lighting Calculation
**Check:** Emergency lighting calculation showing 1 fc average, 0.1 fc min
**Code Reference:** IBC 1008.3.4, NFPA 101 7.9.2.1
**Common Mistakes:** No calculation provided, levels don't meet code
**Pass Criteria:** Calculation shows code compliance (1 fc avg, 0.1 fc min)
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.7: Exit Signs Shown
**Check:** Exit signs shown at all required locations
**Code Reference:** IBC 1013, NFPA 101 7.10
**Common Mistakes:** Exit signs missing at egress doors, not visible from all points
**Pass Criteria:** Exit signs at all required locations per IBC 1013
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.8: Exit Sign Circuits on Emergency Power
**Check:** Exit sign circuits clearly identified as emergency
**Code Reference:** NEC 700.16, IBC 1013.6.3
**Common Mistakes:** Exit signs on normal power, battery backup not shown
**Pass Criteria:** Exit signs on emergency circuits or with battery backup
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.9: Exterior Lighting Shown
**Check:** Exterior lighting shown for building perimeter, parking, walkways
**Code Reference:** IBC 1008.3.5, 1205.2
**Common Mistakes:** Inadequate exterior lighting, no photocell control
**Pass Criteria:** Exterior areas adequately lit, photocell control shown
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.10: Exterior Fixture Ratings
**Check:** Exterior fixtures rated for wet or damp location
**Code Reference:** NEC 410.10
**Common Mistakes:** Interior-rated fixtures shown for exterior use
**Pass Criteria:** All exterior fixtures rated wet or damp per location
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.11: Lighting Power Density (LPD) Compliance
**Check:** Lighting power density calculation meets energy code
**Code Reference:** IECC / ASHRAE 90.1 Section 9.1.3
**Common Mistakes:** LPD exceeds allowance, calculation not provided
**Pass Criteria:** LPD calculation provided, meets or exceeds code requirement
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.12: Dimming and Occupancy Sensors
**Check:** Dimming and occupancy sensors shown per energy code
**Code Reference:** IECC / ASHRAE 90.1 Section 9.4
**Common Mistakes:** Energy code requires automatic controls but not shown
**Pass Criteria:** Automatic lighting controls shown per energy code
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.13: Recessed Fixture IC Rating
**Check:** Recessed fixtures in insulated ceilings rated IC
**Code Reference:** NEC 410.116
**Common Mistakes:** Non-IC fixtures in insulated ceilings
**Pass Criteria:** IC-rated fixtures specified for insulated ceilings
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.14: Fixture Mounting Heights
**Check:** Fixture mounting heights shown (especially pendants, wall sconces)
**Code Reference:** ADA/ANSI A117.1 (protruding objects), IBC 1003.3
**Common Mistakes:** Fixtures too low (<80" AFF) creating head hazards
**Pass Criteria:** Fixture heights shown, meet ADA protruding object requirements
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 5.15: Photometric Analysis (If Required)
**Check:** Photometric analysis provided for critical areas
**Code Reference:** Owner requirements, best practice
**Common Mistakes:** Analysis not provided, or provided but doesn't meet levels
**Pass Criteria:** Photometric analysis shows adequate lighting levels
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

---

## Section 6: Fire Alarm Plan Review (10 Items)

### Item 6.1: Fire Alarm Riser Diagram
**Check:** Fire alarm riser diagram shows all circuits, devices, and FACP
**Code Reference:** NFPA 72 Chapter 10
**Common Mistakes:** Riser diagram incomplete, doesn't match floor plans
**Pass Criteria:** Riser diagram complete, matches floor plan device counts
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 6.2: Smoke Detector Spacing
**Check:** Smoke detector spacing meets NFPA 72 requirements
**Code Reference:** NFPA 72 17.7.3.2 (30 ft spacing typical, adjusted for ceiling height)
**Common Mistakes:** Spacing >30 ft, high ceiling spacing not adjusted
**Pass Criteria:** Spacing calculation provided, meets NFPA 72
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 6.3: Heat Detector Spacing
**Check:** Heat detector spacing meets NFPA 72 requirements
**Code Reference:** NFPA 72 17.6.3.1 (50 ft spacing typical for 135°F)
**Common Mistakes:** Wrong detector temperature rating for area
**Pass Criteria:** Heat detectors appropriately rated and spaced per NFPA 72
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 6.4: Manual Pull Station Locations
**Check:** Manual pull stations at all exits, max 200 ft travel distance
**Code Reference:** NFPA 72 17.14.5
**Common Mistakes:** Pull stations missing at exits, travel distance >200 ft
**Pass Criteria:** Pull stations at all exits, spacing meets NFPA 72
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 6.5: Notification Appliance Spacing
**Check:** Horn/strobes spaced per NFPA 72 audible and visible requirements
**Code Reference:** NFPA 72 18.4 (audible), 18.5 (visible)
**Common Mistakes:** Inadequate strobe candela, audible level not calculated
**Pass Criteria:** Audible and visible calculations provided, meet NFPA 72
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 6.6: Fire Alarm Circuit Designations
**Check:** Circuits clearly designated (IDC, NAC, SLC) on plans and riser
**Code Reference:** NFPA 72 Chapter 10
**Common Mistakes:** Circuit types not identified, ambiguous wiring
**Pass Criteria:** All circuits clearly labeled by type on plans
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 6.7: Voltage Drop Calculation
**Check:** Voltage drop calculation for NACs and SLCs provided
**Code Reference:** NFPA 72 12.4.2
**Common Mistakes:** VD not calculated, circuits don't meet panel EOL voltage
**Pass Criteria:** VD calculation shows all circuits within panel limits
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 6.8: Battery Backup Calculation
**Check:** Battery backup calculation shows 24-hour standby + 5-minute alarm
**Code Reference:** NFPA 72 10.6.7.2.1
**Common Mistakes:** Battery calc not provided, doesn't meet 24+0.083 hours
**Pass Criteria:** Battery calculation provided, meets NFPA 72 duration
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 6.9: Fire Alarm Control Panel Location
**Check:** FACP location shown, accessible, and appropriate environment
**Code Reference:** NFPA 72 10.5
**Common Mistakes:** FACP in inaccessible location, not near building entrance
**Pass Criteria:** FACP accessible to fire department, secure from public
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 6.10: Interfaces to Other Systems
**Check:** Interfaces shown (HVAC shutdown, elevator recall, door release, etc.)
**Code Reference:** NFPA 72 21.4, IBC 909 (smoke control)
**Common Mistakes:** Required interfaces not shown or not coordinated
**Pass Criteria:** All required interfaces shown and coordinated
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

---

## Section 7: Grounding and Bonding (10 Items)

### Item 7.1: Grounding Electrode System
**Check:** Grounding electrode system shown with all NEC-required electrodes
**Code Reference:** NEC 250.50, 250.52
**Common Mistakes:** Only one electrode type, water pipe not bonded
**Pass Criteria:** All available electrodes bonded per NEC 250.50
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.2: Grounding Electrode Conductor Sizing
**Check:** GEC sized per NEC Table 250.66
**Code Reference:** NEC 250.66
**Common Mistakes:** GEC undersized, not based on largest service conductor
**Pass Criteria:** GEC sized correctly per NEC 250.66
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.3: Main Bonding Jumper
**Check:** Main bonding jumper shown at service disconnect
**Code Reference:** NEC 250.28
**Common Mistakes:** MBJ not shown, or shown at subpanel (illegal)
**Pass Criteria:** MBJ shown only at service disconnect, sized per 250.28
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.4: Equipment Grounding Conductor Sizing
**Check:** EGCs sized per NEC Table 250.122
**Code Reference:** NEC 250.122
**Common Mistakes:** EGC undersized, not increased when conductor upsized
**Pass Criteria:** All EGCs meet Table 250.122 minimum, upsized proportionally
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.5: Subpanel Grounding
**Check:** Subpanels show separate ground and neutral bars, no bonding jumper
**Code Reference:** NEC 408.40, 250.142(B)
**Common Mistakes:** Subpanel has bonding jumper, or ground/neutral not separated
**Pass Criteria:** Subpanels have separate ground/neutral, no bonding jumper
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.6: Metal Water Pipe Bonding
**Check:** Metal water pipe bonded within 5 feet of entry
**Code Reference:** NEC 250.52(A)(1), 250.68(C)(1)
**Common Mistakes:** Water pipe not bonded, bonding >5 ft from entry
**Pass Criteria:** Water pipe bonded within 5 ft of entry per NEC 250.68(C)(1)
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.7: Gas Pipe Bonding
**Check:** Gas piping bonded if metal (CSST requires bonding per IFGC)
**Code Reference:** NEC 250.104(B), IFGC 310.1 (CSST bonding)
**Common Mistakes:** CSST not bonded, bonding jumper undersized
**Pass Criteria:** Gas piping bonded per NEC 250.104(B) and IFGC
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.8: Structural Steel Bonding
**Check:** Structural steel bonded if used as grounding electrode
**Code Reference:** NEC 250.52(A)(2), 250.68(C)(2)
**Common Mistakes:** Steel not effectively grounded, bonding not shown
**Pass Criteria:** Steel bonding shown if used as electrode per 250.52(A)(2)
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.9: Communications System Grounding
**Check:** Telecom/data systems bonded to electrical grounding system
**Code Reference:** NEC Article 800, 810, 820, 830
**Common Mistakes:** Separate ground rods for telecom (creates potential difference)
**Pass Criteria:** All systems bonded together per NEC 250.94
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 7.10: Equipment Grounding at Separate Buildings
**Check:** Separate building grounding shown with electrode and GEC
**Code Reference:** NEC 250.32
**Common Mistakes:** No grounding electrode at separate building
**Pass Criteria:** Separate building has electrode system per NEC 250.32
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

---

## Section 8: Details and Specifications (10 Items)

### Item 8.1: Details Match Plans
**Check:** All detail callouts on plans reference existing details
**Code Reference:** Best practice
**Common Mistakes:** Detail callouts with no corresponding detail sheet
**Pass Criteria:** Every callout references a real detail
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 8.2: Details Constructible
**Check:** Details provide sufficient information for construction
**Code Reference:** Best practice
**Common Mistakes:** Details too generic, no manufacturer info
**Pass Criteria:** Details show specific assemblies with part numbers
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 8.3: Service Entrance Detail
**Check:** Service entrance detail shows complete installation
**Code Reference:** NEC Articles 230, 250
**Common Mistakes:** Grounding detail missing, meter not shown
**Pass Criteria:** Complete service entrance with all NEC requirements
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 8.4: Panel Mounting Detail
**Check:** Panel mounting detail shows backing, mounting height, clearances
**Code Reference:** NEC 110.26, 404.8(A)
**Common Mistakes:** No backing specified, height not shown
**Pass Criteria:** Detail shows backing, height, and clearances
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 8.5: Conduit Support Detail
**Check:** Conduit support and hanger spacing shown
**Code Reference:** NEC 344.30 (EMT), 352.30 (PVC), etc.
**Common Mistakes:** Support spacing exceeds NEC requirements
**Pass Criteria:** Support spacing meets NEC for raceway type
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 8.6: Underground Conduit Detail
**Check:** Underground conduit detail shows depth, backfill, warning tape
**Code Reference:** NEC 300.5, Table 300.5
**Common Mistakes:** Insufficient depth, no warning tape
**Pass Criteria:** Depth meets NEC Table 300.5, warning tape shown
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 8.7: Roof Penetration Detail
**Check:** Roof penetrations detailed with waterproofing and flashing
**Code Reference:** Best practice, roofing standards
**Common Mistakes:** No flashing detail, conflicts with roofing warranty
**Pass Criteria:** Complete waterproof detail, coordinated with roofing
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 8.8: Fire-Rated Penetration Detail
**Check:** Fire-rated penetrations detailed with UL-listed firestop system
**Code Reference:** IBC 714.3, UL Fire Resistance Directory
**Common Mistakes:** Generic "firestop" note without UL system number
**Pass Criteria:** Specific UL firestop system referenced
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 8.9: Specification Sections Referenced
**Check:** Details reference applicable specification sections
**Code Reference:** Best practice
**Common Mistakes:** No spec references, or references to non-existent sections
**Pass Criteria:** All details reference current spec sections
- [ ] Pass  [ ] Fail  [ ] N/A
**Notes:** ________________________________________________

### Item 8.10: Arc Flash Warning Label Detail
**Check:** Arc flash warning label detail shown with required information
**Code Reference:** NFPA 70E 130.5(H)
**Common Mistakes:** Label requirements not specified
**Pass Criteria:** Label detail shows all required NFPA 70E information
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
- **QA-201-ELEC through QA-215-ELEC**: Electrical system validation rules
- **QA-001-GENERAL**: Title block and general drawing requirements
- **QA-101-COORD**: Interdisciplinary coordination rules

When automated QA tools are available, this checklist serves as validation criteria for automated checks and manual review of items that cannot be automated (e.g., engineering judgment, constructibility review).

---

**Document Version:** 1.0
**Last Updated:** 2025-01-22
**Next Review:** 2026-01-22
**Owner:** Electrical Engineering Standards Committee
