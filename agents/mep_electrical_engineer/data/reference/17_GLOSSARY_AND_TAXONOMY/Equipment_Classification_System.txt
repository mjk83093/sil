# MEP Equipment Classification System

## Overview

This document provides a comprehensive classification system for MEP equipment, organized by CSI MasterFormat divisions, functional categories, and technical specifications. This taxonomy supports automated tagging, validation, and equipment schedule generation for engineering drawing QA/QC.

---

## 1. Classification Hierarchy

### 1.1 Multi-Dimensional Classification
MEP equipment is classified along five dimensions:

1. **CSI Division** - Industry-standard specification organization
2. **Functional Category** - Primary system function (heating, cooling, distribution, etc.)
3. **Voltage/Pressure Class** - Operating characteristics
4. **Location Category** - Installation environment
5. **Equipment Tag Convention** - Standardized naming scheme

---

## 2. CSI MasterFormat Division Structure

### Division 21 - Fire Suppression
**Scope:** Fire protection systems and equipment

#### 21 10 00 - Water-Based Fire-Suppression Systems
- Fire sprinkler systems (wet, dry, preaction, deluge)
- Standpipe systems
- Fire pumps
- Fire department connections

#### 21 20 00 - Fire-Extinguishing Systems
- Clean agent systems (FM-200, Novec, Inergen)
- CO2 suppression systems
- Dry chemical systems
- Foam suppression systems

#### 21 30 00 - Fire Pumps
- Electric-driven fire pumps
- Diesel-driven fire pumps
- Jockey pumps
- Controllers and accessories

---

### Division 22 - Plumbing
**Scope:** Water supply, drainage, and specialty piping

#### 22 10 00 - Plumbing Piping and Pumps
- Domestic water piping
- Sanitary waste piping
- Storm drainage piping
- Domestic water pumps (booster, circulating, sump)

#### 22 30 00 - Plumbing Equipment
- Water heaters (tank, tankless, heat pump)
- Water treatment equipment
- Backflow preventers
- Expansion tanks and pressure vessels

#### 22 40 00 - Plumbing Fixtures
- Water closets, urinals
- Lavatories, sinks
- Showers, bathtubs
- Service sinks, floor drains

#### 22 60 00 - Gas and Vacuum Systems for Laboratory and Healthcare Facilities
- Medical gas systems (oxygen, medical air, vacuum)
- Laboratory gas distribution
- Waste anesthetic gas disposal (WAGD)

---

### Division 23 - Heating, Ventilating, and Air Conditioning (HVAC)
**Scope:** HVAC systems and equipment

#### 23 05 00 - Common Work Results for HVAC
- HVAC insulation
- Vibration isolation
- Air and hydronic balancing

#### 23 10 00 - Facility Fuel Systems
- Fuel oil piping and tanks
- Natural gas piping
- Propane systems

#### 23 20 00 - HVAC Piping and Pumps
- Hydronic piping (chilled water, hot water, condenser water)
- Hydronic pumps
- Expansion tanks and air separators

#### 23 30 00 - HVAC Air Distribution
- Ductwork (supply, return, exhaust)
- Air terminal units (diffusers, grilles, registers)
- Variable air volume (VAV) boxes
- Duct dampers and access doors

#### 23 40 00 - HVAC Air Cleaning Devices
- Air filters (MERV rated)
- Electronic air cleaners
- HEPA filtration units

#### 23 50 00 - Central Heating Equipment
- Boilers (hot water, steam)
- Furnaces
- Infrared heaters
- Unit heaters

#### 23 60 00 - Central Cooling Equipment
- Chillers (air-cooled, water-cooled)
- Cooling towers
- Condensing units

#### 23 70 00 - Central HVAC Equipment
- Air handling units (AHU)
- Rooftop units (RTU)
- Makeup air units (MAU)
- Energy recovery ventilators (ERV/HRV)

#### 23 80 00 - Decentralized HVAC Equipment
- Fan coil units (FCU)
- Split system air conditioners
- Window air conditioners
- Packaged terminal air conditioners (PTAC)
- Dedicated outdoor air systems (DOAS)

---

### Division 25 - Integrated Automation
**Scope:** Building automation and control systems

#### 25 10 00 - Integrated Automation Facility Controls
- Building automation systems (BAS)
- Direct digital control (DDC) systems
- Controllers and sensors
- HVAC control sequences

