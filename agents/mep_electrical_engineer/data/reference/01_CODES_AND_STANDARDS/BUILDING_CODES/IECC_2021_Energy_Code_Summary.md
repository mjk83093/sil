# IECC 2021 International Energy Conservation Code Summary

**Document Purpose**: Comprehensive reference for energy code compliance in MEP design and QA validation

**Last Updated**: 2025-10-22

**Sources**:
- International Code Council (ICC) IECC 2021 Edition
- DOE Building Energy Codes Program
- ASHRAE Standard 90.1-2019 (comparative reference)
- PNNL Building America Solution Center

---

## 1. CLIMATE ZONES AND DEFINITIONS

### 1.1 DOE Climate Zone Map (IECC Climate Zones)

The IECC 2021 divides the United States into 8 primary climate zones (1-8) with moisture regime modifiers:

| Zone | Thermal Description | Representative Cities | Moisture Regime |
|------|---------------------|----------------------|-----------------|
| 1A | Very Hot - Humid | Miami FL, Key West FL | A = Humid |
| 2A | Hot - Humid | Houston TX, Orlando FL, Atlanta GA | A = Humid |
| 2B | Hot - Dry | Phoenix AZ, Las Vegas NV | B = Dry |
| 3A | Warm - Humid | Memphis TN, Birmingham AL, Dallas TX | A = Humid |
| 3B | Warm - Dry | El Paso TX, Las Vegas NV | B = Dry |
| 3C | Warm - Marine | San Francisco CA, Portland OR | C = Marine |
| 4A | Mixed - Humid | Baltimore MD, Kansas City MO, NYC NY | A = Humid |
| 4B | Mixed - Dry | Albuquerque NM, Salt Lake City UT | B = Dry |
| 4C | Mixed - Marine | Seattle WA, Portland OR | C = Marine |
| 5A | Cool - Humid | Chicago IL, Boston MA, Detroit MI | A = Humid |
| 5B | Cool - Dry | Boise ID, Denver CO | B = Dry |
| 5C | Cool - Marine | Port Angeles WA | C = Marine |
| 6A | Cold - Humid | Burlington VT, Minneapolis MN | A = Humid |
| 6B | Cold - Dry | Helena MT, Bismarck ND | B = Dry |
| 7 | Very Cold | Duluth MN, Fargo ND | (no modifier) |
| 8 | Subarctic/Arctic | Fairbanks AK, Barrow AK | (no modifier) |

**Moisture Regime Definitions**:
- **Humid (A)**: 20+ inches annual precipitation
- **Dry (B)**: <20 inches annual precipitation
- **Marine (C)**: Cool, moderate climates with ocean influence

**Climate Zone Determination**:
- Determined by county or jurisdiction location
- County maps available from DOE and ICC
- Some jurisdictions may be on zone boundaries (use more stringent requirements)

---

## 2. BUILDING ENVELOPE REQUIREMENTS BY CLIMATE ZONE

### 2.1 Commercial Building Envelope (IECC C402.1)

#### 2.1.1 Opaque Assembly U-Factors and R-Values

**Roofs/Ceilings** (Table C402.1.3):

| Climate Zone | Insulation Entirely Above Deck (U-factor) | Metal Building (U-factor) | Attic/Other (R-value) |
|--------------|-------------------------------------------|---------------------------|----------------------|
| 1 | U-0.063 | U-0.065 | R-38 |
| 2 | U-0.063 | U-0.065 | R-38 |
| 3 | U-0.048 | U-0.055 | R-49 |
| 4 | U-0.035 | U-0.055 | R-49 |
| 5 | U-0.028 | U-0.055 | R-49 |
| 6 | U-0.028 | U-0.055 | R-49 |
| 7-8 | U-0.028 | U-0.055 | R-60 |

**Walls Above Grade** (Table C402.1.3):

| Climate Zone | Mass Walls (U-factor) | Metal Building (U-factor) | Steel-Framed (R-value) | Wood-Framed (R-value) |
|--------------|----------------------|---------------------------|------------------------|----------------------|
| 1 | U-0.580 | U-0.113 | R-13 + R-3.8 ci | R-13 + R-3.8 ci |
| 2 | U-0.151 | U-0.113 | R-13 + R-3.8 ci | R-13 + R-3.8 ci |
| 3 | U-0.123 | U-0.086 | R-13 + R-7.5 ci | R-13 + R-7.5 ci |
| 4 | U-0.104 | U-0.057 | R-13 + R-12.5 ci | R-13 + R-15.6 ci |
| 5 | U-0.090 | U-0.057 | R-13 + R-15.6 ci | R-20 + R-3.8 ci |
| 6 | U-0.080 | U-0.057 | R-13 + R-15.6 ci | R-20 + R-3.8 ci |
| 7-8 | U-0.071 | U-0.057 | R-13 + R-18.8 ci | R-20 + R-3.8 ci |

**Key**: ci = continuous insulation (exterior to framing)

**Floors Over Unconditioned Space** (Table C402.1.3):

