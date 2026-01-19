# LEED v4.1 BD+C MEP Requirements

**Document Purpose**: Comprehensive reference for LEED v4.1 Building Design and Construction (BD+C) requirements affecting MEP systems design and QA validation

**Last Updated**: 2025-10-22

**Sources**:
- USGBC LEED v4.1 BD+C Rating System (publicly available information)
- ASHRAE Standards (90.1, 62.1, 55, 189.1)
- EPA GreenChill Program
- ENERGY STAR Portfolio Manager
- ISO 50001 Energy Management Standards
- Professional green building engineering practice

---

## 1. LEED RATING SYSTEM OVERVIEW

### 1.1 LEED v4.1 Building Design and Construction (BD+C)

**Rating Systems under BD+C**:
- **LEED BD+C: New Construction**
- **LEED BD+C: Core and Shell**
- **LEED BD+C: Schools**
- **LEED BD+C: Retail**
- **LEED BD+C: Data Centers**
- **LEED BD+C: Warehouses and Distribution Centers**
- **LEED BD+C: Hospitality**
- **LEED BD+C: Healthcare**

**Certification Levels**:

| Level | Minimum Points | Typical Achievement |
|-------|---------------|---------------------|
| **Certified** | 40-49 points | Entry-level green building |
| **Silver** | 50-59 points | Above-average sustainability |
| **Gold** | 60-79 points | High-performance building |
| **Platinum** | 80+ points | Exceptional sustainability leadership |

**Total Available**: 110 points + 10 bonus points (Innovation, Regional Priority)

### 1.2 LEED Credit Categories

| Category | Maximum Points | MEP Impact |
|----------|---------------|------------|
| **Location and Transportation (LT)** | 16 | Low (site planning, not MEP-focused) |
| **Sustainable Sites (SS)** | 10 | Low-Moderate (stormwater, heat island) |
| **Water Efficiency (WE)** | 11 | **High** (plumbing fixtures, irrigation) |
| **Energy and Atmosphere (EA)** | 33 | **Very High** (HVAC, lighting, renewables) |
| **Materials and Resources (MR)** | 13 | Low (construction waste, not MEP) |
| **Indoor Environmental Quality (EQ)** | 17 | **High** (ventilation, thermal comfort, lighting) |
| **Innovation (IN)** | 6 | Variable (innovative MEP strategies) |
| **Regional Priority (RP)** | 4 | Variable (location-specific) |

**MEP Focus Categories**: Water Efficiency (WE), Energy and Atmosphere (EA), Indoor Environmental Quality (EQ)

---

## 2. ENERGY AND ATMOSPHERE (EA) CREDITS

**Category Total**: 33 points (30% of total score)

### 2.1 EA Prerequisite 1: Fundamental Commissioning and Verification (REQUIRED)

**Intent**: Support design, construction, and operation of energy-efficient, high-performance buildings.

**Requirements**:
1. **Commissioning Authority (CxA)**:
   - Independent party (not on design or construction team)
   - Responsible for commissioning process oversight
   - May be employee of owner or separate firm

2. **Owner's Project Requirements (OPR)**:
   - Document owner's sustainability and performance goals
   - Includes energy efficiency, water efficiency, indoor air quality goals
   - **MEP Impact**: Define HVAC, lighting, and controls performance targets

3. **Basis of Design (BOD)**:
   - Document design team's strategy to meet OPR
   - Describes HVAC systems, lighting systems, controls sequences
   - Updated throughout design process

4. **Commissioning Plan**:
   - CxA develops plan for commissioning activities
   - Includes equipment to be commissioned, testing requirements, schedules

5. **Equipment and Systems to be Commissioned**:
   - **HVAC systems** and controls
   - **Lighting** and daylighting controls
   - **Domestic hot water** systems
   - **Renewable energy systems** (if applicable)

6. **Activities**:
   - Design review (OPR/BOD alignment)
   - Submittal review (equipment specifications)
   - Verification of installation and performance
   - Systems manual (O&M documentation)
   - Training of building operators

**Documentation**:
- Commissioning plan
- OPR and BOD
- Commissioning reports (design review, verification testing)
- Systems manual
- Training records

### 2.2 EA Prerequisite 2: Minimum Energy Performance (REQUIRED)

**Intent**: Reduce environmental and economic impacts of excessive energy use.

**Requirements (Choose One Path)**:

#### Option 1: Whole-Building Energy Simulation (Performance Path)

**Requirements**:
- Demonstrate **5% improvement** over **ASHRAE 90.1-2016 Appendix G** baseline
- Use approved simulation software (DOE-2, EnergyPlus, eQUEST, TRACE, IES-VE, etc.)
- Include all energy end-uses (HVAC, lighting, service water heating, receptacle, process)

**Modeling Requirements**:
- Baseline building per ASHRAE 90.1-2016 Appendix G (rotated orientations, prescriptive systems)
- Proposed building with actual design systems
- Annual energy cost comparison (proposed ≤ 95% of baseline)

**MEP Design Impact**:
- HVAC equipment efficiency selections
- Lighting power density (LPD) and controls
- Envelope (coordinated with architect)
- Service water heating efficiency
- Renewable energy systems (if included)

#### Option 2: Prescriptive Compliance Path (Prescriptive Option 1)

**Requirements**:
- Meet ASHRAE 90.1-2016 mandatory provisions (Sections 5.4, 6.4, 7.4, 8.4, 9.4, 10.4)
- Prescriptive requirements for envelope, lighting, HVAC, service water heating

**MEP Design Impact**:
- Minimum equipment efficiency (ASHRAE 90.1 Tables 6.8.1-1 through 6.8.1-21)
- Maximum lighting power density (ASHRAE 90.1 Tables 9.5.1 and 9.6.1)
- Duct/pipe insulation minimums
- Controls requirements (thermostats, occupancy sensors, daylighting controls)

