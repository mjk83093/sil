# Electrical Entities

## Overview
Definitions and attributes for primary electrical components used in system modeling and load calculations.

## Definition
Electrical entities represent the physical and logical components of a power distribution system, from the utility source to the end-use load.

## Key Entities

### 1. Feeders
- **Description**: Conductors connecting distribution points (e.g., Main Switchboard to Sub-panel).
- **Attributes**:
    - `Voltage`: System nominal voltage (e.g., 480Y/277V).
    - `Ampacity`: Rated capacity based on NEC Table 310.16.
    - `Conductor_Material`: Copper or Aluminum.
    - `Conduit_Type`: EMT, RMC, PVC, etc.

### 2. Panels (Panelboards)
- **Description**: A single panel or group of panel units designed for assembly in the form of a single panel.
- **Attributes**:
    - `Main_Type`: Main Lug Only (MLO) or Main Circuit Breaker (MCB).
    - `Bus_Rating`: Total amperage capacity of the busbars.
    - `AIC_Rating`: Short-circuit current rating (Amps Interrupting Capacity).
    - `Mounting`: Surface or Recessed.

### 3. Transformers
- **Description**: Static apparatus which transforms alternating-current energy from one voltage level to another.
- **Attributes**:
    - `KVA_Rating`: Apparent power capacity.
    - `Primary_Voltage`: Input voltage.
    - `Secondary_Voltage`: Output voltage.
    - `Impedance`: Percentage impedance (%Z) for fault current calcs.

### 4. Loads
- **Description**: Equipment that consumes electrical energy.
- **Categories**:
    - `Lighting`: General, Emergency, Exterior.
    - `Receptacles`: General purpose, Special.
    - `Motors`: HP rated, FLA (Full Load Amps).
    - `HVAC`: MCA (Minimum Circuit Ampacity) and MOCP (Maximum Overcurrent Protection).

## Business Rules
1. **Entity Hierarchy**: Loads connect to Branch Circuits -> Branch Circuits connect to Panels -> Panels connect to Feeders -> Feeders connect to Upstream Distribution or Transformers.
2. **Sizing**: Feeders must be sized to handle the calculated load of all downstream entities plus future growth factors.

## Relationships
- **Depends on**: `nec-terminology.md`
- **Used by**: `calculation-workflows.md`, `load-schedule-template.md`

## Examples
```yaml
entity_definition:
  type: "Transformer"
  id: "T-1"
  kva: 75
  primary: 480
  secondary: 208/120
  mounting: "Floor"
  location: "Elec Room 101"
```