| Climate Zone | Mass Floors (U-factor) | Steel-Joist (R-value) | Wood-Framed (R-value) |
|--------------|----------------------|----------------------|----------------------|
| 1 | U-0.322 | R-19 | R-19 |
| 2 | U-0.087 | R-30 | R-30 |
| 3 | U-0.074 | R-38 | R-38 |
| 4-8 | U-0.064 | R-38 | R-38 |

**Slab-on-Grade Floors** (Table C402.1.3):

| Climate Zone | Unheated Slab (R-value/depth) | Heated Slab (R-value/depth) |
|--------------|------------------------------|----------------------------|
| 1-2 | NR | NR |
| 3 | R-10 / 24" | R-15 / Full slab |
| 4 | R-10 / 24" | R-20 / Full slab |
| 5 | R-15 / 24" | R-25 / Full slab |
| 6-8 | R-15 / 48" | R-25 / Full slab |

**Key**: NR = No Requirement

#### 2.1.2 Fenestration Requirements (Windows/Skylights)

**Vertical Fenestration** (Windows) (Table C402.4):

| Climate Zone | Maximum U-Factor | Maximum SHGC | Minimum VT/SHGC |
|--------------|------------------|--------------|-----------------|
| 1 | 1.20 | 0.25 | 1.10 |
| 2 | 0.65 | 0.25 | 1.10 |
| 3 | 0.50 | 0.25 | 1.10 |
| 4 | 0.40 | 0.40 | NR |
| 5 | 0.35 | 0.40 | NR |
| 6 | 0.35 | 0.40 | NR |
| 7-8 | 0.30 | NR | NR |

**Key**:
- SHGC = Solar Heat Gain Coefficient
- VT = Visible Transmittance
- NR = No Requirement

**Skylight Maximum U-Factor** (Table C402.4):

| Climate Zone | Maximum U-Factor | Maximum SHGC |
|--------------|------------------|--------------|
| 1-2 | 0.90 | 0.35 |
| 3 | 0.70 | 0.35 |
| 4-6 | 0.60 | 0.35 |
| 7-8 | 0.55 | NR |

**Fenestration Area Limits**:
- Maximum 40% window-to-wall ratio (WWR) for vertical glazing
- Maximum 5% skylight-to-roof ratio (SRR)
- Above limits require energy performance compliance path

### 2.2 Residential Building Envelope (IECC R402.1)

#### 2.2.1 Prescriptive Insulation Requirements (Table R402.1.2)

**U-Factor Alternative** (Primary Method in IECC 2021):

| Climate Zone | Ceiling U | Wall U | Floor U | Basement Wall U | Slab R/Depth | Crawl Wall U |
|--------------|-----------|--------|---------|-----------------|--------------|-------------|
| 1 | 0.026 | 0.084 | 0.047 | 0.360 | 0 | 0.477 |
| 2 | 0.026 | 0.084 | 0.047 | 0.360 | 0 | 0.477 |
| 3 | 0.021 | 0.060 | 0.033 | 0.091 | 5/2 ft | 0.136 |
| 4 | 0.016 | 0.045 | 0.033 | 0.059 | 10/2 ft | 0.065 |
| 5 | 0.016 | 0.045 | 0.033 | 0.059 | 10/4 ft | 0.065 |
| 6 | 0.016 | 0.045 | 0.026 | 0.050 | 10/4 ft | 0.065 |
| 7 | 0.016 | 0.045 | 0.026 | 0.050 | 15/full | 0.065 |
| 8 | 0.016 | 0.033 | 0.026 | 0.050 | 15/full | 0.065 |

**R-Value Alternative** (Secondary Method in IECC 2021):

| Climate Zone | Ceiling R | Wall R | Floor R | Basement Wall R | Slab R/Depth | Crawl Wall R |
|--------------|-----------|--------|---------|-----------------|--------------|-------------|
| 1 | R-49 | R-13 | R-19 | R-0 | 0 | R-0 |
| 2 | R-49 | R-13 | R-19 | R-0 | 0 | R-0 |
| 3 | R-49 | R-20 or R-13+R-5 | R-30 | R-5/R-13 | R-5 / 2 ft | R-5/R-13 |
| 4 | R-60 | R-20+R-5 or R-13+R-10 | R-30 | R-10/R-13 | R-10 / 2 ft | R-10/R-13 |
| 5 | R-60 | R-20+R-5 or R-13+R-10 | R-38 | R-10/R-13 | R-10 / 4 ft | R-10/R-13 |
| 6 | R-60 | R-20+R-5 or R-13+R-10 | R-38 | R-15/R-19 | R-10 / 4 ft | R-10/R-13 |
| 7 | R-60 | R-20+R-5 or R-13+R-10 | R-38 | R-15/R-19 | R-15 / full | R-10/R-13 |
| 8 | R-60 | R-30+R-5 or R-13+R-15 | R-49 | R-15/R-19 | R-15 / full | R-10/R-13 |

**Fenestration Maximum U-Factor** (Table R402.1.2):

