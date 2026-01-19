# Common Electrical Equipment Specifications

**Document Purpose**: Comprehensive reference for electrical equipment types, ratings, and specifications used in MEP design and schedule validation

**Last Updated**: 2025-10-22

**Sources**:
- Eaton electrical equipment catalogs
- Schneider Electric/Square D technical specifications
- ABB electrical product guides
- Siemens power distribution products
- GE Industrial Solutions technical data
- NEMA (National Electrical Manufacturers Association) standards
- UL (Underwriters Laboratories) certification standards
- IEEE (Institute of Electrical and Electronics Engineers) standards
- NEC 2023 (NFPA 70) equipment requirements

---

## 1. SWITCHGEAR

### 1.1 Low Voltage Switchgear (< 1000V)

**Definition**: Metal-enclosed power distribution assembly containing circuit breakers, disconnect switches, metering, and protective relaying in a single integrated unit.

#### 1.1.1 Switchgear Ratings and Classifications

**Voltage Ratings**:
- **208Y/120V** (3-phase, 4-wire)
- **480Y/277V** (3-phase, 4-wire) - most common industrial/commercial
- **600Y/347V** (3-phase, 4-wire) - Canada and high-density applications
- **600V** (3-phase, 3-wire delta)

**Current Ratings (Bus)**:
- 1200A, 1600A, 2000A, 2500A, 3000A, 4000A, 5000A, 6000A

**Short-Circuit Ratings (SCCR / AIC)**:
- **25 kA RMS symmetrical** - Light commercial
- **42 kA RMS symmetrical** - Standard commercial
- **65 kA RMS symmetrical** - Heavy industrial
- **85 kA RMS symmetrical** - High fault current utility connections
- **100 kA RMS symmetrical** - Maximum available (utility-grade)

**Construction Types** (NEMA Standards):

| Type | Description | Enclosure Rating | Typical Application |
|------|-------------|------------------|---------------------|
| **Type 1** | General purpose, indoor | NEMA 1 | Clean, dry indoor environments |
| **Type 3R** | Rainproof, outdoor | NEMA 3R | Outdoor installations, weatherproof |
| **Type 12** | Industrial, dustproof | NEMA 12 | Dusty indoor environments |

**Arc-Flash Mitigation**:
- Zone-selective interlocking (ZSI)
- Arc-flash relays (detect light and current)
- Remote racking (isolate personnel from arc-flash boundary)
- Arc-resistant construction (IEEE C37.20.7)

#### 1.1.2 Switchgear Breaker Types

**Molded Case Circuit Breakers (MCCB)** in Switchgear:
- Frame sizes: 400A, 600A, 800A, 1200A, 1600A, 2000A, 2500A
- Trip units: Thermal-magnetic or electronic
- Interrupting ratings: 14 kA to 200 kA (depending on frame)

**Insulated Case Circuit Breakers (ICCB)**:
- Frame sizes: 800A to 5000A
- Electronic trip units with microprocessor control
- Interrupting ratings: 65 kA to 200 kA
- Suitable for main switchgear service entrance

**Low Voltage Power Circuit Breakers (LVPCB)**:
- Frame sizes: 800A to 6000A
- Fully electronic trip, protection, and monitoring
- Draw-out construction (removable for maintenance)
- Interrupting ratings: 50 kA to 100 kA
- Zone-selective interlocking (ZSI) capable

**Comparison Table**:

| Feature | MCCB | ICCB | LVPCB |
|---------|------|------|-------|
| Frame Size Range | 15A - 2500A | 800A - 5000A | 800A - 6000A |
| Trip Unit | Thermal-mag or electronic | Electronic | Fully electronic |
| Interrupting Capacity | 14 kA - 200 kA | 65 kA - 200 kA | 50 kA - 100 kA |
| Construction | Bolt-in or draw-out | Bolt-in | Draw-out |
| Protection Features | Basic O/C, GF | Advanced O/C, GF, metering | Advanced protection, metering, communications |
| Typical Application | Feeder, branch | Main, tie, feeder | Main switchgear, critical feeders |
| Relative Cost | $ | $$ | $$$ |

**Key**: O/C = Overcurrent, GF = Ground Fault

#### 1.1.3 Switchgear Features and Options

**Standard Features**:
- Main bus (copper or aluminum, silver-plated connections)
- Incoming and outgoing circuit breakers
- Current transformers (CTs) for metering and protection
- Ground fault protection (required by NEC for 480V services >1000A)
- Voltage/current metering (digital multi-function meters)
- Control power transformer (CPT) for 120V control circuits

**Common Options**:
- **Power monitoring system**: Real-time energy metering, power quality analysis
- **Communications**: Modbus RTU, Modbus TCP/IP, BACnet, Ethernet/IP
- **Zone-selective interlocking (ZSI)**: Reduces arc-flash incident energy, faster fault clearing
- **Differential protection**: Main bus differential for fast fault detection
- **Vacuum circuit breakers (VCB)**: Maintenance-free, long service life
- **Remote racking**: Operate breakers remotely (reduce arc-flash exposure)
- **Seismic certification**: IBC seismic design categories D, E, F

