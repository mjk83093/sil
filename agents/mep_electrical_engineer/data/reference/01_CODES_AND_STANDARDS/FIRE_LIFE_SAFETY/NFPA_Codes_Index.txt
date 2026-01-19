# NFPA Codes Index - Fire Protection and Life Safety Systems

## Document Overview

**Purpose**: Comprehensive reference for NFPA (National Fire Protection Association) codes and standards applicable to MEP fire protection system design, installation, and quality assurance.

**Scope**: Water-based fire suppression, fire alarm systems, fire pumps, standpipe systems, life safety code provisions, and special hazard protection systems.

---

## NFPA Codes Overview

### Primary Codes for MEP Design

| Standard | Title | Primary Focus |
|----------|-------|---------------|
| **NFPA 13** | Installation of Sprinkler Systems | Automatic sprinkler system design and installation |
| **NFPA 13R** | Installation of Sprinkler Systems in Residential Occupancies up to Four Stories | Low-rise residential sprinklers |
| **NFPA 13D** | Installation of Sprinkler Systems in One- and Two-Family Dwellings | Single-family home sprinklers |
| **NFPA 14** | Installation of Standpipe and Hose Systems | Standpipe systems for fire department use |
| **NFPA 20** | Installation of Stationary Pumps for Fire Protection | Fire pump design, installation, testing |
| **NFPA 72** | National Fire Alarm and Signaling Code | Fire alarm systems, notification, mass notification |
| **NFPA 101** | Life Safety Code | Means of egress, fire protection features, occupancy requirements |
| **NFPA 25** | Inspection, Testing, and Maintenance of Water-Based Fire Protection Systems | Ongoing ITM requirements |
| **NFPA 70** | National Electrical Code (NEC) | Electrical installation (see ELECTRICAL/NEC_2023_Index.md) |

---

## NFPA 13 - Installation of Sprinkler Systems

### Purpose and Scope

Comprehensive standard for design and installation of automatic fire sprinkler systems for protection of buildings and structures.

**Latest Edition**: NFPA 13-2022 (2025 edition in development)
**Applicability**: All sprinkler systems except low-rise residential (13R) and single-family (13D)
**Adoptions**: Referenced by IBC, required by building codes and insurers

### Standard Structure

**Chapters**:
1. Administration
2. Referenced Publications
3. Definitions
4. Classification of Occupancies and Commodities
5. System Components and Hardware
6. Types of Systems
7. Water Supply Requirements
8. Underground Piping
9. Hanging, Bracing, and Restraint of System Piping
10. System Acceptance
11. **Plans and Calculations** (critical for design)
12. Hydraulic Calculation Procedures
13. **Density/Area Requirements** (occupancy-based design)
14. Residential Sprinklers
15. Special Designs and Installations
16. Water Spray Fixed Systems
17. Water Mist Fire Protection Systems

### Chapter 4: Occupancy Classification

**Occupancy Hazard Classifications**:

| Classification | Description | Examples |
|---------------|-------------|----------|
| **Light Hazard** | Low combustibility, low fire load | Churches, hospitals, museums, offices, restaurants, schools |
| **Ordinary Hazard Group 1 (OH1)** | Moderate combustibility | Automobile parking, bakeries, electronic plants, laundries |
| **Ordinary Hazard Group 2 (OH2)** | Moderate to high combustibility | Post offices, machine shops, printing plants, stages |
| **Extra Hazard Group 1 (EH1)** | High combustibility | Aircraft hangars, die casting, metal extruding, plywood manufacturing |
| **Extra Hazard Group 2 (EH2)** | High flammability/combustibility | Flammable liquids, foam plastics, solvent cleaning |

**Commodity Classifications** (storage occupancies):
- **Class I-IV**: Non-plastic commodities (I = low combustibility, IV = high)
- **Plastics Groups**: Group A (high hazard), B (moderate), C (low)
- **Cartoned Unexpanded Plastics (CUP)**
- **Cartoned Expanded Plastics (CEP)**

### Chapter 5: System Components

**Sprinkler Types** (5.2):

| Type | Description | Application |
|------|-------------|-------------|
| **Pendent** | Deflector points downward | Standard ceiling installation |
| **Upright** | Deflector points upward | Exposed piping, industrial |
| **Sidewall** | Horizontal spray pattern | Corridors, small rooms |
| **Concealed** | Cover plate hides sprinkler | Finished ceilings (aesthetic) |
| **ESFR (Early Suppression Fast Response)** | Large orifice, fast response | High-piled storage (suppression mode) |
| **Residential** | Special pattern for dwelling units | NFPA 13D/13R applications |

**Temperature Ratings** (Table 5.4.1.2):

| Rating °F (°C) | Color Code | Max Ceiling Temp °F (°C) |
|----------------|-----------|-------------------------|
| 135-170 (57-77) | Uncolored or Black | 100 (38) |
| 175-225 (79-107) | White | 150 (66) |
| 250-300 (121-149) | Blue | 225 (107) |
| 325-375 (163-191) | Red | 300 (149) |
| 400-475 (204-246) | Green | 375 (191) |
| 500-575 (260-302) | Orange | 475 (246) |