| Climate Zone | Windows U-Factor | Skylights U-Factor |
|--------------|------------------|-------------------|
| 1-2 | 1.20 | 0.75 |
| 3 | 0.40 | 0.65 |
| 4 | 0.30 | 0.55 |
| 5 | 0.30 | 0.55 |
| 6 | 0.27 | 0.55 |
| 7-8 | 0.27 | 0.55 |

---

## 3. MECHANICAL SYSTEM EFFICIENCY REQUIREMENTS

### 3.1 Commercial HVAC Equipment (IECC C403.3)

Equipment efficiency must meet minimum federal standards per:
- **ASHRAE 90.1-2019** Tables 6.8.1-1 through 6.8.1-21
- **NAECA** (National Appliance Energy Conservation Act)
- **DOE** Federal Energy Standards

#### 3.1.1 Air Conditioners and Condensing Units

**Air-Cooled Central Units** (<135,000 Btu/h):

| Equipment Type | Size Category | Minimum Efficiency | Test Standard |
|---------------|---------------|-------------------|---------------|
| Split System | <65,000 Btu/h | 14.0 SEER2 / 11.2 EER2 | AHRI 210/240 |
| Split System | ≥65,000 and <135,000 Btu/h | 13.4 SEER2 / 10.6 EER2 | AHRI 210/240 |
| Single Package | <65,000 Btu/h | 13.4 SEER2 / 10.6 EER2 | AHRI 210/240 |
| Single Package | ≥65,000 and <135,000 Btu/h | 13.4 SEER2 / 10.6 EER2 | AHRI 210/240 |

**Air-Cooled Unitary Air Conditioners** (≥135,000 Btu/h):

| Equipment Type | Size Category | Minimum EER | Test Standard |
|---------------|---------------|-------------|---------------|
| Air-cooled, 3-phase | <65,000 Btu/h | 10.1 EER | AHRI 340/360 |
| Air-cooled, 3-phase | ≥65,000 and <135,000 Btu/h | 9.5 EER | AHRI 340/360 |
| Air-cooled, 3-phase | ≥135,000 and <240,000 Btu/h | 9.7 EER | AHRI 340/360 |
| Air-cooled, 3-phase | ≥240,000 and <760,000 Btu/h | 9.5 EER | AHRI 340/360 |
| Air-cooled, 3-phase | ≥760,000 Btu/h | 9.2 EER | AHRI 340/360 |

**Water-Cooled Unitary Air Conditioners**:

| Size Category | Minimum EER | Test Standard |
|---------------|-------------|---------------|
| <65,000 Btu/h | 12.1 EER | AHRI 340/360 |
| ≥65,000 and <135,000 Btu/h | 11.9 EER | AHRI 340/360 |
| ≥135,000 and <240,000 Btu/h | 12.5 EER | AHRI 340/360 |
| ≥240,000 Btu/h | 12.4 EER | AHRI 340/360 |

#### 3.1.2 Heat Pumps

**Air-Source Heat Pumps** (<135,000 Btu/h cooling):

| Equipment Type | Size Category | Cooling Efficiency | Heating Efficiency | Test Standard |
|---------------|---------------|-------------------|-------------------|---------------|
| Split System | <65,000 Btu/h | 14.3 SEER2 / 11.2 EER2 | 7.5 HSPF2 | AHRI 210/240 |
| Split System | ≥65,000 and <135,000 Btu/h | 13.6 SEER2 / 10.6 EER2 | 6.7 HSPF2 | AHRI 210/240 |
| Single Package | <65,000 Btu/h | 13.4 SEER2 / 10.6 EER2 | 6.7 HSPF2 | AHRI 210/240 |

**Air-Source Heat Pumps** (≥135,000 Btu/h cooling):

| Size Category | Minimum Cooling EER | Minimum Heating COP | Test Standard |
|---------------|---------------------|---------------------|---------------|
| <135,000 Btu/h | 10.1 EER | 3.3 COP (47°F test) | AHRI 340/360 |
| ≥135,000 and <240,000 Btu/h | 9.3 EER | 3.2 COP | AHRI 340/360 |
| ≥240,000 Btu/h | 9.0 EER | 3.2 COP | AHRI 340/360 |

#### 3.1.3 Boilers and Furnaces

**Gas-Fired Boilers**:

| Size Category | Minimum Thermal Efficiency | Minimum Combustion Efficiency | Test Standard |
|---------------|---------------------------|------------------------------|---------------|
| <300,000 Btu/h | 82% AFUE | N/A | DOE 10 CFR 430 |
| ≥300,000 and <2,500,000 Btu/h | 80% Et | 80% Ec | DOE 10 CFR 431 |
| ≥2,500,000 Btu/h | 82% Et | 82% Ec | DOE 10 CFR 431 |

**Gas-Fired Furnaces**:

| Size Category | Minimum AFUE | Test Standard |
|---------------|-------------|---------------|
| <225,000 Btu/h | 80% AFUE | DOE 10 CFR 430 |
| ≥225,000 Btu/h | 80% Et | DOE 10 CFR 431 |

#### 3.1.4 Chillers

**Water-Cooled Chillers** (Electric):

