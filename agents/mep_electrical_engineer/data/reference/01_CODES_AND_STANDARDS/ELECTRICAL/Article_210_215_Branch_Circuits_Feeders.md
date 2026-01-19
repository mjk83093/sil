# NEC 2023 Articles 210 & 215 - Branch Circuits and Feeders (DETAILED)

## Document Information

**NEC Articles**: 210 and 215
**Title**: Branch Circuits (210) and Feeders (215)
**Edition**: NFPA 70-2023 National Electrical Code
**Scope**: Requirements for branch circuit and feeder design, sizing, protection, and installation
**Last Updated**: 2025-01-22
**Curator**: EE_AI Platform - MEP Library Curation Team

---

## Table of Contents

1. [Overview and Relationship](#overview-and-relationship)
2. [Article 210 - Branch Circuits](#article-210---branch-circuits)
3. [Article 215 - Feeders](#article-215---feeders)
4. [Design Examples](#design-examples)
5. [Integration with QA/QC Rules](#integration-with-qaqc-rules)
6. [Quick Reference Tables](#quick-reference-tables)

---

## Overview and Relationship

### System Hierarchy

```
Utility Service
      │
      ▼
Service Equipment (Main Disconnect, Main OCPD)
      │
      ├─── FEEDER (Article 215) ───► Subpanel/Panelboard
      │         │
      │         └─── BRANCH CIRCUIT (Article 210) ───► Load (receptacles, lights, appliances)
      │
      └─── BRANCH CIRCUIT (Article 210) ───► Load (directly from service panel)
```

### Definitions

**Branch Circuit (210.2)**: Circuit conductors between final overcurrent device and outlet(s).

**Feeder (Article 100)**: Circuit conductors between service equipment and final branch circuit overcurrent device.

**Key Distinction**:
- **Branch circuits** supply loads directly (receptacles, lights, appliances)
- **Feeders** supply panelboards/distribution equipment (which then supply branch circuits)

---

## Article 210 - Branch Circuits

### Part I - General Provisions (210.1-210.12)

#### 210.1 Scope

Article 210 covers:
- Branch circuit types and classifications
- Branch circuit voltage limitations
- Receptacle, lighting, and appliance branch circuits
- Required branch circuits for dwelling units

#### 210.2 Definitions

**Branch Circuit, Appliance**: Supplies energy to one or more outlets for appliances.

**Branch Circuit, General-Purpose**: Supplies two or more receptacles or outlets for lighting and appliances.

**Branch Circuit, Individual**: Supplies only one utilization equipment.

**Branch Circuit, Multiwire**: Circuit with grounded conductor (neutral) and two or more ungrounded conductors (hots) with voltage between them.

**Example - Multiwire Branch Circuit**:
```
120/240V Panel
   │
   ├─ Phase A (black) ──┐
   ├─ Neutral (white) ───┼─→ Receptacles/lights (shared neutral)
   └─ Phase B (red) ─────┘

Voltage: A-to-N = 120V, B-to-N = 120V, A-to-B = 240V
Advantage: Saves one conductor (shared neutral), balances load
```

#### 210.3 Rating

**Branch circuits rated** per maximum permitted ampere rating of overcurrent device:
- 15A, 20A, 30A, 40A, 50A (most common)
- Greater than 50A permitted for specific loads

#### 210.4 Multiwire Branch Circuits

**(A) General**: Multiwire branch circuits permitted as multiple circuits.

**(B) Disconnecting Means**: All ungrounded conductors shall be simultaneously disconnected at panelboard (use 2-pole breaker or handle ties).

**Reason**: Prevents neutral from being opened while phases remain energized (shock hazard).

**(C) Line-to-Neutral Loads**: Only permitted on circuits with grounded conductor (neutral).

**(D) Grouping**: Ungrounded and grounded conductors of multiwire branch circuit shall be grouped by cable ties or similar means at panelboard (identification).

**Common Violation**:
```
WRONG: Two single-pole breakers (no handle tie) for multiwire branch circuit
  → If one breaker opens, neutral remains common (objectionable current)

CORRECT: Two-pole breaker or single-poles with handle tie
  → Both phases disconnect simultaneously
```

#### 210.5 Identification for Branch Circuits

**(A) Grounded Conductor (Neutral)**:
- White or gray for circuits ≤ 50A
- Continuous white or gray along entire length

**(B) Equipment Grounding Conductor**:
- Green, green with yellow stripe, or bare

**(C) Ungrounded Conductors (Phase/Hot)**:
- Color-coding not required, but recommended:
  - 120/208V: Black (Phase A), Red (Phase B), Blue (Phase C)
  - 277/480V: Brown (Phase A), Orange (Phase B), Yellow (Phase C)

#### 210.6 Branch-Circuit Voltage Limitations

**(A) Occupancy Limitation**:
- Dwelling units: 120V to ground for receptacles and cord-and-plug appliances
- Exception: 208V, 240V permitted for stationary appliances (range, dryer, HVAC)

**(B) 120 Volts Between Conductors**:
- Lighting fixtures in dwelling units: 120V maximum

**(C) 277 Volts to Ground**:
- Commercial/industrial: 277V lighting permitted (fluorescent, LED)
- Requires specific fixtures rated 277V

**(D) 600 Volts Between Conductors**:
- Industrial: Up to 600V for special equipment

**Summary**:
```
┌────────────────────────────────────┬────────────────────────────────┐
│ Application                        │ Maximum Voltage                │
├────────────────────────────────────┼────────────────────────────────┤
│ Dwelling unit receptacles          │ 120V to ground                 │
│ Dwelling unit lighting             │ 120V                           │
│ Commercial receptacles             │ 125V, 250V                     │
│ Commercial lighting (277V fixtures)│ 277V to ground                 │
│ Industrial equipment               │ 600V                           │
└────────────────────────────────────┴────────────────────────────────┘
```

#### 210.8 Ground-Fault Circuit-Interrupter (GFCI) Protection for Personnel

**GFCI required for 125V, 15A and 20A receptacles** in the following locations:

**(A) Dwelling Units**:
1. **Bathrooms** - All receptacles
2. **Garages and accessory buildings** - All receptacles (except dedicated appliances not readily accessible)
3. **Outdoors** - All receptacles
4. **Crawl spaces** - All receptacles at or below grade level
5. **Unfinished portions of basements** - All receptacles (except dedicated appliances)
6. **Kitchens** - All receptacles serving countertop surfaces
7. **Sinks** - Within 6 feet of outside edge of sink (kitchens, wet bars, laundry, etc.)
8. **Bathtubs or shower stalls** - Within 6 feet of outside edge
9. **Laundry areas** - All receptacles within 6 feet of sink

**(B) Other Than Dwelling Units**:
1. **Bathrooms** - All receptacles
2. **Kitchens** - All receptacles
3. **Rooftops** - All receptacles
4. **Outdoors** - All receptacles in public spaces or at grade level
5. **Sinks** - Within 6 feet of outside edge (commercial kitchens, break rooms, etc.)
6. **Indoor wet locations** - All receptacles
7. **Locker rooms with showers** - All receptacles

**GFCI Protection Methods**:
- GFCI receptacle (device-level protection)
- GFCI circuit breaker (circuit-level protection)
- GFCI portable device

**Exceptions**:
- Receptacles not readily accessible (e.g., appliance on ceiling)
- Dedicated appliance receptacles (garage door opener, sump pump)

**Common GFCI Locations Summary**:
```
┌────────────────────────────────────┬─────────────┬─────────────────┐
│ Location                           │ Dwelling    │ Commercial      │
├────────────────────────────────────┼─────────────┼─────────────────┤
│ Bathrooms                          │ All         │ All             │
│ Kitchens (countertop)              │ All         │ All             │
│ Within 6 ft of sinks               │ Required    │ Required        │
│ Outdoors                           │ All         │ Public/grade    │
│ Garages                            │ All*        │ Not required    │
│ Unfinished basements               │ All*        │ Not required    │
│ Crawl spaces                       │ All         │ Not required    │
│ Laundry (within 6 ft of sink)     │ Required    │ Not specified   │
└────────────────────────────────────┴─────────────┴─────────────────┘
* Except dedicated appliances not readily accessible
```

#### 210.11 Branch Circuits Required

**(A) Number of Branch Circuits**: Based on total computed load and branch circuit size (from Article 220).

**(B) Load Evenly Proportioned**: Branch circuits for lighting and receptacles distributed evenly across phases.

**(C) Dwelling Unit** - Required circuits:

**(C)(1) Small-Appliance Branch Circuits**:
- Minimum **two 20A circuits** for small appliances
- Supply kitchen, pantry, dining room, breakfast room receptacle outlets
- Must be 20A circuits (12 AWG minimum)
- No other outlets permitted on these circuits (lighting, etc.)

**(C)(2) Laundry Branch Circuit**:
- Minimum **one 20A circuit** for laundry receptacle(s)
- Must be 20A circuit (12 AWG minimum)
- No other outlets permitted (laundry area only)

**(C)(3) Bathroom Branch Circuit**:
- Minimum **one 20A circuit** for bathroom receptacle(s)
- Must be 20A circuit (12 AWG minimum)
- May supply only receptacles in bathroom(s) (single dwelling unit)
- **OR** supply receptacles and other equipment (lights, fan) if serves only one bathroom

**Summary - Required Dwelling Unit Circuits**:
```
┌────────────────────────────────────┬───────────┬──────────────────┐
│ Circuit Type                       │ Minimum # │ Rating           │
├────────────────────────────────────┼───────────┼──────────────────┤
│ Small appliance (kitchen, etc.)    │ 2         │ 20A              │
│ Laundry                            │ 1         │ 20A              │
│ Bathroom                           │ 1         │ 20A              │
│ General lighting & receptacles     │ Calculated│ 15A or 20A       │
└────────────────────────────────────┴───────────┴──────────────────┘
```

#### 210.12 Arc-Fault Circuit-Interrupter (AFCI) Protection

**AFCI required** for all 120V, 15A and 20A branch circuits supplying outlets in dwelling unit:
- Family rooms, dining rooms, living rooms, parlors, libraries, dens, bedrooms, sunrooms, recreation rooms, closets, hallways, laundry areas, similar rooms or areas

**Exclusions** (AFCI NOT required):
- Bathrooms
- Garages
- Outdoor outlets
- Unfinished basements

**AFCI Protection Methods**:
- Combination AFCI circuit breaker (most common)
- Outlet branch circuit AFCI (first outlet on circuit)

**Purpose**: Detect arc-faults (series arcs in damaged cords, parallel arcs at loose connections) to prevent electrical fires.

---

### Part II - Branch-Circuit Ratings (210.19-210.23)

#### 210.19 Conductors - Minimum Ampacity and Size

**(A) Branch Circuits Not More Than 600 Volts**:

**(A)(1) General**:
- Conductor ampacity ≥ **maximum load to be served**
- For continuous loads: Conductor ampacity ≥ **125% of continuous load + 100% of noncontinuous load**

**Formula**:
```
Minimum Conductor Ampacity = (Continuous Load × 1.25) + (Noncontinuous Load × 1.0)
```

**Definition - Continuous Load**: Operates for 3 hours or more (lighting in commercial building, HVAC, etc.).

**Example 1 - Continuous Lighting Load**:
```
Given:
  - Continuous lighting load: 12A
  - Circuit breaker: 15A
  - Voltage: 120V

Solution:
  Minimum conductor ampacity = 12A × 1.25 = 15A
  Select: 14 AWG copper (15A @ 60°C) or 12 AWG copper (20A, safer)

Note: While 14 AWG technically meets 15A, many jurisdictions require 12 AWG minimum.
```

**Example 2 - Mixed Load**:
```
Given:
  - Continuous load (lights): 10A
  - Noncontinuous load (receptacles): 8A
  - Voltage: 120V

Solution:
  Minimum conductor ampacity = (10A × 1.25) + (8A × 1.0) = 12.5 + 8 = 20.5A
  Circuit breaker: 25A (next standard size)
  Conductor: 10 AWG copper (30A @ 75°C)
```

**(A)(3) Voltage Drop**:
- **Informational Note** (not enforceable):
  - Branch circuits: Maximum 3% voltage drop recommended
  - Combined feeders + branch circuits: Maximum 5% total voltage drop recommended

**Voltage Drop Calculation** (approximate for copper):
```
VD% = (2 × K × I × L) / (1000 × CM × V) × 100

Where:
  K = Conductivity constant (12.9 for copper at 75°C)
  I = Current (amperes)
  L = One-way length (feet)
  CM = Circular mils of conductor
  V = Voltage
```

**Example - Voltage Drop Check**:
```
Given:
  - 20A circuit, 12 AWG copper (6,530 CM)
  - Circuit length: 100 feet (one-way)
  - Voltage: 120V

Solution:
  VD% = (2 × 12.9 × 20 × 100) / (1000 × 6,530 × 120) × 100
  VD% = 51,600 / 783,600 × 100 = 6.6%

Result: Exceeds 3% recommendation → Upsize to 10 AWG (10,380 CM)
  VD% = (2 × 12.9 × 20 × 100) / (1000 × 10,380 × 120) × 100 = 4.2%
  Better, but still high for branch circuit → Consider 8 AWG (16,510 CM)
  VD% = (2 × 12.9 × 20 × 100) / (1000 × 16,510 × 120) × 100 = 2.6% ✓
```

**(B) Household Ranges and Cooking Appliances**:
- Branch circuit conductors for ranges, ovens, cooktops: Rated for load (use Table 220.55)
- Neutral: 70% of demand per 220.55 Note 3

#### 210.20 Overcurrent Protection

**(A) Continuous and Noncontinuous Loads**:
- OCPD rating ≥ **125% of continuous load + 100% of noncontinuous load**

**Formula**:
```
Minimum OCPD Rating = (Continuous Load × 1.25) + (Noncontinuous Load × 1.0)
```

**Exception**: If assembly (including OCPD device) listed for operation at 100% of rating, no 125% multiplier required.

**Example**:
```
Given:
  - Continuous load: 16A
  - Noncontinuous load: 4A

Solution:
  Minimum OCPD = (16A × 1.25) + (4A × 1.0) = 20 + 4 = 24A
  Select: 25A or 30A circuit breaker (standard sizes per 240.6)
```

#### 210.21 Outlet Devices

**(A) Lampholder Ratings**:
- Heavy-duty lampholders: Minimum 660W at 120V (5.5A)
- Medium-base Edison screw: Maximum 15A

**(B) Receptacle Ratings**:

**(B)(1) Single Receptacle on Individual Branch Circuit**:
- Receptacle rating ≥ branch circuit rating

**Example**:
```
20A individual branch circuit → 20A receptacle (single outlet)
30A individual branch circuit → 30A receptacle (e.g., dryer)
```

**(B)(2) Total Cord-and-Plug-Connected Load**:
- Load ≤ 80% of receptacle rating

**(B)(3) Receptacle Ratings**:

```
┌───────────────────────────┬──────────────────────────────────────┐
│ Circuit Rating            │ Receptacle Rating Permitted          │
├───────────────────────────┼──────────────────────────────────────┤
│ 15A                       │ 15A maximum                          │
│ 20A                       │ 15A or 20A                           │
│ 30A                       │ 30A                                  │
│ 40A                       │ 40A or 50A                           │
│ 50A                       │ 50A                                  │
└───────────────────────────┴──────────────────────────────────────┘
```

**Key Point**: 20A circuits can have 15A receptacles (duplex receptacles are 15A rated, protected by 20A breaker).

#### 210.23 Permissible Loads

**(A) 15- and 20-Ampere Branch Circuits**:
- **Lighting units**: Cord-and-plug or permanently connected
- **Receptacles**: General use
- **Appliances**: Fastened in place (≤ 50% of circuit rating if lighting units and receptacles also supplied)

**Example - 20A Circuit Loading**:
```
20A circuit can supply:
  - Multiple receptacles and lighting (no individual load limit)
  - OR fastened appliance (≤ 10A) + receptacles/lights
  - OR fastened appliance (≤ 16A) only (no other loads)
```

**(B) 30-Ampere Branch Circuits**:
- Fixed lighting with heavy-duty lampholders
- Utilization equipment (appliances, HVAC)
- Not for receptacles except as permitted in 210.21(B)(3)

**(C) 40- and 50-Ampere Branch Circuits**:
- Cooking appliances (ranges, ovens)
- Fixed space heating
- Fixed lighting in industrial locations with heavy-duty lampholders
- Not for general receptacle outlets

---

### Part III - Required Outlets (210.50-210.71)

#### 210.50 General

**Outlet** = Point on wiring system where current is taken to supply equipment.

#### 210.52 Dwelling Unit Receptacle Outlets

**(A) General Provisions**:

**Wall Space**: Receptacle outlet required:
- Every wall space **2 feet or more in width**
- Measured horizontally along floor line
- Maximum **6 feet** between receptacles along walls
- Within **6 feet** of door opening or wall break

**Purpose**: Limits extension cord lengths (reduces trip hazards, fire risk).

**Visualization**:
```
Wall (continuous)
├───────────┼───────────┼───────────┤
0 ft       6 ft       12 ft      18 ft
   Outlet      Outlet      Outlet

→ Maximum 6 ft between outlets
→ Within 6 ft of any point along wall
```

**(B) Small Appliances**:
- Two 20A small appliance circuits required (see 210.11(C)(1))
- Supply kitchen, pantry, dining, breakfast room receptacles

**(C) Countertops**:

**Kitchen and Dining Countertops** - Receptacle outlets required:
- Wall countertop spaces **12 inches or wider** shall have receptacle
- Receptacles **within 20 inches above** countertop
- Maximum **24 inches** along countertop between receptacles
- Peninsulas and islands: Receptacle required if countertop ≥ 24 inches wide and ≥ 12 inches deep

**Visualization - Kitchen Countertop**:
```
Countertop (continuous)
├─────────┼─────────┼─────────┤
0         24 in     48 in    72 in
  Outlet    Outlet    Outlet

→ Maximum 24 inches between outlets along countertop
→ Within 20 inches above countertop surface
```

**Island/Peninsula Requirements**:
- Island ≥ 24 in wide × 12 in deep → 1 receptacle minimum
- Long island (9 ft+ countertop) → 2 receptacles minimum, spaced per 24-inch rule

**(D) Bathrooms**:
- Minimum **one receptacle** within 3 feet of outside edge of basin
- Required on 20A bathroom circuit (210.11(C)(3))

**(E) Outdoor Outlets**:
- **Front and back** of dwelling: Minimum one receptacle (grade level accessible)
- **Each story**: If deck/porch/balcony ≥ 20 sq ft, receptacle required

**(F) Laundry Areas**:
- Minimum **one receptacle** within 6 feet of laundry equipment location
- Required on 20A laundry circuit (210.11(C)(2))

**(G) Basements, Garages, and Accessory Buildings**:
- Minimum **one receptacle** in basement (in addition to laundry)
- Minimum **one receptacle** in attached garage
- Minimum **one receptacle** in detached garage/accessory building with electric power

**(H) Hallways**:
- Hallways **10 feet or more** in length: Minimum one receptacle

#### 210.60 Guest Rooms, Guest Suites, Dormitories

**Hotel/motel guest rooms**:
- Receptacle outlets per 210.52(A) (6-foot spacing rule)
- Minimum two receptacles per room

#### 210.63 Heating, Air-Conditioning, and Refrigeration (HACR) Equipment

**Receptacle outlet required**:
- Within **25 feet** of HVAC equipment
- On **same level** as equipment
- **125V, 15A or 20A** GFCI-protected receptacle
- For service and maintenance access

**Purpose**: Eliminate extension cords for HVAC technicians.

#### 210.64 Electrical Service Areas

**Service equipment locations**:
- Minimum **one 125V, 15A or 20A receptacle** within 25 feet and same level as service equipment
- GFCI-protected if located outdoors

**Purpose**: Service and maintenance access.

#### 210.70 Lighting Outlets Required

**(A) Dwelling Units**:

**Lighting outlets required** in:
- Every **habitable room** (bedroom, living room, kitchen, etc.)
- **Bathrooms**
- **Hallways, stairways**
- **Attached garages** and detached garages with electric power
- **Outdoor entrances and exits** (wall-switch-controlled)

**Habitable Room Exception**: Switched receptacle permitted in lieu of lighting outlet (except kitchen, bathroom).

**(B) Guest Rooms, Guest Suites, Dormitories**:
- Minimum one wall-switch-controlled lighting outlet

**(C) Other Than Dwelling Units**:
- Lighting outlet at each entrance/exit with grade-level access
- Interior stairways with six or more risers: Lighting outlet each floor level

---

## Article 215 - Feeders

### Part I - General Requirements (215.1-215.12)

#### 215.1 Scope

Article 215 covers:
- Feeder conductor sizing and installation
- Feeder overcurrent protection
- Feeder grounding and identification

#### 215.2 Minimum Rating and Size

**(A) Feeders Not More Than 600 Volts**:

**(A)(1) General**:
- Feeder conductor ampacity ≥ **loads supplied**
- For continuous loads: Ampacity ≥ **125% of continuous load + 100% of noncontinuous load**

**Formula** (same as branch circuits):
```
Minimum Feeder Ampacity = (Continuous Load × 1.25) + (Noncontinuous Load × 1.0)
```

**Example - Feeder to Lighting Panel**:
```
Given:
  - Continuous lighting load: 80A (operates >3 hours)
  - Noncontinuous receptacle load: 20A
  - Service voltage: 208Y/120V, 3-phase

Solution:
  Minimum feeder ampacity = (80A × 1.25) + (20A × 1.0) = 100 + 20 = 120A
  Select feeder conductors: #1 AWG copper (130A @ 75°C) or 2/0 AWG aluminum (135A @ 75°C)
  Feeder OCPD: 125A (next standard size)
```

**(A)(2) Grounded Conductor (Neutral)**:
- Ampacity ≥ maximum unbalanced load
- For ranges, dryers: Neutral sized per 220.61 (70% of demand)

**Example - Neutral Sizing**:
```
Given:
  - 208Y/120V, 3-phase feeder
  - Balanced 3-phase load: 100A per phase
  - Line-to-neutral loads: 30A Phase A, 20A Phase B, 25A Phase C

Solution:
  Maximum unbalanced load = 30A (Phase A highest)
  Minimum neutral ampacity = 30A
  Select: #10 AWG copper (35A @ 75°C)

Note: Phase conductors sized for 100A continuous (125A adjusted)
      Neutral sized for maximum unbalanced (30A)
```

**(A)(3) Voltage Drop**:
- **Informational Note**: Maximum 5% voltage drop (feeder + branch circuit combined)
- Feeder alone: 2% recommended (leaving 3% for branch circuits)

**(B) Capacity and Overcurrent Protection**:
- Feeder conductors with capacity and OCPD per 240.4

#### 215.3 Overcurrent Protection

**Feeder OCPD location**: Where conductors receive supply (at source).

**Taps permitted**: See 240.21 (feeder tap rules).

#### 215.4 Feeders with Common Neutral

**Multiwire feeders** (shared neutral):
- Permitted for:
  - Two or three sets of 3-wire feeders
  - Two sets of 4-wire or 5-wire feeders
- Neutral carries only unbalanced current
- All conductors of each set from same phase
- OCPD simultaneously disconnects all ungrounded conductors

**Example - Shared Neutral Feeder**:
```
208Y/120V, 3-phase Panel
   │
   ├─ Phase A (black) ──┐
   ├─ Phase B (red) ─────┼─→ Feeder #1 to Subpanel 1
   ├─ Neutral (white) ───┘    (Phases A, B, N)
   │
   ├─ Phase B (red) ─────┐
   ├─ Phase C (blue) ────┼─→ Feeder #2 to Subpanel 2
   └─ Neutral (white) ───┘    (Phases B, C, N)

Note: Shared neutral carries unbalanced current from both feeders
      (Phases A, B, C must be balanced to avoid neutral overload)
```

#### 215.5 Diagrams of Feeders

**Documentation**: Permanent plaque or directory showing area served by each feeder (if not evident).

**Purpose**: Identification for maintenance and emergency access.

#### 215.6 Feeder Equipment Grounding Conductor

**Equipment grounding conductor** (EGC):
- Required with feeder conductors
- Sized per Table 250.122 (based on feeder OCPD rating)
- May be raceway if listed for grounding (RMC, IMC, EMT)

#### 215.9 Ground-Fault Circuit-Interrupter Protection for Personnel

**GFCI protection required**:
- Feeders supplying 15A and 20A receptacle branch circuits (if those branch circuits require GFCI per 210.8)

**Typical application**: GFCI circuit breaker on feeder to outdoor subpanel.

#### 215.10 Ground-Fault Protection of Equipment (GFPE)

**GFPE required for**:
- Feeder disconnects rated **1000A or more**
- Solidly grounded wye systems (150V to 1000V to ground)
- Not required if GFPE provided on service equipment

**Settings**:
- Maximum pickup: 1200A
- Maximum time delay: 1 second at 3000A ground fault

**Purpose**: Detect arcing ground faults below phase overcurrent trip level (fire prevention).

#### 215.11 Circuits Derived from Autotransformers

**Autotransformer feeders**:
- Grounded conductor from autotransformer must be common to input and output

#### 215.12 Identification for Feeders

**(A) Grounded Conductor (Neutral)**:
- White or gray

**(B) Equipment Grounding Conductor**:
- Green, green with yellow stripe, or bare

**(C) Ungrounded Conductors (Phases)**:
- Means of identification required if multiple systems in building
- Posting at distribution equipment showing phase identification

---

## Design Examples

### Example 1: Dwelling Unit Kitchen Branch Circuits

**Scenario**: Kitchen in single-family dwelling, 12-foot countertop.

**Requirements** (210.52(C)):
- Small appliance circuits: Two 20A circuits minimum
- Receptacle outlets: Maximum 24 inches apart along countertop
- Within 20 inches above countertop
- All kitchen receptacles on 20A small appliance circuits

**Design**:
```
Circuit 1 (20A, #12 AWG copper):
  - Countertop receptacles: South wall (3 outlets, 24" spacing)
  - Countertop receptacles: Island (1 outlet)

Circuit 2 (20A, #12 AWG copper):
  - Countertop receptacles: North wall (3 outlets, 24" spacing)
  - Dining room receptacles (2 outlets)
  - Pantry receptacles (1 outlet)

Separate circuits:
  - Refrigerator: 20A individual circuit
  - Dishwasher: 15A or 20A individual circuit
  - Microwave: 20A individual circuit (if built-in)
  - Disposal: 15A or 20A circuit (may share with dishwasher)
  - Range: 40A or 50A individual circuit (240V)
```

**Notes**:
- All countertop receptacles GFCI-protected (210.8(A)(6))
- 20A circuits require 12 AWG copper minimum (210.11(C)(1))
- Small appliance circuits serve kitchen, dining, pantry only (no other loads)

---

### Example 2: Residential Bathroom Circuit

**Scenario**: Three bathrooms in dwelling unit.

**Requirements** (210.11(C)(3)):
- Minimum one 20A circuit for bathroom receptacles
- Options:
  1. Receptacles only (can serve multiple bathrooms)
  2. One bathroom only (receptacles + lights + fan)

**Design Option 1 - Receptacles Only**:
```
Circuit 1 (20A, #12 AWG copper):
  - Master bath: 2 receptacles (1 each side of double vanity)
  - Guest bath: 1 receptacle
  - Half bath: 1 receptacle

Separate circuits:
  - Bathroom lighting: On general lighting circuit (15A)
  - Exhaust fans: On general lighting circuit
```

**Design Option 2 - Single Bathroom All Loads**:
```
Circuit 1 (20A, #12 AWG copper) - Master Bath Only:
  - Master bath: 2 receptacles
  - Master bath: Lighting (ceiling, vanity)
  - Master bath: Exhaust fan

Circuit 2 (15A or 20A, #14 or #12 AWG) - Guest Bath:
  - Guest bath: 1 receptacle (GFCI)
  - Guest bath: Lighting, fan

Circuit 3 (15A or 20A) - Half Bath:
  - Half bath: 1 receptacle (GFCI)
  - Half bath: Lighting
```

**Notes**:
- All bathroom receptacles GFCI-protected (210.8(A)(1))
- Minimum one 20A circuit required; additional circuits may be 15A or 20A
- Bathroom GFCI: Within 3 feet of basin (210.52(D))

---

### Example 3: Commercial Office Feeder

**Scenario**: 100A feeder to office subpanel, 150 feet from main service.

**Given**:
- Main service: 400A, 208Y/120V, 3-phase
- Subpanel load (calculated per Article 220):
  - Continuous lighting: 60A (balanced 3-phase)
  - Noncontinuous receptacles: 20A (balanced 3-phase)
- Voltage drop limit: 2% (feeder alone)

**Step 1: Minimum Ampacity**
```
Adjusted load = (60A × 1.25) + (20A × 1.0) = 75 + 20 = 95A per phase
OCPD size = 100A (next standard size)
Minimum conductor ampacity = 95A
```

**Step 2: Voltage Drop Check**
```
Voltage drop formula (3-phase):
  VD% = (√3 × K × I × L) / (1000 × CM × V) × 100

Trial: #2 AWG copper (66,360 CM, 115A @ 75°C):
  VD% = (1.732 × 12.9 × 95 × 150) / (1000 × 66,360 × 208) × 100
  VD% = 318,229 / 13,802,880 × 100 = 2.3%

Too high! Upsize to #1 AWG copper (83,690 CM, 130A @ 75°C):
  VD% = (1.732 × 12.9 × 95 × 150) / (1000 × 83,690 × 208) × 100
  VD% = 318,229 / 17,407,520 × 100 = 1.8% ✓
```

**Step 3: Equipment Grounding Conductor (EGC)**
```
Feeder OCPD = 100A
Table 250.122 → EGC = 8 AWG copper
```

**Step 4: Neutral Sizing**
```
Maximum unbalanced load = 60A (lighting, worst case)
(Assume balanced 3-phase, neutral carries minimal current)
Neutral ampacity ≥ 60A
Select: #6 AWG copper (65A @ 75°C)
(Could use #8 if neutral current verified lower via detailed calculation)
```

**Final Feeder Design**:
```
Feeder to Office Subpanel (100A):
  - Phase conductors: #1 AWG copper THHN (3 conductors, black/red/blue)
  - Neutral: #6 AWG copper THHN (white)
  - Equipment grounding: #8 AWG copper THHN (green or bare)
  - Raceway: 1-1/4" EMT
  - Length: 150 feet
  - OCPD: 100A circuit breaker (3-pole at main panel)
  - Voltage drop: 1.8% (acceptable)
```

---

### Example 4: Outdoor Receptacle Branch Circuit (GFCI)

**Scenario**: Outdoor receptacles on rear patio and front porch of dwelling.

**Requirements** (210.8(A)(3)):
- All outdoor receptacles GFCI-protected
- 210.52(E): One receptacle required at front and back

**Design**:
```
Circuit 1 (20A, #12 AWG copper, GFCI-protected):
  - Front porch: 1 weatherproof receptacle (GFCI)
  - Rear patio: 2 weatherproof receptacles (GFCI-protected via upstream GFCI)
  - Garage exterior: 1 receptacle (GFCI-protected)

GFCI Protection Methods:
  Option 1: GFCI circuit breaker at panel (protects entire circuit)
  Option 2: GFCI receptacle at first outlet (front porch), feeds through to others

Note: Weatherproof covers required (while-in-use covers for dwelling units)
```

**Installation**:
```
Panel (20A GFCI breaker)
   │
   └─ #12 AWG copper (in UF cable or PVC conduit underground)
         │
         ├─ Front porch GFCI receptacle (weatherproof box, WP cover)
         ├─ Rear patio receptacles (2) (fed from front GFCI)
         └─ Garage exterior receptacle
```

**Notes**:
- Outdoor receptacles: 15A or 20A, weatherproof
- Underground wiring: Direct burial UF cable or conductors in PVC
- Depth: 12 inches (if GFCI protected), 18 inches (standard), 24 inches (under driveways)
- All receptacles accessible from grade level

---

### Example 5: HVAC Receptacle and Disconnect

**Scenario**: Rooftop HVAC unit on commercial building.

**Requirements**:
- 210.63: Receptacle within 25 feet, same level as HVAC
- 440.14: Disconnect within sight of HVAC

**Design**:
```
HVAC Unit (208V, 3-phase, 30A):
  - Feeder: #10 AWG copper (30A), 208V/3-phase
  - Disconnect: 30A fused disconnect or circuit breaker (within sight of unit)
  - Receptacle: 125V, 20A, GFCI-protected (within 25 feet of unit)

Receptacle Circuit (separate from HVAC):
  - Circuit: 20A, 120V (from nearby panelboard or tapped from HVAC feeder control transformer)
  - Conductor: #12 AWG copper
  - GFCI protection: Required (rooftop location per 210.8(B)(3))
  - Weatherproof enclosure
```

**Installation**:
```
HVAC Feeder (208V/3-phase)
   │
   ├─ 30A Disconnect (fused or circuit breaker)
   │     │
   │     └─ HVAC unit
   │
   └─ Control transformer (208V → 120V)
         │
         └─ 20A circuit → GFCI receptacle (for service, within 25 ft of unit)
```

**Notes**:
- Receptacle must not be on load side of HVAC disconnect (defeats purpose of service receptacle)
- Weatherproof, while-in-use cover on receptacle
- Rooftop = outdoor location → GFCI required (210.8(B)(3))

---

### Example 6: Feeder to Detached Garage

**Scenario**: Detached garage 50 feet from house, needs 60A feeder.

**Requirements**:
- 210.52(G): One receptacle required in detached garage
- 210.70(A)(2)(b): Lighting outlet required in detached garage
- 250.32: Grounding electrode required at separate building

**Feeder Design**:
```
Given:
  - Load: 60A (calculated)
  - Distance: 50 feet
  - Voltage: 240V, single-phase (no neutral loads in garage)

Feeder Conductors:
  - Phases: #6 AWG copper (65A @ 75°C)
  - Equipment grounding conductor: #10 AWG copper (per Table 250.122, 60A OCPD)
  - No neutral required (no 120V loads)

OCPD: 60A circuit breaker (2-pole at main panel)

Grounding at Garage:
  - Grounding electrode: Two ground rods (8 ft, 5/8" diameter)
  - Bond EGC to grounding electrode
  - No neutral-to-ground bond at garage (250.32(B)(1))
```

**Installation**:
```
Main Panel (House)
   │
   ├─ 60A Circuit Breaker (2-pole)
   │     │
   │     └─ #6 AWG copper (2 hots) + #10 AWG copper (ground)
   │           │
   │           └─[50 ft underground in PVC conduit]
   │                 │
   │              Garage Subpanel (60A main breaker)
   │                 │
   │                 ├─ Ground bus (bonded to enclosure, connected to EGC)
   │                 └─ GEC to ground rods (2)
   │
   └─ Loads: 240V only (electric heater, 240V outlets)
```

**Alternative with 120V Loads**:
```
If 120V receptacles/lights needed:
  - Feeder: #6 AWG copper (2 hots) + #8 AWG neutral + #10 AWG EGC
  - Voltage: 120/240V
  - Neutral bus at garage: Isolated from ground bus
  - EGC connected to ground bus (bonded to enclosure and grounding electrodes)
```

---

## Integration with QA/QC Rules

### QA Rules for Branch Circuits and Feeders (QA-301-ELEC through QA-314-ELEC)

#### QA-301-ELEC: Conductor Ampacity for Continuous Loads

**Rule Definition**:
```yaml
- id: QA-301-ELEC
  description: Verify conductor ampacity ≥ 125% continuous + 100% noncontinuous per 210.19(A)(1)
  severity: critical
  category: compliance
  check:
    type: custom
    function: validate_conductor_ampacity_continuous
```

**Validation Logic**:
```python
def validate_conductor_ampacity_continuous(circuit_schedule):
    continuous_load = circuit_schedule.get("continuous_load_amperes", 0)
    noncontinuous_load = circuit_schedule.get("noncontinuous_load_amperes", 0)
    conductor_ampacity = circuit_schedule.get("conductor_ampacity")

    required_ampacity = (continuous_load * 1.25) + noncontinuous_load

    if conductor_ampacity < required_ampacity:
        return {
            "status": "FAIL",
            "message": f"Conductor ampacity {conductor_ampacity}A insufficient for "
                      f"{continuous_load}A continuous + {noncontinuous_load}A noncontinuous "
                      f"(requires {required_ampacity}A per 210.19(A)(1))"
        }

    return {"status": "PASS"}
```

**NEC Reference**: 210.19(A)(1), 215.2(A)(1)

---

#### QA-302-ELEC: GFCI Protection Required Locations

**Rule Definition**:
```yaml
- id: QA-302-ELEC
  description: Verify GFCI protection for receptacles in required locations per 210.8
  severity: critical
  category: compliance
  check:
    type: custom
    function: validate_gfci_protection
```

**Validation Logic**:
```python
def validate_gfci_protection(receptacle_schedule):
    location = receptacle_schedule.get("location")
    occupancy = receptacle_schedule.get("occupancy_type", "dwelling")
    gfci_protected = receptacle_schedule.get("gfci_protected", False)

    # 210.8(A) - Dwelling Units
    dwelling_gfci_locations = [
        "bathroom", "garage", "outdoor", "crawl space", "unfinished basement",
        "kitchen countertop", "within 6 ft of sink", "laundry", "within 6 ft of bathtub/shower"
    ]

    # 210.8(B) - Other Than Dwelling Units
    commercial_gfci_locations = [
        "bathroom", "kitchen", "rooftop", "outdoor", "sink area", "indoor wet location",
        "locker room with shower"
    ]

    if occupancy == "dwelling" and location.lower() in [loc.lower() for loc in dwelling_gfci_locations]:
        if not gfci_protected:
            return {
                "status": "FAIL",
                "message": f"GFCI protection required for {location} receptacle per 210.8(A)"
            }
    elif occupancy != "dwelling" and location.lower() in [loc.lower() for loc in commercial_gfci_locations]:
        if not gfci_protected:
            return {
                "status": "FAIL",
                "message": f"GFCI protection required for {location} receptacle per 210.8(B)"
            }

    return {"status": "PASS"}
```

**NEC Reference**: 210.8

---

#### QA-303-ELEC: Required Dwelling Unit Circuits

**Rule Definition**:
```yaml
- id: QA-303-ELEC
  description: Verify required dwelling unit circuits present (small appliance, laundry, bathroom) per 210.11(C)
  severity: high
  category: compliance
  check:
    type: custom
    function: validate_required_dwelling_circuits
```

**Validation Logic**:
```python
def validate_required_dwelling_circuits(panel_schedule):
    occupancy = panel_schedule.get("occupancy_type")
    if occupancy != "dwelling":
        return {"status": "PASS", "message": "Not applicable to non-dwelling"}

    circuits = panel_schedule.get("circuits", [])

    # Count required circuit types
    small_appliance_circuits = [c for c in circuits if c.get("circuit_type") == "small_appliance"]
    laundry_circuits = [c for c in circuits if c.get("circuit_type") == "laundry"]
    bathroom_circuits = [c for c in circuits if c.get("circuit_type") == "bathroom"]

    errors = []

    # 210.11(C)(1) - Minimum 2 small appliance circuits, 20A
    if len(small_appliance_circuits) < 2:
        errors.append("Minimum 2 small appliance circuits required (210.11(C)(1))")
    for circuit in small_appliance_circuits:
        if circuit.get("rating") < 20:
            errors.append(f"Small appliance circuit {circuit.get('id')} must be 20A (210.11(C)(1))")

    # 210.11(C)(2) - Minimum 1 laundry circuit, 20A
    if len(laundry_circuits) < 1:
        errors.append("Minimum 1 laundry circuit required (210.11(C)(2))")
    for circuit in laundry_circuits:
        if circuit.get("rating") < 20:
            errors.append(f"Laundry circuit {circuit.get('id')} must be 20A (210.11(C)(2))")

    # 210.11(C)(3) - Minimum 1 bathroom circuit, 20A
    if len(bathroom_circuits) < 1:
        errors.append("Minimum 1 bathroom circuit required (210.11(C)(3))")
    for circuit in bathroom_circuits:
        if circuit.get("rating") < 20:
            errors.append(f"Bathroom circuit {circuit.get('id')} must be 20A (210.11(C)(3))")

    if errors:
        return {"status": "FAIL", "message": "; ".join(errors)}

    return {"status": "PASS"}
```

**NEC Reference**: 210.11(C)

---

#### QA-304-ELEC through QA-314-ELEC: Additional Circuit/Feeder Validations

Additional rules cover:

- **QA-304-ELEC**: Receptacle spacing in dwelling units (210.52(A) - 6 ft maximum)
- **QA-305-ELEC**: Kitchen countertop receptacles (210.52(C) - 24 in maximum spacing)
- **QA-306-ELEC**: AFCI protection for dwelling bedrooms/living areas (210.12)
- **QA-307-ELEC**: Multiwire branch circuit handle ties (210.4(B))
- **QA-308-ELEC**: Voltage drop within recommendations (210.19(A)(3) - 3% branch, 2% feeder)
- **QA-309-ELEC**: HVAC receptacle within 25 feet (210.63)
- **QA-310-ELEC**: Outdoor receptacles at front/back of dwelling (210.52(E))
- **QA-311-ELEC**: Bathroom receptacle within 3 feet of basin (210.52(D))
- **QA-312-ELEC**: Feeder equipment grounding conductor sized correctly (215.6, Table 250.122)
- **QA-313-ELEC**: Feeder GFPE for solidly grounded wye ≥1000A (215.10)
- **QA-314-ELEC**: Neutral conductor sized for maximum unbalanced load (215.2(A)(2))

---

## Quick Reference Tables

### Table: GFCI Required Locations Summary

| Location | Dwelling Unit (210.8(A)) | Commercial (210.8(B)) |
|----------|--------------------------|------------------------|
| Bathrooms | All receptacles | All receptacles |
| Kitchens (countertop) | All receptacles | All receptacles |
| Within 6 ft of sinks | Required | Required |
| Outdoors | All receptacles | Public/grade level |
| Garages | All receptacles | Not required |
| Unfinished basements | All receptacles | Not required |
| Crawl spaces | All receptacles | Not required |
| Laundry (within 6 ft sink) | Required | Not specified |
| Rooftops | - | All receptacles |
| Indoor wet locations | - | All receptacles |

### Table: Required Dwelling Unit Circuits (210.11(C))

| Circuit Type | Minimum Quantity | Rating | Permitted Loads |
|--------------|------------------|--------|-----------------|
| Small appliance | 2 | 20A | Kitchen, dining, pantry receptacles only |
| Laundry | 1 | 20A | Laundry receptacles only |
| Bathroom | 1 | 20A | Bathroom receptacles (±lights/fan if single bath) |

### Table: Branch Circuit Ratings and Loads (210.23)

| Circuit Rating | Receptacles Permitted | Lighting Permitted | Max Fixed Appliance (w/ other loads) |
|----------------|----------------------|-------------------|--------------------------------------|
| 15A | 15A | Yes | 7.5A (50% of 15A) |
| 20A | 15A or 20A | Yes | 10A (50% of 20A) |
| 30A | 30A (special) | Heavy-duty only | 24A (80% of 30A) |
| 40A-50A | 40A-50A (special) | Industrial heavy-duty | Fixed appliances only |

### Table: Conductor Sizing for Continuous Loads

| Load Type | Conductor Sizing Multiplier | OCPD Sizing Multiplier |
|-----------|----------------------------|------------------------|
| Continuous (≥3 hours) | 125% (1.25) | 125% (1.25) |
| Noncontinuous (<3 hours) | 100% (1.0) | 100% (1.0) |

**Formula**: `Minimum Ampacity/OCPD = (Continuous × 1.25) + (Noncontinuous × 1.0)`

### Table: Voltage Drop Recommendations

| System Component | Recommended Max Voltage Drop | Notes |
|------------------|------------------------------|-------|
| Branch circuits | 3% | Informational note (not enforceable) |
| Feeders | 2% | Allows 3% for branch circuits |
| Combined (feeder + branch) | 5% total | Overall system recommendation |

**Calculation**: `VD% = (2 × K × I × L) / (1000 × CM × V) × 100` (single-phase)

---

## Conclusion

NEC Articles 210 and 215 establish comprehensive requirements for branch circuits and feeders. Key takeaways:

1. **Continuous load factor**: 125% multiplier for conductor ampacity and OCPD sizing (210.19, 210.20, 215.2)
2. **GFCI protection**: Required in specific locations (bathrooms, kitchens, outdoors, etc.) per 210.8
3. **AFCI protection**: Required for dwelling unit habitable rooms (bedrooms, living areas, etc.) per 210.12
4. **Required dwelling circuits**: Two 20A small appliance, one 20A laundry, one 20A bathroom (210.11(C))
5. **Receptacle spacing**: Maximum 6 feet along walls, 24 inches along kitchen countertops (210.52)
6. **Voltage drop**: 3% branch circuits, 2% feeders recommended (210.19(A)(3), 215.2(A)(3))
7. **Multiwire circuits**: Simultaneous disconnect required (handle ties or multi-pole breakers) (210.4(B))
8. **Feeder grounding**: EGC required, sized per Table 250.122 (215.6)
9. **Feeder GFPE**: Required for solidly grounded wye systems ≥1000A (215.10)
10. **HVAC receptacles**: Within 25 feet of equipment, GFCI-protected (210.63)

Always coordinate with Articles 220 (load calculations), 240 (overcurrent protection), and 250 (grounding) for complete electrical system design.

---

**Document Version**: 1.0
**Last Updated**: 2025-01-22
**Next Review**: NEC 2026 edition adoption
**Maintained By**: EE_AI Platform - MEP Library Curation Team
