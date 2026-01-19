# Code Reference Taxonomy

## Overview

This document provides a hierarchical taxonomy of building codes, standards, and regulations relevant to MEP (Mechanical, Electrical, Plumbing) design and construction. It maps code articles to design tasks and QA validation rules, enabling automated code compliance checking for engineering drawings.

---

## 1. Code Classification Hierarchy

### 1.1 Code Categories
1. **Building Codes** - General building safety and construction (IBC, IRC)
2. **Electrical Codes** - Electrical system safety (NEC)
3. **Mechanical Codes** - HVAC and ventilation (IMC, ASHRAE)
4. **Plumbing Codes** - Water supply and drainage (IPC, UPC)
5. **Fire Codes** - Fire protection and life safety (NFPA)
6. **Energy Codes** - Energy efficiency (ASHRAE 90.1, IECC)
7. **Accessibility Standards** - ADA compliance
8. **Standards and Guidelines** - Industry best practices (ASHRAE, SMACNA, IEEE)

---

## 2. International Building Code (IBC)

### 2.1 IBC Chapters Relevant to MEP

#### Chapter 3 - Occupancy Classification and Use
**MEP Relevance:** Determines design criteria based on occupancy type

| Section | Topic | MEP Impact |
|---------|-------|-----------|
| 303 | Assembly Occupancy | High occupant load → increased ventilation, egress lighting |
| 304 | Business Occupancy | Standard office HVAC, power density |
| 305 | Educational Occupancy | Ventilation rates, emergency lighting |
| 307 | High-Hazard Occupancy | Special exhaust, electrical classification (Class I) |
| 308 | Institutional Occupancy | Healthcare electrical (NEC 517), life safety systems |
| 310 | Residential Occupancy | Dwelling unit load calculations (NEC 220) |

**QA Rule:** Verify MEP systems designed for correct occupancy classification.

---

#### Chapter 4 - Special Detailed Requirements Based on Use and Occupancy
| Section | Topic | MEP Impact |
|---------|-------|-----------|
| 403 | High-Rise Buildings | Standby power, fire pump, emergency/standby lighting, smoke control |
| 407 | Group I-2 (Hospitals) | Essential electrical systems (NEC 517), medical gas (NFPA 99) |
| 408 | Group I-3 (Jails/Prisons) | Security power systems, detention/correctional HVAC |
| 410 | Stages and Platforms | Stage lighting (NEC 520), fire suppression |
| 415 | Group H (High-Hazard) | Explosion-proof electrical, hazardous exhaust ventilation |

**QA Rule:** High-rise buildings must include emergency generator and fire pump.

---

#### Chapter 7 - Fire and Smoke Protection Features
| Section | Topic | MEP Impact |
|---------|-------|-----------|
| 714 | Fire-Resistance-Rated Assemblies | Penetrations must maintain fire rating (firestop systems) |
| 716 | Fire-Resistance-Rated Ducts | Fire/smoke dampers in rated walls and floors |
| 717 | Concealed Spaces | HVAC plenums, sprinkler protection requirements |

**QA Rule:** All MEP penetrations through fire-rated assemblies must have firestop details.

---

#### Chapter 9 - Fire Protection and Life Safety Systems
| Section | Topic | MEP Impact |
|---------|-------|-----------|
| 901 | General Fire Protection | Fire alarm (NFPA 72), sprinkler (NFPA 13) requirements |
| 903 | Automatic Sprinkler Systems | Where sprinklers required, design criteria |
| 904 | Alternative Fire Suppression | Clean agent (data centers), kitchen hood suppression |
| 907 | Fire Alarm and Detection | Fire alarm system requirements, device placement |
| 909 | Smoke Control Systems | Mechanical smoke control design |

**QA Rule:** Verify sprinkler and fire alarm systems installed where required by IBC 903/907.

---

#### Chapter 10 - Means of Egress
| Section | Topic | MEP Impact |
|---------|-------|-----------|
| 1008 | Doors, Gates, and Turnstiles | Electrical panic hardware, access control |
| 1008.3 | Emergency Escape and Rescue Openings | Egress windows in residential |
| 1011.2 | Exit Sign Illumination | Exit signs required at all egress doors |
| 1013.6 | Illumination | Egress lighting minimum 1 footcandle |

