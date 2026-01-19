# NFPA Life Safety Code Overview

**Document Purpose**: Comprehensive reference for NFPA life safety requirements in MEP fire alarm and sprinkler system design and QA validation

**Last Updated**: 2025-10-22

**Sources**:
- NFPA 101 Life Safety Code (2024 Edition - publicly available information)
- NFPA 13 Installation of Sprinkler Systems (2022 Edition - publicly available information)
- NFPA 72 National Fire Alarm and Signaling Code (2022 Edition - publicly available information)
- NFPA 70 National Electrical Code (2023 Edition - NEC)
- International Building Code (IBC 2021) - fire/life safety chapters

---

## 1. OCCUPANCY CLASSIFICATIONS

### 1.1 NFPA 101 Occupancy Types

NFPA 101 classifies buildings by occupancy type based on the characteristics of the occupants and the activities conducted. Each occupancy has unique egress, fire protection, and life safety requirements.

#### 1.1.1 Primary Occupancy Classifications

| Occupancy Code | Occupancy Name | Description | Typical Examples |
|---------------|---------------|-------------|-----------------|
| **Assembly** | Assembly Occupancies | Gatherings of people for civic, social, religious, or entertainment purposes | |
| A-1 | Assembly - Fixed Seating | Venues with fixed seating for viewing performances | Theaters, auditoriums, cinemas |
| A-2 | Assembly - Food/Drink | Facilities serving food and/or drink | Restaurants, bars, nightclubs, cafeterias |
| A-3 | Assembly - Worship/Recreation | Religious, recreational, or amusement uses | Churches, libraries, museums, bowling alleys, arcades |
| A-4 | Assembly - Indoor Sport | Indoor sports events and activities | Arenas, swimming pools, skating rinks |
| A-5 | Assembly - Outdoor | Outdoor venues with seating | Stadiums, grandstands, amusement parks |
| **Business** | Business Occupancies | Professional or business services | |
| B | Business | Office, professional services, educational above 12th grade | Office buildings, banks, city halls, college classrooms |
| **Educational** | Educational Occupancies | Educational purposes through 12th grade | |
| E | Educational | Schools, daycare (6+ people, 4+ hours/day) | Elementary schools, high schools, daycare centers |
| **Healthcare** | Healthcare Occupancies | Medical care for persons incapable of self-preservation | |
| I-1 | Healthcare - Ambulatory | Residential care (>16 people), ambulatory residents | Assisted living, group homes, halfway houses |
| I-2 | Healthcare - Non-Ambulatory | Medical care, non-ambulatory patients | Hospitals, nursing homes, psychiatric facilities |
| **Detention/Correctional** | Detention Occupancies | Housing persons under restraint or security | |
| I-3 | Detention/Correctional | Jails, prisons, detention centers | Correctional facilities, holding cells |
| I-4 | Daycare | Daycare facilities (≥5 people, <24 hour care) | Adult daycare, childcare centers |
| **Residential** | Residential Occupancies | Sleeping accommodations | |
| R-1 | Residential - Transient | Transient lodging (≤16 people) | Hotels, motels, bed & breakfasts |
| R-2 | Residential - Multi-Family | Multi-family dwellings | Apartments, condominiums, dormitories |
| R-3 | Residential - One/Two Family | One and two family dwellings | Single-family homes, townhouses |
| R-4 | Residential - Assisted Living | Residential care (5-16 people) | Small assisted living, group homes |
| **Mercantile** | Mercantile Occupancies | Display and sale of merchandise | |
| M | Mercantile | Retail sales | Stores, shopping malls, markets |
| **Industrial** | Industrial Occupancies | Manufacturing, processing, assembly, repair | |
| I | Industrial | Factories, manufacturing plants | Industrial buildings, workshops, power plants |
| **Storage** | Storage Occupancies | Storage of goods, merchandise, vehicles | |
| S-1 | Storage - Moderate Hazard | Storage of moderate combustibility materials | Warehouses, freight depots, parking garages |
| S-2 | Storage - Low Hazard | Storage of non-combustible materials | Cold storage, open parking structures |

#### 1.1.2 Mixed Occupancies

**Separation Requirements**:
When a building contains multiple occupancy types, NFPA 101 requires either:

1. **Complete Separation** (Separated Occupancies):
   - Fire barrier with appropriate hourly rating between occupancies
   - Each occupancy meets its own life safety requirements independently

2. **Non-Separated** (Multiple Occupancies):
   - Most restrictive requirements of all occupancies apply to entire building
   - No separation barriers required

**Example Fire Barrier Ratings** (NFPA 101 Table 6.1.14.4.1(b)):

| Occupancy A | Occupancy B | Minimum Fire Resistance Rating (hours) |
|-------------|-------------|---------------------------------------|
| Healthcare (I-2) | Any other | 2-hour |
| Detention (I-3) | Any other | 2-hour |
| Assembly (A) | Business (B) | 1-hour |
| Residential (R) | Business (B) | 1-hour |
| Storage (S) | Business (B) | 1-hour |

### 1.2 Occupant Load Calculation

Occupant load determines required egress capacity, alarm notification, and sprinkler design areas. NFPA 101 provides occupant load factors by use.

#### 1.2.1 Occupant Load Factors (NFPA 101 Table 7.3.1.2)

| Use | Occupant Load Factor (ft²/person) |
|-----|----------------------------------|
| **Assembly Uses** | |
| Assembly - concentrated seating (auditoriums) | 7 net |
| Assembly - standing space | 5 net |
| Assembly - unconcentrated (museums, galleries) | 15 net |
| Assembly - Fixed seating | Number of fixed seats |
| Stages | 15 net |
| **Business Uses** | |
| Business areas | 100 gross |
| **Educational Uses** | |
| Classrooms | 20 net |
| Laboratories (classrooms) | 50 net |
| Shops, vocational rooms | 50 net |
| **Healthcare Uses** | |
| Inpatient treatment areas | 240 gross |
| Sleeping areas | 120 gross |
| **Industrial Uses** | |
| General industrial areas | 100 gross |
| **Mercantile Uses** | |
| Sales area (street floor/basement) | 30 gross |
| Sales area (upper floors) | 60 gross |
| Storage, shipping areas | 300 gross |
| **Residential Uses** | |
| Hotels, apartments | 200 gross |
| **Storage Uses** | |
| Storage areas | 500 gross |

**Key**:
- **Gross**: Entire floor area
- **Net**: Actual occupied area (excluding corridors, restrooms, mechanical rooms)

**Calculation Example**:
```
Office building: 10,000 ft² gross floor area
Business occupant load factor: 100 ft²/person
Occupant load = 10,000 / 100 = 100 persons
```

---

## 2. MEANS OF EGRESS REQUIREMENTS

### 2.1 Three Components of Means of Egress

NFPA 101 divides means of egress into three distinct components:

1. **Exit Access**: Path from any point in a building to an exit (corridors, aisles, rooms)
2. **Exit**: Protected path from exit access to exit discharge (stairs, exit passageways, horizontal exits)
3. **Exit Discharge**: Path from exit termination to public way (exterior doors, vestibules, ground level)