**Typical Switchgear Lineup**:
```
[Main Breaker - 2000A] → [Main Bus - 2000A] → [Distribution Section]
    ↓                                              ↓
  Utility                                    [Feeder 1: 400A MCCB]
  Service                                    [Feeder 2: 600A MCCB]
                                             [Feeder 3: 800A ICCB]
                                             [Tie Breaker: 2000A (N.O.)]
```

### 1.2 Medium Voltage Switchgear (1 kV - 38 kV)

**Definition**: Metal-clad or metal-enclosed power distribution for primary utility voltages.

**Common Voltages**:
- **4.16 kV** (3-phase) - industrial plants, campus distribution
- **13.8 kV** (3-phase) - utility distribution, large facilities
- **23 kV** / **34.5 kV** (3-phase) - utility transmission/distribution

**Current Ratings**:
- 600A, 1200A, 2000A, 3000A (bus)

**Short-Circuit Ratings**:
- 25 kA, 31.5 kA, 40 kA, 50 kA (RMS symmetrical)

**Breaker Types**:
- **Vacuum circuit breakers (VCB)**: Most common, maintenance-free, 10,000+ operations
- **SF6 circuit breakers**: High voltage, high interrupting capacity (less common due to environmental concerns)
- **Air-magnetic breakers**: Older technology, being phased out

**Typical Applications**:
- Utility substations
- Industrial plants (refineries, manufacturing)
- Large campus primary distribution (universities, hospitals)
- Commercial high-rises with primary service

---

## 2. TRANSFORMERS

### 2.1 Dry-Type Transformers

**Definition**: Transformers using air as the cooling medium (no oil or liquid insulation).

#### 2.1.1 Voltage Ratings

**Common Primary Voltages**:
- **480V Delta** (most common commercial/industrial)
- **4160V Delta** or **4160Y/2400V** (medium voltage step-down)
- **13.8 kV** (utility primary)

**Common Secondary Voltages**:
- **208Y/120V** (3-phase, 4-wire) - lighting, receptacles, small motors
- **480Y/277V** (3-phase, 4-wire) - motors, large HVAC, 277V lighting
- **240V Delta / 120V** (3-phase, 4-wire high-leg delta) - legacy, not recommended for new construction

#### 2.1.2 kVA Ratings and Sizes

**Single-Phase Transformers**:
- 1 kVA to 333 kVA
- Typical sizes: 5, 10, 15, 25, 37.5, 50, 75, 100, 167, 250, 333 kVA

**Three-Phase Transformers**:
- 3 kVA to 10,000 kVA
- Typical sizes: 15, 30, 45, 75, 112.5, 150, 225, 300, 500, 750, 1000, 1500, 2000, 2500, 3000 kVA

**Sizing Calculation**:
```
Transformer kVA = (Connected Load kVA) / (Diversity Factor) × (Future Growth Factor)

Example:
Connected Load: 800 kVA
Diversity Factor: 0.7 (70% simultaneous demand)
Future Growth: 1.25 (25% spare capacity)

Transformer kVA = 800 / 0.7 × 1.25 = 1,429 kVA
Select: 1500 kVA transformer (next standard size)
```

**Loading Considerations**:
- Continuous load should not exceed **80% of transformer rating** (NEC 450.3 exception allows 100% with proper overcurrent protection)
- Consider harmonic loads (nonlinear loads require derating)
- NEMA TP-1 energy efficiency standards (minimum efficiency)

#### 2.1.3 Insulation Classes and Temperature Rise

**Insulation Classes** (Temperature Ratings):

| Class | Max Winding Temp (°C) | Typical Application |
|-------|----------------------|---------------------|
| **Class 130 (B)** | 130°C | Obsolete |
| **Class 150 (F)** | 150°C | Standard for dry-type |
| **Class 180 (H)** | 180°C | High-temperature, compact designs |
| **Class 220 (N)** | 220°C | Extreme environments |

**Temperature Rise**:
- **80°C rise** (Class 150 insulation): Standard for general-purpose transformers
- **115°C rise** (Class 150 insulation): Compact/economy designs
- **150°C rise** (Class 220 insulation): High-temperature environments

**Total Temperature** = Ambient + Temperature Rise
- Example: 40°C ambient + 80°C rise = 120°C winding temp (within Class 150 limit)

#### 2.1.4 Transformer Construction Types

**Ventilated Dry-Type** (VDT):
- Air-cooled, fan-assisted or natural convection
- NEMA 1 or NEMA 2 enclosures (indoor)
- Most common for commercial/industrial <1000 kVA

**Sealed Dry-Type**:
- Epoxy-encapsulated windings
- NEMA 3R (outdoor) or NEMA 4/4X (corrosive environments)
- Higher cost, better protection