| Type | Size Category | Path A (kW/ton) | Path B (IPLV kW/ton) | Test Standard |
|------|---------------|----------------|---------------------|---------------|
| Centrifugal | All capacities | 0.610 | 0.550 | AHRI 550/590 |
| Positive Displacement | All capacities | 0.780 | 0.630 | AHRI 550/590 |

**Air-Cooled Chillers** (Electric):

| Size Category | Path A (EER) | Path B (IPLV) | Test Standard |
|---------------|-------------|--------------|---------------|
| All capacities | 9.562 EER | 14.050 IPLV | AHRI 550/590 |

### 3.2 Commercial Service Water Heating (IECC C404)

**Gas Storage Water Heaters**:

| Input Rating | Storage Volume | Minimum Et | Minimum SL (Btu/h) | Test Standard |
|-------------|---------------|-----------|-------------------|---------------|
| ≤75,000 Btu/h | ≤55 gal | 0.82 - (0.0019 × V) | N/A | DOE 10 CFR 430 |
| >75,000 Btu/h | ≤100 gal | 80% Et | N/A | DOE 10 CFR 431 |
| >75,000 Btu/h | >100 gal | 80% Et | Maximum 4,400 × (V)^0.5 | DOE 10 CFR 431 |

**Electric Storage Water Heaters**:

| Size Category | Storage Volume | Minimum UEF | Test Standard |
|---------------|---------------|------------|---------------|
| ≤12 kW | ≤55 gal | 0.93 - (0.00132 × V) | DOE 10 CFR 430 |
| >12 kW | All volumes | 0.99 - (0.0012 × V) | DOE 10 CFR 431 |

**Heat Pump Water Heaters**:

| Size Category | Minimum UEF | Test Standard |
|---------------|------------|---------------|
| ≤55 gallons | 3.30 UEF | DOE 10 CFR 430 |
| >55 gallons | 3.30 UEF | DOE 10 CFR 431 |

### 3.3 Ventilation Requirements (IECC C403.7 / ASHRAE 62.1)

**Outdoor Air Requirements**:
- IECC references ASHRAE 62.1-2019 for minimum ventilation rates
- Design ventilation must meet **Table 6.2.2.1** (Minimum Ventilation Rates)
- Exception: Demand control ventilation required for spaces >500 ft² and >40 people/1000 ft²

**Energy Recovery** (IECC C403.7.5):

Required for systems with:
- Design supply air capacity ≥5,000 cfm, AND
- Minimum outdoor air supply ≥70% of design air or >5,000 cfm

| Climate Zone | Required Enthalpy Recovery Ratio |
|--------------|--------------------------------|
| 1-2 | Not required |
| 3-4 | 50% |
| 5-8 | 50% |

---

## 4. LIGHTING POWER DENSITY REQUIREMENTS

### 4.1 Commercial Interior Lighting (IECC C405.4)

#### 4.1.1 Space-by-Space Method (Table C405.4.2(1))

**Maximum Lighting Power Densities (LPD) by Space Type**:

| Space Type | Maximum LPD (W/ft²) |
|-----------|---------------------|
| Auditorium | 0.63 |
| Classroom/Lecture/Training | 0.71 |
| Conference/Meeting/Multipurpose | 0.97 |
| Corridor/Transition | 0.41 |
| Dining Area | 0.65 |
| Electrical/Mechanical | 0.43 |
| Food Preparation | 0.81 |
| Laboratory | 1.11 |
| Lobby | 0.84 |
| Locker Room | 0.52 |
| Office - Enclosed | 0.74 |
| Office - Open | 0.61 |
| Parking Area/Garage | 0.19 |
| Restroom | 0.63 |
| Retail | 1.05 |
| Stairwell | 0.49 |
| Storage | 0.38 |
| Warehouse | 0.43 |
| Workshop | 1.19 |

**Additional Lighting Power Allowances**:
- Display/Accent lighting: 0.6 W/ft² or 150 W (whichever is less)
- Wall wash lighting: 0.40 W/linear foot of wall
- Retail accent lighting: 0.6 W/ft² over merchandise area
- Decorative lighting: 0.4 W/ft²

#### 4.1.2 Building Area Method (Table C405.4.2(2))

**Maximum Lighting Power Densities by Building Type**:

| Building Type | Maximum LPD (W/ft²) |
|--------------|---------------------|
| Automotive Facility | 0.48 |
| Convention Center | 0.71 |
| Courthouse | 0.74 |
| Dining: Bar Lounge/Leisure | 0.65 |
| Dining: Cafeteria/Fast Food | 0.65 |
| Dining: Family | 0.89 |
| Dormitory | 0.50 |
| Exercise Center | 0.72 |
| Gymnasium | 0.72 |
| Healthcare Clinic | 0.71 |
| Hospital | 0.87 |
| Hotel/Motel | 0.54 |
| Library | 0.71 |
| Manufacturing Facility | 0.48 |
| Motion Picture Theater | 0.50 |
| Multifamily | 0.41 |
| Museum | 0.57 |
| Office | 0.60 |
| Parking Garage | 0.19 |
| Penitentiary | 0.69 |
| Performing Arts Theater | 1.19 |
| Police/Fire Station | 0.71 |
| Post Office | 0.63 |
| Religious Building | 0.71 |
| Retail | 0.90 |
| School/University | 0.64 |
| Sports Arena | 0.78 |
| Town Hall | 0.74 |
| Transportation | 0.48 |
| Warehouse | 0.30 |
| Workshop | 0.84 |