**Typical Selection**: 155°F (white) for most applications, 286°F (blue) for high ambient areas (boiler rooms, kitchens)

**Orifice Sizes** (5.2.1):

| Designation | Orifice Diameter | K-factor (US) |
|------------|-----------------|--------------|
| Small Orifice | 3/8 inch | 4.0-4.4 |
| Standard | 1/2 inch | 5.6 |
| Large | 17/32 inch | 8.0 |
| Extra Large | 5/8 inch | 11.0-11.5 |
| ESFR | Various | 14.0-25.2 |

**K-factor**: Flow coefficient relating flow (Q) to pressure (P)
```
Q = K × √P

Where:
Q = Flow rate (gpm)
K = K-factor
P = Pressure (psi)
```

### Chapter 8: Water Supply Requirements

**Water Supply Sources** (8.1):
- Public water mains (most common)
- Fire pumps (boosting public supply or from storage)
- Elevated tanks
- Pressure tanks
- Automatic fire pumps taking suction from below-grade sources

**Water Supply Analysis** (8.2):
- Static pressure (no flow)
- Residual pressure (at test flow rate)
- Flow test data from hydrant tests
- Construct water supply curve on hydraulic calculation graph

**Water Supply Curve**:
```
P_residual = P_static - (Q_test / C)²

Where:
P_residual = Residual pressure at design flow (psi)
P_static = Static pressure (psi)
Q_test = Test flow rate (gpm)
C = Constant from flow test
```

**Duration of Water Supply** (Table 8.2.3):

| Occupancy Hazard | Design Area (ft²) | Duration (minutes) |
|-----------------|------------------|-------------------|
| Light Hazard | 1500-2500 | 30-60 |
| Ordinary Hazard | 1500-4000 | 60-90 |
| Extra Hazard | 2500-5000 | 90-120 |

### Chapter 11: Hydraulic Design Density/Area

**Design Method**: Density/Area curves from Figure 11.2.3.1.1

**Light Hazard**:
- Design density: 0.10 gpm/ft² over 1500-2250 ft²
- Typical for offices, schools, hotels (sleeping areas)

**Ordinary Hazard Group 1**:
- Design density: 0.15 gpm/ft² over 1500 ft² (minimum)
- Curve ranges from 0.10 gpm/ft² @ 4000 ft² to 0.30 gpm/ft² @ 1500 ft²

**Ordinary Hazard Group 2**:
- Design density: 0.20 gpm/ft² over 1500 ft² (minimum)
- Curve ranges from 0.15 gpm/ft² @ 4000 ft² to 0.37 gpm/ft² @ 1500 ft²

**Extra Hazard Group 1**:
- Design density: 0.30 gpm/ft² over 2500 ft² (minimum)
- Curve ranges from 0.20 gpm/ft² @ 5000 ft² to 0.43 gpm/ft² @ 2500 ft²

**Extra Hazard Group 2**:
- Design density: 0.40 gpm/ft² over 2500 ft² (minimum)
- Curve ranges from 0.25 gpm/ft² @ 5000 ft² to 0.55 gpm/ft² @ 2500 ft²

**Hose Stream Allowance** (Table 11.2.3.1.2):

| Occupancy Hazard | Inside Hose (gpm) | Outside Hose (gpm) | Combined (gpm) |
|-----------------|------------------|-------------------|---------------|
| Light Hazard (0-20,000 ft²) | 0-50 | 100-250 | 100-250 |
| Ordinary Hazard | 0-50 | 250-500 | 250-500 |
| Extra Hazard | 50 | 500 | 500-550 |

**Design Calculation Example**:

**Ordinary Hazard Group 2 Office Building**:
- Occupancy: OH2
- Design density: 0.20 gpm/ft²
- Design area: 1500 ft²
- Sprinkler demand: 0.20 × 1500 = 300 gpm at most remote sprinkler
- Hose stream: 250 gpm
- **Total system demand**: 300 + 250 = 550 gpm
- Duration: 60 minutes
- Required water storage: 550 gpm × 60 min = 33,000 gallons

### Chapter 12: Hydraulic Calculation Procedures

**Tree System Calculation**:
1. Identify most hydraulically remote sprinkler
2. Calculate pressure loss from each sprinkler to branch line
3. Calculate branch line friction losses
4. Calculate cross-main and riser friction losses
5. Add static pressure changes for elevation
6. Determine system demand curve (flow vs. pressure)
7. Compare to water supply curve (must be below/right of supply)

**Hazen-Williams Formula** (friction loss):
```
P_f = (4.52 × Q^1.85) / (C^1.85 × d^4.87)

Where:
P_f = Friction loss (psi per foot)
Q = Flow rate (gpm)
C = Hazen-Williams coefficient
d = Internal diameter (inches)
```

**Hazen-Williams C-factors** (Table 11.2.3.2.4):
- Steel pipe (dry, pre-action, deluge): C = 100
- Steel pipe (wet system, 10+ years old): C = 100
- Steel pipe (wet system, new): C = 120
- Copper tube: C = 150
- CPVC plastic: C = 150