#### 25 30 00 - Integrated Automation Instrumentation and Terminal Devices
- Temperature sensors
- Humidity sensors
- Pressure sensors
- Control valves and dampers

---

### Division 26 - Electrical
**Scope:** Electrical power distribution and lighting

#### 26 05 00 - Common Work Results for Electrical
- Raceways and boxes
- Conductors and cables
- Grounding and bonding

#### 26 10 00 - Medium-Voltage Electrical Distribution
- Switchgear (4.16kV, 13.8kV)
- Medium-voltage transformers
- Medium-voltage circuit breakers

#### 26 20 00 - Low-Voltage Electrical Transmission
- Electrical service entrance
- Transformers (dry-type, pad-mounted)
- Main distribution panels
- Panelboards (lighting, power, emergency)
- Switchboards

#### 26 30 00 - Facility Electrical Power Generating and Storing Equipment
- Emergency generators (diesel, natural gas)
- Uninterruptible power supply (UPS) systems
- Battery backup systems
- Automatic transfer switches (ATS)
- Paralleling switchgear

#### 26 40 00 - Electrical and Cathodic Protection
- Grounding electrode systems
- Lightning protection systems

#### 26 50 00 - Lighting
- Interior lighting fixtures
- Exterior lighting fixtures
- Emergency lighting
- Exit signs
- Lighting controls (switches, dimmers, sensors)

---

### Division 27 - Communications
**Scope:** Data, telecommunications, and AV systems

#### 27 10 00 - Structured Cabling
- Horizontal cabling (Cat5e, Cat6, Cat6A)
- Backbone cabling (fiber optic)
- Cable pathways and spaces
- Telecommunications rooms (MDF, IDF)

#### 27 20 00 - Data Communications
- Network switches and routers
- Patch panels
- Data outlets and faceplates

#### 27 40 00 - Audio-Video Communications
- AV equipment racks
- Displays and projectors
- Audio systems and speakers
- Control systems (Crestron, AMX)

---

### Division 28 - Electronic Safety and Security
**Scope:** Fire alarm, security, and access control

#### 28 10 00 - Electronic Access Control and Intrusion Detection
- Access control systems
- Card readers and credentials
- Electronic locks
- Intrusion detection sensors

#### 28 20 00 - Electronic Surveillance
- Security cameras (IP, analog)
- Video management systems (VMS)
- Network video recorders (NVR)

#### 28 30 00 - Electronic Detection and Alarm
- Fire alarm control panels (FACP)
- Smoke detectors (ionization, photoelectric)
- Heat detectors
- Manual pull stations
- Notification devices (horns, strobes, speakers)

---

## 3. Functional Category Classification

### 3.1 Heating Equipment
| Equipment Type | Primary Function | Secondary Function | Fuel/Energy Source |
|---------------|------------------|-------------------|-------------------|
| Boiler - Hot Water | Space heating | Domestic hot water (optional) | Natural gas, oil, electric |
| Boiler - Steam | Process steam | Space heating | Natural gas, oil |
| Furnace | Space heating | N/A | Natural gas, propane, oil |
| Unit Heater | Spot heating | N/A | Natural gas, electric, hot water |
| Infrared Heater | Radiant heating | N/A | Natural gas, electric |
| Heat Pump | Heating/cooling | N/A | Electric |
| Radiant Floor Heating | Space heating | N/A | Hot water, electric |

**Tag Convention:** BLR-XX (Boiler), FUR-XX (Furnace), UH-XX (Unit Heater)

### 3.2 Cooling Equipment
| Equipment Type | Primary Function | Heat Rejection | Typical Capacity |
|---------------|------------------|---------------|------------------|
| Chiller - Air Cooled | Chilled water production | Air-cooled condenser | 10-500 tons |
| Chiller - Water Cooled | Chilled water production | Cooling tower | 100-2000+ tons |
| Cooling Tower | Heat rejection | Evaporative cooling | Match chiller capacity |
| Condensing Unit | Refrigerant condensing | Air-cooled | 1.5-50 tons |
| Computer Room Air Conditioner (CRAC) | Precision cooling | Air/water-cooled | 5-50 tons |

**Tag Convention:** CHL-XX (Chiller), CT-XX (Cooling Tower), CU-XX (Condensing Unit)

