# MEP Discipline Taxonomy

## Overview

This document provides a comprehensive taxonomy of MEP (Mechanical, Electrical, Plumbing) disciplines, their associated trades, drawing conventions, CSI divisions, and coordination requirements for engineering drawing QA/QC.

---

## 1. Architecture (ARCH)

### 1.1 Drawing Prefix
- **A** - Architecture
- Example: A-101, A-201, A-301

### 1.2 Primary Responsibilities
- Building layout and spatial organization
- Code compliance (egress, occupancy, accessibility)
- Fire-rated assemblies and separations
- Vertical penetrations and openings
- Finish selections and interior design

### 1.3 CSI MasterFormat Divisions
- **Division 06** - Wood, Plastics, and Composites
- **Division 08** - Openings (doors, windows, glazing)
- **Division 09** - Finishes
- **Division 10** - Specialties

### 1.4 Key Drawing Types
| Drawing Type | Sheet Prefix | Description |
|-------------|--------------|-------------|
| Site Plans | A-001 to A-099 | Overall site layout |
| Floor Plans | A-101 to A-199 | Level-by-level layouts |
| Reflected Ceiling Plans | A-201 to A-299 | Ceiling layouts (shared with E for lighting) |
| Elevations | A-301 to A-399 | Exterior and interior elevations |
| Building Sections | A-401 to A-499 | Vertical cuts through building |
| Wall Sections/Details | A-501 to A-599 | Construction details |
| Schedules | A-601 to A-699 | Door, window, finish schedules |

### 1.5 MEP Coordination Requirements
- Clearances for mechanical equipment
- Door swing conflicts with electrical panels
- Ceiling height vs. duct/pipe routing
- Fire-rated wall/floor penetrations
- ADA accessibility for fixtures and devices
- Egress path clearances from equipment

### 1.6 Code References
- **IBC** - International Building Code (egress, accessibility, fire safety)
- **ADA** - Americans with Disabilities Act Standards
- **NFPA 101** - Life Safety Code

---

## 2. Electrical (ELEC)

### 2.1 Drawing Prefix
- **E** - Electrical
- Example: E-101, E-201, E-301

### 2.2 Discipline Breakdown

#### 2.2.1 Power Distribution
**Scope:** Service equipment, panels, transformers, generators, UPS

**CSI Division:** Division 26 - Electrical

**Key Components:**
- Service entrance and main distribution
- Panelboards and switchboards
- Branch circuit distribution
- Emergency/standby power systems
- Grounding and bonding systems

**NEC Articles:**
- Article 230 - Services
- Article 408 - Switchboards and Panelboards
- Article 700 - Emergency Systems
- Article 701 - Legally Required Standby Systems
- Article 702 - Optional Standby Systems

#### 2.2.2 Lighting Systems
**Scope:** Interior/exterior lighting fixtures, controls, emergency lighting

**CSI Division:** Division 26 - Electrical

**Key Components:**
- Lighting fixtures (recessed, surface, pendant)
- Switches and dimmers
- Occupancy sensors and photocells
- Exit signs and emergency lights
- Lighting control systems (0-10V, DALI, DMX)

**NEC Articles:**
- Article 210 - Branch Circuits
- Article 404 - Switches
- Article 410 - Luminaires

**Energy Codes:**
- ASHRAE 90.1 - Lighting power density
- IECC - Lighting controls

#### 2.2.3 Fire Alarm Systems
**Scope:** Detection, notification, and control systems

**CSI Division:** Division 28 - Electronic Safety and Security

**Key Components:**
- Fire alarm control panels (FACP)
- Smoke and heat detectors
- Manual pull stations
- Horns, strobes, and speakers
- Remote annunciators

**NFPA References:**
- NFPA 72 - National Fire Alarm and Signaling Code

#### 2.2.4 Low Voltage Systems
**Scope:** Data/telecom, AV, security, access control

**CSI Division:** Division 27 - Communications, Division 28 - Electronic Safety and Security