### 2.3 EA Prerequisite 3: Building-Level Energy Metering (REQUIRED)

**Intent**: Support energy management and identify opportunities for additional savings.

**Requirements**:
- Install **building-level energy meter** (whole-building electricity consumption)
- Meter must be able to:
  - Record data at intervals ≤1 hour
  - Transmit data to remote location or store for ≥18 months
  - Interface with building automation system (BAS) or separate data collection system

**Data Collection**:
- Monthly energy consumption (kWh)
- Monthly energy cost ($)
- Collected for ≥5 years (post-occupancy)

**MEP Design Impact**:
- Electrical: Specify revenue-grade meter at service entrance
  - Digital meter with pulse output or Modbus RTU/TCP communication
  - Integration with BAS or energy management system (EMS)

**Documentation**:
- Meter specification and location
- Data collection plan

### 2.4 EA Prerequisite 4: Fundamental Refrigerant Management (REQUIRED)

**Intent**: Reduce ozone depletion and support early compliance with Montreal Protocol.

**Requirements (Choose One)**:

#### Option 1: No Refrigerants
- Do not install HVAC&R equipment with refrigerants
- Evaporative cooling, chilled beams (water-side only), ground-source heat pumps (water-to-water)

#### Option 2: Reduced Refrigerant Impact
- Calculate **total refrigerant impact** using formula:
  ```
  LCGWP + LCODP × 10⁵ ≤ Threshold
  ```
  Where:
  - LCGWP = Life-Cycle Global Warming Potential (lb CO₂e / ton-year)
  - LCODP = Life-Cycle Ozone Depletion Potential (lb CFC-11e / ton-year)

**MEP Design Impact**:
- Select refrigerants with low GWP (Global Warming Potential)
- Select refrigerants with zero ODP (Ozone Depletion Potential)
- Preferred refrigerants:
  - **R-410A**: Zero ODP, moderate GWP (2088)
  - **R-32**: Zero ODP, lower GWP (675)
  - **R-454B**: Zero ODP, very low GWP (466)
  - **R-744 (CO₂)**: Zero ODP, GWP = 1 (natural refrigerant)
- Avoid legacy refrigerants:
  - **R-22**: High ODP (0.055), being phased out
  - **R-134a**: Zero ODP, high GWP (1430)

**Refrigerant Leakage Rates**:
- Assume 2% annual leakage for typical HVAC systems
- Low-leak design: 0.5% annual leakage (better seals, monitoring)

**Documentation**:
- Refrigerant type and quantity for all HVAC equipment
- LCGWP and LCODP calculations
- Leak detection system (if used to reduce leakage assumption)

### 2.5 EA Credit: Enhanced Commissioning (6 points)

**Intent**: Further support design, construction, and operation beyond fundamental commissioning.

**Requirements (3 points for items 1-2, +3 points for items 3-4)**:

1. **Prior to Mid-Construction** (1 point):
   - CxA reviews contractor submittals for commissioned systems
   - Develops systems manual outline

2. **Prior to Substantial Completion** (2 points):
   - CxA conducts on-site review of equipment installation
   - CxA verifies operator training completion
   - Complete systems manual delivered

3. **Within 10 Months of Substantial Completion** (+2 points):
   - CxA conducts review of building operation with O&M staff
   - Review building performance, seasonal testing
   - Document ongoing commissioning issues

4. **Enhanced Systems Include** (+1 point):
   - Envelope commissioning (air barrier, insulation, fenestration)
   - Lighting controls and daylighting systems
   - Domestic hot water systems
   - Irrigation systems (if applicable)

**MEP Design Impact**:
- Require MEP systems designed for testability
- Controls sequences documented in detail (for verification)
- Test ports and sensors accessible for commissioning

**Documentation**:
- Enhanced commissioning plan
- Submittal reviews
- Installation verification reports
- Operator training records
- 10-month review report (if pursuing)

### 2.6 EA Credit: Optimize Energy Performance (18 points)

**Intent**: Achieve increasing levels of energy performance to reduce environmental impacts.

**Requirements**:
- Energy model demonstrating improvement over ASHRAE 90.1-2016 Appendix G baseline
- Points awarded based on % improvement (cost-based)

**Point Thresholds (New Construction, Non-Residential)**:

| % Improvement Over Baseline | Points Awarded |
|----------------------------|---------------|
| 6% | 1 |
| 8% | 2 |
| 10% | 3 |
| 12% | 4 |
| 14% | 5 |
| 16% | 6 |
| 18% | 7 |
| 20% | 8 |
| 22% | 9 |
| 24% | 10 |
| 26% | 11 |
| 28% | 12 |
| 30% | 13 |
| 32% | 14 |
| 34% | 15 |
| 36% | 16 |
| 38% | 17 |
| 40%+ | 18 |

**Note**: Residential projects and other rating systems have different thresholds

**MEP Strategies to Achieve Points**:

1. **HVAC Efficiency** (5-15% improvement):
   - Higher efficiency equipment (exceed ASHRAE 90.1 minimums)
     - Variable refrigerant flow (VRF) systems
     - High-efficiency chillers (water-cooled centrifugal, magnetic bearing)
     - Premium-efficiency boilers (condensing boilers, >90% efficiency)
   - Energy recovery ventilation (ERV) - exhaust air heat recovery
   - Demand control ventilation (DCV) - CO₂-based outdoor air control
   - Variable speed drives (VSDs) on pumps, fans, cooling tower fans
   - Dedicated outdoor air systems (DOAS) with separate sensible/latent cooling

