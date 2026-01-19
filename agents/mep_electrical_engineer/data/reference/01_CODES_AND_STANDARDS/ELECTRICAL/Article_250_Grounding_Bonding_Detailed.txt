# NEC 2023 Article 250 - Grounding and Bonding (DETAILED)

## Document Information

**NEC Article**: 250
**Title**: Grounding and Bonding
**Edition**: NFPA 70-2023 National Electrical Code
**Scope**: Requirements for grounding and bonding electrical systems, equipment, and surge protection
**Last Updated**: 2025-01-22
**Curator**: EE_AI Platform Reference Library

---

## Table of Contents

1. [Article Overview](#article-overview)
2. [Grounding vs. Bonding Clarification](#grounding-vs-bonding-clarification)
3. [Part I - General (250.1-250.12)](#part-i---general)
4. [Part II - System Grounding (250.20-250.36)](#part-ii---system-grounding)
5. [Part III - Grounding Electrode System (250.50-250.70)](#part-iii---grounding-electrode-system)
6. [Part IV - Enclosure, Raceway, and Service Cable Bonding (250.80-250.106)](#part-iv---bonding)
7. [Part V - Bonding (250.90-250.106)](#part-v---bonding-continued)
8. [Part VI - Equipment Grounding and Equipment Grounding Conductors (250.110-250.126)](#part-vi---equipment-grounding)
9. [Part VII - Methods of Equipment Grounding (250.130-250.148)](#part-vii---methods)
10. [Part VIII - Direct-Current Systems (250.160-250.169)](#part-viii---dc-systems)
11. [Sizing Examples](#sizing-examples)
12. [Special Grounding Applications](#special-grounding)
13. [Integration with QA/QC Rules](#integration-with-qaqc-rules)
14. [Quick Reference Tables](#quick-reference-tables)

---

## Article Overview

Article 250 establishes requirements for **grounding** (connecting to earth) and **bonding** (connecting metallic parts together) to:
1. **Limit voltage** to ground during normal operation
2. **Facilitate overcurrent device operation** during ground faults
3. **Limit voltage** imposed by lightning, line surges, or unintentional contact with higher voltage
4. **Stabilize voltage** to ground during normal operation
5. **Provide safe path** for fault current

**Fundamental Principle**: Create a low-impedance path for ground-fault current to flow back to the source, allowing overcurrent devices to operate quickly.

---

## Grounding vs. Bonding Clarification

### Grounding (Earthing)

**Definition**: Connection to earth through grounding electrodes.

**Purpose**:
- Voltage stabilization (reference to earth potential)
- Lightning surge dissipation
- Limit voltage during line-to-ground faults on utility system

**Key Components**:
- Grounding electrode conductor (GEC)
- Grounding electrodes (ground rods, water pipe, concrete-encased electrode)
- Main bonding jumper (connects grounded conductor to grounding system)

**Visual**:
```
Service Panel
   │
   ├─ Grounded (Neutral) Bus
   │     │
   │     └─[Main Bonding Jumper]───┐
   │                                │
   └─ Equipment Grounding Bus      │
         │                          │
         └─[Grounding Electrode     │
            Conductor (GEC)]────────┴─→ Earth (Grounding Electrodes)
```

### Bonding (Equipment Bonding)

**Definition**: Connection of metallic parts to ensure electrical continuity and capacity to conduct fault current.

**Purpose**:
- Provide low-impedance fault current path
- Ensure overcurrent device operates during ground fault
- Prevent voltage differences between metallic parts

**Key Components**:
- Equipment grounding conductor (EGC)
- Bonding jumpers (around reducing washers, flexible metal conduit, etc.)
- Equipment bonding jumpers (parallel path for fault current)

**Visual**:
```
Service Panel ─[EGC]─┬─ Receptacle (ground terminal)
                     ├─ Metal junction box
                     ├─ Metal raceway system
                     └─ Metal equipment enclosures

All bonded together for fault current path
```

### Critical Distinction

```
┌─────────────────────────────────────────────────────────────────────┐
│ GROUNDING = Connection to EARTH (stabilization, surge dissipation)  │
│ BONDING   = Connection of METAL PARTS (fault current path)          │
└─────────────────────────────────────────────────────────────────────┘
```

**Example**:
- **Grounding Electrode Conductor (GEC)**: Connects equipment grounding system to earth (grounding)
- **Equipment Grounding Conductor (EGC)**: Connects equipment metal parts to grounding system (bonding)
- **Main Bonding Jumper (MBJ)**: Connects neutral bus to equipment grounding bus at service (bonding + grounding connection)

---

## Part I - General (250.1-250.12)

### 250.1 Scope

Article 250 covers:
- Grounding of electrical systems (system grounding)
- Grounding of equipment (equipment grounding)
- Bonding of metallic parts

### 250.2 Definitions

**Bonding Jumper, Equipment**: Connection between two or more portions of equipment grounding conductor.

**Bonding Jumper, Main**: Connection between grounded circuit conductor (neutral) and equipment grounding conductor at service.

**Equipment Grounding Conductor (EGC)**: Conductive path(s) from equipment to system grounded conductor and/or grounding electrode conductor.

**Grounded Conductor**: System or circuit conductor intentionally grounded (neutral in most systems).

**Grounding Electrode Conductor (GEC)**: Conductor connecting system grounded conductor or equipment to grounding electrode(s).

**Grounding Electrode**: Conducting object establishing direct connection to earth (ground rods, water pipe, building steel, etc.).

### 250.4 General Requirements for Grounding and Bonding

#### 250.4(A) Grounded Systems (Most Common)

**(1) Electrical System Grounding**: Limit voltage to ground during normal operation and ground faults.

**(2) Grounding of Electrical Equipment**: Limit voltage on equipment from lightning, surges, or unintentional contact with higher voltage.

**(3) Bonding of Electrical Equipment**: Create low-impedance path for ground-fault current.

**(4) Bonding of Electrically Conductive Materials**: Limit voltage between conductive materials and equipment.

**(5) Effective Ground-Fault Current Path**: Permanently installed, low-impedance, capable of safely carrying fault current, facilitates overcurrent device operation.

**Key Concept**: Effective ground-fault current path has sufficiently low impedance to allow enough current to flow to trip the overcurrent device rapidly.

#### 250.4(B) Ungrounded Systems (Rare, Special Applications)

**(1) Grounding Electrical Equipment**: Same as grounded systems.

**(2) Bonding of Electrical Equipment**: Same as grounded systems.

**(3) Bonding of Electrically Conductive Materials**: Same as grounded systems.

**(4) Path for Fault Current**: Same requirements for low-impedance fault path.

### 250.6 Objectionable Current

**Grounding shall not create objectionable current**:
- Proper use of grounded conductor (no parallel paths)
- Isolated grounding receptacles when required
- No neutral-to-ground bonds except at service (or separately derived systems)

**Example of Objectionable Current**:
```
VIOLATION - Multiple Neutral-to-Ground Bonds:

Service Panel             Subpanel
  N-G Bond                  N-G Bond (WRONG!)
     │                         │
     │                         │
  Neutral return current flows through:
    1. Neutral conductor (intended path)
    2. Equipment grounding conductor (objectionable path)
    3. Metal conduit, building steel (objectionable path)

Result: Stray current, electromagnetic interference, tripped GFCIs
```

**Correct**:
- N-G bond at service only
- Neutral and ground isolated at subpanels

### 250.8 Connection of Grounding and Bonding Equipment

**Listed methods**:
- Listed pressure connectors
- Listed clamps
- Exothermic welding
- Machine screws engaging at least two threads
- Thread-forming machine screws

**Not permitted**:
- Sheet metal screws
- Connection depending solely on solder

### 250.10 Protection of Ground Clamps and Fittings

**Ground clamps and fittings** shall be protected from physical damage:
- In inaccessible locations or protected by metal, wood, or equivalent enclosure

### 250.12 Clean Surfaces

**Connection surfaces** shall be cleaned:
- Remove nonconductive coatings (paint, enamel, lacquer) at connection points
- Ensures low-impedance electrical connection

---

## Part II - System Grounding (250.20-250.36)

### 250.20 Alternating-Current Systems to Be Grounded

**Systems required to be grounded**:

**(B) Alternating-Current Systems of 50 Volts to 1000 Volts**:
- Systems with one conductor grounded (e.g., 120/240V single-phase, 208Y/120V three-phase wye)
- Where maximum voltage to ground on ungrounded conductors ≤ 150V

**Common grounded systems**:
- 120/240V single-phase (residential)
- 208Y/120V three-phase wye (commercial)
- 480Y/277V three-phase wye (commercial/industrial)

**Systems permitted to be ungrounded** (with ground detectors):
- 240V delta, 480V delta (if no neutral required)

### 250.24 Grounding Service-Supplied Alternating-Current Systems

#### 250.24(A) System Grounding Connections

**Grounded conductor (neutral) brought to service** and connected to:
1. Grounding electrode conductor
2. Equipment grounding conductors (via main bonding jumper)

#### 250.24(B) Main Bonding Jumper

**Main bonding jumper (MBJ)** required at service:
- Connects grounded conductor (neutral) to equipment grounding conductor and service enclosure
- Sized per Table 250.66 or 250.102(C)

**Location**: Inside service equipment enclosure or meter socket.

**One location only**: Only one point of connection between grounded conductor and equipment grounding conductor (prevents objectionable current).

#### 250.24(C) Grounded Conductor (Neutral) Brought to Service Equipment

**Grounded conductor** shall:
- Be routed with ungrounded conductors
- Not be smaller than required by 220.61 (neutral load)
- Not be smaller than minimum size per Table 250.66 for GEC (if serving as GEC function)

### 250.26 Conductor to Be Grounded - Alternating-Current Systems

**System conductor to ground**:
- Single-phase, 2-wire: One conductor
- Single-phase, 3-wire: Neutral conductor
- Three-phase, 4-wire wye: Neutral conductor

### 250.30 Grounding Separately Derived Alternating-Current Systems

**Separately derived system** (e.g., transformer, generator with neutral):
- System with no direct electrical connection to supply conductors
- Requires its own grounding electrode system

**Requirements**:
1. **System bonding jumper (SBJ)**: Connect neutral to equipment grounding at first disconnect (like MBJ at service)
2. **Grounding electrode conductor**: Connect to grounding electrode
3. **Equipment grounding conductor**: Run with feeder to source

**Example - Transformer**:
```
Primary (480V, 3-phase) ──[Transformer]── Secondary (208Y/120V)
                                             │
                                  [System Bonding Jumper]
                                             │
                            Neutral ────────┴──── Equipment Ground Bus
                                │
                         [Grounding Electrode
                          Conductor (GEC)]
                                │
                         Grounding Electrodes
```

### 250.32 Buildings or Structures Supplied by a Feeder or Branch Circuit

**Separate building supplied from main building**:

**(A) Grounding Electrode**: Required at separate building.

**(B) Grounded Conductor (Neutral)**:
- **Option 1**: Run equipment grounding conductor with feeder, no neutral-to-ground bond at separate building (preferred)
- **Option 2**: Use grounded conductor (neutral) as equipment grounding conductor AND bond to grounding electrode at separate building (conditions apply, not recommended for new installations)

**Modern practice (post-2008 NEC)**:
- Always run equipment grounding conductor (EGC) with feeder
- Bond EGC to grounding electrode at separate building
- Do NOT bond neutral to ground at separate building

### 250.34 Portable and Vehicle-Mounted Generators

**Portable generators**:
- Frame serves as grounding electrode if generator supplies only equipment mounted on generator
- Grounding electrode required if supplying premises wiring

---

## Part III - Grounding Electrode System (250.50-250.70)

### 250.50 Grounding Electrode System

**All available grounding electrodes** at premises shall be bonded together:
1. Metal underground water pipe
2. Metal frame of building or structure
3. Concrete-encased electrode (Ufer ground)
4. Ground ring
5. Rod and pipe electrodes
6. Plate electrodes
7. Other listed electrodes

**Bonding creates "grounding electrode system"** (GES).

### 250.52 Grounding Electrodes

#### 250.52(A)(1) Metal Underground Water Pipe

**Requirements**:
- In direct contact with earth for at least 10 feet
- Bonding jumper around water meter required (interior metal water piping not isolated)
- **Must supplement** with additional electrode (cannot be sole electrode)

**Reason for supplement**: Water pipe can be isolated (plastic replacement pipe, meter removal, etc.).

#### 250.52(A)(2) Metal Frame of Building or Structure

**Requirements**:
- Building steel in direct contact with earth (10 feet minimum)
- Hold-down bolts securing structural steel to concrete footings (bonded to steel)

**Exception**: Structural steel encased in concrete isolated from earth.

#### 250.52(A)(3) Concrete-Encased Electrode (Ufer Ground)

**Requirements**:
- Minimum 20 feet of bare or zinc-galvanized steel rebar, minimum 1/2 inch diameter
- **OR** Minimum 20 feet of bare copper conductor, minimum 4 AWG
- Encased in at least 2 inches of concrete
- Located within and near bottom of concrete foundation or footing in direct contact with earth

**Most effective electrode** (low resistance to earth, large surface area).

**Common application**:
```
                 Foundation Footing
             ╔═══════════════════════╗
             ║                       ║
             ║  ┌─────────────────┐  ║
             ║  │ #4 Rebar (1/2")  │  ║ <── 20 ft minimum, encased 2" concrete
             ║  └─────────────────┘  ║
             ║                       ║
             ╚═══════════════════════╝
                       Earth

GEC connection: Rebar extended up to service location or bonded to accessible rebar
```

#### 250.52(A)(4) Ground Ring

**Requirements**:
- Minimum 20 feet of bare copper conductor, minimum 2 AWG
- Encircling building or structure
- Buried at least 30 inches below grade

#### 250.52(A)(5) Rod and Pipe Electrodes (Ground Rods)

**Requirements**:
- **Rod**: Minimum 5/8 inch diameter, unless listed
- **Pipe**: Minimum 3/4 inch trade size
- Minimum 8 feet length
- Driven vertically (unless rock bottom encountered, then 45° angle)

**Installation**:
```
Grade Level ──────────────────────
              │
              │ Ground Rod
              │ (5/8" × 8 ft min)
              │
              │
              │
              │
              ↓
           8 ft minimum
```

**(2) Supplemental Electrode Required**: If single rod resistance > 25 ohms, second rod required.

**Spacing**: Rods spaced at least 6 feet apart.

**Testing**: Not required if two rods installed (deemed to meet < 25 ohm requirement).

#### 250.52(A)(6) Plate Electrodes

**Requirements**:
- Minimum 2 square feet surface area exposed to soil
- Iron/steel plates: Minimum 1/4 inch thickness
- Nonferrous (copper) plates: Minimum 0.06 inch thickness

#### 250.52(B) Electrodes Not Permitted

**Not permitted as grounding electrodes**:
- Metal underground gas piping
- Aluminum electrodes

### 250.53 Grounding Electrode System Installation

#### 250.53(A)(2) Supplemental Electrode Required

**Metal underground water pipe** shall be supplemented by additional electrode:
- Rod, pipe, plate
- Building steel
- Concrete-encased electrode

#### 250.53(D) Metal Underground Water Pipe

**Bonding**:
- GEC connection to water pipe within 5 feet of entry to building
- Bonding jumper around water meter and isolating joints (maintain continuity)

**Interior metal water piping** located more than 5 feet from building entry point may be used for bonding (but not primary GEC connection point).

#### 250.53(E) Supplemental Electrode Bonding

**Supplemental electrode bonding jumper**:
- Size per 250.66 (for single electrode) or 250.53(C) (for multiple electrodes)

### 250.66 Size of Grounding Electrode Conductor (GEC)

**Table 250.66** - Grounding Electrode Conductor for AC Systems

```
┌─────────────────────────────────────────────────┬─────────────────────────┐
│ Size of Largest Ungrounded Service-Entrance    │ Size of Grounding       │
│ Conductor or Equivalent Area for Parallel      │ Electrode Conductor     │
│ Conductors (AWG/kcmil)                          │ (AWG/kcmil)             │
├─────────────────────────────────────────────────┼─────────────────────────┤
│ Copper     │ Aluminum or Copper-Clad Aluminum   │ Copper  │ Aluminum*     │
├────────────┼────────────────────────────────────┼─────────┼───────────────┤
│ 2 or smaller│ 1/0 or smaller                    │ 8       │ 6             │
│ 1 or 1/0    │ 2/0 or 3/0                        │ 6       │ 4             │
│ 2/0 or 3/0  │ 4/0 or 250                        │ 4       │ 2             │
│ Over 3/0    │ Over 250 through 500              │ 2       │ 1/0           │
│ through     │                                    │         │               │
│ 350         │                                    │         │               │
│ Over 350    │ Over 500 through 900              │ 1/0     │ 3/0           │
│ through     │                                    │         │               │
│ 600         │                                    │         │               │
│ Over 600    │ Over 900 through 1750             │ 2/0     │ 4/0           │
│ through     │                                    │         │               │
│ 1100        │                                    │         │               │
│ Over 1100   │ Over 1750                          │ 3/0     │ 250           │
└────────────┴────────────────────────────────────┴─────────┴───────────────┘

* Aluminum GEC not permitted in direct earth contact (250.64(A))
```

**How to use Table 250.66**:
1. Determine size of **largest ungrounded service conductor** (phase conductor)
2. For parallel conductors: Sum equivalent area (e.g., two 3/0 per phase = 3/0 + 3/0 = 373 kcmil equivalent)
3. Look up GEC size in table

**Example 1 - Residential 200A Service**:
```
Given:
  - Service: 200A, 120/240V single-phase
  - Service conductors: 2/0 AWG copper (195A @ 75°C)

Solution:
  Table 250.66, row "2/0 or 3/0 copper"
  GEC size: 4 AWG copper

Answer: Minimum 4 AWG copper grounding electrode conductor
```

**Example 2 - Commercial 800A Service with Parallel Conductors**:
```
Given:
  - Service: 800A, 208Y/120V three-phase
  - Service conductors: Two 500 kcmil copper per phase (2 × 380A = 760A)

Solution:
  Equivalent area: 2 × 500 kcmil = 1000 kcmil
  Table 250.66, row "Over 600 through 1100 copper"
  GEC size: 2/0 AWG copper

Answer: Minimum 2/0 AWG copper GEC
```

#### 250.66(A) Connections to Rod, Pipe, or Plate Electrodes

**Maximum size GEC to single ground rod**:
- Copper: 6 AWG
- Aluminum: 4 AWG

**Reason**: Diminishing returns (6 AWG sufficient for single rod resistance).

**Note**: If multiple rods or other electrodes in system, use Table 250.66 for sizing to electrode system (not limited to 6 AWG).

#### 250.66(B) Connections to Concrete-Encased Electrodes

**Maximum size GEC to concrete-encased electrode**:
- Copper: 4 AWG
- Aluminum: 2 AWG

#### 250.66(C) Connections to Ground Rings

**GEC to ground ring**: Not required to be larger than ground ring conductor (2 AWG minimum).

### 250.68 Grounding Electrode Conductor and Bonding Jumper Connection to Grounding Electrodes

#### 250.68(A) Accessibility

**GEC connections to electrodes**:
- Shall be accessible (except concrete-encased, buried, or driven electrodes)

#### 250.68(C) Continuous

**GEC** shall be:
- Installed in one continuous length without splice or joint
- **Exception**: Splicing by irreversible compression connectors or exothermic welding permitted

### 250.70 Methods of Grounding and Bonding Conductor Connection to Electrodes

**Permitted connection methods**:
- Listed clamps (grounding clamp)
- Exothermic welding
- Listed lugs
- Connections to building steel

**Acorn clamps** (one-time use, irreversible compression).

---

## Part IV - Enclosure, Raceway, and Service Cable Bonding (250.80-250.106)

### 250.80 Service Raceways and Enclosures

**Service equipment enclosures** shall be bonded to grounded conductor (neutral).

**Method**: Main bonding jumper (MBJ) at service equipment.

### 250.86 Other Conductor Enclosures and Raceways

**Metal enclosures and raceways** for other than service conductors shall be bonded to equipment grounding conductor.

---

## Part V - Bonding (250.90-250.106)

### 250.90 General

**Bonding ensures electrical continuity and conductivity**.

### 250.92 Services

#### 250.92(B) Method of Bonding at the Service

**Bonding at service** accomplished by:
- Bonding equipment to grounded conductor by main bonding jumper
- Connections using fittings listed for bonding
- Threadless couplings and connectors (if made up tight)
- Threaded connections
- Bonding jumpers

### 250.94 Bonding for Other Systems

**Intersystem bonding termination** (IBT):
- Accessible location for bonding communications, CATV, network, etc.
- Minimum 3 terminals
- Connected to service equipment enclosure, grounding electrode conductor, or grounding electrode

**Purpose**: Bonding point for other systems (phone, cable TV, internet, etc.) to electrical grounding system.

### 250.96 Bonding Other Enclosures

#### 250.96(A) General

**Metal raceways, boxes, enclosures** containing grounded conductors shall be bonded.

#### 250.96(B) Isolated Grounding Circuits

**Isolated ground (IG) receptacles**:
- Equipment grounding conductor run with circuit conductors
- Isolated from raceway and box (insulated connection to receptacle ground terminal only)
- Used to minimize electrical noise (sensitive electronic equipment)

**Application**:
```
Panelboard
   │
   ├─ Circuit conductors in metal conduit
   │     │
   │     └─ Insulated EGC (green, isolated from conduit)
   │             │
   │          [IG Receptacle] <── Orange triangle marking
   │             │
   │          Sensitive equipment (no ground loops through conduit)
```

### 250.97 Bonding for Over 250 Volts

**Systems over 250V to ground**:
- Additional bonding methods required (bonding jumpers around reducing washers, oversized knockouts, etc.)

### 250.102 Bonding Conductors and Jumpers

#### 250.102(C) Equipment Bonding Jumper - Supply Side of Service

**Supply-side bonding jumper**:
- Sized per Table 250.66 (same as GEC)

#### 250.102(D) Equipment Bonding Jumper - Load Side of Service

**Load-side bonding jumper**:
- Sized per Table 250.122 (same as EGC)

### 250.104 Bonding of Piping Systems and Exposed Structural Metal

#### 250.104(A) Metal Water Piping

**Interior metal water piping**:
- Bond to service equipment enclosure
- Bond to grounded conductor (neutral) at service
- Bond to grounding electrode conductor (if adequate size)
- Bond to grounding electrode

**Bonding jumper size**:
- Per Table 250.66 (based on service conductor size)

**Example**:
```
Service Equipment
   │
   └─[Bonding Jumper per Table 250.66]─→ Interior Metal Water Piping

Ensures water piping cannot become energized
```

#### 250.104(B) Other Metal Piping

**Other metal piping** (gas, air, etc.) likely to become energized:
- Bond to service equipment enclosure, grounded conductor, GEC, or grounding electrode
- Bonding conductor sized per Table 250.122 (based on circuit that may energize piping)

#### 250.104(C) Structural Metal

**Exposed structural metal** interconnected to form metal frame of building:
- Bond to service equipment enclosure, grounded conductor, or GEC

### 250.106 Lightning Protection Systems

**Lightning protection system grounding electrodes**:
- Bond to electrical grounding electrode system
- Bonding jumper minimum 6 AWG copper

**Purpose**: Equalize potential between systems during lightning strike.

---

## Part VI - Equipment Grounding and Equipment Grounding Conductors (250.110-250.126)

### 250.110 Equipment Fastened in Place (Fixed) or Connected by Permanent Wiring Methods

**Fixed equipment** requiring grounding:
- Equipment within 8 feet vertically or 5 feet horizontally of ground or grounded metal
- Equipment in wet or damp locations
- Equipment in hazardous (classified) locations
- Equipment supplied by metal-clad, metal-sheathed, or metal-raceway wiring

### 250.112 Specific Equipment Fastened in Place or Connected by Permanent Wiring Methods

**Equipment requiring grounding** (partial list):
- Refrigerators, freezers, air conditioners
- Motor-operated appliances
- Motor-operated tools
- Lighting fixtures in wet locations or within reach of grounded surfaces

### 250.114 Cord-and-Plug-Connected Equipment

**Cord-and-plug equipment requiring grounding**:
- Equipment in hazardous locations
- Equipment over 150V to ground (except motors and appliances)
- Hand-held motor-operated tools
- Appliances in wet or damp locations

### 250.118 Types of Equipment Grounding Conductors

**Acceptable equipment grounding conductors**:
1. Copper, aluminum, or copper-clad aluminum conductor
2. Rigid metal conduit (RMC)
3. Intermediate metal conduit (IMC)
4. Electrical metallic tubing (EMT)
5. Flexible metal conduit (FMC) under certain conditions
6. Armor of Type MC cable (listed for grounding)
7. Copper sheath of mineral-insulated cable
8. Other listed equipment

**Conditions for FMC as EGC** (250.118(5)):
- Listed for grounding
- Circuit overcurrent protection ≤ 20A
- Combined length ≤ 6 feet
- (Otherwise, install EGC inside FMC)

### 250.119 Identification of Equipment Grounding Conductors

**Color coding**:
- Green
- Green with one or more yellow stripes
- Bare (uninsulated) conductor

**Re-identification permitted** (for conductors larger than 6 AWG):
- Green tape or green label at terminations

### 250.122 Size of Equipment Grounding Conductors

**Table 250.122** - Minimum Size Equipment Grounding Conductors for Grounding Raceway and Equipment

```
┌─────────────────────────────────────────────────┬─────────────────────────┐
│ Rating or Setting of Automatic Overcurrent      │ Size (AWG or kcmil)     │
│ Device in Circuit Ahead of Equipment,           │                         │
│ Conduit, etc., Not Exceeding (Amperes)          │                         │
├─────────────────────────────────────────────────┼─────────────────────────┤
│                                                  │ Copper    │ Aluminum*   │
├──────────────────────────────────────────────────┼───────────┼─────────────┤
│ 15                                               │ 14        │ 12          │
│ 20                                               │ 12        │ 10          │
│ 30                                               │ 10        │ 8           │
│ 40                                               │ 10        │ 8           │
│ 60                                               │ 10        │ 8           │
│ 100                                              │ 8         │ 6           │
│ 200                                              │ 6         │ 4           │
│ 300                                              │ 4         │ 2           │
│ 400                                              │ 3         │ 1           │
│ 500                                              │ 2         │ 1/0         │
│ 600                                              │ 1         │ 2/0         │
│ 800                                              │ 1/0       │ 3/0         │
│ 1000                                             │ 2/0       │ 4/0         │
│ 1200                                             │ 3/0       │ 250         │
│ 1600                                             │ 4/0       │ 350         │
│ 2000                                             │ 250       │ 400         │
│ 2500                                             │ 350       │ 600         │
│ 3000                                             │ 400       │ 600         │
│ 4000                                             │ 500       │ 750         │
│ 5000                                             │ 700       │ 1200        │
│ 6000                                             │ 800       │ 1200        │
└──────────────────────────────────────────────────┴───────────┴─────────────┘

* Aluminum EGC not common; check local requirements
```

**How to use Table 250.122**:
1. Determine **overcurrent device rating** protecting circuit
2. Look up minimum EGC size in table

**Example 1 - 20A Branch Circuit**:
```
Given:
  - 20A circuit breaker
  - 12 AWG copper circuit conductors

Solution:
  Table 250.122, 20A OCPD
  Minimum EGC: 12 AWG copper

Answer: 12 AWG copper EGC (matches circuit conductor size for 20A circuit)
```

**Example 2 - 100A Feeder**:
```
Given:
  - 100A feeder breaker
  - #3 AWG copper feeder conductors (100A @ 75°C)

Solution:
  Table 250.122, 100A OCPD
  Minimum EGC: 8 AWG copper

Answer: 8 AWG copper EGC (run with feeder conductors)
```

**Example 3 - 400A Feeder**:
```
Given:
  - 400A feeder breaker
  - 500 kcmil copper feeder conductors

Solution:
  Table 250.122, 400A OCPD
  Minimum EGC: 3 AWG copper

Answer: 3 AWG copper EGC (much smaller than feeder conductors)
```

#### 250.122(B) Increased in Size

**If ungrounded conductors are increased** in size (voltage drop, future capacity, etc.):
- EGC must be increased proportionally

**Formula**:
```
EGC_new (circular mils) = EGC_table × (Conductor_actual / Conductor_minimum)
```

**Example - Voltage Drop Upsizing**:
```
Given:
  - 100A circuit, 200 feet length
  - Minimum conductors: #3 AWG (100A @ 75°C)
  - Upsized for voltage drop: #1 AWG
  - Minimum EGC per Table 250.122: 8 AWG (8,370 CM)

Solution:
  Conductor ratio = #1 AWG (83,690 CM) / #3 AWG (52,620 CM) = 1.59
  EGC upsized = 8 AWG (8,370 CM) × 1.59 = 13,308 CM
  Next standard size: 6 AWG (26,240 CM)

Answer: 6 AWG copper EGC (upsized from 8 AWG)
```

### 250.124 Equipment Grounding Conductor Continuity

#### 250.124(A) Separable Connections

**Connections shall be accessible** for inspection and testing (except for certain inaccessible locations).

#### 250.124(B) Switches

**No switching device in EGC path** (no disconnect in equipment grounding conductor).

### 250.126 Identification of Wiring Device Terminals

**Grounding terminal on receptacles**:
- Hexagonal (not interchangeable with neutral terminal)
- Green colored screw or connection point

---

## Part VII - Methods of Equipment Grounding (250.130-250.148)

### 250.130 Replacing Nongrounding-Type Receptacles

**Replacement options**:
1. Grounding-type receptacle if EGC present
2. GFCI-protected receptacle without EGC (label "No Equipment Ground")
3. Nongrounding-type receptacle (like-for-like replacement)

### 250.134 Equipment Fastened in Place or Connected by Permanent Wiring Methods - Grounding

**Methods of grounding fixed equipment**:
- Equipment grounding conductor (EGC)
- Metal raceway (if listed for grounding)
- Armor of Type MC cable (if listed for grounding)

### 250.138 Cord-and-Plug-Connected Equipment - Grounding

**Grounding for cord-and-plug equipment**:
- Equipment grounding conductor in cord (green wire)
- Connection to grounding terminal on attachment plug (3-prong plug)

### 250.146 Connecting Receptacle Grounding Terminal to Equipment Ground

**Methods**:
- Contact device between yoke and box (device-to-box bonding)
- Equipment bonding jumper from receptacle ground terminal to box
- Self-grounding receptacle (listed device with bonding clips)

### 250.148 Continuity and Attachment of Equipment Grounding Conductors to Boxes

**EGC connection to box**:
- EGC shall connect to metal box
- Splices in EGC permitted only with devices listed for grounding

---

## Part VIII - Direct-Current Systems (250.160-250.169)

### 250.162 Direct-Current Systems to Be Grounded

**DC systems required to be grounded**:
- 2-wire DC if one conductor grounded (per supply source)
- 3-wire DC system (neutral grounded)

### 250.166 Size of Direct-Current Grounding Electrode Conductor

**DC GEC sizing** per Table 250.166:

#### Table 250.166 - Grounding Electrode Conductor for DC Systems

```
┌─────────────────────────────────────────────────┬─────────────────────────┐
│ Size of Largest Conductor or Equivalent         │ Size of Grounding       │
│ Area for Parallel Conductors (AWG/kcmil)        │ Electrode Conductor     │
├─────────────────────────────────────────────────┼─────────────────────────┤
│ Copper     │ Aluminum or Copper-Clad Aluminum   │ Copper  │ Aluminum*     │
├────────────┼────────────────────────────────────┼─────────┼───────────────┤
│ 8 or smaller│ 6 or smaller                      │ 8       │ 6             │
│ 6 or 4      │ 4 or 2                            │ 6       │ 4             │
│ 3 or 2      │ 1 or 1/0                          │ 4       │ 2             │
│ 1 or 1/0    │ 2/0 or 3/0                        │ 2       │ 1/0           │
│ Over 1/0    │ Over 3/0                           │ 1/0     │ 3/0           │
│ through 350 │ through 500                        │         │               │
│ Over 350    │ Over 500 through 900               │ 2/0     │ 4/0           │
│ through 600 │                                    │         │               │
│ Over 600    │ Over 900 through 1750              │ 3/0     │ 250           │
│ through     │                                    │         │               │
│ 1100        │                                    │         │               │
│ Over 1100   │ Over 1750                          │ 4/0     │ 350           │
└────────────┴────────────────────────────────────┴─────────┴───────────────┘
```

**Application**: Solar PV systems, battery energy storage systems (BESS), DC microgrids.

---

## Sizing Examples

### Example 1: Residential 200A Service Grounding

**Given**:
- 200A service, 120/240V single-phase
- Service conductors: 2/0 AWG copper
- Metal underground water pipe (10+ feet)
- Two ground rods (5/8" × 8 ft)
- Concrete-encased electrode (#4 rebar in foundation)

**Grounding Electrode System**:
- Water pipe + ground rods + Ufer ground = grounding electrode system
- All bonded together

**GEC Sizing** (Table 250.66):
```
Service conductors: 2/0 AWG copper
Table 250.66 → GEC = 4 AWG copper
```

**Installation**:
```
Service Panel (200A)
   │
   ├─ Main Bonding Jumper (connects neutral to ground bus)
   │
   └─ 4 AWG Copper GEC ──┬─→ Water Pipe (within 5 ft of entry)
                         ├─→ Ground Rod #1 (5/8" × 8 ft)
                         ├─→ Ground Rod #2 (5/8" × 8 ft, 6 ft away)
                         └─→ Ufer Ground (#4 rebar in footing)
```

**Note**: GEC to single ground rod could be 6 AWG per 250.66(A), but 4 AWG required for connection to full electrode system.

---

### Example 2: Commercial 800A Service with Parallel Conductors

**Given**:
- 800A service, 208Y/120V three-phase
- Service conductors: Two 500 kcmil copper per phase (parallel)
- Building steel (structural steel in contact with earth)
- Ground ring (2 AWG bare copper, 30" deep, encircling building)

**GEC Sizing** (Table 250.66):
```
Equivalent conductor area: 2 × 500 kcmil = 1000 kcmil
Table 250.66, "Over 600 through 1100 copper" → GEC = 2/0 AWG copper
```

**Grounding Electrode System**:
- Building steel + ground ring = grounding electrode system

**Installation**:
```
Service Equipment (800A)
   │
   ├─ Main Bonding Jumper
   │
   └─ 2/0 AWG Copper GEC ──┬─→ Building Steel (bonded to structural steel)
                           └─→ Ground Ring (2 AWG, 30" deep)
```

---

### Example 3: Feeder to Subpanel (Equipment Grounding)

**Given**:
- 100A feeder breaker in main panel
- Subpanel: 100A main breaker, 200 feet away
- Feeder conductors: #3 AWG copper (upsized from #2 for voltage drop)
- Installation: EMT conduit

**EGC Sizing** (Table 250.122):
```
Feeder breaker: 100A
Table 250.122 → EGC = 8 AWG copper (minimum)

Check upsizing requirement (250.122(B)):
  Minimum conductors for 100A: #2 AWG (95A) → Use #1 AWG (110A)
  Actual conductors: #3 AWG (100A)
  Ratio: #3 / #1 = 52,620 CM / 83,690 CM = 0.63 (conductors not upsized)
  EGC remains: 8 AWG copper
```

**Installation**:
```
Main Panel (100A feeder breaker)
   │
   ├─ Phase conductors: #3 AWG copper (3 wires)
   ├─ Neutral: #3 AWG copper (insulated, not bonded to ground at subpanel)
   ├─ EGC: 8 AWG copper (green or bare)
   │
   └─[200 ft in EMT conduit]
         │
      Subpanel (100A main breaker)
         ├─ Neutral bus (isolated from ground bus)
         └─ Ground bus (bonded to enclosure, EGC connected here)
```

**Note**: EMT can serve as EGC per 250.118(4), but installing wire EGC recommended for reliability.

---

### Example 4: Separately Derived System (Transformer)

**Given**:
- 75 kVA transformer, 480V delta primary → 208Y/120V secondary
- Secondary conductors: #3 AWG copper (175A calculated load)
- Transformer located 150 feet from main service
- Structural steel available near transformer

**System Bonding Jumper (SBJ)** at transformer:
- Connects neutral to equipment grounding at transformer
- Sized per Table 250.102(C)(1) (derived from Table 250.66)

**SBJ Sizing**:
```
Secondary conductors: #3 AWG copper
Table 250.66, "2/0 or 3/0 copper" → SBJ = 4 AWG copper
(Use secondary conductor size to determine SBJ, not primary)
```

**Grounding Electrode Conductor (GEC)** at transformer:
```
GEC to nearest structural steel or grounding electrode
Sized per Table 250.66 → 4 AWG copper
```

**Installation**:
```
Transformer (75 kVA)
   Primary (480V) ──[Transformer]── Secondary (208Y/120V)
                                       │
                                    Neutral Bus
                                       │
                            [System Bonding Jumper (4 AWG)]
                                       │
                                  Ground Bus ─┬─ EGC (from primary source)
                                              │
                                              └─ GEC (4 AWG) → Structural Steel
```

**Key Point**: Separately derived system has its own grounding electrode connection (not shared with main service).

---

### Example 5: Solar PV System Grounding (DC System)

**Given**:
- 50 kW solar PV array
- DC conductors from array to inverter: #6 AWG copper (60A)
- Inverter located at main service area
- DC system grounding required

**DC GEC Sizing** (Table 250.166):
```
DC conductors: #6 AWG copper
Table 250.166, "6 or 4 copper" → DC GEC = 6 AWG copper
```

**Installation**:
```
PV Array
   │
   ├─ DC+ (#6 AWG)
   ├─ DC- (#6 AWG, grounded conductor)
   ├─ DC EGC (#10 AWG per 690.45)
   │
   └─[Combiner Box/DC Disconnect]
         │
      [DC GEC (6 AWG)] → Grounding Electrode (same as AC system per 690.47(C))
         │
      Inverter
         │
      AC Output → Main Service Panel
```

**NEC References**: Article 690 (Solar PV), 250.166 (DC GEC sizing)

---

## Special Grounding Applications

### Isolated Grounding (IG) Systems

**Purpose**: Reduce electrical noise for sensitive electronic equipment (computers, medical devices, instrumentation).

**Method**:
- Install insulated equipment grounding conductor (green or green/yellow)
- Isolate EGC from raceway, boxes, and enclosures (except at panelboard)
- Connect EGC directly to isolated ground bus at panelboard or service
- IG receptacles marked with orange triangle

**Sizing**: Per Table 250.122 (same as standard EGC).

**Application**:
```
Panelboard
   ├─ Isolated Ground Bus (separate from enclosure)
   │     │
   │     └─[Insulated EGC, isolated from raceway]
   │             │
   │          IG Receptacle (orange △)
   │             │
   │          Computer equipment
   │
   └─ Regular Equipment Ground Bus (bonded to enclosure)
```

### Technical Power Systems (Article 647)

**Purpose**: 120V single-phase derived from 60V-60V split secondary (center-tapped, but center NOT grounded).

**Application**: Recording studios, broadcast facilities (eliminates ground loops).

**Grounding**:
- Derived neutral brought to premises but NOT grounded
- Equipment grounding conductor required
- GFPE (ground-fault protection of equipment) required

### Healthcare Facilities (Article 517)

**Isolated power systems**:
- Ungrounded electrical systems for operating rooms, critical care
- Line isolation monitor (LIM) detects ground faults without tripping
- Equipment grounding still required

**Grounding**:
- Equipment grounding per 250.118
- Redundant grounding (two EGCs in parallel for critical equipment)

---

## Integration with QA/QC Rules

### QA Rules for Grounding and Bonding (QA-401-ELEC through QA-412-ELEC)

#### QA-401-ELEC: Grounding Electrode Conductor Sized Correctly

**Rule Definition**:
```yaml
- id: QA-401-ELEC
  description: Verify GEC sized per Table 250.66 based on service conductor size
  severity: critical
  category: compliance
  check:
    type: custom
    function: validate_gec_sizing
```

**Validation Logic**:
```python
def validate_gec_sizing(service_schedule):
    service_conductor_size = service_schedule.get("service_conductor_size")
    service_conductor_material = service_schedule.get("conductor_material", "copper")
    gec_size = service_schedule.get("gec_size")
    gec_material = service_schedule.get("gec_material", "copper")

    # Table 250.66 lookup
    table_250_66 = {
        ("copper", "2 AWG or smaller"): {"copper": "8 AWG", "aluminum": "6 AWG"},
        ("copper", "1 AWG or 1/0 AWG"): {"copper": "6 AWG", "aluminum": "4 AWG"},
        ("copper", "2/0 or 3/0 AWG"): {"copper": "4 AWG", "aluminum": "2 AWG"},
        # ... complete table
    }

    # Determine service conductor category
    service_category = determine_conductor_category(service_conductor_size, service_conductor_material)
    required_gec = table_250_66.get((service_conductor_material, service_category), {}).get(gec_material)

    if gec_size_comparison(gec_size, required_gec) < 0:
        return {
            "status": "FAIL",
            "message": f"GEC {gec_size} is smaller than required {required_gec} per Table 250.66"
        }

    return {"status": "PASS"}
```

**NEC Reference**: 250.66, Table 250.66

---

#### QA-402-ELEC: Equipment Grounding Conductor Sized Correctly

**Rule Definition**:
```yaml
- id: QA-402-ELEC
  description: Verify EGC sized per Table 250.122 based on overcurrent device rating
  severity: critical
  category: compliance
  check:
    type: custom
    function: validate_egc_sizing
```

**Validation Logic**:
```python
def validate_egc_sizing(circuit_schedule):
    ocpd_rating = circuit_schedule.get("ocpd_rating")
    egc_size = circuit_schedule.get("egc_size")
    egc_material = circuit_schedule.get("egc_material", "copper")

    # Table 250.122 lookup
    table_250_122 = {
        15: {"copper": "14 AWG", "aluminum": "12 AWG"},
        20: {"copper": "12 AWG", "aluminum": "10 AWG"},
        30: {"copper": "10 AWG", "aluminum": "8 AWG"},
        40: {"copper": "10 AWG", "aluminum": "8 AWG"},
        60: {"copper": "10 AWG", "aluminum": "8 AWG"},
        100: {"copper": "8 AWG", "aluminum": "6 AWG"},
        200: {"copper": "6 AWG", "aluminum": "4 AWG"},
        # ... complete table
    }

    required_egc = table_250_122.get(ocpd_rating, {}).get(egc_material)

    if not required_egc:
        # OCPD not in table, interpolate or use next higher rating
        required_egc = interpolate_table_250_122(ocpd_rating, egc_material)

    if egc_size_comparison(egc_size, required_egc) < 0:
        return {
            "status": "FAIL",
            "message": f"EGC {egc_size} is smaller than required {required_egc} per Table 250.122"
        }

    return {"status": "PASS"}
```

**NEC Reference**: 250.122, Table 250.122

---

#### QA-403-ELEC: Main Bonding Jumper Present at Service

**Rule Definition**:
```yaml
- id: QA-403-ELEC
  description: Verify main bonding jumper present at service equipment per 250.24(B)
  severity: critical
  category: compliance
  check:
    type: field_presence
    field: service_equipment.main_bonding_jumper_present
    condition: equals true
```

**NEC Reference**: 250.24(B)

---

#### QA-404-ELEC: No Neutral-to-Ground Bond at Subpanels

**Rule Definition**:
```yaml
- id: QA-404-ELEC
  description: Verify subpanels do NOT have neutral-to-ground bond per 250.24(A)(5)
  severity: critical
  category: compliance
  check:
    type: custom
    function: validate_subpanel_neutral_isolation
```

**Validation Logic**:
```python
def validate_subpanel_neutral_isolation(panel_schedule):
    is_service_equipment = panel_schedule.get("is_service_equipment", False)
    neutral_ground_bonded = panel_schedule.get("neutral_ground_bonded", False)

    if not is_service_equipment and neutral_ground_bonded:
        return {
            "status": "FAIL",
            "message": "Subpanel has neutral-to-ground bond (violation of 250.24(A)(5)). "
                      "Only service equipment may have neutral-ground bond."
        }

    return {"status": "PASS"}
```

**NEC Reference**: 250.24(A)(5), 250.32(B)(1)

---

#### QA-405-ELEC through QA-412-ELEC: Additional Grounding Validations

Additional rules cover:

- **QA-405-ELEC**: Grounding electrode system includes all available electrodes (250.50)
- **QA-406-ELEC**: Metal water pipe supplemented by additional electrode (250.53(D)(2))
- **QA-407-ELEC**: Ground rods spaced minimum 6 feet apart (250.53(A)(3))
- **QA-408-ELEC**: Interior metal water piping bonded (250.104(A))
- **QA-409-ELEC**: EGC upsized proportionally when conductors upsized (250.122(B))
- **QA-410-ELEC**: Isolated grounding circuits properly installed (250.96(B), 250.146(D))
- **QA-411-ELEC**: Separately derived systems have system bonding jumper (250.30(A))
- **QA-412-ELEC**: DC systems (solar PV) have grounding electrode conductor (250.166)

---

## Quick Reference Tables

### Table 250.66 Summary (GEC Sizing)

| Service Conductor (Copper) | GEC (Copper) | GEC (Aluminum) |
|----------------------------|--------------|----------------|
| 2 AWG or smaller | 8 AWG | 6 AWG |
| 1 AWG or 1/0 AWG | 6 AWG | 4 AWG |
| 2/0 or 3/0 AWG | 4 AWG | 2 AWG |
| Over 3/0 through 350 kcmil | 2 AWG | 1/0 AWG |
| Over 350 through 600 kcmil | 1/0 AWG | 3/0 AWG |
| Over 600 through 1100 kcmil | 2/0 AWG | 4/0 AWG |

### Table 250.122 Summary (EGC Sizing)

| OCPD Rating | EGC (Copper) | EGC (Aluminum) |
|-------------|--------------|----------------|
| 15A | 14 AWG | 12 AWG |
| 20A | 12 AWG | 10 AWG |
| 30-60A | 10 AWG | 8 AWG |
| 100A | 8 AWG | 6 AWG |
| 200A | 6 AWG | 4 AWG |
| 300A | 4 AWG | 2 AWG |
| 400A | 3 AWG | 1 AWG |

### Grounding Electrode Types Summary

| Electrode Type | Minimum Size | Installation | Supplement Required? |
|----------------|--------------|--------------|----------------------|
| Metal water pipe | 10 ft in earth | Within 5 ft of entry | YES (always) |
| Building steel | 10 ft in earth | Contact with earth | No |
| Concrete-encased (Ufer) | #4 rebar or 4 AWG | 20 ft, 2" concrete | No |
| Ground ring | 2 AWG bare | 20 ft, 30" deep | No |
| Ground rods | 5/8" × 8 ft | Driven vertically | If >25Ω, add 2nd rod |

---

## Conclusion

NEC Article 250 provides comprehensive requirements for grounding and bonding to ensure safety and system reliability. Key takeaways:

1. **Grounding vs. Bonding**: Grounding = earth connection (stabilization); Bonding = metallic continuity (fault current path)
2. **GEC sizing**: Based on service conductor size (Table 250.66)
3. **EGC sizing**: Based on overcurrent device rating (Table 250.122)
4. **Grounding electrode system**: Bond all available electrodes (water pipe, building steel, Ufer, ground rods)
5. **One N-G bond**: Only at service equipment or separately derived systems (not at subpanels)
6. **Effective fault path**: Low-impedance path to ensure OCPD operates during ground fault
7. **Special systems**: Isolated grounding, technical power, healthcare facilities have additional requirements

Always coordinate with NEC Articles 210, 215, 230, 240, and 690 for complete electrical system grounding design.

---

**Document Version**: 1.0
**Last Updated**: 2025-01-22
**Next Review**: NEC 2026 edition adoption
**Maintained By**: EE_AI Platform - MEP Library Curation Team