**Key Components:**
- Structured cabling (Cat6, fiber)
- Data outlets and patch panels
- Security cameras and card readers
- Audio/visual systems
- Nurse call, paging, intercom

**Standards:**
- TIA-568 - Commercial Building Telecommunications Cabling
- TIA-569 - Telecommunications Pathways and Spaces
- TIA-606 - Administration Standard

#### 2.2.5 Special Electrical Systems
**Scope:** Specialized electrical installations

**Key Systems:**
- **EV Charging (NEC 625):** Electric vehicle supply equipment
- **Solar PV (NEC 690):** Photovoltaic systems
- **Energy Storage (NEC 706):** Battery energy storage systems
- **Healthcare (NEC 517):** Critical care, patient care areas
- **Data Centers (NFPA 75):** Critical power and cooling

### 2.3 Key Drawing Types
| Drawing Type | Sheet Prefix | Description |
|-------------|--------------|-------------|
| Symbols & Legends | E-001 | Electrical symbols and abbreviations |
| Site Plans | E-002 to E-099 | Site lighting, utility connections |
| Power Plans | E-101 to E-199 | Panel locations, receptacles, equipment |
| Lighting Plans | E-201 to E-299 | Fixture layouts, switching |
| Fire Alarm Plans | E-301 to E-399 | Device locations, notification coverage |
| One-Line Diagrams | E-401 to E-499 | Power distribution schematics |
| Panel Schedules | E-501 to E-599 | Circuit schedules, load calculations |
| Details | E-601 to E-699 | Standard details, mounting heights |