### 2.2 Number and Capacity of Exits

#### 2.2.1 Minimum Number of Exits (NFPA 101 Section 7.4)

| Occupant Load | Minimum Number of Exits |
|---------------|------------------------|
| 1-500 | 2 |
| 501-1,000 | 3 |
| >1,000 | 4 |

**Exceptions**:
- Occupant load ≤50 may have 1 exit if travel distance limitations met
- Certain low-occupancy spaces (storage, utility) may have 1 exit

#### 2.2.2 Exit Capacity (NFPA 101 Table 7.3.3.1)

**Capacity Factors**:

| Egress Component | Width per Person (inches) | Flow per Person (in²/person) |
|-----------------|---------------------------|------------------------------|
| **Doors** | | |
| Level exit discharge | 0.15 | N/A |
| Stairs/ramps | 0.20 | N/A |
| **Corridors/Aisles** | | |
| Level exit discharge | N/A | 0.15 |
| Stairs/ramps | N/A | 0.20 |
| **Stairs** | | |
| Level components | 0.15 | N/A |
| Riser components | 0.20 | N/A |

**Calculation Example**:
```
Occupant load: 200 persons
Exit through stair: Width = 200 persons × 0.20 in/person = 40 inches minimum
Doors at grade: Width = 200 persons × 0.15 in/person = 30 inches minimum
```

**Minimum Clear Width**:
- Doors: 32 inches clear (leaf width ≥34 inches)
- Corridors: 36 inches (44 inches for healthcare)
- Stairs: 36 inches (44 inches for new stairs serving occupant load >50)

### 2.3 Travel Distance Limitations

#### 2.3.1 Maximum Travel Distances (NFPA 101 - varies by occupancy)

**Unsprinklered Buildings**:

| Occupancy | Maximum Travel Distance to Exit |
|-----------|-------------------------------|
| Assembly (A) | 200 ft |
| Business (B) | 200 ft |
| Educational (E) | 200 ft |
| Healthcare (I-2) | 150 ft |
| Residential (R-1, R-2) | 200 ft |
| Mercantile (M) | 200 ft |
| Industrial (I) | 200 ft |
| Storage (S) | 200-400 ft (varies by hazard) |

**Sprinklered Buildings** (NFPA 13 system):

| Occupancy | Maximum Travel Distance to Exit |
|-----------|-------------------------------|
| Assembly (A) | 250 ft |
| Business (B) | 300 ft |
| Educational (E) | 250 ft |
| Healthcare (I-2) | 200 ft |
| Residential (R-1, R-2) | 250 ft |
| Mercantile (M) | 250 ft |
| Industrial (I) | 250 ft |
| Storage (S) | 300-400 ft (varies by hazard) |

**Common Path of Egress Travel**:
- Maximum distance before two separate exit paths available
- Typically 75-100 ft (varies by occupancy and sprinkler protection)

### 2.4 Exit Arrangement and Separation

**Remote Separation** (NFPA 101 Section 7.5.1.3):
- Exits must be separated by minimum 1/3 diagonal of building area
- Ensures exits not blocked by single fire event

**Calculation**:
```
Building: 100 ft × 150 ft
Diagonal = √(100² + 150²) = 180 ft
Minimum exit separation = 180 / 3 = 60 ft
```

**Exit Discharge**:
- At least 50% of exits must discharge directly to exterior at grade (unsprinklered)
- Up to 50% may exit through exit passageways or protected lobbies (sprinklered buildings)

### 2.5 Corridor Fire Resistance

#### 2.5.1 Corridor Ratings by Occupancy (NFPA 101)

| Occupancy | Sprinkler Status | Minimum Corridor Rating |
|-----------|------------------|------------------------|
| Assembly (A) | Unsprinklered | 1-hour |
| Assembly (A) | Sprinklered | 0-hour (no rating) |
| Business (B) | Unsprinklered | 1-hour |
| Business (B) | Sprinklered | 0-hour |
| Educational (E) | Unsprinklered | 1-hour |
| Educational (E) | Sprinklered | 0-hour |
| Healthcare (I-2) | Any | 1-hour (smoke-resistant) |
| Residential (R-1, R-2) | Unsprinklered | 1-hour |
| Residential (R-1, R-2) | Sprinklered | 0.5-hour |

**Smoke Barriers**:
- Healthcare occupancies require smoke barriers dividing building into smoke compartments
- Maximum 22,500 ft² per smoke compartment
- Maximum 200 ft travel to smoke barrier door

---

## 3. FIRE RESISTANCE RATINGS

### 3.1 Construction Types and Fire Resistance

NFPA 101 references IBC construction types for structural fire resistance. Fire resistance affects egress, compartmentation, and sprinkler requirements.

#### 3.1.1 IBC Construction Types

| Type | Description | Structural Frame | Bearing Walls (Exterior) | Nonbearing Walls (Exterior) | Floor Construction | Roof Construction |
|------|-------------|------------------|--------------------------|----------------------------|-------------------|------------------|
| **Type I-A** | Fire-resistive (most protected) | 3-hour | 3-hour | See Table 602 | 2-hour | 1.5-hour |
| **Type I-B** | Fire-resistive | 2-hour | 2-hour | See Table 602 | 2-hour | 1-hour |
| **Type II-A** | Non-combustible protected | 1-hour | 1-hour | See Table 602 | 1-hour | 1-hour |
| **Type II-B** | Non-combustible unprotected | 0-hour | 0-hour | See Table 602 | 0-hour | 0-hour |
| **Type III-A** | Ordinary protected | 1-hour | 2-hour | See Table 602 | 1-hour | 1-hour |
| **Type III-B** | Ordinary unprotected | 0-hour | 2-hour | See Table 602 | 0-hour | 0-hour |
| **Type IV-HT** | Heavy timber | 1-hour HT | 2-hour | See Table 602 | HT | HT |
| **Type V-A** | Wood frame protected | 1-hour | 1-hour | See Table 602 | 1-hour | 1-hour |
| **Type V-B** | Wood frame unprotected | 0-hour | 0-hour | See Table 602 | 0-hour | 0-hour |