**QA Rule:** Exit signs required at all egress doors, emergency lighting in egress paths.

---

#### Chapter 12 - Interior Environment
| Section | Topic | MEP Impact |
|---------|-------|-----------|
| 1203 | Ventilation | Mechanical or natural ventilation required |
| 1204 | Temperature Control | Heating systems required in cold climates |
| 1205 | Lighting | Natural or artificial lighting required |
| 1208 | Interior Space Dimensions | Ceiling height minimums affect ductwork routing |

**QA Rule:** Minimum ventilation rates per IMC or ASHRAE 62.1.

---

#### Chapter 29 - Plumbing Systems
| Section | Topic | MEP Impact |
|---------|-------|-----------|
| 2902 | Minimum Plumbing Facilities | Minimum fixture counts by occupancy |
| 2903 | Required Facilities | Accessible fixtures, drinking fountains |

**QA Rule:** Verify fixture counts meet IBC Table 2902.1.

---

#### Chapter 30 - Elevators and Conveying Systems
| Section | Topic | MEP Impact |
|---------|-------|-----------|
| 3003 | Elevator Machine Rooms | HVAC and lighting for machine rooms |
| 3006 | Elevators and Escalators | Elevator power and emergency power |

**QA Rule:** Elevator machine rooms require dedicated HVAC and lighting.

---

## 3. National Electrical Code (NEC / NFPA 70)

### 3.1 NEC Articles Mapped to Design Tasks

#### Article 90 - Introduction
**Purpose:** Scope, organization, and enforcement of NEC

**QA Rule:** Verify NEC edition adopted by local jurisdiction.

---

#### Article 110 - Requirements for Electrical Installations
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 110.26 | Working Clearances | Panel location layout | Verify 36" min working space in front of panels |
| 110.14 | Electrical Connections | Termination sizing | Use 75°C column for conductor sizing unless marked otherwise |
| 110.16 | Arc-Flash Hazard Warning | Safety labeling | Provide arc-flash labels on equipment |

---

#### Article 210 - Branch Circuits
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 210.8 | GFCI Protection | Receptacle layout | GFCI required in bathrooms, kitchens, outdoors, basements, garages |
| 210.12 | AFCI Protection | Residential circuits | AFCI required for dwelling unit 15A/20A branch circuits |
| 210.19 | Conductor Sizing | Wire sizing | Voltage drop max 3% branch circuits |
| 210.52 | Dwelling Unit Receptacles | Receptacle spacing | Receptacles spaced max 12 ft apart on walls |
| 210.70 | Lighting Outlets | Lighting layout | Lighting outlet required in every habitable room |

---

#### Article 215 - Feeders
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 215.2 | Feeder Conductor Sizing | Feeder sizing | Voltage drop max 2% feeders (5% total) |
| 215.10 | Ground-Fault Protection | Service equipment | GFP required for 1000A+ services at 480/277V |

---

#### Article 220 - Branch-Circuit, Feeder, and Service Load Calculations
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 220.12 | Lighting Load | Load calculation | General lighting: 3 VA/sqft (dwelling), varies by occupancy |
| 220.14 | Other Loads | Load calculation | Receptacles: 180 VA per outlet |
| 220.40 | Dwelling Unit Standard Method | Service sizing | Kitchen: 1500 VA per small appliance circuit |
| 220.52 | Small-Appliance Circuits | Kitchen circuits | Minimum 2 small-appliance circuits in dwelling kitchens |
| 220.82 | Dwelling Unit Optional Method | Service sizing | Alternative calculation for dwelling service size |

---

#### Article 230 - Services
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 230.42 | Service Conductor Size | Service sizing | Minimum 100A service for single-family dwelling |
| 230.70 | Service Disconnect | Main breaker location | Service disconnect accessible, max 6 throws |
| 230.95 | Ground-Fault Protection | Service design | GFP for 1000A+ solidly grounded wye services |

---

#### Article 240 - Overcurrent Protection
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 240.4 | Conductor Protection | OCPD sizing | OCPD rating ≤ conductor ampacity (with exceptions) |
| 240.6 | Standard OCPD Ratings | Breaker selection | Use standard breaker sizes: 15, 20, 30, 40, 50, 60, etc. |
| 240.21 | Feeder Taps | Tap rules | 10-ft tap rule, 25-ft tap rule for feeders |

