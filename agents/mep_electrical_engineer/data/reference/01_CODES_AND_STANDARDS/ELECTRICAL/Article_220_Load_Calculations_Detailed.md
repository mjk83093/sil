# NEC 2023 Article 220 - Branch-Circuit, Feeder, and Service Load Calculations (DETAILED)

## Document Information

**NEC Article**: 220
**Title**: Branch-Circuit, Feeder, and Service Load Calculations
**Edition**: NFPA 70-2023 National Electrical Code
**Scope**: Methods for calculating electrical loads for sizing branch circuits, feeders, and services
**Last Updated**: 2025-01-22
**Curator**: EE_AI Platform Reference Library

---

## Table of Contents

1. [Article Overview](#article-overview)
2. [Part I - General (220.1-220.5)](#part-i---general)
3. [Part II - Branch-Circuit Load Calculations (220.10-220.18)](#part-ii---branch-circuit-load-calculations)
4. [Part III - Feeder and Service Load Calculations (220.40-220.61)](#part-iii---feeder-and-service-load-calculations)
5. [Part IV - Optional Feeder and Service Load Calculations (220.80-220.87)](#part-iv---optional-calculations)
6. [Worked Examples](#worked-examples)
7. [Integration with QA/QC Rules](#integration-with-qaqc-rules)
8. [Quick Reference Tables](#quick-reference-tables)

---

## Article Overview

Article 220 provides methods for calculating electrical loads for dwelling units, multifamily dwellings, commercial buildings, industrial facilities, and special occupancies. The article is organized into four parts:

- **Part I**: General requirements and definitions
- **Part II**: Branch circuit load calculations (receptacles, lighting, appliances)
- **Part III**: Standard method for feeder and service calculations
- **Part IV**: Optional calculation methods (simplified for specific occupancies)

**Key Concept**: Article 220 applies **demand factors** to recognize that not all loads operate simultaneously. This prevents oversizing electrical systems while maintaining safety.

---

## Part I - General (220.1-220.5)

### 220.1 Scope

Article 220 covers:
- Branch circuit load calculations
- Feeder load calculations
- Service load calculations
- Methods: Standard calculation (Part III) and Optional calculation (Part IV)

### 220.3 Computation of Branch Circuit Loads

**Volt-Amperes (VA) vs. Watts (W)**:
- Calculations are performed in **volt-amperes (VA)** not watts
- For resistive loads: VA = Watts
- For inductive/capacitive loads: VA > Watts (due to power factor)

**Formula for Load Current**:
```
Single-phase: I = VA / V
Three-phase: I = VA / (√3 × V × 1.732)
```

### 220.5 Calculations

**Rounding Rules**:
- Fractions of an ampere ≥ 0.5 shall be permitted to be rounded up
- For load calculations, round to two decimal places for intermediate steps
- Final amperage rating must match standard OCPD sizes (240.6)

**Units**:
- All calculations in volt-amperes (VA) or kilovolt-amperes (kVA)
- Convert to amperes using voltage

**Voltage**:
- Nominal system voltage shall be used (120V, 208V, 240V, 277V, 480V)
- Do not use actual measured voltage

---

## Part II - Branch-Circuit Load Calculations (220.10-220.18)

### 220.10 General

Branch circuits supply:
- Lighting outlets
- Receptacle outlets
- Appliances
- Motors
- Other utilization equipment

### 220.12 General Lighting Loads by Occupancy

**Method**: Calculate lighting load based on square footage and occupancy type.

**Formula**:
```
General Lighting Load (VA) = Square Feet × Unit Load (VA/ft²)
```

#### Table 220.12 - General Lighting Loads by Occupancy Type

```
┌─────────────────────────────────────────────┬─────────────────────┐
│ Type of Occupancy                           │ Unit Load (VA/ft²)  │
├─────────────────────────────────────────────┼─────────────────────┤
│ Armories and auditoriums                    │ 1                   │
│ Banks                                       │ 3.5                 │
│ Barber shops and beauty parlors             │ 3                   │
│ Churches                                    │ 1                   │
│ Clubs                                       │ 2                   │
│ Court rooms                                 │ 2                   │
│ Dwelling units                              │ 3                   │
│ Garages - commercial (storage)              │ 0.5                 │
│ Hospitals                                   │ 2                   │
│ Hotels and motels, including apartment      │                     │
│   houses without provisions for cooking     │ 2                   │
│ Industrial commercial (loft) buildings      │ 2                   │
│ Lodge rooms                                 │ 1.5                 │
│ Office buildings                            │ 1                   │
│ Restaurants                                 │ 2                   │
│ Schools                                     │ 3                   │
│ Stores                                      │ 3                   │
│ Warehouses (storage)                        │ 0.25                │
│ In any of the above occupancies except      │                     │
│   one-family dwellings and individual       │                     │
│   dwelling units of two-family and          │                     │
│   multifamily dwellings:                    │                     │
│   Assembly halls and auditoriums            │ 1                   │
│   Halls, corridors, closets, stairways      │ 0.5                 │
│   Storage spaces                            │ 0.25                │
└─────────────────────────────────────────────┴─────────────────────┘
```

**Example - Dwelling Unit**:
```
Given: 2,500 square feet dwelling
Calculation: 2,500 ft² × 3 VA/ft² = 7,500 VA general lighting load
```

**Example - Office Building**:
```
Given: 10,000 square feet office space
Calculation: 10,000 ft² × 1 VA/ft² = 10,000 VA general lighting load
```

**Example - Restaurant**:
```
Given: 3,200 square feet restaurant
Calculation: 3,200 ft² × 2 VA/ft² = 6,400 VA general lighting load
```

### 220.14 Other Loads - All Occupancies

**Additional loads beyond general lighting:**

#### (A) Specific Appliances or Loads

Count at **nameplate rating** in volt-amperes:
- Electric ranges and cooking appliances (see 220.55)
- Motors (see Article 430)
- Air conditioning (see Article 440)
- Fixed electric space heating (see Article 424)

#### (B) Electric Dryers

**Load per unit**:
- Dwelling unit electric dryer: **5,000 VA or nameplate rating** (whichever is larger)

#### (C) Electric Cooking Appliances

**Dwelling unit cooking appliances**:
- Electric ranges, wall-mounted ovens, counter-mounted cooking units
- See 220.55 for demand factors (Table 220.55)

#### (D) Electric Vehicle Supply Equipment (EVSE)

**Load calculation**:
- Count at **maximum output rating** of the EVSE
- Apply diversity per 220.57 for multiple charging stations

#### (E) Motor Loads

**Motors** (see Article 430):
- Use 125% of largest motor FLA plus 100% of all other motors

#### (F) Heating Loads

**Fixed electric space heating** (see Article 424):
- Count at **100% of total connected load**
- No diversity factors unless specifically permitted

#### (G) Air Conditioning

**Air conditioning and refrigeration equipment** (see Article 440):
- Use 125% of largest motor-compressor plus 100% of all others
- Compare heating vs. cooling - count larger (not both)

#### (H) Largest Motor

**125% Rule**:
- Add **25% to the largest motor** included in the calculation
- Applied in addition to motor nameplate rating

**Example**:
```
Given: 3 HP motor (21 A FLA), 1 HP motor (8 A FLA), 1/2 HP motor (4.9 A FLA)
Calculation:
  - Largest motor: 21 A × 1.25 = 26.25 A
  - Other motors: 8 A + 4.9 A = 12.9 A
  - Total motor load: 26.25 + 12.9 = 39.15 A
```

#### (I) Track Lighting

**Load**:
- Track lighting: **150 VA for every 2 feet** of track or fraction thereof
- Apply additional load per 220.43(B)

### 220.16 Loads for Additions to Existing Installations

**New loads added to existing service**:
1. Calculate existing load (actual connected load or previous calculation)
2. Add new load
3. Total must not exceed service rating

**Alternative**: Use 220.87 for existing dwellings

### 220.18 Maximum Loads

**Shall not exceed**:
- Branch circuit rating (210.19, 210.20)
- Feeder rating (215.2, 215.3)
- Service rating (230.42)

---

## Part III - Feeder and Service Load Calculations (220.40-220.61)

### 220.40 General - Standard Calculation Method

**Purpose**: Calculate minimum required capacity for feeders and services.

**Method**: Sum all loads, apply demand factors where permitted.

**Steps**:
1. Calculate general lighting load (220.12)
2. Add required receptacle loads
3. Add appliance loads (ranges, dryers, etc.)
4. Add heating or air conditioning (larger load)
5. Add motor loads with 125% on largest
6. Apply demand factors where applicable
7. Convert to amperes using nominal voltage

### 220.42 General Lighting Demand Factors

**Table 220.42** - Lighting Load Demand Factors

```
┌─────────────────────────────────────────────┬─────────────────────┐
│ Type of Occupancy                           │ Portion of Lighting │
│                                             │ Load to Which       │
│                                             │ Demand Factor       │
│                                             │ Applies (VA)        │
├─────────────────────────────────────────────┼─────────────────────┤
│ Dwelling units                              │                     │
│   First 3,000 or less at                    │ 100%                │
│   From 3,001 to 120,000 at                  │ 35%                 │
│   Remainder over 120,000 at                 │ 25%                 │
├─────────────────────────────────────────────┼─────────────────────┤
│ Hospitals                                   │                     │
│   First 50,000 or less at                   │ 40%                 │
│   Remainder over 50,000 at                  │ 20%                 │
├─────────────────────────────────────────────┼─────────────────────┤
│ Hotels and motels, including apartment      │                     │
│ houses without provision for cooking        │                     │
│   First 20,000 or less at                   │ 50%                 │
│   From 20,001 to 100,000 at                 │ 40%                 │
│   Remainder over 100,000 at                 │ 30%                 │
├─────────────────────────────────────────────┼─────────────────────┤
│ Warehouses (storage)                        │                     │
│   First 12,500 or less at                   │ 100%                │
│   Remainder over 12,500 at                  │ 50%                 │
├─────────────────────────────────────────────┼─────────────────────┤
│ All others                                  │ Total VA × 100%     │
└─────────────────────────────────────────────┴─────────────────────┘
```

**Example - Dwelling Unit Lighting Load**:
```
Given: 12,000 VA total lighting load
Calculation:
  First 3,000 VA × 100% = 3,000 VA
  Remaining 9,000 VA × 35% = 3,150 VA
  Demand lighting load = 3,000 + 3,150 = 6,150 VA
```

**Example - Large Dwelling Unit**:
```
Given: 25,000 VA total lighting load
Calculation:
  First 3,000 VA × 100% = 3,000 VA
  From 3,001-120,000: 22,000 VA × 35% = 7,700 VA
  Demand lighting load = 3,000 + 7,700 = 10,700 VA
```

### 220.43 Show-Window and Track Lighting

**Show-Window Lighting**:
- **200 VA per linear foot** of show window measured horizontally
- No demand factors applied

**Track Lighting**:
- **150 VA per 2 feet** of track or fraction thereof
- No additional demand factors

### 220.44 Receptacle Loads - Other Than Dwelling Units

**Receptacle Load Calculation**:

For non-dwelling units, calculate receptacle loads based on:

**Method 1 - Per Receptacle**:
- **180 VA per receptacle outlet** (includes single, duplex, or triplex)

**Method 2 - General Use Receptacles**:
- Apply demand factor per Table 220.44

#### Table 220.44 - Demand Factors for Non-Dwelling Receptacle Loads

```
┌─────────────────────────────────────┬─────────────────────┐
│ Portion of Receptacle Load          │ Demand Factor (%)   │
├─────────────────────────────────────┼─────────────────────┤
│ First 10 kVA or less at             │ 100%                │
│ Remainder over 10 kVA at            │ 50%                 │
└─────────────────────────────────────┴─────────────────────┘
```

**Example - Office Building Receptacles**:
```
Given: 100 receptacles in office building
Calculation:
  Total receptacle load: 100 × 180 VA = 18,000 VA = 18 kVA
  First 10 kVA × 100% = 10,000 VA
  Remaining 8 kVA × 50% = 4,000 VA
  Demand receptacle load = 10,000 + 4,000 = 14,000 VA
```

**Fixed Multioutlet Assemblies**:
- Where appliances are unlikely to be used simultaneously: **180 VA per 5 feet** or fraction
- Where appliances are likely to be used simultaneously: **180 VA per 1 foot**

### 220.50 Motors

**Motor Load Calculation**:
1. Include all motor loads at **full-load current (FLC)**
2. Add **25% to the largest motor**
3. Use NEC Article 430 for motor FLC values (Tables 430.247-430.250)

**Formula**:
```
Motor Load = (Largest Motor FLC × 1.25) + (Sum of all other motor FLCs)
```

### 220.51 Fixed Electric Space Heating

**Heating Load**:
- Fixed electric space heating: **100% of total connected load**
- No diversity or demand factors unless specifically permitted
- Unit heaters, baseboard heaters, radiant heating

**Example**:
```
Given: Three 5 kW baseboard heaters, two 3 kW unit heaters
Calculation:
  Total heating load = (3 × 5 kW) + (2 × 3 kW) = 21 kW
  Demand heating load = 21 kW × 100% = 21 kW = 21,000 VA
```

### 220.53 Appliance Load - Dwelling Unit(s)

**Small Appliance Branch Circuit Load**:
- **1,500 VA per 2-wire small appliance branch circuit**
- Minimum 2 circuits required per 210.11(C)(1)
- Includes kitchen, dining room, breakfast room, pantry

**Laundry Branch Circuit Load**:
- **1,500 VA per laundry circuit**
- Required per 210.11(C)(2)

**Total Small Appliance + Laundry**:
- Typical dwelling: (2 × 1,500 VA) + (1 × 1,500 VA) = 4,500 VA

**Demand Factors**:
- Small appliance and laundry loads included in general lighting demand (Table 220.42)

### 220.55 Electric Ranges and Other Cooking Appliances - Dwelling Unit(s)

**Purpose**: Apply demand factors recognizing cooking appliances are not used at full capacity simultaneously.

#### Table 220.55 - Demand Factors and Loads for Electric Ranges, Wall-Mounted Ovens, Counter-Mounted Cooking Units, and Other Household Cooking Appliances over 1.75 kW Rating

**Column A - Maximum Demand (kW) for Ranges Not Over 12 kW Rating**

```
┌──────────────────┬─────────────────┬─────────────────────────────────────────┐
│ Number of        │ Maximum Demand  │ Demand Factor (%)                       │
│ Appliances       │ (kW) Column A   │ (Note: Column A shows actual demand)    │
├──────────────────┼─────────────────┼─────────────────────────────────────────┤
│ 1                │ 8               │ 80% (8 kW demand for 10 kW range)       │
│ 2                │ 11              │ 55% (per range)                         │
│ 3                │ 14              │ 47% (per range)                         │
│ 4                │ 17              │ 43% (per range)                         │
│ 5                │ 20              │ 40% (per range)                         │
│ 6                │ 21              │ 35% (per range)                         │
│ 7                │ 22              │ 31% (per range)                         │
│ 8                │ 23              │ 29% (per range)                         │
│ 9                │ 24              │ 27% (per range)                         │
│ 10               │ 25              │ 25% (per range)                         │
│ 11               │ 26              │ 24% (per range)                         │
│ 12               │ 27              │ 23% (per range)                         │
│ 13               │ 28              │ 22% (per range)                         │
│ 14               │ 29              │ 21% (per range)                         │
│ 15               │ 30              │ 20% (per range)                         │
│ 16               │ 31              │ 19% (per range)                         │
│ 17               │ 32              │ 19% (per range)                         │
│ 18               │ 33              │ 18% (per range)                         │
│ 19               │ 34              │ 18% (per range)                         │
│ 20               │ 35              │ 18% (per range)                         │
│ 21               │ 36              │ 17% (per range)                         │
│ 22               │ 37              │ 17% (per range)                         │
│ 23               │ 38              │ 17% (per range)                         │
│ 24               │ 39              │ 16% (per range)                         │
│ 25               │ 40              │ 16% (per range)                         │
│ 26-30            │ 15 + 1 kW per   │                                         │
│                  │ range over 25   │                                         │
│ 31-40            │ 25 + 3/4 kW per │                                         │
│                  │ range over 30   │                                         │
│ 41-50            │ 32.5 + 3/4 kW   │                                         │
│                  │ per range 40    │                                         │
│ 51-60            │ 40 + 3/4 kW per │                                         │
│                  │ range over 50   │                                         │
│ 61 and over      │ 47.5 + 3/4 kW   │                                         │
│                  │ per range 60    │                                         │
└──────────────────┴─────────────────┴─────────────────────────────────────────┘
```

**Note 1**: Over 12 kW through 27 kW ranges - Increase Column A demand by 5% for each kW over 12 kW.

**Note 2**: Over 1.75 kW through 8.75 kW appliances - Use Column C (See below).

**Note 3**: Neutral demand - For ranges, wall ovens, and counter cooktop units, neutral load is 70% of the demand per Column A.

**Column C - Demand Factor (%) for Appliances Rated 1.75 kW to 8.75 kW**

```
┌──────────────────┬─────────────────┐
│ Number of        │ Demand Factor   │
│ Appliances       │ (%)             │
├──────────────────┼─────────────────┤
│ 1                │ 80%             │
│ 2                │ 75%             │
│ 3                │ 70%             │
│ 4                │ 66%             │
│ 5                │ 62%             │
│ 6 and over       │ 59%             │
└──────────────────┴─────────────────┘
```

**Example 1 - Single-Family Dwelling (One 12 kW Range)**:
```
Given: One 12 kW electric range
Table 220.55, Column A, 1 appliance = 8 kW demand
Demand load = 8 kW = 8,000 VA
```

**Example 2 - Apartment Building (20 units, each with 12 kW range)**:
```
Given: 20 × 12 kW ranges
Table 220.55, Column A, 20 appliances = 35 kW demand
Demand load = 35 kW = 35,000 VA
Total connected load = 20 × 12 kW = 240 kW
Diversity factor = 35/240 = 14.6% (only 14.6% of total load)
```

**Example 3 - Range Over 12 kW (14 kW Range)**:
```
Given: One 14 kW electric range
Base demand (Column A, 1 appliance) = 8 kW
Increase: 5% per kW over 12 kW
  14 kW - 12 kW = 2 kW over
  Increase = 8 kW × 5% × 2 = 0.8 kW
Demand load = 8 + 0.8 = 8.8 kW = 8,800 VA
```

**Example 4 - Small Cooking Appliance (6 kW Cooktop)**:
```
Given: One 6 kW counter-mounted cooktop
Use Column C (appliance ≤ 8.75 kW)
  Column C, 1 appliance = 80%
Demand load = 6 kW × 80% = 4.8 kW = 4,800 VA
```

**Example 5 - Wall Oven + Cooktop Combination**:
```
Given: 5 kW wall oven + 6 kW cooktop = 11 kW total
Total nameplate = 11 kW (between 8.75 kW and 12 kW)
Use Column A (11 kW rounds to ≤12 kW category)
  Column A, 1 appliance = 8 kW demand
Demand load = 8 kW = 8,000 VA
```

### 220.56 Kitchen Equipment - Other Than Dwelling Unit(s)

**Commercial Kitchen Equipment**:
- Include at **nameplate rating** of each appliance
- May apply demand factors per Table 220.56 for three or more units

#### Table 220.56 - Demand Factors for Kitchen Equipment - Other Than Dwelling Unit(s)

```
┌──────────────────────────────────┬─────────────────┐
│ Number of Units of Equipment     │ Demand Factor   │
├──────────────────────────────────┼─────────────────┤
│ 1                                │ 100%            │
│ 2                                │ 100%            │
│ 3                                │ 90%             │
│ 4                                │ 80%             │
│ 5                                │ 70%             │
│ 6 and over                       │ 65%             │
└──────────────────────────────────┴─────────────────┘
```

**Example - Restaurant Kitchen**:
```
Given: 6 commercial kitchen appliances
  - 10 kW fryer
  - 8 kW griddle
  - 5 kW convection oven
  - 3 kW steamer
  - 2 kW warmer
  - 1.5 kW toaster
Total connected load = 29.5 kW
Table 220.56, 6 appliances, demand factor = 65%
Demand load = 29.5 kW × 65% = 19.175 kW = 19,175 VA
```

### 220.57 Electric Vehicle Supply Equipment (EVSE)

**Load Calculation for EVSE**:

#### (A) Single EVSE

- Count at **maximum continuous output rating**

#### (B) Multiple EVSE Loads

**Table 220.57** - Demand Factors for Multiple EVSE Loads

```
┌──────────────────────────────────┬─────────────────┐
│ Number of EVSE Ports             │ Demand Factor   │
├──────────────────────────────────┼─────────────────┤
│ 1                                │ 100%            │
│ 2                                │ 100%            │
│ 3                                │ 90%             │
│ 4                                │ 80%             │
│ 5                                │ 70%             │
│ 6                                │ 60%             │
│ 7                                │ 50%             │
│ 8                                │ 50%             │
│ 9                                │ 50%             │
│ 10 and over                      │ 50%             │
└──────────────────────────────────┴─────────────────┘
```

**Example - Apartment Building with 10 EVSE Units**:
```
Given: 10 EVSE units, each rated 7.68 kW (32A × 240V)
Total connected load = 10 × 7.68 kW = 76.8 kW
Table 220.57, 10 units, demand factor = 50%
Demand load = 76.8 kW × 50% = 38.4 kW = 38,400 VA
```

### 220.60 Noncoincident Loads

**Heating vs. Air Conditioning**:
- Where it is unlikely that both heating and air conditioning will operate simultaneously
- Include **only the larger load** in the total load calculation
- Do not sum heating + cooling

**Example**:
```
Given:
  - Electric heat: 30 kW
  - Air conditioning: 25 kW
Calculation:
  Include only heating load = 30 kW (larger)
  Do not add cooling load
```

### 220.61 Feeder or Service Neutral Load

**Neutral Load Calculation**:

The neutral conductor carries unbalanced load between phases. For certain loads, the neutral load is less than the ungrounded conductor load.

**Loads to Include on Neutral at 100%**:
- Lighting and receptacle loads
- 120V appliances
- Line-to-neutral connected loads

**Loads to Include on Neutral at 70%**:
- Electric ranges, wall ovens, counter-mounted cooking units (220.55)
- Electric dryers (220.54)

**Loads NOT Included on Neutral**:
- 240V loads with no neutral connection (baseboard heaters, A/C compressors, etc.)
- Line-to-line connected 3-phase loads

**Demand Factor for Neutral**:
- Apply Table 220.42 demand factors to neutral load (same as ungrounded conductors)

**Example - Neutral Load Calculation**:
```
Given:
  - General lighting/receptacles: 10,000 VA
  - Electric range (demand per 220.55): 8,000 VA
  - Electric dryer: 5,000 VA
  - 240V baseboard heaters: 15,000 VA (no neutral)

Calculation:
  Lighting/receptacles: 10,000 VA × 100% = 10,000 VA
  Range: 8,000 VA × 70% = 5,600 VA
  Dryer: 5,000 VA × 70% = 3,500 VA
  Heaters: 0 VA (line-to-line, no neutral)

  Total neutral load = 10,000 + 5,600 + 3,500 = 19,100 VA
```

---

## Part IV - Optional Feeder and Service Load Calculations (220.80-220.87)

### 220.82 Dwelling Unit - Optional Calculation

**Purpose**: Simplified calculation method for dwelling units, recognizing greater diversity in actual usage.

**Applicability**:
- Single-family dwellings
- Individual apartment units
- Must have electric cooking equipment (range, oven, cooktop)

**Procedure**:

#### Step 1: Calculate General Loads

**Include at 100%**:
1. Air conditioning (nameplate rating)
   - OR -
2. Electric heating (nameplate rating)
   - Include only larger of heating or cooling, not both

#### Step 2: Calculate Other Loads

**Sum the following connected loads**:
- General lighting and receptacles: Square feet × 3 VA/ft²
- Small appliance circuits: 1,500 VA each (minimum 2)
- Laundry circuit: 1,500 VA
- All appliances (fastened in place, permanently connected, or located to be on specific circuit): ranges, wall ovens, counter cooktops, clothes dryers, water heaters, dishwashers, etc.

#### Step 3: Apply Demand Factor

**Table 220.82 - Optional Calculation Demand Factors for Dwelling Units**

```
┌──────────────────────────────────────────┬─────────────────┐
│ Total Connected Load                     │ Demand Factor   │
├──────────────────────────────────────────┼─────────────────┤
│ First 10 kVA or less at                  │ 100%            │
│ Remainder over 10 kVA at                 │ 40%             │
└──────────────────────────────────────────┴─────────────────┘
```

#### Step 4: Total Service Calculation

```
Total Service Load = (A/C or Heat at 100%) + (Other Loads with 220.82 demand factor)
```

**Example 1 - Standard Dwelling Unit (220.82 Optional Method)**:

```
Given:
  - 2,400 sq ft dwelling
  - 2 small appliance circuits
  - 1 laundry circuit
  - 12 kW electric range
  - 5 kW electric dryer
  - 4.5 kW water heater
  - 1.2 kW dishwasher
  - 0.8 kW garbage disposal
  - 12 kW electric heat
  - 3-ton A/C (36A × 240V = 8,640 VA)
  - Service voltage: 240V

Step 1: Heating vs. Cooling (select larger)
  Electric heat: 12,000 VA
  A/C: 8,640 VA
  Select heating: 12,000 VA × 100% = 12,000 VA

Step 2: Calculate Other Loads
  General lighting: 2,400 ft² × 3 VA/ft² = 7,200 VA
  Small appliance: 2 × 1,500 VA = 3,000 VA
  Laundry: 1 × 1,500 VA = 1,500 VA
  Range: 12,000 VA (nameplate)
  Dryer: 5,000 VA (nameplate)
  Water heater: 4,500 VA
  Dishwasher: 1,200 VA
  Disposal: 800 VA
  Total other loads = 35,200 VA

Step 3: Apply Table 220.82 Demand Factor
  First 10 kVA × 100% = 10,000 VA
  Remaining 25.2 kVA × 40% = 10,080 VA
  Demand other loads = 10,000 + 10,080 = 20,080 VA

Step 4: Total Service Load
  Total = Heating + Other Loads Demand
  Total = 12,000 + 20,080 = 32,080 VA

Step 5: Convert to Amperes
  I = 32,080 VA / 240V = 133.67 A

Step 6: Service Size
  Minimum service = 150A (next standard size per 240.6)
```

**Example 2 - Larger Dwelling (220.82 Optional Method)**:

```
Given:
  - 3,800 sq ft dwelling
  - 2 small appliance circuits
  - 1 laundry circuit
  - 14 kW electric range
  - 5.5 kW electric dryer
  - 5 kW water heater
  - 1.5 kW dishwasher
  - 0.9 kW garbage disposal
  - 10 kW heat pump (heating mode)
  - 10 kW heat pump backup heat strips
  - Service voltage: 240V

Step 1: Heating Load
  Heat pump + backup: (10 + 10) kW = 20,000 VA × 100% = 20,000 VA

Step 2: Calculate Other Loads
  General lighting: 3,800 ft² × 3 VA/ft² = 11,400 VA
  Small appliance: 2 × 1,500 VA = 3,000 VA
  Laundry: 1 × 1,500 VA = 1,500 VA
  Range: 14,000 VA
  Dryer: 5,500 VA
  Water heater: 5,000 VA
  Dishwasher: 1,500 VA
  Disposal: 900 VA
  Total other loads = 43,800 VA

Step 3: Apply Table 220.82 Demand Factor
  First 10 kVA × 100% = 10,000 VA
  Remaining 33.8 kVA × 40% = 13,520 VA
  Demand other loads = 10,000 + 13,520 = 23,520 VA

Step 4: Total Service Load
  Total = 20,000 + 23,520 = 43,520 VA

Step 5: Convert to Amperes
  I = 43,520 VA / 240V = 181.33 A

Step 6: Service Size
  Minimum service = 200A
```

### 220.83 Existing Dwelling Unit

**Purpose**: Calculate additional load for service upgrade or additions to existing dwelling.

**Method**:
1. Calculate existing load using actual maximum demand data (optional)
2. Calculate additional load at 100%
3. Sum existing + additional

**Alternative**: Use 220.82 for total load (existing + new)

### 220.84 Multifamily Dwelling - Optional Calculation

**Purpose**: Calculate service or feeder for multifamily buildings (3+ units).

**Method**:

#### Step 1: Calculate Load for Each Unit

Use 220.82 for each dwelling unit (without diversity yet).

#### Step 2: Apply Dwelling Unit Demand Factors

**Table 220.84 - Optional Calculation Demand Factors for Multifamily Dwellings**

```
┌──────────────────────────────────┬─────────────────┐
│ Number of Dwelling Units         │ Demand Factor   │
├──────────────────────────────────┼─────────────────┤
│ 3-5                              │ 45%             │
│ 6-7                              │ 44%             │
│ 8-10                             │ 43%             │
│ 11                               │ 42%             │
│ 12-13                            │ 41%             │
│ 14-15                            │ 40%             │
│ 16-17                            │ 39%             │
│ 18-20                            │ 38%             │
│ 21                               │ 37%             │
│ 22-23                            │ 36%             │
│ 24-25                            │ 35%             │
│ 26-27                            │ 34%             │
│ 28-30                            │ 33%             │
│ 31                               │ 32%             │
│ 32-33                            │ 31%             │
│ 34-36                            │ 30%             │
│ 37-38                            │ 29%             │
│ 39-42                            │ 28%             │
│ 43-45                            │ 27%             │
│ 46-50                            │ 26%             │
│ 51-55                            │ 25%             │
│ 56-61                            │ 24%             │
│ 62 and over                      │ 23%             │
└──────────────────────────────────┴─────────────────┘
```

#### Step 3: Add House Loads

Include at 100%:
- Common area lighting
- Elevators
- Hallway lighting
- Laundry facilities
- Pool equipment
- Common HVAC

**Example - 12-Unit Apartment Building**:

```
Given:
  - 12 identical units, each with calculated load of 32 kW (per 220.82)
  - House loads: 10 kW lighting, 15 kW elevator

Step 1: Total Dwelling Load
  12 units × 32 kW = 384 kW

Step 2: Apply Table 220.84 Demand Factor
  12 units, demand factor = 41%
  Dwelling demand = 384 kW × 41% = 157.44 kW

Step 3: Add House Loads
  House loads = 10 + 15 = 25 kW (at 100%)

Step 4: Total Building Service Load
  Total = 157.44 + 25 = 182.44 kW = 182,440 VA

Step 5: Convert to Amperes (208V/3-phase service)
  I = 182,440 VA / (√3 × 208V) = 182,440 / 360.26 = 506.5 A

Step 6: Service Size
  Minimum service = 600A (3-phase)
```

### 220.85 Two Dwelling Units Supplied by a Single Feeder

**Method**:
- Use 220.82 for each unit individually
- Sum both units at 100% (no additional diversity)

### 220.86 Schools

**Optional calculation for schools**:
- General lighting and receptacles per Table 220.12 (3 VA/ft²)
- HVAC equipment at actual nameplate
- Other loads at nameplate
- Apply demand factor per 220.86

#### Table 220.86 - Optional Calculation Demand Factors for Feeders and Services for Schools

```
┌──────────────────────────────────┬─────────────────┐
│ Connected Load (VA)              │ Demand Factor   │
├──────────────────────────────────┼─────────────────┤
│ All connected load               │ 100%            │
│ (Note: Limited diversity in      │                 │
│  schools due to simultaneous     │                 │
│  operation)                      │                 │
└──────────────────────────────────┴─────────────────┘
```

**Note**: 220.86 provides limited relief; schools typically use standard method (220.40).

### 220.87 Determining Existing Loads

**Purpose**: Calculate existing load for additions, alterations, or service upgrades.

**Method**:

#### Option 1 - Actual Maximum Demand Data

Use actual measurement:
- Measure maximum demand using recording ammeter
- Minimum 30-day recording period
- Use maximum average kW (or kVA) over 15-minute interval

#### Option 2 - Calculation

Use 220.82 or 220.40 to calculate existing load.

**Example - Adding EV Charger to Existing Dwelling**:

```
Given:
  - Existing 2,200 sq ft dwelling with 200A service
  - Actual maximum demand measured: 120A average peak
  - Adding: 7.68 kW (32A) EVSE

Step 1: Determine Existing Load
  Use actual measurement: 120A × 240V = 28,800 VA

Step 2: Calculate EVSE Addition
  EVSE: 7,680 VA × 100% = 7,680 VA
  (Note: 220.57 diversity not applicable for single unit)

Step 3: Total Load
  Total = 28,800 + 7,680 = 36,480 VA

Step 4: Convert to Amperes
  I = 36,480 VA / 240V = 152 A

Step 5: Conclusion
  Existing 200A service is adequate (152A < 200A)
```

---

## Worked Examples

### Example 1: Single-Family Dwelling (Standard Method 220.40)

**Given**:
- 2,600 sq ft dwelling
- 2 small appliance circuits
- 1 laundry circuit
- 12 kW electric range
- 5 kW electric dryer
- 4.5 kW water heater (continuous)
- 1.2 kW dishwasher
- 0.8 kW garbage disposal
- 15 kW electric heat (baseboard)
- 240V service

**Solution**:

**Step 1: General Lighting Load**
```
Lighting load = 2,600 ft² × 3 VA/ft² = 7,800 VA
Small appliance = 2 × 1,500 VA = 3,000 VA
Laundry = 1 × 1,500 VA = 1,500 VA
Total lighting = 7,800 + 3,000 + 1,500 = 12,300 VA
```

**Step 2: Apply Table 220.42 Demand Factor**
```
First 3,000 VA × 100% = 3,000 VA
Remaining 9,300 VA × 35% = 3,255 VA
Demand lighting load = 3,000 + 3,255 = 6,255 VA
```

**Step 3: Electric Range (Table 220.55)**
```
One 12 kW range, Column A = 8,000 VA
```

**Step 4: Electric Dryer**
```
Dryer load = 5,000 VA (at 100%, no demand factor for single unit)
```

**Step 5: Other Appliances**
```
Water heater = 4,500 VA
Dishwasher = 1,200 VA
Disposal = 800 VA
Total other appliances = 6,500 VA (at 100%)
```

**Step 6: Heating Load**
```
Electric heat = 15,000 VA (at 100%, no demand factor per 220.51)
```

**Step 7: Total Service Load**
```
Lighting demand: 6,255 VA
Range demand: 8,000 VA
Dryer: 5,000 VA
Other appliances: 6,500 VA
Heating: 15,000 VA
Total = 40,755 VA
```

**Step 8: Convert to Amperes**
```
I = 40,755 VA / 240V = 169.8 A
```

**Step 9: Service Size**
```
Minimum service = 200A (next standard size per 240.6)
```

---

### Example 2: Single-Family Dwelling (Optional Method 220.82)

**Given**: Same as Example 1

**Solution**:

**Step 1: Heating Load (at 100%)**
```
Electric heat = 15,000 VA × 100% = 15,000 VA
```

**Step 2: Sum All Other Loads**
```
General lighting: 2,600 ft² × 3 VA/ft² = 7,800 VA
Small appliance: 2 × 1,500 VA = 3,000 VA
Laundry: 1 × 1,500 VA = 1,500 VA
Range: 12,000 VA (nameplate)
Dryer: 5,000 VA
Water heater: 4,500 VA
Dishwasher: 1,200 VA
Disposal: 800 VA
Total other loads = 35,300 VA
```

**Step 3: Apply Table 220.82 Demand Factor**
```
First 10 kVA × 100% = 10,000 VA
Remaining 25.3 kVA × 40% = 10,120 VA
Demand other loads = 20,120 VA
```

**Step 4: Total Service Load**
```
Total = 15,000 + 20,120 = 35,120 VA
```

**Step 5: Convert to Amperes**
```
I = 35,120 VA / 240V = 146.3 A
```

**Step 6: Service Size**
```
Minimum service = 150A or 200A
```

**Note**: Optional method (220.82) yields **146.3A** vs. standard method (220.40) yields **169.8A**. Both methods are code-compliant; optional method recognizes greater diversity.

---

### Example 3: Commercial Building (Office)

**Given**:
- 8,000 sq ft office building
- Fluorescent lighting throughout
- 120 receptacles (general use)
- 3-ton packaged A/C unit (36A × 240V × 1.732 = 14,929 VA)
- Electric water heater: 6 kW
- 208V/3-phase service

**Solution**:

**Step 1: General Lighting Load (Table 220.12)**
```
Lighting = 8,000 ft² × 1 VA/ft² = 8,000 VA
(Office = 1 VA/ft² per Table 220.12)
No demand factor (all others category in Table 220.42)
Lighting load = 8,000 VA
```

**Step 2: Receptacle Load (Table 220.44)**
```
Receptacles = 120 × 180 VA = 21,600 VA = 21.6 kVA
First 10 kVA × 100% = 10,000 VA
Remaining 11.6 kVA × 50% = 5,800 VA
Demand receptacle load = 15,800 VA
```

**Step 3: Air Conditioning (Article 440)**
```
A/C load = 14,929 VA (at 100%, includes 125% largest motor already)
```

**Step 4: Water Heater**
```
Water heater = 6,000 VA (at 100%)
```

**Step 5: Total Service Load**
```
Lighting: 8,000 VA
Receptacles: 15,800 VA
A/C: 14,929 VA
Water heater: 6,000 VA
Total = 44,729 VA
```

**Step 6: Convert to Amperes (3-phase)**
```
I = 44,729 VA / (√3 × 208V) = 44,729 / 360.26 = 124.15 A per phase
```

**Step 7: Service Size**
```
Minimum service = 150A (3-phase, 208V)
```

---

### Example 4: Multifamily Building (8 units)

**Given**:
- 8-unit apartment building
- Each unit: 1,200 sq ft, 2 small appliance circuits, 1 laundry, 10 kW range, 5 kW dryer, 3 kW water heater
- Each unit has heat pump (8 kW heating, 6 kW cooling)
- House loads: 5 kW hallway lighting, 10 kW elevator
- 208V/3-phase service

**Solution**:

**Step 1: Calculate Load Per Unit (using 220.82)**

For each unit:
```
Heating load: 8,000 VA × 100% = 8,000 VA

Other loads:
  General lighting: 1,200 ft² × 3 VA/ft² = 3,600 VA
  Small appliance: 2 × 1,500 VA = 3,000 VA
  Laundry: 1,500 VA
  Range: 10,000 VA
  Dryer: 5,000 VA
  Water heater: 3,000 VA
  Total other = 26,100 VA

Apply Table 220.82:
  First 10 kVA × 100% = 10,000 VA
  Remaining 16.1 kVA × 40% = 6,440 VA
  Demand other = 16,440 VA

Total per unit = 8,000 + 16,440 = 24,440 VA
```

**Step 2: Total Dwelling Load**
```
8 units × 24,440 VA = 195,520 VA
```

**Step 3: Apply Table 220.84 Demand Factor**
```
8 units, demand factor = 43%
Dwelling demand = 195,520 × 43% = 84,074 VA
```

**Step 4: Add House Loads**
```
Hallway lighting = 5,000 VA
Elevator = 10,000 VA
House loads = 15,000 VA (at 100%)
```

**Step 5: Total Building Service Load**
```
Total = 84,074 + 15,000 = 99,074 VA
```

**Step 6: Convert to Amperes (3-phase)**
```
I = 99,074 VA / (√3 × 208V) = 99,074 / 360.26 = 275.0 A per phase
```

**Step 7: Service Size**
```
Minimum service = 300A or 400A (3-phase, 208V)
```

---

### Example 5: Restaurant

**Given**:
- 4,000 sq ft restaurant
- General lighting per Table 220.12
- 50 receptacles
- Kitchen equipment: 10 kW fryer, 8 kW griddle, 5 kW oven, 3 kW steamer, 2 kW warmer (5 units)
- 10-ton packaged rooftop unit (RTU): 50A × 480V × 1.732 = 41,569 VA
- 480V/3-phase service

**Solution**:

**Step 1: General Lighting (Table 220.12)**
```
Restaurant = 2 VA/ft² per Table 220.12
Lighting = 4,000 ft² × 2 VA/ft² = 8,000 VA
No demand factor (all others category)
Lighting load = 8,000 VA
```

**Step 2: Receptacle Load (Table 220.44)**
```
Receptacles = 50 × 180 VA = 9,000 VA = 9 kVA
First 9 kVA × 100% = 9,000 VA (below 10 kVA threshold)
Receptacle load = 9,000 VA
```

**Step 3: Kitchen Equipment (Table 220.56)**
```
Connected kitchen load:
  10 kW + 8 kW + 5 kW + 3 kW + 2 kW = 28 kW = 28,000 VA

5 units, demand factor = 70% (per Table 220.56)
Kitchen demand = 28,000 × 70% = 19,600 VA
```

**Step 4: HVAC (RTU)**
```
RTU load = 41,569 VA (at 100%)
```

**Step 5: Total Service Load**
```
Lighting: 8,000 VA
Receptacles: 9,000 VA
Kitchen: 19,600 VA
HVAC: 41,569 VA
Total = 78,169 VA
```

**Step 6: Convert to Amperes (3-phase)**
```
I = 78,169 VA / (√3 × 480V) = 78,169 / 831.38 = 94.0 A per phase
```

**Step 7: Service Size**
```
Minimum service = 100A or 125A (3-phase, 480V)
```

---

### Example 6: School Building

**Given**:
- 25,000 sq ft elementary school
- General lighting per Table 220.12 (schools = 3 VA/ft²)
- Receptacles: 200 outlets
- HVAC: 50-ton chiller + air handlers = 150 kW total
- Kitchen: 40 kW connected load
- 480V/3-phase service

**Solution**:

**Step 1: General Lighting (Table 220.12)**
```
School = 3 VA/ft²
Lighting = 25,000 ft² × 3 VA/ft² = 75,000 VA
No demand factor (schools = all others in Table 220.42)
Lighting load = 75,000 VA
```

**Step 2: Receptacles (Table 220.44)**
```
Receptacles = 200 × 180 VA = 36,000 VA = 36 kVA
First 10 kVA × 100% = 10,000 VA
Remaining 26 kVA × 50% = 13,000 VA
Receptacle demand = 23,000 VA
```

**Step 3: HVAC**
```
HVAC = 150,000 VA (at 100%)
```

**Step 4: Kitchen (Table 220.56)**
```
Assume 6+ kitchen units, demand factor = 65%
Kitchen demand = 40,000 × 65% = 26,000 VA
```

**Step 5: Total Service Load**
```
Lighting: 75,000 VA
Receptacles: 23,000 VA
HVAC: 150,000 VA
Kitchen: 26,000 VA
Total = 274,000 VA
```

**Step 6: Convert to Amperes (3-phase)**
```
I = 274,000 VA / (√3 × 480V) = 274,000 / 831.38 = 329.5 A per phase
```

**Step 7: Service Size**
```
Minimum service = 350A or 400A (3-phase, 480V)
```

---

## Integration with QA/QC Rules

The QA/QC validation system in the `engineering-drawing-qaqc` skill uses the following rule IDs for electrical load calculation validation. These rules ensure that electrical panel schedules and load calculations on engineering drawings comply with NEC Article 220 requirements.

### QA Rules for Load Calculations (QA-201-ELEC through QA-213-ELEC)

#### QA-201-ELEC: Panel Schedule Load Calculation Included

**Rule Definition**:
```yaml
- id: QA-201-ELEC
  description: Verify electrical panel schedules include load calculations per NEC 220
  severity: critical
  category: compliance
  check:
    type: field_presence
    field: schedules.panel_schedule.load_calculation_included
    condition: equals true
```

**Rationale**: NEC 220 requires load calculations for sizing services, feeders, and branch circuits. Panel schedules must document calculated load vs. available capacity.

**NEC Reference**: 220.40, 220.82

---

#### QA-202-ELEC: General Lighting Load Matches Table 220.12

**Rule Definition**:
```yaml
- id: QA-202-ELEC
  description: Verify general lighting load uses correct VA/ft² from Table 220.12
  severity: high
  category: compliance
  check:
    type: custom
    function: validate_lighting_load_density
    params:
      table_reference: "NEC Table 220.12"
```

**Validation Logic**:
```python
def validate_lighting_load_density(panel_schedule, title_block):
    occupancy_type = title_block.get("occupancy_type")
    square_feet = panel_schedule.get("square_feet")
    lighting_load_va = panel_schedule.get("lighting_load_va")

    # Table 220.12 lookup
    table_220_12 = {
        "dwelling": 3,
        "office": 1,
        "school": 3,
        "restaurant": 2,
        "warehouse": 0.25,
        "hospital": 2,
        # ... complete table
    }

    expected_density = table_220_12.get(occupancy_type.lower())
    expected_load = square_feet * expected_density

    tolerance = 0.05  # 5% tolerance for rounding
    if abs(lighting_load_va - expected_load) / expected_load > tolerance:
        return {
            "status": "FAIL",
            "message": f"Lighting load {lighting_load_va} VA does not match expected "
                      f"{expected_load} VA ({square_feet} ft² × {expected_density} VA/ft²)"
        }
    return {"status": "PASS"}
```

**NEC Reference**: 220.12, Table 220.12

---

#### QA-203-ELEC: Demand Factors Applied Correctly

**Rule Definition**:
```yaml
- id: QA-203-ELEC
  description: Verify demand factors applied per Table 220.42 (lighting) or 220.55 (ranges)
  severity: high
  category: compliance
  check:
    type: custom
    function: validate_demand_factors
    params:
      tables: ["220.42", "220.55", "220.84"]
```

**Validation Logic**:
```python
def validate_demand_factors(panel_schedule):
    # Check dwelling unit lighting demand (Table 220.42)
    if panel_schedule.get("occupancy_type") == "dwelling":
        total_lighting = panel_schedule.get("total_lighting_va")
        demand_lighting = panel_schedule.get("demand_lighting_va")

        # Calculate expected demand per Table 220.42
        if total_lighting <= 3000:
            expected_demand = total_lighting
        elif total_lighting <= 120000:
            expected_demand = 3000 + (total_lighting - 3000) * 0.35
        else:
            expected_demand = 3000 + (117000 * 0.35) + (total_lighting - 120000) * 0.25

        if abs(demand_lighting - expected_demand) > 10:  # 10 VA tolerance
            return {
                "status": "FAIL",
                "message": f"Lighting demand factor incorrect. Expected {expected_demand} VA, "
                          f"got {demand_lighting} VA per Table 220.42"
            }

    # Check electric range demand (Table 220.55)
    if "range_count" in panel_schedule:
        range_count = panel_schedule.get("range_count")
        range_rating_kw = panel_schedule.get("range_rating_kw")
        range_demand_kw = panel_schedule.get("range_demand_kw")

        # Table 220.55 Column A lookup
        table_220_55 = {
            1: 8, 2: 11, 3: 14, 4: 17, 5: 20,
            # ... complete table
        }

        expected_demand_kw = table_220_55.get(range_count)

        # Adjust for ranges > 12 kW (Note 1)
        if range_rating_kw > 12:
            increase_kw = (range_rating_kw - 12) * 0.05 * expected_demand_kw
            expected_demand_kw += increase_kw

        if abs(range_demand_kw - expected_demand_kw) > 0.5:
            return {
                "status": "FAIL",
                "message": f"Range demand factor incorrect. Expected {expected_demand_kw} kW "
                          f"for {range_count} ranges per Table 220.55 Column A"
            }

    return {"status": "PASS"}
```

**NEC Reference**: 220.42, 220.55, Table 220.42, Table 220.55

---

#### QA-204-ELEC: Panel Ampacity Calculation Correct

**Rule Definition**:
```yaml
- id: QA-204-ELEC
  description: Verify panel ampacity calculated correctly (Total VA / Voltage)
  severity: critical
  category: compliance
  check:
    type: custom
    function: validate_panel_ampacity
```

**Validation Logic**:
```python
def validate_panel_ampacity(panel_schedule):
    total_va = panel_schedule.get("total_calculated_load_va")
    voltage = panel_schedule.get("voltage")
    phases = panel_schedule.get("phases")
    calculated_ampacity = panel_schedule.get("calculated_ampacity_a")

    # Calculate expected ampacity
    if phases == 1:
        expected_ampacity = total_va / voltage
    elif phases == 3:
        expected_ampacity = total_va / (1.732 * voltage)

    tolerance = 0.02  # 2% tolerance
    if abs(calculated_ampacity - expected_ampacity) / expected_ampacity > tolerance:
        return {
            "status": "FAIL",
            "message": f"Panel ampacity {calculated_ampacity}A does not match expected "
                      f"{expected_ampacity:.1f}A ({total_va} VA / {voltage}V)"
        }

    return {"status": "PASS"}
```

**NEC Reference**: 220.40, 220.5(B)

---

#### QA-205-ELEC: Service/Panel Size Meets or Exceeds Calculated Load

**Rule Definition**:
```yaml
- id: QA-205-ELEC
  description: Verify service or panel rating >= calculated ampacity per 240.6 standard sizes
  severity: critical
  category: compliance
  check:
    type: custom
    function: validate_service_size
```

**Validation Logic**:
```python
def validate_service_size(panel_schedule):
    calculated_ampacity = panel_schedule.get("calculated_ampacity_a")
    panel_rating = panel_schedule.get("panel_rating_a")

    # NEC 240.6(A) standard sizes
    standard_sizes = [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110,
                     125, 150, 175, 200, 225, 250, 300, 350, 400, 450, 500, 600,
                     700, 800, 1000, 1200, 1600, 2000, 2500, 3000, 4000, 5000, 6000]

    if panel_rating < calculated_ampacity:
        return {
            "status": "FAIL",
            "message": f"Panel rating {panel_rating}A is less than calculated load "
                      f"{calculated_ampacity:.1f}A"
        }

    if panel_rating not in standard_sizes:
        return {
            "status": "FAIL",
            "message": f"Panel rating {panel_rating}A is not a standard NEC 240.6(A) size"
        }

    return {"status": "PASS"}
```

**NEC Reference**: 230.42, 215.2, 240.6

---

#### QA-206-ELEC through QA-213-ELEC: Additional Load Calculation Validations

Additional validation rules cover:

- **QA-206-ELEC**: Neutral load calculation for services (220.61)
- **QA-207-ELEC**: Motors include 125% on largest motor (220.14(H), 220.50)
- **QA-208-ELEC**: HVAC vs. heating load (only larger counted per 220.60)
- **QA-209-ELEC**: Small appliance circuits for dwellings (minimum 2 × 1,500 VA)
- **QA-210-ELEC**: Laundry circuit for dwellings (1 × 1,500 VA per 220.52)
- **QA-211-ELEC**: Electric vehicle charging demand factors (220.57)
- **QA-212-ELEC**: Multifamily demand factors applied (220.84)
- **QA-213-ELEC**: Optional calculation method used correctly (220.82)

---

### Integration Example: Validating Electrical Panel Schedule JSON

**Input JSON** (extracted from electrical drawing):
```json
{
  "sheet": "E-301",
  "title_block": {
    "project": "Main Office Building",
    "occupancy_type": "office",
    "discipline": "Electrical"
  },
  "schedules": {
    "panel_schedule": {
      "panel_id": "LP-1",
      "voltage": 208,
      "phases": 3,
      "panel_rating_a": 225,
      "square_feet": 5000,
      "lighting_load_va": 5000,
      "demand_lighting_va": 5000,
      "receptacle_count": 60,
      "receptacle_load_va": 10800,
      "demand_receptacle_va": 9400,
      "hvac_load_va": 15000,
      "total_calculated_load_va": 29400,
      "calculated_ampacity_a": 81.6,
      "load_calculation_included": true
    }
  }
}
```

**QA Validation Results**:

| Rule ID | Status | Details |
|---------|--------|---------|
| QA-201-ELEC | ✓ PASS | Load calculation included |
| QA-202-ELEC | ✓ PASS | Lighting load: 5,000 ft² × 1 VA/ft² = 5,000 VA (Table 220.12) |
| QA-203-ELEC | ✓ PASS | Receptacle demand: First 10 kVA @ 100% + 0.8 kVA @ 50% = 9,400 VA (Table 220.44) |
| QA-204-ELEC | ✓ PASS | Ampacity: 29,400 VA / (1.732 × 208V) = 81.6A ✓ |
| QA-205-ELEC | ✓ PASS | Panel rating 225A > calculated 81.6A, standard size ✓ |

---

## Quick Reference Tables

### Table 220.12 Summary (Top 10 Occupancies)

| Occupancy | VA/ft² |
|-----------|--------|
| Dwelling units | 3 |
| Schools | 3 |
| Stores | 3 |
| Banks | 3.5 |
| Barber/beauty shops | 3 |
| Hospitals | 2 |
| Hotels/motels | 2 |
| Restaurants | 2 |
| Office buildings | 1 |
| Warehouses | 0.25 |

### Table 220.42 Summary (Dwelling Lighting Demand)

| Load Range (VA) | Demand Factor |
|-----------------|---------------|
| First 3,000 | 100% |
| 3,001 - 120,000 | 35% |
| Over 120,000 | 25% |

### Table 220.55 Summary (Electric Ranges)

| Number of Ranges | Demand (kW) Column A |
|------------------|----------------------|
| 1 | 8 |
| 2 | 11 |
| 3 | 14 |
| 5 | 20 |
| 10 | 25 |
| 20 | 35 |
| 30 | 40 |

### Table 220.84 Summary (Multifamily Demand)

| Dwelling Units | Demand Factor |
|----------------|---------------|
| 3-5 | 45% |
| 6-10 | 43-44% |
| 11-20 | 38-42% |
| 21-40 | 28-37% |
| 61+ | 23% |

---

## Conclusion

NEC Article 220 provides comprehensive methods for calculating electrical loads to properly size branch circuits, feeders, and services. Key takeaways:

1. **Standard Method (220.40)**: Conservative approach using demand factors
2. **Optional Method (220.82)**: Simplified for dwellings with greater diversity recognition
3. **Demand Factors**: Critical for preventing oversizing (Tables 220.42, 220.55, 220.84)
4. **Occupancy-Specific**: Different unit loads by occupancy type (Table 220.12)
5. **QA/QC Integration**: Load calculations must be validated on panel schedules per rules QA-201 through QA-213

Always verify with the Authority Having Jurisdiction (AHJ) for local amendments and adopted NEC edition.

---

**Document Version**: 1.0
**Last Updated**: 2025-01-22
**Next Review**: NEC 2026 edition adoption
**Maintained By**: EE_AI Platform - MEP Library Curation Team