### 4.2 Exterior Lighting (IECC C405.5)

**Exterior Lighting Power Allowances** (Table C405.5.2(2) - Uncovered Parking):

| Zone | Description | Maximum LPD (W/ft²) |
|------|------------|---------------------|
| 1 | Developed areas in national parks, state parks, forest land | 0.015 |
| 2 | Areas predominantly residential zones | 0.04 |
| 3 | Areas of mixed use | 0.06 |
| 4 | Areas predominantly commercial/industrial | 0.10 |

**Tradable Exterior Lighting Power** (Table C405.5.2(1)):

| Application | LPD Base Allowance |
|------------|-------------------|
| Building Entrance (main) | 30 W per linear foot of door width |
| Building Entrance (other) | 20 W per linear foot of door width |
| Canopy | 1.25 W/ft² |
| Parking (uncovered) | Per zone (see table above) |
| Pedestrian Plaza | 0.14 W/ft² |
| Walkways ≤10 ft wide | 1.0 W per linear foot |
| Roadway | 0.15 W/ft² |

**Exterior Lighting Controls** (IECC C405.5.1):
- **Astronomical time switch or photosensor** required for all exterior lighting
- Reduction to 30% or less of full power required during non-business hours
- Exception: Lighting for 24-hour operations

---

## 5. COMPLIANCE PATHS AND CALCULATION METHODS

### 5.1 Three Compliance Paths

The IECC 2021 offers three alternative compliance paths for commercial buildings:

#### 5.1.1 Mandatory + Prescriptive Path

**Requirements**:
1. Meet all **mandatory provisions** in Chapter 4 (IECC C4)
2. Meet all **prescriptive requirements** in Chapter 4
   - Building envelope: Tables C402.1.3, C402.4
   - HVAC systems: Section C403
   - Service water heating: Section C404
   - Lighting: Section C405
   - Additional systems: Section C406

**Advantages**:
- No energy modeling required
- Straightforward compliance documentation
- Suitable for simple buildings with standard systems

**Limitations**:
- Less flexibility in design trade-offs
- May result in more expensive solutions
- Cannot trade envelope for HVAC efficiency

#### 5.1.2 Mandatory + Performance Path

**Requirements**:
1. Meet all **mandatory provisions** in Chapter 4
2. Demonstrate through energy modeling that:
   - **Proposed building** ≤ **Baseline building** (modeled per prescriptive)
   - Annual energy cost of proposed design ≤ annual cost of baseline
3. Use approved energy modeling software (DOE-2, EnergyPlus, eQUEST, TRACE, etc.)
4. Follow modeling rules in **ASHRAE 90.1-2019 Appendix G**

**Modeling Requirements**:
- 8760-hour annual simulation
- Weather data: TMY3 or equivalent for project location
- All energy end-uses included (HVAC, lighting, SWH, receptacle, process)
- Energy rates: Actual utility rates or state average commercial rates
- Cost escalation not permitted

**Documentation**:
- Input and output reports from simulation software
- Schedules, loads, and assumptions documentation
- Compliance form signed by design team

**Advantages**:
- Design flexibility (trade envelope for HVAC, etc.)
- Can optimize whole-building energy performance
- Often results in lower energy costs

**Limitations**:
- Requires energy modeling expertise
- More expensive/time-consuming documentation
- Subject to review by code officials

#### 5.1.3 Mandatory + ERI Path (Residential Only)

**Requirements** (IECC R406):
1. Meet all mandatory provisions in Chapter 4 (residential)
2. Calculate **Energy Rating Index (ERI)** using approved software
3. Demonstrate **ERI ≤ ERI Target** for climate zone

**ERI Targets by Climate Zone** (Table R406.4):

| Climate Zone | Maximum ERI |
|--------------|------------|
| 1 | 57 |
| 2 | 57 |
| 3 | 57 |
| 4 | 54 |
| 5 | 55 |
| 6 | 54 |
| 7 | 53 |
| 8 | 53 |

**ERI Definition**:
- **ERI = 100**: 2006 IECC reference home
- **ERI = 0**: Net-zero energy home
- Lower ERI = better energy performance

**Approved Software**:
- RESNET-accredited energy rating software
- REM/Rate, EnergyGauge USA, REM/Design, etc.
- Must be certified to ANSI/RESNET/ICC 301 standard

**Advantages**:
- Flexibility in design trade-offs
- Industry-standard metric (used for certifications)
- Can trade insulation for HVAC efficiency

### 5.2 Compliance Software Tools