**Cast Coil**:
- Windings encased in epoxy resin (cast)
- Moisture-resistant, fire-resistant
- Higher short-circuit withstand
- Suitable for harsh environments

**Specification Checklist**:
- [ ] Primary voltage / Secondary voltage
- [ ] kVA rating
- [ ] Insulation class and temperature rise
- [ ] Impedance (% Z) - typically 5.5% to 6.5%
- [ ] Taps: ±2 × 2.5% or ±4 × 2.5% (voltage adjustment)
- [ ] NEMA enclosure type (1, 2, 3R, 4, 4X, 12)
- [ ] BIL (Basic Impulse Level) - lightning surge protection
- [ ] Sound rating (dBA) - NEMA ST-20 levels
- [ ] Efficiency (NEMA TP-1 or DOE 2016 standards)
- [ ] Seismic certification (if required by jurisdiction)

#### 2.1.5 K-Factor Transformers (Harmonic Loads)

**K-Factor**: Measure of transformer's ability to handle nonlinear loads without overheating.

| K-Factor | Application | Typical Loads |
|----------|-------------|---------------|
| **K-4** | General commercial | Incandescent, linear loads (legacy) |
| **K-9** | Light computer loads | Desktop computers, small servers |
| **K-13** | Moderate computer loads | Office with 25-50% nonlinear loads |
| **K-20** | Heavy computer loads | Data centers, IT equipment, VFDs |

**When to Specify K-Rated Transformers**:
- Total harmonic distortion (THD) >15%
- Nonlinear load >30% of total load
- Sensitive electronic equipment
- Data centers, server rooms, IT closets

**Alternative**: Oversized standard transformer (derate by 10-20%)

### 2.2 Liquid-Filled Transformers (Oil-Immersed)

**Definition**: Transformers using mineral oil or less-flammable liquid as insulation and cooling medium.

**Insulating Liquids**:
- **Mineral oil**: Most common, lowest cost, flammable (NEC 450.23 restrictions)
- **Less-flammable liquids**: Silicone, high-molecular-weight hydrocarbons, natural esters
  - Higher cost, indoor installation allowed with proper protection

**Advantages**:
- Higher efficiency than dry-type (0.5-1% better)
- Lower cost per kVA (for large transformers >500 kVA)
- Better overload capability
- Longer service life (30-40 years typical)

**Disadvantages**:
- Fire hazard (mineral oil is flammable)
- Environmental concerns (oil spill containment required)
- Maintenance required (oil testing, filtration)
- NEC 450.23 restrictions: Cannot be installed indoors (except sprinklered vault)

**Typical Applications**:
- Outdoor pad-mounted transformers (utility-owned or customer-owned)
- Substation transformers (medium voltage to low voltage step-down)
- Large industrial facilities (>1000 kVA)

**Cooling Classes**:
- **OA (Oil-immersed, Air-cooled)**: Natural convection
- **FA (Forced Air)**: Fan-assisted cooling
- **OA/FA**: Two-stage cooling (natural + fans for overload)

**kVA Ratings**: 75 kVA to 100+ MVA (mega volt-amperes)

**Specification Checklist**:
- [ ] Primary/secondary voltages
- [ ] kVA rating and cooling class (OA, FA, OA/FA)
- [ ] Impedance (% Z)
- [ ] Taps (no-load or load tap changer)
- [ ] Insulating liquid type (mineral oil, silicone, ester)
- [ ] BIL (Basic Impulse Level)
- [ ] Sound rating (dBA)
- [ ] Accessories: Liquid level gauge, pressure relief, Buchholz relay, temperature gauges

---

## 3. PANELBOARDS

### 3.1 Panelboard Definitions and Types

**Panelboard** (NEC Article 408): Single panel or group of panel units designed for assembly in the form of a single panel, including buses and automatic overcurrent devices, for control of light, heat, or power circuits.

#### 3.1.1 Lighting and Appliance Branch Circuit Panelboard (LABCP)

**Definition** (NEC 408.34): Panelboard with >10% of its overcurrent devices rated 30A or less for which neutral connections are provided.

**Typical Application**: Lighting, receptacles, small appliances

**Voltage Ratings**:
- **120/208V** (3-phase, 4-wire)
- **277/480V** (3-phase, 4-wire)
- **120/240V** (single-phase, 3-wire)

**Bus Ratings**:
- 100A, 125A, 150A, 200A, 225A, 400A, 600A

**Circuit Breaker Configurations**:
- 12, 18, 24, 30, 36, 42 circuit positions (standard)
- Branch breakers: 15A, 20A, 30A (most common)

**Main Configurations**:
- **Main Lug Only (MLO)**: No main breaker, fed from upstream overcurrent device
- **Main Circuit Breaker (MCB)**: Integral main breaker for panel isolation and protection

#### 3.1.2 Power Distribution Panelboard

**Definition**: Panelboard with ≤10% of overcurrent devices rated 30A or less.

**Typical Application**: Motor loads, large HVAC equipment, distribution to sub-panels