**Key**: HT = Heavy Timber (min 8" × 8" columns, 6" × 10" beams, 2" decking)

#### 3.1.2 Fire Barrier Assemblies

Common fire-rated assemblies used in MEP penetrations:

| Assembly Type | Typical Rating | Common Applications |
|--------------|---------------|---------------------|
| **Fire Walls** | 2-4 hour | Property line separation, major fire separations |
| **Fire Barriers** | 1-3 hour | Occupancy separations, exit enclosures, shaft walls |
| **Fire Partitions** | 1-hour | Corridor walls, dwelling unit separations |
| **Smoke Barriers** | 1-hour + smoke tight | Healthcare smoke compartments |
| **Smoke Partitions** | 0.5-hour + smoke tight | Corridor walls in sprinklered buildings |

### 3.2 Penetrations and Firestopping

All MEP penetrations through fire-rated assemblies must maintain the fire resistance rating using approved firestopping systems.

#### 3.2.1 Through-Penetrations (IBC 714.3, NFPA 101 Section 8.3.5)

**Requirements**:
- Through-penetration firestop system must be tested per **ASTM E814** or **UL 1479**
- F-rating (time to flame passage) ≥ fire resistance rating of assembly
- T-rating (temperature rise limit) may be required for certain locations

**MEP Penetrations Requiring Firestopping**:
- Electrical conduit, cable trays, busway
- HVAC ducts (see fire damper requirements)
- Plumbing pipes (supply, waste, vent)
- Fire protection piping (sprinkler, standpipe)
- Communication/data cable bundles
- Insulated pipes

**Firestop System Selection**:
- Must be UL Listed or approved agency tested system
- UL Firestop Systems Directory provides system numbers (e.g., "C-AJ-1234")
- System must match:
  - Assembly type (concrete, gypsum, CMU, etc.)
  - Penetrating item size and type
  - Required hourly rating

#### 3.2.2 Membrane Penetrations (IBC 714.4)

**Ceiling Membrane Penetrations**:
- Penetrations through ceiling of fire-rated floor/roof assembly
- Sprinkler heads, lighting fixtures, HVAC diffusers, speakers
- Must be protected by:
  - Membrane penetration firestop system (ASTM E814), OR
  - Ceiling radiation damper (for HVAC), OR
  - Listed penetrating item (e.g., recessed light rated for membrane penetration)

### 3.3 Fire Dampers and Smoke Dampers

#### 3.3.1 Fire Dampers (NFPA 80 Section 5.2, IBC 717.3)

**Where Required**:
- Ducts penetrating fire walls (2-3-4 hour rated walls)
- Ducts penetrating fire barriers (1-3 hour occupancy separations, shaft walls)
- Ducts penetrating fire partitions (1-hour corridor walls - where required by code)
- Horizontal assemblies (floors, roofs) - where penetrating duct >100 ft²

**Types**:
1. **Static Fire Damper**: Curtain-type, fusible link (165°F or 286°F), no airflow when closed
2. **Dynamic Fire Damper**: Can close against airflow, UL 555 leakage rating

**Ratings**:
- Fire damper rating = fire resistance rating of penetrated assembly
- 1.5-hour damper for 3-hour walls
- 1.5-hour damper for 2-hour floors
- 0.75-hour damper for 1-hour assemblies

**Access**:
- Minimum 12" × 12" access door/panel required within 10 ft of damper
- Permanent access for inspection and testing

#### 3.3.2 Smoke Dampers (NFPA 90A Section 5.3, IBC 717.4)

**Where Required**:
- Ducts penetrating smoke barriers (healthcare, covered malls, atriums)
- Ducts penetrating smoke partitions (certain corridor walls)
- Return/exhaust air intakes in smoke control systems

**Types**:
1. **Smoke Damper**: Electrically operated, closes on smoke detection signal
2. **Combination Fire/Smoke Damper**: Meets both UL 555 and UL 555S
   - Closes on fusible link (fire) OR smoke detector signal (smoke)

**Leakage Ratings (UL 555S)**:
- Class I: 4 cfm/ft²
- Class II: 10 cfm/ft²
- Class III: 20 cfm/ft²

**Control**:
- Smoke detector at damper location (duct-mounted or area)
- Tied to fire alarm system
- Fail-safe closed on power loss

---

## 4. FIRE ALARM SYSTEM REQUIREMENTS (NFPA 72)

### 4.1 When Fire Alarm Systems Are Required

NFPA 101 mandates fire alarm systems based on occupancy type, building size, and occupant characteristics.

#### 4.1.1 Fire Alarm Requirements by Occupancy

| Occupancy | Fire Alarm Required When... |
|-----------|---------------------------|
| **Assembly (A)** | Occupant load ≥300, OR building >two stories |
| **Business (B)** | Occupant load ≥500, OR building >three stories, OR high-rise |
| **Educational (E)** | Always required (all educational occupancies) |
| **Healthcare (I-2)** | Always required (all healthcare occupancies) |
| **Detention (I-3)** | Always required (all detention/correctional facilities) |
| **Residential (R-1)** | Always required (hotels, motels, boarding houses) |
| **Residential (R-2)** | Building >three stories, OR >16 dwelling units |
| **Mercantile (M)** | Occupant load ≥500, OR building >two stories with occupant load ≥100 above/below discharge |
| **Storage (S)** | High-rise only (typically) |

**High-Rise**: Building with occupied floor >75 ft above lowest level of fire department vehicle access

### 4.2 Fire Alarm System Components

#### 4.2.1 Initiating Devices (NFPA 72 Chapter 17)

**Manual Pull Stations**:
- Required at each exit and exit discharge
- Maximum 200 ft travel distance to nearest pull station
- Located 42-48 inches above finished floor (AFF)
- Red, labeled "FIRE ALARM"

**Automatic Detection Devices**:

| Device Type | Application | Coverage Area |
|------------|-------------|--------------|
| **Smoke Detector - Photoelectric** | General areas, corridors, rooms | 900 ft² (30 ft spacing, smooth ceiling) |
| **Smoke Detector - Ionization** | High air velocity areas | 900 ft² |
| **Smoke Detector - Beam** | Large open areas, atriums, warehouses | Per manufacturer (up to 100 ft beam length) |
| **Heat Detector - Fixed Temperature** | Mechanical rooms, kitchens, dusty areas | Varies by temperature rating |
| **Heat Detector - Rate-of-Rise** | Same as fixed temp, faster response | Varies |
| **Duct Smoke Detector** | HVAC duct smoke detection | Per duct size (NFPA 90A) |

**Smoke Detector Spacing Modifiers** (NFPA 72 Table 17.7.3.2.3.1):

| Ceiling Height | Spacing Multiplier |
|---------------|-------------------|
| 0-10 ft | 1.0 |
| 10-15 ft | 0.9 |
| 15-20 ft | 0.85 |
| 20-30 ft | 0.7 |

**Duct Smoke Detectors** (NFPA 90A):
- Required for HVAC systems >2,000 cfm
- Located in supply air downstream of filters
- Located in return air upstream of any recirculation/fresh air mixing (if >15,000 cfm)
- Shuts down air handling unit upon smoke detection

**Sprinkler Waterflow Switches**:
- Required on all sprinkler systems per NFPA 13
- Initiates fire alarm within 5-90 seconds of water flow
- Bypass/test valves provided for maintenance

**Sprinkler Valve Tamper Switches**:
- Required on all sprinkler control valves per NFPA 13
- Initiates supervisory signal when valve moved from normal position

#### 4.2.2 Notification Appliances (NFPA 72 Chapter 18)

**Audible Notification**:
- **Minimum Sound Level**: 15 dBA above ambient, OR 5 dBA above maximum 60-second sound
- **Public Mode**: Minimum 75 dBA @ 10 ft in corridors, 70 dBA in rooms
- **Private Mode**: Lower levels permitted (occupants trained)
- **Maximum**: 110 dBA at minimum hearing distance from device

**Audible Device Spacing**:
- Corridor: Typically 100-130 ft spacing (horn/speaker)
- Rooms: Coverage depends on dBA output and ambient sound
- Use manufacturer polar plots for spacing calculations

**Visible Notification** (Strobes):
- Required per **ADA/ABA Accessibility Guidelines**
- All public and common-use areas
- Minimum 75 cd effective intensity (small rooms)
- Spacing per NFPA 72 Table 18.5.5.4.1(a) and (b)

**Strobe Spacing Example** (Room <20 ft × 20 ft):

| Minimum Candela | Maximum Room Size (ft) |
|----------------|----------------------|
| 15 cd | 20 × 20 |
| 30 cd | 28 × 28 |
| 60 cd | 40 × 40 |
| 75 cd | 45 × 45 |
| 94 cd | 50 × 50 |
| 110 cd | 54 × 54 |
| 177 cd | 68 × 68 |

**Synchronization**:
- Strobes must be synchronized within 10 ms (NFPA 72 Section 18.5.5.5)
- Prevents disorientation from unsynchronized flashing

**Voice Evacuation Systems** (NFPA 72 Chapter 24):
- Required for high-rise buildings, large assembly occupancies
- Intelligibility: Minimum 0.5 Speech Transmission Index (STI) or 0.65 Common Intelligibility Scale (CIS)
- Paging/background music integration common
- Emergency voice/alarm communications (EVAC) functionality

#### 4.2.3 Fire Alarm Control Panel (FACP)

**Location Requirements**:
- Accessible to fire department (within 10 ft of main entrance, or in fire command center)
- Room ambient temperature: 32-120°F
- Room humidity: 0-93% RH non-condensing

**Power Requirements** (NFPA 72 Chapter 10):
- **Primary Power**: Dedicated branch circuit from building electrical system
  - 120VAC or 277VAC (depending on panel)
  - Supervised (power fail trouble)
  - Identified: "FIRE ALARM"
- **Secondary Power**: Battery backup
  - 24-hour standby capacity
  - Plus 5 minutes full alarm (notification appliances)
  - Or 15 minutes alarm (if evacuation signal required)

**System Supervision**:
All initiating device circuits (IDC), notification appliance circuits (NAC), and signaling line circuits (SLC) must be electrically supervised for:
- Open circuit
- Ground fault
- Short circuit
- Trouble conditions annunciate at FACP (amber LED, trouble buzzer)

### 4.3 Fire Alarm System Types

#### 4.3.1 Conventional (Hardwired) Systems

**Characteristics**:
- Zone-based addressing (one zone = one circuit with multiple devices)
- Each initiating device circuit (IDC) is a zone
- Cannot identify individual device in alarm (only zone number)
- Notification appliance circuits (NAC) are power-limited output circuits

**Typical Applications**:
- Small buildings (<10,000 ft²)
- Simple occupancies (small offices, retail)
- Renovation where addressable not cost-effective

**Advantages**:
- Lower initial cost
- Simple troubleshooting
- Less complex programming

**Limitations**:
- Limited device capacity per zone (typically 20-30 devices)
- Difficult to pinpoint fault location
- More wire required (home-run circuits)

#### 4.3.2 Addressable (Analog) Systems

**Characteristics**:
- Each device has unique address on signaling line circuit (SLC)
- FACP identifies specific device in alarm or trouble
- Class A or Class B signaling circuits (Class A = redundant path)
- Reduced wire (loop/T-tap topology)

**Device Types**:
- Addressable smoke detectors (analog or multi-criteria)
- Addressable heat detectors
- Addressable modules (monitor, relay, isolator)
- Addressable pull stations
- Addressable notification appliances

**Typical Applications**:
- Medium to large buildings (>10,000 ft²)
- Complex occupancies (hospitals, high-rises, campuses)
- Buildings requiring detailed event reporting

**Advantages**:
- Pinpoint device identification (floor, room, device number)
- Reduced wiring costs (loop topology)
- Advanced features (pre-alarm, sensitivity adjustment, device verification)
- Easier troubleshooting

**Limitations**:
- Higher initial cost per device
- More complex programming
- Requires trained technicians for service

#### 4.3.3 Networked Systems

**Characteristics**:
- Multiple FACPs networked together (typically fiber optic)
- Peer-to-peer communication (distributed intelligence)
- Campus-wide or multi-building fire alarm reporting

**Applications**:
- Large campus facilities (universities, corporate campuses)
- Multi-building complexes
- Buildings requiring offsite monitoring/control

**Advantages**:
- Central monitoring and reporting
- Coordinated response across buildings
- Redundant communication paths

### 4.4 Fire Alarm Circuit Classes

#### 4.4.1 Circuit Class Definitions (NFPA 72 Chapter 12)

| Class | Description | Fault Tolerance | Typical Wiring |
|-------|-------------|----------------|----------------|
| **Class B (Style 4)** | Single path, no redundancy | Open fault = loss of devices beyond fault | T-tap or daisy-chain |
| **Class A (Style 7)** | Redundant return path | Open fault = system still operational | Loop (return to panel) |
| **Class X (Style 6)** | Survivability - monitored for shorts | Short circuit isolates only affected section | Loop with isolator modules |

**SLC (Signaling Line Circuit) Classes**:
- **Class B**: Most common for addressable systems, single fault disables devices beyond fault point
- **Class A**: Loop returns to panel, single open fault = system continues operating from other direction
- **Class X**: Class A + short circuit isolation via isolator modules (one per device or per zone)

**NAC (Notification Appliance Circuit) Classes**:
- **Class B**: Single path power-limited circuit
- **Class A**: Loop configuration with redundant power feed

**Power-Limited Circuits**:
- Fire alarm circuits typically power-limited per **NEC Article 760**
- PLFA (Power-Limited Fire Alarm): Volts and current limited to safe levels
- Wiring may be in same raceway (with restrictions), less conduit required

### 4.5 Fire Alarm Wiring (NEC Article 760)

#### 4.5.1 PLFA (Power-Limited Fire Alarm) Circuits

**Conductor Types**:
- **FPLP** (Plenum): Use in ducts, plenums, spaces used for environmental air
- **FPLR** (Riser): Use in vertical runs between floors
- **FPL** (General): Use in general building areas

**Typical Cables**:
- 18 AWG or 16 AWG stranded copper
- 2-conductor for NACs, 2 or 4 conductor for SLCs
- Shielded cable for SLCs (reduces EMI/RFI interference)

**Color Coding** (Industry Standard):
- **Red**: Fire alarm circuits (PLFA)
- **Red jacket**: Fire alarm cables
- Differentiate from other low-voltage systems

**Circuit Voltage Drop**:
- Maximum 10% voltage drop at end-of-line device during alarm
- Critical for proper notification appliance operation
- Calculate: VD = (2 × L × I × R) / 1000, where L = one-way length (ft), I = current (A), R = resistance (Ω per 1000 ft)

**Example Calculation**:
```
Circuit: 500 ft one-way, 18 AWG (6.4 Ω/1000 ft), 2 A load
VD = (2 × 500 × 2 × 6.4) / 1000 = 12.8 V drop
If circuit voltage = 24 VDC, VD% = (12.8 / 24) × 100 = 53% (FAIL - exceeds 10%)
Solution: Use 16 AWG (4.0 Ω/1000 ft) or increase circuit voltage
```

#### 4.5.2 Conduit and Raceway Requirements

**General**:
- PLFA circuits may run in same conduit/raceway with power and lighting circuits **if**:
  - All circuits operate at 150V or less to ground, AND
  - All circuits associated with same equipment or function
- Separate raceways preferred for troubleshooting

**Fire Alarm Circuit Identification**:
- Red wire/cable or red tape identification at terminations
- Labeling: "FIRE ALARM CIRCUIT" on boxes, panels

**Separation from Power Circuits**:
- 2-inch minimum separation from power circuits >150V (if not in raceway)
- Physical barrier or separate raceway if >150V to ground

---

## 5. SPRINKLER SYSTEM REQUIREMENTS (NFPA 13)

### 5.1 When Sprinkler Systems Are Required

NFPA 101 and IBC mandate automatic sprinkler systems based on occupancy, building size, and fire risk.

#### 5.1.1 Sprinkler Requirements by Occupancy (NFPA 101)

| Occupancy | Sprinkler Required When... |
|-----------|---------------------------|
| **Assembly (A)** | Occupant load ≥300, OR building area >12,000 ft², OR located above or below discharge level |
| **Business (B)** | Building area >15,000 ft², OR building >two stories, OR high-rise |
| **Educational (E)** | Building area >20,000 ft², OR building >two stories |
| **Healthcare (I-2)** | Always required (all healthcare occupancies, all sizes) |
| **Detention (I-3)** | Always required (all detention/correctional facilities) |
| **Residential (R-1)** | Always required (hotels, motels ≥4 stories or >4 units) |
| **Residential (R-2)** | Building >four stories, OR building >three stories with >16 units |
| **Mercantile (M)** | Building area >12,000 ft², OR building >two stories with occupant load >100 above/below discharge |
| **Storage (S)** | High-piling storage, hazardous materials, or high-rise |

**IBC High-Rise** (IBC Section 403):
- Buildings with occupied floor >75 ft above fire department access
- Automatic sprinklers required throughout (no exceptions)

**NFPA 13 Occupancy Hazard Classifications**:
- **Light Hazard**: Churches, hospitals, offices, schools, theaters (low combustibility)
- **Ordinary Hazard Group 1**: Automotive parking, electronics, laundries, restaurants
- **Ordinary Hazard Group 2**: Libraries, machine shops, warehouses (moderate combustibility)
- **Extra Hazard Group 1**: Aircraft hangars, printing, sawmills (high combustibility)
- **Extra Hazard Group 2**: Flammable liquids, chemical manufacturing (very high hazard)

### 5.2 Sprinkler System Types

#### 5.2.1 Wet Pipe Systems

**Description**:
- Piping filled with water under pressure at all times
- Fusible link on sprinkler head opens at design temperature (typically 165°F or 286°F)
- Water discharges immediately
- Most common and reliable system type

**Applications**:
- Buildings with heated spaces (no freezing risk)
- General commercial, residential, educational, healthcare
- Interior spaces maintained above 40°F

**Advantages**:
- Simplest and most reliable design
- Immediate water discharge
- Lowest maintenance
- Least expensive

**Limitations**:
- Not suitable for unheated spaces (freezing risk)
- Water damage risk from accidental discharge or leaks

#### 5.2.2 Dry Pipe Systems

**Description**:
- Piping filled with compressed air or nitrogen (typically 20-40 psi)
- Dry pipe valve holds water back (differential pressure)
- Fusible link opens, air releases, valve trips, water flows
- Time delay: 30-60 seconds for water to reach sprinkler head

**Applications**:
- Unheated spaces (parking garages, warehouses, loading docks)
- Exterior areas subject to freezing
- Buildings with intermittent heating

**Advantages**:
- No freezing risk
- Can protect unheated spaces
- Water damage limited to activated zones

**Limitations**:
- Slower water delivery (30-60 sec delay)
- More complex (compressor, dry valve, trip test required)
- Higher maintenance (air leaks, corrosion from moisture)
- Increased fire growth during delay

**Design Considerations**:
- Maximum 750 gallons system capacity per NFPA 13 (limits piping volume)
- Air compressor required (typically 1/3 HP to 1 HP)
- Quick-opening device may be required (reduces delay)

#### 5.2.3 Preaction Systems

**Description**:
- Piping filled with air (supervised) or empty
- Activation requires two events:
  1. Detection system activation (smoke/heat detectors), AND
  2. Sprinkler head fusible link opening
- Preaction valve admits water to piping on detection
- Water discharges only if sprinkler head also opens

**Types**:
- **Single Interlock**: Detection OR sprinkler head opening admits water
- **Double Interlock**: Detection AND sprinkler head opening required (most common)
- **Non-Interlock**: Detection admits water, no air supervision

**Applications**:
- High-value equipment areas (data centers, server rooms)
- Museums, archives, libraries (water-sensitive contents)
- Cold storage facilities
- Areas where accidental discharge must be prevented

**Advantages**:
- Early warning (detection system alarms before sprinkler discharge)
- Minimizes water damage (two-stage activation)
- Supervised piping (detects leaks)

**Limitations**:
- Most complex system type
- Higher initial cost
- More maintenance (detection system + sprinkler system)
- Time delay before discharge

#### 5.2.4 Deluge Systems

**Description**:
- Piping empty at all times
- Open sprinkler heads (no fusible link)
- Deluge valve admits water on detection system activation
- All heads discharge simultaneously

**Applications**:
- High-hazard areas (flammable liquids, aircraft hangars, chemical storage)
- Transformers, fuel loading racks
- Areas requiring rapid, simultaneous coverage

**Advantages**:
- Immediate coverage of entire protected area
- Suitable for fast-spreading fires
- No fusible links (no thermal lag)

**Limitations**:
- Highest water demand (all heads discharge)
- Extensive water damage
- Complex detection and control systems
- Requires manual reset after activation

### 5.3 Sprinkler Design Criteria (NFPA 13)

#### 5.3.1 Design Density and Area

**Design Method**: Density/Area method per NFPA 13 Figure 11.2.3.1.1

**Density**: Gallons per minute per square foot (gpm/ft²) application rate

**Design Area**: Contiguous area of most hydraulically remote sprinklers

| Occupancy Hazard | Design Density (gpm/ft²) | Design Area (ft²) | Coverage per Head (ft²) |
|-----------------|-------------------------|------------------|------------------------|
| Light Hazard | 0.10 | 1,500 | 130-200 |
| Ordinary Hazard 1 | 0.15 | 1,500 | 130 |
| Ordinary Hazard 2 | 0.20 | 1,500 | 130 |
| Extra Hazard 1 | 0.30 | 2,500 | 100 |
| Extra Hazard 2 | 0.40 | 2,500 | 100 |

**Example Calculation**:
```
Occupancy: Ordinary Hazard Group 2 (warehouse)
Design density: 0.20 gpm/ft²
Design area: 1,500 ft²
Total water demand = 0.20 × 1,500 = 300 gpm (sprinklers only)
Add hose stream allowance: 250 gpm (OH2)
Total water supply required = 300 + 250 = 550 gpm
Duration: 60-90 minutes (OH2)
```

#### 5.3.2 Sprinkler Head Spacing

**Maximum Spacing** (NFPA 13 Table 8.6.2.2.1):

| Construction Type | Maximum Spacing Between Heads |
|------------------|------------------------------|
| Combustible | 15 ft |
| Noncombustible | 15 ft |

**Maximum Area of Coverage per Head**:

| Occupancy Hazard | Maximum Area per Head (ft²) |
|-----------------|----------------------------|
| Light Hazard | 130 (with beams), 200 (smooth ceiling) |
| Ordinary Hazard | 130 |
| Extra Hazard | 100 |

**Minimum Spacing**:
- 6 ft between sprinkler heads (prevents thermal disruption)

**Distance from Walls**:
- Maximum 1/2 the allowable distance between heads
- Typically 7.5 ft from wall (if 15 ft spacing)

#### 5.3.3 Sprinkler Head Types

**Pendent**:
- Hangs down from piping
- Deflector directs water downward and outward
- Most common type for offices, commercial spaces

**Upright**:
- Installed on top of piping
- Deflector directs water upward then outward
- Common in mechanical rooms, storage areas (exposed piping)

**Sidewall**:
- Mounts on wall, projects into room
- One-sided coverage pattern
- Used in corridors, small rooms (reduces piping)

**Concealed**:
- Recessed in ceiling with decorative cover plate
- Cover drops away at lower temperature (135°F typical)
- Sprinkler activates at rated temperature (165°F or 286°F)
- Used in finished spaces for aesthetics

**ESFR (Early Suppression Fast Response)**:
- Large orifice (K-factor ≥11.2)
- Fast response element (RTI ≤50)
- High-challenge fires (rack storage)
- Reduces design area and water demand vs. standard spray

**Temperature Ratings**:

| Color Code | Temperature Rating (°F) | Typical Application |
|-----------|------------------------|---------------------|
| Uncolored/Black | 135-170 | Standard office, commercial |
| White | 135-170 | Standard office, commercial |
| Blue | 175-225 | Boiler rooms, kitchens (high ambient) |
| Red | 250-300 | Near heat sources (ovens, dryers) |
| Green | 325-375 | Extremely high ambient temp areas |

### 5.4 Water Supply Requirements

#### 5.4.1 Water Supply Sources

**Municipal Water**:
- Most common source
- Must provide adequate pressure and flow at design point
- Backflow preventer required (NFPA 13 Section 8.16.1)
- Pressure-reducing valve if supply >175 psi

**Fire Pump**:
- Required when municipal supply insufficient
- Typical sizes: 250-2500 gpm, 50-150 psi boost
- Electric motor or diesel engine driven
- Located in dedicated fire pump room (2-hour rated)
- Weekly testing required

**Water Storage Tanks**:
- Gravity tank, pressure tank, or ground-level suction tank
- Required capacity: Design flow × duration (gpm × minutes / 60)
- Must be maintained above freezing

#### 5.4.2 Backflow Prevention (NFPA 13 Section 8.16.1)

**Required for All Sprinkler Systems**:
- Prevents contaminated water from entering municipal supply
- Type depends on connection and system additives

**Backflow Preventer Types**:
- **Reduced Pressure Zone (RPZ)**: High hazard, used when antifreeze or foam additives in system
- **Double Check Valve Assembly (DCVA)**: Standard for wet pipe systems, no additives
- **Pressure Vacuum Breaker (PVB)**: Atmospheric protection, cannot be under continuous pressure

**Location**:
- Between municipal water supply and sprinkler system
- Accessible for testing and maintenance
- Protected from freezing if outdoors

#### 5.4.3 Hose Stream Allowance

In addition to sprinkler water demand, NFPA 13 requires hose stream allowance for fire department use:

| Occupancy Hazard | Hose Stream Allowance (gpm) | Duration (minutes) |
|-----------------|----------------------------|-------------------|
| Light Hazard | 100 | 30 |
| Ordinary Hazard | 250 | 60-90 |
| Extra Hazard | 500 | 90-120 |

**Total Water Supply** = Sprinkler demand (gpm) + Hose stream (gpm) for duration specified

### 5.5 Piping and Components

#### 5.5.1 Piping Materials (NFPA 13 Table 6.3.1.1)

**Steel Pipe**:
- Black steel (Schedule 10, 40, or listed thin-wall)
- Galvanized steel (dry pipe systems, corrosion protection)
- Threaded, grooved, or welded fittings

**CPVC (Chlorinated Polyvinyl Chloride)**:
- Listed for Light Hazard occupancies only
- Residential and light commercial
- Maximum 150°F operating temperature
- Lower cost, easier installation

**Copper Tubing**:
- Type K, L, or M
- Soldered or brazed fittings
- Suitable for Light and Ordinary Hazard

**Diameter**:
- Hydraulically calculated based on flow and pressure loss
- Typical ranges: 1-inch (branch lines) to 8-inch (mains)
- Minimum 1-inch diameter to sprinkler heads

#### 5.5.2 Sprinkler System Valves

**Main Control Valve** (Riser):
- OS&Y (Outside Screw and Yoke) gate valve most common
- Post indicator valve (PIV) for underground supply
- Tamper switch required (fire alarm supervision)
- Locked or supervised open position

**Alarm Check Valve** (Wet Pipe):
- One-way valve with pressure switch
- Allows water flow to sprinklers, triggers alarm on flow
- Retarding chamber delays false alarms (surges)

**Dry Pipe Valve** (Dry Pipe Systems):
- Differential pressure valve holds water back
- Air/nitrogen on system side, water on supply side
- Low pressure air trip opens valve, admits water

**Preaction Valve** (Preaction Systems):
- Electrically operated deluge valve with air supervision
- Opens on detection system signal
- Manual release also provided

**Inspector's Test Connection**:
- Simulates one sprinkler head opening
- Tests waterflow alarm and pressure switch
- Located at most remote point of system

**Drain Valves**:
- Required at low points and end of mains
- Drain system for maintenance or freezing risk

---

## 6. EMERGENCY LIGHTING AND EXIT SIGNS

### 6.1 Emergency Lighting Requirements (NFPA 101 Section 7.9)

#### 6.1.1 When Emergency Lighting Is Required

**Required in**:
- Means of egress (exit access corridors, stairs, exit discharge)
- Assembly occupancies (>50 occupant load)
- Educational occupancies (>100 occupant load)
- Healthcare, detention/correctional (all occupancies)
- Business occupancies (>500 occupant load or >two stories)
- Mercantile, industrial (based on size and hazard)

**Not Required**:
- One- and two-family dwellings (R-3)
- Small occupancies with immediate exit access to exterior

#### 6.1.2 Emergency Lighting Performance

**Illumination Levels** (NFPA 101 Section 7.9.2):
- **Average**: 1.0 foot-candle (fc) at floor level along path of egress
- **Minimum**: 0.1 fc at any point along path of egress
- **Uniformity**: Maximum-to-minimum ratio ≤40:1

**Duration**:
- Minimum **90 minutes** of illumination after loss of normal power

**Lighting Sources**:
1. **Unit Equipment** (Battery-powered emergency lights):
   - Self-contained battery backup in light fixture
   - LED or halogen lamps
   - Test button and charge indicator
   - 90-minute rated battery

2. **Central Battery System**:
   - Central battery bank feeds emergency fixtures
   - Typically 90-120 minute capacity
   - Requires dedicated emergency circuits

3. **Generator with Automatic Transfer Switch (ATS)**:
   - Emergency generator starts on power loss
   - Transfer switch connects emergency circuits <10 seconds
   - Provides indefinite emergency power (fuel supply dependent)

#### 6.1.3 Emergency Lighting Design

**Coverage**:
- All exit access corridors and passageways
- All exit stairs and ramps
- Exit discharge areas (exterior paths to public way)
- Interior rooms >1,000 ft² with occupant load >50

**Fixture Placement**:
- Provide uniform illumination (no dark spots)
- Illumination level measured at floor
- Use photometric calculations or manufacturer spacing data

**Testing** (NFPA 101 Section 7.9.3):
- Monthly 30-second functional test
- Annual 90-minute full-duration test
- Documentation of all tests required

### 6.2 Exit Sign Requirements (NFPA 101 Section 7.10)

#### 6.2.1 When Exit Signs Are Required

**Required at**:
- Every exit door
- Doors that might be mistaken for exits (mark "NOT AN EXIT")
- Locations where exit path direction is not obvious

**Visibility**:
- Clearly visible from all directions of egress approach
- Intermediate directional signs where path to exit not apparent

#### 6.2.2 Exit Sign Performance

**Illumination**:
- **Internally Illuminated**: Lettering minimum 6 inches high, ¾-inch stroke
  - Red or green lettering (green typically for LED signs)
- **Externally Illuminated**: Minimum 5 foot-candles on sign face

**Power**:
- Connected to emergency power source (same as emergency lighting)
- Battery backup or generator
- Minimum 90 minutes of illumination after power loss

**Mounting Height**:
- No specific NFPA 101 requirement (IBC: top of sign ≥80 inches AFF)
- Typical mounting: 80-96 inches to bottom of sign

**Viewing Distance**:
- Internally illuminated: Visible at 100 feet minimum

#### 6.2.3 Photoluminescent Exit Signs

**Alternative to Illuminated Signs**:
- Absorb ambient light, glow in darkness
- No electrical connection required
- Must charge with minimum 54 lux (5 fc) for ≥60 minutes
- Luminance must meet NFPA 101 Section 7.10.7 requirements

**Advantages**:
- No electrical power required
- No battery maintenance
- Compliant for emergency egress marking

---

## 7. INTEGRATION WITH MEP QA VALIDATION

### 7.1 Fire Alarm System QA Validation

#### 7.1.1 Fire Alarm Drawing Checks

**Device Placement**:
- Verify smoke detector spacing ≤900 ft² coverage (30 ft × 30 ft, smooth ceiling)
- Apply ceiling height spacing modifiers (Table 17.7.3.2.3.1)
- Check pull station locations ≤200 ft travel distance
- Duct smoke detectors shown on HVAC systems >2,000 cfm

**Device Counts and Zoning**:
- Verify device addressable or zone assignment matches submittal
- Check initiating device circuit (IDC) device capacity not exceeded
- Notification appliance circuit (NAC) load calculation (amps) within panel capacity

**Notification Appliance Coverage**:
- Audible: Verify 75 dBA minimum in corridors, 70 dBA in rooms (public mode)
- Visible: Verify strobe candela ratings meet room size requirements (Table 18.5.5.4.1)
- Synchronization noted for all visible appliances

**Example QA Rule**:
```
IF smoke_detector.ceiling_height > 15_ft AND smoke_detector.ceiling_height <= 20_ft
THEN max_spacing = 30_ft × 0.85 = 25.5_ft
IF actual_spacing > 25.5_ft
THEN FAIL("Smoke detector spacing exceeds NFPA 72 requirement for ceiling height")
```

#### 7.1.2 Fire Alarm Electrical Integration

**Panel Location**:
- Accessible to fire department (within 10 ft of entrance or fire command center)
- Dedicated circuit labeled "FIRE ALARM"
- Battery backup capacity: 24-hour standby + 5-minute alarm

**Circuit Classes**:
- Verify SLC (signaling line circuit) Class A or B shown on drawings
- NAC (notification appliance circuit) Class A or B shown
- End-of-line resistors (EOLRs) indicated for Class B circuits

**Wiring and Conduit**:
- Fire alarm circuits in red conduit or red-jacketed cable
- FPLP (plenum), FPLR (riser), or FPL (general) cable types specified
- Voltage drop calculation performed for NACs (≤10% maximum)

**Example Voltage Drop QA Check**:
```python
def validate_nac_voltage_drop(circuit_length_ft, wire_gauge, current_amps, voltage):
    resistance_per_1000ft = {"18": 6.4, "16": 4.0, "14": 2.5, "12": 1.6}
    R = resistance_per_1000ft[str(wire_gauge)]
    VD = (2 × circuit_length_ft × current_amps × R) / 1000
    VD_percent = (VD / voltage) × 100

    if VD_percent > 10:
        return f"FAIL: NAC voltage drop {VD_percent:.1f}% exceeds 10% limit (NFPA 72)"
    return "PASS"
```

#### 7.1.3 Fire Alarm and HVAC Coordination

**Duct Smoke Detectors**:
- Verify duct detector shown on supply air (>2,000 cfm)
- Verify return air duct detector (>15,000 cfm return)
- Control sequence: Shut down AHU on smoke detection
- Coordinate with mechanical drawings (AHU start/stop)

**Smoke Dampers**:
- Smoke dampers shown at smoke barriers
- Control: Tied to fire alarm (smoke detector at damper or area detector)
- Damper fail-safe: Closes on power loss
- Coordinate damper location with fire-rated wall schedules

### 7.2 Sprinkler System QA Validation

#### 7.2.1 Sprinkler Drawing Checks

**Occupancy Hazard Classification**:
- Verify occupancy hazard documented (Light, OH1, OH2, EH1, EH2)
- Cross-reference NFPA 13 Table 5.3.1 for correct classification

**Sprinkler Head Spacing**:
- Maximum 15 ft between heads (combustible/noncombustible construction)
- Maximum area per head: 130 ft² (OH), 200 ft² (LH smooth ceiling), 100 ft² (EH)
- Minimum 6 ft between heads

**Coverage**:
- All areas shown with sprinkler coverage (no unprotected spaces)
- Under mezzanines, platforms, and similar obstructions
- Closets >24 ft² or containing equipment

**Example QA Rule**:
```
IF occupancy_hazard = "Ordinary Hazard"
AND sprinkler_spacing_ft > 15_ft
THEN FAIL("Sprinkler spacing exceeds NFPA 13 maximum 15 ft for OH")

IF area_per_head > 130_sqft
THEN FAIL("Area per head exceeds 130 ft² for OH occupancy")
```

#### 7.2.2 Hydraulic Calculation Review

**Water Supply Data**:
- Verify water supply flow test data documented
- Static pressure, residual pressure, and flow (gpm) at test hydrant
- Date of flow test (<1 year old preferred)

**Hydraulic Calc Summary**:
- Design area (ft²) matches occupancy hazard classification
- Design density (gpm/ft²) meets NFPA 13 Figure 11.2.3.1.1
- Hose stream allowance added (100-500 gpm depending on hazard)
- Total demand at BOR (base of riser) + static pressure ≤ available supply

**Example Hydraulic Validation**:
```python
def validate_hydraulic_demand(occupancy, design_area, design_density, hose_stream):
    requirements = {
        "Light Hazard": {"area": 1500, "density": 0.10, "hose": 100},
        "OH1": {"area": 1500, "density": 0.15, "hose": 250},
        "OH2": {"area": 1500, "density": 0.20, "hose": 250},
        "EH1": {"area": 2500, "density": 0.30, "hose": 500},
    }

    req = requirements[occupancy]
    issues = []

    if design_area < req["area"]:
        issues.append(f"Design area {design_area} < required {req['area']} ft²")
    if design_density < req["density"]:
        issues.append(f"Design density {design_density} < required {req['density']} gpm/ft²")
    if hose_stream < req["hose"]:
        issues.append(f"Hose stream {hose_stream} gpm < required {req['hose']} gpm")

    return "FAIL: " + "; ".join(issues) if issues else "PASS"
```

#### 7.2.3 Sprinkler and Fire Alarm Integration

**Waterflow Switches**:
- Verify waterflow switch shown on each sprinkler zone
- Connected to fire alarm system IDC
- Time delay: 5-90 seconds (adjustable, typically 30 seconds)

**Tamper Switches**:
- Tamper switch shown on all control valves (main riser, zone valves)
- Connected to fire alarm supervisory circuit
- Supervisory signal to fire alarm (not alarm signal)

**Fire Pump Integration**:
- Fire pump start signal on waterflow or pressure drop
- Fire pump running status to fire alarm (supervisory)

**Control Sequence Coordination**:
```
Sprinkler waterflow detected →
  Fire alarm IDC activates →
    FACP initiates building alarm →
      Notification appliances activate (horns/strobes) →
        HVAC units shut down (duct detectors or central shutdown) →
          Elevator recall to main floor (if building has elevators) →
            Fire department notified (central station monitoring)
```

### 7.3 Occupancy and Life Safety Code Coordination

#### 7.3.1 Means of Egress Validation

**Exit Capacity Calculation**:
- Occupant load calculation based on NFPA 101 Table 7.3.1.2
- Required exit width = occupant load × 0.15" (doors at grade) or 0.20" (stairs)
- Verify door widths, corridor widths, stair widths meet minimum

**Travel Distance Validation**:
- Maximum travel distance to exit based on occupancy and sprinkler protection
- Sprinklered: 250-300 ft (typical)
- Unsprinklered: 200 ft (typical)

**Example QA Rule**:
```
IF occupancy = "Business" AND sprinklered = TRUE
AND travel_distance_to_exit > 300_ft
THEN FAIL("Travel distance exceeds NFPA 101 limit for sprinklered business occupancy")
```

#### 7.3.2 Fire Resistance Rating Validation

**Occupancy Separation**:
- Verify fire barrier ratings between occupancies meet NFPA 101 Table 6.1.14.4.1(b)
- Healthcare (I-2) or Detention (I-3) adjacent to other occupancies: 2-hour minimum

**Corridor Fire Ratings**:
- Verify corridor walls rated per occupancy and sprinkler status
- Healthcare: 1-hour smoke barrier (always)
- Business sprinklered: No rating required (0-hour)

**MEP Penetration Firestopping**:
- All penetrations through fire-rated assemblies show firestopping detail reference
- UL system number specified for firestopping
- Fire dampers and smoke dampers shown where required

#### 7.3.3 Emergency Power Coordination

**Fire Alarm Emergency Power**:
- Primary: Dedicated branch circuit
- Secondary: Battery backup (24-hour standby + 5-minute alarm)
- Verify battery amp-hour capacity calculation shown

**Emergency Lighting Emergency Power**:
- Unit equipment: Self-contained battery (90-minute rated)
- Central system: Battery bank or generator with ATS
- Verify 90-minute duration provided

**Standby Power Systems** (NEC Article 701):
- Fire pumps, emergency lighting, fire alarm, smoke control
- Automatic transfer switch (ATS) <10 seconds
- Generator sized for connected emergency loads

---

## 8. REFERENCES AND RESOURCES

### 8.1 Primary NFPA Standards

1. **NFPA 101: Life Safety Code** (2024 Edition)
   - Available: https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=101
   - Free online access (read-only) with NFPA account

2. **NFPA 13: Installation of Sprinkler Systems** (2022 Edition)
   - Available: https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=13

3. **NFPA 72: National Fire Alarm and Signaling Code** (2022 Edition)
   - Available: https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=72

4. **NFPA 70: National Electrical Code (NEC)** (2023 Edition)
   - Available: https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=70

### 8.2 Related Codes and Standards

- **IBC 2021**: International Building Code (fire/life safety chapters)
- **NFPA 80**: Fire Doors and Other Opening Protectives
- **NFPA 90A**: Air Conditioning and Ventilating Systems
- **NFPA 92**: Smoke Control Systems
- **NFPA 110**: Emergency and Standby Power Systems
- **UL 555**: Fire Dampers
- **UL 555S**: Smoke Dampers
- **ASTM E814 / UL 1479**: Fire Resistive Penetrations

### 8.3 Testing and Certification

- **UL (Underwriters Laboratories)**: Product testing and listing
- **FM Global**: Property loss prevention and equipment approval
- **ICC-ES**: Product evaluation and certification
- **AHRI**: Air-conditioning and refrigeration equipment certification

### 8.4 Online Resources

- **NFPA Free Access**: https://www.nfpa.org/codes-and-standards/free-access
- **ICC Digital Codes**: https://codes.iccsafe.org/
- **UL Product iQ**: https://iq.ulprospector.com/ (product listings and certifications)
- **FM Approvals**: https://www.fmapprovals.com/ (approved equipment search)

---

## 9. DOCUMENT CONTROL

**Version**: 1.0
**Effective Date**: 2025-10-22
**Author**: Agent 2 - Life Safety Specialist
**Review Cycle**: Annual or upon code adoption changes

**Paraphrasing Notice**: All content has been paraphrased from publicly available NFPA and ICC resources. No verbatim reproduction of copyrighted text. Users must consult official code publications for legal compliance.

**Jurisdiction Disclaimer**: This summary reflects base NFPA codes. Local jurisdictions may adopt different editions or amendments. Always verify adopted code editions for your project jurisdiction.

**Integration Note**: This document supports the MEP Drawing QA/QC workflow defined in `skills/engineering-drawing-qaqc/SKILL.md`. Occupancy classification, fire alarm, and sprinkler system requirements drive validation rules for fire protection drawings.

---

**End of Document**
