# ASHRAE Standards Index - HVAC and Mechanical Systems

## Document Overview

**Purpose**: Comprehensive reference for ASHRAE (American Society of Heating, Refrigerating and Air-Conditioning Engineers) standards applicable to MEP design, analysis, and quality assurance.

**Scope**: Energy efficiency, ventilation, indoor air quality, thermal comfort, commissioning, and refrigeration standards for building mechanical systems.

---

## ASHRAE Standards Overview

### Primary Standards for MEP Design

| Standard | Title | Primary Focus |
|----------|-------|---------------|
| **ASHRAE 90.1** | Energy Standard for Buildings Except Low-Rise Residential | Energy efficiency, envelope, HVAC, lighting |
| **ASHRAE 62.1** | Ventilation for Acceptable Indoor Air Quality | Outdoor air rates, IAQ procedures |
| **ASHRAE 55** | Thermal Environmental Conditions for Human Occupancy | Comfort zones, PMV/PPD, adaptive comfort |
| **ASHRAE 15** | Safety Standard for Refrigeration Systems | Refrigerant safety, machinery room requirements |
| **ASHRAE 34** | Designation and Safety Classification of Refrigerants | Refrigerant numbering, toxicity/flammability |
| **ASHRAE 189.1** | Standard for Design of High-Performance Green Buildings | Sustainability, green building design |
| **Guideline 0** | Commissioning Process | Commissioning phases, documentation |
| **Guideline 1.1** | HVAC&R Technical Requirements for The Commissioning Process | Functional performance testing |

---

## ASHRAE 90.1 - Energy Standard for Buildings

### Purpose and Scope

Establishes minimum energy efficiency requirements for design and construction of new buildings and their systems.

**Latest Edition**: ASHRAE 90.1-2022 (with 2023 and 2025 addenda in development)
**Applicability**: All buildings except low-rise residential (covered by IECC/IRC)
**Adoptions**: Basis for IECC commercial provisions, adopted by many states

### Standard Structure

**Sections**:
1. Purpose, Scope, and Administration
2. Definitions
3. Compliance
4. **Building Envelope**
5. **Heating, Ventilating, and Air Conditioning (HVAC)**
6. **Service Water Heating**
7. **Power**
8. **Lighting**
9. **Referenced Standards**
10. Other Equipment
11. Energy Cost Budget Method
12. Normative References

Appendices: Climate zones, modeling procedures, informative references

### Section 3: Compliance Paths

**Three Compliance Options**:

1. **Prescriptive Compliance** (Sections 4-10):
   - Meet all mandatory provisions
   - Meet prescriptive requirements for each system
   - Simplest approach, component-by-component

2. **Building Energy Cost Budget Method** (Section 11):
   - Proposed design energy cost ≤ Baseline building energy cost
   - Whole-building performance approach
   - Allows trade-offs between systems
   - Requires approved energy modeling software

3. **Performance Rating Method** (Appendix G):
   - Demonstrates better than standard performance
   - Used for green building certifications (LEED)
   - Most flexible but most complex

### Climate Zones (Figure 3.1, Table B-2)

ASHRAE defines 8 thermal climate zones (1-8) and 3 moisture regimes (A, B, C):

| Zone | Description | Representative Cities |
|------|-------------|---------------------|
| **1A** | Very Hot - Humid | Miami, FL |
| **2A** | Hot - Humid | Houston, TX |
| **2B** | Hot - Dry | Phoenix, AZ |
| **3A** | Warm - Humid | Atlanta, GA |
| **3B** | Warm - Dry | Las Vegas, NV |
| **3C** | Warm - Marine | San Francisco, CA |
| **4A** | Mixed - Humid | New York, NY |
| **4B** | Mixed - Dry | Albuquerque, NM |
| **4C** | Mixed - Marine | Seattle, WA |
| **5A** | Cool - Humid | Chicago, IL |
| **5B** | Cool - Dry | Denver, CO |
| **6A** | Cold - Humid | Minneapolis, MN |
| **6B** | Cold - Dry | Helena, MT |
| **7** | Very Cold | Duluth, MN |
| **8** | Subarctic/Arctic | Fairbanks, AK |

### Section 5: HVAC Requirements

#### 5.2 Mandatory Provisions

**Equipment Efficiency** (Section 5.2.1):
- Minimum efficiency requirements in Tables 6.8.1-1 through 6.8.1-16
- Examples:
  - Air conditioners <65,000 Btu/h: 14 SEER2 minimum
  - Water-cooled chillers (150-300 tons): 0.610 kW/ton max
  - Gas furnaces: 80% AFUE minimum
  - Boilers (>300 kBtu/h): 82% combustion efficiency

**Load Calculations** (Section 5.2.2):
- Must be performed in accordance with approved methods
- ASHRAE Fundamentals Handbook Chapter 18 (residential)
- ASHRAE Fundamentals Handbook Chapters 17-18 (non-residential)
- ACCA Manual J (residential)

