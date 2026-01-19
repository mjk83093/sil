# IFC MEP Entity Mapping Guide

**Document Version**: 2.0
**Agent**: IFC Schema Specialist
**Last Updated**: 2025-10-22
**Integration Point**: Maps IFC entities to SKILL.md JSON schema (symbols, equipment, schedules)

---

## Executive Summary

This document provides comprehensive mapping between IFC (Industry Foundation Classes) schema entities and MEP (Mechanical, Electrical, Plumbing) systems. It enables accurate data extraction from BIM models for QA/QC validation workflows, ensuring seamless integration with the `engineering-drawing-qaqc` skill.

**Covered IFC Versions:**
- IFC 2x3 (legacy, limited support)
- IFC4 (primary)
- IFC4.3 (latest, enhanced MEP support)

**Key Use Cases:**
1. Export MEP equipment data from Revit/ArchiCAD for JSON validation
2. Map property sets to QA rule target fields
3. Extract schedule data for completeness checks
4. Validate symbol-legend consistency from BIM models

---

## Table of Contents

1. [IFC Schema Overview](#ifc-schema-overview)
2. [Electrical Systems Entity Mapping](#electrical-systems-entity-mapping)
3. [Mechanical Systems Entity Mapping](#mechanical-systems-entity-mapping)
4. [Plumbing Systems Entity Mapping](#plumbing-systems-entity-mapping)
5. [Fire Protection Entity Mapping](#fire-protection-entity-mapping)
6. [Property Sets (Psets)](#property-sets-psets)
7. [Quantity Sets (Qtos)](#quantity-sets-qtos)
8. [IFC Extraction from BIM Tools](#ifc-extraction-from-bim-tools)
9. [IFC to JSON Mapping for QA Validation](#ifc-to-json-mapping-for-qa-validation)
10. [Integration with SKILL.md Workflow](#integration-with-skillmd-workflow)

---

## IFC Schema Overview

### IFC Hierarchy and Structure

IFC defines a hierarchical object model for building information:

```
IfcRoot (abstract)
├── IfcObjectDefinition (abstract)
│   ├── IfcObject (abstract)
│   │   ├── IfcProduct (abstract)
│   │   │   ├── IfcElement (abstract)
│   │   │   │   ├── IfcBuildingElement
│   │   │   │   ├── IfcDistributionElement (MEP base class)
│   │   │   │   │   ├── IfcDistributionControlElement
│   │   │   │   │   ├── IfcDistributionFlowElement
│   │   │   │   │   │   ├── IfcFlowTerminal
│   │   │   │   │   │   ├── IfcFlowSegment
│   │   │   │   │   │   ├── IfcFlowFitting
│   │   │   │   │   │   └── IfcFlowController
```

### Core MEP Base Classes

**IfcDistributionElement**
- Abstract base class for all MEP components
- Inherited by control elements (sensors, controllers) and flow elements (pipes, ducts)

**IfcDistributionControlElement**
- Controls distribution systems (sensors, actuators, alarms, controllers)
- Examples: thermostats, fire alarm devices, BAS controllers

**IfcDistributionFlowElement**
- Transports fluids, air, or electricity
- Four main subcategories:
  - **IfcFlowTerminal**: End devices (outlets, diffusers, fixtures)
  - **IfcFlowSegment**: Linear connectors (pipes, ducts, cables)
  - **IfcFlowFitting**: Connectors and transitions (elbows, tees, reducers)
  - **IfcFlowController**: Flow regulation (dampers, valves, switches)

### Entity Naming Convention

IFC4 naming pattern:
```
Ifc[System][Component][Type]

Examples:
- IfcElectricDistributionBoard → Electrical system, distribution board component
- IfcAirTerminal → HVAC system, air terminal component
- IfcSanitaryTerminal → Plumbing system, sanitary fixture component
```

### Type Objects vs. Occurrences

IFC distinguishes between **type definitions** (shared properties) and **occurrences** (instances):

```
IfcElectricDistributionBoardType (Type)
├── Properties shared across all instances:
│   ├── Manufacturer: "Square D"
│   ├── Model: "NQOD430M100"
│   └── Voltage Rating: 208V
└── Instances (IfcElectricDistributionBoard):
    ├── LP-1 (Ground Floor, Electrical Room 101)
    ├── LP-2 (Second Floor, Electrical Room 201)
    └── LP-3 (Roof, Penthouse)
```

**Type Object**: Defines shared characteristics (IfcElectricDistributionBoardType)
**Occurrence**: Specific instance placed in model (IfcElectricDistributionBoard)

### Property Sets and Quantity Sets

**Property Sets (Pset_*)**: Non-geometric attributes
- `Pset_ElectricalDeviceCommon`: Voltage, current, power factor
- `Pset_AirTerminalTypeCommon`: Airflow rate, throw distance

**Quantity Sets (Qto_*)**: Measurable quantities
- `Qto_PipeFittingBaseQuantities`: Length, weight, surface area
- `Qto_DuctFittingBaseQuantities`: Cross-sectional area, volume

---

## Electrical Systems Entity Mapping

### IfcElectricDistributionBoard

**Purpose**: Panelboards, distribution boards, load centers
**IFC4 Class**: IfcElectricDistributionBoard (subtype of IfcFlowController)
**IFC4.3 Enhancement**: Added `PredefinedType` attribute

**Attributes:**
| IFC Attribute | Type | Description | Example Value |
|---------------|------|-------------|---------------|
| GlobalId | IfcGloballyUniqueId | Unique identifier | "2XbR$6fTj9QvhP4n0Z8I5D" |
| Name | IfcLabel | User-defined name | "LP-1" |
| Description | IfcText | Additional description | "Main Lighting Panel - Ground Floor" |
| ObjectType | IfcLabel | User type designation | "Lighting Panelboard" |
| PredefinedType | IfcElectricDistributionBoardTypeEnum | Standard type | DISTRIBUTIONBOARD |

**PredefinedType Enum Values:**
- `CONSUMERUNIT`: Residential service panel
- `DISTRIBUTIONBOARD`: Commercial distribution panel
- `MOTORCONTROLCENTRE`: MCC for motor loads
- `SWITCHBOARD`: Main switchboard
- `USERDEFINED`: Custom type
- `NOTDEFINED`: Not specified

**Property Sets:**
```
Pset_ElectricalDeviceCommon:
- Manufacturer: IfcLabel → "Square D"
- ModelReference: IfcIdentifier → "NQOD430M100"
- NominalVoltageAC: IfcElectricVoltageMeasure → 208 V
- NominalFrequency: IfcFrequencyMeasure → 60 Hz
- PowerFactor: IfcNormalisedRatioMeasure → 0.95

Pset_ElectricDistributionBoard (custom):
- MainBreakerRating: IfcElectricCurrentMeasure → 100 A
- PhaseReference: IfcLabel → "3-phase, 4-wire"
- ShortCircuitRating: IfcElectricCurrentMeasure → 22000 AIC
- BusBarMaterial: IfcLabel → "Copper"
- EnclosureType: IfcLabel → "NEMA 1"
```

**Mapping to SKILL.md JSON:**
```json
{
  "schedules": {
    "panel_schedule": {
      "panel_id": "LP-1",
      "voltage": 120/208,
      "phases": 3,
      "main_breaker": "100A",
      "manufacturer": "Square D",
      "model": "NQOD430M100",
      "short_circuit_rating": 22000,
      "enclosure_type": "NEMA 1"
    }
  }
}
```

### IfcOutlet

**Purpose**: Electrical receptacles, outlets, convenience outlets
**IFC4 Class**: IfcOutlet (subtype of IfcFlowTerminal)

**Attributes:**
| IFC Attribute | Type | Description | Example Value |
|---------------|------|-------------|---------------|
| Name | IfcLabel | Outlet identifier | "R1" |
| ObjectType | IfcLabel | User type | "Duplex Receptacle" |
| PredefinedType | IfcOutletTypeEnum | Standard type | POWEROUTLET |

**PredefinedType Enum Values:**
- `AUDIOVISUALOUTLET`: AV outlet
- `COMMUNICATIONSOUTLET`: Data/telecom outlet
- `DATAOUTLET`: Network data outlet
- `POWEROUTLET`: Standard electrical receptacle
- `TELEPHONEOUTLET`: Phone jack
- `USERDEFINED`: Custom type
- `NOTDEFINED`: Not specified

**Property Sets:**
```
Pset_ElectricalDeviceCommon:
- NominalVoltageAC: 120 V
- NominalCurrentAC: 20 A
- NumberOfPoles: 2 (duplex)

Pset_Outlet (custom):
- CircuitReference: IfcLabel → "A1"
- MountingHeight: IfcLengthMeasure → 18 inches AFF
- WeatherResistant: IfcBoolean → False
- GFCIProtection: IfcBoolean → False
```

**Mapping to SKILL.md JSON:**
```json
{
  "legend": [
    {
      "symbol_id": "R1",
      "description": "Duplex Receptacle, 120V, 20A",
      "type": "receptacle"
    }
  ],
  "symbols": [
    {
      "class": "receptacle",
      "tag": "R1",
      "location": {"x": 100, "y": 200},
      "circuit": "A1",
      "height_aff": "18\"",
      "quantity": 1
    }
  ]
}
```

### IfcLightFixture

**Purpose**: Lighting fixtures, luminaires
**IFC4 Class**: IfcLightFixture (subtype of IfcFlowTerminal)

**Attributes:**
| IFC Attribute | Type | Description | Example Value |
|---------------|------|-------------|---------------|
| Name | IfcLabel | Fixture tag | "D1" |
| ObjectType | IfcLabel | User type | "LED Troffer" |
| PredefinedType | IfcLightFixtureTypeEnum | Standard type | DIRECTIONSOURCE |

**PredefinedType Enum Values:**
- `DIRECTIONSOURCE`: Directional lighting
- `POINTSOURCE`: Point source (downlights)
- `SECURITYLIGHTING`: Security/emergency lighting
- `USERDEFINED`: Custom type
- `NOTDEFINED`: Not specified

**Property Sets:**
```
Pset_LightFixtureTypeCommon:
- LampBallastType: IfcLabel → "Electronic Ballast"
- LightEmitterNominalPower: IfcPowerMeasure → 35 W
- ColorTemperature: IfcThermodynamicTemperatureMeasure → 3500 K
- LuminousFlux: IfcLuminousFluxMeasure → 3500 lumens
- ColorRenderingIndex: IfcInteger → 85

Pset_LightFixture (custom):
- CircuitReference: IfcLabel → "A1"
- MountingType: IfcLabel → "Recessed"
- LensType: IfcLabel → "Prismatic"
- ControlType: IfcLabel → "Dimming 0-10V"
```

**Mapping to SKILL.md JSON:**
```json
{
  "legend": [
    {
      "symbol_id": "D1",
      "description": "2x2 LED Troffer, 3500K, 3500 lumens",
      "type": "lighting_fixture"
    }
  ],
  "symbols": [
    {
      "class": "lighting_fixture",
      "tag": "D1",
      "location": {"x": 125, "y": 340},
      "circuit": "A1",
      "quantity": 1
    }
  ]
}
```

### IfcCableCarrierFitting

**Purpose**: Conduit fittings, cable tray fittings, junction boxes
**IFC4 Class**: IfcCableCarrierFitting (subtype of IfcFlowFitting)

**Attributes:**
| IFC Attribute | Type | Description | Example Value |
|---------------|------|-------------|---------------|
| ObjectType | IfcLabel | Fitting type | "EMT Conduit Elbow" |
| PredefinedType | IfcCableCarrierFittingTypeEnum | Standard type | BEND |

**PredefinedType Enum Values:**
- `BEND`: Elbow or sweep
- `CONNECTOR`: Coupling or connector
- `CROSS`: Four-way intersection
- `JUNCTION`: Junction box
- `REDUCER`: Size transition
- `TEE`: T-fitting
- `TRANSITION`: Material or type transition
- `USERDEFINED`: Custom type
- `NOTDEFINED`: Not specified

**Property Sets:**
```
Pset_CableCarrierFittingTypeCommon:
- ConnectionType: IfcLabel → "Compression"
- ConduitSize: IfcLabel → "3/4 inch EMT"
- Material: IfcLabel → "Steel"

Qto_CableCarrierFittingBaseQuantities:
- Length: IfcLengthMeasure → 6 inches
- CrossSectionArea: IfcAreaMeasure → 0.5 sq in
```

### IfcCableSegment

**Purpose**: Electrical cables, wires, conductors
**IFC4 Class**: IfcCableSegment (subtype of IfcFlowSegment)

**Attributes:**
| IFC Attribute | Type | Description | Example Value |
|---------------|------|-------------|---------------|
| ObjectType | IfcLabel | Cable type | "THHN Copper Conductor" |
| PredefinedType | IfcCableSegmentTypeEnum | Standard type | CONDUCTORSEGMENT |

**PredefinedType Enum Values:**
- `BUSBARSEGMENT`: Busbar conductor
- `CABLESEGMENT`: Multi-conductor cable
- `CONDUCTORSEGMENT`: Single conductor
- `CORESEGMENT`: Cable core
- `USERDEFINED`: Custom type
- `NOTDEFINED`: Not specified

**Property Sets:**
```
Pset_CableSegmentTypeCommon:
- ConductorMaterial: IfcLabel → "Copper"
- InsulationMaterial: IfcLabel → "THHN"
- TemperatureRating: IfcThermodynamicTemperatureMeasure → 90°C
- VoltageRating: IfcElectricVoltageMeasure → 600 V
- Ampacity: IfcElectricCurrentMeasure → 20 A

Qto_CableSegmentBaseQuantities:
- Length: IfcLengthMeasure → 150 ft
- CrossSectionArea: IfcAreaMeasure → 3310 cmil (12 AWG)
- NetWeight: IfcMassMeasure → 15 lbs
```

### IfcSwitchingDevice

**Purpose**: Switches, breakers, disconnects, contactors
**IFC4 Class**: IfcSwitchingDevice (subtype of IfcFlowController)

**Attributes:**
| IFC Attribute | Type | Description | Example Value |
|---------------|------|-------------|---------------|
| ObjectType | IfcLabel | Device type | "Miniature Circuit Breaker" |
| PredefinedType | IfcSwitchingDeviceTypeEnum | Standard type | CIRCUITBREAKER |

**PredefinedType Enum Values:**
- `CIRCUITBREAKER`: Thermal or magnetic trip breaker
- `CONTACTOR`: Electromagnetic contactor
- `DIMMERSWITCH`: Lighting dimmer
- `EMERGENCYSTOP`: E-stop button
- `KEYPAD`: Multi-button control
- `MOMENTARYSWITCH`: Push-button
- `SELECTORSWITCH`: Rotary selector
- `STARTER`: Motor starter
- `SWITCHDISCONNECTOR`: Disconnect switch
- `TOGGLESWITCH`: Toggle or rocker switch
- `USERDEFINED`: Custom type
- `NOTDEFINED`: Not specified

**Property Sets:**
```
Pset_SwitchingDeviceTypeCommon:
- NumberOfPoles: IfcInteger → 1
- SwitchFunction: IfcLabel → "Overcurrent Protection"
- HasLock: IfcBoolean → False
- IsIlluminated: IfcBoolean → False

Pset_CircuitBreaker (custom):
- BreakerRating: IfcElectricCurrentMeasure → 20 A
- InterruptingCapacity: IfcElectricCurrentMeasure → 10000 AIC
- TripCurveType: IfcLabel → "Type C"
- InstantaneousTripSetting: IfcElectricCurrentMeasure → 200 A
```

---

## Mechanical Systems Entity Mapping

### IfcAirTerminal

**Purpose**: Diffusers, grilles, registers
**IFC4 Class**: IfcAirTerminal (subtype of IfcFlowTerminal)

**Attributes:**
| IFC Attribute | Type | Description | Example Value |
|---------------|------|-------------|---------------|
| Name | IfcLabel | Diffuser tag | "SD1" |
| ObjectType | IfcLabel | User type | "Supply Diffuser" |
| PredefinedType | IfcAirTerminalTypeEnum | Standard type | DIFFUSER |

**PredefinedType Enum Values:**
- `DIFFUSER`: Supply diffuser
- `GRILLE`: Return or exhaust grille
- `LOUVRE`: Fixed or operable louver
- `REGISTER`: Adjustable register
- `USERDEFINED`: Custom type
- `NOTDEFINED`: Not specified

**Property Sets:**
```
Pset_AirTerminalTypeCommon:
- AirFlowrateRange: IfcVolumetricFlowRateMeasure → 400-800 CFM
- TemperatureRange: IfcThermodynamicTemperatureMeasure → 55-75°F
- NominalAirFlowRate: IfcVolumetricFlowRateMeasure → 800 CFM
- AirDiffusionPerformanceIndex: IfcReal → 80
- Finish: IfcLabel → "White Powder Coat"

Pset_AirTerminal (custom):
- NeckSize: IfcLabel → "12 inch round"
- ThrowDistance: IfcLengthMeasure → 15 ft
- NumberOfWays: IfcInteger → 4 (4-way diffuser)
- ZoneReference: IfcLabel → "Zone-1A"
```

**Mapping to SKILL.md JSON:**
```json
{
  "legend": [
    {
      "symbol_id": "SD1",
      "description": "24\"x24\" Supply Diffuser, 4-way, 800 CFM",
      "type": "diffuser"
    }
  ],
  "symbols": [
    {
      "class": "diffuser",
      "tag": "SD1",
      "location": {"x": 200, "y": 300},
      "zone": "Zone-1A",
      "cfm": 800
    }
  ],
  "schedules": {
    "diffuser_schedule": [
      {
        "tag": "SD1",
        "type": "Supply",
        "size": "24x24",
        "cfm": 800,
        "throw": "15 ft",
        "neck_size": "12\" round"
      }
    ]
  }
}
```

### IfcDuctSegment

**Purpose**: Ductwork, air distribution piping
**IFC4 Class**: IfcDuctSegment (subtype of IfcFlowSegment)

**Attributes:**
| IFC Attribute | Type | Description | Example Value |
|---------------|------|-------------|---------------|
| ObjectType | IfcLabel | Duct type | "Rectangular Duct" |
| PredefinedType | IfcDuctSegmentTypeEnum | Standard type | RIGIDSEGMENT |

**PredefinedType Enum Values:**
- `RIGIDSEGMENT`: Rigid duct (galvanized steel, aluminum)
- `FLEXIBLESEGMENT`: Flexible duct
- `USERDEFINED`: Custom type
- `NOTDEFINED`: Not specified

**Property Sets:**
```
Pset_DuctSegmentTypeCommon:
- WorkingPressure: IfcPressureMeasure → 2 inches w.g.
- PressureClass: IfcLabel → "Low Pressure"
- Material: IfcLabel → "Galvanized Steel"
- InsulationThickness: IfcLengthMeasure → 1 inch
- InsulationMaterial: IfcLabel → "Fiberglass"

Qto_DuctSegmentBaseQuantities:
- Length: IfcLengthMeasure → 10 ft
- CrossSectionArea: IfcAreaMeasure → 2 sq ft (24" x 12")
- OuterSurfaceArea: IfcAreaMeasure → 72 sq ft
- NetWeight: IfcMassMeasure → 85 lbs
```

### IfcChiller

**Purpose**: Chillers, cooling equipment
**IFC4 Class**: IfcChiller (subtype of IfcEnergyConversionDevice)

**Attributes:**
| IFC Attribute | Type | Description | Example Value |
|---------------|------|-------------|---------------|
| Name | IfcLabel | Chiller tag | "CH-1" |
| ObjectType | IfcLabel | User type | "Water-Cooled Chiller" |
| PredefinedType | IfcChillerTypeEnum | Standard type | WATERCOOLED |

**PredefinedType Enum Values:**
- `AIRCOOLED`: Air-cooled chiller
- `WATERCOOLED`: Water-cooled chiller
- `HEATRECOVERY`: Heat recovery chiller
- `USERDEFINED`: Custom type
- `NOTDEFINED`: Not specified

**Property Sets:**
```
Pset_ChillerTypeCommon:
- NominalCapacity: IfcPowerMeasure → 500 tons (1758 kW)
- NominalEfficiency: IfcNormalisedRatioMeasure → 0.58 kW/ton
- RefrigerantClass: IfcLabel → "HFC-134a"
- CompressorType: IfcLabel → "Centrifugal"
- CondenserType: IfcLabel → "Water-Cooled"

Pset_Chiller_Performance (custom):
- CoolingCapacity_100Pct: 500 tons
- CoolingCapacity_75Pct: 380 tons
- CoolingCapacity_50Pct: 260 tons
- CoolingCapacity_25Pct: 135 tons
- EER_IPLV: IfcReal → 15.5 (Integrated Part Load Value)
```

### IfcPump

**Purpose**: Pumps (chilled water, hot water, condenser water)
**IFC4 Class**: IfcPump (subtype of IfcFlowMovingDevice)

**Attributes:**
| IFC Attribute | Type | Description | Example Value |
|---------------|------|-------------|---------------|
| Name | IfcLabel | Pump tag | "P-1" |
| ObjectType | IfcLabel | User type | "Chilled Water Pump" |
| PredefinedType | IfcPumpTypeEnum | Standard type | CIRCULATOR |

**PredefinedType Enum Values:**
- `CIRCULATOR`: Small circulating pump
- `ENDSUCTION`: End-suction centrifugal pump
- `SPLITCASE`: Split-case centrifugal pump
- `SUBMERSIBLEPUMP`: Submersible pump
- `SUMPPUMP`: Sump pump
- `VERTICALINLINE`: Vertical inline pump
- `VERTICALTURBINE`: Vertical turbine pump
- `USERDEFINED`: Custom type
- `NOTDEFINED`: Not specified

**Property Sets:**
```
Pset_PumpTypeCommon:
- FlowRateRange: IfcVolumetricFlowRateMeasure → 0-500 GPM
- FlowResistanceRange: IfcPressureMeasure → 0-80 ft head
- NominalRotationSpeed: IfcRotationalFrequencyMeasure → 1750 RPM
- ImpellerDiameter: IfcLengthMeasure → 8 inches

Pset_Pump_Performance:
- PumpCurve: [Flow vs. Head data points]
- BestEfficiencyPoint_GPM: 400 GPM
- BestEfficiencyPoint_Head: 65 ft
- MotorPower: IfcPowerMeasure → 15 HP
- MotorEfficiency: 92%
```

### IfcFan

**Purpose**: Fans, blowers, air movers
**IFC4 Class**: IfcFan (subtype of IfcFlowMovingDevice)

**Attributes:**
| IFC Attribute | Type | Description | Example Value |
|---------------|------|-------------|---------------|
| Name | IfcLabel | Fan tag | "SF-1" |
| ObjectType | IfcLabel | User type | "Supply Fan" |
| PredefinedType | IfcFanTypeEnum | Standard type | CENTRIFUGALFORWARDCURVED |

**PredefinedType Enum Values:**
- `CENTRIFUGALAIRFOIL`: Airfoil blade centrifugal
- `CENTRIFUGALBACKWARDINCLINEDCURVED`: Backward inclined
- `CENTRIFUGALFORWARDCURVED`: Forward curved
- `CENTRIFUGALRADIAL`: Radial blade
- `PROPELLORAXIAL`: Propeller/axial fan
- `TUBEAXIAL`: Tube axial fan
- `VANEAXIAL`: Vane axial fan
- `USERDEFINED`: Custom type
- `NOTDEFINED`: Not specified

**Property Sets:**
```
Pset_FanTypeCommon:
- NominalAirFlowRate: IfcVolumetricFlowRateMeasure → 10000 CFM
- NominalStaticPressure: IfcPressureMeasure → 3 inches w.g.
- NominalRotationSpeed: IfcRotationalFrequencyMeasure → 1200 RPM
- NominalPowerRate: IfcPowerMeasure → 10 HP
- MotorDriveType: IfcLabel → "Belt Drive"

Pset_Fan_Performance:
- FanCurve: [CFM vs. Static Pressure data points]
- OperatingPoint_CFM: 10000 CFM
- OperatingPoint_StaticPressure: 3 inches w.g.
- FanEfficiency: 75%
```

---

## Plumbing Systems Entity Mapping

### IfcSanitaryTerminal

**Purpose**: Plumbing fixtures (sinks, toilets, urinals, floor drains)
**IFC4 Class**: IfcSanitaryTerminal (subtype of IfcFlowTerminal)

**Attributes:**
| IFC Attribute | Type | Description | Example Value |
|---------------|------|-------------|---------------|
| Name | IfcLabel | Fixture tag | "WC-1" |
| ObjectType | IfcLabel | User type | "Water Closet" |
| PredefinedType | IfcSanitaryTerminalTypeEnum | Standard type | WC |

**PredefinedType Enum Values:**
- `BATH`: Bathtub
- `BIDET`: Bidet
- `CISTERN`: Toilet cistern (tank)
- `DRINKINGFOUNTAIN`: Drinking fountain
- `SANITARYFOUNTAIN`: Floor-mounted sanitary fountain
- `SHOWER`: Shower
- `SINK`: Lavatory or sink
- `TOILETPAN`: Toilet bowl
- `URINAL`: Urinal
- `WASHHANDBASIN`: Hand washing basin
- `WC`: Complete water closet (tank + bowl)
- `WCSEAT`: Toilet seat only
- `USERDEFINED`: Custom type
- `NOTDEFINED`: Not specified

**Property Sets:**
```
Pset_SanitaryTerminalTypeCommon:
- Mounting: IfcLabel → "Floor-Mounted"
- Color: IfcLabel → "White"
- Material: IfcLabel → "Vitreous China"
- DrainSize: IfcLabel → "3 inch"

Pset_SanitaryTerminal_WC (custom):
- FlushVolume: IfcVolumeMeasure → 1.28 gallons (WaterSense)
- FlushType: IfcLabel → "Dual Flush"
- TrapType: IfcLabel → "P-Trap"
- RoughInDistance: IfcLengthMeasure → 12 inches
```

**Mapping to SKILL.md JSON:**
```json
{
  "schedules": {
    "plumbing_fixture_schedule": [
      {
        "tag": "WC-1",
        "type": "Water Closet",
        "manufacturer": "Kohler",
        "model": "K-3999",
        "mounting": "Floor",
        "flush_volume": "1.28 GPF",
        "drain_size": "3 inch"
      }
    ]
  }
}
```

### IfcPipeSegment

**Purpose**: Plumbing piping (domestic water, sanitary, storm, gas)
**IFC4 Class**: IfcPipeSegment (subtype of IfcFlowSegment)

**Attributes:**
| IFC Attribute | Type | Description | Example Value |
|---------------|------|-------------|---------------|
| ObjectType | IfcLabel | Pipe type | "Copper Type L" |
| PredefinedType | IfcPipeSegmentTypeEnum | Standard type | RIGIDSEGMENT |

**PredefinedType Enum Values:**
- `CULVERT`: Culvert pipe
- `FLEXIBLESEGMENT`: Flexible pipe
- `GUTTER`: Gutter or downspout
- `RIGIDSEGMENT`: Rigid pipe
- `SPOOL`: Spool piece
- `USERDEFINED`: Custom type
- `NOTDEFINED`: Not specified

**Property Sets:**
```
Pset_PipeSegmentTypeCommon:
- WorkingPressure: IfcPressureMeasure → 150 PSI
- Material: IfcLabel → "Copper"
- PipeGrade: IfcLabel → "Type L"
- NominalDiameter: IfcLengthMeasure → 1 inch
- InsulationThickness: IfcLengthMeasure → 0.5 inch

Qto_PipeSegmentBaseQuantities:
- Length: IfcLengthMeasure → 20 ft
- CrossSectionArea: IfcAreaMeasure → 0.785 sq in
- OuterSurfaceArea: IfcAreaMeasure → 5.2 sq ft
- NetWeight: IfcMassMeasure → 12 lbs
```

### IfcPipeFitting

**Purpose**: Pipe fittings (elbows, tees, reducers, couplings)
**IFC4 Class**: IfcPipeFitting (subtype of IfcFlowFitting)

**Attributes:**
| IFC Attribute | Type | Description | Example Value |
|---------------|------|-------------|---------------|
| ObjectType | IfcLabel | Fitting type | "90° Elbow" |
| PredefinedType | IfcPipeFittingTypeEnum | Standard type | BEND |

**PredefinedType Enum Values:**
- `BEND`: Elbow or bend
- `CONNECTOR`: Coupling
- `ENTRY`: Pipe entry or boot
- `EXIT`: Pipe exit
- `JUNCTION`: Junction box or manifold
- `OBSTRUCTION`: Flow obstruction device
- `TRANSITION`: Transition fitting
- `USERDEFINED`: Custom type
- `NOTDEFINED`: Not specified

**Property Sets:**
```
Pset_PipeFittingTypeCommon:
- Material: IfcLabel → "Copper"
- ConnectionType: IfcLabel → "Soldered"
- NominalDiameter1: IfcLengthMeasure → 1 inch
- NominalDiameter2: IfcLengthMeasure → 1 inch (same for elbow)

Qto_PipeFittingBaseQuantities:
- Length: IfcLengthMeasure → 3 inches
- NetWeight: IfcMassMeasure → 0.5 lbs
```

### IfcValve

**Purpose**: Valves (isolation, control, check, pressure relief)
**IFC4 Class**: IfcValve (subtype of IfcFlowController)

**Attributes:**
| IFC Attribute | Type | Description | Example Value |
|---------------|------|-------------|---------------|
| Name | IfcLabel | Valve tag | "V-1" |
| ObjectType | IfcLabel | User type | "Gate Valve" |
| PredefinedType | IfcValveTypeEnum | Standard type | ISOLATING |

**PredefinedType Enum Values:**
- `AIRRELEASE`: Air release valve
- `ANTIVACUUM`: Anti-vacuum valve
- `CHANGEOVER`: Changeover valve
- `CHECK`: Check valve (one-way)
- `COMMISSIONING`: Test and balance valve
- `DIVERTING`: Diverting valve
- `DRAWOFFCOCK`: Hose bibb or spigot
- `DOUBLECHECK`: Double-check backflow preventer
- `DOUBLEREGULATING`: Double-regulating valve
- `FAUCET`: Faucet or tap
- `FLUSHING`: Flush valve
- `GASCOCK`: Gas shutoff valve
- `GASTAP`: Gas appliance connection
- `ISOLATING`: Isolation valve (gate, ball, butterfly)
- `MIXING`: Mixing valve (thermostatic, pressure)
- `PRESSUREREDUCING`: Pressure-reducing valve
- `PRESSURERELIEF`: Pressure relief valve
- `REGULATING`: Balancing or flow control valve
- `SAFETYCUTOFF`: Safety shutoff valve
- `STEAMTRAP`: Steam trap
- `STOPCOCK`: Stop valve
- `USERDEFINED`: Custom type
- `NOTDEFINED`: Not specified

**Property Sets:**
```
Pset_ValveTypeCommon:
- ValvePattern: IfcLabel → "Gate Valve"
- ValveOperation: IfcLabel → "Manual"
- ValveMechanism: IfcLabel → "Rising Stem"
- Size: IfcLengthMeasure → 2 inch
- CloseOffRating: IfcPressureMeasure → 150 PSI
- WorkingPressure: IfcPressureMeasure → 125 PSI

Pset_Valve_IsolatingValve:
- TestPressure: IfcPressureMeasure → 200 PSI
- Material_Body: IfcLabel → "Brass"
- EndConnection: IfcLabel → "Threaded"
```

---

## Fire Protection Entity Mapping

### IfcFireSuppressionTerminal

**Purpose**: Fire protection devices (sprinkler heads, hose connections)
**IFC4 Class**: IfcFireSuppressionTerminal (subtype of IfcFlowTerminal)

**Attributes:**
| IFC Attribute | Type | Description | Example Value |
|---------------|------|-------------|---------------|
| Name | IfcLabel | Device tag | "SH-1" |
| ObjectType | IfcLabel | User type | "Pendant Sprinkler" |
| PredefinedType | IfcFireSuppressionTerminalTypeEnum | Standard type | SPRINKLER |

**PredefinedType Enum Values:**
- `BREECHINGINLET`: Fire department connection inlet
- `FIREHYDRANT`: Fire hydrant
- `HOSEREEL`: Hose reel cabinet
- `SPRINKLER`: Automatic sprinkler head
- `SPRINKLERDEFLECTOR`: Sprinkler deflector only
- `USERDEFINED`: Custom type
- `NOTDEFINED`: Not specified

**Property Sets:**
```
Pset_FireSuppressionTerminalTypeSprinkler:
- SprinklerType: IfcLabel → "Pendent"
- TemperatureRating: IfcThermodynamicTemperatureMeasure → 165°F
- ResponseTime: IfcLabel → "Quick Response"
- KFactor: IfcReal → 5.6 (K-factor)
- OrificeDiameter: IfcLengthMeasure → 0.5 inch
- CoverageArea: IfcAreaMeasure → 225 sq ft

Pset_SprinklerHead (custom):
- Finish: IfcLabel → "Chrome"
- EscutcheonType: IfcLabel → "Recessed"
- PressureRating: IfcPressureMeasure → 175 PSI
- NFPACompliance: IfcLabel → "NFPA 13-2022"
```

**Mapping to SKILL.md JSON:**
```json
{
  "schedules": {
    "sprinkler_schedule": [
      {
        "tag": "SH-1",
        "type": "Pendent Sprinkler",
        "temperature_rating": "165°F",
        "response_time": "Quick Response",
        "k_factor": 5.6,
        "coverage_area": "225 sq ft",
        "finish": "Chrome"
      }
    ]
  }
}
```

### IfcPump (Fire Pump Application)

Fire pumps use the same `IfcPump` entity as HVAC pumps, differentiated by property sets:

**Property Sets:**
```
Pset_PumpTypeCommon:
- PredefinedType: ENDSUCTION or VERTICALINLINE
- FlowRateRange: IfcVolumetricFlowRateMeasure → 0-1500 GPM
- FlowResistanceRange: IfcPressureMeasure → 0-150 PSI

Pset_FirePump (custom):
- RatedFlowRate: IfcVolumetricFlowRateMeasure → 1250 GPM
- RatedPressure: IfcPressureMeasure → 125 PSI
- ChuteFlowTest: IfcVolumetricFlowRateMeasure → 1875 GPM @ 95 PSI
- MotorDriver: IfcLabel → "Electric Motor" or "Diesel Engine"
- MotorPower: IfcPowerMeasure → 125 HP
- NFPACompliance: IfcLabel → "NFPA 20-2022"
- ControllerType: IfcLabel → "Automatic Start/Stop"
```

---

## Property Sets (Psets)

### Standard IFC4 Property Sets

Property sets provide non-geometric attributes for IFC entities. Standard property sets are defined in the IFC schema and recognized by all compliant software.

#### Pset_ElectricalDeviceCommon

**Applies To**: All electrical devices (panels, outlets, fixtures, switches)

**Properties:**
| Property Name | Type | Description | Example |
|---------------|------|-------------|---------|
| Reference | IfcIdentifier | Reference designation | "LP-1" |
| Status | IfcLabel | Operational status | "New", "Existing", "Demolition" |
| Manufacturer | IfcLabel | Manufacturer name | "Square D" |
| ModelReference | IfcIdentifier | Model number | "NQOD430M100" |
| NominalVoltageAC | IfcElectricVoltageMeasure | AC voltage rating | 208 V |
| NominalVoltageAC1 | IfcElectricVoltageMeasure | AC voltage L1-N | 120 V |
| NominalVoltageAC2 | IfcElectricVoltageMeasure | AC voltage L2-N | 120 V |
| NominalVoltageAC3 | IfcElectricVoltageMeasure | AC voltage L3-N | 120 V |
| NominalFrequency | IfcFrequencyMeasure | Frequency | 60 Hz |
| PowerFactor | IfcNormalisedRatioMeasure | Power factor | 0.95 |
| ConductorFunction | IfcLabel | Conductor role | "Phase", "Neutral", "Ground" |

#### Pset_AirTerminalTypeCommon

**Applies To**: Air terminals (diffusers, grilles, registers)

**Properties:**
| Property Name | Type | Description | Example |
|---------------|------|-------------|---------|
| Reference | IfcIdentifier | Tag designation | "SD1" |
| AirFlowrateRange | IfcVolumetricFlowRateMeasure | Min-max CFM | 400-800 CFM |
| TemperatureRange | IfcThermodynamicTemperatureMeasure | Operating temp range | 55-75°F |
| NominalAirFlowRate | IfcVolumetricFlowRateMeasure | Design CFM | 800 CFM |
| AirDiffusionPerformanceIndex | IfcReal | ADPI rating | 80 |
| NeckSize | IfcLabel | Connection size | "12 inch round" |
| CoreType | IfcLabel | Core configuration | "Perforated" |
| Finish | IfcLabel | Surface finish | "White Powder Coat" |

#### Pset_SanitaryTerminalTypeCommon

**Applies To**: Plumbing fixtures

**Properties:**
| Property Name | Type | Description | Example |
|---------------|------|-------------|---------|
| Reference | IfcIdentifier | Fixture tag | "WC-1" |
| Mounting | IfcLabel | Mounting type | "Floor-Mounted", "Wall-Hung" |
| Color | IfcLabel | Fixture color | "White" |
| DrainSize | IfcLabel | Drain connection size | "3 inch" |
| HasOverflow | IfcBoolean | Overflow present | True/False |
| SpilloverLevel | IfcLengthMeasure | Overflow height | 18 inches |
| IsWasteTrap | IfcBoolean | Trap included | True/False |

### Custom Property Sets (Project-Specific)

Custom property sets extend IFC with project-specific data not covered by standard Psets.

**Naming Convention**: `Pset_[EntityType]_[Application]`

Example: `Pset_ElectricalPanel_LoadData`

#### Example: Pset_ElectricalPanel_LoadData

**Purpose**: NEC load calculation data for panels

**Properties:**
```xml
<PropertySet name="Pset_ElectricalPanel_LoadData">
  <Property name="TotalConnectedLoad_VA" type="IfcReal" />
  <Property name="DemandLoad_VA" type="IfcReal" />
  <Property name="LoadCalculationMethod" type="IfcLabel" />
    <!-- Example values: "NEC 220.82 Optional", "NEC 220.40 Standard" -->
  <Property name="DiversityFactor" type="IfcNormalisedRatioMeasure" />
  <Property name="DemandFactor" type="IfcNormalisedRatioMeasure" />
  <Property name="ContinuousLoad_VA" type="IfcReal" />
  <Property name="NonContinuousLoad_VA" type="IfcReal" />
  <Property name="MinimumPanelSize_A" type="IfcElectricCurrentMeasure" />
</PropertySet>
```

#### Example: Pset_AirTerminal_PerformanceData

**Purpose**: HVAC performance data for test and balance

**Properties:**
```xml
<PropertySet name="Pset_AirTerminal_PerformanceData">
  <Property name="DesignAirFlow_CFM" type="IfcVolumetricFlowRateMeasure" />
  <Property name="MeasuredAirFlow_CFM" type="IfcVolumetricFlowRateMeasure" />
  <Property name="ThrowDistance_ft" type="IfcLengthMeasure" />
  <Property name="InletStaticPressure_inWG" type="IfcPressureMeasure" />
  <Property name="NoiseLevel_NC" type="IfcInteger" />
  <Property name="ZoneAssignment" type="IfcLabel" />
    <!-- Example: "Zone-1A" -->
</PropertySet>
```

---

## Quantity Sets (Qtos)

Quantity sets provide measurable physical quantities for estimating and material takeoffs.

### Qto_PipeFittingBaseQuantities

**Applies To**: Pipe fittings

**Quantities:**
| Quantity Name | Type | Description | Example |
|---------------|------|-------------|---------|
| Length | IfcLengthMeasure | Overall length | 3 inches |
| GrossCrossSectionArea | IfcAreaMeasure | Cross-section area | 0.785 sq in |
| NetCrossSectionArea | IfcAreaMeasure | Internal area | 0.601 sq in |
| OuterSurfaceArea | IfcAreaMeasure | External surface | 0.25 sq ft |
| GrossWeight | IfcMassMeasure | Total weight | 0.6 lbs |
| NetWeight | IfcMassMeasure | Net weight (excl. packaging) | 0.5 lbs |

### Qto_DuctFittingBaseQuantities

**Applies To**: Duct fittings

**Quantities:**
| Quantity Name | Type | Description | Example |
|---------------|------|-------------|---------|
| Length | IfcLengthMeasure | Fitting length | 12 inches |
| GrossCrossSectionArea | IfcAreaMeasure | Duct cross-section | 2 sq ft |
| NetCrossSectionArea | IfcAreaMeasure | Internal area | 1.8 sq ft |
| OuterSurfaceArea | IfcAreaMeasure | Sheet metal area | 8 sq ft |
| GrossWeight | IfcMassMeasure | Total weight | 18 lbs |
| NetWeight | IfcMassMeasure | Fitting weight only | 15 lbs |

---

## IFC Extraction from BIM Tools

### Revit IFC Export Configuration

**Revit IFC Export Settings for MEP:**

1. **IFC Version**: IFC4 (Design Transfer View) or IFC4.3
2. **Export Scope**: Current View or Entire Project
3. **Space Boundaries**: 2nd Level (for energy analysis)
4. **Property Sets**: Include IFC Common Property Sets
5. **Base Quantities**: Export Base Quantities
6. **Coordinate Base**: Shared Coordinates (for federated models)

**File → Export → IFC Options:**
```
IFC Version: IFC4 Design Transfer View
File Type: IFC4
Space Boundaries: 2nd Level
Project Origin: Shared Coordinates
Phase to Export: New Construction
Export Base Quantities: Checked
Export schedules as property sets: Checked
Export Revit property sets: Checked
Export IFC Common Property Sets: Checked
Export linked files as separate IFCs: Unchecked (for single file)
Store IFC GUID in file: Checked (for round-tripping)
```

**MEP-Specific Mapping:**
- Revit Electrical Panels → `IfcElectricDistributionBoard`
- Revit Lighting Fixtures → `IfcLightFixture`
- Revit Electrical Fixtures (receptacles) → `IfcOutlet`
- Revit Air Terminals → `IfcAirTerminal`
- Revit Ducts → `IfcDuctSegment`
- Revit Pipes → `IfcPipeSegment`
- Revit Plumbing Fixtures → `IfcSanitaryTerminal`
- Revit Sprinklers → `IfcFireSuppressionTerminal`

### ArchiCAD IFC Export Configuration

**ArchiCAD IFC Translator Settings:**

1. **IFC Version**: IFC4 or IFC4.3
2. **Data Conversion**: Geometry and Properties
3. **MEP Systems**: Enable MEP Port and Connection export
4. **Property Mapping**: Include custom property sets

**File → Save As → IFC:**
```
IFC Scheme: IFC4 Design Transfer View
Translator: ArchiCAD 26 IFC4 Design Transfer View
Export Filter: All MEP Systems
Geometry Conversion: Exact (BRep)
Include Properties: All Properties
Custom Property Sets: Checked
MEP Ports: Export
MEP Connections: Export
```

### IFC Export Validation

After export, validate IFC file quality:

1. **Open in IFC Viewer**: Solibri, Simplebim, or FZKViewer
2. **Check Entity Mapping**: Verify MEP elements have correct IFC classes
3. **Verify Property Sets**: Confirm Psets are populated
4. **Coordinate System**: Ensure all models share same origin
5. **File Size**: Typical 10-50 MB for single-discipline MEP model

---

## IFC to JSON Mapping for QA Validation

This section demonstrates how IFC entities are extracted and transformed into the JSON schema expected by `engineering-drawing-qaqc` skill (defined in `data_format_examples.md`).

### Extraction Workflow

```
┌──────────────────────────────────────────────────────────┐
│  Step 1: IFC File Input                                  │
│  - Electrical_Model_2024-06-01.ifc                       │
│  - Contains IfcElectricDistributionBoard, IfcLightFixture│
└────────────────────────┬─────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────┐
│  Step 2: Parse IFC Entities                              │
│  - IfcOpenShell or similar IFC parser                    │
│  - Extract entities by type                              │
│  - Read property sets and attributes                     │
└────────────────────────┬─────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────┐
│  Step 3: Map to JSON Schema                              │
│  - Title block from IfcProject metadata                  │
│  - Legend from unique IfcType objects                    │
│  - Symbols from IfcElement instances                     │
│  - Schedules from aggregated property sets               │
└────────────────────────┬─────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────┐
│  Step 4: JSON Output                                     │
│  - HQ2024-ABC-01-GF-QA-ELE-0101.json                     │
│  - Ready for engineering-drawing-qaqc validation         │
└──────────────────────────────────────────────────────────┘
```

### Mapping Example: Electrical Panel

**IFC Input:**
```
#12345=IFCELECTRICDISTRIBUTIONBOARD('2XbR$6fTj9QvhP4n0Z8I5D',$,'LP-1','Main Lighting Panel - Ground Floor',$,$,$,$);
#12346=IFCRELDEFINESBYTYPE('3YcS$7gUk0RwiQ5o1A9J6E',$,$,$,(#12345),#12350);
#12350=IFCELECTRICDISTRIBUTIONBOARDTYPE('4ZdT$8hVl1SxjR6p2B0K7F',$,'Panelboard',$,$,$,$,$,.DISTRIBUTIONBOARD.);

#12360=IFCPROPERTYSET('5AeU$9iWm2TykS7q3C1L8G',$,'Pset_ElectricalDeviceCommon',$,(#12361,#12362,#12363,#12364));
#12361=IFCPROPERTYSINGLEVALUE('Manufacturer',$,IFCLABEL('Square D'),$);
#12362=IFCPROPERTYSINGLEVALUE('ModelReference',$,IFCIDENTIFIER('NQOD430M100'),$);
#12363=IFCPROPERTYSINGLEVALUE('NominalVoltageAC',$,IFCELECTRICVOLTAGEMEASURE(208.),$);
#12364=IFCPROPERTYSINGLEVALUE('NominalFrequency',$,IFCFREQUENCYMEASURE(60.),$);

#12370=IFCPROPERTYSET('6BfV$0jXn3UzlT8r4D2M9H',$,'Pset_ElectricalPanel_LoadData',$,(#12371,#12372,#12373));
#12371=IFCPROPERTYSINGLEVALUE('TotalConnectedLoad_VA',$,IFCREAL(28500.),$);
#12372=IFCPROPERTYSINGLEVALUE('DemandLoad_VA',$,IFCREAL(21300.),$);
#12373=IFCPROPERTYSINGLEVALUE('LoadCalculationMethod',$,IFCLABEL('NEC 220.82 Optional'),$);
```

**JSON Output:**
```json
{
  "schedules": {
    "panel_schedule": {
      "panel_id": "LP-1",
      "description": "Main Lighting Panel - Ground Floor",
      "voltage": 120/208,
      "phases": 3,
      "main_breaker": "100A",
      "manufacturer": "Square D",
      "model": "NQOD430M100",
      "total_connected_load": 28500,
      "demand_load": 21300,
      "load_calculation_included": true,
      "load_calculation_method": "NEC 220.82 Optional"
    }
  }
}
```

### Mapping Example: Lighting Fixture to Legend and Symbols

**IFC Input:**
```
#20001=IFCLIGHTFIXTURE('7CgW$1kYo4V0mU9s5E3N0I',$,'D1','2x2 LED Troffer, 3500K, 3500 lumens',$,$,(#20010),$);
#20010=IFCCARTESIANPOINT((125.,340.,10.));

#20020=IFCLIGHTFIXTURETYPE('8DhX$2lZp5W1nV0t6F4O1J',$,'LED Troffer',$,$,$,$,$,.DIRECTIONSOURCE.);

#20030=IFCPROPERTYSET('9EiY$3mAq6X2oW1u7G5P2K',$,'Pset_LightFixtureTypeCommon',$,(#20031,#20032,#20033));
#20031=IFCPROPERTYSINGLEVALUE('LightEmitterNominalPower',$,IFCPOWERMEASURE(35.),$);
#20032=IFCPROPERTYSINGLEVALUE('ColorTemperature',$,IFCTHERMODYNAMICTEMPERATUREMEASURE(3500.),$);
#20033=IFCPROPERTYSINGLEVALUE('LuminousFlux',$,IFCLUMINOUSFLUXMEASURE(3500.),$);
```

**JSON Output:**
```json
{
  "legend": [
    {
      "symbol_id": "D1",
      "description": "2x2 LED Troffer, 3500K, 3500 lumens",
      "type": "lighting_fixture"
    }
  ],
  "symbols": [
    {
      "class": "lighting_fixture",
      "tag": "D1",
      "location": {"x": 125, "y": 340},
      "circuit": "A1",
      "quantity": 1
    }
  ]
}
```

### Mapping Table: IFC Properties → JSON Fields

| IFC Property Set | IFC Property | JSON Field Path | Notes |
|------------------|--------------|-----------------|-------|
| Pset_ElectricalDeviceCommon | Manufacturer | schedules.panel_schedule.manufacturer | Direct mapping |
| Pset_ElectricalDeviceCommon | ModelReference | schedules.panel_schedule.model | Direct mapping |
| Pset_ElectricalDeviceCommon | NominalVoltageAC | schedules.panel_schedule.voltage | Convert to combined voltage notation (120/208) |
| Pset_ElectricalPanel_LoadData | TotalConnectedLoad_VA | schedules.panel_schedule.total_connected_load | Direct mapping |
| Pset_ElectricalPanel_LoadData | DemandLoad_VA | schedules.panel_schedule.demand_load | Direct mapping |
| Pset_ElectricalPanel_LoadData | LoadCalculationMethod | schedules.panel_schedule.load_calculation_method | Direct mapping |
| IfcElectricDistributionBoard.Name | - | schedules.panel_schedule.panel_id | Entity attribute |
| IfcLightFixture.Name | - | legend[].symbol_id, symbols[].tag | Entity attribute |
| IfcLightFixture.Description | - | legend[].description | Entity attribute |
| IfcCartesianPoint | - | symbols[].location | Geometry extraction |

---

## Integration with SKILL.md Workflow

### Data Flow Integration

The IFC entity mapping directly supports the `engineering-drawing-qaqc` SKILL.md workflow:

**SKILL.md Step 1: Understand Input Data**
- IFC files exported from BIM tools (Revit, ArchiCAD) contain MEP element data
- IFC entities and property sets are mapped to JSON schema per `data_format_examples.md`
- JSON data structure includes title_block, legend, symbols, schedules

**IFC Integration:**
```
BIM Model (Revit/ArchiCAD)
    ↓ Export
IFC File (IfcElectricDistributionBoard, IfcLightFixture, etc.)
    ↓ Parse & Map
JSON Data (panel_schedule, lighting_symbols, etc.)
    ↓ Load
SKILL.md Step 1 Input
```

**SKILL.md Step 2: Load or Define QA Rules**
- QA rules target JSON field paths that correspond to IFC property sets
- Example: Rule checks `schedules.panel_schedule.load_calculation_included` (from IFC `Pset_ElectricalPanel_LoadData`)

**IFC Integration:**
```yaml
- id: QA-201-ELEC
  description: Verify electrical panel schedules include load calculations
  severity: critical
  category: compliance
  check:
    type: field_presence
    field: schedules.panel_schedule.load_calculation_included
    condition: equals true
  rationale: NEC requires load calculations for service and feeder sizing
  ifc_source: Pset_ElectricalPanel_LoadData.LoadCalculationIncluded
```

**SKILL.md Step 3: Execute QA Validation**
- Validation engine evaluates rules against JSON data extracted from IFC
- Field paths in rules directly reference IFC property mappings

**SKILL.md Step 4: Aggregate Results**
- Results include IFC entity identifiers (GlobalId, Name) for traceability back to BIM model

**SKILL.md Step 5: Generate Report**
- QA report includes IFC entity references for model coordination

**Report Output Example:**
```csv
Sheet,Rule ID,Severity,Category,Status,Description,Details,IFC Entity
E-301,QA-201-ELEC,critical,compliance,PASS,Verify panel load calculations,Load calc included,IfcElectricDistributionBoard:LP-1 (2XbR$6fTj9QvhP4n0Z8I5D)
E-301,QA-102,high,legend,FAIL,Confirm symbols match legend,"Symbol 'D4' not found in legend",IfcLightFixture:D4 (7CgW$1kYo4V0mU9s5E3N0I)
```

### End-to-End Workflow Example

**Scenario**: Validate electrical drawings from coordinated Revit MEP model

**Step 1**: BIM Authoring (Revit)
- Electrical engineer models panels, lighting, receptacles in Revit
- Populates panel schedules with load calculations
- Assigns circuits to devices
- Completes coordination with architectural and mechanical disciplines

**Step 2**: IFC Export
- Export Revit electrical model to IFC4 using Design Transfer View
- IFC file: `HQ2024-ABC-01-GF-M3-ELE-0101-S4.ifc`
- Confirm property sets are included (Pset_ElectricalDeviceCommon, etc.)

**Step 3**: IFC to JSON Conversion
- Parse IFC file using IfcOpenShell or similar library
- Extract electrical panels → `schedules.panel_schedule[]`
- Extract lighting fixtures → `legend[]`, `symbols[]`
- Extract receptacles → `legend[]`, `symbols[]`
- Build title block from IFC project metadata
- Output: `HQ2024-ABC-01-GF-QA-ELE-0101-S4.json`

**Step 4**: QA Validation (engineering-drawing-qaqc skill)
- Load JSON data file
- Load electrical QA ruleset: `04_QA_QC_RULESETS/Electrical/electrical_qa_rules.yaml`
- Execute validation engine
- Rules evaluated:
  - QA-001: Title block completeness (check IfcProject metadata)
  - QA-102: Symbol-legend match (verify all IfcLightFixture instances in legend)
  - QA-201-ELEC: Panel load calculations (check Pset_ElectricalPanel_LoadData)
  - QA-301: Cross-reference validation (check IfcRelAssignsToGroup relationships)

**Step 5**: Review and Correction
- QA report identifies 2 failures:
  - Symbol D4 not in legend (IfcLightFixture instance missing from type definitions)
  - Panel LP-3 missing load calculation (Pset_ElectricalPanel_LoadData incomplete)
- Electrical engineer returns to Revit model
- Adds D4 to lighting fixture schedule (creates IfcLightFixtureType)
- Populates LP-3 load calculation properties
- Re-exports IFC, repeats validation
- Pass rate: 98% (meets >95% threshold)

**Step 6**: Authorization and Publication
- Validated drawings authorized for construction (A7)
- IFC model and JSON data archived together for as-built traceability

---

## Appendix: IFC Class Hierarchy Reference

### Complete MEP Entity Hierarchy

```
IfcDistributionElement (abstract)
│
├── IfcDistributionControlElement (abstract)
│   ├── IfcActuator (damper actuators, valve actuators)
│   ├── IfcAlarm (fire alarm devices, security alarms)
│   ├── IfcController (BAS controllers, PLC)
│   ├── IfcFlowInstrument (sensors, gauges, meters)
│   ├── IfcProtectiveDeviceTrippingUnit (circuit breaker trip units)
│   ├── IfcSensor (temperature, pressure, flow sensors)
│   ├── IfcUnitaryControlElement (thermostats, humidistats)
│
├── IfcDistributionFlowElement (abstract)
│   │
│   ├── IfcDistributionChamberElement (manholes, valve vaults)
│   │
│   ├── IfcEnergyConversionDevice (abstract)
│   │   ├── IfcAirToAirHeatRecovery
│   │   ├── IfcBoiler
│   │   ├── IfcBurner
│   │   ├── IfcChiller
│   │   ├── IfcCoil (heating coils, cooling coils)
│   │   ├── IfcCondenser
│   │   ├── IfcCooledBeam
│   │   ├── IfcCoolingTower
│   │   ├── IfcElectricGenerator
│   │   ├── IfcElectricMotor
│   │   ├── IfcEngine (diesel generators)
│   │   ├── IfcEvaporativeCooler
│   │   ├── IfcEvaporator
│   │   ├── IfcHeatExchanger
│   │   ├── IfcHumidifier
│   │   ├── IfcMotorConnection
│   │   ├── IfcSolarDevice (solar thermal collectors)
│   │   ├── IfcTransformer
│   │   ├── IfcTubeBundle
│   │   ├── IfcUnitaryEquipment (packaged HVAC units)
│   │
│   ├── IfcFlowController (abstract)
│   │   ├── IfcAirTerminalBox (VAV boxes)
│   │   ├── IfcDamper
│   │   ├── IfcElectricDistributionBoard
│   │   ├── IfcElectricTimeControl (timers, programmable switches)
│   │   ├── IfcFlowMeter
│   │   ├── IfcProtectiveDevice (fuses, breakers)
│   │   ├── IfcSwitchingDevice (switches, contactors)
│   │   ├── IfcValve
│   │
│   ├── IfcFlowFitting (abstract)
│   │   ├── IfcCableCarrierFitting
│   │   ├── IfcCableFitting (cable connectors, lugs)
│   │   ├── IfcDuctFitting
│   │   ├── IfcJunctionBox
│   │   ├── IfcPipeFitting
│   │
│   ├── IfcFlowMovingDevice (abstract)
│   │   ├── IfcCompressor
│   │   ├── IfcFan
│   │   ├── IfcPump
│   │
│   ├── IfcFlowSegment (abstract)
│   │   ├── IfcCableCarrierSegment (conduit, cable tray)
│   │   ├── IfcCableSegment
│   │   ├── IfcDuctSegment
│   │   ├── IfcPipeSegment
│   │
│   ├── IfcFlowStorageDevice (abstract)
│   │   ├── IfcElectricFlowStorageDevice (batteries, UPS)
│   │   ├── IfcTank
│   │
│   ├── IfcFlowTerminal (abstract)
│   │   ├── IfcAirTerminal
│   │   ├── IfcAudioVisualAppliance (TVs, speakers)
│   │   ├── IfcCommunicationsAppliance (routers, switches)
│   │   ├── IfcElectricAppliance (appliances)
│   │   ├── IfcFireSuppressionTerminal
│   │   ├── IfcLamp (lamps, bulbs)
│   │   ├── IfcLightFixture
│   │   ├── IfcMedicalDevice
│   │   ├── IfcOutlet
│   │   ├── IfcSanitaryTerminal
│   │   ├── IfcSpaceHeater
│   │   ├── IfcStackTerminal (plumbing vents)
│   │   ├── IfcWasteTerminal (floor drains, cleanouts)
│   │
│   ├── IfcFlowTreatmentDevice (abstract)
│       ├── IfcDuctSilencer
│       ├── IfcFilter (air filters, water filters)
│       ├── IfcInterceptor (grease trap, oil separator)
```

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-06-01 | IFC Schema Specialist | Initial document creation |
| 2.0 | 2025-10-22 | IFC Schema Specialist | Enhanced with IFC4.3, SKILL.md integration, JSON mapping examples |

**Next Review**: 2026-01-01

---

**End of Document**