2. **Lighting** (3-8% improvement):
   - LED lighting throughout
   - Lower lighting power density (LPD) than ASHRAE 90.1 allowances
   - Daylighting controls (dimming in perimeter zones)
   - Occupancy sensors (all spaces, not just required by code)
   - Personal lighting controls (task lighting, reduced ambient levels)

3. **Envelope** (3-10% improvement):
   - Higher R-values for walls, roofs, floors (exceed code minimum)
   - Lower U-factors for windows (high-performance glazing)
   - Lower SHGC (solar heat gain coefficient) in cooling-dominated climates
   - Reduced air infiltration (enhanced air sealing, <0.25 cfm/ft²@75Pa)

4. **Renewable Energy** (5-20% improvement):
   - On-site solar photovoltaic (PV) systems
   - Solar thermal (service water heating or space heating)
   - Wind turbines (if site suitable)
   - Geothermal heat pumps (ground-source heat pumps)

5. **Service Water Heating** (1-3% improvement):
   - High-efficiency water heaters (heat pump water heaters, condensing gas)
   - Solar thermal pre-heating
   - Heat recovery from refrigeration or process equipment

**Example Energy Model Summary**:
```
Baseline Building (ASHRAE 90.1-2016 Appendix G):
  - Annual Energy Cost: $100,000
  - Chiller: Air-cooled, 9.5 EER
  - Boiler: 80% combustion efficiency
  - Lighting: 0.90 W/ft² (building area method)
  - Envelope: Code-minimum R-values

Proposed Building:
  - Annual Energy Cost: $72,000 (28% savings)
  - Chiller: Water-cooled centrifugal, 0.50 kW/ton (COP 7.0)
  - Boiler: Condensing, 95% efficiency
  - Lighting: 0.60 W/ft² (LED + controls)
  - Envelope: R-30 walls, U-0.30 windows
  - Solar PV: 50 kW array (5% of building load)

Points Earned: 12 points (28% improvement)
```

**Documentation**:
- Whole-building energy model report (baseline and proposed)
- Equipment schedules showing efficiency ratings
- Renewable energy system capacity (if applicable)

### 2.7 EA Credit: Advanced Energy Metering (1 point)

**Intent**: Support energy management and identify additional opportunities for savings through advanced metering.

**Requirements**:
- Install **submeters** for end-uses representing ≥80% of total annual energy consumption
- Minimum end-uses to submeter:
  - **HVAC systems** (chillers, boilers, air handlers)
  - **Interior lighting** (by floor or zone)
  - **Exterior lighting**
  - **Receptacle loads** (by floor or zone)
  - **Process loads** (if applicable)

**Metering Requirements**:
- Record data at intervals ≤1 hour
- Transmit to building automation system (BAS) or energy management system (EMS)
- Data storage ≥36 months
- Support ENERGY STAR Portfolio Manager data entry

**MEP Design Impact**:
- Electrical: Submeter specifications
  - Individual circuit breaker meters (MCCB with metering), OR
  - Branch circuit monitoring systems (BCMS), OR
  - Power monitoring system with CTs on feeders
- All submeters with communication protocol (Modbus, BACnet, Ethernet/IP)

**Documentation**:
- Submetering plan showing end-uses covered
- Equipment specifications
- System architecture (communication to BAS/EMS)

### 2.8 EA Credit: Demand Response (2 points)

**Intent**: Increase participation in demand response programs to reduce peak energy loads and improve grid reliability.

**Requirements (Choose One)**:

#### Option 1: Load Shedding (1 point)
- Demonstrate ability to reduce building electrical demand by ≥10% for ≥4 hours
- Load shedding strategies:
  - Curtail non-critical lighting
  - Raise cooling setpoints (76°F → 78°F)
  - Reduce ventilation to minimum code levels
  - Shed non-critical receptacle loads (task lighting, vending machines)

#### Option 2: Demand Response Program Participation (2 points)
- Enroll building in utility or ISO demand response program
- Commit to participate for ≥10 years

**MEP Design Impact**:
- Controls: BAS capable of automated demand response (Auto-DR)
  - OpenADR 2.0 protocol support (LBNL standard)
  - Automated load shedding sequences programmed
- Metering: Real-time demand monitoring (kW)
- Shedding strategies:
  - Lighting controls (reduce to 70% in non-critical areas)
  - HVAC controls (reset setpoints, reduce outdoor air)
  - Energy storage (if battery backup installed, discharge during peak)

**Documentation**:
- Load shedding plan (sequences, estimated reduction)
- Demand response program enrollment agreement (if Option 2)
- Controls narrative

### 2.9 EA Credit: Renewable Energy Production (3 points)

**Intent**: Reduce environmental impacts from fossil fuel energy use through on-site renewable energy generation.

**Requirements**:
- Generate renewable energy on-site (or within project boundary)
- Achieve % of annual energy use from renewables

**Point Thresholds**:

| % of Annual Energy Use | Points |
|-----------------------|--------|
| 1% | 1 |
| 3% | 2 |
| 5% | 3 |

**Eligible Renewable Energy Systems**:
- **Solar photovoltaic (PV)** - most common
- **Solar thermal** (service water heating)
- **Wind turbines** (if site suitable)
- **Geothermal electricity** (binary cycle plants)
- **Biogas/Biomass** (anaerobic digestion, sustainable biomass)
- **Hydroelectric** (small-scale, low-head)

**Solar PV Sizing Example**:
```
Building Annual Energy Use: 500,000 kWh/year
Target: 3% renewable = 15,000 kWh/year

PV System Sizing:
  - System capacity = 15,000 kWh / (1,400 kWh/kW-year × 0.8 derate) ≈ 13.4 kW DC
  - Select: 15 kW DC solar array (60 × 250W panels)

Assumptions:
  - Solar resource: 1,400 kWh/kW-year (varies by location, use PVWatts)
  - System derate: 0.80 (soiling, shading, inverter losses)
```