**Equipment and System Sizing** (Section 5.2.3):
- Heating: Based on design heating load
- Cooling: Based on design cooling load
- Oversizing limits (except certain applications)

**Ventilation** (Section 5.2.4):
- Mechanical ventilation required per ASHRAE 62.1 or IMC
- Outdoor air intake location requirements

**Exhaust Hoods** (Section 5.2.5):
- Kitchen hoods: ASHRAE 154 or IMC
- Laboratory hoods: ANSI/AIHA Z9.5

**Controls** (Section 5.2.6 - 5.2.12)**:
- Thermostatic controls: deadband ≥5°F between heating and cooling
- Setpoint overlap restriction
- Off-hour controls (automatic shutdown)
- Optimum start controls
- Zone controls
- Shutoff damper controls (relief, exhaust, economizer)

#### 5.3 Prescriptive Path Requirements

**Economizers** (Section 5.3.1.1):

Required for:
- Air-cooled equipment ≥54,000 Btu/h (Climate Zones 3-8)
- Water-cooled equipment ≥54,000 Btu/h (all climate zones)

Exceptions:
- Systems serving spaces with open refrigerated casework
- Systems with extensive humidification
- Systems in Climate Zones 1, 2 (air-cooled only)

**Economizer Types**:
- Differential dry-bulb
- Differential enthalpy
- Fixed dry-bulb
- Fixed enthalpy
- Electronic enthalpy

**Energy Recovery** (Section 5.3.1.2):

Required when outdoor air supply ≥ thresholds in Table 5.3.1.2:

| Climate Zone | Outdoor Air (% of design flow) |
|-------------|-------------------------------|
| 3B, 3C, 4C, 5B, 5C, 6B, 7, 8 | ≥30% |
| 1B, 2B, 3A, 4A, 5A, 6A | ≥40% |
| 1A, 2A | ≥50% |

**Effectiveness Requirements**:
- Enthalpy recovery ratio: ≥50%
- Design conditions: 0°F heating, 95°F/67°F WB cooling

**Ductwork Insulation** (Table 5.4.3.3):

| Location | Min Insulation (R-value) |
|----------|------------------------|
| Outdoor supply ducts | R-8 |
| Outdoor return ducts | R-6 |
| Unconditioned space supply ducts | R-6 |
| Unconditioned space return ducts (CZ 1-4) | R-3.5 |
| Unconditioned space return ducts (CZ 5-8) | R-6 |

**Duct Sealing** (Section 5.4.3.2):
- Seal class: Seal Class B (or better)
- Duct leakage testing required for ducts >5000 cfm
- Leakage limit: 6% at 1 inch w.g. (supply), 3% (return/exhaust)

**Piping Insulation** (Table 5.4.4.2):

| Fluid Temperature Range | Nominal Pipe Diameter | Min Insulation Thickness |
|------------------------|---------------------|------------------------|
| >350°F | ≤1 inch | 2.5 inches |
| >350°F | >8 inches | 5.0 inches |
| 201°F - 350°F | ≤1 inch | 1.5 inches |
| 201°F - 350°F | >8 inches | 4.0 inches |
| 105°F - 200°F | All sizes | 1.0 inch |
| 55°F - 105°F | All sizes | 0.5 inch |
| 40°F - 55°F (chilled water) | All sizes | 1.0 inch |
| <40°F (glycol, refrigerant) | All sizes | 1.5 inches |

**Hydronic System Controls** (Section 5.3.2):

- **Automatic temperature reset** for supply water temperature (or returnwater temperature for radiant heating)
  - Heating systems: outdoor air or representative zone load
  - Cooling systems: outdoor air, zone load, or chilled water plant demand
- **Differential pressure reset** for variable flow systems
  - Reset based on valve position or zone demand
- **Hydronic pump isolation**: dedicated shutoff valve and check valve

**Fan Speed Control** (Section 5.3.3.1):

Variable flow systems required for:
- VAV air distribution systems
- Chilled water and condenser water pumps >10 HP

**Control Types**:
- Variable Frequency Drives (VFD) preferred
- Multiple-speed motors acceptable
- Inlet vanes or dampers not compliant (low efficiency)

**Ventilation Controls** (Section 5.3.3.7):
- Demand control ventilation (DCV) required for spaces >500 ft² with design occupant density >25 people per 1000 ft²
- CO₂ sensors or occupancy sensors

**Chiller Isolation** (Section 5.3.6.1):
- Automatic isolation valves for multiple chiller installations
- Prevents reverse flow through idle chillers

### Section 6: Service Water Heating

**Water Heater Efficiency** (Table 6.8.1-7):