**Velocity Limitations** (12.3.1.5):
- Underground pipe: no limit specified
- Aboveground pipe: practical limit ~15-20 fps (noise, erosion)
- For high-rise buildings: consider 10 fps to reduce pressure loss

### Chapter 9: Seismic Bracing and Restraint

**Seismic Design Categories** (SDC A-F per ASCE 7):
- SDC A, B, C: Limited seismic requirements
- SDC D, E, F: Full seismic bracing required

**Bracing Requirements** (9.3):
- Longitudinal bracing: resist horizontal forces parallel to pipe
- Lateral bracing: resist horizontal forces perpendicular to pipe
- Four-way bracing: combination of longitudinal and lateral
- Vertical restraint: prevent upward pipe movement

**Maximum Spacing** (Table 9.3.5.4):

| Pipe Size | Spacing (feet) |
|-----------|---------------|
| ≤3 inches | 40 |
| 4 inches | 50 |
| 5 inches | 60 |
| 6 inches | 80 |
| 8+ inches | Piping length / # of braces + 1 |

**Bracing at Changes in Direction**:
- Elbows, tees, and crosses require four-way bracing
- Within 24 inches of change in direction

### Design Application

**NFPA 13 Design Checklist**:
- [ ] Occupancy classification determined (Light, OH1, OH2, EH1, EH2)
- [ ] Design density and area selected from Figure 11.2.3.1.1
- [ ] Sprinkler type and temperature rating appropriate
- [ ] Hydraulic calculations performed (tree system or grid)
- [ ] Water supply adequate for system demand + hose stream
- [ ] Duration requirements met
- [ ] Seismic bracing designed per SDC
- [ ] Spacing requirements met (coverage area per sprinkler)
- [ ] Clearance to storage maintained (18-36 inches typical)
- [ ] Plans and calculations submitted for approval

**MEP Coordination**:
- Architectural: reflected ceiling plans, sprinkler locations coordinated with lights, diffusers
- Structural: seismic bracing attachment points, load capacity verification
- Electrical: fire pump electrical service per NFPA 20 and NEC Article 695
- Plumbing: domestic water separation, backflow prevention, drain locations

---

## NFPA 14 - Installation of Standpipe and Hose Systems

### Purpose and Scope

Requirements for installation of standpipe and hose systems for fire department and building occupant use.

**Latest Edition**: NFPA 14-2022
**Applicability**: Buildings requiring standpipes per building codes (typically >30 feet in height or underground)
**Coordination**: NFPA 13 sprinkler systems often combined with NFPA 14 standpipes

### Standard Structure

**Chapters**:
1-3. Administration, Referenced Publications, Definitions
4. **General Requirements**
5. **System Types and Components**
6. Design and Installation
7. Water Supply
8. Testing

### Chapter 5: System Types

**Class of Service** (5.3):

| Class | Occupant Use | Fire Department Use | Hose Valve Type |
|-------|-------------|-------------------|----------------|
| **Class I** | No | Yes (2.5-inch outlets) | 2.5-inch outlet, fire department hose connection |
| **Class II** | Yes (1.5-inch hose stations) | No | 1.5-inch outlet with rack, hose, and nozzle |
| **Class III** | Yes | Yes | Both 2.5-inch and 1.5-inch outlets |

**Type of System** (5.4):

| Type | Description | Water Supply |
|------|-------------|-------------|
| **Automatic-Wet** | Piping filled with water, connected to water supply | Immediate water available |
| **Automatic-Dry** | Piping filled with air/nitrogen, connected to water supply | Water enters when valve opens |
| **Semiautomatic-Dry** | Piping filled with air/nitrogen, manual activation | Requires manual action at valve |
| **Manual-Dry** | Piping normally dry, no permanent water supply | Fire department pumps in water |
| **Manual-Wet** | Piping filled with water, no permanent water supply | Fire department augments supply |

**Typical Combinations**:
- High-rise office building: Class I, Automatic-Wet
- Hospital with hose stations: Class III, Automatic-Wet
- Unheated warehouse: Class I, Automatic-Dry
- Underground parking garage: Class I, Automatic-Wet

### Chapter 6: Design Requirements

**Hose Outlet Location** (6.2.2):
- Exit stairways (enclosed stairs)
- Horizontal exits
- Exit passageways
- Every floor (including below grade)
- On roof if flat and accessible

**Hose Valve Spacing** (6.2.4):
- Maximum 200 feet of hose travel (Class I)
- All portions of building within 130 feet of Class II hose station

**Pipe Sizing** (6.3.1):

| Standpipe Class | Minimum Size |
|----------------|--------------|
| Class I (combined system) | 6 inches (risers), 4 inches (floor outlets) |
| Class I (separate system) | 4 inches (risers and outlets) |
| Class II | 2 inches (for 1 hose, up to 3 floors) |
| Class III | Same as Class I |

### Chapter 7: Water Supply Requirements