**MEP Design Impact**:
- Electrical: Solar PV system integration
  - Inverter sizing and location
  - AC disconnect and overcurrent protection
  - Connection to electrical service (supply-side or load-side tap)
  - Net metering (if utility allows) or on-site consumption only
- Roof coordination: PV array layout (avoid shading, maximize south exposure)
- Electrical room: Space for inverters, DC/AC disconnects

**Documentation**:
- Renewable energy system capacity (kW DC for PV)
- Annual energy production estimate (kWh/year from PVWatts or equivalent)
- % of building energy use from renewables

---

## 3. WATER EFFICIENCY (WE) CREDITS

**Category Total**: 11 points (10% of total score)

### 3.1 WE Prerequisite: Outdoor Water Use Reduction (REQUIRED)

**Intent**: Reduce outdoor water consumption.

**Requirements (Choose One)**:

#### Option 1: No Irrigation
- Do not install permanent landscape irrigation systems
- Natural precipitation only

#### Option 2: Reduced Irrigation
- Reduce landscape irrigation by ≥30% from calculated baseline
- Use EPA WaterSense Water Budget Tool or equivalent

**MEP Design Impact**:
- Plumbing/Irrigation: High-efficiency irrigation (if provided)
  - Drip irrigation for plantings
  - Weather-based irrigation controllers (ET controllers)
  - Soil moisture sensors
  - Rain sensors (shut off during precipitation)

**Documentation**:
- No irrigation commitment, OR
- Irrigation calculations showing ≥30% reduction

### 3.2 WE Prerequisite: Indoor Water Use Reduction (REQUIRED)

**Intent**: Reduce indoor water consumption.

**Requirements**:
- Reduce aggregate water consumption by ≥20% from calculated baseline
- Use EPA WaterSense Water Calculator or LEED calculator

**Baseline Fixture Flush/Flow Rates** (per LEED v4.1):

| Fixture Type | Baseline Rate |
|-------------|--------------|
| Water closet (toilet) | 1.6 gpf (gallons per flush) |
| Urinal | 1.0 gpf |
| Lavatory faucet | 2.2 gpm @ 60 psi (private), 0.5 gpm (public) |
| Shower | 2.5 gpm @ 80 psi |
| Kitchen sink | 2.2 gpm @ 60 psi |

**High-Efficiency Fixture Targets** (20% reduction minimum):

| Fixture Type | High-Efficiency Rate | % Reduction |
|-------------|---------------------|-------------|
| Water closet (toilet) | 1.28 gpf (WaterSense) | 20% |
| Dual-flush toilet | 1.1 gpf average | 31% |
| Urinal | 0.5 gpf (pint flush) | 50% |
| Waterless urinal | 0.0 gpf | 100% |
| Lavatory faucet | 1.5 gpm (private), 0.5 gpm (public) | 32% (private) |
| Shower | 2.0 gpm (WaterSense) | 20% |

**MEP Design Impact**:
- Plumbing: Specify WaterSense-labeled fixtures throughout
- Fixture schedules show flush/flow rates
- Water use calculation (fixture count × usage × flush rate)

**Documentation**:
- Plumbing fixture schedule with flush/flow rates
- Water use reduction calculation (baseline vs. design)

### 3.3 WE Credit: Outdoor Water Use Reduction (2 points)

**Intent**: Further reduce outdoor water consumption.

**Requirements**:

| % Reduction from Baseline | Points |
|--------------------------|--------|
| 50% | 1 |
| No irrigation (or 100% reduction) | 2 |

**MEP Strategies**:
- Native/adaptive plantings (require less water)
- Drip irrigation (most efficient delivery)
- Rainwater harvesting for irrigation (cisterns)
- Graywater reuse for irrigation (laundry, cooling tower blowdown)

**Documentation**:
- Irrigation calculations (or no irrigation commitment)

### 3.4 WE Credit: Indoor Water Use Reduction (6 points)

**Intent**: Further reduce indoor water consumption.

**Requirements**:

| % Reduction from Baseline | Points |
|--------------------------|--------|
| 25% | 1 |
| 30% | 2 |
| 35% | 3 |
| 40% | 4 |
| 45% | 5 |
| 50% | 6 |

**MEP Strategies**:
- Ultra-low-flow fixtures:
  - 1.0 gpf dual-flush toilets
  - 0.125 gpf waterless urinals
  - 0.5 gpm public lavatory faucets
  - 1.5 gpm private lavatory faucets
  - 1.5 gpm showerheads
- Sensor-operated faucets (reduce waste from running water)
- Pre-rinse spray valves (commercial kitchens): 1.3 gpm vs. 2.2 gpm baseline

**Ultra-High-Efficiency Fixture Example**:
```
Office Building: 200 occupants, 8-hour shifts

Baseline Water Use:
  - WC: 1.6 gpf × 3 uses/day × 200 occupants = 960 gpd
  - Urinals: 1.0 gpf × 2 uses/day × 100 male occupants = 200 gpd
  - Lavatories: 0.5 gpm × 30 sec × 3 uses/day × 200 / 60 = 150 gpd
  Total: 1,310 gpd (gallons per day)

Design Water Use:
  - WC: 1.1 gpf (dual-flush avg) × 3 uses/day × 200 = 660 gpd
  - Urinals: 0.125 gpf (waterless) × 2 uses/day × 100 = 25 gpd
  - Lavatories: 0.5 gpm × 30 sec × 3 uses/day × 200 / 60 = 150 gpd
  Total: 835 gpd

Reduction: (1,310 - 835) / 1,310 = 36% → 3 points
```