**Voltage Ratings**:
- **480V** (3-phase, 3-wire or 4-wire)
- **208V** (3-phase, 3-wire or 4-wire)

**Bus Ratings**:
- 100A, 200A, 400A, 600A, 800A, 1200A

**Circuit Breaker Sizes**:
- 60A, 70A, 80A, 100A, 125A, 150A, 200A, 250A, 300A, 400A, 600A (typical)

**Main Configurations**:
- **MLO**: Fed from upstream fused disconnect or circuit breaker
- **MCB**: Integral main breaker (frame sizes 400A-1200A typical)

#### 3.1.3 Panelboard Short-Circuit Ratings

**Available Fault Current (AFC)**: Maximum short-circuit current available at panelboard location (calculated from utility transformer and feeder impedance).

**Short-Circuit Current Rating (SCCR)**: Maximum fault current panelboard can safely withstand (tested per UL 67).

| Panelboard Bus Rating | Typical SCCR (kA RMS) | Application |
|----------------------|----------------------|-------------|
| 100A - 225A | 10 kA, 14 kA, 22 kA | Residential, small commercial |
| 400A | 22 kA, 42 kA, 65 kA | Commercial standard |
| 600A | 42 kA, 65 kA, 100 kA | Large commercial, industrial |

**NEC Requirement**: SCCR must be ≥ available fault current at point of installation (NEC 110.9, 110.24)

**Series Ratings** (NEC 240.86):
- Allows downstream breaker with lower AIC rating if protected by upstream breaker
- Must be tested and listed as series combination
- Not preferred; use fully-rated breakers when possible

#### 3.1.4 Panelboard Construction and Features

**Standard Features**:
- Aluminum or copper bus (copper preferred for high-current panels)
- Neutral bus (isolated or bonded depending on service/feeder)
- Ground bus (bonded to enclosure)
- Circuit directory (typed or handwritten circuit identification)
- NEMA 1 enclosure (indoor, general purpose)

**Common Options**:
- **NEMA 3R enclosure**: Outdoor, rainproof
- **NEMA 12 enclosure**: Indoor, dust-tight
- **Surge protective device (SPD)**: Type 2 SPD per NEC 242.3 (recommended for critical loads)
- **Metering**: Panel-mounted digital meter (voltage, current, kWh)
- **Space for future breakers**: Leave 20-30% spare breaker positions
- **Ground fault protection** (GFCI or GFP)

**Panelboard Schedule Information** (Drawing Requirements):
- Panel designation (e.g., "LP-1", "PP-2")
- Voltage (120/208V, 277/480V)
- Phase (1Ø, 3Ø)
- Bus rating (e.g., 400A)
- Main breaker or MLO (e.g., "400A MCB" or "MLO")
- Short-circuit rating (e.g., "42 kA SCCR")
- Feeder size and source panel
- Circuit-by-circuit listing:
  - Circuit number
  - Breaker size (A)
  - Poles (1P, 2P, 3P)
  - Description / Load served
  - Calculated load (VA or A)

**Sample Panelboard Schedule Entry**:
```
Panel: LP-1
Voltage: 120/208V, 3Ø, 4W
Bus: 225A MLO
SCCR: 22 kA
Fed From: SWBD-1, Breaker #3, 225A, 3P
Feeder: (3) #4/0 AWG, (1) #2 AWG, (1) #6 AWG GND in 3" EMT

Ckt | Breaker | Poles | Description              | Load (VA)
----|---------|-------|--------------------------|----------
1   | 20A     | 1P    | Receptacles - East Wall  | 1800
3   | 20A     | 1P    | Receptacles - West Wall  | 1800
5   | 20A     | 1P    | Lighting - Open Office   | 2400
2   | 20A     | 1P    | Receptacles - North Wall | 1800
4   | 20A     | 1P    | Computer Room Recepts    | 1800
6   | 20A     | 1P    | Lighting - Conference Rm | 1200
```

---

## 4. CIRCUIT BREAKERS

### 4.1 Molded Case Circuit Breakers (MCCB)

**Definition** (NEC Article 100): Circuit breaker enclosed in an insulating housing (molded case).

#### 4.1.1 Frame Sizes and Trip Ratings

**Frame Size**: Physical size and maximum ampere rating of breaker frame.

| Frame Size | Typical Trip Ratings Available | Poles | AIC Ratings (kA) |
|------------|-------------------------------|-------|------------------|
| **100 AF** | 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100 | 1P, 2P, 3P | 10, 14, 18, 22 |
| **225 AF** | 125, 150, 175, 200, 225 | 2P, 3P | 18, 22, 25, 35, 42 |
| **400 AF** | 250, 300, 350, 400 | 2P, 3P | 25, 35, 42, 65 |
| **600 AF** | 400, 500, 600 | 2P, 3P | 35, 42, 65, 100 |
| **800 AF** | 700, 800 | 2P, 3P | 42, 65, 100 |
| **1200 AF** | 1000, 1200 | 3P | 65, 100, 150 |
| **1600 AF** | 1600 | 3P | 65, 100, 150 |
| **2000 AF** | 2000 | 3P | 65, 100, 150, 200 |
| **2500 AF** | 2500 | 3P | 100, 150, 200 |

