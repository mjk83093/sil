# Electrical Calculation Templates

**Document Version**: 2.0
**Agent**: Calculation Template Specialist
**Last Updated**: 2025-10-22
**Integration Point**: Templates align with discipline guides and support QA validation

---

## Executive Summary

This document provides comprehensive calculation templates for electrical engineering design following NEC (National Electrical Code) requirements. Templates include step-by-step procedures, formulas, example calculations, and Excel automation equivalents.

**Covered Calculations:**
1. Voltage Drop Calculations (NEC 210.19, 215.2)
2. Short Circuit Calculations (Point-to-Point Method)
3. Load Calculations (NEC Article 220)
4. Lighting Calculations (Lumen Method, Point-by-Point)
5. Panel Schedule Templates with Load Summary

**Integration with QA/QC Workflow:**
- Templates support validation rule development (QA-201-ELEC: Panel load calculations)
- Calculation results populate JSON schedules for automated validation
- Excel formulas enable rapid design iteration and error checking

---

## Table of Contents

1. [Voltage Drop Calculations](#voltage-drop-calculations)
2. [Short Circuit Calculations](#short-circuit-calculations)
3. [Load Calculations (NEC Article 220)](#load-calculations-nec-article-220)
4. [Lighting Calculations](#lighting-calculations)
5. [Panel Schedule Template](#panel-schedule-template)
6. [Excel Automation Guide](#excel-automation-guide)

---

## Voltage Drop Calculations

### Overview

Voltage drop calculations determine the voltage loss in conductors between source and load. NEC recommends maximum 3% voltage drop for branch circuits and 5% total for feeders + branch circuits combined.

**NEC References:**
- **210.19(A)(1) FPN No. 4**: Conductors sized to prevent voltage drop >3% for branch circuits
- **215.2(A)(1) FPN No. 2**: Conductors sized to prevent voltage drop >3% for feeders
- **Combined**: Total voltage drop (feeder + branch) should not exceed 5%

**Key Factors:**
- Circuit current (amperes)
- Circuit length (one-way distance, feet)
- Conductor size (AWG or kcmil)
- Conductor material (copper or aluminum)
- System voltage and phase configuration
- Power factor (for AC circuits)

---

### Single-Phase Voltage Drop Calculation

**Formula:**
```
VD = (2 × K × I × L) / CM

Where:
VD = Voltage drop (volts)
K = Resistivity constant
    - Copper: 12.9 Ω·cmil/ft (at 75°C)
    - Aluminum: 21.2 Ω·cmil/ft (at 75°C)
I = Load current (amperes)
L = One-way circuit length (feet)
CM = Conductor circular mil area (cmil)
2 = Multiplier for two-conductor circuit (hot + neutral)

Voltage Drop Percentage:
VD% = (VD / V_source) × 100
```

**Conductor Circular Mil Areas (Common Sizes):**
| AWG Size | Copper CM | Aluminum CM |
|----------|-----------|-------------|
| 14 AWG   | 4,110     | N/A         |
| 12 AWG   | 6,530     | 6,530       |
| 10 AWG   | 10,380    | 10,380      |
| 8 AWG    | 16,510    | 16,510      |
| 6 AWG    | 26,240    | 26,240      |
| 4 AWG    | 41,740    | 41,740      |
| 2 AWG    | 66,360    | 66,360      |
| 1/0 AWG  | 105,600   | 105,600     |
| 2/0 AWG  | 133,100   | 133,100     |
| 3/0 AWG  | 167,800   | 167,800     |
| 4/0 AWG  | 211,600   | 211,600     |

---

#### Example 1: Single-Phase 120V Branch Circuit

**Given:**
- Load: 15 amperes continuous
- Voltage: 120V single-phase
- Distance: 100 feet (one-way)
- Conductor: 12 AWG copper (6,530 cmil)
- Temperature: 75°C

**Step 1: Calculate Voltage Drop**
```
VD = (2 × K × I × L) / CM
VD = (2 × 12.9 × 15 × 100) / 6,530
VD = 38,700 / 6,530
VD = 5.93 volts
```

**Step 2: Calculate Voltage Drop Percentage**
```
VD% = (VD / V_source) × 100
VD% = (5.93 / 120) × 100
VD% = 4.94%
```

**Step 3: Evaluate Against NEC Recommendation**
- Calculated VD%: 4.94%
- NEC Recommendation: ≤3% for branch circuits
- **Result**: FAILS recommendation (exceeds 3%)

**Step 4: Determine Required Conductor Size**
To meet 3% maximum (3.6V drop at 120V):
```
Required CM = (2 × K × I × L) / VD_max
Required CM = (2 × 12.9 × 15 × 100) / 3.6
Required CM = 38,700 / 3.6
Required CM = 10,750 cmil

Select: 10 AWG copper (10,380 cmil) - closest standard size
```

**Verification with 10 AWG:**
```
VD = (2 × 12.9 × 15 × 100) / 10,380
VD = 38,700 / 10,380
VD = 3.73 volts
VD% = (3.73 / 120) × 100 = 3.11%
```
**Result**: Still slightly exceeds 3%, use 8 AWG (16,510 cmil) for margin:
```
VD = 38,700 / 16,510 = 2.34 volts (1.95%) ✓
```

---

#### Example 2: Single-Phase 240V Circuit

**Given:**
- Load: 30 amperes (electric water heater)
- Voltage: 240V single-phase
- Distance: 80 feet
- Conductor: 10 AWG copper (10,380 cmil)

**Step 1: Calculate Voltage Drop**
```
VD = (2 × 12.9 × 30 × 80) / 10,380
VD = 61,920 / 10,380
VD = 5.97 volts
```

**Step 2: Calculate Percentage**
```
VD% = (5.97 / 240) × 100 = 2.49% ✓
```

**Result**: Meets 3% recommendation

---

### Three-Phase Voltage Drop Calculation

**Formula:**
```
VD = (√3 × K × I × L × PF) / CM

Where:
VD = Voltage drop (volts)
√3 = 1.732 (square root of 3)
K = Resistivity constant (12.9 for copper, 21.2 for aluminum)
I = Load current per phase (amperes)
L = One-way circuit length (feet)
PF = Power factor (0.8-1.0, use 1.0 for resistive loads)
CM = Conductor circular mil area

Voltage Drop Percentage:
VD% = (VD / V_line-to-line) × 100
```

**Note**: Three-phase voltage drop is measured line-to-line, not line-to-neutral.

---

#### Example 3: Three-Phase 208V Circuit

**Given:**
- Load: 50 amperes three-phase
- Voltage: 208V three-phase (120/208V system)
- Distance: 150 feet
- Conductor: 6 AWG copper (26,240 cmil)
- Power factor: 0.85 (motor load)

**Step 1: Calculate Voltage Drop**
```
VD = (√3 × K × I × L × PF) / CM
VD = (1.732 × 12.9 × 50 × 150 × 0.85) / 26,240
VD = 142,289 / 26,240
VD = 5.42 volts
```

**Step 2: Calculate Percentage**
```
VD% = (5.42 / 208) × 100 = 2.61% ✓
```

**Result**: Meets 3% recommendation

---

#### Example 4: Three-Phase 480V Feeder

**Given:**
- Load: 200 amperes three-phase
- Voltage: 480V three-phase
- Distance: 250 feet
- Conductor: 4/0 AWG copper (211,600 cmil)
- Power factor: 0.90

**Step 1: Calculate Voltage Drop**
```
VD = (1.732 × 12.9 × 200 × 250 × 0.90) / 211,600
VD = 1,003,140 / 211,600
VD = 4.74 volts
```

**Step 2: Calculate Percentage**
```
VD% = (4.74 / 480) × 100 = 0.99% ✓
```

**Result**: Well within 3% feeder recommendation

---

### Voltage Drop Template (Calculation Worksheet)

```
PROJECT: _________________________________  DATE: __________
CALCULATED BY: ___________________________  CHECKED BY: __________

CIRCUIT IDENTIFICATION: _______________________________________

INPUT DATA:
┌─────────────────────────────────────────────────────────────┐
│ Load Current (I):              _________ A                  │
│ System Voltage (V):            _________ V                  │
│ Phase Configuration:           [ ] Single-Phase             │
│                                [ ] Three-Phase              │
│ One-Way Distance (L):          _________ feet               │
│ Conductor Material:            [ ] Copper   [ ] Aluminum    │
│ Conductor Size:                _________ AWG/kcmil          │
│ Conductor CM Area:             _________ cmil               │
│ Power Factor (PF):             _________ (default 1.0)      │
│ Temperature:                   _________ °C (default 75°C)  │
└─────────────────────────────────────────────────────────────┘

CALCULATIONS:
┌─────────────────────────────────────────────────────────────┐
│ Resistivity Constant (K):     _________ Ω·cmil/ft           │
│   (Copper: 12.9, Aluminum: 21.2 at 75°C)                   │
│                                                             │
│ Voltage Drop Formula:                                       │
│   Single-Phase:  VD = (2 × K × I × L) / CM                 │
│   Three-Phase:   VD = (√3 × K × I × L × PF) / CM           │
│                                                             │
│ Calculated Voltage Drop (VD): _________ volts              │
│ Voltage Drop Percentage:      _________ %                  │
│                                                             │
│ NEC Recommendation:            ≤3% branch circuits          │
│                                ≤3% feeders                  │
│                                ≤5% total (feeder + branch)  │
│                                                             │
│ Compliance Status:             [ ] PASS   [ ] FAIL          │
└─────────────────────────────────────────────────────────────┘

NOTES/COMMENTS:
___________________________________________________________________
___________________________________________________________________
```

---

## Short Circuit Calculations

### Overview

Short circuit calculations determine the maximum fault current available at equipment locations. This data is critical for:
- Circuit breaker and fuse selection (interrupting capacity)
- Equipment short-circuit current ratings (SCCR)
- Arc flash hazard analysis
- Protective device coordination

**NEC References:**
- **110.9**: Equipment shall have adequate interrupting rating for available fault current
- **110.10**: Component short-circuit current ratings shall not be exceeded
- **110.24**: Service equipment labeling with maximum available fault current

**Calculation Method**: Point-to-Point method (simplified approach suitable for most installations)

---

### Point-to-Point Method

The point-to-point method calculates fault current at each point in the distribution system, accounting for impedance from:
1. Utility source
2. Transformers
3. Conductors
4. Connections and terminations

**Key Principles:**
- Fault current decreases as distance from source increases
- Conductor impedance limits fault current
- Larger conductors = higher fault current at load
- Three-phase bolted fault is the worst-case scenario

---

### Step-by-Step Procedure

#### Step 1: Determine Utility Source Fault Current

Obtain from utility company:
- Available fault current at service point (typically 5,000 to 100,000+ A)
- Source impedance or %Z
- If unavailable, assume infinite bus (conservative approach)

**Typical Utility Fault Currents:**
| Service Type | Typical Fault Current |
|--------------|-----------------------|
| Residential 200A service | 10,000 - 22,000 A |
| Small commercial 400A | 18,000 - 42,000 A |
| Large commercial 2000A+ | 50,000 - 100,000+ A |
| Industrial with dedicated transformer | 20,000 - 65,000 A |

#### Step 2: Calculate Transformer Secondary Fault Current

**Formula:**
```
I_fault = (I_rated × 100) / %Z

Where:
I_fault = Secondary fault current (amperes)
I_rated = Transformer full load current (amperes)
%Z = Transformer impedance (percentage)

Full Load Current (FLA):
Three-phase: I_rated = (kVA × 1000) / (√3 × V_secondary)
Single-phase: I_rated = (kVA × 1000) / V_secondary
```

**Typical Transformer Impedances (%Z):**
| Transformer kVA | Typical %Z |
|-----------------|------------|
| 15 - 75 kVA     | 2.0 - 3.5% |
| 100 - 500 kVA   | 3.5 - 5.5% |
| 750 - 2500 kVA  | 5.0 - 6.5% |

---

#### Example 5: Transformer Secondary Fault Current

**Given:**
- Transformer: 500 kVA, 480V delta secondary, 3-phase
- Transformer impedance: 5.5%

**Step 1: Calculate Full Load Current**
```
I_rated = (kVA × 1000) / (√3 × V_secondary)
I_rated = (500 × 1000) / (1.732 × 480)
I_rated = 500,000 / 831.36
I_rated = 601 A
```

**Step 2: Calculate Secondary Fault Current**
```
I_fault = (I_rated × 100) / %Z
I_fault = (601 × 100) / 5.5
I_fault = 60,100 / 5.5
I_fault = 10,927 A ≈ 11 kA
```

**Result**: Available fault current at transformer secondary = **11,000 A**

---

#### Step 3: Calculate Fault Current Through Conductors

Conductor impedance reduces fault current from transformer to downstream equipment.

**Formula:**
```
I_fault_downstream = I_fault_upstream / √(1 + (f_multiplier)²)

Where:
f_multiplier = (C × L) / (I_fault_upstream × CM)

C = Conductor constant
    - Copper: 12.9 (single-phase), 10.6 (three-phase)
    - Aluminum: 21.2 (single-phase), 17.4 (three-phase)
L = One-way conductor length (feet)
CM = Circular mil area

Simplified formula (when f_multiplier << 1):
I_fault_downstream ≈ I_fault_upstream - (C × L × I_fault_upstream) / CM
```

---

#### Example 6: Point-to-Point Calculation (Complete System)

**System Configuration:**
- Utility: Infinite bus (conservative)
- Transformer: 500 kVA, 480V, 3-phase, %Z = 5.5%
- Main switchboard to Panel A: 100 feet, 500 kcmil copper conductors
- Panel A to load: 50 feet, 3/0 AWG copper conductors

**Point 1: Transformer Secondary (Switchboard)**
```
I_rated = (500 × 1000) / (1.732 × 480) = 601 A
I_fault_switchboard = (601 × 100) / 5.5 = 10,927 A
```

**Point 2: Panel A (100 feet from switchboard)**
```
Conductor: 500 kcmil copper = 500,000 cmil
C = 10.6 (three-phase copper)
L = 100 feet

f_multiplier = (10.6 × 100) / (10,927 × 500,000)
f_multiplier = 1,060 / 5,463,500,000
f_multiplier = 0.000194

I_fault_panel = 10,927 / √(1 + 0.000194²)
I_fault_panel ≈ 10,927 A (negligible drop due to large conductors)
```

**Point 3: Load (50 feet from Panel A)**
```
Conductor: 3/0 AWG copper = 167,800 cmil
C = 10.6
L = 50 feet

f_multiplier = (10.6 × 50) / (10,927 × 167,800)
f_multiplier = 530 / 1,833,550,600
f_multiplier = 0.000289

I_fault_load = 10,927 / √(1 + 0.000289²)
I_fault_load ≈ 10,925 A
```

**Summary:**
| Location | Fault Current |
|----------|---------------|
| Transformer secondary (switchboard) | 10,927 A |
| Panel A (100 ft from switchboard) | 10,927 A |
| Load (50 ft from Panel A) | 10,925 A |

**Equipment Requirements:**
- Switchboard: ≥15 kA AIC rating (typical 22 kA or 65 kA)
- Panel A: ≥15 kA AIC rating
- Branch circuit breakers at load: ≥10 kA AIC rating (standard 10 kA adequate)

---

### Short Circuit Calculation Template

```
PROJECT: _________________________________  DATE: __________
CALCULATED BY: ___________________________  CHECKED BY: __________

POINT-TO-POINT SHORT CIRCUIT CALCULATION

POINT 1: UTILITY SOURCE
┌─────────────────────────────────────────────────────────────┐
│ Utility Fault Current:         _________ A (from utility)   │
│ Or assume infinite bus:        [ ] Yes  [ ] No              │
└─────────────────────────────────────────────────────────────┘

POINT 2: TRANSFORMER SECONDARY
┌─────────────────────────────────────────────────────────────┐
│ Transformer kVA:               _________ kVA                │
│ Secondary Voltage:             _________ V                  │
│ Transformer %Z:                _________ %                  │
│                                                             │
│ Full Load Current (FLA):       _________ A                  │
│ Secondary Fault Current:       _________ A                  │
└─────────────────────────────────────────────────────────────┘

POINT 3: DOWNSTREAM EQUIPMENT (Through Conductors)
┌─────────────────────────────────────────────────────────────┐
│ From: ____________________  To: ____________________        │
│                                                             │
│ Upstream Fault Current:        _________ A                  │
│ Conductor Size:                _________ AWG/kcmil          │
│ Conductor CM:                  _________ cmil               │
│ Conductor Length:              _________ feet               │
│ Conductor Material:            [ ] Copper  [ ] Aluminum     │
│ C Constant:                    _________ (10.6 Cu, 17.4 Al) │
│                                                             │
│ f_multiplier:                  _________                    │
│ Downstream Fault Current:      _________ A                  │
└─────────────────────────────────────────────────────────────┘

EQUIPMENT SHORT-CIRCUIT RATINGS:
┌─────────────────────────────────────────────────────────────┐
│ Equipment                  │ Fault Current │ AIC Required   │
│────────────────────────────│───────────────│────────────────│
│ Switchboard breakers       │ _________ A   │ _________ kA   │
│ Panel breakers             │ _________ A   │ _________ kA   │
│ Branch circuit breakers    │ _________ A   │ _________ kA   │
└─────────────────────────────────────────────────────────────┘

Standard AIC Ratings: 5kA, 10kA, 14kA, 18kA, 22kA, 42kA, 65kA, 100kA

NOTES:
___________________________________________________________________
___________________________________________________________________
```

---

## Load Calculations (NEC Article 220)

### Overview

NEC Article 220 provides methods for calculating electrical loads to properly size service equipment, feeders, and branch circuits. Two primary methods:

1. **Standard Method (NEC 220.40)**: Traditional calculation with specific demand factors
2. **Optional Method (NEC 220.82/220.84)**: Simplified method for dwellings

**NEC References:**
- **220.40**: General lighting and receptacle loads
- **220.82**: Optional calculation for one-family dwellings
- **220.84**: Optional calculation for multifamily dwellings
- **220 Part III**: Commercial and industrial loads

---

### Residential Load Calculation (NEC 220.82 Optional Method)

**Applicable to**: Single-family dwellings, multifamily dwelling units

**Step-by-Step Procedure:**

#### Step 1: General Loads (100% Demand)

Calculate at 100% demand factor:

**A. Heating or Air Conditioning (Largest of):**
- Central air conditioning nameplate rating
- Central electric heating (65% for heat pumps)
- Less than four separately controlled space heating units

**B. All Other Loads:**
- 1500 VA for each 20A small appliance and laundry circuit (minimum 3 circuits)
- 3 VA per square foot for general lighting and receptacles
- All appliances (range, water heater, dryer, dishwasher, disposal, etc.)

#### Step 2: Apply Demand Factors

| Load Type | First 10 kVA | Remainder |
|-----------|--------------|-----------|
| General loads from Step 1 | 100% | 40% |

#### Step 3: Calculate Service Size

```
Total Load (VA) = (First 10,000 VA × 100%) + (Remaining VA × 40%)
Service Amperes = Total Load VA / Voltage
Minimum Service = Round up to standard size (100A, 150A, 200A, etc.)
```

---

#### Example 7: Single-Family Dwelling Load Calculation

**Given:**
- Dwelling: 2,400 sq ft, 4 bedrooms
- Voltage: 240V single-phase service
- Appliances:
  - Electric range: 12 kW (nameplate)
  - Electric water heater: 4.5 kW
  - Electric dryer: 5.5 kW
  - Dishwasher: 1.5 kW
  - Disposal: 0.9 kW
  - Central air conditioning: 18,000 BTU = 5.5 kW (largest HVAC)
  - Electric heat: 15 kW (not selected, AC is larger)

**Step 1: Calculate General Loads (100% Demand)**

**A. Heating/AC (Largest):**
```
Central AC: 5,500 VA
```

**B. Other Loads:**
```
Small appliance circuits:     2 circuits × 1,500 VA =  3,000 VA
Laundry circuit:              1 circuit × 1,500 VA =  1,500 VA
General lighting/receptacles: 2,400 sq ft × 3 VA =    7,200 VA
Electric range:                                      12,000 VA
Electric water heater:                                4,500 VA
Electric dryer:                                       5,500 VA
Dishwasher:                                           1,500 VA
Disposal:                                               900 VA
                                                     ─────────
Subtotal (Other Loads):                              36,100 VA
```

**Total General Loads:**
```
Heating/AC:       5,500 VA
Other Loads:     36,100 VA
                ─────────
Total:           41,600 VA
```

**Step 2: Apply Demand Factors**
```
First 10,000 VA @ 100%:  10,000 × 1.00 = 10,000 VA
Remainder @ 40%:         31,600 × 0.40 = 12,640 VA
                                        ─────────
Total Calculated Load:                  22,640 VA
```

**Step 3: Calculate Service Size**
```
Service Amperes = Total VA / Voltage
Service Amperes = 22,640 / 240
Service Amperes = 94.3 A

Minimum Service Size: 100 A (standard size)
Recommended Service Size: 200 A (allows for future growth)
```

**Panel Schedule Summary:**
```
Service: 200A, 120/240V, 1-phase
Total Connected Load: 41,600 VA
Calculated Demand Load: 22,640 VA
Demand Factor: 54.4%
Spare Capacity: 200A - 94A = 106A (111%)
```

---

### Commercial Load Calculation (NEC 220 Part III)

**Applicable to**: Commercial buildings, offices, retail, industrial

**Key Demand Factors:**

| Load Type | VA per Sq Ft | Demand Factor |
|-----------|--------------|---------------|
| Offices | 3.5 VA/sq ft | 100% |
| Banks | 3.5 VA/sq ft | 100% |
| Retail stores | 3.0 VA/sq ft | 100% |
| Restaurants | 2.0 VA/sq ft | 100% |
| Schools | 3.0 VA/sq ft | 100% |
| Warehouses | 0.25 VA/sq ft | 100% |

**Additional Loads:**
- Receptacle loads: 180 VA per receptacle (or 1.5 VA per sq ft if using general calculation)
- HVAC equipment: 125% of largest motor + 100% of other motors
- Elevator loads: 125% of largest motor
- Continuous loads: 125% of load (NEC 210.20(A))

---

#### Example 8: Small Office Building Load Calculation

**Given:**
- Building: 8,000 sq ft office space
- Voltage: 208V three-phase service
- HVAC: Rooftop unit 30 kW (three-phase)
- Receptacles: 80 outlets
- Lighting: LED fixtures, separate metering
- Miscellaneous: Copier 2 kW, Coffee maker 1.5 kW, Refrigerator 0.8 kW

**Step 1: General Lighting Load**
```
Lighting: 8,000 sq ft × 3.5 VA/sq ft = 28,000 VA
(Note: If actual lighting load is calculated, use greater of calculated or 3.5 VA/sq ft)
```

**Step 2: Receptacle Load**
```
Method A (per receptacle): 80 outlets × 180 VA = 14,400 VA
Method B (per sq ft): 8,000 sq ft × 1.5 VA/sq ft = 12,000 VA

Use Method A: 14,400 VA

Demand Factor per NEC 220.44:
First 10 kVA @ 100%:     10,000 VA
Remainder @ 50%:          4,400 × 0.50 = 2,200 VA
                                        ─────────
Receptacle Demand Load:                 12,200 VA
```

**Step 3: HVAC Load**
```
Rooftop unit: 30,000 VA × 125% (continuous) = 37,500 VA
```

**Step 4: Miscellaneous Loads**
```
Copier:        2,000 VA
Coffee maker:  1,500 VA
Refrigerator:    800 VA
              ─────────
Subtotal:      4,300 VA
```

**Step 5: Total Connected and Demand Loads**
```
                        Connected    Demand
                        ─────────    ──────
General Lighting:        28,000 VA   28,000 VA
Receptacles:             14,400 VA   12,200 VA
HVAC:                    30,000 VA   37,500 VA
Miscellaneous:            4,300 VA    4,300 VA
                        ─────────    ──────
Total:                   76,700 VA   82,000 VA
```

**Step 6: Calculate Service Size**
```
Three-Phase Service Amperes = VA / (√3 × V)
Service Amperes = 82,000 / (1.732 × 208)
Service Amperes = 82,000 / 360.26
Service Amperes = 227.6 A

Minimum Service Size: 250A (standard size)
Recommended Service Size: 400A (allows for future expansion)
```

---

### Load Calculation Template

```
PROJECT: _________________________________  DATE: __________
BUILDING TYPE: [ ] Residential  [ ] Commercial  [ ] Industrial
CALCULATION METHOD: [ ] NEC 220.82 Optional  [ ] NEC 220.40 Standard

BUILDING DATA:
┌─────────────────────────────────────────────────────────────┐
│ Building Area:                 _________ sq ft              │
│ Occupancy Type:                _________________________    │
│ Service Voltage:               _________ V                  │
│ Phase:                         [ ] Single  [ ] Three        │
└─────────────────────────────────────────────────────────────┘

CONNECTED LOADS:
┌─────────────────────────────────────────────────────────────┐
│ Load Description              │ VA/Unit │ Qty  │ Total VA   │
│───────────────────────────────│─────────│──────│────────────│
│ General Lighting (____VA/sf)  │         │      │            │
│ Small Appliance Circuits      │ 1,500   │      │            │
│ Laundry Circuit               │ 1,500   │      │            │
│ Receptacles                   │   180   │      │            │
│ HVAC (nameplate)              │         │      │            │
│ Electric Range                │         │      │            │
│ Water Heater                  │         │      │            │
│ Dryer                         │         │      │            │
│ Other: ________________       │         │      │            │
│ Other: ________________       │         │      │            │
│                               │         │      │            │
│ Total Connected Load:         │         │      │ ________VA │
└─────────────────────────────────────────────────────────────┘

DEMAND LOAD CALCULATION:
┌─────────────────────────────────────────────────────────────┐
│ First 10 kVA @ 100%:          10,000 × 1.00 = ________ VA   │
│ Remainder @ 40%:              ______ × 0.40 = ________ VA   │
│ (or apply applicable demand factors)                        │
│                                                             │
│ Total Calculated Demand Load:              ________ VA     │
└─────────────────────────────────────────────────────────────┘

SERVICE SIZE CALCULATION:
┌─────────────────────────────────────────────────────────────┐
│ Service Amperes = VA / Voltage (or VA / (√3 × V) for 3Ø)   │
│                                                             │
│ Calculated Amperes:            ________ A                   │
│ Minimum Service Size:          ________ A (standard size)   │
│ Recommended Service Size:      ________ A (with margin)     │
│                                                             │
│ Panel Main Breaker:            ________ A                   │
│ Bus Rating:                    ________ A                   │
└─────────────────────────────────────────────────────────────┘
```

---

## Lighting Calculations

### Overview

Lighting calculations ensure adequate illumination levels per IES (Illuminating Engineering Society) recommendations and energy code requirements.

**Methods:**
1. **Lumen Method**: Average illumination over entire area
2. **Point-by-Point Method**: Precise illumination at specific locations

**Key Terms:**
- **Lumen (lm)**: Unit of luminous flux (light output)
- **Lux (lx)** or **Foot-Candle (fc)**: Illuminance (1 fc = 10.76 lux)
- **Coefficient of Utilization (CU)**: Percentage of lamp lumens reaching work surface
- **Light Loss Factor (LLF)**: Accounts for lamp aging and dirt accumulation

---

### Lumen Method (Zonal Cavity Method)

**Formula:**
```
Number of Fixtures = (E × A) / (N × Φ × CU × LLF)

Where:
E = Required illuminance (foot-candles or lux)
A = Area (square feet or square meters)
N = Number of lamps per fixture
Φ = Lumens per lamp (from manufacturer data)
CU = Coefficient of Utilization (from fixture photometric data)
LLF = Light Loss Factor (typically 0.70 to 0.85)
```

**Typical Illuminance Levels (IES Recommendations):**
| Space Type | Foot-Candles | Lux |
|------------|--------------|-----|
| Offices (general) | 30-50 fc | 300-500 lx |
| Conference rooms | 30-50 fc | 300-500 lx |
| Retail stores | 50-100 fc | 500-1000 lx |
| Classrooms | 30-50 fc | 300-500 lx |
| Warehouses | 10-30 fc | 100-300 lx |
| Parking garages | 5-10 fc | 50-100 lx |
| Corridors | 10-20 fc | 100-200 lx |

**Light Loss Factor Components:**
```
LLF = LLD × LDD × BF

Where:
LLD = Lamp Lumen Depreciation (0.85-0.95 for LED, 0.75-0.85 for fluorescent)
LDD = Luminaire Dirt Depreciation (0.85-0.95 depending on environment)
BF = Ballast Factor (0.95-1.0 for electronic ballasts, 1.0 for LED)

Typical Combined LLF: 0.75 (average conditions), 0.70 (dusty), 0.80 (clean)
```

---

#### Example 9: Lumen Method - Open Office Space

**Given:**
- Space: Open office, 40 ft × 60 ft = 2,400 sq ft
- Ceiling height: 9 ft
- Work plane height: 30 inches (2.5 ft)
- Required illuminance: 40 fc (office work)
- Fixture: 2x4 LED troffer, 4000 lumens per fixture
- Coefficient of Utilization (CU): 0.60 (from manufacturer data for room dimensions)
- Light Loss Factor (LLF): 0.75

**Step 1: Calculate Number of Fixtures**
```
N_fixtures = (E × A) / (Φ × CU × LLF)
N_fixtures = (40 fc × 2,400 sq ft) / (4,000 lm × 0.60 × 0.75)
N_fixtures = 96,000 / 1,800
N_fixtures = 53.3 fixtures

Round up: 54 fixtures required
```

**Step 2: Verify Spacing**
```
Area per fixture = 2,400 sq ft / 54 = 44.4 sq ft/fixture

Fixture layout: 9 rows × 6 columns = 54 fixtures
Spacing: 40 ft / 9 = 4.4 ft (along length)
         60 ft / 6 = 10 ft (along width)

Check spacing-to-mounting-height ratio:
Mounting height above work plane = 9 ft - 2.5 ft = 6.5 ft
Spacing ratio = 10 ft / 6.5 ft = 1.54

Typical maximum spacing ratio: 1.5 to 1.8
Result: Adequate spacing ✓
```

**Step 3: Calculate Connected Load**
```
Fixture wattage: 40W per fixture (from manufacturer data)
Total load: 54 fixtures × 40W = 2,160W = 2.16 kW

Watts per square foot: 2,160W / 2,400 sq ft = 0.90 W/sq ft

Energy code allowance (ASHRAE 90.1): 1.0 W/sq ft for offices
Result: Complies with energy code ✓
```

---

### Point-by-Point Method

The point-by-point method calculates exact illuminance at specific locations using inverse square law and cosine law.

**Formula:**
```
E = (I × cos³(θ)) / d²

Where:
E = Illuminance at point (foot-candles or lux)
I = Luminous intensity in candelas (cd) at angle θ
θ = Angle between fixture-to-point line and vertical
d = Distance from fixture to point (feet or meters)
```

This method requires:
- Fixture photometric data (candela distribution curves)
- Precise fixture and point locations
- Typically performed using lighting software (AGi32, Dialux, Relux)

**Use Cases:**
- Task lighting verification (workstation illuminance)
- Exterior lighting (parking lots, building facades)
- Specialized lighting (sports facilities, galleries)

---

### Lighting Calculation Template

```
PROJECT: _________________________________  DATE: __________
SPACE: ___________________________________________

LUMEN METHOD CALCULATION

SPACE DATA:
┌─────────────────────────────────────────────────────────────┐
│ Room Length:                   _________ ft                 │
│ Room Width:                    _________ ft                 │
│ Room Area:                     _________ sq ft              │
│ Ceiling Height:                _________ ft                 │
│ Work Plane Height:             _________ ft (default 30\")   │
│ Mounting Height (above WP):    _________ ft                 │
└─────────────────────────────────────────────────────────────┘

ILLUMINANCE REQUIREMENTS:
┌─────────────────────────────────────────────────────────────┐
│ Required Illuminance (E):      _________ fc (or lux)        │
│ Task Type:                     _________________________    │
│ IES Category:                  _________________________    │
└─────────────────────────────────────────────────────────────┘

FIXTURE DATA:
┌─────────────────────────────────────────────────────────────┐
│ Manufacturer/Model:            _________________________    │
│ Lumens per Fixture (Φ):        _________ lm                 │
│ Wattage per Fixture:           _________ W                  │
│ Coefficient of Utilization:    _________ (from chart)       │
│ Light Loss Factor (LLF):       _________ (default 0.75)     │
└─────────────────────────────────────────────────────────────┘

CALCULATION:
┌─────────────────────────────────────────────────────────────┐
│ N = (E × A) / (Φ × CU × LLF)                                │
│                                                             │
│ Number of Fixtures Required:   _________ fixtures           │
│ Actual Fixtures Installed:     _________ fixtures           │
│                                                             │
│ Fixture Layout:   ____ rows × ____ columns                  │
│ Spacing (length): _________ ft                              │
│ Spacing (width):  _________ ft                              │
│ Spacing-to-MH Ratio: _________ (max 1.5-1.8)               │
└─────────────────────────────────────────────────────────────┘

CONNECTED LOAD:
┌─────────────────────────────────────────────────────────────┐
│ Total Fixtures:                _________ fixtures           │
│ Watts per Fixture:             _________ W                  │
│ Total Connected Load:          _________ W (kW)             │
│                                                             │
│ Lighting Power Density:        _________ W/sq ft            │
│ Energy Code Allowance:         _________ W/sq ft            │
│ Compliance Status:             [ ] PASS   [ ] FAIL          │
└─────────────────────────────────────────────────────────────┘
```

---

## Panel Schedule Template

### Panel Schedule Format

Panel schedules document circuit assignments, loads, and breaker sizes. They serve as:
- Construction documents for electricians
- Operational references for facilities management
- QA validation targets (engineering-drawing-qaqc skill checks for completeness)

**Required Information:**
- Panel identification and location
- Voltage and phase configuration
- Main breaker and bus ratings
- Circuit-by-circuit listings with descriptions, breaker sizes, and loads
- Total connected and demand loads
- Load calculation summary

---

### Panel Schedule Example

```
┌──────────────────────────────────────────────────────────────────────────┐
│                          PANEL SCHEDULE: LP-1                             │
├──────────────────────────────────────────────────────────────────────────┤
│ Location: Electrical Room 101                Voltage: 120/208V, 3Ø, 4W  │
│ Mounting: Surface                            Main Breaker: 100A          │
│ Manufacturer: Square D                       Bus Rating: 100A            │
│ Model: NQOD430M100                           Short Circuit: 22kA AIC     │
│ Fed From: Switchboard SB-1                   Feeder: 3-#1 AWG, 1-#6 AWG │
└──────────────────────────────────────────────────────────────────────────┘

┌──────┬─────────────────────────────┬─────┬──────┬──────┬─────────────────────────────┬─────┬──────┐
│ CKT  │ DESCRIPTION                 │ BKR │ POLE │ LOAD │ DESCRIPTION                 │ BKR │ CKT  │
│      │                             │ (A) │      │ (VA) │                             │ (A) │      │
├──────┼─────────────────────────────┼─────┼──────┼──────┼─────────────────────────────┼─────┼──────┤
│  A1  │ Office Lighting - North     │  20 │  1   │ 1800 │ Office Lighting - South     │  20 │  A2  │
│  A3  │ Conference Room Lighting    │  20 │  1   │ 1600 │ Corridor Lighting           │  20 │  A4  │
│  A5  │ Exit Signs & Emergency Ltg  │  20 │  1   │  400 │ Exterior Building Lighting  │  20 │  A6  │
│      │                             │     │      │      │                             │     │      │
│  B1  │ Receptacles - North Wall    │  20 │  1   │ 1440 │ Receptacles - South Wall    │  20 │  B2  │
│  B3  │ Receptacles - East Wall     │  20 │  1   │ 1440 │ Receptacles - West Wall     │  20 │  B4  │
│  B5  │ Receptacles - GFCI (Break)  │  20 │  1   │ 1440 │ Server Room Receptacles     │  20 │  B6  │
│      │                             │     │      │      │                             │     │      │
│  C1  │ HVAC Unit - RTU-1           │  30 │  2   │ 7200 │ HVAC Unit - RTU-2           │  30 │  C3  │
│  C5  │ Exhaust Fan - EF-1          │  20 │  1   │ 1200 │ Exhaust Fan - EF-2          │  20 │  C6  │
│      │                             │     │      │      │                             │     │      │
│  D1  │ Water Cooler                │  20 │  1   │ 1200 │ Refrigerator                │  20 │  D2  │
│  D3  │ Microwave                   │  20 │  1   │ 1500 │ Coffee Maker                │  20 │  D4  │
│  D5  │ Copier/Printer              │  20 │  1   │ 1800 │ SPARE                       │  20 │  D6  │
│      │                             │     │      │      │                             │     │      │
│  E1  │ SPARE                       │  20 │  1   │    0 │ SPARE                       │  20 │  E2  │
│  E3  │ SPARE                       │  20 │  1   │    0 │ SPARE                       │  20 │  E4  │
└──────┴─────────────────────────────┴─────┴──────┴──────┴─────────────────────────────┴─────┴──────┘

┌──────────────────────────────────────────────────────────────────────────┐
│                         LOAD SUMMARY                                      │
├──────────────────────────────────────────────────────────────────────────┤
│ Total Connected Load:                                     28,020 VA      │
│ Calculated Demand Load (per NEC 220):                    21,315 VA      │
│ Main Breaker Rating:                                         100 A       │
│ Panel Capacity (@ 80%):                        (80A × 208V × 1.732) =    │
│                                                           28,800 VA      │
│ Load Percentage:                   (21,315 VA / 28,800 VA) = 74.0%     │
│                                                                          │
│ Load Calculation Method:  NEC 220 Part III Commercial                   │
│ Load Calculation Date:    2024-06-01                                    │
│ Calculated By:            JKL, PE                                       │
└──────────────────────────────────────────────────────────────────────────┘

NOTES:
1. All wiring per NEC 2023
2. Minimum 12 AWG copper conductors for 20A circuits
3. Continuous loads factored at 125% per NEC 210.20(A)
4. Equipment grounding conductor per NEC 250.122
5. Panel clearance: 36\" min per NEC 110.26(A)
```

---

## Excel Automation Guide

### Excel Formulas for Electrical Calculations

Automating calculations in Excel enables rapid design iteration and reduces errors.

#### Voltage Drop Formula (Single-Phase)

```excel
=((2 * K * I * L) / CM)

Where:
K = 12.9 (copper) or 21.2 (aluminum) - Cell reference
I = Load current (amperes) - Cell reference
L = One-way distance (feet) - Cell reference
CM = Circular mil area - Cell reference

Voltage Drop Percentage:
=(VD / V_source) * 100
```

**Example Excel Setup:**

| Cell | Label | Formula | Value |
|------|-------|---------|-------|
| B2 | Material | Dropdown: Copper/Aluminum | Copper |
| B3 | K Constant | =IF(B2="Copper",12.9,21.2) | 12.9 |
| B4 | Current (A) | User input | 15 |
| B5 | Length (ft) | User input | 100 |
| B6 | AWG Size | Dropdown: 14,12,10,8... | 12 |
| B7 | CM Area | =VLOOKUP(B6,AWG_Table,2,FALSE) | 6530 |
| B8 | Voltage Drop (V) | =(2*B3*B4*B5)/B7 | 5.93 |
| B9 | Source Voltage (V) | User input | 120 |
| B10 | VD Percentage | =(B8/B9)*100 | 4.94% |
| B11 | NEC Compliant? | =IF(B10<=3,"PASS","FAIL") | FAIL |

**AWG Lookup Table (separate sheet):**
| AWG | CM Area |
|-----|---------|
| 14  | 4110    |
| 12  | 6530    |
| 10  | 10380   |
| 8   | 16510   |
| ... | ...     |

---

#### Load Calculation Formula (Residential)

```excel
=IF(Total_Load<=10000, Total_Load, 10000 + (Total_Load-10000)*0.4)

Connected Load:
=SUM(Range_of_loads)

Demand Load (NEC 220.82):
=IF(B20<=10000, B20, 10000 + (B20-10000)*0.4)

Service Amperes:
=Demand_Load / Voltage
```

**Example Residential Load Calculation Spreadsheet:**

| Item | Connected Load (VA) | Formula |
|------|---------------------|---------|
| General Lighting (sq ft × 3) | =B2*3 | 7200 |
| Small Appliance (2 circuits) | =2*1500 | 3000 |
| Laundry (1 circuit) | =1*1500 | 1500 |
| Range | User input | 12000 |
| Dryer | User input | 5500 |
| Water Heater | User input | 4500 |
| HVAC (largest) | User input | 5500 |
| **Total Connected Load** | =SUM(above) | **39200** |
| | | |
| **Demand Load Calculation** | | |
| First 10 kVA @ 100% | =MIN(B15,10000) | 10000 |
| Remainder @ 40% | =IF(B15>10000,(B15-10000)*0.4,0) | 11680 |
| **Total Demand Load** | =B17+B18 | **21680** |
| | | |
| Service Voltage | User input | 240 |
| **Service Amperes** | =B20/B22 | **90.3 A** |
| **Minimum Service** | =CEILING(B24,50) | **100 A** |

---

#### Panel Schedule Load Summary

```excel
Total Connected Load:
=SUM(Circuit_Load_Range)

Demand Load (with demand factors):
=SUM(Lighting_Circuits*DF1, Receptacle_Circuits*DF2, HVAC_Circuits*DF3, ...)

Panel Capacity:
=Main_Breaker * Voltage * SQRT(3) * 0.8  (for three-phase)
=Main_Breaker * Voltage * 0.8  (for single-phase)

Load Percentage:
=(Demand_Load / Panel_Capacity) * 100
```

**Conditional Formatting:**
- Load % < 80%: Green (acceptable)
- Load % 80-100%: Yellow (at capacity)
- Load % > 100%: Red (overloaded, increase panel size)

---

### Excel Template Structure

**Workbook Tabs:**
1. **Voltage Drop Calculator** - Single/three-phase calculations
2. **Short Circuit** - Point-to-point fault current
3. **Load Calculation** - Residential/commercial load calculations
4. **Lighting Calculation** - Lumen method calculations
5. **Panel Schedules** - Individual panel templates
6. **Reference Tables** - AWG sizes, NEC tables, material properties

**Key Features:**
- Data validation dropdowns (conductor sizes, materials, occupancy types)
- Named ranges for formulas
- Conditional formatting for pass/fail indicators
- Print-optimized formatting for submittal documents
- Locked cells to prevent accidental formula changes

---

## Integration with QA/QC Workflow

### How Calculation Templates Support Validation

**SKILL.md Integration Points:**

1. **Load Calculation → Panel Schedule Validation**
   - Template output: Demand load, load calculation method
   - JSON field: `schedules.panel_schedule.load_calculation_included`, `load_calculation_method`
   - QA Rule: QA-201-ELEC (Verify panel load calculations included)

2. **Voltage Drop → Conductor Sizing Validation**
   - Template output: Conductor size, voltage drop percentage
   - JSON field: `schedules.panel_schedule.circuits[].wire_size`
   - QA Rule: Ensure conductor sizes meet NEC recommendations

3. **Short Circuit → Equipment Rating Validation**
   - Template output: Fault current at equipment
   - JSON field: `schedules.panel_schedule.short_circuit_rating`
   - QA Rule: Verify equipment AIC ratings adequate for fault current

4. **Lighting → Energy Code Compliance Validation**
   - Template output: Lighting power density (W/sq ft)
   - JSON field: `code_compliance.energy_code_compliant`
   - QA Rule: Verify lighting load ≤ energy code allowance

**Workflow:**
```
Calculation Template (Excel)
    ↓ Generate results
Panel Schedule (Drawing)
    ↓ Extract to JSON
QA Validation (engineering-drawing-qaqc skill)
    ↓ Validate against rules
Compliance Report (CSV/PDF)
```

---

## Appendix: Quick Reference Tables

### NEC Voltage Drop Recommendations

| Circuit Type | Maximum Recommended VD |
|--------------|------------------------|
| Branch circuits | 3% |
| Feeders | 3% |
| Combined (feeder + branch) | 5% |

### Conductor Ampacity (75°C, Copper, NEC Table 310.16)

| AWG | Ampacity (A) |
|-----|--------------|
| 14  | 20           |
| 12  | 25           |
| 10  | 35           |
| 8   | 50           |
| 6   | 65           |
| 4   | 85           |
| 2   | 115          |
| 1/0 | 150          |
| 2/0 | 175          |
| 3/0 | 200          |
| 4/0 | 230          |

### Standard Breaker Sizes (NEC 240.6(A))

15A, 20A, 25A, 30A, 35A, 40A, 45A, 50A, 60A, 70A, 80A, 90A, 100A, 110A, 125A, 150A, 175A, 200A, 225A, 250A, 300A, 350A, 400A, 450A, 500A, 600A, 700A, 800A, 1000A, 1200A, 1600A, 2000A, 2500A, 3000A, 4000A, 5000A, 6000A

### Continuous Load Factors (NEC 210.20, 215.3)

| Load Type | Factor |
|-----------|--------|
| Continuous loads (≥3 hours) | 125% |
| Non-continuous loads | 100% |
| Motor loads (largest motor) | 125% |
| Other motors | 100% |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-06-01 | Calculation Template Specialist | Initial document |
| 2.0 | 2025-10-22 | Calculation Template Specialist | Enhanced with Excel automation, QA integration, comprehensive examples |

**Next Review**: 2026-01-01

---

**End of Document**