**Documentation**:
- Plumbing fixture schedule with flush/flow rates
- Water use calculation

### 3.5 WE Credit: Cooling Tower Water Use (2 points)

**Intent**: Conserve water through efficient cooling tower operation.

**Requirements (Achieve ≥2 of the following)**:

1. **Conductivity Controllers and Automated Chemical Feed**:
   - Maintain cycles of concentration (COC) ≥4.0 (potable water makeup)
   - Higher COC = less blowdown = less water waste

2. **Eliminate Once-Through Cooling**:
   - No single-pass cooling (water-cooled condensers discharging to drain)
   - Closed-loop cooling towers or air-cooled equipment only

3. **Non-Potable Water for Makeup**:
   - Use captured rainwater, graywater, or reclaimed water for ≥20% of makeup water

4. **Cover Cooling Tower When Not in Use**:
   - Seasonal cover to reduce evaporation during off-season

**MEP Design Impact**:
- HVAC: Cooling tower with conductivity controller
  - Automated blowdown control (maintain COC ≥4)
  - Chemical feed system (scale/corrosion inhibitors)
- Plumbing: Non-potable water connection (if graywater/rainwater available)

**Cycles of Concentration Calculation**:
```
COC = Makeup Water Conductivity / Blowdown Water Conductivity

Higher COC = Less Blowdown (water savings)

Example:
Makeup: 500 µS/cm (microsiemens per centimeter)
Blowdown: 2000 µS/cm
COC = 2000 / 500 = 4.0 (meets requirement)

Water Savings:
  - 3 COC: 33% blowdown loss
  - 4 COC: 25% blowdown loss (8% water savings)
  - 5 COC: 20% blowdown loss (13% water savings vs. 3 COC)
```

**Documentation**:
- Cooling tower specification (conductivity controller)
- COC target (≥4.0)
- Non-potable water source (if applicable)

---

## 4. INDOOR ENVIRONMENTAL QUALITY (EQ) CREDITS

**Category Total**: 17 points (15% of total score)

### 4.1 EQ Prerequisite: Minimum Indoor Air Quality Performance (REQUIRED)

**Intent**: Contribute to occupant comfort and well-being through good indoor air quality.

**Requirements**:
- Design outdoor air ventilation to meet **ASHRAE 62.1-2016** minimum rates

**ASHRAE 62.1 Ventilation Rates** (Selected Occupancies):

| Space Type | People Outdoor Air (cfm/person) | Area Outdoor Air (cfm/ft²) |
|-----------|------------------------------|--------------------------|
| Office Space | 5 | 0.06 |
| Conference Room | 5 | 0.06 |
| Classroom | 10 | 0.12 |
| Retail | 7.5 | 0.06 |
| Corridor | - | 0.06 |
| Restroom | - | - (exhaust only) |
| Gym/Weight Room | 20 | 0.06 |
| Auditorium | 5 | 0.06 |

**Ventilation Rate Calculation** (Ventilation Rate Procedure):
```
Voz = Rp × Pz + Ra × Az

Where:
  Voz = Zone outdoor airflow (cfm)
  Rp = People outdoor air rate (cfm/person)
  Pz = Zone population (people)
  Ra = Area outdoor air rate (cfm/ft²)
  Az = Zone floor area (ft²)

Example (Office Space):
  Rp = 5 cfm/person, Ra = 0.06 cfm/ft²
  Pz = 20 people, Az = 3,000 ft²

  Voz = (5 × 20) + (0.06 × 3,000) = 100 + 180 = 280 cfm minimum outdoor air
```

**MEP Design Impact**:
- HVAC: Outdoor air ventilation design
  - Dedicated outdoor air system (DOAS), OR
  - Outdoor air intake on air handling units (AHUs)
  - Minimum outdoor air dampers (sized for ASHRAE 62.1 rates)
  - Outdoor air measurement (airflow stations)

**Documentation**:
- Ventilation design calculations per ASHRAE 62.1
- HVAC system outdoor air rates documented

### 4.2 EQ Prerequisite: Environmental Tobacco Smoke Control (REQUIRED)

**Intent**: Prevent exposure of building occupants to environmental tobacco smoke (ETS).

**Requirements (Choose One)**:

#### Option 1: No Smoking
- Prohibit smoking inside building and within 25 ft of entries, outdoor air intakes, operable windows
- Signage at building entries

#### Option 2: Separate Smoking Rooms
- Dedicated smoking rooms with:
  - Self-closing doors
  - Deck-to-deck partitions
  - Negative pressure (≥0.02 inches w.g. relative to adjacent spaces)
  - Direct exhaust to outdoors (no recirculation)
  - Minimum 60 cfm/person outdoor air
  - Sealing of penetrations

**MEP Design Impact** (if Option 2):
- HVAC: Dedicated exhaust system for smoking rooms
  - Separate exhaust fan (no connection to general exhaust)
  - Discharge above roof, away from air intakes

**Documentation**:
- Smoking policy (signage locations), OR
- Smoking room design (pressurization, exhaust calculations)

### 4.3 EQ Credit: Enhanced Indoor Air Quality Strategies (2 points)

**Intent**: Promote occupants' well-being through enhanced indoor air quality.

**Requirements (1 point each, max 2 points)**:

#### Option 1: Enhanced Outdoor Air Ventilation (1 point)
- Increase outdoor air ventilation rates by ≥30% above ASHRAE 62.1-2016 minimums

**Example**:
```
Baseline OA: 280 cfm (from prerequisite example)
Enhanced OA: 280 × 1.30 = 364 cfm minimum

Design outdoor air = 370 cfm (meets requirement)
```