| Equipment Type | Input/Storage | Minimum Efficiency |
|---------------|--------------|-------------------|
| Gas storage ≤75 kBtu/h | ≤55 gal | 0.675 EF (Energy Factor) |
| Gas instantaneous ≥200 kBtu/h | -- | 94% Et (thermal efficiency) |
| Electric storage ≤12 kW | ≤55 gal | 0.93 EF |
| Heat pump water heater | ≤55 gal | 3.75 UEF (Uniform Energy Factor) |

**Piping Insulation** (Section 6.4.4.1.2):
- Hot water piping: 1 inch minimum (fluid >105°F)
- First 8 feet of cold water inlet pipe: 0.5 inch minimum

**Pool Heaters** (Section 6.4.3.7):
- Pool covers required (except safety concerns)
- Time switches for heaters

### Section 7: Power

**Transformer Efficiency** (Table 7.2.2):
- Low-voltage dry-type transformers: efficiency requirements by capacity
- Example: 75 kVA transformer ≥98.0% efficiency at 35% load

**Motor Efficiency** (Table 7.3.1):
- NEMA Premium efficiency motors required for most applications
- Applies to motors 1-500 HP

**Elevator Regenerative Drives** (Section 7.4.5):
- Required for traction elevators ≥50 HP in buildings ≥4 stories

### Section 8: Lighting

**Interior Lighting Power Allowance** (Table 8.3.3.1):

Space-by-space method (W/ft²):

| Space Type | LPD (W/ft²) |
|-----------|-----------|
| Office - Enclosed | 0.96 |
| Office - Open | 0.74 |
| Conference/Meeting | 1.14 |
| Classroom/Lecture | 1.06 |
| Corridor/Transition | 0.49 |
| Lobby | 1.01 |
| Restroom | 0.73 |
| Stairway | 0.48 |
| Storage | 0.52 |

**Lighting Controls** (Section 8.4.3):
- Automatic shutoff: occupancy sensors or time switches
- Space controls: independent control for every 2500 ft² (or enclosed space)
- Daylight-responsive controls for sidelit and toplit zones

### Appendix G: Performance Rating Method

**Baseline Building Model Rules**:

- **HVAC System Type**: Determined by building type and size (Table G3.1.1-1)
  - Residential: System 1 (PTAC) or 2 (PTHP)
  - Non-residential ≤25,000 ft²: System 3 (PSZ-AC) or 4 (PSZ-HP)
  - Non-residential >25,000 ft², ≤5 floors: System 5 (Packaged VAV with reheat) or 6 (Packaged VAV with PFP boxes)
  - Non-residential >75,000 ft², >5 floors: System 7 (VAV with reheat) or 8 (VAV with PFP boxes)

- **Equipment Efficiency**: Minimum from Tables 6.8.1-1 through 6.8.1-16
- **Economizer**: As required by Section 5.3.1.1
- **Energy Recovery**: As required by Section 5.3.1.2
- **Fan Power Limitation**: Based on system type and configuration
- **Supply Air Temperature Reset**: Required for VAV systems
- **Chilled Water Supply Temperature Reset**: Required

**Energy Cost Calculation**:
```
Percent Energy Cost Savings = ((Baseline Cost - Proposed Cost) / Baseline Cost) × 100%
```

**Performance targets**:
- Code compliance: Proposed ≤ Baseline (0% savings)
- LEED v4 BD+C: 5-25% savings (1-10 points)
- Net Zero Energy: 100% savings (with renewables)

### Design Application

**90.1 Compliance Documentation**:
1. Climate zone determination
2. Compliance path selection (prescriptive vs. performance)
3. Load calculations
4. Equipment schedules with efficiency ratings
5. Control sequences of operation
6. Duct and pipe insulation schedules
7. Lighting power density calculations
8. Energy modeling report (if performance path)

**MEP Coordination**:
- Electrical: coordinate motor and transformer efficiencies, lighting power budgets
- Controls: DDC points list, sequences for economizers, energy recovery, DCV
- Plumbing: water heater efficiency, solar thermal interfaces
- Envelope: coordinate outdoor air intakes, exhaust locations

---

## ASHRAE 62.1 - Ventilation for Acceptable Indoor Air Quality

### Purpose and Scope

Minimum ventilation rates and other measures to provide indoor air quality acceptable to human occupants and to minimize adverse health effects.

**Latest Edition**: ASHRAE 62.1-2022 (with 2023 addenda)
**Applicability**: All occupancies except detached single-family, multifamily ≤3 stories, vehicles, aircraft
**Adoptions**: Referenced by IMC, incorporated into ASHRAE 90.1

### Standard Structure

**Sections**:
1. Purpose, Scope, and Administration
2. Definitions
3. General Requirements
4. Outdoor Air Requirements (Prescriptive Procedure)
5. System and Equipment (Design and Operation)
6. Procedures (Performance-based alternatives)
7. Construction and System Start-up
8. Operations and Maintenance
9. Referenced Standards

