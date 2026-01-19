# NEC 2023 Article 240 - Overcurrent Protection (DETAILED)

## Document Information

**NEC Article**: 240
**Title**: Overcurrent Protection
**Edition**: NFPA 70-2023 National Electrical Code
**Scope**: Requirements for overcurrent protective devices (circuit breakers, fuses) to protect conductors and equipment
**Last Updated**: 2025-01-22
**Curator**: EE_AI Platform Reference Library

---

## Table of Contents

1. [Article Overview](#article-overview)
2. [Part I - General (240.1-240.13)](#part-i---general)
3. [Part II - Location (240.20-240.24)](#part-ii---location)
4. [Part III - Enclosures (240.30-240.33)](#part-iii---enclosures)
5. [Part IV - Disconnecting Means (240.40-240.41)](#part-iv---disconnecting-means)
6. [Part V - Plug Fuses, Fuseholders, and Adapters (240.50-240.54)](#part-v---plug-fuses)
7. [Part VI - Cartridge Fuses and Fuseholders (240.60-240.61)](#part-vi---cartridge-fuses)
8. [Part VII - Circuit Breakers (240.80-240.87)](#part-vii---circuit-breakers)
9. [Part VIII - Supervised Industrial Installations (240.90-240.92)](#part-viii---supervised-industrial)
10. [Part IX - Overcurrent Protection Over 1000 Volts (240.100-240.101)](#part-ix---over-1000v)
11. [Design Scenarios and Examples](#design-scenarios-and-examples)
12. [Circuit Breakers vs. Fuses Selection Guide](#circuit-breakers-vs-fuses)
13. [Selective Coordination](#selective-coordination)
14. [Integration with QA/QC Rules](#integration-with-qaqc-rules)
15. [Quick Reference Tables](#quick-reference-tables)

---

## Article Overview

Article 240 establishes requirements for overcurrent protective devices (OCPDs) that protect conductors and equipment from excessive current that could cause conductor overheating, insulation damage, or fire.

**Key Functions of Overcurrent Protection**:
1. **Overload protection**: Protect against sustained excess current (125% for 3+ hours)
2. **Short-circuit protection**: Clear faults rapidly (milliseconds to seconds)
3. **Ground-fault protection**: Detect and clear ground faults
4. **Coordination**: Minimize outage area by isolating only faulted section

**Types of OCPDs**:
- **Circuit breakers**: Mechanical switching device, resettable, thermal-magnetic or electronic
- **Fuses**: One-time fusible element, must be replaced after operation
- **Electronic trip units**: Solid-state protection with programmable curves

---

## Part I - General (240.1-240.13)

### 240.1 Scope

Article 240 covers:
- General requirements for overcurrent protection
- Overcurrent protective devices (circuit breakers, fuses)
- Installation and location requirements
- Coordination requirements for specific systems

**What's NOT in Article 240**:
- Motor overload protection (see Article 430)
- Transformer protection (see Article 450)
- Conductor ampacity (see Article 310)

### 240.2 Definitions

**Coordination (Selective)**:
- Localization of overcurrent condition to restrict outages to circuit or equipment affected
- Upstream device does not trip when downstream device operates

**Current-Limiting Overcurrent Protective Device**:
- Device that limits instantaneous peak current during first half-cycle
- Reduces available let-through energy (I²t)

**Supervised Industrial Installation**:
- Industrial facility with qualified maintenance personnel
- Written safety procedures
- Allows certain relaxations (see Part VIII)

### 240.3 Other Articles

**Specific requirements in other articles take precedence**:
- **Article 250**: Grounding and bonding
- **Article 310**: Conductor ampacity
- **Article 430**: Motors, motor circuits, and controllers
- **Article 450**: Transformers
- **Article 480**: Storage batteries

### 240.4 Protection of Conductors

**General Rule**: Conductors shall be protected against overcurrent per their ampacity from Table 310.16 (or applicable table).

**OCPD Rating**:
```
OCPD Rating ≤ Conductor Ampacity (after corrections/adjustments)
```

**Exception**: Where conductor ampacity does not correspond to standard OCPD rating (240.6), next higher standard rating is permitted if conditions in 240.4(B) are met.

#### 240.4(B) Devices Rated 800 Amperes or Less

If conductor ampacity does NOT match a standard fuse or circuit breaker rating (Table 240.6(A)), the **next higher standard rating** is permitted provided:

1. Conductors are not part of multioutlet branch circuit supplying receptacles
2. Ampacity does not correspond to standard rating
3. Next higher rating does not exceed 800 amperes

**Example**:
```
Given: #4 AWG copper THHN conductor in conduit
  From Table 310.16: 85A ampacity @ 75°C
  Standard OCPD sizes: 70A, 80A, 90A, 100A

Question: What OCPD size is permitted?
Answer: 90A is permitted (next size up from 85A per 240.4(B))
```

#### 240.4(D) Small Conductors

**Specific maximum OCPD ratings for small conductors**:

```
┌──────────────────────────┬─────────────────────────────────────┐
│ Conductor Size           │ Maximum OCPD Rating                 │
├──────────────────────────┼─────────────────────────────────────┤
│ 18 AWG copper            │ 7 amperes                           │
│ 16 AWG copper            │ 10 amperes                          │
│ 14 AWG copper            │ 15 amperes                          │
│ 12 AWG copper            │ 20 amperes                          │
│ 12 AWG aluminum          │ 15 amperes                          │
│ 10 AWG copper            │ 30 amperes                          │
│ 10 AWG aluminum          │ 25 amperes                          │
└──────────────────────────┴─────────────────────────────────────┘
```

**Critical Rule**: 14 AWG copper maximum 15A, 12 AWG copper maximum 20A (most common branch circuits).

**Example - Residential Branch Circuit**:
```
Given: 14 AWG copper NM cable, 15A circuit breaker
Validation:
  14 AWG max OCPD = 15A per 240.4(D)
  ✓ Compliant
```

**Example - Violation**:
```
Given: 14 AWG copper conductor protected by 20A breaker
Validation:
  14 AWG max OCPD = 15A per 240.4(D)
  20A > 15A
  ✗ Code violation - conductor undersized for OCPD
```

### 240.5 Protection of Flexible Cords, Flexible Cables, and Fixture Wires

**Flexible cords and fixture wires**:
- Protected per their ampacity in Tables 400.5(A)(1) and 400.5(A)(2)
- Maximum OCPD ratings listed in those tables

### 240.6 Standard Ampere Ratings

#### 240.6(A) Fuses and Fixed-Trip Circuit Breakers

**Standard ampere ratings**:

```
┌──────────────────────────────────────────────────────────────────┐
│ Standard OCPD Ratings (240.6(A))                                 │
├──────────────────────────────────────────────────────────────────┤
│ 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 125,  │
│ 150, 175, 200, 225, 250, 300, 350, 400, 450, 500, 600, 700,     │
│ 800, 1000, 1200, 1600, 2000, 2500, 3000, 4000, 5000, 6000       │
└──────────────────────────────────────────────────────────────────┘
```

**Note**: Additional standard ratings exist for fuses above 6000A.

**Non-Standard Ratings**: Not permitted unless they are adjustable-trip circuit breakers.

#### 240.6(B) Adjustable-Trip Circuit Breakers

**Adjustable-trip breakers**:
- Electronic trip units with adjustable settings
- Rating is maximum setting of adjustable element
- Must be sealed or accessible only to qualified persons

### 240.8 Fuses or Circuit Breakers in Parallel

**General Rule**: Fuses and circuit breakers shall NOT be connected in parallel.

**Exception**: Factory-assembled parallel OCPDs (e.g., meter centers, switchboards) listed for the purpose.

**Rationale**: Unequal current sharing between parallel devices can cause one device to carry excessive current.

### 240.9 Thermal Devices

**Thermal cutouts and thermal relays**:
- Protect motors and motor-operated appliances
- NOT permitted as branch circuit protection (must have fuse or CB upstream)

### 240.10 Supplementary Overcurrent Protection

**Supplementary OCPDs** (e.g., internal fuses in appliances):
- Used to protect internal components
- NOT required to be readily accessible
- NOT used as branch circuit protection

### 240.12 Electrical System Coordination

**Coordination required for**:
- Emergency systems (Article 700)
- Legally required standby systems (Article 701)
- Critical operations power systems (COPS, Article 708)
- Elevator circuits (Article 620)

**Definition**: Selective coordination = upstream OCPD does not trip when downstream OCPD clears fault.

**Purpose**: Minimize outage area, maintain power to non-faulted loads.

### 240.13 Ground-Fault Protection of Equipment (GFPE)

**Requirements** (see 230.95 and 215.10):
- Solidly grounded wye services 150V-to-ground, >1000A
- Set to trip at 1200A or less
- Maximum time delay of 1 second at 3000A ground fault

**Purpose**: Detect arcing ground faults that are below phase overcurrent trip settings.

**Note**: GFPE is NOT the same as GFCI (ground-fault circuit interrupter for personnel protection at 4-6 mA).

---

## Part II - Location (240.20-240.24)

### 240.21 Location in Circuit

**General Rule**: Overcurrent protection shall be provided at the point where conductors receive their supply (i.e., where they connect to higher-ampacity conductors).

**Exceptions - Feeder Taps**: Permitted under specific conditions (tap rules).

#### 240.21(B) Feeder Taps

Feeder taps allow smaller conductors to be tapped from larger feeders without OCPD at the tap point, provided tap conductors meet specific length and capacity requirements.

##### 240.21(B)(1) Taps Not Over 10 Feet (3 m) Long

**Requirements** (10-foot tap rule):
1. Length ≤ 10 feet
2. Tap conductor ampacity ≥ combined calculated load
3. Tap conductor ampacity ≥ 10% of OCPD rating protecting feeder
4. Tap does not extend beyond switchboard, panelboard, or control device it supplies
5. Tap conductors enclosed in raceway (from tap point to enclosure)

**Formula**:
```
Minimum tap conductor ampacity = MAX(
  Combined load on tap,
  10% × Feeder OCPD rating
)
```

**Example - 10-Foot Tap**:
```
Given:
  - Feeder: 400A OCPD protecting 500 kcmil conductors (380A ampacity)
  - Tap load: 100A
  - Tap length: 8 feet

Solution:
  Minimum tap ampacity = MAX(100A, 400A × 10%) = MAX(100A, 40A) = 100A

  Select: #1 AWG copper (110A @ 75°C) or larger
  ✓ Meets 10-foot tap rule
```

**Diagram**:
```
Feeder (400A OCPD)
   │
   └──[Tap point - No OCPD]
         │
         │ <── 10 ft max, #1 AWG (110A), in conduit
         │
      [Panelboard with 100A main breaker]
```

##### 240.21(B)(2) Taps Not Over 25 Feet (7.5 m) Long

**Requirements** (25-foot tap rule):
1. Length ≤ 25 feet
2. Tap conductor ampacity ≥ 1/3 of feeder OCPD rating
3. Tap terminates in single OCPD ≤ tap conductor ampacity
4. Tap conductors protected from physical damage

**Formula**:
```
Minimum tap conductor ampacity ≥ (Feeder OCPD rating / 3)
```

**Example - 25-Foot Tap**:
```
Given:
  - Feeder: 600A OCPD
  - Tap length: 20 feet
  - Tap load: 150A

Solution:
  Minimum tap ampacity = 600A / 3 = 200A

  Select: 3/0 AWG copper (200A @ 75°C)
  Terminate in: 200A OCPD (can be sized for tap conductor, not load)

  ✓ Meets 25-foot tap rule
```

**Diagram**:
```
Feeder (600A OCPD)
   │
   └──[Tap point - No OCPD]
         │
         │ <── 25 ft max, 3/0 AWG (200A), protected
         │
      [200A OCPD] <── Single OCPD at tap termination
         │
      [150A load]
```

##### 240.21(B)(5) Outside Taps of Unlimited Length

**Requirements** (outside tap rule):
1. Tap conductors are outside the building
2. Tap conductor ampacity ≥ 1/10 of feeder OCPD rating
3. Tap terminates at single OCPD (on inside or outside) ≤ tap conductor ampacity
4. Conductors protected per 230.6 (outside protection methods)
5. No length limit for outdoor portion

**Formula**:
```
Minimum tap conductor ampacity ≥ (Feeder OCPD rating / 10)
```

**Example - Outside Tap**:
```
Given:
  - Main building feeder: 1000A OCPD
  - Detached building: 300 feet away
  - Load: 80A

Solution:
  Minimum tap ampacity = 1000A / 10 = 100A

  Select: #1 AWG copper (110A @ 75°C) for outdoor run
  Terminate in: 110A OCPD at detached building

  ✓ Meets outside tap rule (no length limit outdoors)
```

**Diagram**:
```
Main Building                           Detached Building
Feeder (1000A)
   │
   └──[Outside tap - No OCPD]
         │
         │ <── 300 ft, #1 AWG (110A), outdoor
         │
         └─────────────────────────────>[110A OCPD]
                                            │
                                         [80A load]
```

### 240.22 Grounded Conductor (Neutral)

**No OCPD in grounded conductor** except:
- Where simultaneous opening of all ungrounded conductors occurs (e.g., 2-pole breaker)

**Rationale**: Opening only the neutral creates shock hazard (equipment remains energized through ground path).

### 240.23 Change in Size of Grounded Conductor (Neutral)

If neutral size changes (reduced), provide OCPD at the point of reduction.

### 240.24 Location in or on Premises

#### 240.24(A) Accessibility

**OCPDs shall be readily accessible** unless:
- Supplementary overcurrent protection
- For busway (see 368.17)
- Service overcurrent protection (see 230.92)

**Readily accessible**: Capable of being reached without climbing over or removing obstacles, or using portable ladders.

#### 240.24(B) Occupant Access to Overcurrent Protective Devices

For guest rooms, guest suites, and dormitory units:
- Occupants shall have ready access to OCPDs
- Exception: Central panelboard accessible to building management

#### 240.24(C) Not Exposed to Physical Damage

OCPDs shall not be located where exposed to physical damage.

#### 240.24(D) Not in Vicinity of Easily Ignitable Material

OCPDs shall not be located near easily ignitable materials (e.g., clothes closets).

#### 240.24(E) Not Located in Bathrooms

OCPDs (panelboards) shall not be located in bathrooms in dwelling units, guest rooms, or dormitories.

**Exception**: Supplementary overcurrent protection.

---

## Part III - Enclosures (240.30-240.33)

### 240.30 General

**OCPD enclosures** (panelboards, switchboards):
- Type based on installation location (indoor, outdoor, wet, hazardous)
- NEMA ratings or IEC IP codes

### 240.32 Damp or Wet Locations

**Enclosures in damp/wet locations**:
- Weatherproof (NEMA 3R, 4, 4X)
- Mounted to prevent moisture entry
- Minimum 6 mm (1/4 inch) airspace between enclosure and mounting surface

### 240.33 Vertical Position

**Enclosure mounting**:
- Mounted in vertical position unless specifically listed otherwise
- Handles operate vertically (up = OFF, down = ON)

---

## Part IV - Disconnecting Means (240.40-240.41)

### 240.40 Disconnecting Means for Fuses

**Cartridge fuses in circuits over 150V-to-ground**:
- Disconnecting means required on supply side
- Accessible to each occupant

### 240.41 Arcing or Suddenly Moving Parts

**OCPD enclosures**:
- Designed to minimize injury from arcing or suddenly moving parts
- Arc flash labels required per 110.16

---

## Part V - Plug Fuses, Fuseholders, and Adapters (240.50-240.54)

### 240.50 General

**Plug fuses** (Edison base and Type S):
- 125V or less
- 30A or less
- Residential applications

### 240.51 Edison-Base Fuses

**Edison-base fuses**:
- Maximum 125V, 30A
- Used only as replacements in existing installations

**Limitation**: Not permitted for new installations (Type S required for new work).

### 240.53 Type S Fuses

**Type S fuses**:
- Specific fuseholder configuration prevents overfusing
- Classification: 0-15A, 16-20A, 21-30A
- Required for all new 125V plug fuse installations

### 240.54 Type S Fuses, Adapters, and Fuseholders

**Adapters**:
- Once installed in Edison-base fuseholder, cannot be removed
- Prevents installation of larger fuse

---

## Part VI - Cartridge Fuses and Fuseholders (240.60-240.61)

### 240.60 General

**Cartridge fuses**:
- All voltages (common: 250V, 600V)
- All current ratings (10A to 6000A+)
- Commercial and industrial applications

**Classes**:
- **Class RK1/RK5**: 250V/600V, current-limiting, time-delay available
- **Class J**: 600V, current-limiting, 200kA interrupting rating
- **Class L**: 600V, current-limiting, 601A to 6000A
- **Class T**: 300V/600V, very fast-acting, space-saving

### 240.61 Classification

**Interrupting rating**:
- Must equal or exceed available fault current
- Common ratings: 10kA, 20kA, 50kA, 100kA, 200kA

---

## Part VII - Circuit Breakers (240.80-240.87)

### 240.80 Method of Operation

**Circuit breakers**:
- Capable of being opened and closed by hand
- Trip-free: Cannot be held closed against internal trip mechanism

### 240.81 Indicating

**Position indication**:
- Indicate whether ON or OFF
- Not required to indicate tripped position (but most do)

### 240.82 Nontamperable

**Circuit breaker trip settings**:
- Shall not be adjustable except by qualified persons with tools
- Electronic trip settings require password or key

### 240.83 Marking

**Circuit breaker nameplate** shall include:
- Voltage rating
- Current rating
- Interrupting rating (if other than 5000A)
- Manufacturer name or trademark

#### 240.83(C) Interrupting Rating

**Interrupting rating (AIR = Ampere Interrupting Rating)**:
- Current breaker can safely interrupt without damage
- Minimum: 5,000A (if not marked)
- Higher ratings: 10kA, 14kA, 18kA, 22kA, 25kA, 35kA, 42kA, 65kA, 100kA, 200kA

**Example - Available Fault Current Check**:
```
Given:
  - Service entrance: 480V/3-phase
  - Utility transformer: 2500 kVA, 5.75% impedance, 200 feet from service
  - Calculated available fault current: 28,000A

Question: What minimum interrupting rating (AIR) is required for main breaker?

Solution:
  Available fault = 28 kA
  Select breaker with AIR ≥ 28 kA
  Standard ratings: 25 kA (insufficient), 35 kA (adequate), 42 kA (adequate)

  Answer: Minimum 35 kA AIR circuit breaker required
```

### 240.85 Applications

**Circuit breakers rated 240V or less, 60A or less**:
- Permitted for line-to-neutral applications (120V) in multiwire circuits
- Must simultaneously disconnect all ungrounded conductors

**Circuit breakers rated 120/240V**:
- Permitted on 3-phase, 4-wire wye systems (208Y/120V, 480Y/277V) only if marked for such use

### 240.86 Series Ratings

**Series-rated systems**:
- Utilize higher interrupting rating of upstream OCPD to protect downstream lower-rated OCPD
- Must be selected under engineering supervision
- Requires legible marking on service equipment

**Fully-rated systems** (preferred):
- Each OCPD has interrupting rating ≥ available fault current at its location
- No coordination required between devices for interrupting duty

**Example - Series Rating**:
```
Configuration:
  Main breaker: 400A, 65 kA AIR
  Branch breaker: 100A, 10 kA AIR (series-rated with main)

Available fault at branch location: 18 kA

Explanation:
  - Branch breaker alone (10 kA AIR) cannot interrupt 18 kA fault
  - Main breaker (65 kA AIR) will help clear fault if branch attempts to interrupt
  - System tested and listed as series combination
  - Marking required: "Series Rated System - Max Fault ___ kA"

Limitation:
  - Specific manufacturer combinations only
  - Verification required (listing, testing)
  - May not provide selective coordination
```

### 240.87 Arc Energy Reduction

**Purpose**: Reduce arc flash incident energy for personnel safety.

**Methods** (one or more required for certain systems):

#### 240.87(B) Service Equipment

**Applicability**:
- Service equipment rated 1200A or more
- Applies to services installed after January 1, 2020 (check local adoption date)

**Compliance Options** (one required):
1. **Zone-selective interlocking (ZSI)**: Coordinates trip times between OCPDs
2. **Differential relaying**: Detects faults within protected zone
3. **Energy-reducing maintenance switch**: Reduces trip time during maintenance
4. **Energy-reducing active arc flash mitigation system**: Optical detection, rapid tripping
5. **Approved equivalent means**

**Example - Zone-Selective Interlocking**:
```
System:
  Main service breaker: 2000A, electronic trip
  Feeder breakers: 800A, electronic trip

ZSI Operation:
  1. Normal: All breakers set to long-time-delay (coordination)
  2. Downstream fault: Downstream breaker sees fault, sends "restraint" signal upstream
  3. Upstream breakers held in long-time-delay mode
  4. If downstream fails to clear: Upstream trips in short-time (backup)

Benefit:
  - Selective coordination maintained
  - Arc flash incident energy reduced (faster clearing on faults)
```

---

## Part VIII - Supervised Industrial Installations (240.90-240.92)

### 240.90 General

**Supervised industrial installations**:
- Conditions of maintenance and engineering supervision ensure qualified persons service equipment
- Allows certain relaxations (e.g., increased tap lengths)

### 240.92 Locked Rotor Current Protection

**Motor circuits in supervised industrial installations**:
- May use group motor protection instead of individual overload protection
- Requires engineering supervision

---

## Part IX - Overcurrent Protection Over 1000 Volts (240.100-240.101)

### 240.100 Feeders and Branch Circuits

**Medium voltage (MV) overcurrent protection**:
- Fuses or circuit breakers required
- Interrupting rating must exceed available fault current
- Coordination typically required

### 240.101 Additional Requirements for Feeders

**MV feeders**:
- Ground-fault indication or protection
- Arc flash labels (110.16)

---

## Design Scenarios and Examples

### Scenario 1: Panelboard Protection (Branch Circuit Design)

**Given**:
- 120V/1-phase panelboard
- 12 AWG copper branch circuits
- Continuous lighting loads
- Non-continuous receptacle loads

**Question**: What OCPD ratings are permitted for branch circuits?

**Solution**:

**Per 240.4(D)**:
- 12 AWG copper maximum OCPD = 20A

**Continuous loads** (per 210.19(A)(1)):
- Circuit breaker rated ≥ 125% × continuous load
- Example: 15A continuous load requires 15A × 1.25 = 18.75A → 20A OCPD

**Non-continuous loads**:
- Circuit breaker rated ≥ 100% × non-continuous load
- Example: 16A non-continuous load requires 16A OCPD → 20A OCPD

**Summary**:
```
12 AWG copper branch circuits:
  - 15A or 20A circuit breakers permitted (240.4(D) limit)
  - Cannot use 25A or 30A (exceeds 240.4(D) maximum for 12 AWG)
```

---

### Scenario 2: Feeder Tap Design (10-Foot Tap Rule)

**Given**:
- Main feeder: 600A circuit breaker protecting 3x500 kcmil conductors (380A each × 3 = 1140A)
- Need to tap feeder for subpanel 8 feet away
- Subpanel load: 150A calculated demand
- Tap conductors: THHN/THWN in EMT

**Question**: What is the minimum tap conductor size using 10-foot tap rule (240.21(B)(1))?

**Solution**:

**10-foot tap requirements**:
1. Length ≤ 10 feet: ✓ (8 feet)
2. Tap ampacity ≥ combined load: 150A
3. Tap ampacity ≥ 10% feeder OCPD: 600A × 10% = 60A
4. Enclosed in raceway: ✓ (EMT)
5. Terminates in OCPD ≤ tap conductor ampacity

**Minimum tap ampacity** = MAX(150A, 60A) = 150A

**Select conductor** (Table 310.16, THHN, 75°C):
- #1/0 AWG copper: 150A ✓

**Subpanel main breaker**:
- 150A breaker (matches tap conductor ampacity)

**Result**:
```
Feeder (600A) ──┐
                 │
                 └─[Tap: #1/0 AWG (150A), 8 ft in EMT]─[150A OCPD Subpanel]
```

---

### Scenario 3: Transformer Secondary Protection

**Given**:
- 112.5 kVA transformer, 480V delta primary, 208Y/120V secondary
- Primary OCPD: 150A fuses
- Secondary conductors: #3/0 AWG copper (200A @ 75°C)
- Conductor length: 12 feet to main distribution panel (MDP)

**Question**: Is secondary OCPD required at transformer? Can we use 25-foot tap rule?

**Solution**:

**Transformer secondary current**:
```
I_secondary = 112,500 VA / (√3 × 208V) = 312A
```

**Option 1 - OCPD at transformer** (standard):
- Install 300A or 350A circuit breaker at transformer secondary
- Conductors #3/0 (200A) are undersized for 312A load
- Need larger: 500 kcmil (380A @ 75°C)

**Option 2 - Use 25-foot tap rule** (240.21(C)(6)):
- Transformer secondary conductors may be tapped per 240.21(C)(6)
- Requirements:
  1. Conductors have ampacity ≥ secondary current: #3/0 (200A) < 312A → ✗
  2. Length ≤ 25 feet: 12 feet → ✓
  3. Terminate in single OCPD

**Correction**: #3/0 is insufficient. Recalculate:

**Use 240.21(C)(2) - Transformer Secondary Conductors, Not Over 10 Feet Long**:
- Length ≤ 10 feet: 12 feet → ✗ (cannot use 10-foot rule)

**Use 240.21(C)(6) - 25-Foot Transformer Secondary Tap**:
- Conductor ampacity ≥ 1/3 × (primary OCPD × transformer ratio)
  - Primary OCPD = 150A at 480V
  - Transformer ratio = 480V / 208V = 2.31
  - Required secondary ampacity = (150A × 2.31) / 3 = 115A
- #3/0 (200A) > 115A → ✓
- Length ≤ 25 feet: 12 feet → ✓
- Terminates in OCPD ≤ conductor ampacity: Need 200A MDP main breaker

**Result**:
```
Transformer 112.5 kVA
  Primary: 150A fuses
  Secondary: [No OCPD at transformer]
             │
             └─[#3/0 AWG (200A), 12 ft]─[200A Main Breaker at MDP]

Using 240.21(C)(6) - 25-foot transformer secondary tap rule
```

---

### Scenario 4: Outside Feeder Tap (Detached Building)

**Given**:
- Main building: 1200A service
- Detached garage: 80A load, 250 feet away
- Outdoor feeder in PVC conduit underground

**Question**: What is the minimum feeder conductor size using outside tap rule (240.21(B)(5))?

**Solution**:

**Outside tap rule** (240.21(B)(5)):
- Outdoor portion: No length limit
- Conductor ampacity ≥ feeder OCPD / 10
- Minimum ampacity = 1200A / 10 = 120A

**Select conductor** (Table 310.16, THWN, 75°C):
- #1 AWG copper: 110A → Insufficient
- #1/0 AWG copper: 150A → ✓

**Termination OCPD**:
- 150A breaker at garage (or smaller, down to 100A for 80A load)

**Result**:
```
Main Building (1200A)
   │
   └─[Outside tap: #1/0 AWG (150A), 250 ft underground]
         │
         └─[Garage: 100A or 150A OCPD for 80A load]
```

---

### Scenario 5: Motor Circuit Protection

**Given**:
- 25 HP, 460V, 3-phase motor
- Full-load current (FLC) from Table 430.250: 34A
- Inverse-time circuit breaker for branch circuit protection

**Question**: What is the maximum OCPD size for motor branch circuit?

**Solution**:

**Per Article 430** (not 240):
- Motor branch circuit protection: 250% FLC maximum for inverse-time breaker
- If 250% rating doesn't correspond to standard size, next higher permitted

**Calculation**:
```
Maximum OCPD = 34A × 250% = 85A

Standard sizes (240.6): 70A, 80A, 90A, 100A
Next size up from 85A = 90A

Maximum motor branch circuit OCPD = 90A
```

**Note**: Motor overload protection is separate (typically 115-125% FLC).

---

## Circuit Breakers vs. Fuses Selection Guide

### Comparison Table

```
┌────────────────────────┬─────────────────────────┬─────────────────────────┐
│ Feature                │ Circuit Breakers        │ Fuses                   │
├────────────────────────┼─────────────────────────┼─────────────────────────┤
│ Resettable             │ Yes (mechanical reset)  │ No (replace after blow) │
│ Initial cost           │ Higher                  │ Lower                   │
│ Maintenance cost       │ Lower (reset, no parts) │ Higher (replacement)    │
│ Interrupting rating    │ 10kA-200kA typical      │ Up to 300kA (Class J/L) │
│ Current limiting       │ Some models             │ Yes (most types)        │
│ Let-through energy     │ Higher (most types)     │ Lower (I²t reduction)   │
│ Response time          │ Slower (thermal-mag)    │ Faster (for faults)     │
│ Overload protection    │ Adjustable curves       │ Fixed time-current      │
│ Visual indication      │ Trip position visible   │ Fuse element visible    │
│ Selectivity            │ Coordination required   │ Easier to coordinate    │
│ Arc flash energy       │ Higher (typically)      │ Lower (fast clearing)   │
│ Size/space             │ Larger                  │ Smaller (esp. Class T)  │
│ Ambient sensitivity    │ Yes (thermal element)   │ Less sensitive          │
│ Tamper resistance      │ Moderate                │ High (proper holder)    │
└────────────────────────┴─────────────────────────┴─────────────────────────┘
```

### When to Use Circuit Breakers

**Best for**:
- Frequently operated circuits (manual switching)
- Motor circuits with adjustable trip (overload protection)
- Systems requiring easy reset (residential, light commercial)
- Locations with non-technical personnel
- Adjustable trip requirements (electronic trip units)
- GFCI/AFCI protection (built into breaker)

**Typical applications**:
- Residential panelboards
- Commercial lighting and receptacle panels
- Motor control centers (MCCs)
- Variable frequency drive (VFD) circuits

### When to Use Fuses

**Best for**:
- Maximum fault current interruption (>100kA)
- Current-limiting required (arc flash reduction)
- Minimum let-through energy (I²t)
- High-inrush loads (transformers, motors with time-delay fuses)
- Space-constrained installations (Class T)
- Predictable coordination (time-current curves)

**Typical applications**:
- Service entrance protection (high fault currents)
- Transformer primary protection
- Medium voltage (MV) circuits
- Industrial switchgear
- High available fault current locations (near utility source)

---

## Selective Coordination

### Definition (NEC 240.12)

**Selective coordination**: Localization of an overcurrent condition to restrict outages to the circuit or equipment affected, accomplished by the selection and installation of overcurrent protective devices and their ratings or settings.

**Goal**: Minimize outage area - only the faulted circuit loses power, upstream loads remain energized.

### Required Systems (per 240.12)

Coordination required for:
- **Emergency systems** (700.28)
- **Legally required standby systems** (701.27)
- **Critical operations power systems (COPS)** (708.54)
- **Elevator circuits** (620.62)

### Time-Current Curves

**Coordination study uses time-current curves (TCCs)**:
- X-axis: Current (log scale, amperes)
- Y-axis: Time (log scale, seconds)
- Plot all OCPDs from source to load
- Verify upstream TCC does not overlap downstream TCC

**Example - Coordinated System**:
```
Main breaker: 800A, long-time-delay
  │
  ├─ Feeder breaker: 400A, long-time-delay
  │     │
  │     └─ Branch breaker: 100A, thermal-magnetic
  │
  └─ Feeder breaker: 200A, long-time-delay
```

**Time-Current Curve Sketch**:
```
Time (seconds)
  100 ─┐
       │    Main 800A (longest delay)
   10 ─┤  ╱
       │ ╱
    1 ─┤╱  Feeder 400A (medium delay)
       ╱│
  0.1 ╱─┤
     ╱  │   Branch 100A (fastest trip)
0.01 ───┴────────────────────────
     100  1000  10000  Current (A)

Key: Each curve is "below and to the right" of upstream device
     = selective coordination achieved
```

### Coordination Strategies

#### Strategy 1: Time Delays (Electronic Trip Units)

- **Long-time pickup (LTP)**: Overload protection (inverse-time)
- **Short-time pickup (STP)**: Short-circuit protection with intentional delay
- **Instantaneous pickup (I)**: Immediate trip for high faults

**Settings example**:
```
Main breaker (2000A frame):
  - LTP: 2000A at 150% in 20 seconds
  - STP: 8000A with 0.3 second delay
  - I: 16,000A instantaneous

Feeder breaker (800A frame):
  - LTP: 800A at 150% in 10 seconds
  - STP: 3200A with 0.1 second delay
  - I: 6,400A instantaneous

Branch breaker (400A frame):
  - LTP: 400A at 125% in 5 seconds
  - STP: OFF (or very short 0.05s)
  - I: 3,200A instantaneous

Result: Coordination achieved by time delay separation
```

#### Strategy 2: Current-Limiting Devices

**Current-limiting fuses or breakers**:
- Reduce peak let-through current
- Enable coordination with downstream devices
- Lower arc flash incident energy

**Example**:
```
Service entrance: Class L fuses, 1200A, 200kA AIR, current-limiting
Feeder: Standard molded-case breakers, 400A, 22kA AIR

Coordination:
  - Class L fuses limit fault current seen by feeder breakers
  - Even high-fault locations protected
  - Fuses clear before downstream breakers see full fault
```

#### Strategy 3: Zone-Selective Interlocking (ZSI)

**How ZSI works**:
1. Downstream breaker detects fault, sends "blocking" signal upstream
2. Upstream breakers remain in long-time-delay mode (do not trip)
3. If downstream fails to clear (300-500ms timeout), upstream trips

**Benefits**:
- Coordination maintained
- Faster fault clearing (arc flash reduction per 240.87)
- No sacrifice of protection

---

## Integration with QA/QC Rules

### QA Rules for Overcurrent Protection (QA-301-ELEC through QA-314-ELEC)

#### QA-301-ELEC: OCPD Rating Matches Conductor Ampacity

**Rule Definition**:
```yaml
- id: QA-301-ELEC
  description: Verify OCPD rating ≤ conductor ampacity per 240.4
  severity: critical
  category: compliance
  check:
    type: custom
    function: validate_ocpd_conductor_sizing
```

**Validation Logic**:
```python
def validate_ocpd_conductor_sizing(circuit_schedule):
    conductor_size = circuit_schedule.get("conductor_size")
    conductor_ampacity = circuit_schedule.get("conductor_ampacity")  # After adjustments
    ocpd_rating = circuit_schedule.get("ocpd_rating")

    # 240.4(B) - Next size up rule (if ≤ 800A)
    if ocpd_rating <= 800 and conductor_ampacity not in STANDARD_OCPD_SIZES:
        next_size_up = next((s for s in STANDARD_OCPD_SIZES if s >= conductor_ampacity), None)
        if ocpd_rating == next_size_up:
            return {"status": "PASS", "message": "Next size up rule (240.4(B)) applied correctly"}

    # Standard check
    if ocpd_rating > conductor_ampacity:
        return {
            "status": "FAIL",
            "message": f"OCPD rating {ocpd_rating}A exceeds conductor ampacity {conductor_ampacity}A"
        }

    return {"status": "PASS"}
```

**NEC Reference**: 240.4

---

#### QA-302-ELEC: Small Conductor Protection (240.4(D))

**Rule Definition**:
```yaml
- id: QA-302-ELEC
  description: Verify small conductors (#14, #12 AWG) protected per 240.4(D) maximum ratings
  severity: critical
  category: compliance
  check:
    type: custom
    function: validate_small_conductor_ocpd
```

**Validation Logic**:
```python
def validate_small_conductor_ocpd(circuit_schedule):
    conductor_size = circuit_schedule.get("conductor_size")
    conductor_material = circuit_schedule.get("conductor_material", "copper")
    ocpd_rating = circuit_schedule.get("ocpd_rating")

    # Table 240.4(D) maximum OCPD ratings
    max_ocpd_table = {
        ("copper", "14 AWG"): 15,
        ("copper", "12 AWG"): 20,
        ("copper", "10 AWG"): 30,
        ("aluminum", "12 AWG"): 15,
        ("aluminum", "10 AWG"): 25,
    }

    key = (conductor_material.lower(), conductor_size)
    max_ocpd = max_ocpd_table.get(key)

    if max_ocpd and ocpd_rating > max_ocpd:
        return {
            "status": "FAIL",
            "message": f"{conductor_size} {conductor_material} maximum OCPD is {max_ocpd}A "
                      f"per 240.4(D), but {ocpd_rating}A is specified"
        }

    return {"status": "PASS"}
```

**NEC Reference**: 240.4(D)

---

#### QA-303-ELEC: Standard OCPD Ratings (240.6)

**Rule Definition**:
```yaml
- id: QA-303-ELEC
  description: Verify OCPD rating is a standard size per 240.6(A)
  severity: high
  category: compliance
  check:
    type: enumeration
    field: circuit_schedule.ocpd_rating
    allowed_values: [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100,
                     110, 125, 150, 175, 200, 225, 250, 300, 350, 400,
                     450, 500, 600, 700, 800, 1000, 1200, 1600, 2000,
                     2500, 3000, 4000, 5000, 6000]
```

**NEC Reference**: 240.6(A)

---

#### QA-304-ELEC: Feeder Tap Rule Compliance (240.21)

**Rule Definition**:
```yaml
- id: QA-304-ELEC
  description: Verify feeder taps meet 10-ft, 25-ft, or outside tap rules per 240.21(B)
  severity: critical
  category: compliance
  check:
    type: custom
    function: validate_feeder_tap
```

**Validation Logic**:
```python
def validate_feeder_tap(feeder_schedule):
    is_tap = feeder_schedule.get("is_feeder_tap", False)
    if not is_tap:
        return {"status": "PASS", "message": "Not a feeder tap"}

    tap_length = feeder_schedule.get("tap_length_feet")
    tap_ampacity = feeder_schedule.get("tap_conductor_ampacity")
    feeder_ocpd = feeder_schedule.get("feeder_ocpd_rating")
    tap_location = feeder_schedule.get("tap_location", "indoor")  # indoor/outdoor

    # 10-foot tap rule
    if tap_length <= 10:
        min_ampacity = max(
            feeder_schedule.get("tap_load_amperes"),
            feeder_ocpd * 0.10
        )
        if tap_ampacity >= min_ampacity:
            return {
                "status": "PASS",
                "message": f"10-ft tap rule (240.21(B)(1)): {tap_ampacity}A ≥ {min_ampacity:.1f}A"
            }
        else:
            return {
                "status": "FAIL",
                "message": f"10-ft tap rule violation: {tap_ampacity}A < {min_ampacity:.1f}A required"
            }

    # 25-foot tap rule
    if tap_length <= 25:
        min_ampacity = feeder_ocpd / 3
        if tap_ampacity >= min_ampacity:
            return {
                "status": "PASS",
                "message": f"25-ft tap rule (240.21(B)(2)): {tap_ampacity}A ≥ {min_ampacity:.1f}A"
            }
        else:
            return {
                "status": "FAIL",
                "message": f"25-ft tap rule violation: {tap_ampacity}A < {min_ampacity:.1f}A required"
            }

    # Outside tap rule (unlimited length)
    if tap_location == "outdoor":
        min_ampacity = feeder_ocpd / 10
        if tap_ampacity >= min_ampacity:
            return {
                "status": "PASS",
                "message": f"Outside tap rule (240.21(B)(5)): {tap_ampacity}A ≥ {min_ampacity:.1f}A"
            }
        else:
            return {
                "status": "FAIL",
                "message": f"Outside tap rule violation: {tap_ampacity}A < {min_ampacity:.1f}A required"
            }

    return {
        "status": "FAIL",
        "message": f"Tap length {tap_length} ft exceeds 25 ft and is not outdoor (no tap rule applies)"
    }
```

**NEC Reference**: 240.21(B)

---

#### QA-305-ELEC through QA-314-ELEC: Additional OCPD Validations

Additional rules cover:

- **QA-305-ELEC**: Interrupting rating ≥ available fault current (240.86)
- **QA-306-ELEC**: Series-rated systems properly marked (240.86(B))
- **QA-307-ELEC**: Arc energy reduction compliance (240.87) for services ≥1200A
- **QA-308-ELEC**: Selective coordination for emergency/standby systems (240.12)
- **QA-309-ELEC**: Ground-fault protection for services >1000A (240.13, 230.95)
- **QA-310-ELEC**: OCPD accessible and not in bathrooms (240.24)
- **QA-311-ELEC**: No OCPD in grounded (neutral) conductor (240.22)
- **QA-312-ELEC**: Continuous load factor applied (125% for breakers per 210.20(A))
- **QA-313-ELEC**: Motor circuits sized per Article 430 (not Article 240)
- **QA-314-ELEC**: Panel schedule shows available fault current and AIR

---

## Quick Reference Tables

### Table 240.4(D) - Small Conductor Maximum OCPD

| Conductor Size | Copper Max OCPD | Aluminum Max OCPD |
|----------------|-----------------|-------------------|
| 14 AWG | 15A | - |
| 12 AWG | 20A | 15A |
| 10 AWG | 30A | 25A |

### Table 240.6(A) - Standard OCPD Ratings (Excerpt)

| Branch Circuits | Feeders/Services |
|-----------------|------------------|
| 15, 20, 25, 30 | 125, 150, 175, 200 |
| 35, 40, 45, 50 | 225, 250, 300, 350 |
| 60, 70, 80, 90 | 400, 450, 500, 600 |
| 100, 110 | 700, 800, 1000, 1200 |

### Table 240.21(B) - Feeder Tap Rules Summary

| Tap Type | Max Length | Min Ampacity | Termination | Protection |
|----------|------------|--------------|-------------|------------|
| 10-foot | 10 ft | MAX(load, feeder×10%) | Panelboard/switchboard | Enclosed raceway |
| 25-foot | 25 ft | Feeder OCPD / 3 | Single OCPD ≤ tap ampacity | From physical damage |
| Outside | Unlimited (outdoor) | Feeder OCPD / 10 | Single OCPD ≤ tap ampacity | Per 230.6 |

---

## Conclusion

NEC Article 240 provides critical requirements for overcurrent protection to ensure conductor and equipment safety. Key takeaways:

1. **Protection at the source**: OCPDs located where conductors receive supply (240.21)
2. **Conductor protection**: OCPD rating ≤ conductor ampacity (240.4)
3. **Small conductors**: Specific maximum ratings (14 AWG = 15A, 12 AWG = 20A)
4. **Feeder taps**: Three rules (10-ft, 25-ft, outside) allow taps without immediate OCPD
5. **Interrupting rating**: Must meet or exceed available fault current (240.83(C))
6. **Coordination**: Required for emergency, standby, COPS, and elevator systems (240.12)
7. **Arc flash reduction**: Services ≥1200A require arc energy reduction methods (240.87)
8. **Standard ratings**: Only standard OCPD sizes permitted (240.6)

Always coordinate with NEC Articles 210 (branch circuits), 215 (feeders), 230 (services), and 430 (motors) for complete system design.

---

**Document Version**: 1.0
**Last Updated**: 2025-01-22
**Next Review**: NEC 2026 edition adoption
**Maintained By**: EE_AI Platform - MEP Library Curation Team