**Key**: AF = Ampere Frame, AIC = Amperes Interrupting Capacity (short-circuit rating)

**Trip Rating**: Maximum continuous current breaker will carry without tripping.

**Frame vs. Trip Rating**:
- Frame size ≥ trip rating (e.g., 400 AF breaker can have 250A, 300A, 350A, or 400A trip)
- Specifying frame allows future trip rating increase without panel modification

#### 4.1.2 Trip Unit Types

**Thermal-Magnetic Trip**:
- **Thermal element**: Bimetallic strip responds to overload (inverse time delay)
- **Magnetic element**: Solenoid responds to short circuit (instantaneous)
- Standard for branch circuit breakers (15A-100A)
- Fixed trip settings

**Electronic Trip (Solid-State)**:
- Microprocessor-based trip unit
- Adjustable settings: Long-time (overload), short-time, instantaneous, ground fault
- Available on larger breakers (≥400 AF typically)
- LCD display for settings and metering

**Trip Curves**:

| Curve Type | Description | Application |
|-----------|-------------|-------------|
| **B Curve** | 3-5× In magnetic trip | Resistive loads, lighting |
| **C Curve** | 5-10× In magnetic trip | General purpose, inductive loads |
| **D Curve** | 10-20× In magnetic trip | High inrush loads (motors, transformers) |

**Key**: In = Nominal current rating

#### 4.1.3 Ground Fault Protection

**Ground Fault Circuit Interrupter (GFCI)**:
- Detects imbalance between hot and neutral (leakage current)
- Trip threshold: 4-6 mA (Class A) for personnel protection
- Required by NEC for specific locations (bathrooms, kitchens, outdoors, etc.)
- Available in 15A, 20A, 1P and 2P

**Equipment Ground Fault Protection (EGFP)**:
- Detects ground faults on equipment (not personnel protection)
- Trip threshold: Adjustable 50-1200A (typical)
- Required by NEC 230.95 for solidly grounded wye services >150V to ground and >1000A
- Typical settings: 1200A pickup, 0.3 second time delay

**Arc Fault Circuit Interrupter (AFCI)**:
- Detects arc faults (parallel or series arcs)
- Required by NEC 210.12 for dwelling unit branch circuits
- Combination AFCI detects both series and parallel arcs
- Available in 15A, 20A, 1P and 2P

### 4.2 Miniature Circuit Breakers (MCB)

**Definition**: Small, modular circuit breakers for DIN rail mounting (common in industrial control panels).

**Frame Sizes**: 1, 2, 3, 4 poles
**Trip Ratings**: 0.5A to 63A (IEC), up to 100A (UL)
**Trip Curves**: B, C, D (same as MCCB)
**Interrupting Capacity**: 6 kA, 10 kA, 15 kA, 25 kA

**Applications**:
- Control panels
- Industrial machinery
- International projects (IEC standards)

**Difference from MCCB**:
- Smaller physical size
- Lower current ratings
- Modular/snap-in mounting
- Not typically used for building branch circuits in North America

---

## 5. GENERATORS (EMERGENCY AND STANDBY POWER)

### 5.1 Generator Types by Application

#### 5.1.1 Emergency Power Systems (NEC Article 700)

**Definition**: Systems required by code to provide power for life safety (egress lighting, fire alarm, fire pumps).

**Fuel Types**:
- **Diesel**: Most common for large generators (>150 kW), reliable, long run time
- **Natural gas**: Common for standby generators (<500 kW), unlimited run time (utility gas)
- **Propane (LPG)**: Suitable where natural gas unavailable, requires on-site tank

**Generator Sizing**:

```
Generator kW = (Total Connected Load kW) × (Demand Factor) × (Future Factor) / (Power Factor)

Example:
Fire Pump: 75 HP = 75 × 0.746 = 56 kW
Egress Lighting: 10 kW
Fire Alarm: 2 kW
HVAC (required): 20 kW
Total: 88 kW

Demand Factor: 1.0 (all loads simultaneous)
Future: 1.25 (25% spare)
Power Factor: 0.8 (inductive loads)

Generator kW = 88 × 1.0 × 1.25 / 0.8 = 138 kW
Select: 150 kW generator (next standard size)
```

**Standard Generator Sizes** (kW):
- 20, 30, 40, 60, 80, 100, 125, 150, 175, 200, 250, 300, 350, 400, 500, 600, 750, 1000, 1250, 1500, 2000, 2500, 3000

**Voltage Ratings**:
- **120/208V, 3Ø, 4W** (small generators, <100 kW)
- **277/480V, 3Ø, 4W** (most common industrial/commercial, 100-2000 kW)
- **12.47 kV or 13.8 kV, 3Ø** (large generators, >2 MVA)