### Section 4: Outdoor Air Requirements (Ventilation Rate Procedure)

#### 4.2 Breathing Zone Outdoor Airflow

**Formula**:
```
V_bz = R_p × P_z + R_a × A_z

Where:
V_bz = Breathing zone outdoor airflow (cfm)
R_p = Outdoor air flow rate required per person (cfm/person)
R_a = Outdoor air flow rate required per unit area (cfm/ft²)
P_z = Zone population (occupant density × zone area)
A_z = Zone floor area (ft²)
```

**Ventilation Rates** (Table 6.2.2.1 - selected spaces):

| Occupancy Category | People Outdoor Air Rate R_p (cfm/person) | Area Outdoor Air Rate R_a (cfm/ft²) | Default Occupant Density (people/1000 ft²) |
|-------------------|---------------------------------------|----------------------------------|----------------------------------------|
| **Office Buildings** | | | |
| Office space | 5 | 0.06 | 5 |
| Conference/meeting | 5 | 0.06 | 25 |
| Reception | 5 | 0.06 | 30 |
| Telephone/data entry | 5 | 0.06 | 60 |
| **Educational** | | | |
| Classroom (ages 5-8) | 10 | 0.12 | 25 |
| Classroom (ages 9+) | 10 | 0.12 | 35 |
| Computer lab | 10 | 0.12 | 25 |
| Lecture hall | 7.5 | 0.06 | 65 |
| Science labs | 10 | 0.18 | 25 |
| **Hotels** | | | |
| Bedroom/living room | 5 | 0.06 | 10 |
| Multipurpose assembly | 5 | 0.06 | 100 |
| **Retail** | | | |
| Sales | 7.5 | 0.12 | 15 |
| Mall common area | 7.5 | 0.06 | 40 |
| **Sports** | | | |
| Spectator area | 7.5 | 0.06 | 150 |
| Gym/exercise room | 20 | 0.06 | 40 |
| **Restaurants** | | | |
| Dining room | 7.5 | 0.18 | 70 |
| Cafeteria/fast food | 7.5 | 0.18 | 100 |
| Kitchen (commercial) | 15 | 0.12 | 20 |

#### 4.3 System Outdoor Air Intake Flow

For single-zone systems:
```
V_ot = V_bz

Where:
V_ot = Outdoor air intake flow (cfm)
V_bz = Breathing zone outdoor airflow (cfm)
```

For multiple-zone recirculating systems:
```
V_ot = Σ(R_p × P_z × D) + Σ(R_a × A_z)

Where D = 1 + (X_s - Z_p) / E_v

X_s = Uncorrected system outdoor air fraction
Z_p = Zone primary outdoor air fraction
E_v = System ventilation efficiency (Section 6.2.7)
```

**System Ventilation Efficiency** (Table 6.2.7-1):

| System Type | E_v |
|------------|-----|
| Single zone | 1.0 |
| 100% outdoor air | 1.0 |
| Multiple-zone VAV with terminal reheat (Z_p ≤ 0.15) | 0.60 |
| Multiple-zone VAV with terminal reheat (Z_p > 0.55) | 0.85 |
| Multiple-zone VAV with VVT and DDC to zone | 0.80 |

Lower E_v = higher outdoor air intake required for equivalent zone delivery.

#### Example Calculation

**Office Space**:
- Area: 10,000 ft²
- Occupancy: 5 people/1000 ft² = 50 people
- R_p: 5 cfm/person
- R_a: 0.06 cfm/ft²

**Breathing zone outdoor air**:
```
V_bz = (5 cfm/person × 50 people) + (0.06 cfm/ft² × 10,000 ft²)
V_bz = 250 cfm + 600 cfm = 850 cfm
```

**System outdoor air intake** (single zone, E_v = 1.0):
```
V_ot = 850 cfm
```

**System outdoor air intake** (multi-zone VAV, E_v = 0.75):
```
V_ot = 850 cfm / 0.75 = 1,133 cfm
```

### Section 5: Systems and Equipment

**5.1 Air Intakes**:
- Locate to avoid contamination (exhaust, vehicle traffic, cooling towers)
- Separation distances: 10 feet horizontal, 3 feet vertical (typical minimum)
- Screening: protect against rain, insects, debris

**5.2 Local Exhaust**:
- Kitchen hoods: capture contamination, makeup air provided
- Toilet rooms: continuous or automatic operation, negative pressure
- Parking garages: CO monitoring (if enclosed)

**5.3 Filtration** (Table 5.2):

| Outdoor Air Quality | Minimum MERV Filter |
|--------------------|-------------------|
| Good | MERV 6 |
| Moderate | MERV 11 |
| Unhealthy for Sensitive Groups | MERV 13 |
| Unhealthy or worse | MERV 14 or higher |

**Recirculation Air**: MERV 8 minimum

