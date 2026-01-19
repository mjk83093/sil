# One-Line Diagram Standards
## IEEE/ANSI Standards for Electrical Power Distribution

**Document Version**: 1.0
**Last Updated**: 2025-01-22
**Applicable Standards**: IEEE Std 315, ANSI Y32.2, IEEE Std 141 (Red Book), IEEE Std 241 (Gray Book)
**NEC Reference**: Articles 215, 225, 230, 408, 450, 700, 701, 702

---

## Table of Contents

1. [Introduction and Purpose](#introduction-and-purpose)
2. [Standard Symbols and Conventions](#standard-symbols-and-conventions)
3. [Equipment Representation](#equipment-representation)
4. [Voltage Levels and Color Coding](#voltage-levels-and-color-coding)
5. [Protective Device Symbology](#protective-device-symbology)
6. [Metering and Instrumentation](#metering-and-instrumentation)
7. [Normal vs Emergency Power](#normal-vs-emergency-power)
8. [Layout and Organization](#layout-and-organization)
9. [Common Mistakes and QA Checkpoints](#common-mistakes-and-qa-checkpoints)
10. [Calculation Examples](#calculation-examples)

---

## 1. Introduction and Purpose

### What is a One-Line Diagram?

A one-line (single-line) diagram is a simplified notation for representing a three-phase power system. It shows the electrical distribution path from the utility service entrance through all major equipment to branch panels, using standardized symbols to represent electrical components.

### Purpose and Applications

- **System Overview**: Provides high-level view of entire electrical distribution
- **Coordination Study**: Basis for protective device coordination analysis
- **Arc Flash Study**: Foundation for arc flash hazard analysis (IEEE 1584)
- **Design Communication**: Primary document for electrical engineers, contractors, and inspectors
- **As-Built Documentation**: Essential for facility management and future modifications
- **Code Compliance**: Demonstrates compliance with NEC Articles 215, 230, 408, 700-702

### Key Standards Referenced

| Standard | Title | Application |
|----------|-------|-------------|
| IEEE Std 315-1975 (R1993) | Graphic Symbols for Electrical and Electronics Diagrams | Standard symbols for all electrical components |
| ANSI Y32.2 | Graphic Symbols for Electrical Diagrams | Legacy standard, still widely referenced |
| IEEE Std 141 (Red Book) | Recommended Practice for Electric Power Distribution for Industrial Plants | Industrial power systems |
| IEEE Std 241 (Gray Book) | Recommended Practice for Commercial Building Electrical Systems | Commercial power systems |
| IEEE Std 242 (Buff Book) | Recommended Practice for Protection and Coordination | Protective device coordination |
| NFPA 70 (NEC) | National Electrical Code | Code compliance requirements |

---

## 2. Standard Symbols and Conventions

### Basic Power Symbols

#### Circuit Breakers
```
Standard Circuit Breaker:
    ──┤├──  or  ──╫──

Molded Case Circuit Breaker (MCCB):
    ──┤MCCB├──

Low Voltage Power Circuit Breaker (LVPCB):
    ──┤LPCB├──

Vacuum Circuit Breaker (VCB):
    ──┤VCB├──

Medium Voltage Circuit Breaker:
    ══╪══  (with double lines indicating MV)
```

#### Fuses
```
Standard Fuse:
    ──┤>├──  or  ──>──

Current-Limiting Fuse:
    ──┤>*├──

High-Voltage Fuse:
    ══>══
```

#### Disconnect Switches
```
Non-Fused Disconnect:
    ──/──  or  ──◊──

Fused Disconnect Switch:
    ──/>├──

Motor Disconnect:
    ──/M──

Safety Switch:
    ──[SS]──
```

### Transformers

#### Power Transformers
```
Two-Winding Transformer:
    ──⟨)((⟩──  or  ──◯──

Three-Winding Transformer:
    ──⟨)|(⟩──

Auto-Transformer:
       │
    ──⟨))⟩──
       │

Transformer with Taps:
    ──⟨)±(⟩──
```

#### Transformer Connection Designations
```
Delta-Wye: Δ-Y
Wye-Delta: Y-Δ
Delta-Delta: Δ-Δ
Wye-Wye: Y-Y

Example label: 1500 kVA, 480Δ-208Y/120V, Z=5.75%
```

### Distribution Equipment

#### Switchboards and Panelboards
```
Switchboard:
    ┌─────────┐
    │   SWB   │
    │  Main   │
    └─────────┘

Distribution Panelboard:
    ┌───────┐
    │  DP   │
    │  A-1  │
    └───────┘

Lighting Panelboard:
    ┌───────┐
    │  LP   │
    │  L-2  │
    └───────┘

Motor Control Center (MCC):
    ┌─────────┐
    │  MCC-1  │
    └─────────┘
```

### Motors and Loads

#### Motor Symbols
```
Motor (General):
    ──○M──

Three-Phase Motor:
    ──○3M──

Variable Frequency Drive (VFD):
    ┌───────┐
    │  VFD  │──○3M──
    └───────┘

Motor Starter with OCPD:
    ──┤├──○M──
```

#### Load Representations
```
General Load:
    ──┬──
      │
    ──┴──

Feeder to Remote Panel:
    ──→ DP-2

Spare/Future Load:
    ──┬──  (dashed line)
      :
    ──┴──
```

### Bus Arrangements

```
Single Bus:
    ════════════════

Double Bus:
    ════════════════  (Bus 1)
    ════════════════  (Bus 2)

Main-Tie-Main:
    ══╪══──BUS A──╪══BUS B──╪══
     Main 1      Tie      Main 2
```

---

## 3. Equipment Representation

### Service Entrance Equipment

#### Utility Service Point
```
Utility Meter:
┌──────────────┐
│   UTILITY    │
│   kWh METER  │
│  CT: 2000:5  │
└──────────────┘
      │
    ══╪══ (Service Point - 480V, 3φ, 4W)
      │
```

#### Main Service Switchboard
```
┌─────────────────────────────────────────┐
│         MAIN SWITCHBOARD MSB-1          │
│                                         │
│  Main LPCB: 2000A, 3P, 65kAIC          │
│  Bus Rating: 2000A                      │
│  SCCR: 65kA at 480V                    │
│                                         │
│  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  │
│  │ 400A│  │ 600A│  │ 225A│  │ 100A│  │
│  │ DP-1│  │ T-1 │  │ DP-2│  │LP-1 │  │
│  └─────┘  └─────┘  └─────┘  └─────┘  │
└─────────────────────────────────────────┘
```

### Transformer Representation

#### Complete Transformer Information
```
┌────────────────────────────────┐
│     TRANSFORMER T-1            │
│                                │
│  480V, 3φ ──⟨)((⟩── 208Y/120V │
│                                │
│  Rating: 225 kVA               │
│  Connection: Δ-Y               │
│  Impedance: 5.75%              │
│  Primary OCPD: 300A            │
│  Secondary OCPD: 700A          │
│  Temp Rise: 150°C              │
│  Type: Dry Type, K-13          │
└────────────────────────────────┘
```

### Generator Systems

#### Emergency Generator
```
┌─────────────────────────────────────┐
│    EMERGENCY GENERATOR GEN-1        │
│                                     │
│  Rating: 500 kW, 625 kVA           │
│  Voltage: 480V, 3φ, 4W             │
│  Type: Diesel                       │
│  Starting: Automatic, <10 sec      │
│  Fuel: 500 gal, 24hr runtime       │
│  Generator CB: 800A, 3P, 65kAIC    │
│                                     │
│  ATS ──/─┬─\── [Normal/Emergency]  │
│          │                          │
│        [EMGCY                       │
│         LOADS]                      │
└─────────────────────────────────────┘
```

### Panelboard Representation

#### Distribution Panel Schedule Summary
```
┌─────────────────────────────────┐
│    DISTRIBUTION PANEL DP-1      │
│                                 │
│  Fed From: MSB-1, Ckt 1        │
│  Location: 1st Floor Elec Room │
│  Voltage: 208Y/120V, 3φ, 4W    │
│  Main Breaker: 400A, 3P        │
│  Bus Rating: 400A              │
│  SCCR: 22kAIC                  │
│                                 │
│  Feeder: 500 kcmil Cu per ph   │
│  Conduit: 3" EMT                │
│  Length: 75 ft                  │
│  Voltage Drop: 1.8%            │
│                                 │
│  Connected Load: 285A           │
│  Demand Load: 320A              │
│  Spare Capacity: 20%           │
└─────────────────────────────────┘
```

---

## 4. Voltage Levels and Color Coding

### Standard Voltage Systems

#### Common Distribution Voltages

| System | Voltage | Configuration | Application |
|--------|---------|---------------|-------------|
| Utilization | 120V | 1φ, 2W | Lighting, small loads |
| Utilization | 120/240V | 1φ, 3W | Residential, small commercial |
| Utilization | 208Y/120V | 3φ, 4W | Commercial buildings (most common) |
| Utilization | 480Y/277V | 3φ, 4W | Large commercial, industrial |
| Utilization | 600Y/347V | 3φ, 4W | Canadian applications |
| Distribution | 4160V | 3φ, 3W | Campus distribution |
| Distribution | 13.8kV | 3φ, 3W | Utility distribution |

### Voltage Level Representation

#### Line Weight Standards
```
Low Voltage (120V-600V):
    ──────  (Single line weight)

Medium Voltage (601V-35kV):
    ══════  (Double line weight)

High Voltage (>35kV):
    ══════  (Double line weight, bold)
```

### Color Coding Standards

#### IEEE Color Code for Voltage Levels

```
120V Single Phase:       Black line
208Y/120V Three Phase:   Red line
240V Single Phase:       Blue line
480V Three Phase:        Orange line
480Y/277V Three Phase:   Brown line
600V Three Phase:        Purple line
Medium Voltage (4-35kV): Green line
```

#### Emergency/Standby Power Color Coding
```
Normal Power:            Black or standard voltage color
Emergency Power:         Red (with "EMGCY" label)
Legally Required Power:  Red/Orange dashed
Optional Standby:        Orange dashed
UPS/Critical Power:      Green
```

#### Example Color-Coded One-Line
```
         NORMAL (Black)     EMERGENCY (Red)
              │                   │
    ┌─────────┴────────┐   ┌─────┴──────┐
    │   MSB-1 (480V)   │   │  GEN-1     │
    │     Orange       │   │  (480V)    │
    └──────────────────┘   └────────────┘
```

---

## 5. Protective Device Symbology

### Overcurrent Protective Devices (OCPD)

#### Circuit Breaker Types and Ratings

```
Thermal-Magnetic Breaker:
    ──┤TM├──  (Trip: 800A frame, 600A trip)

Electronic Trip Breaker:
    ──┤ET├──  (LSI settings shown)

Ground Fault Protection:
    ──┤GF├──  (GF: 1200A/0.3s)

Arc Flash Reduction:
    ──┤ZSI├── (Zone Selective Interlocking)
```

#### Complete Breaker Annotation
```
┌──────────────────────────────────────┐
│  Main Circuit Breaker                │
│                                      │
│  ──┤LPCB├──                         │
│                                      │
│  Frame: 2000A                        │
│  Trip: 2000A                         │
│  Poles: 3P                           │
│  AIC: 65kA @ 480V                   │
│  Type: Fixed Electronic Trip (LSI)   │
│  LSI Settings:                       │
│    Long Time: 2000A, 100%           │
│    Short Time: 4800A, 0.3s          │
│    Instantaneous: 16,000A           │
│  GFP: 1200A, 0.3s                   │
│  Mfr: Square D, Type NW20H3         │
└──────────────────────────────────────┘
```

#### Fuse Designation
```
┌──────────────────────────────────┐
│  Primary Fuse                    │
│                                  │
│  ──┤>*├──                       │
│                                  │
│  Rating: 200E (200A Class RK1)   │
│  Voltage: 600V                   │
│  AIC: 200kA                      │
│  Type: Current-Limiting          │
│  Time-Current: See Curve E1      │
│  Mfr: Ferraz Shawmut A6D200R     │
└──────────────────────────────────┘
```

### Protective Relaying

#### Relay Functions (IEEE Device Numbers)

| Number | Function | Symbol | Application |
|--------|----------|--------|-------------|
| 27 | Undervoltage | 27 | Generator/motor protection |
| 50 | Instantaneous Overcurrent | 50 | Phase fault protection |
| 51 | Time Overcurrent | 51 | Overload/fault protection |
| 50G/51G | Ground Overcurrent | 50G/51G | Ground fault protection |
| 67 | Directional Overcurrent | 67 | Loop/tie systems |
| 87 | Differential | 87 | Transformer protection |
| 81 | Frequency | 81 | Generator protection |

#### Relay Representation
```
┌────────────────────────────────┐
│  Protective Relay Package      │
│                                │
│  Functions: 50/51, 50G/51G    │
│                                │
│  Phase O/C (51):               │
│    Pick-up: 800A               │
│    Time Dial: 5                │
│    Curve: Very Inverse         │
│                                │
│  Ground O/C (51G):             │
│    Pick-up: 240A (30%)         │
│    Time Dial: 3                │
│    Curve: Inverse              │
│                                │
│  Inst. O/C (50):               │
│    Pick-up: 4800A (6x)         │
│    Time Delay: Instantaneous   │
└────────────────────────────────┘
```

---

## 6. Metering and Instrumentation

### Current Transformers (CTs)

#### CT Representation and Specifications
```
Current Transformer:
    ──⊂⊃── or ──[CT]──

CT Specification Example:
┌────────────────────────────────┐
│  CT-1: Main Service Metering   │
│                                │
│  Ratio: 2000:5                 │
│  Accuracy Class: 0.3           │
│  Burden: B-0.5                 │
│  Rating Factor: 1.0            │
│  Application: Revenue Metering │
└────────────────────────────────┘

CT for Protection:
┌────────────────────────────────┐
│  CT-2: Main Breaker Protection │
│                                │
│  Ratio: 2000:5                 │
│  Accuracy Class: C200          │
│  Application: Breaker Trip     │
└────────────────────────────────┘
```

### Potential Transformers (PTs) / Voltage Transformers (VTs)

```
Potential Transformer:
    ──◇── or ──[PT]──

PT Specification:
┌────────────────────────────────┐
│  PT-1: Medium Voltage Metering │
│                                │
│  Ratio: 4160:120V              │
│  Accuracy Class: 0.3W          │
│  Burden: 200 VA                │
│  Connection: Wye-Wye           │
└────────────────────────────────┘
```

### Meters and Instruments

#### Standard Meter Symbols
```
Ammeter:           ──[A]──
Voltmeter:         ──[V]──
Wattmeter:         ──[W]──
Var Meter:         ──[VAR]──
Power Factor:      ──[PF]──
Frequency:         ──[Hz]──
kWh Meter:         ──[kWh]──
Demand Meter:      ──[kW-D]──
```

#### Comprehensive Metering Package
```
┌─────────────────────────────────────┐
│   MAIN SERVICE METERING PANEL       │
│                                     │
│   CT: 2000:5, Class 0.3            │
│   PT: 480V (Direct Connection)      │
│                                     │
│   Digital Multifunction Meter:      │
│   - Voltage (V-L, V-N)             │
│   - Current (Per Phase)             │
│   - Real Power (kW)                 │
│   - Reactive Power (kVAR)           │
│   - Apparent Power (kVA)            │
│   - Power Factor                    │
│   - Energy (kWh)                    │
│   - Demand (kW, 15-min interval)   │
│   - THD (Voltage & Current)        │
│   - Frequency                       │
│                                     │
│   Communication: Modbus RTU/TCP     │
│   Data Logging: 60-day buffer       │
└─────────────────────────────────────┘
```

---

## 7. Normal vs Emergency Power

### Emergency Power System (EPS) Classification

#### NEC Articles 700, 701, 702 Overview

| System Type | NEC Article | Transfer Time | Fuel Supply | Application |
|-------------|-------------|---------------|-------------|-------------|
| Emergency | 700 | 10 seconds | 2 hours min | Life safety (egress, fire alarm, etc.) |
| Legally Required Standby | 701 | 60 seconds | 2 hours min | Health/safety (HVAC, elevators, etc.) |
| Optional Standby | 702 | No requirement | No requirement | Comfort/convenience |

### Automatic Transfer Switch (ATS) Representation

#### Basic ATS Symbol
```
Simple ATS:
    Normal ──┬──/──┬── Emergency
             │  ATS │
           [LOAD]

Detailed ATS:
┌─────────────────────────────────────┐
│   AUTOMATIC TRANSFER SWITCH ATS-1   │
│                                     │
│  Rating: 400A, 3P, 480V             │
│  Type: Closed Transition            │
│  Transfer Time: <10 seconds         │
│  Bypass/Isolation: Yes              │
│  Normal Source: MSB-1, Ckt 3       │
│  Emergency Source: GEN-1            │
│  Control: Voltage/Frequency Sensing │
│  Time Delays:                       │
│    - Engine Start: 5 sec            │
│    - Transfer to Emgcy: 10 sec     │
│    - Return to Normal: 30 min      │
│    - Engine Cool Down: 5 min       │
│  Exercise Mode: Weekly, 30 min     │
└─────────────────────────────────────┘
```

### Emergency Power Distribution Diagram

```
UTILITY SERVICE                    EMERGENCY GENERATOR
480V, 3φ, 4W                      500kW, 480V, 3φ
     │                                   │
  ══╪══                               ══╪══
     │                                   │
┌────┴─────────┐                  ┌─────┴────────┐
│   MSB-1      │                  │   GEN-1      │
│   2000A Main │                  │   800A OCPD  │
└────┬─────────┘                  └─────┬────────┘
     │                                   │
     ├──────────────────┬────────────────┤
     │                  │                │
┌────┴──────┐     ┌────┴────┐     ┌────┴─────┐
│  NORMAL   │     │  ATS-1  │     │  ATS-2   │
│  LOADS    │     │  400A   │     │  225A    │
│           │     └────┬────┘     └────┬─────┘
│  DP-1     │          │               │
│  DP-2     │     ┌────┴────────┐ ┌────┴──────┐
│  LP-1     │     │ EMERGENCY   │ │  LEGALLY  │
│  LP-2     │     │ LOADS       │ │  REQUIRED │
└───────────┘     │  (Art 700)  │ │  STANDBY  │
                  │             │ │  (Art 701)│
                  │  Fire Alarm │ │           │
                  │  Egress Ltg │ │  HVAC-1   │
                  │  Exit Signs │ │  Elevator │
                  │  Fire Pump  │ │  Sump Pump│
                  └─────────────┘ └───────────┘

Legend:
────── Normal Power (Black)
══════ Emergency Power (Red)
- - - - Legally Required Standby (Red/Orange Dashed)
```

### UPS Systems

#### UPS Representation
```
┌──────────────────────────────────────┐
│    UPS SYSTEM UPS-1                  │
│                                      │
│  Rating: 100 kVA / 80 kW            │
│  Voltage: 480V Input, 208Y/120V Out │
│  Configuration: Online Double Conv  │
│  Battery: 30 min @ full load        │
│  Efficiency: 95% (Online)           │
│  Bypass: Internal Automatic         │
│  Maintenance Bypass: External       │
│                                      │
│  Normal ──┬──[RECTIFIER]──[BATTERY] │
│           │       │                  │
│           │   [INVERTER]──┬─→ LOAD  │
│           │               │          │
│           └──[BYPASS]─────┘          │
│                                      │
│  Critical Loads Fed:                 │
│    - Data Center                     │
│    - Server Rooms                    │
│    - Telecom Equipment               │
│    - Critical Process Controls       │
└──────────────────────────────────────┘
```

---

## 8. Layout and Organization

### One-Line Diagram Organization Principles

#### Top-Down Flow Convention
```
Standard Flow (Utility to Loads):

        UTILITY
           ↓
    SERVICE ENTRANCE
           ↓
     MAIN SWITCHBOARD
           ↓
    ┌──────┼──────┐
    ↓      ↓      ↓
  DIST   TRANS   MCC
  PANEL   FORM
    ↓      ↓      ↓
  BRANCH SECONDARY MOTORS
  CIRCUITS PANELS
```

#### Logical Grouping
```
Group equipment by:
1. Voltage level (MV → LV)
2. Function (Normal, Emergency, UPS)
3. Location (Building/Floor)
4. Load type (Power, Lighting, Mechanical)
```

### Title Block and Notes

#### Standard One-Line Title Block
```
┌─────────────────────────────────────────────────────────┐
│  PROJECT: ABC Commercial Building                       │
│  DRAWING: One-Line Diagram - Main Electrical Service    │
│  SHEET: E-100                                           │
│  DATE: 2025-01-22                                       │
│  ENGINEER: XYZ Engineering, PE #12345                   │
│  SCALE: Not to Scale                                    │
│  REVISION: A - Initial Issue                            │
│                                                          │
│  GENERAL NOTES:                                         │
│  1. All work shall comply with NEC 2023 and local codes│
│  2. Short circuit currents shown are at 480V           │
│  3. Protective device coordination per IEEE 242        │
│  4. Arc flash labels required per NFPA 70E            │
│  5. See panel schedules for branch circuit details     │
│  6. Voltage drop calculations per NEC 215.2(A)(3)     │
│                                                          │
│  ABBREVIATIONS:                                         │
│  AIC = Ampere Interrupting Capacity                    │
│  OCPD = Overcurrent Protective Device                  │
│  GFP = Ground Fault Protection                         │
│  SCCR = Short Circuit Current Rating                   │
│  LSI = Long-Short-Instantaneous                        │
└─────────────────────────────────────────────────────────┘
```

### Load Summary Tables

#### System Load Summary
```
┌──────────────────────────────────────────────────────────┐
│  LOAD SUMMARY - MAIN SERVICE                             │
├───────────────────┬──────────┬──────────┬───────────────┤
│  Load Category    │Connected │ Demand   │ Demand Factor │
│                   │   (kVA)  │  (kVA)   │      (%)      │
├───────────────────┼──────────┼──────────┼───────────────┤
│ Lighting          │   350    │   350    │     100%      │
│ Receptacles       │   420    │   252    │      60%      │
│ HVAC Equipment    │   950    │   950    │     100%      │
│ Motors/MCC        │   680    │   544    │      80%      │
│ Elevators         │   225    │   225    │     100%      │
│ Data Center       │   400    │   400    │     100%      │
│ Kitchen           │   285    │   228    │      80%      │
│ Misc. Equipment   │   175    │   140    │      80%      │
├───────────────────┼──────────┼──────────┼───────────────┤
│ TOTAL             │  3,485   │  3,089   │    88.6%      │
├───────────────────┼──────────┼──────────┼───────────────┤
│ Future/Spare (25%)│          │   772    │               │
├───────────────────┼──────────┼──────────┼───────────────┤
│ TOTAL w/ SPARE    │          │  3,861   │               │
└───────────────────┴──────────┴──────────┴───────────────┘

Service Size: 4800A at 480V, 3φ
               (3,861 kVA ÷ (480V × √3) = 4,641A → 4800A std)
```

### Short Circuit Current Table

```
┌─────────────────────────────────────────────────────────┐
│  SHORT CIRCUIT CURRENT SUMMARY                          │
├──────────────────────┬──────────┬──────────┬───────────┤
│  Bus Location        │ Voltage  │ 3φ Fault │ L-G Fault │
│                      │   (V)    │  (kA)    │   (kA)    │
├──────────────────────┼──────────┼──────────┼───────────┤
│ Utility Service Point│   480    │   65.0   │   58.2    │
│ MSB-1 Main Bus       │   480    │   62.8   │   56.3    │
│ DP-1 Main Lugs       │   480    │   18.5   │   16.7    │
│ T-1 Primary          │   480    │   58.4   │   52.4    │
│ T-1 Secondary        │   208    │   28.6   │   25.8    │
│ DP-2 (from T-1)      │   208    │   22.3   │   20.1    │
│ LP-1 Main Lugs       │   208    │   14.7   │   13.2    │
│ MCC-1 Bus            │   480    │   42.1   │   37.8    │
├──────────────────────┴──────────┴──────────┴───────────┤
│  Notes:                                                 │
│  1. Calculations per IEEE 141/242 methodology          │
│  2. Utility fault contribution: 65kA @ 480V (infinite) │
│  3. All OCPD ratings meet or exceed fault current      │
│  4. See calculation package for detailed analysis      │
└─────────────────────────────────────────────────────────┘
```

---

## 9. Common Mistakes and QA Checkpoints

### Critical Errors to Avoid

#### 1. Missing or Incorrect Equipment Ratings

**WRONG**:
```
┌─────────┐
│  DP-1   │
└─────────┘
```

**CORRECT**:
```
┌──────────────────────────────┐
│    DISTRIBUTION PANEL DP-1   │
│  Fed From: MSB-1, Ckt 1      │
│  Voltage: 208Y/120V, 3φ, 4W  │
│  Main Breaker: 400A, 3P      │
│  Bus Rating: 400A            │
│  SCCR: 22kAIC                │
│  Feeder: 500 kcmil Cu        │
└──────────────────────────────┘
```

#### 2. Inconsistent Voltage Designations

**WRONG**: Mixing 480V and 480Y/277V without clarification

**CORRECT**: Always specify:
- Voltage level
- Phase (1φ or 3φ)
- Wires (3W or 4W)
- Grounding (Y for wye, Δ for delta)

Examples:
- 480V, 3φ, 3W, Δ (no neutral)
- 480Y/277V, 3φ, 4W (with neutral)
- 208Y/120V, 3φ, 4W (most common)

#### 3. Missing Short Circuit Ratings

**WRONG**: Circuit breaker shown without AIC rating

**CORRECT**:
```
Main CB: 2000A, 3P, 65kAIC @ 480V
Available Fault Current: 62.8kA
```

All OCPD must have AIC ≥ available fault current at that point.

#### 4. Improper Transformer Information

**WRONG**:
```
T-1: 225 kVA
480V → 208V
```

**CORRECT**:
```
T-1: 225 kVA, 480Δ-208Y/120V
Impedance: 5.75%
Primary OCPD: 300A (NEC 450.3(B))
Secondary OCPD: 700A (NEC 450.3(B))
Temp Rise: 150°C, Dry Type, K-13
```

#### 5. Emergency Power Source Not Clearly Identified

**WRONG**: Using same line style for normal and emergency

**CORRECT**: Use red lines or dashed lines with "EMGCY" labels, show ATS ratings and transfer times

#### 6. Missing Grounding/Bonding Information

**ENSURE SHOWN**:
- Main bonding jumper location
- System grounding electrode conductor size
- Equipment grounding conductor routing
- Separately derived system bonding
- Grounding symbols at appropriate locations

### QA Checklist for One-Line Diagrams

#### Design Completeness
- [ ] All equipment properly labeled with unique identifiers
- [ ] Voltage levels clearly marked throughout
- [ ] All OCPD have ratings (amps, poles, AIC)
- [ ] Transformer sizes, voltages, impedances shown
- [ ] Feeder sizes and lengths documented
- [ ] Short circuit currents calculated and shown
- [ ] Bus ratings and SCCR values indicated
- [ ] Load summary table included
- [ ] Emergency power sources clearly differentiated

#### NEC Compliance
- [ ] Transformer protection per NEC 450.3
- [ ] Feeder protection per NEC 215.3, 240.4
- [ ] Service entrance per NEC Article 230
- [ ] Emergency systems per NEC 700
- [ ] Legally required standby per NEC 701
- [ ] Ground fault protection per NEC 230.95, 215.10
- [ ] OCPD series ratings verified if used

#### Coordination Study Support
- [ ] All OCPD types identified (thermal-mag, electronic trip)
- [ ] Time-current curve references noted
- [ ] CT ratios shown for relayed breakers
- [ ] Relay settings documented
- [ ] Selective coordination notes included

#### Arc Flash Study Support
- [ ] Working distances noted for equipment
- [ ] Bus ratings/configurations clear
- [ ] Fault current at each bus calculated
- [ ] Equipment boundaries defined
- [ ] Arc flash label locations identified

#### Drafting Standards
- [ ] Standard symbols per IEEE 315 used
- [ ] Line weights appropriate for voltage levels
- [ ] Logical top-down or left-right flow
- [ ] Title block complete with project info
- [ ] General notes and abbreviations listed
- [ ] Revision block with dates and descriptions
- [ ] Legend/symbol key provided
- [ ] Drawing cross-references correct

---

## 10. Calculation Examples

### Example 1: Feeder Sizing Calculation

**Given**:
- Panel DP-1 load: 320A demand at 208Y/120V
- Distance from MSB-1 to DP-1: 175 feet
- Conductor: Copper, THHN/THWN, 75°C terminations
- Conduit: Steel EMT
- Voltage drop limit: 2% feeder (NEC 215.2(A)(3) recommendation)

**Step 1: Conductor Ampacity (NEC 215.2, 310.16)**
```
Required ampacity: 320A
Termination temperature: 75°C (NEC 110.14(C))

From NEC Table 310.16 (75°C column):
- 350 kcmil Cu: 310A (too small)
- 400 kcmil Cu: 335A (too small)
- 500 kcmil Cu: 380A ✓

Base conductor size: 500 kcmil Cu (before adjustments)
```

**Step 2: Adjustment Factors**
```
Assume:
- 3 current-carrying conductors (no derating needed for 3-wire)
- Ambient temperature: 30°C (86°F) - no adjustment
- More than 3 CCCs in conduit: Not applicable

Adjusted ampacity: 380A (no derating required)
```

**Step 3: Voltage Drop Calculation**
```
Formula: VD% = (K × I × L × 2) / (CM × V)

Where:
K = 12.9 (copper constant for 3-phase)
I = 320A (load current)
L = 175 feet (one-way length)
CM = 500,000 circular mils
V = 208V (line-to-line voltage)

VD% = (12.9 × 320 × 175 × 2) / (500,000 × 208)
VD% = 1,435,200 / 104,000,000
VD% = 1.38%

Voltage drop: 1.38% < 2% ✓
```

**Step 4: OCPD Selection (NEC 240.4)**
```
Conductor ampacity: 380A
Next standard OCPD: 400A (NEC 240.6)

Selected OCPD: 400A, 3-pole circuit breaker
```

**Step 5: Conduit Size (NEC Chapter 9, Annex C)**
```
Conductors:
- (3) 500 kcmil THHN/THWN
- (1) 3/0 AWG Cu equipment grounding conductor (NEC 250.122)

From NEC Annex C, Table C1 (EMT):
- 3" EMT: Maximum 3 conductors at 500 kcmil ✓
- Verify 3/0 EGC fits: Yes ✓

Conduit size: 3" EMT
```

**Final Specification**:
```
FEEDER TO DP-1:
- OCPD: 400A, 3P circuit breaker at MSB-1
- Conductor: (3) 500 kcmil Cu THHN/THWN + (1) 3/0 Cu EGC
- Conduit: 3" EMT
- Length: 175 feet
- Voltage Drop: 1.38% @ 320A load
```

### Example 2: Transformer Primary/Secondary Protection

**Given**:
- Transformer: 225 kVA, 480V Δ primary - 208Y/120V secondary
- Impedance: 5.75%
- Type: Dry type

**Step 1: Primary OCPD (NEC 450.3(B), Table 450.3(B))**
```
Primary Current = kVA / (V × √3)
Primary Current = 225,000 / (480 × 1.732)
Primary Current = 270.6A

Per NEC 450.3(B) for ≥1000V up to ≤1000V transformers:
- Primary protection: 125% if secondary protection provided
- Maximum: 125% × 270.6A = 338.3A

Next standard OCPD below 338.3A: 300A (NEC 240.6)
Next standard OCPD above if 300A insufficient: 350A (allowed)

Selected Primary OCPD: 300A, 3P
```

**Step 2: Secondary OCPD (NEC 450.3(B))**
```
Secondary Current = kVA / (V × √3)
Secondary Current = 225,000 / (208 × 1.732)
Secondary Current = 624.6A

Per NEC 450.3(B):
- Secondary protection: 125% maximum
- Maximum: 125% × 624.6A = 780.8A

Next standard OCPD: 700A or 800A (NEC 240.6)

Selected Secondary OCPD: 700A, 3P
```

**Step 3: Verify Short Circuit Protection**
```
Available fault current at transformer secondary:
Let Z = Transformer impedance = 5.75%

Full load current: 624.6A
Fault current (approximate): I_FL / Z
Fault current = 624.6A / 0.0575 = 10,862A

Required AIC for secondary OCPD: ≥ 10,862A
Standard rating: 14kAIC or 22kAIC ✓
```

**One-Line Representation**:
```
                 480V, 3φ
                    │
              ──┤300A├──  (Primary OCPD)
                    │
                    │
            ┌───────┴────────┐
            │  TRANSFORMER   │
            │      T-1       │
            │   225 kVA      │
            │   480Δ-208Y    │
            │   Z = 5.75%    │
            └───────┬────────┘
                    │
              ──┤700A├──  (Secondary OCPD)
                    │
                 208Y/120V
```

### Example 3: Emergency Generator Sizing

**Given**:
- Emergency loads per NEC 700: 125 kVA
- Legally required standby per NEC 701: 85 kVA
- Optional standby per NEC 702: 60 kVA
- System: 480V, 3φ

**Step 1: Calculate Required Generator Capacity**
```
Priority 1 - Emergency (NEC 700): 125 kVA (mandatory)
Priority 2 - Legally Required (NEC 701): 85 kVA (mandatory)
Priority 3 - Optional (NEC 702): 60 kVA (optional)

Mandatory load: 125 + 85 = 210 kVA
Optional load: 60 kVA
Total: 270 kVA

Add margin for motor starting (largest motor):
Largest motor: 50 HP = ~48 kVA @ 0.85 PF
Starting: 48 kVA × 6 (typical DOL) = 288 kVA momentary
Continuous margin: Add 25% = 210 × 1.25 = 262.5 kVA

Select standard generator size: 300 kVA minimum
Recommended with optional loads: 350-400 kVA
```

**Step 2: Generator Specifications**
```
Generator Rating: 350 kVA / 280 kW (0.8 PF)
Voltage: 480V, 3φ, 4W
Type: Diesel engine
Starting: Automatic, <10 seconds (NEC 700.12)
Fuel tank: 300 gallons minimum (2+ hours @ full load, NEC 700.12(B)(2))
Runtime @ full load: 12 hours minimum
```

**Step 3: Generator OCPD**
```
Generator full load current:
I = kVA / (V × √3)
I = 350,000 / (480 × 1.732)
I = 421A

Generator OCPD sizing (NEC 445.13):
- Generator with overcurrent protection: 115-125% of nameplate
- Selected OCPD: 500A, 3P, 65kAIC

Generator breaker: 500A, 3P
```

**Step 4: Transfer Switch Sizing**
```
Emergency loads (NEC 700): 125 kVA = 150A
Legally required (NEC 701): 85 kVA = 102A

Total continuous current: 150A + 102A = 252A
ATS rating: 252A × 1.25 = 315A minimum

Selected ATS: 400A, 3P, 480V
Type: Automatic, closed transition
Transfer time: <10 seconds (NEC 700.12)
```

**One-Line Summary**:
```
┌────────────────────────────┐
│   GENERATOR GEN-1          │
│   350 kVA, 480V, 3φ       │
│   Diesel, Auto Start       │
│   Generator CB: 500A       │
└──────────┬─────────────────┘
           │
     ┌─────┴─────┬──────────┐
     │           │          │
  ──┤ATS-1├── ──┤ATS-2├── ──┤ATS-3├──
   400A       225A       100A
     │           │          │
  EMGCY-1    EMGCY-2    OPT-STB
 (NEC 700)  (NEC 701)  (NEC 702)
```

---

## Summary

One-line diagrams are the foundational electrical engineering document for power distribution systems. Proper application of IEEE/ANSI standards, comprehensive equipment specifications, clear voltage level representation, and thorough annotation ensures successful project execution and long-term system maintainability.

**Key Takeaways**:
1. Use standard symbols per IEEE 315
2. Annotate all equipment with complete ratings
3. Show short circuit currents and protective device coordination
4. Differentiate emergency/standby power with color coding
5. Include comprehensive notes, load summaries, and calculation tables
6. Follow systematic QA checklist before issuing drawings
7. Maintain consistency across all electrical drawings
8. Support downstream studies (coordination, arc flash, load flow)

**References**:
- IEEE Std 315-1975 (R1993) - Graphic Symbols
- IEEE Std 141 - Red Book (Industrial)
- IEEE Std 241 - Gray Book (Commercial)
- IEEE Std 242 - Buff Book (Protection & Coordination)
- NFPA 70 (NEC) - National Electrical Code
- IEEE Std 1584 - Arc Flash Hazard Calculation

---

*Document maintained by: Power Distribution Engineering Team*
*Next review date: 2026-01-22*