**Transfer Switch Types**:
- **Automatic Transfer Switch (ATS)**: Senses utility failure, starts generator, transfers load
  - Transfer time: <10 seconds (NEC 700.12)
  - Closed-transition (momentary parallel) or open-transition
- **Manual Transfer Switch**: Manually operated (not permitted for emergency systems per NEC 700)

**Generator Features**:
- Automatic start/stop (utility fail detection)
- Battery charger for starting batteries
- Fuel tank (on-board or day tank + bulk storage)
- Outdoor sound-attenuated enclosure or indoor installation
- Exhaust system (critical silencer for indoor)
- Cooling system (radiator or heat exchanger)

#### 5.1.2 Legally Required Standby Systems (NEC Article 701)

**Definition**: Systems required by code for orderly shutdown or safety (HVAC smoke control, elevators).

**Similar to Emergency Systems**:
- Automatic transfer switch required
- Transfer time: <60 seconds (more lenient than emergency)

**Typical Loads**:
- HVAC smoke control systems
- Elevator emergency power (one elevator required per NEC 700.12)
- Fire pumps (if not on emergency system)

#### 5.1.3 Optional Standby Systems (NEC Article 702)

**Definition**: Systems installed to provide backup power for convenience or business continuity (not required by code).

**Typical Loads**:
- Data centers (uninterruptible operation)
- Healthcare (beyond code-required emergency loads)
- Manufacturing (process continuity)
- Commercial buildings (tenant operations)

**Transfer Switch Options**:
- Automatic transfer switch (ATS) - most common
- Manual transfer switch - permissible for optional standby
- Soft-load transfer switch - for sensitive electronic loads

### 5.2 Generator Specifications Checklist

- [ ] Application: Emergency (NEC 700), Legally Required Standby (NEC 701), Optional Standby (NEC 702)
- [ ] Fuel type: Diesel, natural gas, propane
- [ ] Generator rating: kW at 0.8 PF (or kVA)
- [ ] Voltage: 120/208V, 277/480V, 12.47 kV, etc.
- [ ] Frequency: 60 Hz (50 Hz for international)
- [ ] Enclosure: Outdoor weather-protective, indoor open/enclosed
- [ ] Sound attenuation: dBA at 7m (23 ft) - typically 65-75 dBA
- [ ] Fuel tank capacity: Hours of run time at full load
- [ ] ATS: Automatic transfer switch rating (matching or exceeding generator output)
- [ ] Accessories: Remote monitoring, paralleling switchgear (multiple generators)

---

## 6. UNINTERRUPTIBLE POWER SUPPLY (UPS) SYSTEMS

### 6.1 UPS Topologies

#### 6.1.1 Standby (Offline) UPS

**Operation**:
- Normal: Utility power passes through to load (bypass mode)
- Failure: Battery inverter activates and supplies load
- Transfer time: 4-10 ms (acceptable for most IT equipment)

**Applications**: Desktop computers, workstations, small servers
**Sizes**: 300 VA to 2 kVA
**Advantages**: Low cost, high efficiency (98-99% in bypass)
**Disadvantages**: No power conditioning, brief transfer time interruption

#### 6.1.2 Line-Interactive UPS

**Operation**:
- Normal: Utility power passes through with voltage regulation (buck/boost transformer)
- Failure: Battery inverter supplies load
- Transfer time: 2-4 ms

**Applications**: Servers, network equipment, telecom
**Sizes**: 500 VA to 5 kVA (single-phase)
**Advantages**: Voltage regulation, lower cost than online
**Disadvantages**: Brief transfer time, limited power conditioning

#### 6.1.3 Double-Conversion Online UPS

**Operation**:
- Normal: Utility power → Rectifier (AC to DC) → Inverter (DC to AC) → Load
- Failure: Battery supplies DC bus, inverter continues supplying load
- Transfer time: 0 ms (no transfer, seamless)

**Applications**: Data centers, critical servers, medical equipment, industrial controls
**Sizes**: 1 kVA to 2+ MVA (parallel configurations)
**Advantages**: Zero transfer time, complete power conditioning (voltage, frequency, harmonics), isolation from utility disturbances
**Disadvantages**: Higher cost, lower efficiency (92-96%, recent models up to 98%)

**Efficiency Modes**:
- **ECO mode**: Bypass during normal operation, online mode on utility disturbance
- **VFI mode** (Voltage and Frequency Independent): True double-conversion (IEC 62040-3 VFI-SS-111)

### 6.2 UPS Sizing and Runtime

**Sizing Calculation**:

```
UPS kVA = (Connected IT Load kW) / (Load Power Factor) × (Future Factor)

Example:
IT Load: 30 kW
Load PF: 0.9 (typical for servers with active PFC)
Future: 1.2 (20% growth)

UPS kVA = 30 / 0.9 × 1.2 = 40 kVA
Select: 40 kVA or 50 kVA UPS
```