### Section 6: Procedures

**6.1 Indoor Air Quality (IAQ) Procedure**:
- Performance-based alternative to prescriptive ventilation rates
- Requires contaminant concentration analysis
- Used for specialized applications (labs, industrial)

**6.2 Natural Ventilation Procedure**:
- Climate zones 1-3 only (warm/hot climates)
- Window/opening area ≥4% of floor area
- Interior spaces: adjoining rooms with openings ≥8% of interior wall area
- Envelope openings shall be permanent or readily operable

### Design Application

**62.1 Compliance Documentation**:
1. Space-by-space outdoor air calculation (V_bz for each zone)
2. System outdoor air intake calculation (V_ot for each air handler)
3. Occupant density assumptions (default or project-specific)
4. System ventilation efficiency determination
5. Airflow measurement/control locations
6. Filter selection and schedule

**Integration with ASHRAE 90.1**:
- 62.1 determines required outdoor air quantity (IAQ)
- 90.1 determines energy efficiency of delivering that outdoor air
- Energy recovery reduces outdoor air heating/cooling penalty
- Demand control ventilation adjusts outdoor air based on occupancy

**MEP Coordination**:
- Architectural: occupant densities, space programs, operable window coordination
- Electrical: CO₂ sensors, airflow measurement devices, damper actuators
- Fire protection: smoke control, stairwell pressurization outdoor air

---

## ASHRAE 55 - Thermal Environmental Conditions for Human Occupancy

### Purpose and Scope

Specifies combinations of thermal environmental factors and personal factors that produce acceptable thermal environmental conditions for a majority of building occupants.

**Latest Edition**: ASHRAE 55-2023
**Applicability**: Human-occupied spaces for general comfort
**Exclusions**: Unusual activity levels, special thermal requirements (operating rooms, clean rooms)

### Standard Structure

**Sections**:
1. Purpose, Scope, and Administration
2. Definitions
3. General Requirements
4. Normative References
5. Engineering Considerations
6. **Graphical Comfort Zone Method**
7. **Analytical Comfort Zone Method (PMV/PPD)**
8. **Adaptive Comfort Model** (naturally conditioned spaces)

### Section 5: Conditions for Thermal Comfort

**Thermal Comfort Factors**:

**Environmental**:
- Air temperature (°F or °C)
- Radiant temperature (°F or °C)
- Air speed (fpm or m/s)
- Humidity (relative humidity or dew point)

**Personal**:
- Metabolic rate (met)
- Clothing insulation (clo)

**Metabolic Rates** (Table 5.2.1.2):

| Activity | Metabolic Rate (met) |
|----------|-------------------|
| Reclining | 0.8 |
| Seated, quiet | 1.0 |
| Standing, relaxed | 1.2 |
| Office activities (typing, filing) | 1.1 - 1.3 |
| Walking (2 mph on level ground) | 2.0 |
| Sustained hand and arm work | 2.0 - 2.5 |
| Light bench work | 1.6 - 2.0 |

**Typical Design Values**: 1.0 - 1.3 met (sedentary office work)

**Clothing Insulation** (Table 5.2.2.2):

| Ensemble | Insulation (clo) |
|----------|----------------|
| Walking shorts, short-sleeve shirt | 0.36 |
| Trousers, short-sleeve shirt | 0.57 |
| Trousers, long-sleeve shirt | 0.61 |
| Business suit | 1.0 |
| Heavy suit, overcoat | 1.5 |

**Typical Design Values**:
- Summer: 0.5 clo
- Winter: 1.0 clo

### Section 5.3: Graphical Comfort Zone Method

**Acceptable Operating Conditions** (Figure 5.3.1):

For sedentary activity (1.0-1.3 met), typical clothing (0.5 clo summer, 1.0 clo winter):

**Summer (0.5 clo)**:
- Operative temperature range: 73.5°F - 79.5°F (23.0°C - 26.5°C)
- Humidity: 0.012 humidity ratio max (approx. 65% RH at 75°F)
- Air speed: ≤40 fpm (0.2 m/s)

**Winter (1.0 clo)**:
- Operative temperature range: 68.5°F - 75.5°F (20.5°C - 24.0°C)
- Humidity: 0.012 humidity ratio max
- Air speed: ≤30 fpm (0.15 m/s)

**Elevated Air Speed Extension** (Figure 5.3.2):
- Occupant control of air speed: up to 200 fpm (1.0 m/s)
- Allows higher temperature setpoints with increased air movement

### Section 5.4: Analytical Comfort Method (PMV/PPD)

**Predicted Mean Vote (PMV)**:

Scale from -3 (cold) to +3 (hot):
- -3: Cold
- -2: Cool
- -1: Slightly cool
- 0: Neutral
- +1: Slightly warm
- +2: Warm
- +3: Hot