#### Option 2: CO₂ Monitoring (1 point)
- Install CO₂ sensors in all densely occupied spaces (≥25 people/1000 ft²)
- Sensor locations: 3-6 ft above floor in breathing zone
- Display CO₂ levels to occupants (visible display or BAS-accessible)

**MEP Design Impact**:
- HVAC: Demand control ventilation (DCV) with CO₂ sensors
  - Modulate outdoor air based on actual occupancy (CO₂ proxy)
  - Setpoint: 1,000-1,200 ppm typical (maintain <700 ppm above outdoor)
- Controls: CO₂ sensor specifications (accuracy ±50 ppm)
  - Wired to BAS for monitoring and control

**Documentation**:
- Enhanced ventilation rates (calculations), OR
- CO₂ sensor locations and specifications

### 4.4 EQ Credit: Low-Emitting Materials (3 points)

**Intent**: Reduce indoor air concentrations of pollutants from building materials.

**Requirements**:
- Specify low-VOC (volatile organic compound) materials for ≥80% (by cost or surface area) of products in each category

**MEP Impact** (Limited - mostly architectural materials):
- Adhesives/sealants: Low-VOC duct sealants, pipe joint compounds
- Insulation: Low-emitting thermal and acoustic insulation (duct lining, pipe insulation)
- Paints/coatings: Equipment painting (if required)

**Applicable Standards**:
- **SCAQMD Rule 1168** (adhesives/sealants)
- **SCAQMD Rule 1113** (architectural coatings)
- **California Section 01350** (low-emitting materials)
- **GreenGuard Gold Certification** (furniture, insulation)

**Documentation**:
- Product data sheets with VOC content
- Certifications (GreenGuard, Section 01350 compliant)

### 4.5 EQ Credit: Thermal Comfort (1 point)

**Intent**: Promote occupants' productivity and well-being through thermal comfort.

**Requirements**:
- Design HVAC systems to meet **ASHRAE 55-2017** thermal comfort criteria
- Demonstrate compliance using:
  - Predicted Mean Vote (PMV) and Predicted Percentage Dissatisfied (PPD) method, OR
  - Elevated Air Speed method, OR
  - Adaptive Comfort method (naturally ventilated spaces)

**ASHRAE 55 Comfort Zones**:
- **Winter** (0.5 clo clothing): 68-75°F operative temperature, 30-60% RH
- **Summer** (0.5 clo clothing): 73-79°F operative temperature, 30-60% RH

**MEP Design Impact**:
- HVAC: Temperature control by zone
  - Individual zone thermostats (not central control for entire floor)
  - Setpoint range: 70-76°F cooling, 68-74°F heating
- Humidity control: Dehumidification (maintain <60% RH)

**Documentation**:
- HVAC design narrative (temperature control strategy)
- ASHRAE 55 compliance statement

### 4.6 EQ Credit: Interior Lighting (2 points)

**Intent**: Promote occupants' productivity and well-being through effective lighting design.

**Requirements (1 point each)**:

#### Option 1: Lighting Control (1 point)
- Provide individual or group lighting controls for ≥90% of occupants
  - Individual controls: Task lights, dimmers at workstations
  - Group controls: Zones ≤200 ft² or ≤6 people per control

**MEP Design Impact**:
- Electrical/Lighting: Dimming controls in open offices
  - Zone lighting by workstation groups (<6 people)
  - Wall-mounted dimmer switches or occupancy sensors with local override

#### Option 2: Daylight (1 point)
- Provide daylight illumination to ≥55% of regularly occupied floor area
  - 2% sDA (Spatial Daylight Autonomy), OR
  - Calculation/simulation method, OR
  - Prescriptive method (glazing area, geometry)

**MEP Design Impact**:
- Electrical/Lighting: Daylighting controls (photocell dimming)
  - Automatically dim lights when daylight sufficient (perimeter zones)
  - Daylight sensors: 1 per 400 ft² of daylit area

**Documentation**:
- Lighting control plan (zones, control types), OR
- Daylighting analysis (sDA calculation or prescriptive)

### 4.7 EQ Credit: Acoustic Performance (1 point)

**Intent**: Provide workspaces and classrooms that promote occupants' well-being through effective acoustic design.

**Requirements**:
- Meet **ANSI S12.60** (classrooms) or **FGI Guidelines** (healthcare) acoustical performance requirements
- Parameters:
  - **Background noise** (HVAC systems): NC 35 or less (classrooms), NC 30-40 (offices)
  - **Reverberation time** (RT60): ≤0.7 seconds (classrooms <10,000 ft³), ≤0.8 seconds (>10,000 ft³)
  - **Sound Transmission Class (STC)**: ≥50 for partitions between critical spaces

**MEP Design Impact**:
- HVAC: Acoustic design for low noise
  - Duct silencers on supply/return near AHUs
  - Flex duct connections at diffusers (vibration isolation)
  - Low-velocity ductwork (≤1,500 fpm in occupied spaces)
  - Equipment vibration isolation (springs, pads)
  - Rooftop equipment: Locate away from occupied spaces
- Plumbing: Quiet pipe supports (isolate water hammer)

**NC (Noise Criteria) Curves**:

| Space Type | Target NC |
|-----------|----------|
| Private Office | 30-35 |
| Open Office | 35-40 |
| Conference Room | 25-30 |
| Classroom | 30-35 |
| Hospital Patient Room | 30-35 |

**Documentation**:
- Acoustic design narrative (HVAC noise control measures)
- Background noise calculations (NC curves)

---

## 5. ADDITIONAL LEED CREDITS WITH MEP IMPACT

### 5.1 SS Credit: Rainwater Management (3 points)