### 3.3 Air Handling Equipment
| Equipment Type | Configuration | Typical CFM Range | Heating/Cooling |
|---------------|---------------|-------------------|----------------|
| Air Handling Unit (AHU) | Built-up, factory assembled | 1,000-100,000 CFM | Hot water, chilled water, steam, electric, DX |
| Rooftop Unit (RTU) | Packaged, self-contained | 1,000-50,000 CFM | Gas heat, electric heat, DX cooling |
| Makeup Air Unit (MAU) | 100% outdoor air | 2,000-50,000 CFM | Gas heat, hot water, electric |
| Exhaust Fan | Centrifugal, axial | 100-50,000 CFM | N/A |
| Energy Recovery Ventilator (ERV) | Sensible + latent recovery | 100-10,000 CFM | N/A |
| Heat Recovery Ventilator (HRV) | Sensible only | 100-10,000 CFM | N/A |

**Tag Convention:** AHU-XX, RTU-XX, MAU-XX, EF-XX, ERV-XX

### 3.4 Terminal Equipment
| Equipment Type | Control Type | Typical CFM Range | Reheat Source |
|---------------|-------------|-------------------|--------------|
| VAV Box with Reheat | Variable volume | 300-5,000 CFM | Hot water, electric |
| VAV Box (Cooling Only) | Variable volume | 300-5,000 CFM | N/A |
| Fan Powered VAV Box | Variable volume + fan | 300-5,000 CFM | Hot water, electric |
| Fan Coil Unit (FCU) | Constant/variable volume | 200-2,000 CFM | Hot water, chilled water |
| Unit Ventilator | Outdoor air + recirculation | 500-3,000 CFM | Hot water, steam, electric |

**Tag Convention:** VAV-XX, FCU-XX, UV-XX

### 3.5 Pumping Equipment
| Equipment Type | Application | Typical GPM Range | Typical Head |
|---------------|-------------|-------------------|-------------|
| Chilled Water Pump | Primary/secondary loop | 10-10,000 GPM | 40-150 ft |
| Hot Water Pump | Primary/secondary loop | 10-5,000 GPM | 40-100 ft |
| Condenser Water Pump | Cooling tower circulation | 50-10,000 GPM | 60-120 ft |
| Domestic Water Booster Pump | Pressure boosting | 5-500 GPM | 50-200 ft |
| Sump Pump | Drainage | 10-100 GPM | 10-30 ft |
| Sewage Ejector Pump | Wastewater | 10-200 GPM | 15-40 ft |
| Fire Pump | Fire protection | 500-3,000 GPM | 100-300 ft |

**Tag Convention:** P-XX (Pump), CHW-P-XX (Chilled Water Pump), HW-P-XX (Hot Water Pump)

### 3.6 Power Distribution Equipment
| Equipment Type | Voltage Class | Typical Ratings | Application |
|---------------|--------------|----------------|-------------|
| Switchgear | 480V-13.8kV | 1200-4000A bus | Main distribution |
| Main Distribution Panel (MDP) | 480V | 800-4000A | Service entrance |
| Switchboard | 480V | 800-4000A | Secondary distribution |
| Panelboard - Lighting | 120/208V, 277/480V | 100-400A | Lighting branch circuits |
| Panelboard - Power | 120/208V, 208V, 480V | 100-400A | Receptacle/equipment circuits |
| Panelboard - Emergency | 120/208V | 100-225A | Emergency/life safety loads |
| Transformer - Dry Type | 480V-120/208V | 15-500 kVA | Step-down distribution |
| Transformer - Pad Mounted | 13.8kV-480V | 75-2000 kVA | Utility service |

**Tag Convention:** SWGR-XX (Switchgear), MDP (Main Distribution Panel), LP-XX (Lighting Panel), PP-XX (Power Panel), EM-XX (Emergency Panel), T-XX (Transformer)

### 3.7 Standby Power Equipment
| Equipment Type | Fuel Source | Typical Ratings | Run Time |
|---------------|------------|----------------|----------|
| Emergency Generator | Diesel | 20-2000 kW | Unlimited (with fuel supply) |
| Emergency Generator | Natural Gas | 20-500 kW | Unlimited (utility gas) |
| UPS System | Battery | 5-500 kVA | 5-30 minutes |
| Battery Backup System | Battery | 1-100 kW | 1-8 hours |
| Automatic Transfer Switch (ATS) | N/A | 100-4000A | N/A |