**Predicted Percentage Dissatisfied (PPD)**:
```
PPD = 100 - 95 × e^(-(0.03353×PMV⁴ + 0.2179×PMV²))
```

**Acceptable Thermal Environments**:
- PMV: -0.5 to +0.5 (Category A)
- PMV: -0.7 to +0.7 (Category B)
- PMV: -1.0 to +1.0 (Category C)
- PPD < 10% (for PMV within ±0.5)

**PMV Calculation**:

Complex equation considering:
- Metabolic rate (M)
- Effective mechanical power (W)
- Clothing insulation (I_cl)
- Air temperature (T_a)
- Mean radiant temperature (T_r)
- Air velocity (v_ar)
- Water vapor partial pressure (p_a)

**Online calculators** available on ASHRAE website for PMV/PPD computation.

### Section 5.5: Adaptive Comfort Model

**Applicability**:
- Naturally conditioned spaces (no mechanical cooling)
- Occupants have access to operable windows
- Metabolic rate: 1.0 - 1.3 met
- Outdoor conditions suitable for natural ventilation

**Acceptable Operative Temperature** (Figure 5.5.1):

```
T_comf = 0.31 × T_pma(out) + 17.8°C

Where:
T_comf = Comfort temperature (°C)
T_pma(out) = Prevailing mean outdoor air temperature (°C)
           = arithmetic mean of mean daily outdoor temps for 7-30 days prior
```

**80% Acceptability Limits**: T_comf ± 3.5°C
**90% Acceptability Limits**: T_comf ± 2.5°C

**Example**:
- Prevailing outdoor temperature: 25°C (77°F)
- T_comf = 0.31 × 25 + 17.8 = 25.6°C (78°F)
- 80% acceptability: 22.1°C - 29.1°C (72°F - 84°F)

### Design Application

**HVAC Setpoint Selection**:

**Typical Design Conditions** (based on 55-2023, 0.5/1.0 clo):
- Cooling setpoint: 75°F (24°C) (with humidity control to 65% RH max)
- Heating setpoint: 70°F (21°C)
- Deadband: 5°F minimum (per ASHRAE 90.1)

**High-Performance Building Targets**:
- Expanded comfort range: 68°F - 78°F (20°C - 26°C)
- Adaptive comfort opportunities (operable windows, personal fans)
- Humidity control: 30-60% RH for optimal comfort and IAQ

**Vertical Temperature Stratification** (Section 5.2.5):
- Head-to-ankle temperature difference: <5.4°F (3°C) for seated occupants

**Radiant Asymmetry** (Section 5.2.4):
- Warm ceiling: <9°F (5°C) asymmetry
- Cool wall: <18°F (10°C) asymmetry
- Coordination with radiant heating/cooling systems

**MEP Coordination**:
- Architectural: window operability, shading devices, thermal mass
- Electrical: personal task fans, temperature/humidity sensors
- Controls: adaptive setpoints based on outdoor temperature

---

## ASHRAE 15 - Safety Standard for Refrigeration Systems

### Purpose and Scope

Establishes safeguards for life, limb, health, and property and prescribes safety requirements for refrigeration systems.

**Latest Edition**: ASHRAE 15-2022
**Applicability**: All refrigeration systems, including HVAC chillers, air conditioning equipment, walk-in coolers
**Adoptions**: Referenced by IMC, incorporated into building codes

### Key Requirements

#### Refrigerant Classification (per ASHRAE 34)

**Safety Group** (Table 5):

| Group | Toxicity | Flammability | Common Refrigerants |
|-------|----------|-------------|-------------------|
| **A1** | Lower | No flame propagation | R-134a, R-410A, R-404A, R-407C |
| **A2L** | Lower | Mildly flammable | R-32, R-454B, R-1234yf |
| **A2** | Lower | Flammable | R-152a |
| **A3** | Lower | Highly flammable | R-290 (propane), R-600a (isobutane) |
| **B1** | Higher | No flame propagation | R-123 |
| **B2L** | Higher | Mildly flammable | (few in use) |
| **B2** | Higher | Flammable | (few in use) |
| **B3** | Higher | Highly flammable | R-717 (ammonia) |

#### Refrigerant Charge Limits (Section 7)

**Occupied Spaces**:
- Refrigerant charge limited based on toxicity/flammability classification
- A1 refrigerants: highest allowable charge per room volume
- A2L refrigerants: reduced charge limits
- A3, B2, B3 refrigerants: generally prohibited in occupied spaces without special safeguards

**Example**: R-410A (A1) in direct system:
- Institutional occupancies: 0.015 lb/ft³ max
- General occupancies: 0.044 lb/ft³ max
- Industrial occupancies: 0.29 lb/ft³ max

#### Machinery Room Requirements (Section 8)

**When Required**:
- Systems exceeding charge limits for occupied spaces
- High-probability refrigeration systems (certain occupancies)
- Refrigerant piping in plenums (indirect systems)