**Commercial Buildings**:
- **COMcheck**: Free DOE tool for prescriptive compliance
- **eQUEST**: Detailed energy simulation (DOE-2 based)
- **EnergyPlus**: Open-source whole-building simulation
- **TRACE 3D Plus**: Trane energy modeling software
- **IES-VE**: Integrated Environmental Solutions modeling suite

**Residential Buildings**:
- **REScheck**: Free DOE tool for prescriptive compliance
- **REM/Rate**: RESNET-accredited rating software
- **EnergyGauge USA**: RESNET-accredited simulation tool
- **HERS Index Calculator**: Home Energy Rating System tools

---

## 6. COMMON STATE AMENDMENTS

### 6.1 California (Title 24)

**Adoption Status**: California does not adopt IECC; uses Title 24 Part 6 (Energy Code)

**Key Differences from IECC 2021**:
- **More stringent** envelope requirements in most climate zones
- Mandatory **solar PV** for new residential (effective 2020)
- Mandatory **battery storage** for new residential (effective 2023)
- Prescriptive **HERS verification** required for many measures
- Mandatory **time-dependent valuation (TDV)** for performance path
- California-specific climate zones (16 zones vs. IECC 8 zones)
- **JA4 envelope compliance** reporting forms required

**Title 24 2022 Edition**:
- Effective January 1, 2023
- Photovoltaic and battery requirements for residential
- Enhanced ventilation requirements (ASHRAE 62.2 + California amendments)
- Electric-ready requirements for new construction

### 6.2 Massachusetts

**Adoption Status**: Adopts IECC with state amendments (9th Edition Base Code)

**Key Amendments**:
- IECC 2021 adopted with Massachusetts-specific modifications
- **Stretch Energy Code** available as opt-in for municipalities
  - Net Zero Appendix available (most stringent)
- Massachusetts Climate Zones: 5A (most of state), 6A (Berkshires)
- Additional air sealing requirements
- Enhanced commissioning requirements for commercial buildings

**Stretch Energy Code Highlights**:
- HERS Index ≤ 45 for residential (vs. IECC ERI 55)
- Zero fossil fuel for space/water heating in new residential
- Enhanced envelope requirements
- Mandatory blower door testing (≤3.0 ACH50)

### 6.3 New York

**Adoption Status**: Adopts IECC 2018 with amendments (2020 Energy Code)

**Key Amendments**:
- Currently on **IECC 2018** (not yet adopted 2021)
- New York Climate Zones: 4A, 5A, 6A depending on location
- New York City uses **NYC Energy Conservation Code**
  - Based on ASHRAE 90.1-2016 for commercial
  - More stringent than statewide code
- Mandatory commissioning for buildings >50,000 ft²
- Enhanced air barrier and testing requirements

### 6.4 Florida

**Adoption Status**: Adopts IECC 2021 with amendments (Florida Energy Code)

**Key Amendments**:
- IECC 2021 adopted effective December 31, 2023
- Florida Climate Zones: 1A (south), 2A (central/north)
- **Wind resistance requirements** integrated with energy code
- High-velocity hurricane zone (HVHZ) additional requirements
- Solar-ready zone mandatory provisions for residential roofs
- Enhanced duct sealing and testing requirements

**Florida-Specific Considerations**:
- High cooling loads dominate energy use
- SHGC requirements critical (solar heat gain)
- Air sealing and moisture control paramount
- Hurricane-rated equipment required in HVHZ

### 6.5 Texas

**Adoption Status**: No statewide mandatory code; local jurisdictions adopt individually

**Common Adoptions**:
- Major cities adopt **IECC 2021** or **IECC 2018**
  - Dallas: IECC 2021
  - Houston: IECC 2021
  - Austin: Austin Energy Code (more stringent than IECC)
  - San Antonio: IECC 2021
- Texas Climate Zones: 2A (most), 2B (far west), 3A (north)
- Highly variable by jurisdiction

**Austin Energy Code** (Most Stringent):
- Based on IECC + enhanced requirements
- Mandatory HERS rating ≤ 60 for residential
- Enhanced envelope and HVAC requirements
- Rebate programs for exceeding minimum

### 6.6 Illinois

**Adoption Status**: Adopts IECC 2021 (effective January 1, 2023)

**Key Provisions**:
- Illinois Climate Zone: 5A (entire state)
- IECC 2021 prescriptive path most common
- Chicago adopts **Chicago Energy Conservation Code**
  - Based on IECC + amendments
  - More stringent commercial requirements
  - Mandatory commissioning >10,000 ft²

---

## 7. INTEGRATION WITH MEP QA VALIDATION

### 7.1 How IECC Connects to Drawing QA

The IECC 2021 energy code compliance drives multiple MEP design decisions that must be validated during QA review:

#### 7.1.1 HVAC System QA Validation

**Equipment Schedules Must Show**:
- Minimum efficiency ratings (SEER2, EER, HSPF2, COP, AFUE)
- Climate zone determination documented
- Equipment manufacturer/model numbers verified for compliance
- Performance ratings from AHRI or equivalent certification