---

#### Article 250 - Grounding and Bonding
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 250.4 | General Requirements | Grounding system design | Establish effective ground-fault current path |
| 250.50 | Grounding Electrode System | Grounding design | Use all available electrodes (water pipe, building steel, rods) |
| 250.52 | Grounding Electrodes | Grounding design | Ground rods minimum 8 ft long, 6 ft spacing |
| 250.66 | Grounding Electrode Conductor | Wire sizing | Size per Table 250.66 based on service conductors |
| 250.122 | Equipment Grounding Conductor | Wire sizing | Size per Table 250.122 based on OCPD rating |

---

#### Article 400 - Flexible Cords and Cables
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 400.8 | Uses Not Permitted | Cord usage | Flexible cords not permitted as permanent wiring |

---

#### Article 404 - Switches
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 404.2 | Switch Connections | Switch wiring | Switches in grounded conductor prohibited (except specific cases) |
| 404.8 | Accessibility | Switch location | Switches accessible, not behind doors |
| 404.9 | Provisions for General-Use Switches | Switch height | Max height 6 ft-7 in. to center, ADA: 48 in. max |

---

#### Article 406 - Receptacles, Cord Connectors, and Attachment Plugs
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 406.4 | Receptacle Mounting | Receptacle installation | Boxes flush with combustible surfaces, recessed max 1/4" |
| 406.9 | Receptacles in Damp/Wet Locations | Outdoor receptacles | Weatherproof covers required, WP while in use |

---

#### Article 408 - Switchboards, Switchgear, and Panelboards
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 408.4 | Circuit Directory | Panel schedule | All panels require circuit directory/schedule |
| 408.36 | Overcurrent Protection | Panel sizing | Panelboard main OCPD required (with exceptions) |

---

#### Article 410 - Luminaires, Lampholders, and Lamps
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 410.10 | Luminaires in Specific Locations | Fixture placement | Fixtures in clothes closets: clearances required |
| 410.16 | Clearances | Fixture installation | Recessed fixtures: clearances from thermal insulation |
| 410.36 | Wet and Damp Locations | Exterior lighting | Fixtures rated for wet/damp locations |

---

#### Article 430 - Motors, Motor Circuits, and Controllers
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 430.6 | Ampacity Determination | Motor circuit sizing | Use FLA from nameplate or NEC tables |
| 430.22 | Conductor Sizing | Wire sizing | Motor circuit conductors: 125% of FLA |
| 430.32 | Overload Protection | Motor protection | Overload: 115-125% of FLA |
| 430.52 | Branch-Circuit OCPD | Breaker sizing | Branch-circuit OCPD: 250% of FLA (inverse time breaker) |
| 430.102 | Disconnect Location | Disconnect placement | Disconnect within sight of motor |

---

#### Article 445 - Generators
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 445.13 | Ampacity of Conductors | Generator feeder sizing | Conductors: 115% of generator nameplate rating |

---

#### Article 450 - Transformers
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 450.3 | Overcurrent Protection | Transformer protection | Primary/secondary OCPD per Table 450.3(B) |
| 450.9 | Ventilation | Transformer room design | Adequate ventilation for heat dissipation |
| 450.21 | Dry-Type Transformers | Transformer location | Transformers 600V and less: 12" clearance from combustibles |

---

#### Article 517 - Health Care Facilities
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 517.13 | Grounding | Hospital grounding | Insulated equipment grounding in patient care areas |
| 517.18 | Patient Care Areas | Circuit design | Min 8 receptacles in critical care areas |
| 517.30 | Essential Electrical System | Emergency power | 3 branches: life safety, critical, equipment |

---

#### Article 520 - Theaters, Audience Areas, and Similar Locations
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 520.5 | Wiring Methods | Stage wiring | Type MC, Type AC cable permitted for stage circuits |

---

#### Article 625 - Electric Vehicle Charging Systems
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 625.40 | Electric Vehicle Supply Equipment Connection | EVSE design | Listed EVSE required |
| 625.42 | Cord-and-Plug-Connected EVSE | Receptacle circuits | 125% continuous load for circuit sizing |

---