**Tag Convention:** GEN-XX (Generator), UPS-XX (UPS), ATS-XX (Transfer Switch)

### 3.8 Lighting Equipment
| Equipment Type | Lamp Type | Typical Applications | Voltage |
|---------------|-----------|---------------------|---------|
| Recessed Downlight | LED, CFL | General lighting | 120V, 277V |
| Recessed Troffer | LED, T8 fluorescent | Office lighting | 120V, 277V |
| High Bay/Low Bay | LED, metal halide | Warehouse, industrial | 277V, 480V |
| Wall Pack | LED | Exterior perimeter | 120V, 277V |
| Area Light | LED | Parking lot, roadway | 120V, 277V, 480V |
| Exit Sign | LED | Egress marking | 120V, 277V |
| Emergency Light | LED | Emergency illumination | 120V, 277V |

**Tag Convention:** By fixture type letter (see lighting fixture schedule)

### 3.9 Fire Protection Equipment
| Equipment Type | System Type | Typical Ratings | Application |
|---------------|------------|----------------|-------------|
| Fire Sprinkler Riser | Wet, dry, preaction, deluge | 4"-8" pipe | Automatic suppression |
| Fire Pump | Electric, diesel | 500-2000 GPM @ 100-200 PSI | Pressure boosting |
| Fire Department Connection (FDC) | Siamese, standpipe | 4"-6" | Fire department access |
| Backflow Preventer | Double check, reduced pressure | 3"-8" | Cross-connection control |

**Tag Convention:** FP-RISER-XX, FP-PUMP-XX, FP-FDC-XX

### 3.10 Plumbing Equipment
| Equipment Type | Capacity | Fuel/Energy | Application |
|---------------|----------|------------|-------------|
| Water Heater - Tank | 30-120 gallons | Gas, electric | Domestic hot water |
| Water Heater - Tankless | 180,000-380,000 BTU/hr | Gas | Continuous hot water |
| Water Heater - Heat Pump | 50-80 gallons | Electric | Energy-efficient DHW |
| Water Softener | 30,000-100,000 grains | N/A | Hard water treatment |
| Backflow Preventer | 1/2"-6" | N/A | Potable water protection |
| Grease Interceptor | 20-1000 GPM | N/A | Commercial kitchen |

**Tag Convention:** WH-XX (Water Heater), WS-XX (Water Softener), BP-XX (Backflow Preventer)

### 3.11 Fire Alarm Equipment
| Equipment Type | Zones/Capacity | Protocol | Application |
|---------------|---------------|----------|-------------|
| Fire Alarm Control Panel (FACP) | 4-128 zones | Conventional, addressable | Central monitoring |
| Smoke Detector | N/A | Conventional, addressable | Fire detection |
| Heat Detector | 135°F-200°F | Conventional, addressable | Fire detection |
| Manual Pull Station | N/A | Conventional, addressable | Manual activation |
| Horn/Strobe | 15-177 candela | 24VDC | Notification |
| Annunciator | Zone display | N/A | Remote indication |

**Tag Convention:** FACP-XX, SD-XX (Smoke Detector), HD-XX (Heat Detector), PS-XX (Pull Station), HS-XX (Horn/Strobe)

---

## 4. Voltage/Pressure Class Classification

### 4.1 Electrical Voltage Classes
| Voltage Class | Typical Voltages | Equipment Types | Wire/Conduit Requirements |
|--------------|-----------------|----------------|--------------------------|
| Low Voltage (LV) | 12V, 24V | Fire alarm, BAS, controls | Class 2/3 wiring, plenum-rated |
| Line Voltage - Single Phase | 120V, 208V, 240V | Receptacles, small equipment | 14-12 AWG copper min |
| Line Voltage - Three Phase | 208V, 240V, 480V, 600V | Motors, large equipment | Sized per NEC 430 |
| Medium Voltage (MV) | 4.16kV, 13.8kV | Utility service, large campus | Shielded cable, specialized terminations |