**Drawing Checks**:
- Verify outdoor air rates meet ASHRAE 62.1 minimums (IECC C403.7)
- Demand control ventilation shown for applicable spaces
- Energy recovery shown where required (>5,000 cfm OA)
- Economizer provisions where required by climate zone
- Control sequences note setpoint requirements

**Example QA Rule**:
```
IF climate_zone IN [3, 4, 5, 6, 7, 8]
AND outdoor_air_supply >= 5000_CFM
THEN energy_recovery_required = TRUE
AND enthalpy_recovery_ratio >= 50%
```

#### 7.1.2 Lighting System QA Validation

**Lighting Schedules Must Show**:
- Lighting power density calculations (space-by-space or building area method)
- Total connected load ≤ maximum LPD × floor area
- Fixture types, quantities, and wattages
- Control zones and strategies

**Drawing Checks**:
- Automatic shutoff controls shown (occupancy sensors, time switches)
- Daylight-responsive controls in applicable spaces (>250W, sidelighting/toplighting)
- Exterior lighting controls (astronomical time switch or photosensor)
- Lighting control panel schedules show zoning meeting IECC C405.2.2

**Example QA Rule**:
```
IF space_type = "Office - Open"
AND total_lighting_watts / area_sf > 0.61_W_per_sf
THEN FAIL("Exceeds IECC C405.4 LPD for Open Office")
```

#### 7.1.3 Electrical Load Calculations QA

**Service Size Verification**:
- HVAC equipment efficiency affects connected load (higher efficiency = lower draw)
- Lighting LPD compliance affects lighting loads in service calc
- Service water heating equipment efficiency affects load

**Drawing Integration**:
- Panelboard schedules reflect actual loads meeting IECC efficiency
- Generator sizing accounts for code-minimum HVAC loads
- Transformer sizing based on compliant equipment

#### 7.1.4 Plumbing/FP System Considerations

**Service Water Heating**:
- Water heater efficiency ratings shown on schedules (UEF, Et, SL)
- Pipe insulation meeting IECC C404.5 shown on details
- Recirculation pump controls documented (IECC C404.7)
- Solar water heating pre-plumbing shown (where required)

**Drawing Checks**:
- Verify water heater efficiency ≥ IECC Table C404.2
- Pipe insulation R-value ≥ IECC Table C403.11.3
- Temperature maintenance systems show controls

### 7.2 Climate Zone Impact on QA Rules

The project climate zone fundamentally changes QA validation rules:

**Example: Envelope Validation Rule Set**

```python
# Pseudo-code for climate-zone-specific QA rules
def validate_wall_insulation(climate_zone, wall_type, r_value):
    requirements = {
        "1": {"steel_framed": 13 + 3.8},   # R-13 + R-3.8 ci
        "2": {"steel_framed": 13 + 3.8},
        "3": {"steel_framed": 13 + 7.5},   # R-13 + R-7.5 ci
        "4": {"steel_framed": 13 + 12.5},  # More stringent
        "5": {"steel_framed": 13 + 15.6},
        "6": {"steel_framed": 13 + 15.6},
        "7": {"steel_framed": 13 + 18.8},
        "8": {"steel_framed": 13 + 18.8},
    }

    required = requirements[climate_zone][wall_type]

    if r_value < required:
        return f"FAIL: Wall R-value {r_value} < required {required} for CZ {climate_zone}"
    return "PASS"
```

**Example: HVAC Efficiency Validation**

```python
def validate_heat_pump_efficiency(climate_zone, capacity_btuh, cooling_seer2, heating_hspf2):
    # Climate zones 1-3: Higher cooling emphasis
    # Climate zones 5-8: Higher heating emphasis

    if capacity_btuh < 65000:
        min_cooling = 14.3
        min_heating = 7.5 if climate_zone in ["5", "6", "7", "8"] else 7.5
    else:
        min_cooling = 13.6
        min_heating = 6.7

    issues = []
    if cooling_seer2 < min_cooling:
        issues.append(f"Cooling SEER2 {cooling_seer2} < {min_cooling}")
    if heating_hspf2 < min_heating:
        issues.append(f"Heating HSPF2 {heating_hspf2} < {min_heating}")

    return "FAIL: " + "; ".join(issues) if issues else "PASS"
```

### 7.3 Compliance Documentation in QA Workflow

**Required Deliverables for Code Compliance**:
1. **COMcheck/REScheck Reports** (prescriptive path)
   - Must be included in submittal package
   - QA validates report matches drawings

2. **Energy Model Reports** (performance path)
   - Baseline and proposed building comparison
   - Annual energy cost comparison
   - Model inputs match design documents

3. **Lighting Power Density Calculations**
   - Space-by-space or building area method
   - Total connected load summary
   - Control strategy narrative

4. **Equipment Efficiency Documentation**
   - AHRI certificate numbers for all equipment
   - Manufacturer cut sheets showing ratings
   - Commissioning plan for verification

**QA Validation Sequence**:
```
1. Verify climate zone determination documented
2. Check compliance path documented (prescriptive/performance/ERI)
3. Validate COMcheck/REScheck report present and current
4. Cross-check equipment schedules against IECC minimums
5. Verify lighting calculations and control strategies
6. Check mechanical ventilation rates and ERV provisions
7. Validate service water heating efficiency and controls
8. Confirm mandatory provisions met (all paths)
```