**Runtime Calculation**:
- Depends on battery capacity (Ah) and load (kW)
- Typical runtimes:
  - 5-10 minutes: Ride-through short outages, graceful shutdown
  - 15-30 minutes: Extended shutdown time, critical process completion
  - >1 hour: Generator start and stabilization, long-duration support

**Battery Types**:
- **VRLA (Valve-Regulated Lead-Acid)**: Most common, 3-5 year life, maintenance-free
- **Lithium-Ion**: Longer life (8-10 years), smaller footprint, higher cost

### 6.3 UPS Features and Options

**Standard Features**:
- Automatic bypass (utility restoration or UPS fault)
- Battery monitoring and charging
- LCD display (load, battery, alarms)
- Communications: USB, serial RS-232, SNMP network card

**Common Options**:
- **Redundancy configurations**:
  - **N+1**: N units required for load, +1 for redundancy
  - **2N**: Full system redundancy (two independent UPS systems)
- **Maintenance bypass**: Manual bypass switch for UPS service without load interruption
- **External battery cabinets**: Extended runtime
- **Parallel operation**: Multiple UPS units for increased capacity and redundancy
- **Transformer**: Input/output isolation, step-up/step-down voltage

---

## 7. PROTECTIVE DEVICES AND SAFETY EQUIPMENT

### 7.1 Surge Protective Devices (SPD)

**Definition** (NEC Article 285): Device to limit transient overvoltages and divert surge currents.

**Types**:
- **Type 1 SPD** (Service entrance): Installed at main service equipment or line side of service disconnect
  - Highest surge current rating (100-400 kA per phase)
  - Required for critical facilities
- **Type 2 SPD** (Load side): Installed on load side of service disconnect (panelboards, switchboards)
  - Typical surge current: 50-100 kA per phase
  - Most common for commercial/industrial
- **Type 3 SPD** (Point-of-use): Plug-in or receptacle-mounted
  - Lowest surge rating (10-20 kA)
  - Supplemental protection for sensitive equipment

**Voltage Protection Rating (VPR)**:
- Maximum voltage let-through during surge
- Typical VPR: 600-1200V for 120V circuits, 1500-3000V for 277/480V

**Applications**:
- Service entrance (Type 1)
- Distribution panelboards (Type 2)
- IT equipment, data centers (Type 3)

### 7.2 Arc-Flash Protection

**Arc-Flash Hazard** (NFPA 70E): Dangerous release of energy from electrical arc fault.

**Mitigation Methods**:
1. **Proper PPE (Personal Protective Equipment)**: Based on arc-flash hazard analysis
2. **Current-Limiting Devices**: Fuses, current-limiting circuit breakers
3. **Zone-Selective Interlocking (ZSI)**: Coordinates breakers to trip only faulted zone (reduces clearing time and incident energy)
4. **Arc-Flash Relays**: Detect light and current, trip breaker <2 cycles (0.033 seconds)
5. **Remote Racking/Operation**: Operate switchgear remotely (personnel outside arc-flash boundary)

**Arc-Flash Labels** (NFPA 70E 130.5):
- Required on equipment >50V
- Shows: Arc-flash boundary, incident energy (cal/cm²), PPE category

---

## 8. BUSWAY (BUS DUCT)

**Definition**: Prefabricated electrical distribution system using aluminum or copper busbars in a protective enclosure.

### 8.1 Busway Types

**Feeder Busway**:
- High-current distribution (200A to 6000A)
- Lower cost per ampere than cable for large feeders
- Applications: Riser distribution in high-rises, heavy industrial

**Plug-In Busway**:
- Allows plug-in circuit breakers at any point along busway
- Ratings: 100A to 1000A (continuous)
- Applications: Manufacturing (flexible tool connections), data centers

**Lighting Busway**:
- Low-current (20A, 30A, 60A) with track-mounted lighting fixtures
- Commercial and industrial lighting

### 8.2 Busway Advantages

- **High current capacity**: More compact than equivalent cable
- **Flexibility**: Easy to relocate or add tap-offs
- **Lower voltage drop**: Larger conductor area
- **Ease of installation**: Pre-fabricated, modular sections

**Disadvantages**:
- Higher initial cost (vs. cable for smaller sizes)
- Requires adequate vertical/horizontal space
- Limited availability in some regions

---

## 9. INTEGRATION WITH MEP QA VALIDATION

### 9.1 Equipment Schedule Validation Rules

**Switchgear Schedule Checks**:
```python
def validate_switchgear(bus_rating, sccr, afc, voltage):
    # Short-circuit rating must exceed available fault current
    if sccr < afc:
        return f"FAIL: SCCR {sccr} kA < AFC {afc} kA (NEC 110.9)"

    # Verify voltage matches system
    if voltage not in ["208V", "480V", "600V"]:
        return f"WARN: Unusual voltage {voltage} for switchgear"

    # Bus rating should accommodate future growth
    if bus_rating < 1.25 × calculated_load:
        return "WARN: Bus rating <125% of calculated load (recommend 25% spare)"

    return "PASS"
```