**Intent**: Reduce runoff volume and improve water quality through stormwater management.

**MEP Connection**:
- Green roof systems (HVAC roof coordination: ensure adequate clearances)
- Rainwater harvesting cisterns (plumbing integration for non-potable uses)

### 5.2 SS Credit: Heat Island Reduction (2 points)

**Intent**: Minimize effects on microclimates and human/wildlife habitats.

**MEP Connection**:
- Cool roofs (high SRI - Solar Reflectance Index) affect HVAC cooling loads
- Rooftop HVAC equipment layout coordinated with reflective roofing

---

## 6. COMMISSIONING REQUIREMENTS SUMMARY

### 6.1 Fundamental Commissioning (Prerequisite)

**Commissioned Systems** (Minimum):
- HVAC systems and controls
- Lighting and daylighting controls
- Domestic hot water systems
- Renewable energy systems

**Activities**:
- Design review (OPR/BOD alignment)
- Submittal review
- Verification testing
- Systems manual
- Operator training

### 6.2 Enhanced Commissioning (Credit)

**Additional Requirements**:
- Submittal reviews by CxA
- On-site installation verification
- Operator training verification
- 10-month post-occupancy review (optional +2 points)
- Envelope commissioning (optional +1 point)

**Envelope Commissioning** (if pursuing):
- Air barrier testing (blower door or tracer gas)
- Insulation inspection (thermal imaging)
- Fenestration performance verification

---

## 7. MEASUREMENT AND VERIFICATION (M&V)

### 7.1 EA Credit: Optimize Energy Performance (Option Path 3 - UNUSED IN MOST PROJECTS)

**Intent**: Support energy performance through ongoing measurement and verification.

**Requirements** (If M&V Path Selected):
- Develop M&V plan per **ASHRAE Guideline 14** or **IPMVP** (International Performance Measurement and Verification Protocol)
- Meter end-uses representing ≥80% of total energy consumption
- Monitor for ≥1 year post-occupancy

**M&V Plan Contents**:
- Baseline energy model
- Metering and monitoring plan
- Analysis methodology (monthly comparison of actual vs. predicted)
- Corrective action plan if performance <target

**MEP Design Impact**:
- Advanced energy metering (same as EA Credit: Advanced Energy Metering)

---

## 8. LEED CERTIFICATION DOCUMENTATION FOR MEP

### 8.1 Required MEP Documentation Submittals

**Energy and Atmosphere (EA)**:
- [ ] Commissioning plan and reports
- [ ] Energy model (baseline and proposed) - if performance path
- [ ] Equipment schedules with efficiency ratings
- [ ] Lighting power density calculations
- [ ] Renewable energy system capacity and production estimates
- [ ] Energy metering plan (building-level and submeters)
- [ ] Refrigerant calculations (LCGWP, LCODP)
- [ ] Demand response plan (if pursuing credit)

**Water Efficiency (WE)**:
- [ ] Plumbing fixture schedule with flush/flow rates
- [ ] Water use calculations (baseline vs. design)
- [ ] Irrigation calculations (if applicable)
- [ ] Cooling tower conductivity controller specs (if applicable)

**Indoor Environmental Quality (EQ)**:
- [ ] Ventilation calculations per ASHRAE 62.1
- [ ] Smoking policy or smoking room design (if applicable)
- [ ] CO₂ sensor locations (if pursuing enhanced IAQ)
- [ ] Thermal comfort analysis (ASHRAE 55)
- [ ] Lighting control plan
- [ ] Acoustic design calculations (if pursuing acoustic credit)

### 8.2 Drawing Requirements for LEED

**Mechanical Drawings**:
- Outdoor air ventilation rates shown on schedules (cfm)
- Equipment efficiency ratings on schedules (SEER, EER, COP, AFUE)
- Refrigerant type and quantity on equipment schedules
- Energy recovery ventilators (ERV) shown and scheduled
- Demand control ventilation (DCV) noted on control diagrams
- CO₂ sensor locations (if required)
- Duct/pipe insulation R-values noted

**Plumbing Drawings**:
- Fixture flush/flow rates on plumbing fixture schedule
- Water meter locations (building-level and submeters if applicable)
- Cooling tower makeup water source and treatment
- Rainwater/graywater systems (if applicable)

**Electrical Drawings**:
- Lighting power density (LPD) calculations on schedules
- Lighting control types noted (occupancy sensors, daylighting controls, dimmers)
- Energy meter locations (building-level and submeters)
- Renewable energy system (PV array, inverters, disconnects)
- Generator and ATS (if emergency/standby power)

**Fire Protection Drawings**:
- Minimal direct LEED impact (indirectly affects energy through sprinkler pump loads)

---

## 9. INTEGRATION WITH MEP QA VALIDATION

### 9.1 LEED-Specific QA Validation Rules

**Energy Performance Validation**:
```python
def validate_leed_energy_performance(equipment_list, target_improvement_pct):
    """Validate equipment efficiency selections support LEED energy target."""

    baseline_equipment = get_ashrae_901_baseline(equipment_list)
    proposed_equipment = equipment_list

    baseline_energy = calculate_annual_energy(baseline_equipment)
    proposed_energy = calculate_annual_energy(proposed_equipment)

    improvement_pct = (baseline_energy - proposed_energy) / baseline_energy × 100

    target_points = get_leed_ea_points(target_improvement_pct)

    if improvement_pct < target_improvement_pct:
        return f"FAIL: Energy improvement {improvement_pct:.1f}% < target {target_improvement_pct}% (LEED EA Goal: {target_points} points)"

    return f"PASS: Energy improvement {improvement_pct:.1f}% meets target {target_improvement_pct}%"
```