#### Article 690 - Solar Photovoltaic (PV) Systems
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 690.7 | Maximum Voltage | PV string design | Max voltage based on coldest expected temperature |
| 690.8 | Circuit Sizing | Conductor sizing | PV circuit conductors: 156% of short-circuit current |
| 690.12 | Rapid Shutdown | Rooftop PV | Array rapid shutdown required within 30 seconds |

---

#### Article 695 - Fire Pumps
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 695.3 | Power Source | Fire pump power | Dedicated service or ahead of main disconnect |
| 695.4 | Conductors | Wire sizing | No OCPD on fire pump supply, supervised disconnect |
| 695.6 | Power Wiring | Feeder routing | Fire pump feeders isolated from other building wiring |

---

#### Article 700 - Emergency Systems
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 700.5 | Transfer Equipment | ATS design | Automatic transfer switch required |
| 700.10 | Wiring | Emergency wiring | Emergency circuits separate from normal circuits |
| 700.12 | Power Sources | Generator/battery | 10-second transfer time max for emergency systems |

---

#### Article 701 - Legally Required Standby Systems
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 701.7 | Transfer Equipment | ATS design | Automatic transfer switch required |
| 701.12 | Power Sources | Generator design | 60-second transfer time max for standby systems |

---

#### Article 702 - Optional Standby Systems
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 702.5 | Transfer Equipment | ATS design | Manual or automatic transfer permitted |

---

## 4. International Mechanical Code (IMC)

### 4.1 IMC Chapters Mapped to HVAC Design

#### Chapter 4 - Ventilation
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 403 | Mechanical Ventilation | Outdoor air calculation | Min outdoor air per ASHRAE 62.1 or IMC Table 403.3 |
| 401.3 | Outdoor Air | OA intake location | OA intake 10 ft from contamination sources |

**QA Rule:** Verify outdoor air CFM meets ASHRAE 62.1 or IMC 403.3.

---

#### Chapter 5 - Exhaust Systems
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 501 | General | Exhaust systems | Exhaust required for bathrooms, kitchens, hazardous areas |
| 505 | Domestic Kitchen Exhaust | Residential kitchen exhaust | 100 CFM intermittent or 25 CFM continuous |

**QA Rule:** Toilet rooms require exhaust: 50 CFM per water closet, 50 CFM per urinal.

---

#### Chapter 6 - Duct Systems
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 601 | General | Duct design | Ducts designed per SMACNA standards |
| 606 | Smoke Detection Systems | Fire/smoke dampers | Duct smoke detectors required in air distribution systems >2000 CFM |

**QA Rule:** Duct smoke detectors required for AHUs >2000 CFM per IMC 606.2.

---

#### Chapter 9 - Specific Appliances
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 904 | Commercial Kitchen Hoods | Kitchen exhaust | Type I hoods for grease-producing appliances |
| 918 | Evaporative Coolers | HVAC design | Water quality and blowdown requirements |

**QA Rule:** Commercial kitchen hoods require fire suppression system (NFPA 96).

---

## 5. ASHRAE Standards

### 5.1 ASHRAE 62.1 - Ventilation for Acceptable Indoor Air Quality
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 6.2 | Ventilation Rate Procedure | OA calculation | Outdoor air = People OA + Area OA |
| Table 6-1 | Minimum Ventilation Rates | OA rates by space type | Office: 5 CFM/person + 0.06 CFM/sqft |

**QA Rule:** Calculate outdoor air per ASHRAE 62.1 Ventilation Rate Procedure.

---

### 5.2 ASHRAE 90.1 - Energy Standard for Buildings
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 6.4 | HVAC Equipment Efficiency | Equipment selection | Minimum efficiency per Tables 6.8.1-1 through 6.8.1-18 |
| 9.1 | Lighting Power Allowance | Lighting design | Max lighting power density per Table 9.5.1 or 9.6.1 |
| 9.4 | Lighting Controls | Lighting controls | Occupancy sensors, automatic shutoff, daylighting controls |

**QA Rule:** Lighting power density must not exceed ASHRAE 90.1 Table 9.5.1 (building area method) or 9.6.1 (space-by-space method).

---

### 5.3 ASHRAE 135 - BACnet Protocol
**Purpose:** Building automation and control network communication protocol

**QA Rule:** BAS systems specify BACnet protocol for interoperability.

---

## 6. International Plumbing Code (IPC)

### 6.1 IPC Chapters Mapped to Plumbing Design