**Transformer Schedule Checks**:
```python
def validate_transformer(kva_rating, load_kva, temp_rise, insulation_class):
    # Loading check
    if load_kva > 0.8 × kva_rating:
        return "WARN: Load >80% of transformer rating (consider next size)"

    # Insulation class vs. temperature rise
    if insulation_class == 150 and temp_rise > 150:
        return f"FAIL: {temp_rise}°C rise exceeds Class {insulation_class} limit"

    # Efficiency standard
    if not meets_nema_tp1_efficiency(kva_rating):
        return "WARN: Transformer may not meet NEMA TP-1 efficiency standards"

    return "PASS"
```

**Panelboard Schedule Checks**:
```python
def validate_panelboard(bus_rating, main_breaker, sccr, afc, circuits):
    # Main breaker ≤ bus rating
    if main_breaker > bus_rating:
        return f"FAIL: Main breaker {main_breaker}A > bus rating {bus_rating}A"

    # SCCR ≥ AFC
    if sccr < afc:
        return f"FAIL: SCCR {sccr} kA < AFC {afc} kA (NEC 110.9)"

    # Check for spare capacity (20% minimum)
    total_circuits = len(circuits)
    spare_circuits = sum(1 for c in circuits if c.description == "SPARE")
    spare_ratio = spare_circuits / total_circuits

    if spare_ratio < 0.2:
        return f"WARN: Spare circuits {spare_ratio*100:.0f}% < 20% recommended"

    # Verify all branch breaker ratings ≤ bus rating
    for circuit in circuits:
        if circuit.breaker_rating > bus_rating:
            return f"FAIL: Breaker {circuit.breaker_rating}A > bus {bus_rating}A"

    return "PASS"
```

**Generator Schedule Checks**:
```python
def validate_generator(rating_kw, total_load_kw, fuel_type, nec_article):
    # Sizing check (125% of load minimum)
    if rating_kw < 1.25 × total_load_kw:
        return f"WARN: Generator {rating_kw} kW < 125% of load {total_load_kw} kW"

    # Transfer time for emergency systems
    if nec_article == "700" and transfer_time > 10:
        return f"FAIL: Transfer time {transfer_time}s > 10s for NEC 700 (emergency)"

    # Fuel type considerations
    if fuel_type == "Natural Gas" and nec_article == "700":
        return "WARN: Natural gas relies on utility (ensure gas supply reliability for emergency)"

    return "PASS"
```

### 9.2 Equipment Nameplate Data Validation

**Required Nameplate Information** (NEC 110.21):
- Manufacturer name
- Model/catalog number
- Voltage rating(s)
- Current/kVA/kW rating
- Short-circuit rating (SCCR or AIC)
- Serial number
- UL or ETL listing mark

**Drawing Schedule Cross-Check**:
- Equipment schedules on drawings must match specified equipment nameplates
- Verify cut sheet data matches schedule data during submittal review

---

## 10. RESOURCES AND STANDARDS

### 10.1 Manufacturer Resources

- **Eaton**: https://www.eaton.com/us/en-us/products/electrical-circuit-protection.html
- **Schneider Electric**: https://www.se.com/us/en/
- **ABB**: https://new.abb.com/low-voltage
- **Siemens**: https://new.siemens.com/us/en/products/energy/low-voltage.html
- **GE Industrial Solutions**: https://www.geindustrial.com/

### 10.2 Standards Organizations

- **NEMA**: https://www.nema.org/ (equipment standards)
- **UL**: https://www.ul.com/ (safety certification)
- **IEEE**: https://www.ieee.org/ (electrical engineering standards)
- **NFPA**: https://www.nfpa.org/ (NEC, NFPA 70E)

### 10.3 Key Standards Referenced

- **NEC 2023 (NFPA 70)**: National Electrical Code
- **NEMA 250**: Enclosures for Electrical Equipment
- **UL 67**: Panelboards
- **UL 891**: Switchboards and Switchgear
- **UL 1449**: Surge Protective Devices
- **UL 1008**: Automatic Transfer Switches
- **IEEE C37.20.7**: Arc-Resistant Switchgear
- **NEMA TP-1**: Efficiency Standards for Dry-Type Transformers

---

## 11. DOCUMENT CONTROL

**Version**: 1.0
**Effective Date**: 2025-10-22
**Author**: Agent 4 - Equipment Specification Specialist
**Review Cycle**: Annual or upon major standard updates

**Paraphrasing Notice**: All content paraphrased from publicly available manufacturer catalogs and industry standards. No verbatim reproduction. Users should consult manufacturer technical data and official standards for detailed specifications.

**Integration Note**: This document supports the MEP Drawing QA/QC workflow defined in `skills/engineering-drawing-qaqc/SKILL.md`. Equipment specifications inform schedule validation rules for electrical drawings.

---

**End of Document**