---

## 8. ADDITIONAL MANDATORY REQUIREMENTS

### 8.1 Air Leakage (IECC C402.5)

**Commercial Building Envelope**:
- Maximum **0.40 cfm/ft²** @ 75 Pa (0.08 inches w.g.) for building envelope
- Testing required per **ASTM E779** or **ASTM E1827**
- Alternative: Visual inspection per **ATTCP Section 5** if no testing

**Residential Buildings**:
- Maximum **5.0 ACH50** for Climate Zones 1-2
- Maximum **3.0 ACH50** for Climate Zones 3-8
- Testing required per **ANSI/RESNET/ICC 380** (blower door)

### 8.2 Duct and Pipe Insulation (IECC C403.11)

**Supply Ducts and Plenums**:

| Location | Minimum R-Value |
|----------|----------------|
| Outdoors | R-8 |
| Unconditioned space | R-6 |
| Buried (below grade) | R-8 |
| Indirectly conditioned space | R-6 |

**Return Ducts**:

| Location | Minimum R-Value |
|----------|----------------|
| Outdoors | R-6 |
| Unconditioned space | R-6 |

**Hydronic Piping**:
- Minimum **R-3** for piping >1½" diameter
- Minimum **R-2** for piping ≤1½" diameter

### 8.3 Equipment Controls (IECC C403.4)

**Mandatory Controls**:
- Automatic thermostat setback/setup (unoccupied periods)
- Humidity control with deadband (if humidification provided)
- Ventilation system controls (outdoor air dampers, interlocks)
- Zone controls (individual control for <600 ft² per zone)
- Shutoff dampers (isolation for economizers and ventilation)

---

## 9. REFERENCES AND RESOURCES

### 9.1 Primary Code Documents

1. **ICC IECC 2021**: International Energy Conservation Code, 2021 Edition
   - Available: https://codes.iccsafe.org/
   - Purchase: International Code Council

2. **ASHRAE 90.1-2019**: Energy Standard for Buildings Except Low-Rise Residential
   - Available: https://www.ashrae.org/technical-resources/bookstore
   - Referenced for equipment efficiencies

3. **ASHRAE 62.1-2019**: Ventilation for Acceptable Indoor Air Quality
   - Referenced for outdoor air requirements

### 9.2 Online Tools and Resources

- **DOE Building Energy Codes Program**: https://www.energycodes.gov/
  - Climate zone maps
  - COMcheck and REScheck free tools
  - Compliance guides and fact sheets

- **PNNL Building America**: https://basc.pnnl.gov/
  - Climate zone information
  - Envelope requirement tables
  - Technical guidance

- **ASHRAE Free Resources**: https://www.ashrae.org/technical-resources
  - Free standards access (read-only)
  - Technical guidance documents

- **ICC Code Adoption Maps**: https://www.iccsafe.org/products-and-services/i-codes/code-adoption-maps/
  - State-by-state adoption status

### 9.3 State-Specific Resources

- **California Title 24**: https://www.energy.ca.gov/programs-and-topics/programs/building-energy-efficiency-standards
- **Massachusetts Stretch Energy Code**: https://www.mass.gov/stretch-energy-code
- **New York Energy Code**: https://dos.ny.gov/energy-code
- **Florida Energy Code**: https://www.floridabuilding.org/c/default.aspx
- **Austin Energy Green Building**: https://austinenergy.com/green-building

### 9.4 Additional Standards Referenced

- **ANSI/RESNET/ICC 301**: Standard for the Calculation and Labeling of the Energy Performance of Dwelling and Sleeping Units
- **AHRI Standards**: Air-Conditioning, Heating, and Refrigeration Institute equipment certification
  - AHRI 210/240: Performance rating of unitary AC and heat pumps
  - AHRI 340/360: Commercial unitary equipment
  - AHRI 550/590: Water chilling packages
- **DOE 10 CFR Part 430**: Energy conservation program for consumer products
- **DOE 10 CFR Part 431**: Energy efficiency standards for commercial equipment

---

## 10. DOCUMENT CONTROL

**Version**: 1.0
**Effective Date**: 2025-10-22
**Author**: Agent 1 - Energy Code Specialist
**Review Cycle**: Annual or upon code adoption changes

**Paraphrasing Notice**: All content in this document has been paraphrased from publicly available sources. No verbatim reproduction of copyrighted code text is included. Users should consult official code publications for legal compliance.

**Jurisdiction Disclaimer**: This summary reflects the IECC 2021 base code. Local jurisdictions may adopt different editions or amendments. Always verify the specific code edition and amendments adopted in your project jurisdiction before finalizing design.

**Integration Note**: This document supports the MEP Drawing QA/QC workflow defined in `skills/engineering-drawing-qaqc/SKILL.md`. Climate zone determination and energy code compliance are prerequisite inputs for validation rules.

---

**End of Document**