#### Chapter 4 - Fixtures, Faucets, and Fixture Fittings
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 403 | Minimum Plumbing Facilities | Fixture count | Min fixture counts per IPC Table 403.1 based on occupancy |
| 405 | Installation of Fixtures | Fixture layout | Clearances per IPC 405 and ADA |

**QA Rule:** Verify fixture counts meet IPC Table 403.1.

---

#### Chapter 6 - Water Supply and Distribution
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 604 | Water Supply System Design Criteria | Pipe sizing | Min 8 PSI residual pressure at fixtures |
| 608 | Protection of Potable Water Supply | Backflow prevention | Backflow preventers required for hazardous connections |
| 610 | Hot Water Supply | DHW design | Max 120°F at fixtures accessible to children/elderly |

**QA Rule:** Water supply pipe sizing per IPC Table 610.3 (fixture unit method).

---

#### Chapter 7 - Sanitary Drainage
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 703 | Drainage System Design | Drain sizing | Sanitary drains sized per IPC Table 703.2 (fixture unit method) |
| 704 | Vent Systems | Vent sizing | Every trap requires vent per IPC 903 |
| 708 | Cleanouts | Cleanout placement | Cleanouts at base of stacks, direction changes, max 100 ft spacing |

**QA Rule:** Drain pipe slope minimum 1/4" per foot (IPC Table 704.1).

---

#### Chapter 9 - Vents
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 903 | Vent Termination | Vent stack roof penetration | Vent termination 6" above roof, 10 ft from vertical surfaces |
| 906 | Vent Sizing | Vent pipe sizing | Vent sizing per IPC Table 916.1 based on fixture units |

**QA Rule:** Verify all fixtures have proper venting per IPC Chapter 9.

---

#### Chapter 11 - Storm Drainage
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 1106 | Roof Drainage | Roof drain sizing | Roof drains sized per IPC Table 1106.3 based on rainfall intensity |
| 1107 | Scuppers | Overflow protection | Scuppers or secondary drains required |

**QA Rule:** Storm drain pipe sizing per IPC Table 1106.3 (rainfall intensity and roof area).

---

## 7. NFPA Standards

### 7.1 NFPA 13 - Installation of Sprinkler Systems
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 8.3 | Obstruction to Sprinkler Discharge | Sprinkler coverage | Min 18" clearance below sprinkler deflector |
| 8.5 | Spacing of Sprinklers | Head spacing | Max 15 ft spacing, max 225 sqft coverage (light hazard) |
| 8.6 | Clearance to Ceiling | Sprinkler placement | Max 12" below ceiling (standard spray) |
| 10.1 | System Components | Sprinkler design | All components listed for fire protection service |

**QA Rule:** Sprinkler heads spaced per NFPA 13 Table 8.6.2.2.1 (max 15 ft spacing, 225 sqft coverage for light hazard).

---

### 7.2 NFPA 14 - Installation of Standpipe and Hose Systems
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 4.2 | Types of Systems | Standpipe design | Class I (2.5" hose), Class II (1.5" hose), Class III (combination) |
| 5.5 | Hose Connection Location | Hose valve placement | Max 5 ft from egress stair entrance |

**QA Rule:** Class I standpipe required in buildings >30 ft above/below grade per IBC 905.3.

---

### 7.3 NFPA 20 - Installation of Stationary Pumps for Fire Protection
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 4.8 | Pump Room | Fire pump room design | Dedicated room, 2-hour fire rating, drainage |
| 9.2 | Electric Motor-Driven Pumps | Fire pump power | Normal and alternate power sources |

**QA Rule:** Fire pump power per NEC Article 695 (ahead of service disconnect).

---

### 7.4 NFPA 72 - National Fire Alarm and Signaling Code
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 17.5 | Smoke Detector Spacing | Device layout | Max 30 ft spacing in smooth ceiling |
| 17.6 | Heat Detector Spacing | Device layout | Spacing per detector listing (typically 30-50 ft) |
| 18.5 | Notification Appliance Spacing | Horn/strobe layout | Visual: min 15 candela at all points (75 sqft per candela typical) |
| 23.3 | Protected Premises Fire Alarm | FACP design | FACP located in normally occupied area |

**QA Rule:** Smoke detectors spaced max 30 ft on smooth ceilings per NFPA 72 17.7.3.2.3.

