# Domestic Water Sizing Guide
## Comprehensive Plumbing Design Manual for Water Supply Systems

**Document Version**: 1.0
**Last Updated**: 2025-01-22
**Applicable Codes**: IPC 2021 (International Plumbing Code), UPC 2021 (Uniform Plumbing Code), ASPE Standards
**Related Standards**: NSF/ANSI 61 (Drinking Water Components), AWWA (American Water Works Association)

---

## Table of Contents

1. [Introduction and Code Overview](#introduction-and-code-overview)
2. [Fixture Unit Method](#fixture-unit-method)
3. [Water Supply Fixture Units (WSFU)](#water-supply-fixture-units)
4. [Pipe Sizing Tables and Velocity Limits](#pipe-sizing-tables)
5. [Water Pressure Requirements](#water-pressure-requirements)
6. [Hot Water System Sizing](#hot-water-system-sizing)
7. [Backflow Prevention](#backflow-prevention)
8. [Design Examples](#design-examples)
9. [Quality Assurance](#quality-assurance)
10. [Troubleshooting Common Issues](#troubleshooting)

---

## 1. Introduction and Code Overview

### Fundamental Design Principles

```
DOMESTIC WATER SYSTEM COMPONENTS:
┌────────────────────────────────────────────────────────────┐
│                                                            │
│  Water Meter → Backflow Preventer → Water Softener (opt) │
│       ↓                                                    │
│  Building Main → Branch Lines → Fixture Supply Lines      │
│       ↓                                                    │
│  Hot Water Heater → Hot Water Distribution → Fixtures     │
│       ↓                                                    │
│  Recirculation Pump (if applicable) → Return Line         │
└────────────────────────────────────────────────────────────┘

DESIGN OBJECTIVES:
├─ Adequate flow rate to all fixtures simultaneously
├─ Maintain minimum pressure at highest/furthest fixture
├─ Limit velocity to prevent noise and erosion (5-8 fps max)
├─ Minimize water hammer
├─ Provide backflow prevention where required
└─ Size water heater and circulation system properly
```

### Code Comparison: IPC vs UPC

```
┌────────────────────────────────┬───────────────┬──────────────┐
│ Design Element                 │ IPC 2021      │ UPC 2021     │
├────────────────────────────────┼───────────────┼──────────────┤
│ Fixture unit method            │ Yes (Ch 6)    │ Yes (Ch 6)   │
│ Water service sizing           │ Table 610.3   │ Table 6-3    │
│ Branch sizing                  │ Table 610.3   │ Table 6-3    │
│ Minimum fixture pressure       │ 15 psi (typ)  │ 15 psi (typ) │
│ Maximum static pressure        │ 80 psi        │ 80 psi       │
│ Velocity limit (explicit)      │ Not specified │ Not explicit │
│ Hot water sizing               │ Ch 5 (IPC)    │ Ch 5 (UPC)   │
│ Backflow prevention            │ Ch 6          │ Ch 6         │
└────────────────────────────────┴───────────────┴──────────────┘

Note: Most jurisdictions adopt IPC or UPC with local amendments.
      Always verify with Authority Having Jurisdiction (AHJ).
```

### Pipe Materials and Selection

```
COMMON PIPE MATERIALS FOR DOMESTIC WATER:

┌─────────────────┬────────────┬───────────┬──────────────────┐
│ Material        │ Temp Range │ Pressure  │ Application      │
├─────────────────┼────────────┼───────────┼──────────────────┤
│ Copper Type L   │ -100°F to  │ 250 psi   │ Hot & cold water │
│                 │  250°F     │ @ 100°F   │ (most common)    │
│                 │            │           │                  │
│ Copper Type K   │ -100°F to  │ 300 psi   │ Underground      │
│                 │  250°F     │ @ 100°F   │ service entrance │
│                 │            │           │                  │
│ CPVC            │  33°F to   │ 100 psi   │ Hot water        │
│ (Schedule 40)   │  200°F     │ @ 73°F    │ distribution     │
│                 │            │ 50psi@180°│                  │
│                 │            │           │                  │
│ PEX (Crosslinked│ -40°F to   │ 160 psi   │ Hot & cold water │
│ Polyethylene)   │  200°F     │ @ 73°F    │ residential/comm │
│                 │            │ 100psi@180│                  │
│                 │            │           │                  │
│ Galvanized Steel│  32°F to   │ 150 psi   │ Cold water only  │
│ (Schedule 40)   │  200°F     │           │ (obsolete for new│
│                 │            │           │  construction)   │
└─────────────────┴────────────┴───────────┴──────────────────┘

MATERIAL SELECTION CRITERIA:
├─ Building type: Residential vs commercial
├─ Water chemistry: Corrosion potential
├─ Local code requirements
├─ Installation method: Soldered, threaded, crimped, push-fit
├─ Cost considerations
└─ Life-cycle maintenance
```

---

## 2. Fixture Unit Method

### What is a Fixture Unit?

```
FIXTURE UNIT CONCEPT:
A fixture unit (FU) is an arbitrary unit representing the load-
producing effects on the plumbing system of different plumbing
fixtures.

Historical basis: 1 FU ≈ 7.5 gallons per minute (GPM) flow
                        from a typical lavatory

Purpose: Allows design without calculating simultaneous use
         probability for every fixture combination

Key principle: Not all fixtures operate simultaneously
              (Diversity factor built into sizing tables)
```

### Water Supply Fixture Units (WSFU) by Fixture Type

**IPC 2021 Table 610.3 / UPC 2021 Table 6-3**:

```
┌──────────────────────────────────┬─────────┬─────────┬──────────┐
│ Fixture Type                     │ Cold    │ Hot     │ Total    │
│                                  │ (WSFU)  │ (WSFU)  │ (WSFU)   │
├──────────────────────────────────┼─────────┼─────────┼──────────┤
│ RESIDENTIAL FIXTURES             │         │         │          │
├──────────────────────────────────┼─────────┼─────────┼──────────┤
│ Bathtub (with/without shower)    │   2.0   │   2.0   │   3.0    │
│ Bidet                            │   1.0   │   1.0   │   1.5    │
│ Clothes washer (residential)     │   2.0   │   2.0   │   3.0    │
│ Dishwasher (residential)         │    -    │   1.5   │   1.5    │
│ Hose bibb (each)                 │   2.5   │    -    │   2.5    │
│ Kitchen sink                     │   1.0   │   1.0   │   1.5    │
│ Laundry tub (1-3 compartments)   │   2.0   │   2.0   │   3.0    │
│ Lavatory                         │   0.5   │   0.5   │   0.75   │
│ Shower (single head)             │    -    │   2.0   │   2.0    │
│ Water closet (flush tank)        │   2.5   │    -    │   2.5    │
│ Water closet (flushometer)       │   5.0   │    -    │   5.0    │
│                                  │         │         │          │
│ COMMERCIAL FIXTURES              │         │         │          │
├──────────────────────────────────┼─────────┼─────────┼──────────┤
│ Clothes washer (commercial 8 lb) │   3.0   │   3.0   │   4.5    │
│ Dishwasher (commercial)          │    -    │   4.0   │   4.0    │
│ Drinking fountain                │   0.25  │    -    │   0.25   │
│ Kitchen sink (restaurant)        │   3.0   │   3.0   │   4.5    │
│ Lavatory (public)                │   1.0   │   1.0   │   1.5    │
│ Service sink (mop sink)          │   2.0   │   2.0   │   3.0    │
│ Shower (public, per head)        │    -    │   3.0   │   3.0    │
│ Urinal (1 gal flush or less)     │   2.0   │    -    │   2.0    │
│ Urinal (flushometer)             │   3.0   │    -    │   3.0    │
│ Water closet (public, flush tank)│   4.0   │    -    │   4.0    │
│ Water closet (public, flushometer│  10.0   │    -    │  10.0    │
│                                  │         │         │          │
│ SPECIAL FIXTURES                 │         │         │          │
├──────────────────────────────────┼─────────┼─────────┼──────────┤
│ Bathtub (hospital/institutional) │   3.0   │   3.0   │   4.5    │
│ Hydrotherapy tub                 │   4.0   │   4.0   │   6.0    │
│ Washing machine (commercial >8lb)│   4.0   │   4.0   │   6.0    │
│ Emergency shower/eyewash         │   2.0   │    -    │   2.0    │
└──────────────────────────────────┴─────────┴─────────┴──────────┘

IMPORTANT NOTES:
1. Values shown are typical; verify with adopted code edition
2. For fixtures not listed: Use similar fixture or manufacturer data
3. Hot + Cold ≠ Total (diversity factor built in)
4. Continuous flow fixtures: Calculate separately (see below)
```

### Continuous Flow Fixtures

```
FIXTURES WITH CONTINUOUS OPERATION:
These fixtures do NOT use fixture units; add GPM directly to system:

┌────────────────────────────────┬─────────────────────┐
│ Equipment                      │ Design Flow (GPM)   │
├────────────────────────────────┼─────────────────────┤
│ Lawn irrigation (per zone)     │ 10-30 GPM (varies)  │
│ Evaporative cooler             │ 3-5 GPM             │
│ Cooling tower makeup water     │ Per manufacturer    │
│ Reverse osmosis system         │ Per manufacturer    │
│ Coffee/espresso machine (comm) │ Per manufacturer    │
│ Ice machine (commercial)       │ Per manufacturer    │
│ Humidifier (commercial)        │ Per manufacturer    │
└────────────────────────────────┴─────────────────────┘

DESIGN APPROACH:
1. Calculate demand from fixture units (see tables below)
2. Add continuous flow fixtures at full rated flow
3. Total demand = FU demand + continuous flow demand
```

---

## 3. Water Supply Fixture Units (WSFU) and Demand

### Converting WSFU to GPM (Flow Rate)

**IPC 2021 Table 610.3(2) / UPC 2021 Table 6-3**:

```
┌─────────────────────────────────────────────────────────────┐
│ DEMAND (GPM) VS TOTAL FIXTURE UNITS (WSFU)                 │
│ For predominantly flush tank systems                        │
├──────────────┬──────────────┬──────────────┬───────────────┤
│ Total WSFU   │ Demand (GPM) │ Total WSFU   │ Demand (GPM)  │
├──────────────┼──────────────┼──────────────┼───────────────┤
│      1       │      3.0     │     40       │     40.0      │
│      2       │      5.0     │     50       │     48.0      │
│      3       │      6.5     │     60       │     55.0      │
│      4       │      8.0     │     70       │     61.0      │
│      5       │      9.4     │     80       │     67.0      │
│      6       │     10.7     │     90       │     73.0      │
│      8       │     13.0     │    100       │     78.0      │
│     10       │     15.0     │    120       │     88.0      │
│     12       │     17.0     │    140       │     98.0      │
│     15       │     19.8     │    160       │    107.0      │
│     20       │     24.0     │    180       │    115.0      │
│     25       │     28.0     │    200       │    124.0      │
│     30       │     32.0     │    250       │    145.0      │
│     35       │     36.0     │    300       │    165.0      │
│     40       │     40.0     │    400       │    201.0      │
│     50       │     48.0     │    500       │    235.0      │
│     60       │     55.0     │    750       │    315.0      │
│     80       │     67.0     │   1000       │    385.0      │
│    100       │     78.0     │   1250       │    449.0      │
│    150       │    102.0     │   1500       │    510.0      │
│    200       │    124.0     │   2000       │    625.0      │
└──────────────┴──────────────┴──────────────┴───────────────┘

PREDOMINANTLY FLUSHOMETER SYSTEMS:
Multiply table values by 1.2-1.5 due to higher instantaneous demand
Or use separate tables if provided in adopted code
```

**Key Observations**:
- Non-linear relationship due to diversity
- 100 WSFU = 78 GPM (not 750 GPM if all simultaneous)
- Larger systems have greater diversity factor

---

## 4. Pipe Sizing Tables and Velocity Limits

### Water Service and Branch Sizing

**IPC Table 610.3(1) - Copper Pipe (Type L)**:

```
┌────────────────────────────────────────────────────────────────┐
│ MAXIMUM FIXTURE UNITS (WSFU) FOR COPPER PIPE                  │
│ Based on: Type L copper, 40 psi minimum pressure, 5 fps max   │
├──────────┬───────────────────────────────────────────────────┤
│ Pipe Size│ Maximum Fixture Units (WSFU)                      │
│          ├─────────┬─────────┬─────────┬──────────┬──────────┤
│          │ 40 psi  │ 45 psi  │ 50 psi  │ 55 psi   │ 60+ psi  │
├──────────┼─────────┼─────────┼─────────┼──────────┼──────────┤
│   ½"     │    2    │    3    │    4    │    5     │    6     │
│   ¾"     │    5    │    6    │    8    │   10     │   12     │
│   1"     │   12    │   15    │   18    │   21     │   24     │
│  1¼"     │   23    │   28    │   33    │   38     │   43     │
│  1½"     │   39    │   47    │   55    │   63     │   71     │
│   2"     │   75    │   90    │  105    │  120     │  135     │
│  2½"     │  140    │  168    │  196    │  224     │  252     │
│   3"     │  250    │  300    │  350    │  400     │  450     │
│   4"     │  480    │  576    │  672    │  768     │  864     │
│   5"     │  850    │ 1020    │ 1190    │ 1360     │ 1530     │
│   6"     │ 1400    │ 1680    │ 1960    │ 2240     │ 2520     │
└──────────┴─────────┴─────────┴─────────┴──────────┴──────────┘

NOTES:
1. Table assumes reasonably straight runs
2. For long runs or many fittings: Increase pipe size
3. Pressure shown is available at fixture (after losses)
4. Velocities at maximum capacity approach 5-8 fps
```

### Velocity Limits and Noise Control

```
WATER VELOCITY RECOMMENDATIONS:

┌────────────────────────────────┬─────────────────────┐
│ Application                    │ Maximum Velocity    │
├────────────────────────────────┼─────────────────────┤
│ General distribution           │ 5-8 fps             │
│ Noise-sensitive areas          │ 4-5 fps             │
│ Long runs (>100 ft)            │ 5-6 fps             │
│ Pump discharge (short runs)    │ 8-10 fps            │
│ Minimum velocity (avoid silt)  │ 2 fps               │
└────────────────────────────────┴─────────────────────┘

VELOCITY CALCULATION:
V = (0.4085 × GPM) / d²

Where:
V = Velocity (feet per second)
GPM = Flow rate (gallons per minute)
d = Inside diameter (inches)

COPPER TYPE L INSIDE DIAMETERS:
┌────────────┬──────────────┐
│ Nominal    │ Inside Dia.  │
│ Size       │ (inches)     │
├────────────┼──────────────┤
│   ½"       │    0.545     │
│   ¾"       │    0.785     │
│   1"       │    1.025     │
│  1¼"       │    1.265     │
│  1½"       │    1.505     │
│   2"       │    1.985     │
│  2½"       │    2.465     │
│   3"       │    2.945     │
│   4"       │    3.905     │
└────────────┴──────────────┘

VELOCITY CHECK EXAMPLE:
Pipe: 1" Type L copper (ID = 1.025")
Flow: 15 GPM (from 12 WSFU)
V = (0.4085 × 15) / (1.025)²
V = 6.13 / 1.05 = 5.8 fps ✓ (acceptable, <8 fps)
```

### Pressure Loss Calculations

```
PRESSURE LOSS IN PIPES:
Two methods: (1) Friction loss charts, (2) Hazen-Williams formula

HAZEN-WILLIAMS FORMULA:
ΔP = (0.433 × L × Q^1.852) / (C^1.852 × d^4.87)

Where:
ΔP = Pressure loss (psi)
L = Pipe length (feet)
Q = Flow rate (GPM)
C = Hazen-Williams coefficient (roughness factor)
d = Inside diameter (inches)

C VALUES:
├─ Copper: C = 130-150 (use 130 for design)
├─ PEX: C = 150
├─ CPVC: C = 150
├─ Steel (new): C = 100-120
└─ Steel (aged): C = 60-80

SIMPLIFIED FRICTION LOSS (Copper, C=130):
┌──────────┬────────────────────────────────────────────────┐
│ Pipe Size│ Pressure Loss (psi per 100 ft) at Various GPM  │
│          ├──────┬──────┬──────┬──────┬──────┬───────┬─────┤
│          │ 5GPM │ 10GPM│ 15GPM│ 20GPM│ 30GPM│ 40GPM │60GPM│
├──────────┼──────┼──────┼──────┼──────┼──────┼───────┼─────┤
│   ¾"     │ 6.2  │ 21.5 │ 44.0 │ 73.0 │  -   │   -   │  -  │
│   1"     │ 1.8  │  6.3 │ 12.9 │ 21.4 │ 44.5 │  73.0 │  -  │
│  1¼"     │ 0.6  │  2.1 │  4.3 │  7.2 │ 15.0 │  24.6 │ 52.0│
│  1½"     │ 0.3  │  1.0 │  2.1 │  3.5 │  7.3 │  12.1 │ 25.5│
│   2"     │ 0.08 │  0.3 │  0.6 │  1.0 │  2.1 │   3.5 │  7.4│
│  2½"     │ 0.03 │  0.1 │  0.2 │  0.4 │  0.8 │   1.3 │  2.8│
│   3"     │ 0.01 │  0.04│  0.08│  0.14│  0.3 │   0.5 │  1.1│
└──────────┴──────┴──────┴──────┴──────┴──────┴───────┴─────┘

EQUIVALENT LENGTH FOR FITTINGS (add to straight pipe):
├─ 90° elbow: 5 ft equivalent
├─ 45° elbow: 2 ft equivalent
├─ Tee (flow through run): 2 ft equivalent
├─ Tee (flow through branch): 10 ft equivalent
├─ Gate valve (fully open): 1 ft equivalent
└─ Ball valve (fully open): 2 ft equivalent
```

---

## 5. Water Pressure Requirements

### Minimum and Maximum Pressures

```
CODE REQUIREMENTS:

MINIMUM PRESSURES (IPC/UPC):
├─ Flush tank water closet: 8-10 psi
├─ Flushometer water closet: 15-25 psi (check manufacturer)
├─ Flushometer urinal: 15 psi minimum
├─ Shower: 12-15 psi (8 psi absolute minimum)
├─ Lavatory faucet: 8 psi minimum
├─ Kitchen sink: 8 psi minimum
└─ General rule: 15 psi minimum at highest/furthest fixture

MAXIMUM STATIC PRESSURE:
├─ 80 psi maximum per IPC/UPC
├─ Pressure reducing valve (PRV) required if supply exceeds 80 psi
└─ PRV typically set to 50-60 psi for residential, 60-75 psi commercial
```

### Booster Pump Sizing

```
WHEN BOOSTER PUMPS REQUIRED:
├─ City water pressure insufficient for building height/length
├─ Water pressure < 40 psi at service entrance
├─ Tall buildings (>4 stories typically need boost)
└─ Remote locations with long supply runs

BOOSTER PUMP SYSTEM DESIGN:

Total Dynamic Head (TDH) Calculation:
TDH = Static Height + Pressure Loss + Required Pressure

Where:
Static Height = Elevation difference (ft) × 0.433 psi/ft
Pressure Loss = Pipe friction + fitting losses (psi)
Required Pressure = Minimum fixture pressure (typically 15-20 psi)

EXAMPLE:
5-story building, 60 ft elevation from ground to roof fixtures
City supply: 40 psi at meter

Static head: 60 ft × 0.433 = 26 psi
Friction loss (pipes/fittings): 12 psi (calculated)
Required pressure at fixture: 15 psi
Total required: 26 + 12 + 15 = 53 psi

Booster pressure needed: 53 - 40 = 13 psi boost

PUMP SELECTION:
Flow rate: Peak demand from fixture units (GPM)
Head: 13 psi × 2.31 ft/psi = 30 ft TDH
Select: Pump rated for required GPM at 30+ ft head

TYPICAL CONFIGURATIONS:
├─ Single pump with pressure tank (small buildings)
├─ Duplex pumps with VFD (redundancy, variable demand)
└─ Hydro-pneumatic tank for surge protection
```

### Pressure Zones in Tall Buildings

```
PRESSURE ZONE DESIGN:

Buildings >100 ft tall typically require multiple pressure zones
to prevent excessive pressure at lower floors.

ZONE PRESSURE LIMITS:
├─ Maximum static pressure any zone: 80 psi
├─ Typical zone pressure range: 40-70 psi
└─ Zone height: Typically 10-15 stories (100-150 ft)

ZONE CONFIGURATION EXAMPLE (20-story building):

┌──────────────────────────────────────────────────┐
│ Floors 16-20 (HIGH ZONE)                         │
│   Booster pump #2: 40 psi boost                  │
│   Supplied from intermediate tank or mains       │
└──────────────────────────────────────────────────┘
                       ↑
┌──────────────────────────────────────────────────┐
│ Floors 6-15 (MID ZONE)                           │
│   Booster pump #1: 40 psi boost                  │
│   Supplied from city mains                       │
└──────────────────────────────────────────────────┘
                       ↑
┌──────────────────────────────────────────────────┐
│ Floors 1-5 (LOW ZONE)                            │
│   Direct city water supply (reduced to 60 psi)   │
│   Pressure reducing valve at service entrance    │
└──────────────────────────────────────────────────┘
```

---

## 6. Hot Water System Sizing

### Water Heater Capacity

**Storage Tank Sizing** (Residential):

```
TANK SIZE SELECTION (ASHRAE/ASPE Method):

RESIDENTIAL (based on # of bathrooms and bedrooms):
┌────────────┬──────────────────────────────────────────┐
│ Bedrooms/  │ Storage Tank Size (gallons)              │
│ Bathrooms  ├──────────┬──────────┬────────────────────┤
│            │ Gas      │ Electric │ First Hour Rating  │
├────────────┼──────────┼──────────┼────────────────────┤
│ 1-1.5 BR   │  30 gal  │  30 gal  │  40-50 GPH         │
│ 2-2.5 BR   │  40 gal  │  40 gal  │  50-60 GPH         │
│ 3-3.5 BR   │  50 gal  │  50 gal  │  60-75 GPH         │
│ 4-4.5 BR   │  60 gal  │  66 gal  │  75-90 GPH         │
│ 5+ BR      │  75 gal  │  80 gal  │  90-110 GPH        │
└────────────┴──────────┴──────────┴────────────────────┘

FIRST HOUR RATING (FHR):
More important than tank size alone.
FHR = Tank capacity × 0.7 + (Recovery rate × 1 hour)

Recovery rate (GPH) = (BTU input × Efficiency) / (8.33 × ΔT)
Where ΔT = Temperature rise (typically 90°F: 50°F inlet → 140°F)

EXAMPLE:
50-gallon gas water heater, 40,000 BTU/hr, 80% efficient
Recovery = (40,000 × 0.80) / (8.33 × 90) = 42.7 GPH
FHR = (50 × 0.7) + 42.7 = 35 + 42.7 = 77.7 GPH
```

**Commercial Water Heating**:

```
COMMERCIAL SIZING METHOD (Hunter Curve for Hot Water):

1. Calculate total hot water fixture units
2. Determine peak demand (GPM) from Hunter curve
3. Calculate hourly demand and daily demand
4. Size storage tank and heater capacity

PEAK DEMAND VS FIXTURE UNITS (Hot Water):
┌─────────────┬──────────────┬────────────────────────┐
│ Hot Water   │ Peak Demand  │ Example Application    │
│ WSFU        │ (GPM)        │                        │
├─────────────┼──────────────┼────────────────────────┤
│     10      │     8.0      │ Small office           │
│     20      │    12.5      │ Restaurant (small)     │
│     40      │    20.0      │ School (moderate)      │
│     60      │    26.0      │ Hospital wing          │
│    100      │    35.0      │ Large hotel wing       │
│    150      │    45.0      │ Major commercial       │
└─────────────┴──────────────┴────────────────────────┘

STORAGE TANK SIZING:
Storage (gallons) = (Peak GPM × Peak Duration) - (Recovery GPM × Duration)

Typical peak durations:
├─ Hotels: 30-60 minutes (morning showers)
├─ Restaurants: 60-120 minutes (meal service)
├─ Schools: 15-30 minutes (between classes)
└─ Healthcare: 24-hour continuous (smaller peaks)

HEATER INPUT CAPACITY:
BTU/hr = (GPH recovery × 8.33 × ΔT) / Efficiency

Target recovery: Reheat storage tank in 4-6 hours
```

### Hot Water Recirculation

```
RECIRCULATION SYSTEM DESIGN:

PURPOSE:
Eliminate wait time for hot water at fixtures by maintaining
continuous circulation loop.

WHEN REQUIRED:
├─ IPC: Required when developed length exceeds 100 ft from heater to fixture
├─ UPC: Similar requirement (check local amendment)
├─ Practical: Consider for any run >50 ft in commercial
└─ Energy codes: May restrict continuous recirc; use timers/sensors

RECIRCULATION FLOW RATE:
Q_recirc (GPM) = Heat Loss (BTU/hr) / (500 × ΔT)

Where:
Heat Loss = Pipe heat loss (depends on insulation, length, temperature)
ΔT = Temperature drop in return line (typically 10-20°F)
500 = Constant (8.33 lb/gal × 60 min/hr × 1 BTU/lb·°F)

PIPE HEAT LOSS (bare copper pipe, 140°F water, 70°F ambient):
┌────────────┬──────────────────────────────────────────┐
│ Pipe Size  │ Heat Loss (BTU/hr per linear foot)       │
│            ├──────────┬───────────┬───────────────────┤
│            │ Bare     │ ½" Insul  │ 1" Insulation     │
├────────────┼──────────┼───────────┼───────────────────┤
│   ¾"       │   35     │    12     │      7            │
│   1"       │   45     │    15     │      9            │
│  1¼"       │   55     │    18     │     11            │
│  1½"       │   65     │    21     │     13            │
│   2"       │   82     │    26     │     16            │
└────────────┴──────────┴───────────┴───────────────────┘

EXAMPLE CALCULATION:
System: 200 ft total loop length (supply + return)
Pipe: 1" copper, ½" insulation
Heat loss: 200 ft × 15 BTU/hr·ft = 3,000 BTU/hr
ΔT allowed: 15°F
Q_recirc = 3,000 / (500 × 15) = 0.4 GPM

PUMP SIZING:
Flow: Calculated recirculation rate (GPM)
Head: Friction loss in loop + check valve + strainer
      Typically 5-15 ft head for residential/small commercial

RETURN LINE SIZING:
Return pipe typically 1-2 sizes smaller than supply
Check velocity: Should be 2-4 fps (avoid air entrainment if too slow)

CONTROLS:
├─ Continuous operation (older systems, high energy use)
├─ Timer control (operate during peak demand hours)
├─ Aquastat control (temperature-based cycling)
├─ Demand control (motion sensor/push-button activation)
└─ Smart controls (occupancy-based, learning algorithms)
```

---

## 7. Backflow Prevention

### Backflow Hazard Classification

```
CROSS-CONNECTION CONTROL:

HAZARD LEVELS (IPC 608 / UPC 603):
┌────────────────────┬──────────────────────────────────────┐
│ Hazard Level       │ Definition & Examples                │
├────────────────────┼──────────────────────────────────────┤
│ HIGH HAZARD        │ Potential for contamination with     │
│ (Health hazard)    │ toxic substances, sewage, chemicals  │
│                    │                                      │
│ Examples:          │ - Irrigation systems                 │
│                    │ - Fire sprinkler systems (chemical)  │
│                    │ - Boilers with chemical treatment    │
│                    │ - Hospital/lab equipment             │
│                    │ - Industrial process water           │
│                    │                                      │
│ Required Device:   │ Reduced Pressure Principle (RP)      │
│                    │ Backflow Preventer or Air Gap        │
│                    │                                      │
├────────────────────┼──────────────────────────────────────┤
│ LOW HAZARD         │ Potential for aesthetic or non-toxic │
│ (Non-health hazard)│ contamination                        │
│                    │                                      │
│ Examples:          │ - Heating systems (non-toxic)        │
│                    │ - Carbonated beverage machines       │
│                    │ - Landscaping systems (no chemicals) │
│                    │ - Decorative fountains               │
│                    │                                      │
│ Required Device:   │ Double Check Valve Assembly (DCVA)   │
│                    │ or Pressure Vacuum Breaker (PVB)     │
└────────────────────┴──────────────────────────────────────┘
```

### Backflow Prevention Device Selection

```
DEVICE TYPES AND APPLICATIONS:

1. AIR GAP (AG):
   - Physical separation between supply and flood level rim
   - Minimum 1 inch above flood level rim (2× pipe diameter minimum)
   - Most reliable protection (gravity-based, no mechanical failure)
   - Use: High hazard, where space permits
   - Drawback: Requires elevation, can't maintain pressure

2. REDUCED PRESSURE PRINCIPLE (RP or RPZ):
   - Two check valves with differential pressure relief valve between
   - Relief valve opens if backpressure exceeds forward pressure
   - Testable, approved for high hazard
   - Use: High hazard protection, irrigation, fire systems
   - Requirement: Drainage for relief valve discharge

3. DOUBLE CHECK VALVE ASSEMBLY (DCVA or DC):
   - Two check valves in series with shutoff valves and test cocks
   - Testable, approved for low hazard
   - Use: Low hazard protection, residential services
   - No relief valve (can't handle high hazard)

4. PRESSURE VACUUM BREAKER (PVB):
   - Check valve with atmospheric vent
   - Opens to atmosphere on backpressure/backsiphonage
   - Must be installed minimum 12" above highest outlet
   - Use: Irrigation, hose bibbs (low hazard)
   - Cannot be used under continuous pressure

5. ATMOSPHERIC VACUUM BREAKER (AVB):
   - Simple check with atmospheric vent
   - Not testable, must be installed on each outlet
   - Use: Individual hose bibbs, janitor sinks
   - Cannot be used under continuous pressure

6. HOSE BIBB VACUUM BREAKER:
   - Small atmospheric vacuum breaker for hose bibbs
   - Non-testable, inexpensive
   - Use: Individual hose connections (no continuous pressure)
```

**Installation Requirements**:

```
BACKFLOW PREVENTER INSTALLATION:

LOCATION:
├─ RP devices: Indoors or in heated enclosure (freeze protection)
├─ DCVA: Can be installed in pit/vault (with drainage)
├─ PVB: Must be 12" minimum above highest outlet
└─ All devices: Accessible for testing and maintenance

TESTING:
├─ Annual testing required for RP, DCVA (by certified tester)
├─ Test reports submitted to water authority
├─ Tag/label showing last test date
└─ Repairs by qualified technician only

SIZING:
Size backflow preventer based on flow rate, NOT pipe size
(Devices cause pressure loss; may need larger size than pipe)

PRESSURE LOSS (typical values through device):
┌───────────┬────────────────────────────────────────┐
│ Device    │ Pressure Loss at Rated Flow            │
├───────────┼────────────────────────────────────────┤
│ RP        │ 10-12 psi (higher than DC)             │
│ DCVA      │ 3-5 psi                                │
│ PVB       │ 2-3 psi                                │
└───────────┴────────────────────────────────────────┘
```

---

## 8. Design Examples

### Example 1: Small Office Building

**Project Data**:
- 2-story office building
- Floor 1: 4 restrooms (2M/2F), break room, janitor closet
- Floor 2: 4 restrooms (2M/2F), break room, janitor closet
- City water pressure: 65 psi at meter
- Elevation difference: 12 ft floor-to-floor

**Fixture Count and WSFU**:

```
FLOOR 1 FIXTURES:
Men's Restroom:
├─ 2 Water closets (flush tank): 2 × 2.5 = 5.0 WSFU
├─ 2 Lavatories: 2 × 0.75 = 1.5 WSFU
└─ 1 Urinal (flush tank): 1 × 2.0 = 2.0 WSFU
    Subtotal: 8.5 WSFU

Women's Restroom:
├─ 3 Water closets (flush tank): 3 × 2.5 = 7.5 WSFU
└─ 2 Lavatories: 2 × 0.75 = 1.5 WSFU
    Subtotal: 9.0 WSFU

Break Room:
├─ 1 Kitchen sink: 1.5 WSFU
├─ 1 Dishwasher: 1.5 WSFU
└─ 1 Coffee maker: 1.0 GPM (continuous, add directly)
    Subtotal: 3.0 WSFU + 1.0 GPM

Janitor Closet:
└─ 1 Service sink: 3.0 WSFU

FLOOR 1 TOTAL: 8.5 + 9.0 + 3.0 + 3.0 = 23.5 WSFU
FLOOR 2 TOTAL: 23.5 WSFU (identical)

BUILDING TOTAL: 47 WSFU + 2.0 GPM continuous

From IPC Table 610.3(2):
47 WSFU ≈ 47 GPM (interpolate between 40 and 50 WSFU)
Add continuous: 47 + 2 = 49 GPM peak demand
```

**Service Entrance Sizing**:

```
PRESSURE AVAILABLE AT SECOND FLOOR:
Elevation loss: 12 ft × 0.433 psi/ft = 5.2 psi
Available at Floor 2: 65 - 5.2 = 59.8 psi ✓ (adequate)

WATER SERVICE SIZE (from meter to building):
Peak demand: 49 GPM
Available pressure: 65 psi at meter
Distance: 50 ft from meter to building

From IPC Table 610.3(1):
At 60+ psi: 2" copper pipe = 135 WSFU capacity ✓

Verify velocity:
V = (0.4085 × 49) / (1.985)² = 5.1 fps ✓ (acceptable)

Verify pressure loss:
From friction table: 2" pipe at 49 GPM ≈ 1.0 psi/100 ft
Loss in 50 ft: 0.5 psi (negligible)

RESULT: 2" Type L copper service entrance
```

**Branch Sizing**:

```
FLOOR 1 MAIN BRANCH:
23.5 WSFU + 1.0 GPM continuous = ~24 GPM
From table: 1½" pipe adequate (39 WSFU capacity @ 60 psi)

RESTROOM BRANCHES:
Men's room: 8.5 WSFU → 1" pipe (12 WSFU capacity @ 60 psi) ✓
Women's room: 9.0 WSFU → 1" pipe (12 WSFU capacity @ 60 psi) ✓

INDIVIDUAL FIXTURE SUPPLIES:
├─ Water closets: ½" supply line (standard)
├─ Lavatories: ⅜" supply line (standard)
├─ Kitchen sink: ½" supply line
└─ Service sink: ½" supply line
```

### Example 2: Residential Hot Water Sizing

**Given**:
- 3 bedroom, 2.5 bath home
- Gas water heater consideration
- Family of 4

**Sizing Calculation**:

```
FIXTURE UNITS (Hot Water Only):
┌────────────────────────┬──────┬─────────┐
│ Fixture                │ Qty  │ HW WSFU │
├────────────────────────┼──────┼─────────┤
│ Kitchen sink           │  1   │   1.0   │
│ Dishwasher             │  1   │   1.5   │
│ Clothes washer         │  1   │   2.0   │
│ Master bath shower     │  1   │   2.0   │
│ Master bath lavatory   │  2   │   1.0   │
│ Hall bath tub/shower   │  1   │   2.0   │
│ Hall bath lavatory     │  1   │   0.5   │
│ Powder room lavatory   │  1   │   0.5   │
└────────────────────────┴──────┴─────────┘
TOTAL HOT WATER: 10.5 WSFU ≈ 15 GPM peak

TANK SELECTION (Method 1 - Rule of Thumb):
3 bedrooms, 2.5 baths → 50-gallon tank (from table)

TANK SELECTION (Method 2 - First Hour Rating):
Peak hour demand (morning showers + laundry):
├─ 2 showers @ 10 min each × 2.5 GPM = 50 gallons
├─ 1 lavatory @ 5 min × 1.5 GPM = 7.5 gallons
├─ Clothes washer (hot water): 7 gallons
└─ Kitchen cleanup: 5 gallons
    Total peak hour: 69.5 gallons

Required FHR: 70 gallons minimum

Check 50-gallon gas heater with 40,000 BTU input, 80% efficient:
Recovery rate: (40,000 × 0.80) / (8.33 × 90) = 42.7 GPH
FHR = (50 × 0.7) + 42.7 = 35 + 42.7 = 77.7 GPH ✓

RESULT: 50-gallon gas water heater with FHR ≥ 70 GPH
        (Verify specific model FHR rating on label)

ALTERNATIVE: Tankless water heater
Flow rate needed: 15 GPM
Temperature rise: 50°F inlet → 120°F = 70°F rise
BTU required: 15 GPM × 8.33 × 70 × 60 = 524,790 BTU/hr
Tankless size: 525,000 BTU/hr input (accounting for 85% efficiency)
```

---

## 9. Quality Assurance

```
DOMESTIC WATER SYSTEM QA CHECKLIST:

☐ DESIGN CALCULATIONS
  ☐ Fixture unit totals calculated correctly
  ☐ Peak demand (GPM) determined from WSFU tables
  ☐ Continuous flow fixtures added to demand
  ☐ Pressure available at furthest/highest fixture ≥ 15 psi
  ☐ Velocity checked at all pipe sizes (< 8 fps)

☐ PIPE SIZING
  ☐ Service entrance sized for total building demand
  ☐ Branch lines sized per IPC/UPC tables
  ☐ Fixture supply lines meet minimum code sizes
  ☐ Hot water return line sized (if applicable)

☐ PRESSURE CONTROL
  ☐ PRV specified if supply pressure > 80 psi
  ☐ Booster pump specified if insufficient pressure
  ☐ Pressure zones identified (tall buildings)
  ☐ Water hammer arrestors located at quick-closing valves

☐ HOT WATER SYSTEM
  ☐ Water heater capacity adequate (tank size or FHR)
  ☐ Temperature/pressure relief valve specified
  ☐ Recirculation system designed (if required)
  ☐ Recirculation pump sized for heat loss
  ☐ Expansion tank sized for closed system

☐ BACKFLOW PREVENTION
  ☐ Hazard assessment completed
  ☐ Appropriate devices selected (RP, DCVA, PVB, AVB)
  ☐ Installation location appropriate
  ☐ Drainage provided for RP relief valve
  ☐ Devices accessible for testing

☐ CODE COMPLIANCE
  ☐ IPC or UPC tables/methods applied correctly
  ☐ Local amendments reviewed
  ☐ Minimum fixture pressures met
  ☐ Maximum static pressure not exceeded
  ☐ Cross-connection control per local authority

☐ DOCUMENTATION
  ☐ Isometric drawings complete
  ☐ Riser diagrams for multi-story buildings
  ☐ Fixture schedules with WSFU values
  ☐ Calculations signed/sealed (if required)
  ☐ Equipment specifications and cut sheets
```

---

## 10. Troubleshooting Common Issues

```
COMMON PROBLEMS AND SOLUTIONS:

ISSUE: Insufficient flow at fixtures
CAUSES:
├─ Undersized piping
├─ Excessive friction loss (too many fittings, long runs)
├─ Partially closed valves
├─ Corroded/restricted pipes
└─ Low supply pressure

SOLUTIONS:
├─ Recalculate pipe sizes, upsize if needed
├─ Minimize fittings, use long-radius elbows
├─ Install booster pump system
└─ Replace corroded pipes (if existing building)

ISSUE: Water hammer (loud banging)
CAUSES:
├─ Quick-closing valves (solenoid, flushometer)
├─ High water velocity
├─ Lack of air chambers or arrestors
└─ Loose pipes

SOLUTIONS:
├─ Install water hammer arrestors at quick-closing valves
├─ Reduce velocity by increasing pipe size
├─ Secure pipes with proper hangers/straps
└─ Lower supply pressure if excessive

ISSUE: Hot water takes too long to arrive
CAUSES:
├─ Long pipe runs without recirculation
├─ Undersized water heater
├─ Inadequate insulation
└─ Malfunctioning recirculation pump

SOLUTIONS:
├─ Install recirculation system (per code requirements)
├─ Upsize water heater capacity
├─ Insulate all hot water pipes (minimum R-3)
└─ Verify pump operation, adjust controls

ISSUE: Pressure drops when multiple fixtures operate
CAUSES:
├─ Undersized service or branch piping
├─ Insufficient supply pressure
└─ Clogged/restricted backflow preventer

SOLUTIONS:
├─ Upsize piping to meet simultaneous demand
├─ Install booster pump if supply pressure inadequate
└─ Clean/service backflow preventer, upsize if needed

ISSUE: Scalding or inconsistent hot water temperature
CAUSES:
├─ Water heater temperature set too high (>140°F)
├─ Lack of thermostatic mixing valves
├─ Simultaneous cold water demand causing temperature swing
└─ Undersized water heater recovery

SOLUTIONS:
├─ Install thermostatic mixing valves at fixtures
├─ Set heater to 120-140°F, mix down to 120°F at fixtures
├─ Upsize water heater or add mixing valve with bypass
└─ Pressure-balancing valves at showers
```

---

## Summary

Proper domestic water system design ensures adequate flow, pressure, and temperature at all plumbing fixtures while maintaining safety through backflow prevention and code compliance. This guide provides:

1. **Fixture unit methodology** for calculating water demand per IPC/UPC
2. **Pipe sizing procedures** using code tables and velocity limits
3. **Pressure calculations** including friction loss and booster pump requirements
4. **Hot water system design** including storage tank and recirculation systems
5. **Backflow prevention** device selection and installation requirements
6. **Complete design examples** for commercial and residential applications
7. **QA procedures** to ensure compliant, functional systems

**Key References**:
- IPC 2021: International Plumbing Code, Chapter 6 (Water Supply)
- UPC 2021: Uniform Plumbing Code, Chapter 6 (Water Supply Systems)
- ASPE Data Book Volume 1: Fundamentals of Plumbing Engineering
- ASPE Data Book Volume 2: Plumbing Engineering Design Handbook
- ASHRAE Handbook - HVAC Applications: Service Water Heating
- AWWA M22: Sizing Water Service Lines and Meters

---

*Document maintained by: Plumbing Design Engineering Team*
*Next review date: 2026-01-22*