### 4.2 Mechanical Pressure Classes
| Pressure Class | Typical Range | Equipment Types | Piping Standards |
|---------------|--------------|----------------|-----------------|
| Low Pressure Steam | 0-15 PSIG | Heating systems | ASME B31.9 |
| High Pressure Steam | 15-150+ PSIG | Process steam, sterilizers | ASME B31.1 |
| Hydronic - Low Pressure | 0-30 PSIG | Hot water heating, chilled water | ASME B31.9 |
| Hydronic - Medium Pressure | 30-125 PSIG | High-rise buildings | ASME B31.9 |
| Domestic Water | 40-80 PSIG static | Potable water distribution | IPC, UPC |
| Compressed Air | 80-125 PSIG | Laboratory, industrial | ASME B31.9 |
| Medical Gas | 50-55 PSIG | Healthcare facilities | NFPA 99 |

### 4.3 HVAC Duct Pressure Classes
| Pressure Class | Static Pressure Range | Construction Standard | Typical Applications |
|---------------|----------------------|---------------------|---------------------|
| Low Pressure | 0-2 in. w.c. | SMACNA Low Pressure | Residential, small commercial |
| Medium Pressure | 2-6 in. w.c. | SMACNA Medium Pressure | Commercial VAV systems |
| High Pressure | 6-10 in. w.c. | SMACNA High Pressure | Large AHU systems |

---

## 5. Location Category Classification

### 5.1 Indoor Locations
| Location Type | Environmental Conditions | Typical Equipment | Special Requirements |
|--------------|-------------------------|------------------|---------------------|
| Mechanical Room | Conditioned or semi-conditioned | Boilers, chillers, AHUs, pumps | Adequate ventilation, floor drains |
| Electrical Room | Conditioned | Panels, switchgear, transformers | NEC 110.26 clearances, dedicated HVAC |
| Telecommunications Room (IDF/MDF) | Conditioned, 72°F ±2° | Network equipment, patch panels | Dedicated cooling, humidity control |
| Penthouse | Semi-conditioned | AHUs, exhaust fans | Weatherproof construction, snow/wind loads |
| Ceiling Space | Unconditioned | VAV boxes, FCUs, piping | Access for maintenance |
| Interstitial Space | Unconditioned | Major ductwork and piping | Coordinated ceiling height |

### 5.2 Outdoor Locations
| Location Type | Exposure | Typical Equipment | Special Requirements |
|--------------|----------|------------------|---------------------|
| Rooftop | Full weather exposure | RTUs, exhaust fans, condensing units | NEMA 3R, seismic/wind rated, roof penetration flashing |
| Ground Level - Equipment Pad | Ground exposure | Transformers, generators, condensing units | Concrete pad, NEMA 3R, fence/bollards |
| Remote Site | Full weather exposure | Pad-mounted transformers, cooling towers | Utility access, drainage |

### 5.3 Hazardous Locations (NEC Article 500)
| Class/Division | Hazard Type | Typical Locations | Equipment Requirements |
|---------------|------------|------------------|----------------------|
| Class I, Division 1 | Flammable gases/vapors continuously present | Spray booths, fuel dispensing | Explosion-proof equipment |
| Class I, Division 2 | Flammable gases/vapors under abnormal conditions | Adjacent to Class I, Div 1 | Enclosed equipment |
| Class II | Combustible dust | Grain elevators, flour mills | Dust-ignition-proof equipment |
| Class III | Ignitable fibers | Textile mills, woodworking | Enclosed equipment |

---

## 6. Equipment Tag Naming Conventions

### 6.1 Standard Tag Format
```
[SYSTEM PREFIX]-[EQUIPMENT TYPE]-[SEQUENCE NUMBER]-[LOCATION SUFFIX]
```

**Example:** CHW-P-01-B2 = Chilled Water Pump #01, Basement Level 2