**Machinery Room Design**:
- Dedicated to refrigeration equipment (no other systems)
- Self-closing, tight-fitting doors (outward swing)
- Mechanical ventilation: continuous or automatically activated
- Minimum ventilation rate: 0.5 cfm/ft² or refrigerant-specific calculation
- Refrigerant detection and alarm system
- Emergency shut-off (outside machinery room)
- Access limited to authorized personnel
- Explosion-proof electrical if flammable refrigerant

#### Ventilation (Section 8.13)

**Mechanical Ventilation Rate**:
```
Q = 100 × √(G / TLWQ)

Where:
Q = Air flow rate (cfm/lb refrigerant)
G = Mass of refrigerant charge (lb)
TLV = Threshold Limit Value (ppm)
```

For common refrigerants, simplified rates:
- R-134a, R-410A, R-404A: 0.5 cfm/ft² minimum
- R-123 (B1): 1.0 cfm/ft² minimum or more
- Ammonia (R-717): 2.5 cfm/ft² or more

**Emergency Ventilation**:
- Activated by refrigerant detection system
- Higher rate than normal ventilation
- Discharge outdoors (not to return air)

### Design Application

**Refrigerant Selection**:
- A1 refrigerants (R-134a, R-410A): standard applications, minimal restrictions
- A2L refrigerants (R-32, R-454B, R-1234yf): emerging low-GWP options, charge limits apply
- A3 refrigerants (R-290): limited to small appliances, high safety requirements
- B1 refrigerants (R-123): low-pressure chillers, machinery room required

**Chiller Room Coordination**:
- Mechanical: chiller footprint, refrigerant piping, ventilation ductwork
- Electrical: normal power, emergency power for ventilation, explosion-proof fixtures (if flammable)
- Plumbing: floor drains, safety showers (if toxic refrigerant)
- Architectural: room separation, door hardware, signage
- Fire protection: consider suppression system compatibility with refrigerant

---

## ASHRAE Guideline 0 - The Commissioning Process

### Purpose and Scope

Defines the commissioning process for buildings and associated systems, applicable to new construction, existing buildings, and recommissioning.

**Latest Edition**: ASHRAE Guideline 0-2019
**Applicability**: All building types and systems, voluntary standard
**Integration**: Referenced by LEED, ASHRAE 189.1, state/local green building codes

### Commissioning Phases

#### Phase 1: Pre-Design

**Owner's Project Requirements (OPR)**:
- Clear statement of owner's expectations, goals, objectives
- Program requirements (occupancy, hours, space uses)
- Operational needs and philosophies
- Sustainability goals (energy, water, IAQ)
- Budget and schedule

#### Phase 2: Design

**Basis of Design (BOD)**:
- Engineer's documentation of how OPR will be met
- Design concepts, assumptions, criteria
- Code compliance strategies
- System descriptions and performance criteria
- Failure mode considerations

**Commissioning Plan**:
- Commissioning team roles and responsibilities
- Systems to be commissioned (MEP, envelope, renewables)
- Commissioning schedule integrated with project schedule
- Testing and verification procedures
- Documentation requirements

**Design Review**:
- Review submittals at each design phase (SD, DD, CD)
- Verify alignment with OPR and BOD
- Identify conflicts, constructability issues, missing information
- Document findings and recommendations

#### Phase 3: Construction

**Submittal Review**:
- Equipment submittals (compare to design intent)
- Control sequences (verify completeness and accuracy)
- Construction documents (shop drawings, coordination drawings)
- O&M manuals (verify completeness)

**Site Observations**:
- Installation verification (per approved submittals)
- Phased construction checkpoints
- Document deficiencies for correction

**Functional Performance Testing (FPT)**:
- Static testing (verify installed conditions)
- Pre-functional testing (component testing)
- Functional performance testing (system and integrated testing)

#### Phase 4: Occupancy and Operations

**Systems Manual**:
- Compilation of design intent documentation (OPR, BOD)
- As-built drawings and O&M manuals
- Test procedures and results
- Training records
- Warranty information

**Training**:
- Owner's O&M staff training
- Multiple sessions (initial, follow-up, seasonal)
- Hands-on training on actual equipment
- Documentation of training provided

**Commissioning Report**:
- Summary of commissioning activities
- Systems verified and tested
- Deficiencies and resolutions
- Outstanding issues requiring follow-up
- Recommendations for future recommissioning

#### Phase 5: Ongoing Commissioning

**Seasonal Testing**:
- Test all modes of operation (heating, cooling, economizer)
- 10-month post-occupancy testing recommended

**Monitoring-Based Commissioning (MBCx)**:
- Continuous or interval monitoring of key performance indicators
- Automated fault detection and diagnostics (AFDD)
- Trending of energy use, IAQ, comfort

