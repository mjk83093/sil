# HVAC Load Calculations Guide
## Comprehensive Manual for Heating and Cooling Load Analysis

**Document Version**: 1.0
**Last Updated**: 2025-01-22
**Applicable Standards**: ASHRAE Handbook - Fundamentals (2021), ASHRAE 90.1-2022, IECC 2021, ACCA Manual J (Residential)
**Related Standards**: SMACNA, ACCA Manual D (Duct Sizing), ACCA Manual S (Equipment Selection)

---

## Table of Contents

1. [Introduction and Fundamental Concepts](#introduction-and-fundamental-concepts)
2. [Cooling Load Calculation Methods](#cooling-load-calculation-methods)
3. [Heating Load Calculation Methods](#heating-load-calculation-methods)
4. [Psychrometric Processes](#psychrometric-processes)
5. [Equipment Selection Criteria](#equipment-selection-criteria)
6. [Duct Sizing Methods](#duct-sizing-methods)
7. [Hydronic Pipe Sizing](#hydronic-pipe-sizing)
8. [Load Calculation Worksheets](#load-calculation-worksheets)
9. [Examples and Case Studies](#examples-and-case-studies)
10. [QA Checklist](#qa-checklist)

---

## 1. Introduction and Fundamental Concepts

### Heat Transfer Fundamentals

#### Basic Heat Transfer Modes

```
┌──────────────────────────────────────────────────────────────┐
│ HEAT TRANSFER MECHANISMS                                     │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│ 1. CONDUCTION (through solid materials)                     │
│    Q = (k × A × ΔT) / d                                     │
│    Q = Heat transfer rate (Btu/hr or W)                     │
│    k = Thermal conductivity (Btu·in/hr·ft²·°F or W/m·K)   │
│    A = Area (ft² or m²)                                     │
│    ΔT = Temperature difference (°F or K)                    │
│    d = Thickness (inches or meters)                         │
│                                                              │
│ 2. CONVECTION (fluid movement)                              │
│    Q = h × A × ΔT                                           │
│    h = Convection coefficient (Btu/hr·ft²·°F or W/m²·K)   │
│                                                              │
│ 3. RADIATION (electromagnetic waves)                         │
│    Q = σ × ε × A × (T₁⁴ - T₂⁴)                           │
│    σ = Stefan-Boltzmann constant                           │
│    ε = Emissivity (0-1)                                    │
│    T = Absolute temperature (Rankine or Kelvin)            │
└──────────────────────────────────────────────────────────────┘
```

#### R-Value and U-Factor

```
R-VALUE (Thermal Resistance):
R = d / k  or  R = 1 / h
Units: hr·ft²·°F/Btu (Imperial) or m²·K/W (SI)

Higher R-value = Better insulation

U-FACTOR (Overall Heat Transfer Coefficient):
U = 1 / R_total
Units: Btu/hr·ft²·°F (Imperial) or W/m²·K (SI)

Lower U-factor = Better insulation

COMPOSITE WALL R-VALUE:
R_total = R_inside air film + R_material₁ + R_material₂ + ... + R_outside air film

Example: Standard wall assembly
├─ Inside air film: R = 0.68
├─ ½" Gypsum board: R = 0.45
├─ 3½" Fiberglass batt: R = 13.0
├─ ½" Plywood sheathing: R = 0.62
├─ Building wrap: R = 0.5
└─ Outside air film: R = 0.17
────────────────────────────────
Total: R = 15.42 hr·ft²·°F/Btu
U = 1/15.42 = 0.065 Btu/hr·ft²·°F
```

### Design Conditions

#### ASHRAE Design Conditions (from local climate data)

```
┌────────────────────────────────────────────────────────────┐
│ OUTDOOR DESIGN CONDITIONS                                  │
├────────────────────────────────────────────────────────────┤
│ Summer (Cooling):                                          │
│  - Dry bulb temperature: 99.6% or 99.0% design value      │
│  - Wet bulb temperature: Corresponding value               │
│  - Daily temperature range: Mean coincident               │
│                                                            │
│ Winter (Heating):                                          │
│  - Dry bulb temperature: 99.6% or 99.0% design value      │
│  - Usually most extreme 1% or 0.4% condition not used     │
│                                                            │
│ Example: Dallas, TX (ASHRAE Climate Zone 3A)              │
│  Summer 0.4%: 100°F DB / 75°F WB                         │
│  Summer 1.0%: 98°F DB / 75°F WB                          │
│  Winter 99.6%: 22°F DB                                    │
│  Winter 99.0%: 26°F DB                                    │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ INDOOR DESIGN CONDITIONS                                   │
├────────────────────────────────────────────────────────────┤
│ ASHRAE 55 Thermal Comfort Ranges:                         │
│                                                            │
│ Summer (Cooling Season):                                   │
│  - Temperature: 73-79°F (23-26°C)                         │
│  - Relative Humidity: 30-60%                              │
│  - Typical design: 75°F DB, 50% RH                        │
│                                                            │
│ Winter (Heating Season):                                   │
│  - Temperature: 68-76°F (20-24°C)                         │
│  - Relative Humidity: 30-60%                              │
│  - Typical design: 70°F DB, 40% RH                        │
│                                                            │
│ Special Occupancies:                                       │
│  - Healthcare patient rooms: 70-75°F, 30-60% RH           │
│  - Computer rooms: 68-77°F, 40-55% RH                     │
│  - Laboratories: 68-75°F, 30-60% RH                       │
│  - Natatoriums (pools): 75-85°F, 50-60% RH               │
└────────────────────────────────────────────────────────────┘
```

### Load Components

```
COOLING LOAD COMPONENTS:
├─ Envelope loads (transmission through walls, roof, windows)
├─ Solar gain through windows (fenestration)
├─ Internal heat gains (people, lights, equipment)
├─ Ventilation/infiltration (outdoor air)
└─ Latent loads (moisture from people, ventilation, infiltration)

HEATING LOAD COMPONENTS:
├─ Envelope loads (transmission through walls, roof, windows)
├─ Infiltration (outdoor air leakage)
├─ Ventilation (mechanical outdoor air)
└─ Pickup load (morning warm-up, if intermittent operation)
```

---

## 2. Cooling Load Calculation Methods

### Radiant Time Series (RTS) Method

**Current ASHRAE standard method** (replaced older CLTD/CLF and Transfer Function methods)

#### Key Concepts

```
RADIANT TIME SERIES METHOD:
Accounts for thermal mass and time delay in heat gain.

1. Calculate instantaneous heat gains
2. Apply radiant time factors (RTF) to convert radiant gains to cooling loads
3. Sum convective loads directly (no time delay)

Heat Gain vs Cooling Load:
- Heat gain: Energy entering space at instant in time
- Cooling load: Rate HVAC must remove heat (accounts for thermal storage)

Example: Solar gain through window
  - Instantaneous heat gain: 10,000 Btu/hr at 2 PM
  - Peak cooling load: 7,500 Btu/hr at 4 PM (time delay due to thermal mass)
```

#### Cooling Load Temperature Difference (CLTD) - Simplified Method

```
ROOF/WALL CONDUCTION:
Q = U × A × CLTD

Where:
Q = Cooling load (Btu/hr)
U = Overall heat transfer coefficient (Btu/hr·ft²·°F)
A = Area (ft²)
CLTD = Cooling Load Temperature Difference (°F)
       (from ASHRAE tables based on wall/roof type, orientation, time of day)

WINDOW CONDUCTION:
Q = U × A × (T_outdoor - T_indoor)

Simpler for windows due to low thermal mass
```

#### Solar Heat Gain Through Windows

```
SOLAR HEAT GAIN:
Q_solar = A × SHGC × SCL

Where:
A = Window area (ft²)
SHGC = Solar Heat Gain Coefficient (dimensionless, 0-1)
       From manufacturer data or ASHRAE tables
SCL = Solar Cooling Load factor (Btu/hr·ft²)
      From ASHRAE tables based on orientation, latitude, time

Alternative formula:
Q_solar = A × SC × SHGF

SC = Shading Coefficient (older method, dimensionless)
SHGF = Solar Heat Gain Factor (Btu/hr·ft²)

Relationship: SHGC ≈ SC × 0.87
```

**Solar Heat Gain Coefficients (SHGC) - Typical Values**:

```
┌──────────────────────────────────┬──────────┐
│ Glazing Type                     │ SHGC     │
├──────────────────────────────────┼──────────┤
│ Single-pane clear glass          │ 0.86     │
│ Double-pane clear glass (¼" gap) │ 0.76     │
│ Double-pane low-E (¼" gap)       │ 0.40-0.70│
│ Triple-pane low-E                │ 0.30-0.50│
│ Single-pane bronze tint          │ 0.73     │
│ Double-pane reflective           │ 0.20-0.40│
└──────────────────────────────────┴──────────┘

Lower SHGC = Less solar heat gain = Better for cooling-dominated climates
```

#### Internal Heat Gains

**People (Sensible + Latent)**:

```
OCCUPANT HEAT GAIN (ASHRAE Handbook - Fundamentals, Table 1):

┌────────────────────────┬──────────┬─────────┬──────────┐
│ Activity               │ Sensible │ Latent  │ Total    │
│                        │ (Btu/hr) │ (Btu/hr)│ (Btu/hr) │
├────────────────────────┼──────────┼─────────┼──────────┤
│ Seated, very light work│   230    │   190   │   420    │
│ (office, theater)      │          │         │          │
│                        │          │         │          │
│ Seated, eating         │   255    │   235   │   490    │
│                        │          │         │          │
│ Standing, light work   │   250    │   250   │   500    │
│ (retail, laboratory)   │          │         │          │
│                        │          │         │          │
│ Walking, 3 mph         │   305    │   345   │   650    │
│ (shopping mall)        │          │         │          │
│                        │          │         │          │
│ Moderate work          │   375    │   625   │  1,000   │
│ (factory, heavy work)  │          │         │          │
│                        │          │         │          │
│ Heavy work/athletics   │   580    │  1,020  │  1,600   │
│ (gymnasium, sports)    │          │         │          │
└────────────────────────┴──────────┴─────────┴──────────┘

Total cooling load from people:
Q_people = N × (Sensible + Latent) × CLF

N = Number of occupants
CLF = Cooling Load Factor (accounts for diversity, typically 0.7-1.0)
```

**Lighting**:

```
LIGHTING HEAT GAIN:
Q_lights = W × F_ul × F_sa

Where:
W = Total lighting watts installed
F_ul = Use factor (actual operation, typically 1.0 if all on)
F_sa = Special allowance factor
       = 1.0 for recessed fixtures vented to return air
       = 1.2 for recessed fixtures not vented
       = 1.0 for surface or pendant-mounted fixtures

Conversion: 1 watt = 3.412 Btu/hr

Example:
Office space: 10,000 ft²
Lighting power density: 0.9 W/ft² (ASHRAE 90.1)
Total watts: 10,000 × 0.9 = 9,000W
Q_lights = 9,000 × 1.0 × 1.0 = 9,000W = 30,708 Btu/hr
```

**Equipment (Appliances, Computers, etc.)**:

```
EQUIPMENT HEAT GAIN:

Computers/Office Equipment:
├─ Desktop computer: 100-150W sensible (340-510 Btu/hr)
├─ Laptop computer: 50-75W sensible (170-255 Btu/hr)
├─ LCD monitor: 40-80W sensible (135-270 Btu/hr)
├─ Laser printer: 150-500W sensible when printing
└─ Copy machine: 1,000-3,000W sensible when operating

Diversity Factor: 0.5-0.75 (not all equipment on simultaneously)

Kitchen Equipment:
├─ Refrigerator: 1,000-2,000 Btu/hr (sensible)
├─ Electric range: 3,500W × 3.412 = 11,942 Btu/hr (with hood: 50% captured)
├─ Dishwasher: 1,500W sensible + latent (steam)
└─ Microwave: 1,200W sensible (rated input, not cooking power)

Medical Equipment:
MRI machine, CT scanner, X-ray: Per manufacturer specifications (substantial loads)
```

#### Ventilation and Infiltration

```
VENTILATION (Outdoor Air):
Q_sensible = 1.08 × CFM × (T_outdoor - T_indoor)
Q_latent = 0.68 × CFM × (W_outdoor - W_indoor)

Where:
CFM = Outdoor air volume flow rate (ft³/min)
1.08 = Constant for air (0.075 lb/ft³ × 0.24 Btu/lb·°F × 60 min/hr)
0.68 = Constant for latent (0.075 lb/ft³ × 1,061 Btu/lb × 60 min/hr ÷ 7,000 grains/lb)
W = Humidity ratio (grains H₂O per lb dry air)

INFILTRATION:
Q = CFM_infiltration × 1.08 × ΔT

Infiltration rate estimation:
CFM_infiltration = (Volume × ACH) / 60

ACH (Air Changes per Hour):
├─ Tight construction: 0.1-0.3 ACH
├─ Average construction: 0.3-0.6 ACH
└─ Loose construction: 0.6-1.0 ACH
```

### Room-by-Room Cooling Load Summary

```
TOTAL COOLING LOAD SUMMARY (Btu/hr):

Envelope Loads:
├─ Walls (all orientations): U × A × CLTD
├─ Roof: U × A × CLTD
├─ Windows conduction: U × A × ΔT
└─ Windows solar: A × SHGC × SCL

Internal Gains:
├─ People sensible: N × 250 Btu/hr (typical office)
├─ People latent: N × 200 Btu/hr (typical office)
├─ Lights: W × 3.412
└─ Equipment: W × 3.412 × diversity

Outdoor Air:
├─ Ventilation sensible: 1.08 × CFM × ΔT
├─ Ventilation latent: 0.68 × CFM × ΔW
├─ Infiltration sensible: 1.08 × CFM × ΔT
└─ Infiltration latent: 0.68 × CFM × ΔW

Safety Factor: 10-15% typical
Total Sensible Load: Sum all sensible components
Total Latent Load: Sum all latent components
Grand Total Load: Sensible + Latent

Equipment Sizing: Total load ÷ Equipment efficiency
```

---

## 3. Heating Load Calculation Methods

### Heat Loss Calculation

**Simpler than cooling - steady-state conditions, no solar gain, minimal internal gains**

#### Envelope Heat Loss

```
TRANSMISSION HEAT LOSS:
Q = U × A × (T_indoor - T_outdoor)

Where:
Q = Heat loss (Btu/hr)
U = Overall heat transfer coefficient (Btu/hr·ft²·°F)
A = Area (ft²)
T_indoor = Indoor design temperature (typically 70°F)
T_outdoor = Outdoor design temperature (99.6% or 99% winter condition)

BELOW-GRADE HEAT LOSS (Basement walls, slab-on-grade):
Q = F × P × (T_indoor - T_ground)

F = Heat loss coefficient (Btu/hr·ft·°F) from ASHRAE tables
P = Perimeter (ft) for slab or wall length for basement
T_ground = Ground temperature (typically 45-55°F, varies by location)
```

#### Infiltration Heat Loss

```
INFILTRATION:
Q = 1.08 × CFM × (T_indoor - T_outdoor)

CFM_infiltration = (Volume × ACH) / 60

Typical ACH values (heating season, tighter due to closed windows):
├─ New construction, tight: 0.15-0.25 ACH
├─ Average residential: 0.35-0.50 ACH
├─ Old/leaky construction: 0.75-1.5 ACH
└─ Commercial buildings: 0.1-0.3 ACH (if well-sealed)
```

#### Mechanical Ventilation Heat Loss

```
OUTDOOR AIR HEATING:
Q = 1.08 × CFM_OA × (T_indoor - T_outdoor)

Outdoor air requirements per ASHRAE 62.1:
┌────────────────────────┬────────────────────┐
│ Space Type             │ Ventilation Rate   │
├────────────────────────┼────────────────────┤
│ Office space           │ 5 CFM/person +     │
│                        │ 0.06 CFM/ft²       │
│                        │                    │
│ Conference room        │ 5 CFM/person +     │
│                        │ 0.06 CFM/ft²       │
│                        │                    │
│ Retail sales           │ 7.5 CFM/person +   │
│                        │ 0.12 CFM/ft²       │
│                        │                    │
│ Classroom              │ 10 CFM/person +    │
│                        │ 0.12 CFM/ft²       │
│                        │                    │
│ Gymnasium              │ 20 CFM/person      │
└────────────────────────┴────────────────────┘
```

#### Pickup Load (Morning Warm-Up)

```
PICKUP ALLOWANCE:
For buildings with night/weekend setback, additional capacity
needed to bring space to temperature in reasonable time.

Typical pickup factors:
├─ 2-hour warm-up: 20-30% of calculated heat loss
├─ 1-hour warm-up: 40-50% of calculated heat loss
└─ Massive construction: Higher percentage

Q_pickup = Q_design × Pickup_Factor

Example:
Building heat loss: 500,000 Btu/hr
Night setback: 60°F → 70°F in 2 hours
Pickup allowance: 500,000 × 0.25 = 125,000 Btu/hr
Total heating capacity: 500,000 + 125,000 = 625,000 Btu/hr
```

### Total Heating Load Summary

```
TOTAL HEATING LOAD (Btu/hr):

Envelope Losses:
├─ Walls (all orientations): U × A × ΔT
├─ Roof: U × A × ΔT
├─ Windows: U × A × ΔT
├─ Doors: U × A × ΔT
├─ Floors (if above unconditioned): U × A × ΔT
└─ Below-grade (basement/slab): F × P × ΔT

Infiltration:
└─ Infiltration: 1.08 × CFM × ΔT

Ventilation:
└─ Outdoor air: 1.08 × CFM × ΔT

Pickup (if applicable):
└─ Morning warm-up: Q_design × 0.20 to 0.50

Safety Factor: 10-15%
Total Heating Load: Sum all components + pickup + safety factor
```

---

## 4. Psychrometric Processes

### Psychrometric Chart Fundamentals

```
PSYCHROMETRIC PROPERTIES:
├─ Dry bulb temperature (DB): Measured air temperature
├─ Wet bulb temperature (WB): Temperature with evaporative cooling
├─ Dew point temperature (DP): Temperature at 100% RH (saturation)
├─ Relative humidity (RH): %RH = (P_vapor / P_saturation) × 100
├─ Humidity ratio (W): Mass of water vapor per mass of dry air (lb/lb or gr/lb)
├─ Enthalpy (h): Total heat content (Btu/lb or kJ/kg)
└─ Specific volume (v): Volume per mass of dry air (ft³/lb or m³/kg)

Key relationships:
- As RH increases, WB approaches DB
- At 100% RH: DB = WB = DP
- Horizontal line on chart = constant DB
- Vertical line = constant humidity ratio (W)
- Curved line = constant RH
```

### Common HVAC Processes on Psychrometric Chart

```
1. SENSIBLE HEATING (Winter heat only):
   - Horizontal line to the right (increasing DB)
   - No change in humidity ratio (W constant)
   - RH decreases

2. SENSIBLE COOLING (Cooling coil above dewpoint):
   - Horizontal line to the left (decreasing DB)
   - No change in humidity ratio (W constant)
   - RH increases

3. COOLING & DEHUMIDIFICATION (Typical summer cooling):
   - Diagonal line down and to the left
   - DB decreases, W decreases
   - Process line slope = Sensible Heat Ratio (SHR)

4. HUMIDIFICATION (Winter humidifier):
   - Vertical line upward (increasing W)
   - Nearly constant DB (slight decrease if adiabatic)
   - RH increases

5. MIXING TWO AIR STREAMS:
   - Resulting condition lies on straight line between two points
   - Location on line proportional to mass flow rates
```

### Sensible Heat Ratio (SHR)

```
SHR = Sensible Load / Total Load = Q_sensible / (Q_sensible + Q_latent)

Example:
Sensible load: 80,000 Btu/hr
Latent load: 20,000 Btu/hr
Total load: 100,000 Btu/hr
SHR = 80,000 / 100,000 = 0.80

Typical SHR values:
├─ Office spaces: 0.75-0.85 (moderate latent load)
├─ Conference rooms: 0.70-0.75 (high occupancy → more latent)
├─ Computer rooms: 0.95-1.0 (mostly sensible, minimal latent)
└─ Natatoriums (pools): 0.40-0.60 (very high latent load)

Equipment selection must match space SHR for proper dehumidification.
```

### Cooling Coil Performance

```
APPARATUS DEW POINT (ADP):
Theoretical temperature if all air contacted coil surface
(intersection of process line with saturation curve)

BYPASS FACTOR (BF):
Fraction of air that "bypasses" coil without contacting surface
BF = (T_leaving - T_ADP) / (T_entering - T_ADP)

Lower BF = More coil rows = Better dehumidification

Typical bypass factors:
├─ 4-row coil: BF = 0.30-0.40
├─ 6-row coil: BF = 0.20-0.30
├─ 8-row coil: BF = 0.10-0.20
└─ DX coil (A-frame): BF = 0.10-0.20
```

---

## 5. Equipment Selection Criteria

### Cooling Equipment Sizing

```
EQUIPMENT CAPACITY REQUIRED:
Tons = Total Cooling Load (Btu/hr) / 12,000 Btu/hr per ton

kW_cooling = Total Cooling Load (Btu/hr) / 3,412 Btu/hr per kW

Example:
Total cooling load: 450,000 Btu/hr
Equipment size: 450,000 / 12,000 = 37.5 tons

Select equipment: 40-ton unit (next standard size up)

OVERSIZING CAUTION:
├─ Excessive oversizing (>25%) causes:
│   ├─ Short cycling
│   ├─ Poor humidity control
│   ├─ Higher energy consumption
│   └─ Increased wear on compressor
└─ Target: 10-15% oversizing maximum
```

### Equipment Efficiency Ratings

```
COOLING EQUIPMENT EFFICIENCY:

EER (Energy Efficiency Ratio):
EER = Cooling Capacity (Btu/hr) / Power Input (watts)
Measured at standard rating conditions (95°F outdoor, 80°F indoor)

SEER (Seasonal Energy Efficiency Ratio):
SEER = Total seasonal cooling (Btu) / Total seasonal energy (watt-hours)
Accounts for part-load operation and cycling losses
Residential standard (minimum): SEER 14-15 (varies by region)

IEER (Integrated Energy Efficiency Ratio):
Commercial equipment equivalent to SEER
Weighted average of EER at 100%, 75%, 50%, and 25% load

Minimum efficiency requirements (ASHRAE 90.1-2022):
┌─────────────────────────┬────────────────────┐
│ Equipment Type          │ Minimum Efficiency │
├─────────────────────────┼────────────────────┤
│ Air-cooled chiller      │ 9.5 EER / 13 IPLV  │
│ (<150 tons)             │                    │
│                         │                    │
│ Water-cooled chiller    │ 5.5 COP / 6.2 IPLV │
│ (>150 tons)             │                    │
│                         │                    │
│ Packaged rooftop unit   │ 11.0 EER / 13 IEER │
│ (>65,000 Btu/hr)        │                    │
│                         │                    │
│ Split system AC         │ 13.0 SEER minimum  │
│ (Residential)           │                    │
└─────────────────────────┴────────────────────┘

COP (Coefficient of Performance):
COP = Cooling Capacity (Btu/hr) / Power Input (Btu/hr)
COP = EER / 3.412
```

### Heating Equipment Sizing

```
HEATING CAPACITY REQUIRED:
Btu/hr = Total Heating Load (from heat loss calculation)
kW = Btu/hr / 3,412

Furnace/Boiler output rating:
Select equipment with OUTPUT capacity ≥ calculated load

INPUT capacity = OUTPUT capacity / Efficiency

Example:
Heating load: 800,000 Btu/hr
Furnace efficiency (AFUE): 95%
Required input: 800,000 / 0.95 = 842,105 Btu/hr input

HEATING EQUIPMENT EFFICIENCY:

AFUE (Annual Fuel Utilization Efficiency):
├─ Gas furnaces minimum: 80% AFUE (non-condensing)
├─ Gas furnaces high-efficiency: 90-98% AFUE (condensing)
├─ Oil furnaces: 80-87% AFUE
└─ Electric resistance: 100% (but higher operating cost)

Boiler Efficiency:
├─ Non-condensing: 80-85% combustion efficiency
├─ Condensing: 90-98% combustion efficiency
└─ Electric boiler: 99-100%

Heat Pump Efficiency:
HSPF (Heating Seasonal Performance Factor):
├─ Minimum: HSPF 8.2 (varies by region)
├─ High-efficiency: HSPF 10-13
└─ COP at 47°F: 3.0-4.5 typical
```

---

## 6. Duct Sizing Methods

### Equal Friction Method (Most Common)

```
EQUAL FRICTION PRINCIPLE:
Maintain constant pressure drop per 100 ft of duct throughout system

Steps:
1. Determine total CFM required
2. Select main duct velocity (500-900 fpm for low-velocity systems)
3. Size main duct for this velocity
4. Calculate friction rate (inches wc per 100 ft)
5. Size all branches using same friction rate

DUCT VELOCITY GUIDELINES:
┌──────────────────────────┬──────────────────┐
│ Application              │ Velocity (fpm)   │
├──────────────────────────┼──────────────────┤
│ Main ducts               │ 700-900          │
│ Branch ducts             │ 500-700          │
│ Supply outlets           │ 500-750          │
│ Return air               │ 600-800          │
│ Outdoor air intake       │ 500-700          │
└──────────────────────────┴──────────────────┘

FRICTION RATE GUIDELINES:
Typical: 0.08-0.10" wc per 100 ft
Low-velocity systems: 0.05-0.15" wc per 100 ft
High-velocity systems: 0.15-0.30" wc per 100 ft
```

**Duct Sizing Chart Usage**:

```
Using ASHRAE or SMACNA friction chart:
1. Locate CFM on horizontal axis
2. Move vertically to intersection with friction rate curve
3. Read duct diameter (or W×H for rectangular)
4. Round up to next standard duct size

Example:
CFM: 2,000
Friction rate: 0.10" wc/100 ft
From chart: 16" diameter round duct
Standard size: 16" round or 14" × 18" rectangular

Rectangular duct equivalent diameter:
D_eq = 1.30 × [(W × H)^0.625] / [(W + H)^0.25]

Where W = width, H = height (inches)
```

### Velocity Reduction Method

```
VELOCITY REDUCTION PRINCIPLE:
Systematically reduce velocity at each branch takeoff to control noise

Steps:
1. Start with main duct velocity (800-900 fpm typical)
2. At each branch, reduce velocity by 100-200 fpm
3. Continue until outlet velocities reach 500-600 fpm

Advantages:
├─ Lower noise levels at outlets
├─ Reduced pressure losses
└─ Better for noise-sensitive spaces

Disadvantages:
└─ Larger duct sizes downstream (higher cost)
```

### Static Regain Method

```
STATIC REGAIN PRINCIPLE:
Size ducts so velocity reduction converts to static pressure increase,
compensating for friction losses between branches.

Used for:
├─ Long duct runs with multiple branches
├─ High-velocity systems (>2,000 fpm)
└─ Critical applications requiring balanced pressures

Complex method requiring iterative calculations.
```

### Duct Sizing Calculation Example

**Given**:
- Supply air: 5,000 CFM
- Main duct velocity: 800 fpm
- Friction rate: 0.10" wc/100 ft
- Branch 1: 1,500 CFM (30 ft from unit)
- Branch 2: 2,000 CFM (60 ft from unit)
- Branch 3: 1,500 CFM (90 ft from unit)

**Solution (Equal Friction Method)**:

```
MAIN DUCT (0 to Branch 1):
CFM: 5,000
Velocity target: 800 fpm
Area required: 5,000 / 800 = 6.25 ft² = 900 in²
Diameter: √(900 × 4 / π) = 33.8"
Standard size: 34" round or 24" × 36" rectangular

From friction chart at 5,000 CFM, 800 fpm:
Friction rate: 0.092" wc/100 ft
Use 0.10" wc/100 ft for consistency

BRANCH 1:
CFM: 1,500
Friction rate: 0.10" wc/100 ft (same as main)
From chart: 14" diameter
Standard size: 14" round

MAIN DUCT (Branch 1 to Branch 2):
CFM: 5,000 - 1,500 = 3,500
Friction rate: 0.10" wc/100 ft
From chart: 22" diameter
Standard size: 22" round or 18" × 24" rectangular

BRANCH 2:
CFM: 2,000
Friction rate: 0.10" wc/100 ft
From chart: 16" diameter
Standard size: 16" round

MAIN DUCT (Branch 2 to Branch 3):
CFM: 3,500 - 2,000 = 1,500
Friction rate: 0.10" wc/100 ft
From chart: 14" diameter
Standard size: 14" round

BRANCH 3:
CFM: 1,500
Friction rate: 0.10" wc/100 ft
From chart: 14" diameter
Standard size: 14" round

TOTAL DUCT PRESSURE LOSS:
Main duct 0→Branch 1: 30 ft × 0.10/100 = 0.03" wc
Main duct 1→Branch 2: 30 ft × 0.10/100 = 0.03" wc
Main duct 2→Branch 3: 30 ft × 0.10/100 = 0.03" wc
Add fittings losses (elbows, transitions): ~0.15" wc
Total static pressure: ~0.24" wc

Fan static pressure required: 0.24" + coil drop + filter drop
Typical total: 1.0-1.5" wc for low-velocity system
```

---

## 7. Hydronic Pipe Sizing

### Water Flow Rate Calculations

```
WATER FLOW RATE (GPM):
GPM = (Q × 12,000) / (500 × ΔT)

Simplified for HVAC (500 = ρ × c_p):
GPM = Q (tons) × 24 / ΔT (°F)

Or:
GPM = Q (Btu/hr) / (500 × ΔT)

Where:
Q = Cooling/heating load (tons or Btu/hr)
ΔT = Temperature difference between supply and return (°F)
500 = Constant (8.33 lb/gal × 60 min/hr × 1 Btu/lb·°F)

Standard ΔT values:
├─ Chilled water: 10-12°F (42°F supply, 54°F return typical)
├─ Hot water heating: 20°F (180°F supply, 160°F return typical)
└─ Condenser water: 10°F (85°F supply, 95°F return typical)

Example:
Cooling load: 100 tons
Chilled water ΔT: 10°F
GPM = 100 × 24 / 10 = 240 GPM
```

### Pipe Sizing Methods

```
PIPE VELOCITY METHOD:
1. Calculate GPM required
2. Select velocity (typically 4-8 fps for HVAC)
3. Calculate pipe area: A = (GPM × 0.321) / V
4. Select pipe size

Recommended velocities:
├─ 4-6 fps: Typical design range (low noise, erosion)
├─ 6-8 fps: Maximum for most applications
├─ 8-10 fps: High-velocity systems (higher noise/erosion)
└─ <4 fps: May have air separation issues

PRESSURE DROP METHOD:
Target pressure drop: 1-4 ft head per 100 ft pipe

Lower pressure drop = Lower pumping energy
Higher pressure drop = Smaller pipes (lower cost)

Typical design: 2-3 ft head per 100 ft
```

### Pipe Sizing Charts (Copper Type L)

```
┌──────────────────────────────────────────────────────────────┐
│ CHILLED WATER PIPE SIZING (4 fps velocity, 10°F ΔT)         │
├────────┬─────────┬──────────┬──────────┬────────────────────┤
│ Pipe   │ GPM     │ Velocity │ Pressure │ Capacity           │
│ Size   │ Capacity│ (fps)    │ Drop     │ (tons @ 10°F ΔT)  │
│        │         │          │(ft/100ft)│                    │
├────────┼─────────┼──────────┼──────────┼────────────────────┤
│ 1"     │   12    │   4.3    │   6.5    │   5 tons           │
│ 1¼"    │   20    │   4.5    │   5.8    │   8 tons           │
│ 1½"    │   30    │   4.8    │   5.5    │  12 tons           │
│ 2"     │   55    │   5.0    │   4.8    │  23 tons           │
│ 2½"    │   90    │   5.2    │   4.3    │  37 tons           │
│ 3"     │  135    │   5.1    │   3.5    │  56 tons           │
│ 4"     │  250    │   5.0    │   2.5    │ 104 tons           │
│ 5"     │  415    │   5.3    │   2.1    │ 173 tons           │
│ 6"     │  625    │   5.5    │   1.8    │ 260 tons           │
│ 8"     │ 1,200   │   5.8    │   1.3    │ 500 tons           │
│ 10"    │ 2,000   │   6.1    │   1.0    │ 833 tons           │
│ 12"    │ 3,000   │   6.4    │   0.8    │1,250 tons          │
└────────┴─────────┴──────────┴──────────┴────────────────────┘

Note: Actual capacity varies with specific system parameters.
      Chart based on copper Type L pipe, water at 45°F.
```

### Pump Sizing

```
PUMP HEAD CALCULATION:
Total Dynamic Head (TDH) = ΔP_pipes + ΔP_fittings + ΔP_equipment + ΔP_elevation

Components:
├─ Friction loss in pipes (ft head per 100 ft × total length)
├─ Fitting losses (equivalent length method or K-factor)
├─ Equipment pressure drops (coils, heat exchangers, valves)
└─ Elevation changes (if significant)

PUMP POWER (BHP):
BHP = (GPM × TDH) / (3,960 × Pump Efficiency)

Typical pump efficiencies:
├─ Small pumps (<5 HP): 50-65%
├─ Medium pumps (5-20 HP): 65-75%
└─ Large pumps (>20 HP): 75-85%

Example:
Flow: 500 GPM
Total head: 80 ft
Pump efficiency: 70%
BHP = (500 × 80) / (3,960 × 0.70) = 14.4 HP
Select: 15 HP motor (next standard size)
```

---

## 8. Load Calculation Worksheets

### Cooling Load Worksheet Template

```
PROJECT: _______________________  DATE: ____________
SPACE: ________________________  AREA: _______ ft²

OUTDOOR DESIGN CONDITIONS:
Summer DB/WB: _____°F / _____°F (0.4% or 1% values)
Daily range: _____°F

INDOOR DESIGN CONDITIONS:
Temperature: _____°F    Relative Humidity: _____%

═══════════════════════════════════════════════════════

ENVELOPE LOADS:

WALLS:
┌─────────────┬──────┬──────┬──────┬──────┬─────────┐
│ Orientation │ Area │  U   │ CLTD │  =   │ Btu/hr  │
│             │ (ft²)│(Btu/h│ (°F) │      │         │
│             │      │r·ft²│      │      │         │
│             │      │  ·°F)│      │      │         │
├─────────────┼──────┼──────┼──────┼──────┼─────────┤
│ North       │      │      │      │      │         │
│ South       │      │      │      │      │         │
│ East        │      │      │      │      │         │
│ West        │      │      │      │      │         │
└─────────────┴──────┴──────┴──────┴──────┴─────────┘
                                    Subtotal: _______

ROOF:
Area: _____ ft²  U: _____ CLTD: _____  Q = _______

WINDOWS:
┌─────────────┬──────┬──────┬──────┬─────────┐
│ Orientation │ Area │  U   │  ΔT  │ Conduct │
│             │ (ft²)│      │ (°F) │ (Btu/hr)│
├─────────────┼──────┼──────┼──────┼─────────┤
│ North       │      │      │      │         │
│ South       │      │      │      │         │
│ East        │      │      │      │         │
│ West        │      │      │      │         │
└─────────────┴──────┴──────┴──────┴─────────┘
                            Subtotal: _______

SOLAR GAIN:
┌─────────────┬──────┬──────┬──────┬─────────┐
│ Orientation │ Area │ SHGC │ SCL  │  Solar  │
│             │ (ft²)│      │(Btu/h│ (Btu/hr)│
│             │      │      │r·ft²)│         │
├─────────────┼──────┼──────┼──────┼─────────┤
│ North       │      │      │      │         │
│ South       │      │      │      │         │
│ East        │      │      │      │         │
│ West        │      │      │      │         │
└─────────────┴──────┴──────┴──────┴─────────┘
                            Subtotal: _______

INTERNAL GAINS:

PEOPLE:
Number of occupants: _____
Sensible: _____ Btu/hr each × _____ = ________
Latent:   _____ Btu/hr each × _____ = ________

LIGHTING:
Total watts: _____  × 3.412 = ________ Btu/hr

EQUIPMENT:
Description: _______________  Watts: _____ = _______ Btu/hr

VENTILATION/INFILTRATION:

OUTDOOR AIR:
CFM: _____
Sensible: 1.08 × _____ × _____ = ________ Btu/hr
Latent:   0.68 × _____ × _____ = ________ Btu/hr

═══════════════════════════════════════════════════════

LOAD SUMMARY:

Total Sensible Load:                    ________ Btu/hr
Total Latent Load:                      ________ Btu/hr
                                        ───────────────
GRAND TOTAL COOLING LOAD:               ________ Btu/hr

Equipment Size (tons): _______ / 12,000 = _______ tons

Safety Factor (10%): _______
Final Equipment Size: _______ tons

Sensible Heat Ratio (SHR): _______ / _______ = _______
```

---

## 9. Examples and Case Studies

### Complete Example: Small Office Building

**Project Data**:
- Location: Dallas, TX (Climate Zone 3A)
- Office space: 40 ft × 60 ft = 2,400 ft²
- Ceiling height: 10 ft
- Occupancy: 20 people (typical office density)
- Lighting: 0.9 W/ft² (ASHRAE 90.1)
- Equipment: 100W per workstation × 20 = 2,000W
- Hours: 8 AM - 6 PM, Monday-Friday

**Design Conditions**:
- Summer outdoor: 98°F DB / 75°F WB (1% values)
- Winter outdoor: 26°F DB
- Summer indoor: 75°F / 50% RH
- Winter indoor: 70°F / 40% RH

**Construction**:
- Walls: Wood frame, R-13 insulation, U = 0.077
- Roof: Flat roof, R-30 insulation, U = 0.033
- Windows: 20% of wall area (480 ft² total), double-pane low-E, U = 0.30, SHGC = 0.40
- Slab-on-grade floor

**COOLING LOAD CALCULATION**:

```
ENVELOPE LOADS:

Walls (gross area: 2×(40+60)×10 = 2,000 ft²):
Net area (minus windows): 2,000 - 480 = 1,520 ft²
U = 0.077, CLTD = 15°F (average all orientations, 4 PM peak)
Q_walls = 0.077 × 1,520 × 15 = 1,756 Btu/hr

Roof:
Area: 2,400 ft²
U = 0.033, CLTD = 45°F (flat roof, peak afternoon)
Q_roof = 0.033 × 2,400 × 45 = 3,564 Btu/hr

Windows (conduction):
Area: 480 ft²
U = 0.30, ΔT = 98 - 75 = 23°F
Q_windows_cond = 0.30 × 480 × 23 = 3,312 Btu/hr

Windows (solar gain):
Assume: 50% North, 25% East, 25% West (reasonable distribution)
North: 240 ft² × 0.40 SHGC × 25 SCL = 2,400 Btu/hr
East: 120 ft² × 0.40 SHGC × 120 SCL = 5,760 Btu/hr (morning peak)
West: 120 ft² × 0.40 SHGC × 180 SCL = 8,640 Btu/hr (afternoon peak)
Q_windows_solar = 16,800 Btu/hr (peak when West sun hits)

INTERNAL GAINS:

People:
20 occupants × (250 sensible + 200 latent) = 4,500 sens + 4,000 lat
Q_people_sens = 4,500 Btu/hr
Q_people_lat = 4,000 Btu/hr

Lighting:
2,400 ft² × 0.9 W/ft² = 2,160W
Q_lights = 2,160 × 3.412 = 7,370 Btu/hr

Equipment:
2,000W × 0.75 diversity = 1,500W
Q_equipment = 1,500 × 3.412 = 5,118 Btu/hr

VENTILATION:

Outdoor air per ASHRAE 62.1 for office:
Rate: 5 CFM/person + 0.06 CFM/ft²
CFM_OA = (5 × 20) + (0.06 × 2,400) = 100 + 144 = 244 CFM

Sensible:
Q_OA_sens = 1.08 × 244 × (98 - 75) = 6,058 Btu/hr

Latent (using humidity ratio difference):
Outdoor: 98°F DB/75°F WB = W = 105 grains/lb
Indoor: 75°F/50% RH = W = 65 grains/lb
ΔW = 105 - 65 = 40 grains/lb
Q_OA_lat = 0.68 × 244 × 40 = 6,636 Btu/hr

INFILTRATION (minimal during cooling with positive building pressure):
Assume 0.1 ACH (tight construction, minimal)
Volume: 2,400 × 10 = 24,000 ft³
CFM_infil = (24,000 × 0.1) / 60 = 40 CFM
Q_infil = 1.08 × 40 × 23 = 994 Btu/hr (sensible only, small)

═══════════════════════════════════════════════════════

COOLING LOAD SUMMARY:

Envelope:
  Walls:              1,756 Btu/hr
  Roof:               3,564 Btu/hr
  Windows (cond):     3,312 Btu/hr
  Windows (solar):   16,800 Btu/hr
                     ─────────────
  Subtotal:          25,432 Btu/hr

Internal Gains:
  People (sens):      4,500 Btu/hr
  People (lat):       4,000 Btu/hr
  Lighting:           7,370 Btu/hr
  Equipment:          5,118 Btu/hr
                     ─────────────
  Subtotal (sens):   16,988 Btu/hr
  Subtotal (lat):     4,000 Btu/hr

Outdoor Air:
  OA (sensible):      6,058 Btu/hr
  OA (latent):        6,636 Btu/hr
  Infiltration:         994 Btu/hr
                     ─────────────
  Subtotal (sens):    7,052 Btu/hr
  Subtotal (lat):     6,636 Btu/hr

═══════════════════════════════════════════════════════

TOTAL SENSIBLE:      49,472 Btu/hr
TOTAL LATENT:        14,636 Btu/hr
                     ─────────────
GRAND TOTAL:         64,108 Btu/hr

Equipment size: 64,108 / 12,000 = 5.34 tons
Select: 5-ton unit (acceptable) or 6-ton unit (safer)

Sensible Heat Ratio (SHR):
SHR = 49,472 / 64,108 = 0.77

RESULT: Select 5-ton packaged rooftop unit with SHR ≈ 0.75-0.80
        (typical for office applications)
```

**HEATING LOAD CALCULATION**:

```
ENVELOPE LOSSES:

Walls:
1,520 ft² × 0.077 × (70 - 26) = 5,150 Btu/hr

Roof:
2,400 ft² × 0.033 × (70 - 26) = 3,485 Btu/hr

Windows:
480 ft² × 0.30 × (70 - 26) = 6,336 Btu/hr

Slab-on-grade:
Perimeter: 2×(40+60) = 200 ft
F-factor: 0.70 Btu/hr·ft·°F (unheated slab, R-0 insulation)
T_ground: 50°F (Dallas area)
Q_slab = 0.70 × 200 × (70 - 50) = 2,800 Btu/hr

INFILTRATION:

0.3 ACH (heating season, tighter building)
CFM_infil = (24,000 × 0.3) / 60 = 120 CFM
Q_infil = 1.08 × 120 × (70 - 26) = 5,702 Btu/hr

VENTILATION:

244 CFM outdoor air (same as cooling)
Q_vent = 1.08 × 244 × (70 - 26) = 11,594 Btu/hr

═══════════════════════════════════════════════════════

HEATING LOAD SUMMARY:

Walls:               5,150 Btu/hr
Roof:                3,485 Btu/hr
Windows:             6,336 Btu/hr
Slab:                2,800 Btu/hr
Infiltration:        5,702 Btu/hr
Ventilation:        11,594 Btu/hr
                    ─────────────
SUBTOTAL:           35,067 Btu/hr

Pickup allowance (2-hr warmup): 35,067 × 0.25 = 8,767 Btu/hr
Safety factor (10%): 35,067 × 0.10 = 3,507 Btu/hr

═══════════════════════════════════════════════════════

TOTAL HEATING LOAD: 35,067 + 8,767 + 3,507 = 47,341 Btu/hr

Input capacity (95% AFUE furnace): 47,341 / 0.95 = 49,833 Btu/hr

RESULT: Select 50,000 Btu/hr input furnace or heat pump with
        minimum 48,000 Btu/hr heating capacity at 26°F outdoor
```

---

## 10. QA Checklist

```
HVAC LOAD CALCULATION QA CHECKLIST:

☐ DESIGN CONDITIONS
  ☐ Outdoor design temperatures from ASHRAE climate data
  ☐ Correct percentile values used (0.4%, 1%, or 99.6%)
  ☐ Indoor conditions appropriate for space type
  ☐ Humidity levels specified for cooling calculations

☐ BUILDING ENVELOPE
  ☐ Wall U-factors calculated or from tables
  ☐ Roof U-factors appropriate for construction type
  ☐ Window U-factors and SHGC from manufacturer data
  ☐ Areas verified from architectural drawings
  ☐ Below-grade heat transfer properly calculated

☐ INTERNAL GAINS
  ☐ Occupancy density appropriate for space type
  ☐ People load includes sensible and latent components
  ☐ Lighting power density verified (ASHRAE 90.1 or actual)
  ☐ Equipment loads documented with diversity factors
  ☐ Operating schedules considered

☐ VENTILATION
  ☐ Outdoor air rates per ASHRAE 62.1 or 62.2
  ☐ Ventilation heating/cooling loads included
  ☐ Infiltration rates reasonable for construction quality
  ☐ Exhaust air makeup considered

☐ CALCULATIONS
  ☐ All formulas applied correctly
  ☐ Unit conversions checked (Btu/hr, tons, kW)
  ☐ Peak loads identified for equipment sizing
  ☐ Sensible heat ratio (SHR) calculated
  ☐ Safety factors applied appropriately (10-15%)

☐ EQUIPMENT SELECTION
  ☐ Cooling capacity adequate for total load
  ☐ Heating capacity adequate for design condition
  ☐ Equipment efficiency meets code minimum
  ☐ SHR of equipment matches space requirements
  ☐ Equipment oversizing not excessive (<25%)

☐ DISTRIBUTION SYSTEM
  ☐ Duct or pipe sizes calculated
  ☐ Airflow (CFM) or water flow (GPM) determined
  ☐ Pressure drops calculated
  ☐ Fan or pump sized for system requirements

☐ DOCUMENTATION
  ☐ Load calculation worksheets complete
  ☐ Assumptions documented
  ☐ Equipment schedules prepared
  ☐ Calculations signed and sealed (if required)
```

---

## Summary

Proper HVAC load calculations are the foundation of successful system design, ensuring occupant comfort, energy efficiency, and code compliance. This guide provides comprehensive procedures for:

1. **Cooling load calculations** using ASHRAE methods (RTS, CLTD/CLF)
2. **Heating load calculations** accounting for envelope losses and ventilation
3. **Psychrometric analysis** for understanding air conditioning processes
4. **Equipment selection** based on calculated loads and efficiency requirements
5. **Duct sizing** using equal friction and velocity methods
6. **Hydronic pipe sizing** for chilled water and heating systems
7. **Complete design examples** with step-by-step calculations

**Key References**:
- ASHRAE Handbook - Fundamentals (2021 and later editions)
- ASHRAE Standard 90.1-2022: Energy Standard for Buildings
- ASHRAE Standard 62.1-2022: Ventilation for Acceptable Indoor Air Quality
- ACCA Manual J: Residential Load Calculation (8th Edition)
- ACCA Manual D: Duct Design
- SMACNA HVAC Systems - Duct Design

---

*Document maintained by: HVAC Design Engineering Team*
*Next review date: 2026-01-22*