### 6.2 System Prefixes
| Prefix | System | Example Equipment |
|--------|--------|------------------|
| CHW | Chilled Water | CHW-P-01 (Chilled Water Pump #1) |
| HW | Hot Water | HW-P-01 (Hot Water Pump #1) |
| CW | Condenser Water | CW-P-01 (Condenser Water Pump #1) |
| DW | Domestic Water | DW-P-01 (Domestic Water Booster Pump #1) |
| SS | Sanitary Sewer | SS-P-01 (Sewage Ejector Pump #1) |
| SD | Storm Drain | SD-P-01 (Sump Pump #1) |
| SA | Supply Air | SA-1 (Supply Air AHU #1) |
| RA | Return Air | RA-1 (Return Air Fan #1) |
| EA | Exhaust Air | EA-1 (Exhaust Fan #1) |
| FP | Fire Protection | FP-RISER-01 (Fire Sprinkler Riser #1) |

### 6.3 Equipment Type Abbreviations
| Abbreviation | Equipment Type | Example Tag |
|-------------|---------------|-------------|
| AHU | Air Handling Unit | AHU-01 |
| RTU | Rooftop Unit | RTU-01 |
| MAU | Makeup Air Unit | MAU-01 |
| EF | Exhaust Fan | EF-01 |
| ERV | Energy Recovery Ventilator | ERV-01 |
| BLR | Boiler | BLR-01 |
| CHL | Chiller | CHL-01 |
| CT | Cooling Tower | CT-01 |
| CU | Condensing Unit | CU-01 |
| P | Pump | CHW-P-01 |
| VAV | Variable Air Volume Box | VAV-101 |
| FCU | Fan Coil Unit | FCU-101 |
| UH | Unit Heater | UH-01 |
| WH | Water Heater | WH-01 |
| T | Transformer | T-01 |
| GEN | Generator | GEN-01 |
| UPS | Uninterruptible Power Supply | UPS-01 |
| ATS | Automatic Transfer Switch | ATS-01 |

### 6.4 Location Suffixes
| Suffix | Location | Example |
|--------|----------|---------|
| -RF | Roof | RTU-01-RF |
| -B1 | Basement Level 1 | AHU-01-B1 |
| -B2 | Basement Level 2 | BLR-01-B2 |
| -01 | First Floor | FCU-101-01 |
| -02 | Second Floor | FCU-201-02 |
| -PH | Penthouse | EF-01-PH |
| -EXT | Exterior | T-01-EXT |

### 6.5 Panel Naming Conventions
| Panel Type | Prefix | Example | Voltage |
|-----------|--------|---------|---------|
| Main Distribution Panel | MDP | MDP | 480V |
| Lighting Panel | LP | LP-1A, LP-2B | 120/208V, 277/480V |
| Power Panel | PP | PP-1A, PP-2B | 120/208V, 208V, 480V |
| Emergency Panel | EM | EM-1, EM-2 | 120/208V |
| Equipment Panel | EP | EP-MER (Mechanical Equipment Room) | Varies |
| Fire Alarm Panel | FACP | FACP-1 | 120V input, 24V output |

---

## 7. Equipment Attribute Schema

### 7.1 Electrical Equipment Attributes
| Attribute | Data Type | Units | Required | Validation Rules |
|-----------|-----------|-------|----------|-----------------|
| Voltage | Numeric | V | Yes | Standard voltage: 120, 208, 240, 277, 480, 600, 4160, 13800 |
| Phases | Integer | - | Yes | 1 or 3 |
| Full Load Amps (FLA) | Numeric | A | Yes (motors) | > 0 |
| Min Circuit Ampacity (MCA) | Numeric | A | Yes (equipment) | > 0 |
| Max Overcurrent Protection (MOP) | Numeric | A | Yes (equipment) | ≥ MCA |
| Short Circuit Rating | Numeric | kA | Yes (panels/switchgear) | 10, 22, 25, 42, 65, 100 kA |
| Main Breaker Size | Numeric | A | Yes (panels) | Standard breaker sizes |
| Bus Rating | Numeric | A | Yes (panels/switchgear) | 100, 200, 400, 600, 800, 1000, 1200, 1600, 2000, 2500, 3000, 4000 A |
| kVA Rating | Numeric | kVA | Yes (transformers/UPS) | > 0 |
| Efficiency | Percentage | % | Optional | 0-100% |

### 7.2 Mechanical Equipment Attributes
| Attribute | Data Type | Units | Required | Validation Rules |
|-----------|-----------|-------|----------|-----------------|
| CFM (Airflow) | Numeric | CFM | Yes (air-moving equipment) | > 0 |
| ESP (External Static Pressure) | Numeric | in. w.c. | Yes (fans/AHUs) | > 0 |
| Heating Capacity | Numeric | MBH or kW | Optional | > 0 |
| Cooling Capacity | Numeric | Tons or MBH | Optional | > 0 |
| Motor Horsepower (HP) | Numeric | HP | Yes (if motor-driven) | 0.25, 0.33, 0.5, 0.75, 1, 1.5, 2, 3, 5, 7.5, 10, 15, 20, 25, 30, 40, 50, 60, 75, 100 |
| GPM (Flow Rate) | Numeric | GPM | Yes (pumps) | > 0 |
| Head (Pressure) | Numeric | ft or PSI | Yes (pumps) | > 0 |
| Efficiency (Motor) | Percentage | % | Optional | 0-100%, specify NEMA Premium or IE3 |
| Sound Level | Numeric | dB(A) | Optional | Typical range 50-85 dB(A) |
| Weight (Operating) | Numeric | lbs | Optional | For structural coordination |

### 7.3 Plumbing Equipment Attributes
| Attribute | Data Type | Units | Required | Validation Rules |
|-----------|-----------|-------|----------|-----------------|
| Water Heater Capacity | Numeric | Gallons | Yes (tank water heaters) | Standard: 30, 40, 50, 80, 100, 120 |
| Recovery Rate | Numeric | GPH | Yes (tank water heaters) | > 0, verify adequate for demand |
| BTU Input | Numeric | BTU/hr | Yes (gas water heaters) | > 0 |
| kW Rating | Numeric | kW | Yes (electric water heaters) | > 0 |
| GPM Rating | Numeric | GPM | Yes (tankless water heaters) | > 0 at specified temp rise |
| Pressure Rating | Numeric | PSI | Yes (piping/valves) | 125, 150, 250, 300 PSI typical |
| Temperature Rating | Numeric | °F | Yes (water heaters) | Max 180°F typical |
| Fuel Type | Enumeration | - | Yes (gas equipment) | Natural Gas, Propane, Oil, Electric |

### 7.4 Fire Protection Equipment Attributes
| Attribute | Data Type | Units | Required | Validation Rules |
|-----------|-----------|-------|----------|-----------------|
| Flow Rate | Numeric | GPM | Yes (fire pumps) | Verify adequate for system demand |
| Discharge Pressure | Numeric | PSI | Yes (fire pumps) | Verify adequate for highest head |
| Suction Pressure | Numeric | PSI | Yes (fire pumps) | > 0 (or negative if suction lift) |
| Motor HP | Numeric | HP | Yes (electric fire pumps) | Sized per NFPA 20 |
| Sprinkler K-Factor | Numeric | - | Yes (sprinkler heads) | 5.6, 8.0, 11.2, 14.0, 16.8, 25.2 |
| Temperature Rating | Numeric | °F | Yes (sprinkler heads) | 135, 155, 175, 200, 286 |
| Response Type | Enumeration | - | Yes (sprinkler heads) | Standard, Quick, Special |
| Coverage Area | Numeric | sqft | Yes (sprinkler heads) | Max per NFPA 13 (130, 168, 225 sqft typical) |

---

## 8. Equipment Schedule Templates

### 8.1 Electrical Panel Schedule
| Panel ID | Location | Voltage | Phases | Main Breaker | Bus Rating | AIC | Mounting | Notes |
|---------|----------|---------|--------|-------------|-----------|-----|----------|-------|
| LP-1A | 1st Floor Elec Room | 120/208V | 3 | 225A | 225A | 22kA | Surface | Lighting - North Wing |
| PP-1A | 1st Floor Elec Room | 120/208V | 3 | 225A | 225A | 22kA | Surface | Receptacles - North Wing |
| EM-1 | Generator Room | 120/208V | 3 | 100A | 100A | 22kA | Surface | Emergency/Life Safety |

### 8.2 Mechanical Equipment Schedule
| Equipment Tag | Type | Location | CFM | ESP | Heating | Cooling | Motor HP | Sound | Weight | Notes |
|--------------|------|----------|-----|-----|---------|---------|----------|-------|--------|-------|
| AHU-01 | Air Handling Unit | Penthouse | 15,000 | 3.5 in.wc | 450 MBH HW | 300 MBH CHW | 15 HP | 68 dB(A) | 3,500 lbs | Serves Floors 1-3 |
| RTU-01 | Rooftop Unit | Roof | 5,000 | 1.0 in.wc | 300 MBH Gas | 10 Tons | 7.5 HP | 72 dB(A) | 1,800 lbs | Serves Floor 4 |

### 8.3 Plumbing Equipment Schedule
| Equipment Tag | Type | Location | Capacity | Fuel | GPH Recovery | Input | Efficiency | Notes |
|--------------|------|----------|----------|------|-------------|-------|-----------|-------|
| WH-01 | Storage Water Heater | Mechanical Room | 80 Gal | Natural Gas | 80 GPH | 75,000 BTU/hr | 0.67 EF | Domestic hot water |
| WH-02 | Tankless Water Heater | Kitchenette | N/A | Natural Gas | N/A | 199,000 BTU/hr | 0.95 EF | Local DHW boost |

### 8.4 Fire Sprinkler Head Schedule
| Head Type | Model | K-Factor | Temperature | Finish | Coverage | Application |
|----------|-------|----------|-------------|--------|----------|-------------|
| Pendent | Viking VK302 | 5.6 | 155°F | Chrome | 130 sqft | Light Hazard |
| Upright | Viking VK102 | 5.6 | 155°F | Brass | 130 sqft | Mech Room |
| Sidewall | Viking VK450 | 5.6 | 155°F | White | Extended | Corridors |

---

## 9. Equipment Interrelationships

### 9.1 Dependency Matrix
| Parent Equipment | Child Equipment | Relationship Type | Interface |
|-----------------|----------------|------------------|-----------|
| Chiller | Chilled Water Pumps | Served By | Piping system |
| Chiller | Cooling Tower | Heat Rejection | Condenser water piping |
| AHU | VAV Boxes | Distribution | Supply ductwork |
| Boiler | Hot Water Pumps | Served By | Piping system |
| Generator | Automatic Transfer Switch | Power Source | Electrical feeders |
| ATS | Emergency Panels | Distribution | Electrical feeders |
| Fire Alarm Control Panel | Smoke Detectors | Monitoring | Class A/B wiring |
| Water Heater | Recirculation Pump | Circulation | Hot water return piping |
| Fire Pump | Fire Sprinkler Riser | Supply | Fire main piping |

### 9.2 Control Relationships
| Controlled Equipment | Controller | Control Signal | Actuator/Device |
|---------------------|-----------|---------------|----------------|
| AHU Supply Fan | DDC Controller | VFD | Variable Frequency Drive |
| Chilled Water Valve | DDC Controller | 0-10VDC or 4-20mA | 2-way modulating valve |
| VAV Damper | VAV Controller | 0-10VDC or 4-20mA | Damper actuator |
| Boiler | Boiler Controller | On/Off or Modulating | Gas valve, burner |

---

## 10. Validation Rules for Equipment Data

### 10.1 Electrical Equipment Validation
- **Voltage:** Must be standard voltage (120, 208, 240, 277, 480, 600, 4160, 13800V)
- **Phase:** Must be 1 or 3
- **Panel circuits:** Total circuit breaker amperage should not exceed 80% of main breaker rating
- **MCA/MOP:** MOP must be ≥ MCA
- **AIC Rating:** Must be ≥ available fault current at installation location

### 10.2 Mechanical Equipment Validation
- **Motor HP vs. CFM:** Verify fan HP is adequate for CFM and ESP
- **Pump HP vs. GPM:** Verify pump HP is adequate for GPM and head
- **Heating capacity:** Verify adequate for design heating load
- **Cooling capacity:** Verify adequate for design cooling load
- **Sound levels:** Verify compliance with space sound criteria (NC/RC curves)

### 10.3 Plumbing Equipment Validation
- **Water heater recovery:** Verify GPH recovery adequate for fixture demand
- **Pressure rating:** Verify adequate for system pressure + safety factor
- **Temperature rating:** Verify compatible with system design temperature
- **Fuel gas sizing:** Verify BTU input does not exceed gas service capacity

### 10.4 Fire Protection Equipment Validation
- **Sprinkler coverage:** Verify coverage area does not exceed NFPA 13 maximums
- **K-factor selection:** Verify adequate for design density and pressure
- **Temperature rating:** Verify compatible with space ambient temperature
- **Fire pump flow:** Verify adequate for most remote area demand + hose allowance

---

## 11. Conclusion

This equipment classification system provides:
- **Standardized taxonomy** for all MEP equipment types
- **Consistent naming conventions** for equipment tags
- **Comprehensive attribute schema** for equipment specifications
- **Validation rules** for data quality assurance
- **Interrelationship mapping** for system coordination

This classification system enables automated equipment validation, schedule generation, and interdisciplinary coordination throughout the engineering drawing QA/QC process.