**Recommissioning**:
- Periodic recommissioning every 3-5 years
- Verify systems maintained per original intent
- Update documentation as systems modified

### Systems Commissioned

**Typical Scope**:
- HVAC systems (air handlers, chillers, boilers, terminal units, controls)
- Electrical systems (emergency power, lighting controls, metering)
- Plumbing systems (domestic water heating, rainwater harvesting)
- Renewable energy systems (solar PV, solar thermal, geothermal)
- Building envelope (air barrier, insulation verification)
- Fire protection systems (coordination with fire alarm testing)
- Telecommunications and data systems (optional)

### Guideline 1.1: HVAC&R Technical Requirements

Companion to Guideline 0, provides detailed test procedures for HVAC&R systems:
- Air handling units
- Terminal units (VAV boxes, fan coil units)
- Chillers and cooling towers
- Boilers and pumps
- Control sequences verification
- Integrated system testing

### Design Application

**Commissioning Integration**:

**Design Phase**:
- Incorporate commissioning requirements in specifications (Division 01 91 00)
- Include testable performance criteria in equipment schedules
- Provide detailed control sequences in BAS specifications
- Coordinate commissioning schedule with project milestones

**Construction Phase**:
- Commissioning agent attends site meetings
- Review control shop drawings for sequence accuracy
- Witness factory testing of custom equipment
- Coordinate FPT with construction schedule (avoid delays)

**Documentation**:
- OPR: Updated with design changes
- BOD: Tracks design evolution, documents key decisions
- Commissioning Plan: Living document, updated as project progresses
- Issues Log: Track deficiencies through resolution

**MEP Coordination**:
- Electrical: metering points for monitoring-based commissioning
- Controls: comprehensive points list, trending capabilities, remote access
- Architectural: access for testing equipment, permanent test ports
- Fire protection: coordinate commissioning with fire alarm testing

---

## Cross-Reference: ASHRAE Standards Integration

| Building System | ASHRAE 90.1 | ASHRAE 62.1 | ASHRAE 55 | ASHRAE 15 | Guideline 0 |
|----------------|------------|------------|-----------|-----------|------------|
| **HVAC Equipment** | Efficiency requirements | -- | -- | Refrigerant safety | Functional testing |
| **Ventilation** | Economizers, ERV | Outdoor air rates | -- | -- | Airflow verification |
| **Controls** | Setback, reset, DCV | -- | Setpoint ranges | -- | Sequence verification |
| **Ductwork** | Insulation, sealing | -- | Air speeds | -- | TAB, leakage test |
| **Chilled Water** | Pump VFD, isolation | -- | -- | Chiller room | System performance |
| **Zone Comfort** | -- | Zone OA calculation | Thermal comfort | -- | Temperature, RH verification |

---

## Design and QA/QC Application

### Mechanical Design Checklist

**ASHRAE 90.1 Compliance**:
- [ ] Climate zone determined
- [ ] Equipment efficiencies meet minimum (Tables 6.8.1-x)
- [ ] Economizers provided where required
- [ ] Energy recovery provided where required
- [ ] Ductwork insulation per Table 5.4.3.3
- [ ] Piping insulation per Table 5.4.4.2
- [ ] Duct sealing and leakage testing specified
- [ ] Controls include required resets and setbacks
- [ ] Demand control ventilation provided where required

**ASHRAE 62.1 Compliance**:
- [ ] Breathing zone outdoor air calculated per space type
- [ ] System outdoor air intake accounts for ventilation efficiency
- [ ] Outdoor air measurement/control specified
- [ ] Filters selected per outdoor air quality (Table 5.2)
- [ ] Exhaust air rates for toilets, kitchens determined
- [ ] Air intake location avoids contamination sources

**ASHRAE 55 Comfort**:
- [ ] Design setpoints within comfort zone (73-79°F cooling, 68-76°F heating)
- [ ] Humidity control specified (30-65% RH target)
- [ ] Air speeds at occupied zone ≤40 fpm
- [ ] Radiant asymmetry considered for radiant systems
- [ ] Vertical stratification <5°F for seated occupants

**ASHRAE 15 Refrigerant Safety**:
- [ ] Refrigerant classification verified (A1, A2L, etc.)
- [ ] Refrigerant charge calculated
- [ ] Machinery room required determination
- [ ] Machinery room ventilation designed (if required)
- [ ] Refrigerant detection and alarm specified

**Commissioning Requirements**:
- [ ] OPR and BOD prepared and updated
- [ ] Commissioning Plan prepared
- [ ] Testable performance criteria in specifications
- [ ] Control sequences detailed and complete
- [ ] Commissioning schedule integrated with construction

---

## Document Control

**Last Updated**: 2025-10-22
**Maintained By**: EE_AI Platform - MEP Library
**Review Cycle**: Annual (standards update monitoring)
**Next Review**: 2026-10-22

---

END OF DOCUMENT