### 2.4 MEP Coordination Requirements
- Panel clearances (36" min working space per NEC 110.26)
- Voltage drop calculations for long circuit runs
- Lighting coordination with ceiling diffusers/sprinklers
- Fire alarm coordination with mechanical smoke control
- Generator/transformer pad coordination with civil
- Electrical room HVAC requirements

### 2.5 Code References
- **NEC** - National Electrical Code (NFPA 70)
- **NFPA 72** - Fire Alarm Code
- **ASHRAE 90.1** - Energy Standard for Buildings
- **IECC** - International Energy Conservation Code

---

## 3. Mechanical (MECH)

### 3.1 Drawing Prefix
- **M** - Mechanical
- Example: M-101, M-201, M-301

### 3.2 Discipline Breakdown

#### 3.2.1 HVAC Systems
**Scope:** Heating, ventilation, and air conditioning

**CSI Division:** Division 23 - Heating, Ventilating, and Air Conditioning

**Key Components:**
- Air handling units (AHU)
- Rooftop units (RTU)
- Chillers, boilers, cooling towers
- Ductwork (supply, return, exhaust)
- Diffusers, grilles, and registers
- Variable air volume (VAV) boxes
- Fan coil units (FCU)
- Energy recovery ventilators (ERV/HRV)

**Code References:**
- IMC - International Mechanical Code
- ASHRAE 62.1 - Ventilation for Acceptable Indoor Air Quality
- ASHRAE 90.1 - Energy Standard for Buildings
- IECC - International Energy Conservation Code

#### 3.2.2 Building Automation Systems (BAS)
**Scope:** HVAC control and monitoring

**CSI Division:** Division 23 - HVAC, Division 25 - Integrated Automation

**Key Components:**
- Building automation controllers (BAC)
- Temperature, humidity, and pressure sensors
- Control dampers and valves
- Variable frequency drives (VFD)
- Setpoint programming and scheduling

**Standards:**
- ASHRAE 135 - BACnet protocol
- ASHRAE 90.1 - Control requirements

#### 3.2.3 Specialty Mechanical
**Key Systems:**
- **Kitchen Ventilation:** Commercial kitchen hoods, Type I/II hoods
- **Laboratory Ventilation:** Fume hoods, lab exhaust systems
- **Medical Gas (NFPA 99):** Oxygen, vacuum, medical air
- **Clean Rooms:** HEPA filtration, pressure control
- **Smoke Control (IBC 909):** Smoke exhaust, pressurization

### 3.3 Key Drawing Types
| Drawing Type | Sheet Prefix | Description |
|-------------|--------------|-------------|
| Symbols & Legends | M-001 | Mechanical symbols and abbreviations |
| Site Plans | M-002 to M-099 | Outdoor equipment, utility connections |
| HVAC Plans | M-101 to M-199 | Equipment locations, ductwork layout |
| Piping Plans | M-201 to M-299 | Hydronic piping (chilled water, hot water) |
| Control Diagrams | M-301 to M-399 | BAS control sequences |
| Riser Diagrams | M-401 to M-499 | Vertical distribution risers |
| Details | M-501 to M-599 | Equipment details, typical connections |
| Schedules | M-601 to M-699 | Equipment schedules |

### 3.4 MEP Coordination Requirements
- Ductwork vs. structural beam clearances
- Equipment access and maintenance clearances
- Electrical coordination for equipment power
- Plumbing coordination for condensate drains
- Fire sprinkler coordination with ductwork
- Acoustic coordination for noise-sensitive spaces

### 3.5 Code References
- **IMC** - International Mechanical Code
- **ASHRAE 62.1** - Ventilation Requirements
- **ASHRAE 90.1** - Energy Efficiency
- **NFPA 96** - Commercial Cooking Operations
- **NFPA 99** - Healthcare Facilities

---

## 4. Plumbing (PLMB)

### 4.1 Drawing Prefix
- **P** - Plumbing
- Example: P-101, P-201, P-301

### 4.2 Discipline Breakdown

#### 4.2.1 Domestic Water Systems
**Scope:** Potable water distribution

**CSI Division:** Division 22 - Plumbing

**Key Components:**
- Cold water piping and distribution
- Hot water generation and circulation
- Water heaters (tank, tankless)
- Booster pumps and pressure regulation
- Backflow preventers
- Mixing valves (thermostatic, pressure-balanced)

**Code References:**
- IPC - International Plumbing Code
- UPC - Uniform Plumbing Code
- ASPE - American Society of Plumbing Engineers standards

#### 4.2.2 Sanitary and Vent Systems
**Scope:** Wastewater collection and venting

**CSI Division:** Division 22 - Plumbing

**Key Components:**
- Sanitary drain piping
- Vent piping (individual, common, stack vents)
- Traps and cleanouts
- Grease interceptors and oil separators
- Sewage ejector pumps

**Code Requirements:**
- Fixture unit calculations
- Trap arm length limitations
- Vent sizing and termination
- Slope requirements (1/4" per foot typical)

#### 4.2.3 Storm Drainage Systems
**Scope:** Rainwater collection and disposal

**CSI Division:** Division 22 - Plumbing

**Key Components:**
- Roof drains and scuppers
- Storm drain piping
- Area drains and trench drains
- Sump pumps
- Overflow protection

**Code References:**
- IPC - International Plumbing Code
- ASPE rainfall intensity calculations

#### 4.2.4 Medical Gas Systems
**Scope:** Healthcare gas distribution (NFPA 99)

**CSI Division:** Division 22 - Plumbing

**Key Components:**
- Medical air, oxygen, nitrogen, nitrous oxide
- Medical vacuum systems
- Waste anesthetic gas disposal (WAGD)
- Zone valves and alarm panels
- Outlets at patient care locations

#### 4.2.5 Fuel Gas Systems
**Scope:** Natural gas and propane distribution

**CSI Division:** Division 22 - Plumbing

**Key Components:**
- Gas meters and regulators
- Gas piping (black steel, CSST)
- Gas valves and shutoffs
- Connections to appliances (boilers, water heaters, kitchen equipment)

**Code References:**
- IFGC - International Fuel Gas Code
- NFPA 54 - National Fuel Gas Code

### 4.3 Key Drawing Types
| Drawing Type | Sheet Prefix | Description |
|-------------|--------------|-------------|
| Symbols & Legends | P-001 | Plumbing symbols and abbreviations |
| Site Plans | P-002 to P-099 | Site utilities, storm drainage |
| Domestic Water Plans | P-101 to P-199 | Cold/hot water distribution |
| Sanitary Plans | P-201 to P-299 | Sanitary drain and vent piping |
| Storm Drain Plans | P-301 to P-399 | Roof drains, storm piping |
| Riser Diagrams | P-401 to P-499 | Vertical water/drain risers |
| Details | P-501 to P-599 | Typical connections, mounting details |
| Schedules | P-601 to P-699 | Fixture schedules, equipment schedules |

### 4.4 MEP Coordination Requirements
- Plumbing fixture locations with architectural layouts
- Floor drains under mechanical equipment
- Condensate drain connections from HVAC equipment
- Hot water circulation coordination with electrical heaters
- Sanitary vent termination above roof line
- Backflow preventer clearances and accessibility

### 4.5 Code References
- **IPC** - International Plumbing Code
- **UPC** - Uniform Plumbing Code
- **IFGC** - International Fuel Gas Code
- **NFPA 54** - National Fuel Gas Code
- **NFPA 99** - Healthcare Facilities (medical gas)
- **ASSE** - American Society of Sanitary Engineering standards

---

## 5. Fire Protection (FP)

### 5.1 Drawing Prefix
- **FP** or **F** - Fire Protection
- Example: FP-101, FP-201

### 5.2 Discipline Breakdown

#### 5.2.1 Automatic Sprinkler Systems
**Scope:** Fire suppression via automatic sprinklers

**CSI Division:** Division 21 - Fire Suppression

**Key Components:**
- Sprinkler heads (pendent, upright, sidewall)
- Fire sprinkler piping (wet, dry, preaction, deluge)
- Sprinkler risers and cross mains
- Fire department connections (FDC)
- Backflow preventers
- Alarm valves and flow switches

**NFPA References:**
- NFPA 13 - Installation of Sprinkler Systems
- NFPA 13R - Sprinkler Systems in Residential Occupancies
- NFPA 13D - Sprinkler Systems in One- and Two-Family Dwellings

**Design Criteria:**
- Occupancy hazard classification (Light, Ordinary, Extra)
- Density (gpm/sqft) and area of application
- Water supply requirements (flow and pressure)
- Hydraulic calculations

#### 5.2.2 Standpipe Systems
**Scope:** Manual fire suppression via hose connections

**CSI Division:** Division 21 - Fire Suppression

**Key Components:**
- Standpipe risers (Class I, II, III)
- Hose valves and connections
- Fire department connections (FDC)
- Hose cabinets with hose and nozzles

**NFPA References:**
- NFPA 14 - Installation of Standpipe and Hose Systems

#### 5.2.3 Clean Agent Systems
**Scope:** Gaseous fire suppression for sensitive equipment

**CSI Division:** Division 21 - Fire Suppression

**Key Systems:**
- FM-200 (HFC-227ea)
- Novec 1230
- Inergen
- CO2 systems

**NFPA References:**
- NFPA 2001 - Clean Agent Fire Extinguishing Systems

**Typical Applications:**
- Data centers and server rooms
- Telecommunications rooms
- Museums and archives
- Electrical/control rooms

#### 5.2.4 Special Hazard Systems
**Key Systems:**
- **Kitchen Hood Suppression (NFPA 96):** Wet chemical systems for commercial kitchens
- **Paint Booth Suppression:** Foam or dry chemical systems
- **Hangar Suppression (NFPA 409):** High-expansion foam systems

### 5.3 Key Drawing Types
| Drawing Type | Sheet Prefix | Description |
|-------------|--------------|-------------|
| Symbols & Legends | FP-001 | Fire protection symbols and abbreviations |
| Sprinkler Plans | FP-101 to FP-199 | Sprinkler head layout, piping |
| Standpipe Plans | FP-201 to FP-299 | Standpipe risers, hose connections |
| Riser Diagrams | FP-301 to FP-399 | Vertical sprinkler/standpipe risers |
| Hydraulic Calculations | FP-401 to FP-499 | Flow calculations, system curves |
| Details | FP-501 to FP-599 | Typical sprinkler details |

### 5.4 MEP Coordination Requirements
- Sprinkler head clearance from lights, diffusers (minimum 3")
- Sprinkler coverage for obstructions (structural beams, ducts)
- Fire pump electrical coordination (NEC Article 695)
- Water supply coordination with plumbing (separate tap required)
- Fire alarm interface with flow/tamper switches
- Access to fire risers and FDCs

### 5.5 Code References
- **NFPA 13** - Sprinkler Systems
- **NFPA 14** - Standpipe Systems
- **NFPA 20** - Installation of Stationary Pumps for Fire Protection
- **NFPA 24** - Installation of Private Fire Service Mains
- **NFPA 25** - Inspection, Testing, and Maintenance of Water-Based Systems
- **NEC Article 695** - Fire Pumps

---

## 6. Structural (STRUC)

### 6.1 Drawing Prefix
- **S** - Structural
- Example: S-101, S-201, S-301

### 6.2 Primary Responsibilities
- Structural integrity and load-bearing capacity
- Foundation design
- Steel and concrete framing
- Floor and roof structural systems
- Lateral load resisting systems (seismic, wind)

### 6.3 CSI MasterFormat Divisions
- **Division 03** - Concrete
- **Division 04** - Masonry
- **Division 05** - Metals (structural steel)

### 6.4 MEP Coordination Requirements
- **Equipment Loading:**
  - Rooftop unit weights and vibration isolation
  - Mechanical room floor loading (chillers, boilers)
  - Transformer and generator pad design
  - Suspended equipment (lights, piping, ductwork)

- **Penetrations:**
  - Core drilling locations for pipes/conduits
  - Beam copes for duct/pipe routing
  - Fire-rated penetration assemblies
  - Structural impact of large openings

- **Clearances:**
  - Minimum headroom for ductwork below beams
  - Depth of steel beams vs. required ceiling height
  - Conflict resolution between structure and MEP routing

### 6.5 Code References
- **IBC** - International Building Code (structural loads)
- **ASCE 7** - Minimum Design Loads for Buildings
- **ACI 318** - Building Code Requirements for Structural Concrete
- **AISC** - Steel Construction Manual

---

## 7. Civil (CIVIL)

### 7.1 Drawing Prefix
- **C** - Civil
- Example: C-101, C-201, C-301

### 7.2 Primary Responsibilities
- Site grading and drainage
- Utilities (water, sewer, storm, gas, electric)
- Paving and hardscape
- Erosion control and stormwater management
- Grounding and lightning protection

### 7.3 CSI MasterFormat Divisions
- **Division 02** - Existing Conditions
- **Division 31** - Earthwork
- **Division 32** - Exterior Improvements
- **Division 33** - Utilities

### 7.4 MEP Coordination Requirements
- **Site Utilities:**
  - Water service connection to building
  - Sanitary sewer connection and cleanouts
  - Storm drain connection
  - Natural gas service
  - Electric utility service and transformer pad

- **Grounding Systems:**
  - Building grounding electrode system (NEC 250)
  - Driven ground rods and ground rings
  - Ufer ground (concrete-encased electrode)
  - Lightning protection grounding (NFPA 780)

- **Exterior Equipment:**
  - Pad-mounted transformers
  - Generator and fuel tank pads
  - Cooling towers and outdoor condensing units
  - Fire department connections (FDC) accessibility

### 7.5 Code References
- **IBC** - International Building Code (site requirements)
- **NEC Article 250** - Grounding and Bonding
- **NFPA 780** - Lightning Protection Systems
- **Local Utility Standards** - Water, sewer, electric service

---

## 8. Cross-Discipline Coordination Matrix

### 8.1 Architectural ↔ MEP Coordination
| Item | Arch Responsibility | MEP Responsibility | Code Reference |
|------|---------------------|-------------------|----------------|
| Ceiling Height | Provide required clear height | Route ducts/pipes within available space | IBC 1208 |
| Fire-Rated Assemblies | Design rated walls/floors | Maintain rating at penetrations | IBC 714 |
| Door Swings | Show door swing on plans | Verify panel/equipment clearances | NEC 110.26 |
| ADA Compliance | Accessible routes and clearances | Accessible fixture mounting heights | ADA Standards |
| Equipment Rooms | Size rooms for equipment | Provide clearances and access | IBC, NEC |

### 8.2 Electrical ↔ Mechanical Coordination
| Item | Electrical | Mechanical | Notes |
|------|-----------|-----------|-------|
| Equipment Power | Size circuits, provide disconnects | Provide nameplate data (FLA, MCA) | NEC 430 |
| Lighting vs. Diffusers | Fixture layout | Diffuser/grille layout | 3" minimum clearance |
| Fire Alarm | Duct smoke detectors | Duct locations for detectors | NFPA 72, IMC 606 |
| Panel Rooms | Provide panel and lighting | Provide HVAC for heat load | NEC 110.26 |
| BAS Wiring | Provide power and conduit | Provide control devices | ASHRAE 135 |

### 8.3 Electrical ↔ Plumbing Coordination
| Item | Electrical | Plumbing | Notes |
|------|-----------|----------|-------|
| Water Heater | Size circuits, provide disconnect | Size heater, provide piping | NEC 422 |
| Equipment Power | Circuits for pumps, heaters | Nameplate data | NEC 430 |
| Floor Drains | GFI protection near drains | Drains under equipment | NEC 210.8 |
| Fixture Locations | Lighting and receptacles | Fixture rough-in locations | Coordinate early |

### 8.4 Mechanical ↔ Plumbing Coordination
| Item | Mechanical | Plumbing | Notes |
|------|-----------|----------|-------|
| Condensate Drains | Provide drain connection points | Route drains to sanitary/storm | IMC, IPC |
| Domestic Hot Water | May provide air-to-water heat pump | Provide DHW distribution | Coordinate system type |
| Equipment Rooms | Equipment layout | Water/drain piping to equipment | Access and clearances |
| Vent Terminations | Combustion air/flue vents | Plumbing vents | Coordinate roof penetrations |

### 8.5 Fire Protection ↔ All MEP Coordination
| Item | Fire Protection | Electrical | Mechanical | Plumbing |
|------|----------------|-----------|-----------|----------|
| Water Supply | Sprinkler system demand | N/A | N/A | Verify adequate supply |
| Fire Alarm Interface | N/A | Flow/tamper switches | Duct smoke detectors | N/A |
| Sprinkler Coverage | Head layout | Verify lighting clearance | Verify duct clearance | N/A |
| Fire Pump | Power demand | Size circuits (NEC 695) | N/A | Water supply to pump |

---

## 9. Drawing Numbering Standards by Discipline

### 9.1 Standard Sheet Numbering Convention
```
[DISCIPLINE] - [SERIES] [NUMBER]
```
**Example:** E-201 = Electrical, Lighting Series, Sheet 01

### 9.2 Discipline Prefixes
| Prefix | Discipline | Color Code (Optional) |
|--------|-----------|----------------------|
| A | Architecture | Black |
| S | Structural | Red |
| C | Civil | Brown |
| E | Electrical | Blue |
| M | Mechanical | Green |
| P | Plumbing | Yellow |
| FP or F | Fire Protection | Orange |
| L | Landscape | Light Green |

### 9.3 Series Numbering by Discipline
| Series | Sheet Range | Typical Content |
|--------|------------|----------------|
| 000-099 | General | Symbols, legends, notes, site plans |
| 100-199 | Plans 1 | Floor plans (Arch), Power plans (Elec), HVAC plans (Mech), Domestic water plans (Plumb) |
| 200-299 | Plans 2 | RCPs (Arch), Lighting plans (Elec), Piping plans (Mech), Sanitary plans (Plumb) |
| 300-399 | Plans 3 | Elevations (Arch), Fire alarm plans (Elec), Control diagrams (Mech), Storm plans (Plumb) |
| 400-499 | Diagrams | Sections (Arch), One-lines (Elec), Risers (Mech/Plumb/FP) |
| 500-599 | Details | Construction details, typical details |
| 600-699 | Schedules | Equipment schedules, panel schedules, fixture schedules |

---

## 10. Project Phases and Drawing Status

### 10.1 Design Phases
| Phase | Description | Typical Completeness | Drawing Stamp |
|-------|-------------|---------------------|---------------|
| **SD** | Schematic Design | 15-30% | SCHEMATIC DESIGN |
| **DD** | Design Development | 50-65% | DESIGN DEVELOPMENT |
| **CD** | Construction Documents | 90-100% | CONSTRUCTION DOCUMENTS |
| **BID** | Bidding/Permit | 100% | FOR BIDDING / FOR PERMIT |
| **ASB** | Addenda/Supplemental Bulletins | 100% + changes | ADDENDUM #X |
| **RECORD** | Record Drawings (As-Builts) | Post-construction | RECORD DRAWINGS |

### 10.2 Drawing Status Codes
| Code | Status | Description |
|------|--------|-------------|
| **PRELIMINARY** | Pre-SD | Conceptual layouts, not for construction |
| **NOT FOR CONSTRUCTION** | SD/DD | Design in progress |
| **FOR REVIEW** | Any phase | Submitted for review/comment |
| **FOR PERMIT** | CD | Submitted to AHJ for permit |
| **FOR BIDDING** | CD | Issued to contractors for bidding |
| **FOR CONSTRUCTION** | CD | Approved for construction |
| **ISSUED FOR RECORD** | Post-construction | As-built conditions |

---

## 11. Coordination Meeting Agenda by Discipline

### 11.1 Typical MEP Coordination Topics
1. **Equipment Locations and Clearances**
   - Rooftop equipment coordination with structural capacity
   - Electrical/mechanical room layouts
   - Access and maintenance clearances

2. **Vertical Coordination**
   - Shaft sizes for risers (electrical, plumbing, FP, HVAC)
   - Duct/pipe routing through floor penetrations
   - Structural beam depth vs. required ceiling height

3. **Horizontal Coordination**
   - Corridor ceiling coordination (ducts, pipes, lights, sprinklers)
   - Utility room coordination (panel locations, equipment access)
   - Ceiling-mounted device coordination (diffusers, lights, sprinklers, smoke detectors)

4. **Interface Coordination**
   - Electrical power to mechanical equipment
   - Condensate drains from HVAC to plumbing
   - Fire alarm integration with mechanical smoke control
   - BAS integration with electrical lighting controls

5. **Code Compliance Verification**
   - NEC working clearances for electrical panels
   - NFPA 13 sprinkler coverage verification
   - IMC duct clearances from combustibles
   - ADA accessibility for fixtures and controls

---

## 12. Discipline-Specific Calculation Requirements

### 12.1 Electrical Calculations
- **Load Calculations:** NEC Article 220 (dwelling unit, commercial, industrial)
- **Voltage Drop:** NEC 210.19, 215.2 (3% branch circuit, 5% total max)
- **Short Circuit/Coordination:** OCPD sizing and coordination
- **Lighting Power Density:** ASHRAE 90.1, IECC (watts per sqft)
- **Fault Current:** Available fault current at equipment

### 12.2 Mechanical Calculations
- **Heating/Cooling Load:** ASHRAE Handbook - Fundamentals
- **Duct Sizing:** Equal friction method, static regain method
- **Airflow Balancing:** Terminal device CFM vs. design CFM
- **Ventilation:** ASHRAE 62.1 (outdoor air requirements)
- **Energy Modeling:** ASHRAE 90.1 Appendix G

### 12.3 Plumbing Calculations
- **Water Supply Sizing:** IPC Table 610.3, fixture unit method
- **Drain/Vent Sizing:** IPC Table 703.2, fixture unit method
- **Hot Water Demand:** Storage capacity and recovery rate
- **Storm Drainage:** Rainfall intensity, roof area drainage
- **Water Pressure:** Residual pressure at fixtures

### 12.4 Fire Protection Calculations
- **Sprinkler Hydraulics:** Hazen-Williams formula, NFPA 13
- **Water Supply Analysis:** Flow test, system demand curve
- **Standpipe Pressure:** NFPA 14, residual pressure at hose valve
- **Fire Pump Sizing:** NFPA 20, rated flow and pressure

---

## 13. Quality Assurance Checkpoints by Discipline

### 13.1 Electrical QA Checklist
- [ ] Panel locations comply with NEC 110.26 working clearances
- [ ] Circuit breaker totals match panel schedule
- [ ] Voltage drop calculations provided for long runs
- [ ] GFCI/AFCI protection in required locations (NEC 210.8, 210.12)
- [ ] Emergency lighting coverage meets IBC 1008
- [ ] Exit signs at all egress doors (IBC 1013)
- [ ] Fire alarm device spacing meets NFPA 72

### 13.2 Mechanical QA Checklist
- [ ] Equipment schedules match plan layouts
- [ ] Duct sizing calculations provided
- [ ] Outdoor air calculations meet ASHRAE 62.1
- [ ] Energy compliance (ASHRAE 90.1, IECC) documented
- [ ] Equipment clearances for access/maintenance
- [ ] Duct smoke detectors in required locations (IMC 606)

### 13.3 Plumbing QA Checklist
- [ ] Fixture unit calculations for water supply sizing
- [ ] Fixture unit calculations for drain/vent sizing
- [ ] Water heater recovery rate adequate for demand
- [ ] Backflow prevention devices in required locations
- [ ] ADA fixture mounting heights and clearances
- [ ] Floor drains under mechanical equipment

### 13.4 Fire Protection QA Checklist
- [ ] Sprinkler head spacing meets NFPA 13 (max 15' typical)
- [ ] Hydraulic calculations provided and stamped
- [ ] Water supply test data included
- [ ] FDC locations accessible to fire department
- [ ] Fire pump electrical sizing meets NEC 695
- [ ] Sprinkler coverage for obstructions verified

---

## 14. Interdisciplinary Dependencies

### 14.1 Design Sequence Dependencies
```
Architecture (Floor Plans)
  ↓
Structural (Framing Plan)
  ↓
Mechanical (Equipment Sizing & Layout)
  ↓
Electrical (Panel Sizing & Lighting Layout)
  ↓
Plumbing (Fixture & Pipe Routing)
  ↓
Fire Protection (Sprinkler Layout)
  ↓
BIM Coordination (Clash Detection)
  ↓
Final Construction Documents
```

### 14.2 Information Exchange Requirements
| From | To | Information Needed | Phase |
|------|----|--------------------|-------|
| Architect | All MEP | Floor plans, RCPs, sections | SD |
| Structural | All MEP | Beam locations, depths, floor elevations | DD |
| Mechanical | Electrical | Equipment nameplate data (FLA, MCA, MOP) | DD |
| Mechanical | Plumbing | Condensate drain locations | DD |
| Electrical | Fire Alarm | Duct locations for smoke detectors | DD |
| Plumbing | Fire Protection | Water service size and pressure | DD |
| All MEP | Architect | Equipment sizes, clearances, penetrations | DD/CD |

---

## 15. Conclusion

This taxonomy provides a structured classification system for MEP disciplines, enabling:
- **Automated Drawing Validation:** Rules-based QA/QC for discipline-specific requirements
- **Coordination Automation:** Systematic clash detection and resolution
- **Code Compliance:** Discipline-specific code reference mapping
- **Project Workflows:** Standardized design sequence and information exchange

All MEP design and documentation should follow this taxonomy to ensure consistency, completeness, and code compliance throughout the project lifecycle.