**Flow and Pressure Requirements** (Table 7.3.1.1.1):

| Standpipe Class | Minimum Flow (gpm) | Minimum Pressure (psi at outlet) | Number of Outlets Calculated Simultaneously |
|----------------|-------------------|------------------------------|-------------------------------------------|
| **Class I (Manual)** | 500 per outlet | 65 | See building height* |
| **Class I (Automatic)** | 500 per outlet | 100 at topmost outlet | See building height* |
| **Class II** | 100 per outlet | 65 | 1 (most remote) |
| **Class III (Manual)** | 500 per outlet | 65 | See building height* |
| **Class III (Automatic)** | 500 per outlet | 100 at topmost outlet | See building height* |

**Number of Outlets Calculated** (based on building height above grade):
- 1-75 feet: 1 outlet (500 gpm)
- 76-200 feet: 2 outlets (1000 gpm)
- 201-300 feet: 3 outlets (1500 gpm)
- 301-400 feet: 4 outlets (2000 gpm)
- >400 feet: Special design required

**Duration of Water Supply** (7.10):
- 30 minutes minimum
- Example: 2-outlet system = 1000 gpm × 30 min = 30,000 gallons

### Design Application

**NFPA 14 Design Checklist**:
- [ ] Standpipe class determined (I, II, or III)
- [ ] Standpipe type determined (automatic-wet, manual-dry, etc.)
- [ ] Hose valve locations identified (stairwells, exits)
- [ ] Pipe sizing per minimum requirements
- [ ] Water supply demand calculated (flow + pressure at topmost outlet)
- [ ] Duration requirement met (30 minutes)
- [ ] Fire department connections located and sized
- [ ] Roof outlet provided (if flat, accessible roof)
- [ ] Pressure-reducing valves where static pressure >175 psi
- [ ] Hydraulic calculations performed for automatic systems

**Combined Sprinkler/Standpipe Systems**:
- Sprinkler demand per NFPA 13
- Standpipe demand per NFPA 14
- If combined: use greater of individual demands, not additive (typically)
- Exception: Some jurisdictions require additive demands

**MEP Coordination**:
- Architectural: standpipe cabinets in stairwells, roof access
- Structural: riser penetrations, seismic bracing attachments
- Electrical: fire pump for water supply (if required)
- Fire Alarm: supervisory and alarm signals from standpipe system

---

## NFPA 20 - Installation of Stationary Pumps for Fire Protection

### Purpose and Scope

Requirements for selection and installation of stationary fire pumps used in fire protection systems.

**Latest Edition**: NFPA 20-2022
**Applicability**: All fire pumps (sprinkler, standpipe, combined systems)
**Coordination**: NFPA 13, NFPA 14 (system demand), NEC Article 695 (electrical)

### Standard Structure

**Chapters**:
1-3. Administration, Referenced Publications, Definitions
4. **General Requirements**
5. **Centrifugal Fire Pumps**
6. Positive Displacement Fire Pumps
7. System Components
8. Drivers
9. Controllers, Power Wiring, and Transferring
10. Pressure Maintenance (Jockey) Pumps
11. **Acceptance Tests**

### Chapter 5: Centrifugal Fire Pump Selection

**Fire Pump Types**:
- **Horizontal split case**: Most common, easy maintenance
- **Vertical inline**: Space-constrained installations
- **Vertical turbine**: Below-grade water sources (tanks, reservoirs)
- **End suction**: Small capacity applications (<500 gpm)

**Pump Performance Curve** (5.2.4):
- **Rated capacity**: 100% of nameplate flow
- **150% flow point**: Maximum flow, pressure drops to 65% of rated
- **Churn (shutoff) pressure**: Zero flow, maximum pressure (140% of rated typical)

**Standard Rated Capacities** (Table 5.2.4.1):
- 25, 50, 100, 150, 200, 250, 300, 400, 450, 500, 750, 1000, 1250, 1500, 2000, 2500, 3000, 4000, 5000 gpm

**Pressure Ranges**:
- Low pressure: up to 100 psi
- Medium pressure: 101-200 psi
- High pressure: 201-300 psi

**Pump Selection Procedure**:
1. Determine system demand (NFPA 13 + NFPA 14)
2. Add safety margin: typically 105% of system demand
3. Select standard capacity ≥ required flow
4. Determine required pressure at pump discharge (hydraulic calculation)
5. Verify suction supply adequate (net positive suction head)

### Chapter 7: Suction and Discharge Piping

**Suction Piping** (7.2):
- Size: ≥ pump suction flange (typically 6-12 inches for large pumps)
- Eccentric reducer at pump suction (flat side up)
- No valves except listed indicating control valve
- Suction screen if open water source
- Minimum pressure: 0 psi (gauge) at pump churn conditions

**Discharge Piping** (7.3):
- Listed indicating control valve (OS&Y gate valve typical)
- Check valve (in-line or swing check)
- Listed pressure relief valve (if churn >175 psi)
- Test header with flowmeter and pressure gauge
- Fire department connection (FDC) downstream of check valve