---

### 7.5 NFPA 96 - Ventilation Control and Fire Protection of Commercial Cooking Operations
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 5.3 | Exhaust Hoods | Kitchen hood design | Type I hoods for grease-producing appliances |
| 10 | Fire-Extinguishing Systems | Hood suppression | Automatic suppression required for Type I hoods |

**QA Rule:** Type I hoods require fire suppression system per NFPA 96 Chapter 10.

---

### 7.6 NFPA 99 - Health Care Facilities Code
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 5.1 | Medical Gas Systems | Medical gas design | Medical gas piping per NFPA 99 |
| 6.3 | Essential Electrical Systems | Hospital power | Per NEC Article 517 |

**QA Rule:** Medical gas outlets at patient care locations per NFPA 99.

---

## 8. Americans with Disabilities Act (ADA)

### 8.1 ADA Standards for Accessible Design
| Section | Topic | Design Task | QA Rule |
|---------|-------|------------|---------|
| 213 | Toilet and Bathing Facilities | Accessible fixtures | Min 5% (min 1) accessible fixtures |
| 308 | Reach Ranges | Device mounting heights | Max reach: 48" forward, 54" side |
| 606 | Lavatories and Sinks | Lavatory design | Knee clearance: 27" high, 8" deep |
| 609 | Grab Bars | Grab bar installation | Side grab: 42" min, rear grab: 36" min |

**QA Rule:** Electrical switches and thermostats max 48" AFF per ADA 308.

---

## 9. Code Cross-Reference Matrix

### 9.1 Design Task → Code Reference Mapping
| Design Task | Primary Code | Article/Section | Validation Rule |
|------------|-------------|----------------|----------------|
| Service sizing | NEC | Article 230 | Min 100A service for dwelling |
| Panel clearances | NEC | 110.26 | 36" working space minimum |
| GFCI receptacles | NEC | 210.8 | Required in bathrooms, kitchens, outdoors, garages |
| Lighting load calculation | NEC | 220.12 | 3 VA/sqft dwelling unit |
| Voltage drop | NEC | 210.19, 215.2 | Max 3% branch, 2% feeder (5% total) |
| Emergency generator | NEC | Article 700 | 10-second transfer time |
| Fire pump power | NEC | Article 695 | Dedicated service ahead of main |
| Ventilation rates | IMC / ASHRAE 62.1 | 403 / Table 6-1 | Min CFM per person + area |
| Sprinkler spacing | NFPA 13 | 8.5 | Max 15 ft spacing, 225 sqft coverage |
| Fixture counts | IPC | 403 | Per Table 403.1 based on occupancy |
| Exit signs | IBC | 1013.6 | At all egress doors |
| Emergency lighting | IBC | 1008.3 | Min 1 footcandle in egress paths |

---

## 10. Code Compliance Validation Rules

### 10.1 Electrical Code Validation Rules
```yaml
rules:
  - rule_id: NEC_110_26_CLEARANCE
    code: NEC 110.26
    description: "Electrical equipment working clearances"
    validation: "Verify 36\" minimum working space in front of electrical panels"
    severity: critical

  - rule_id: NEC_210_8_GFCI
    code: NEC 210.8
    description: "GFCI protection required locations"
    validation: "Verify GFCI receptacles in bathrooms, kitchens, outdoors, garages, basements"
    severity: critical

  - rule_id: NEC_210_52_SPACING
    code: NEC 210.52
    description: "Dwelling receptacle spacing"
    validation: "Verify receptacles spaced max 12 ft apart on walls"
    severity: major

  - rule_id: NEC_220_12_LOAD
    code: NEC 220.12
    description: "General lighting load"
    validation: "Verify lighting load calculation uses correct VA/sqft for occupancy"
    severity: major

  - rule_id: NEC_250_66_GROUNDING
    code: NEC 250.66
    description: "Grounding electrode conductor sizing"
    validation: "Verify GEC sized per Table 250.66 based on service conductors"
    severity: critical
```

---