**Water Efficiency Validation**:
```python
def validate_leed_water_efficiency(fixture_schedule, target_reduction_pct):
    """Validate plumbing fixture selections support LEED water target."""

    baseline_fixtures = {
        "Water Closet": 1.6,  # gpf
        "Urinal": 1.0,         # gpf
        "Lavatory": 2.2,       # gpm
        "Shower": 2.5,         # gpm
    }

    total_baseline_use = calculate_water_use(baseline_fixtures, occupancy)
    total_proposed_use = calculate_water_use(fixture_schedule, occupancy)

    reduction_pct = (total_baseline_use - total_proposed_use) / total_baseline_use × 100

    target_points = get_leed_we_points(target_reduction_pct)

    if reduction_pct < target_reduction_pct:
        return f"FAIL: Water reduction {reduction_pct:.1f}% < target {target_reduction_pct}% (LEED WE Goal: {target_points} points)"

    return f"PASS: Water reduction {reduction_pct:.1f}% meets target {target_reduction_pct}%"
```

**Ventilation Rate Validation**:
```python
def validate_leed_ventilation(space_type, area_sf, occupancy, design_oa_cfm):
    """Validate outdoor air ventilation meets ASHRAE 62.1 (LEED EQ Prerequisite)."""

    ashrae_621_rates = {
        "Office": {"Rp": 5, "Ra": 0.06},
        "Conference": {"Rp": 5, "Ra": 0.06},
        "Classroom": {"Rp": 10, "Ra": 0.12},
        # ... additional space types
    }

    rates = ashrae_621_rates[space_type]
    required_oa_cfm = (rates["Rp"] × occupancy) + (rates["Ra"] × area_sf)

    if design_oa_cfm < required_oa_cfm:
        return f"FAIL: OA ventilation {design_oa_cfm} cfm < ASHRAE 62.1 minimum {required_oa_cfm:.0f} cfm"

    # Check for Enhanced IAQ credit (30% above minimum)
    enhanced_oa_cfm = required_oa_cfm × 1.30
    if design_oa_cfm >= enhanced_oa_cfm:
        return f"PASS: OA ventilation {design_oa_cfm} cfm meets Enhanced IAQ (EQ Credit)"

    return f"PASS: OA ventilation {design_oa_cfm} cfm meets ASHRAE 62.1 (EQ Prerequisite)"
```

### 9.2 LEED Drawing Review Checklist

**Mechanical Drawings**:
- [ ] Equipment schedules show efficiency ratings (SEER, EER, COP, AFUE) ≥ ASHRAE 90.1-2016
- [ ] Outdoor air ventilation rates documented on AHU schedules (cfm)
- [ ] Refrigerant types specified (low GWP preferred)
- [ ] Energy recovery ventilators (ERV) shown if required by climate zone
- [ ] CO₂ sensors shown in densely occupied spaces (if Enhanced IAQ pursued)
- [ ] Cooling tower conductivity controller specified (if WE credit pursued)

**Plumbing Drawings**:
- [ ] Plumbing fixture schedule shows flush/flow rates
- [ ] All fixtures meet WaterSense standards (1.28 gpf toilets, 1.5 gpm faucets)
- [ ] Water meter locations shown (building-level minimum)
- [ ] Irrigation system high-efficiency (drip, weather-based controller) if provided

**Electrical Drawings**:
- [ ] Lighting power density (LPD) ≤ ASHRAE 90.1-2016 allowances
- [ ] Lighting control plan shows occupancy sensors, daylighting controls
- [ ] Energy meter locations shown (building-level and submeters if Advanced Metering pursued)
- [ ] Solar PV system shown (if Renewable Energy credit pursued)
  - [ ] PV array size (kW DC)
  - [ ] Inverter location and rating
  - [ ] AC disconnect and interconnection to electrical service

---

## 10. RESOURCES AND REFERENCES

### 10.1 LEED Resources

- **USGBC**: https://www.usgbc.org/leed/v41
- **LEED Online**: https://www.usgbc.org/leed-online (project registration and documentation)
- **GBCI**: https://www.gbci.org/ (Green Building Certification Institute - credentialing)

### 10.2 Referenced Standards

- **ASHRAE 90.1-2016**: Energy Standard for Buildings (baseline for LEED energy modeling)
- **ASHRAE 62.1-2019**: Ventilation for Acceptable Indoor Air Quality
- **ASHRAE 55-2017**: Thermal Environmental Conditions for Human Occupancy
- **ASHRAE Guideline 14**: Measurement of Energy and Demand Savings
- **EPA WaterSense Calculator**: Water use calculations
- **IPMVP**: International Performance Measurement and Verification Protocol

### 10.3 Calculation Tools

- **LEED Online Calculators**: Built into LEED Online platform
- **Energy Modeling Software**: eQUEST, EnergyPlus, TRACE, IES-VE
- **EPA WaterSense Water Budget Tool**: Irrigation calculations
- **PVWatts**: Solar PV production estimates (NREL)
- **ENERGY STAR Portfolio Manager**: Building energy benchmarking

---

## 11. DOCUMENT CONTROL

**Version**: 1.0
**Effective Date**: 2025-10-22
**Author**: Agent 5 - Sustainability Specialist
**Review Cycle**: Annual or upon LEED rating system updates

**Paraphrasing Notice**: All content paraphrased from publicly available USGBC resources and referenced standards. No verbatim reproduction of copyrighted LEED credit language. Users must consult official LEED v4.1 BD+C rating system for certification requirements.

**Integration Note**: This document supports the MEP Drawing QA/QC workflow defined in `skills/engineering-drawing-qaqc/SKILL.md`. LEED requirements add sustainability validation layer to MEP design review.

---

**End of Document**