**Piping Arrangement** (Figure 7.3.1.4):
```
[Fire Pump] → [Check Valve] → [OS&Y Valve] → [Relief Valve (if req'd)] → [System]
                    ↓
              [Test Header]
              [FDC Connection]
```

### Chapter 8: Drivers

**Electric Motor Drivers** (8.3):
- Standard motors rated for fire pump service (NEMA Design B)
- Service factor: 1.15 minimum
- Locked rotor code: J or higher
- Continuous duty at 150% of pump nameplate flow

**Diesel Engine Drivers** (8.4):
- Used where reliable electric power not available
- Engine rated for continuous duty at 150% pump capacity
- Fuel tank: 1 gallon per hp + 5%, or 8-hour run time at 100%
- Battery system for engine starting
- Automatic and manual start capability
- Cooling system (radiator or heat exchanger)

### Chapter 9: Controllers and Power Wiring

**Electric Motor Controller** (9.2):
- Listed fire pump controller
- Automatic start on pressure drop
- Manual stop only (no automatic stop)
- Phase reversal protection (3-phase motors)
- Integral disconnect means

**Power Supply** (9.6):
- **Reliable source required**: Utility service ahead of main disconnect
- Separate service or connection ahead of main
- **No overcurrent protection** except at utility transformer or generator
- Dedicated to fire pump (no other loads)
- Supervised for integrity

**Emergency Generator** (9.6.4):
- If normal power unreliable, emergency generator required
- Generator sized for fire pump locked rotor starting + other loads
- Automatic transfer switch
- Generator on standby power, not emergency power (no 10-second transfer limit)

### Chapter 11: Acceptance Testing

**Flow Test Requirements** (11.3):
- Test at 150% of rated capacity (maximum flow point)
- Record pressure and flow at rated capacity (100%)
- Verify churn pressure (shutoff, 0% flow)
- Plot pump performance curve, compare to manufacturer's curve
- Test duration: 1 hour at 100% flow minimum

**Test Setup**:
- Discharge to test header (with flowmeter)
- Pressure gauges at pump suction and discharge
- Measure ambient temperature, barometric pressure (for NPSH)
- Record electrical parameters (voltage, current, power)

**Acceptance Criteria** (11.5):
- Pump flow within 95-105% of rated flow at rated pressure
- Pump churn pressure: 100-140% of rated pressure
- Net pressure rise at 150% flow: ≥ 65% of rated net pressure

**Annual Testing** (per NFPA 25):
- Churn test (no flow)
- Rated capacity test (100% flow)
- Peak load test (150% flow)
- Full acceptance test every 3 years or after major repairs

### Design Application

**NFPA 20 Design Checklist**:
- [ ] System demand calculated (sprinkler + standpipe)
- [ ] Fire pump capacity selected (standard size ≥105% demand)
- [ ] Fire pump pressure rating adequate for system
- [ ] Suction supply verified (public main, storage tank, etc.)
- [ ] Driver type selected (electric motor or diesel engine)
- [ ] Power supply coordination with electrical engineer
- [ ] Fire pump room requirements met (size, access, drainage)
- [ ] Suction and discharge piping sized and arranged per standard
- [ ] Test header and FDC locations coordinated
- [ ] Acceptance test procedures included in specifications

**Fire Pump Room Requirements**:
- Dedicated room (no other equipment except fire protection)
- Adequate clearances for maintenance (36 inches minimum)
- Drainage (floor drain or sump)
- Ventilation (for diesel engine: combustion air and cooling)
- Lighting and electrical outlets
- Heating if subject to freezing
- Fire-resistant construction (per IBC Chapter 9)

**MEP Coordination**:
- Electrical: dedicated power supply per NEC 695, emergency generator sizing
- Plumbing: domestic water separation, suction piping from source
- Structural: equipment loads, seismic bracing
- Fire alarm: supervisory (running, failure, power loss) and alarm signals

---

## NFPA 72 - National Fire Alarm and Signaling Code

### Purpose and Scope

Requirements for design, installation, and testing of fire alarm systems and emergency communications systems.

**Latest Edition**: NFPA 72-2022
**Applicability**: All fire alarm systems in buildings and structures
**Coordination**: IBC Chapter 9, NFPA 101 (required locations), NFPA 13 (sprinkler system interfaces)

### Standard Structure

**Chapters**:
1-3. Administration, Referenced Publications, Definitions
10. Fundamentals
12. **Circuits and Pathways**
14. **Inspection, Testing, and Maintenance**
17. **Initiating Devices**
18. **Notification Appliances**
21. Emergency Control Functions
23. Protected Premises Fire Alarm Systems
24. Emergency Communications Systems
26. Supervising Station Fire Alarm Systems
27. Public Emergency Alarm Reporting Systems
29. Single- and Multiple-Station Alarms and Household Fire Alarm Systems

### Chapter 17: Initiating Devices

**Device Types**:

| Device | Function | Typical Application |
|--------|----------|-------------------|
| **Manual Pull Station** | Manual alarm initiation | Exits, egress paths (required by codes) |
| **Smoke Detector (Spot)** | Senses smoke particles | Corridors, rooms, return air |
| **Smoke Detector (Duct)** | Smoke in HVAC ductwork | Air handlers, return/supply ducts |
| **Heat Detector (Fixed Temp)** | Activates at set temperature | Kitchens, mechanical rooms, warehouses |
| **Heat Detector (ROR)** | Senses rapid temperature rise | General coverage |
| **Flame Detector** | Detects UV/IR from flames | Industrial, high-ceiling areas |
| **Waterflow Switch** | Sprinkler water flow alarm | Sprinkler system risers, floor control valves |
| **Valve Supervisory Switch** | Monitors valve position | Sprinkler control valves |
| **Pressure Switch** | Monitors system pressure | Dry pipe, pre-action systems |

**Smoke Detector Spacing** (Table 17.7.3.2.3.1):

| Ceiling Height | Smooth Ceiling Spacing | Beam Spacing |
|---------------|----------------------|-------------|
| 0-10 feet | 30 feet | 30 feet |
| 10-15 feet | 30 feet | 30 feet |
| 15-20 feet | 30 feet | 25 feet |
| 20-25 feet | 30 feet | 20 feet |
| 25-30 feet | 30 feet | 15 feet |
| >30 feet | Engineering analysis | Engineering analysis |

**Coverage Area**: 900 ft² per detector (30 ft × 30 ft) typical

**Heat Detector Spacing** (Table 17.7.3.2.3.2):

Varies by temperature rating and ceiling height:
- **Fixed temperature (135°F-170°F)**: 50-70 feet spacing, depending on height
- **Rate-of-rise (ROR)**: Similar to fixed temperature
- Coverage area: up to 4900 ft² per detector (70 ft × 70 ft)

**Manual Pull Station Placement** (17.15):
- Within 5 feet of each exit doorway
- Maximum travel distance: 200 feet
- Mounted 42-48 inches above floor (ADA compliant)
- Clearly visible and accessible

### Chapter 18: Notification Appliances

**Audible Notification Appliances** (18.4):

**Sound Pressure Level Requirements**:
- **Public mode** (general evacuation): 75 dBA minimum, 110 dBA maximum
- **Private mode** (fire service only): 65 dBA minimum, 110 dBA maximum
- Measured 5 feet above floor in occupied areas

**Sound Level above Ambient**:
- 15 dB above average ambient sound level
- 5 dB above maximum ambient sound level (60-second duration)

**Sleeping Areas** (18.4.5):
- 75 dBA at pillow level, or
- 15 dB above average ambient (whichever is greater)
- Low-frequency alarms (520 Hz) for deep sleep wake-up

**Audible Coverage**:
- Continuous sound path
- No areas >55 dBA from nearest appliance
- Typical appliance spacing: 50-100 feet in corridors

**Visible Notification Appliances (Strobes)** (18.5):

**Light Intensity** (Table 18.5.5.4.1):

| Room Size (ft²) | Minimum Intensity (candela) | Maximum Room Size |
|----------------|---------------------------|-----------------|
| ≤200 | 15 cd | 20 × 20 ft |
| 201-400 | 30 cd | 28 × 28 ft |
| 401-500 | 60 cd | 40 × 40 ft |
| 501-1000 | 75 cd | 45 × 45 ft |
| 1001-1600 | 95 cd | 54 × 54 ft |
| >1600 | 110 cd | 60 × 60 ft |

**Strobe Flash Rate**: 1-2 Hz (flashes per second)
**Strobe Mounting Height**: 80-96 inches above floor (centerline)

**Corridor Spacing** (18.5.5.3):
- 15 cd strobes: Maximum 100-foot spacing (if one wall mount)
- 30 cd strobes: Maximum 130-foot spacing
- Higher intensities for longer corridors

**Synchronization** (18.5.10):
- All visible appliances on same notification zone shall be synchronized
- Prevents disorientation from multiple unsynchronized flashes

### Chapter 23: Protected Premises Fire Alarm Systems

**System Types**:

| Type | Description | Typical Application |
|------|-------------|-------------------|
| **Manual** | Manual pull stations only | Small, simple buildings |
| **Automatic** | Automatic detection (smoke, heat, waterflow) | Most commercial buildings |
| **Manual and Automatic** | Both manual and automatic initiation | Standard design |
| **Voice Evacuation** | Two-way voice communication + tones | High-rise, large assembly, schools |

**Signaling Line Circuits (SLC)** (12.4):
- Class A (Style 4): Redundant pathway, survives single fault
- Class B (Style 4): Single pathway, non-redundant
- Class A required in most high-rise and critical facilities

**Notification Appliance Circuits (NAC)** (12.5):
- Class A: Redundant pathway
- Class B: Single pathway
- Class A typical for large systems, high-rise

### Chapter 24: Emergency Communications Systems

**Mass Notification Systems (MNS)** (24.4):
- Wide-area coverage (campus, city)
- Combination indoor/outdoor
- High-power speaker arrays
- Integration with voice evacuation