### 10.2 Mechanical Code Validation Rules
```yaml
rules:
  - rule_id: IMC_403_VENTILATION
    code: IMC 403 / ASHRAE 62.1
    description: "Minimum outdoor air ventilation"
    validation: "Verify outdoor air CFM meets ASHRAE 62.1 or IMC Table 403.3"
    severity: critical

  - rule_id: IMC_606_SMOKE_DET
    code: IMC 606
    description: "Duct smoke detectors"
    validation: "Verify duct smoke detectors for AHUs >2000 CFM"
    severity: major

  - rule_id: ASHRAE_90_1_EQUIPMENT
    code: ASHRAE 90.1 Table 6.8.1
    description: "HVAC equipment efficiency"
    validation: "Verify equipment efficiency meets ASHRAE 90.1 minimums"
    severity: major
```

---

### 10.3 Plumbing Code Validation Rules
```yaml
rules:
  - rule_id: IPC_403_FIXTURES
    code: IPC Table 403.1
    description: "Minimum plumbing fixtures"
    validation: "Verify fixture counts meet IPC Table 403.1 by occupancy"
    severity: critical

  - rule_id: IPC_610_SIZING
    code: IPC Table 610.3
    description: "Water supply pipe sizing"
    validation: "Verify pipe sizing per fixture unit method, min 8 PSI residual"
    severity: major

  - rule_id: IPC_704_SLOPE
    code: IPC Table 704.1
    description: "Drain pipe slope"
    validation: "Verify drain pipe slope minimum 1/4\" per foot"
    severity: major
```

---

### 10.4 Fire Protection Code Validation Rules
```yaml
rules:
  - rule_id: NFPA13_SPACING
    code: NFPA 13 Table 8.6.2.2.1
    description: "Sprinkler head spacing"
    validation: "Verify max 15 ft spacing, 225 sqft coverage for light hazard"
    severity: critical

  - rule_id: NFPA13_CLEARANCE
    code: NFPA 13 8.5.5
    description: "Clearance to sprinkler heads"
    validation: "Verify 18\" clearance below sprinkler deflector, 3\" from obstructions"
    severity: critical

  - rule_id: NFPA72_SMOKE
    code: NFPA 72 17.7.3.2.3
    description: "Smoke detector spacing"
    validation: "Verify smoke detectors spaced max 30 ft on smooth ceilings"
    severity: major

  - rule_id: IBC_903_SPRINKLERS
    code: IBC 903
    description: "Automatic sprinkler requirements"
    validation: "Verify sprinklers installed where required by occupancy/building area"
    severity: critical
```

---

## 11. Jurisdiction-Specific Code Adoptions

### 11.1 Code Adoption Status Tracking
| Jurisdiction | Building Code | Electrical Code | Mechanical Code | Plumbing Code | Fire Code | Energy Code |
|-------------|--------------|----------------|----------------|--------------|-----------|-------------|
| State/National | IBC 2021 | NEC 2020 | IMC 2021 | IPC 2021 | IFC 2021 | IECC 2021 / ASHRAE 90.1-2019 |
| Local Amendments | TBD | TBD | TBD | TBD | TBD | TBD |

**QA Rule:** Verify code editions adopted by local jurisdiction before design.

---

## 12. Code Update Cycle

### 12.1 Code Publication Schedule
| Code | Publishing Organization | Update Cycle | Latest Edition |
|------|------------------------|--------------|---------------|
| IBC | ICC | 3 years | 2024 |
| IRC | ICC | 3 years | 2024 |
| NEC | NFPA | 3 years | 2023 |
| IMC | ICC | 3 years | 2024 |
| IPC | ICC | 3 years | 2024 |
| IECC | ICC | 3 years | 2024 |
| ASHRAE 62.1 | ASHRAE | Variable | 2022 |
| ASHRAE 90.1 | ASHRAE | Variable | 2022 |
| NFPA 13 | NFPA | 3 years | 2022 |
| NFPA 72 | NFPA | 3 years | 2022 |

**QA Rule:** Track code update cycles and jurisdiction adoptions for project compliance.

---

## 13. Conclusion

This code reference taxonomy provides:
- **Hierarchical organization** of all MEP-relevant building codes and standards
- **Direct mapping** from code articles to design tasks
- **Automated validation rules** for code compliance checking
- **Cross-reference matrix** linking design tasks to applicable code sections
- **Jurisdiction tracking** for code edition adoptions

This taxonomy enables systematic code compliance verification throughout the engineering drawing QA/QC process, ensuring designs meet all applicable codes, standards, and regulations.