**In-Building Mass Notification (IBMN)** (24.5):
- Voice messages for emergencies other than fire
- Integration with fire alarm voice evacuation
- Active shooter, severe weather, hazmat warnings

**Two-Way Emergency Communications** (24.6):
- Fire fighter telephone system (high-rise)
- Area of refuge communications (ADA)
- Elevator emergency phones

### Chapter 14: Inspection, Testing, and Maintenance

**Testing Frequencies** (Table 14.3.1):

| Component | Inspection | Testing |
|-----------|-----------|---------|
| Control panel | Annually | Annually |
| Smoke detectors | Semi-annually | Annually (sensitivity test every 2 years) |
| Heat detectors | Annually | Annually |
| Manual pull stations | Annually | Annually |
| Notification appliances | Annually | Annually |
| Battery (primary) | Annually | Annually (load test) |
| Battery (secondary) | Monthly (visual) | Semi-annually (load test) |
| Waterflow devices | Quarterly | Annually |
| Valve supervisory | Quarterly | Annually |

**Acceptance Testing** (Chapter 14.2.3):
- 100% device testing before system turned over
- Verification of all circuits, zones, notification appliances
- Interface testing (elevator recall, door release, HVAC, etc.)
- Battery backup capacity test (24-hour standby + 5 minutes alarm)

### Design Application

**NFPA 72 Design Checklist**:
- [ ] Initiating device locations determined (smoke, heat, manual pull stations)
- [ ] Notification appliance locations determined (speakers, strobes)
- [ ] Coverage calculations performed (audible, visible)
- [ ] Circuit class determined (Class A or B for SLC/NAC)
- [ ] Interfaces identified (HVAC, elevators, doors, access control)
- [ ] Voice evacuation required determination
- [ ] Emergency communications systems required (MNS, IBMN)
- [ ] Power supply and battery backup calculations
- [ ] Riser diagram and floor plans prepared
- [ ] Sequence of operations documented
- [ ] Testing and acceptance procedures specified

**Typical Device Counts** (10,000 ft² floor):
- Smoke detectors (corridors): ~12-15 devices
- Smoke detectors (rooms): Varies by room layout
- Manual pull stations: 2-4 per floor (at exits)
- Strobes: ~8-12 per floor (depending on room sizes)
- Speakers: ~6-10 per floor (for voice evacuation)

**MEP Coordination**:
- Electrical: dedicated circuits, conduit pathways, panel locations
- HVAC: duct smoke detectors, fan shutdown sequences, smoke control activation
- Elevators: recall function, firefighter service, elevator machine room detection
- Security: access control integration, lockdown functions
- Architectural: device locations coordinated with ceilings, walls, finishes

---

## NFPA 101 - Life Safety Code

### Purpose and Scope

Minimum requirements for life safety from fire and similar emergencies in new and existing buildings.

**Latest Edition**: NFPA 101-2021 (2024 edition released)
**Applicability**: All occupancies, new and existing buildings
**Coordination**: Building codes (IBC) reference NFPA 101 provisions

### Standard Structure

**Chapters**:
1-4. Administration, Referenced Publications, Definitions, General
6-42. Occupancy-specific requirements (Assembly, Educational, Healthcare, Residential, etc.)
43. Building Rehabilitation

### Chapter 7: Means of Egress

**Means of Egress Components**:
1. **Exit access**: Portion of egress path from any point to exit
2. **Exit**: Separated, protected path to exit discharge (stairs, exit passageways)
3. **Exit discharge**: Portion from exit to public way

**Exit Capacity** (7.3.3):

**Stairs**:
- Level exit components: 0.2 inches per person
- Stairways (new buildings): 0.3 inches per person
- Stairways (existing): 0.2 inches per person

**Example**: 500-person occupant load, new stairway
```
Required stair width = 500 persons × 0.3 inches/person = 150 inches
Number of 44-inch stairs = 150 / 44 = 3.4 → 4 stairs required (minimum 2 per code)
```

**Doors**:
- Level exit components: 0.2 inches per person
- Minimum clear width: 32 inches (typically 36-inch door)

**Number of Exits** (Table 7.4.1.2):

| Occupant Load | Minimum Number of Exits |
|--------------|----------------------|
| 1-500 | 2 |
| 501-1000 | 3 |
| >1000 | 4 |

**Travel Distance** (Table 7.6):

| Occupancy | Unsprinklered | Sprinklered |
|-----------|--------------|------------|
| Assembly | 200 feet | 250 feet |
| Business | 200 feet | 300 feet |
| Educational | 200 feet | 250 feet |
| Industrial | 200 feet | 250-400 feet |
| Residential (hotels) | 200 feet | 250 feet |
| Storage | 200 feet | 400 feet |

### Chapter 9: Building Service and Fire Protection Equipment

**Automatic Sprinkler Requirements** (9.7):
- Requirements vary by occupancy chapter
- Generally required for: high-rise, large area, high hazard, healthcare

**Fire Alarm System Requirements** (9.6):
- Manual fire alarm system: manual pull stations + notification
- Automatic fire alarm: includes automatic detection
- Requirements vary by occupancy chapter

**Emergency Lighting** (7.9):
- Required in designated stairs, aisles, corridors, passageways
- Minimum illumination: 1 foot-candle average, 0.1 fc minimum
- Duration: 1.5 hours minimum
- Transfer time: 10 seconds maximum to emergency power

**Exit Signs** (7.10):
- Required at exits and exit access doors
- Illumination: internally or externally illuminated
- Letter height: ≥6 inches (principal strokes ≥3/4 inch)
- Visibility: 100 feet minimum
- Emergency power: same as emergency lighting

### Occupancy-Specific Chapters

**Chapter 38: Business Occupancies** (typical office example):

**Sprinkler Requirement** (38.3.5):
- High-rise (>75 feet): Required throughout
- Other: Not specifically required by NFPA 101, but often by IBC

**Fire Alarm System** (38.3.4):
- Required if: occupant load >500, or >100 occupants above/below level of exit discharge
- Manual fire alarm system minimum
- Voice evacuation not required (but often provided)

**Exit Requirements**:
- 2 exits minimum per floor
- Travel distance: 200 feet (unsprinklered), 300 feet (sprinklered)
- Corridor width: 44 inches minimum

### Design Application

**NFPA 101 Compliance Checklist**:
- [ ] Occupancy classification determined
- [ ] Occupant load calculated
- [ ] Number of exits verified (2, 3, or 4 minimum)
- [ ] Exit capacity calculated (stairs, doors)
- [ ] Travel distance verified (≤200-300 feet)
- [ ] Emergency lighting provided (1.5 hours, 1 fc average)
- [ ] Exit signs provided and illuminated
- [ ] Fire alarm system required determination
- [ ] Automatic sprinklers required determination
- [ ] Special egress provisions (areas of refuge, horizontal exits)

**MEP Coordination**:
- Electrical: emergency lighting, exit sign circuits, fire alarm power
- Fire Protection: sprinkler and alarm interface with egress requirements
- Architectural: exit widths, travel distances, door hardware

---

## Cross-Reference: NFPA Standards Integration

| Building System | NFPA 13 | NFPA 14 | NFPA 20 | NFPA 72 | NFPA 101 |
|----------------|---------|---------|---------|---------|----------|
| **Automatic Sprinklers** | Design requirements | Combined systems | Fire pump for supply | Waterflow alarm | Required locations |
| **Standpipes** | -- | Design requirements | Fire pump for supply | Supervisory signals | Exit stairway location |
| **Fire Pumps** | Water supply | Water supply | Installation requirements | Running/failure alarm | -- |
| **Fire Alarm** | Waterflow interface | Waterflow interface | Controller supervision | Design requirements | Required locations |
| **Means of Egress** | Sprinkler increase travel distance | Standpipe in exits | -- | Manual pull stations at exits | Design requirements |

---

## Design and QA/QC Application

### Fire Protection Design Checklist

**NFPA 13 Sprinkler System**:
- [ ] Occupancy hazard classification determined
- [ ] Design density and area selected
- [ ] Sprinkler type, temperature rating, K-factor specified
- [ ] Hydraulic calculations performed
- [ ] Water supply verified adequate (flow test data)
- [ ] Seismic bracing designed
- [ ] Spacing and coverage requirements met
- [ ] Plans and calculations submitted to AHJ

**NFPA 14 Standpipe System**:
- [ ] Standpipe class and type determined
- [ ] Hose valve locations identified
- [ ] Pipe sizing adequate
- [ ] Water supply demand calculated
- [ ] Fire department connections located
- [ ] Pressure-reducing valves specified where required
- [ ] Roof outlet provided (if applicable)

**NFPA 20 Fire Pump**:
- [ ] System demand calculated (sprinkler + standpipe)
- [ ] Fire pump capacity and pressure selected
- [ ] Suction supply verified
- [ ] Driver type selected (electric or diesel)
- [ ] Power supply coordinated with electrical engineer
- [ ] Fire pump room requirements met
- [ ] Acceptance test procedures specified

**NFPA 72 Fire Alarm System**:
- [ ] Initiating device locations determined
- [ ] Notification appliance coverage calculated
- [ ] Circuit class determined (Class A or B)
- [ ] Interfaces documented (HVAC, elevators, doors)
- [ ] Voice evacuation system specified (if required)
- [ ] Battery backup calculations performed
- [ ] Testing and acceptance procedures specified

**NFPA 101 Life Safety**:
- [ ] Occupancy classification and load calculated
- [ ] Number and capacity of exits verified
- [ ] Travel distance within limits
- [ ] Emergency lighting and exit signs provided
- [ ] Fire alarm system required determination
- [ ] Automatic sprinklers required determination

---

## Document Control

**Last Updated**: 2025-10-22
**Maintained By**: EE_AI Platform - MEP Library
**Review Cycle**: Triennial (NFPA code cycle)
**Next Review**: 2025 (NFPA 2025 editions)

---

END OF DOCUMENT
