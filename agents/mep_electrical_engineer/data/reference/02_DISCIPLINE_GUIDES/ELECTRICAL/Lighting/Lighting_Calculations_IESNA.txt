# Lighting Calculations - IESNA/IES Standards
## Comprehensive Guide to Illuminance Design and Energy Code Compliance

**Document Version**: 1.0
**Last Updated**: 2025-01-22
**Applicable Standards**: IES RP-1-21, ASHRAE 90.1-2022, IECC 2021, California Title 24, NFPA 101
**Code References**: NEC Articles 210.70, 220.12, 220.14(K), IBC Chapter 12

---

## Table of Contents

1. [Introduction and Fundamental Concepts](#introduction-and-fundamental-concepts)
2. [Illuminance Levels by Space Type](#illuminance-levels-by-space-type)
3. [Lumen Method Calculations](#lumen-method-calculations)
4. [Point-by-Point Calculation Method](#point-by-point-calculation-method)
5. [Lighting Power Density (LPD) Calculations](#lighting-power-density-lpd-calculations)
6. [Emergency and Egress Lighting](#emergency-and-egress-lighting)
7. [Lighting Controls and Zoning](#lighting-controls-and-zoning)
8. [Advanced Topics](#advanced-topics)
9. [Calculation Examples](#calculation-examples)
10. [Quality Assurance Checklist](#quality-assurance-checklist)

---

## 1. Introduction and Fundamental Concepts

### Photometric Quantities and Units

#### Basic Definitions

| Quantity | Symbol | Unit | Definition |
|----------|--------|------|------------|
| Luminous Flux | Φ (phi) | lumen (lm) | Total light output from source |
| Luminous Intensity | I | candela (cd) | Light intensity in specific direction |
| Illuminance | E | lux (lx) or footcandle (fc) | Light falling on surface |
| Luminance | L | cd/m² or fL | Light reflected/emitted from surface |
| Luminous Efficacy | η (eta) | lm/W | Efficiency of light source |

**Key Conversion**:
```
1 footcandle (fc) = 10.764 lux (lx)
1 lux (lx) = 0.0929 footcandles (fc)

Common approximation: 1 fc ≈ 10 lx
```

#### Light Source Characteristics

**Efficacy Comparison**:
```
┌────────────────────────────┬──────────┬───────────┬─────────┐
│ Light Source               │ Efficacy │ CRI       │ CCT (K) │
│                            │ (lm/W)   │           │         │
├────────────────────────────┼──────────┼───────────┼─────────┤
│ Incandescent               │  10-17   │ 95-100    │ 2700    │
│ Halogen                    │  15-25   │ 95-100    │ 3000    │
│ T8 Fluorescent             │  75-95   │ 75-85     │ 3500-5000│
│ Compact Fluorescent (CFL)  │  50-70   │ 80-85     │ 2700-6500│
│ Metal Halide               │  70-115  │ 65-90     │ 3000-6000│
│ High Pressure Sodium       │  85-140  │ 20-25     │ 2100    │
│ LED (Standard)             │  80-120  │ 70-90     │ 2700-6500│
│ LED (High Performance)     │ 120-180  │ 80-95     │ 2700-6500│
└────────────────────────────┴──────────┴───────────┴─────────┘

CRI = Color Rendering Index (100 = perfect color rendition)
CCT = Correlated Color Temperature (Kelvin)
```

### Design Criteria Fundamentals

#### Age and Maintenance Factors

**Light Loss Factors (LLF)**:
```
LLF = LLD × LDD × BF × RSDD

Where:
LLD  = Lamp Lumen Depreciation (typically 0.85-0.95)
LDD  = Luminaire Dirt Depreciation (0.80-0.95 depending on environment)
BF   = Ballast/Driver Factor (0.95-1.00)
RSDD = Room Surface Dirt Depreciation (0.90-0.98)

Typical combined LLF values:
- Clean environment (office): 0.85
- Normal environment (retail): 0.80
- Dirty environment (warehouse): 0.70
- Very dirty (industrial): 0.60
```

**Luminaire Dirt Depreciation by Environment**:
```
┌──────────────────┬───────────┬────────────────────────┐
│ Environment      │ Category  │ LDD @ 24 mo (typical) │
├──────────────────┼───────────┼────────────────────────┤
│ Very Clean       │ I         │ 0.95                   │
│ Clean            │ II        │ 0.91                   │
│ Medium           │ III       │ 0.88                   │
│ Dirty            │ IV        │ 0.83                   │
│ Very Dirty       │ V         │ 0.75                   │
└──────────────────┴───────────┴────────────────────────┘

Cleaning intervals: 12-36 months typical
```

---

## 2. Illuminance Levels by Space Type

### IES Recommended Illuminance Levels

Based on **IES RP-1-21 (Recommended Practice for Office Lighting)** and related standards.

#### Commercial/Office Spaces

```
┌─────────────────────────────────┬──────────────┬──────────────┐
│ Space Type                      │ Illuminance  │ IES Category │
│                                 │ (fc / lx)    │              │
├─────────────────────────────────┼──────────────┼──────────────┤
│ OFFICES                         │              │              │
│  Conference rooms               │ 30 / 300     │ D            │
│  Open office                    │ 30-50 / 300-500│ D-E        │
│  Private offices                │ 30-50 / 300-500│ D-E        │
│  Computer work areas            │ 30 / 300     │ D            │
│  Corridors/lobbies              │ 10-20 / 100-200│ B-C        │
│                                 │              │              │
│ RETAIL                          │              │              │
│  Circulation areas              │ 30 / 300     │ D            │
│  Feature displays               │ 150-300 / 1500-3000│ F-G  │
│  Sales areas                    │ 50 / 500     │ E            │
│  Dressing rooms                 │ 50 / 500     │ E            │
│                                 │              │              │
│ EDUCATIONAL                     │              │              │
│  Classrooms                     │ 30-50 / 300-500│ D-E        │
│  Lecture halls                  │ 50-75 / 500-750│ E-F        │
│  Laboratories                   │ 75-100 / 750-1000│ F-G     │
│  Libraries - reading            │ 30-50 / 300-500│ D-E        │
│  Libraries - stacks             │ 20-30 / 200-300│ C-D        │
│                                 │              │              │
│ HEALTHCARE                      │              │              │
│  Patient rooms (general)        │ 10-20 / 100-200│ B-C        │
│  Patient rooms (exam)           │ 50-100 / 500-1000│ E-F     │
│  Operating rooms                │ 200-500 / 2000-5000│ G-H   │
│  Laboratories                   │ 75-100 / 750-1000│ F-G     │
│  Nurses' stations               │ 50 / 500     │ E            │
│                                 │              │              │
│ HOSPITALITY                     │              │              │
│  Hotel lobby                    │ 10-20 / 100-200│ B-C        │
│  Hotel guest rooms              │ 10-30 / 100-300│ B-D        │
│  Restaurant dining              │ 10-30 / 100-300│ B-D        │
│  Kitchen preparation            │ 75 / 750     │ F            │
│  Kitchen cooking                │ 50 / 500     │ E            │
│                                 │              │              │
│ INDUSTRIAL/WAREHOUSE            │              │              │
│  Low bay storage (<20' ceiling) │ 20-30 / 200-300│ C-D        │
│  High bay storage (>20' ceiling)│ 10-20 / 100-200│ B-C        │
│  Assembly - rough               │ 50 / 500     │ E            │
│  Assembly - fine                │ 100-200 / 1000-2000│ G     │
│  Inspection - detailed          │ 200-500 / 2000-5000│ G-H   │
│                                 │              │              │
│ PARKING                         │              │              │
│  Parking garage - active        │ 5-10 / 50-100│ A-B          │
│  Parking garage - inactive      │ 1-2 / 10-20  │ Below A      │
│  Surface parking                │ 1-2 / 10-20  │ Below A      │
└─────────────────────────────────┴──────────────┴──────────────┘

Note: Illuminance measured at task height (typically 30" AFF for horizontal tasks)
```

#### Age-Adjusted Illuminance Targets

```
For occupants under 40 years: Use base values above
For occupants 40-55 years: Increase by 1.5×
For occupants over 55 years: Increase by 2×

Example:
Office general lighting base: 30 fc
Senior living facility office: 30 × 2 = 60 fc
```

### Uniformity Requirements

**Uniformity Ratio** = Minimum illuminance / Average illuminance

```
┌─────────────────────────────┬──────────────────┐
│ Space Type                  │ Max Ratio        │
│                             │ (Avg:Min)        │
├─────────────────────────────┼──────────────────┤
│ General office lighting     │ 3:1 to 5:1       │
│ Task lighting               │ 3:1              │
│ Computer areas              │ 3:1              │
│ Sports/gymnasium            │ 2:1 to 3:1       │
│ Parking structures          │ 10:1 maximum     │
└─────────────────────────────┴──────────────────┘

IES recommendation: Strive for 3:1 or better in task areas
```

---

## 3. Lumen Method Calculations

### Zonal Cavity Method (Most Common)

The zonal cavity method divides a room into three cavities for calculation purposes:

```
┌──────────────────────────────────┐ Ceiling (Rc = ceiling reflectance)
│ CEILING CAVITY (hcc)             │
├──────────────────────────────────┤ Luminaire mounting plane
│                                  │
│ ROOM CAVITY (hrc)                │ ← Working plane (typically 30" AFF)
│                                  │
├──────────────────────────────────┤ Working plane
│ FLOOR CAVITY (hfc)               │
└──────────────────────────────────┘ Floor (Rf = floor reflectance)

Where:
hcc = Height of ceiling cavity (ceiling to luminaire)
hrc = Height of room cavity (luminaire to work plane)
hfc = Height of floor cavity (floor to work plane)
```

### Step-by-Step Lumen Method Procedure

#### Step 1: Determine Room Dimensions and Reflectances

```
Room length: L (feet)
Room width: W (feet)
Room area: A = L × W (square feet)

Ceiling height: HC
Luminaire mounting height: HM
Work plane height: HW (typically 2.5 ft or 30")

Calculate cavity heights:
hcc = HC - HM
hrc = HM - HW
hfc = HW
```

**Typical Reflectance Values**:
```
┌──────────────────────┬───────────────────────┐
│ Surface              │ Reflectance (%)       │
├──────────────────────┼───────────────────────┤
│ Ceiling              │                       │
│  - White/light       │ 80-90%                │
│  - Medium            │ 50-70%                │
│  - Dark              │ 30-50%                │
│                      │                       │
│ Walls                │                       │
│  - Light colors      │ 50-70%                │
│  - Medium colors     │ 30-50%                │
│  - Dark colors       │ 10-30%                │
│                      │                       │
│ Floor                │                       │
│  - Light (concrete)  │ 20-30%                │
│  - Medium (carpet)   │ 10-20%                │
│  - Dark (tile)       │ 5-10%                 │
└──────────────────────┴───────────────────────┘
```

#### Step 2: Calculate Room Cavity Ratio (RCR)

```
Formula:
RCR = (5 × hrc × (L + W)) / (L × W)

Simplified for square rooms:
RCR = (10 × hrc) / L

RCR interpretation:
- RCR < 1: Very open space, high ceilings
- RCR 1-3: Normal office/commercial spaces
- RCR 3-5: Lower ceilings or smaller rooms
- RCR > 5: Tight spaces, requires more luminaires
```

#### Step 3: Determine Effective Ceiling/Floor Cavity Reflectances

For most applications with recessed or surface-mounted luminaires:
```
ρcc (ceiling cavity reflectance) = ρc (ceiling reflectance)
ρfc (floor cavity reflectance) = ρf (floor reflectance) × 0.2 (approximate)

For pendant-mounted luminaires:
Calculate Ceiling Cavity Ratio (CCR):
CCR = (5 × hcc × (L + W)) / (L × W)

Use CCR and wall reflectance to find effective ρcc from IES tables
```

#### Step 4: Find Coefficient of Utilization (CU)

The CU is obtained from manufacturer's photometric data tables based on:
- Room Cavity Ratio (RCR)
- Effective ceiling reflectance (ρcc)
- Wall reflectance (ρw)

**Example CU Table** (Sample luminaire):
```
Luminaire: 2×4 LED Troffer, Direct Distribution
Light distribution: 0% up, 100% down

┌─────┬────────────────────────────────────────────────┐
│ RCR │  Effective Ceiling Reflectance = 80%          │
│     ├───────────┬───────────┬───────────┬───────────┤
│     │ Wall Refl │ Wall Refl │ Wall Refl │ Wall Refl │
│     │   70%     │   50%     │   30%     │   10%     │
├─────┼───────────┼───────────┼───────────┼───────────┤
│  1  │   0.67    │   0.63    │   0.60    │   0.57    │
│  2  │   0.59    │   0.54    │   0.50    │   0.47    │
│  3  │   0.52    │   0.47    │   0.43    │   0.40    │
│  4  │   0.46    │   0.41    │   0.37    │   0.34    │
│  5  │   0.41    │   0.36    │   0.32    │   0.29    │
│  6  │   0.37    │   0.32    │   0.28    │   0.25    │
│  7  │   0.33    │   0.28    │   0.24    │   0.22    │
│  8  │   0.30    │   0.25    │   0.21    │   0.19    │
│  9  │   0.27    │   0.22    │   0.19    │   0.17    │
│ 10  │   0.24    │   0.20    │   0.17    │   0.15    │
└─────┴───────────┴───────────┴───────────┴───────────┘
```

#### Step 5: Calculate Number of Luminaires Required

```
Formula:
N = (E × A) / (F × CU × LLF)

Where:
N = Number of luminaires required
E = Target illuminance (footcandles)
A = Room area (square feet)
F = Initial lumens per luminaire
CU = Coefficient of utilization (from manufacturer data)
LLF = Light loss factor (typically 0.70-0.85)

Rearranged to find illuminance from given number of luminaires:
E = (N × F × CU × LLF) / A
```

### Complete Lumen Method Example

**Given**:
- Office space: 40 ft × 60 ft = 2,400 sq ft
- Ceiling height: 9 ft
- Work plane height: 2.5 ft
- Luminaire: 2×4 LED troffer, 5000 lumens
- Reflectances: Ceiling 80%, Walls 50%, Floor 20%
- Light loss factor: 0.85
- Target illuminance: 35 fc

**Step 1: Calculate cavity heights**
```
hcc = 0 (recessed luminaires)
hrc = 9.0 - 2.5 = 6.5 ft
hfc = 2.5 ft
```

**Step 2: Calculate RCR**
```
RCR = (5 × hrc × (L + W)) / (L × W)
RCR = (5 × 6.5 × (40 + 60)) / (40 × 60)
RCR = (5 × 6.5 × 100) / 2400
RCR = 3250 / 2400
RCR = 1.35 ≈ 1.4
```

**Step 3: Determine CU**
```
From table (interpolating between RCR 1 and 2):
RCR = 1.4, ρc = 80%, ρw = 50%

At RCR 1: CU = 0.63
At RCR 2: CU = 0.54
Interpolated: CU = 0.63 - (0.4 × (0.63 - 0.54)) = 0.594 ≈ 0.59
```

**Step 4: Calculate number of luminaires**
```
N = (E × A) / (F × CU × LLF)
N = (35 × 2400) / (5000 × 0.59 × 0.85)
N = 84,000 / 2507.5
N = 33.5 luminaires

Round up: 34 luminaires required
```

**Step 5: Verify achieved illuminance**
```
E = (N × F × CU × LLF) / A
E = (34 × 5000 × 0.59 × 0.85) / 2400
E = 85,255 / 2400
E = 35.5 fc ✓ (Meets 35 fc target)
```

**Step 6: Layout spacing**
```
Area per luminaire: 2400 / 34 = 70.6 sq ft per fixture

Recommended spacing-to-mounting-height ratio for general lighting: 1.3-1.5
Luminaire mounting height above work plane: 6.5 ft
Maximum spacing: 6.5 × 1.5 = 9.75 ft

Layout suggestion: 6 rows × 6 columns = 36 luminaires (provides better uniformity)
Spacing: 40/6 = 6.67 ft × 60/6 = 10 ft
(Spacing slightly exceeds recommended; consider 6×7 = 42 total for better uniformity)

Final layout: 7 rows × 6 columns = 42 luminaires
Row spacing: 40/7 = 5.71 ft
Column spacing: 60/6 = 10.0 ft
```

---

## 4. Point-by-Point Calculation Method

### When to Use Point-by-Point

Use point-by-point method for:
- Irregular room shapes
- Accent/task lighting design
- Outdoor area lighting
- Sports lighting
- Verification of uniformity
- Detailed lighting analysis

### Basic Point-by-Point Formula

#### Horizontal Illuminance from Point Source

```
E = (I × cos³θ) / d²

Where:
E = Illuminance at point (footcandles or lux)
I = Luminous intensity in direction of point (candelas)
θ = Angle between luminaire axis and point (degrees)
d = Direct distance from luminaire to point (feet or meters)
```

#### Simplified for Direct Illumination

```
E_h = (I_0 × H³) / D⁵

Where:
E_h = Horizontal illuminance at calculation point
I_0 = Luminous intensity at nadir (0° vertical, candelas)
H = Mounting height above work plane (feet)
D = Direct distance from luminaire to point (feet)
    D = √(H² + r²), where r = horizontal distance from luminaire

Alternative formula using angles:
E_h = (I_θ / d²) × cos θ

Where:
I_θ = Intensity at angle θ from nadir
d = Direct distance
θ = Angle from nadir
```

### Obtaining Luminaire Intensity Data

Intensity values are obtained from manufacturer's **candela distribution tables** or **candlepower distribution curves**.

**Example Candela Distribution** (Floodlight):
```
┌────────────────────────────────────────────────────┐
│ Vertical Angle (degrees from nadir)               │
├───────┬────────────────────────────────────────────┤
│ Angle │ Candela Intensity at Horizontal Angles    │
│  (θ)  ├─────┬─────┬─────┬─────┬─────┬─────┬──────┤
│       │  0° │ 15° │ 30° │ 45° │ 60° │ 75° │  90° │
├───────┼─────┼─────┼─────┼─────┼─────┼─────┼──────┤
│   0°  │15000│15000│15000│15000│15000│15000│15000 │
│  10°  │14500│14500│14400│14300│14200│14000│13800 │
│  20°  │13000│12900│12700│12400│12000│11500│11000 │
│  30°  │10500│10300│10000│ 9500│ 8900│ 8200│ 7500 │
│  40°  │ 7500│ 7300│ 7000│ 6500│ 5900│ 5200│ 4500 │
│  50°  │ 4500│ 4300│ 4000│ 3600│ 3100│ 2500│ 2000 │
│  60°  │ 2000│ 1900│ 1700│ 1500│ 1200│  900│  600 │
│  70°  │  800│  750│  650│  550│  400│  250│  100 │
│  80°  │  200│  180│  150│  100│   50│   20│   10 │
│  90°  │    0│    0│    0│    0│    0│    0│    0 │
└───────┴─────┴─────┴─────┴─────┴─────┴─────┴──────┘

Total lumens: 850,000 (from photometric test report)
```

### Complete Point-by-Point Calculation Example

**Given**:
- Parking lot lighting
- Luminaire: 250W LED area light, 35,000 lumens
- Mounting height: 30 feet
- Calculate illuminance at point 40 feet horizontally from pole

**Step 1: Determine geometry**
```
Mounting height: H = 30 ft
Horizontal distance: r = 40 ft
Direct distance: D = √(H² + r²) = √(30² + 40²) = √(900 + 1600) = √2500 = 50 ft

Angle from nadir:
tan θ = r / H = 40 / 30 = 1.333
θ = arctan(1.333) = 53.1°
```

**Step 2: Get intensity from candela table**
```
From manufacturer data at θ = 53° (interpolating at 50° and 60°):
I_50° = 4500 cd
I_60° = 2000 cd

Linear interpolation:
I_53° = 4500 - ((53-50)/(60-50)) × (4500-2000)
I_53° = 4500 - (0.3 × 2500) = 4500 - 750 = 3750 cd
```

**Step 3: Calculate horizontal illuminance**
```
Method 1 - Basic formula:
E_h = (I_θ / d²) × cos θ
E_h = (3750 / 50²) × cos(53.1°)
E_h = (3750 / 2500) × 0.600
E_h = 1.5 × 0.600 = 0.90 fc

Method 2 - Alternative formula:
E_h = (I_θ × cos³θ) / d²
E_h = (3750 × 0.600³) / 2500
E_h = (3750 × 0.216) / 2500
E_h = 810 / 2500 = 0.324 fc

[Use Method 1 for direct component; Method 2 includes additional geometric factors]
```

**Step 4: Consider multiple luminaires**
```
For uniformity, calculate illuminance contribution from multiple poles:
- Direct luminaire overhead: E1
- Adjacent luminaires: E2, E3, E4, etc.

Total illuminance at point:
E_total = E1 + E2 + E3 + E4 + ...

Typical parking lot requirement: 1-2 fc maintained average
```

### Point-by-Point for Interior Spaces

**Vertical Illuminance Calculation** (for wall lighting):
```
E_v = (I_θ / d²) × sin θ

Where:
E_v = Vertical illuminance at point on wall
I_θ = Intensity at angle θ
d = Direct distance
θ = Angle from nadir

Use for:
- Display lighting
- Art gallery lighting
- Retail product lighting
- Signage illumination
```

---

## 5. Lighting Power Density (LPD) Calculations

### ASHRAE 90.1-2022 Overview

Lighting power density limits control energy consumption in buildings. Two compliance methods available:
1. **Building Area Method**: Simple, single LPD for entire building
2. **Space-by-Space Method**: More flexible, different LPD per space type

### Building Area Method

**ASHRAE 90.1-2022 Table 9.5.1** - Building Area Method LPDs:

```
┌─────────────────────────────────┬──────────────┬────────────┐
│ Building Area Type              │ LPD (W/ft²)  │ Notes      │
├─────────────────────────────────┼──────────────┼────────────┤
│ Automotive facility             │    0.67      │            │
│ Convention center               │    0.82      │            │
│ Courthouse                      │    0.88      │            │
│ Dining: bar lounge/leisure      │    0.75      │            │
│ Dining: cafeteria/fast food     │    0.40      │            │
│ Dining: family                  │    0.62      │            │
│ Dormitory                       │    0.50      │            │
│ Exercise center                 │    0.72      │            │
│ Gymnasium                       │    0.85      │            │
│ Healthcare/hospital             │    0.87      │            │
│ Hotel/motel                     │    0.82      │            │
│ Library                         │    0.96      │            │
│ Manufacturing facility          │    0.82      │            │
│ Motion picture theater          │    0.83      │            │
│ Multifamily                     │    0.41      │            │
│ Museum                          │    0.87      │            │
│ Office                          │    0.74      │   ← Most common │
│ Parking garage                  │    0.19      │            │
│ Penitentiary                    │    0.85      │            │
│ Performing arts theater         │    1.39      │            │
│ Police/fire station             │    0.71      │            │
│ Post office                     │    0.87      │            │
│ Religious building              │    0.91      │            │
│ Retail                          │    1.05      │            │
│ School/university               │    0.87      │            │
│ Sports arena                    │    0.78      │            │
│ Town hall                       │    0.88      │            │
│ Transportation                  │    0.50      │            │
│ Warehouse (storage)             │    0.45      │            │
│ Workshop                        │    1.26      │            │
└─────────────────────────────────┴──────────────┴────────────┘
```

**Building Area Method Calculation**:
```
Step 1: Determine building type
Step 2: Find LPD from Table 9.5.1
Step 3: Calculate allowed lighting power

Formula:
P_allowed = LPD × Area

Example - Office Building:
Building area: 50,000 sq ft
LPD limit: 0.74 W/ft²
P_allowed = 0.74 × 50,000 = 37,000 watts

Proposed lighting: 35,500 watts
Compliance: 35,500 < 37,000 ✓ COMPLIES
```

### Space-by-Space Method

**ASHRAE 90.1-2022 Table 9.6.1** - Space-by-Space Method LPDs (Selected):

```
┌──────────────────────────────────────┬─────────────┐
│ Space Type                           │ LPD (W/ft²) │
├──────────────────────────────────────┼─────────────┤
│ OFFICE SPACES                        │             │
│  Conference/meeting/multipurpose     │    1.11     │
│  Corridor/transition                 │    0.41     │
│  Enclosed office                     │    0.74     │
│  Open office                         │    0.61     │
│  Lobby - office/general              │    0.84     │
│  Restroom                            │    0.63     │
│  Stairway                            │    0.49     │
│  Storage - general                   │    0.38     │
│  Break room                          │    0.73     │
│  Copy/print room                     │    0.72     │
│  Electrical/mechanical room          │    0.43     │
│                                      │             │
│ RETAIL SPACES                        │             │
│  Sales area                          │    1.05     │
│  Dressing/fitting room               │    0.96     │
│  Mall concourse                      │    0.82     │
│                                      │             │
│ EDUCATION SPACES                     │             │
│  Classroom/lecture hall              │    1.00     │
│  Laboratory - science                │    1.11     │
│  Lobby - educational                 │    0.88     │
│  Corridor - educational              │    0.46     │
│                                      │             │
│ WAREHOUSE SPACES                     │             │
│  Fine material storage               │    0.84     │
│  Medium/bulky material storage       │    0.44     │
│  Loading dock (interior)             │    0.47     │
│                                      │             │
│ PARKING                              │             │
│  Parking area (interior)             │    0.15     │
│  Parking area (exterior)             │    0.04     │
└──────────────────────────────────────┴─────────────┘
```

**Space-by-Space Calculation Example**:

```
OFFICE BUILDING - 1ST FLOOR LAYOUT
┌─────────────────────┬────────────┬─────────────┬──────────────┐
│ Space               │ Area (SF)  │ LPD (W/ft²) │ Allowed (W)  │
├─────────────────────┼────────────┼─────────────┼──────────────┤
│ Open office area    │   5,000    │    0.61     │    3,050     │
│ 10 Enclosed offices │   1,500    │    0.74     │    1,110     │
│ 2 Conference rooms  │     800    │    1.11     │      888     │
│ Break room          │     400    │    0.73     │      292     │
│ Corridors           │   1,200    │    0.41     │      492     │
│ 4 Restrooms         │     600    │    0.63     │      378     │
│ Storage             │     300    │    0.38     │      114     │
│ IT/electrical room  │     200    │    0.43     │       86     │
├─────────────────────┼────────────┼─────────────┼──────────────┤
│ TOTAL               │  10,000    │    0.541*   │    5,410     │
└─────────────────────┴────────────┴─────────────┴──────────────┘

*Effective LPD = 5,410W / 10,000 SF = 0.541 W/ft²

Comparison to Building Area Method:
Building Area Method LPD for office: 0.74 W/ft²
Building Area Method allowance: 0.74 × 10,000 = 7,400W
Space-by-Space allowance: 5,410W

Space-by-Space method is more restrictive in this case, but allows
optimization of lighting design for actual space usage.
```

### Additional Lighting Power

**ASHRAE 90.1-2022 Section 9.6.2** - Additional Lighting Power Allowances:

```
┌────────────────────────────────────┬─────────────────────────┐
│ Application                        │ Additional Allowance    │
├────────────────────────────────────┼─────────────────────────┤
│ Retail display lighting (track/    │ 0.6 W/ft² of display    │
│ directional)                       │ area                    │
│                                    │                         │
│ Retail accent lighting for         │ 0.4 W/ft² of floor area │
│ special displays                   │                         │
│                                    │                         │
│ Decorative appearance (wall wash,  │ 0.2 W/linear foot of    │
│ cove, artistic)                    │ illuminated length      │
│                                    │                         │
│ Retail merchandise highlighting    │ 120W per luminaire      │
│                                    │ (max 120W each)         │
└────────────────────────────────────┴─────────────────────────┘
```

---

## 6. Emergency and Egress Lighting

### Code Requirements Overview

| Code | Section | Requirement |
|------|---------|-------------|
| IBC 2021 | 1008.3 | Means of egress illumination minimum 1 fc |
| IBC 2021 | 1008.3.5 | Emergency lighting duration 90 minutes minimum |
| NFPA 101 | 7.9 | Average 1 fc, minimum 0.1 fc along path of egress |
| NEC 2023 | 700.16 | Emergency system wiring separate and identified |

### Egress Lighting Calculations

#### Minimum Illuminance Requirements

```
MEANS OF EGRESS ILLUMINATION (IBC 1008.3):
┌─────────────────────────────────────┬──────────────────┐
│ Location                            │ Minimum Illum.   │
├─────────────────────────────────────┼──────────────────┤
│ Exit access (corridors, aisles)     │ 1.0 fc           │
│ Exit stairs                         │ 10.0 fc          │
│ Exit discharge                      │ 1.0 fc           │
│                                     │                  │
│ Per NFPA 101 (alternative):         │                  │
│  - Average along path               │ 1.0 fc           │
│  - Minimum at any point             │ 0.1 fc           │
│  - Maximum/minimum ratio            │ 40:1             │
└─────────────────────────────────────┴──────────────────┘

Measurement: At floor level in center of path of egress
```

#### Emergency Lighting Duration

```
NEC 700.12 / IBC 1008.3.5 Requirements:
┌────────────────────────────────────┬─────────────────┐
│ Occupancy/Application              │ Duration        │
├────────────────────────────────────┼─────────────────┤
│ Most buildings                     │ 90 minutes      │
│ Group I-2 (hospitals/nursing)      │ 4 hours minimum │
│ Group I-3 (detention/correctional) │ 4 hours minimum │
└────────────────────────────────────┴─────────────────┘

Power source options (NEC 700.12):
1. Storage battery within luminaire (integral)
2. Generator set (on-site)
3. Separate central battery system
4. UPS system
```

### Exit Sign Requirements

**NEC 700.15 / IBC 1013 / NFPA 101 7.10**:

```
EXIT SIGN SPECIFICATIONS:
┌────────────────────────────────────┬──────────────────────┐
│ Characteristic                     │ Requirement          │
├────────────────────────────────────┼──────────────────────┤
│ Letter height                      │ 6" minimum principal │
│                                    │ strokes, 3/4" wide   │
│ Visibility                         │ 100 ft min viewing   │
│ Illumination (internal)            │ 5 fc minimum on face │
│ Illumination (external)            │ 5 fc minimum on sign │
│ Color                              │ Red or green letters │
│                                    │ (red typical in US)  │
│ Emergency duration                 │ 90 minutes minimum   │
│ Directional indicators             │ Required where path  │
│                                    │ not obvious          │
│ Mounting height                    │ 80" to bottom        │
└────────────────────────────────────┴──────────────────────┘

LED exit sign power consumption: 2-5 watts typical
Incandescent exit sign: 20-40 watts (obsolete)
```

### Emergency Lighting Calculation Example

**Given**:
- Corridor: 8 ft wide × 100 ft long × 9 ft ceiling
- Emergency luminaires: LED, 900 lumens each, integral battery
- Required: 1.0 fc average, 0.1 fc minimum

**Step 1: Calculate required lumen output**
```
Area: 8 × 100 = 800 sq ft
Target: 1.0 fc average
Light loss factor (emergency): 0.90 (better maintained)
Coefficient of utilization: 0.40 (corridor, dark walls)

Total lumens required:
Φ = (E × A) / (CU × LLF)
Φ = (1.0 × 800) / (0.40 × 0.90)
Φ = 800 / 0.36
Φ = 2,222 lumens

Number of 900-lumen luminaires:
N = 2,222 / 900 = 2.47 → 3 luminaires minimum
```

**Step 2: Verify spacing**
```
3 luminaires in 100 ft corridor:
Spacing: 100 / 3 = 33.3 ft on center

Check uniformity with point-by-point at critical points:
- Midpoint between luminaires (worst case)
- 16.7 ft from nearest luminaire

Luminaire at mounting height 9 ft:
Distance to floor: d = √(9² + 16.7²) = √(81 + 279) = 19 ft

Intensity at 62° angle: ~150 cd (typical emergency luminaire)
E = (I × cos³θ) / d²
E = (150 × cos³(62°)) / 19²
E = (150 × 0.088) / 361
E = 0.037 fc

THIS FAILS - Below 0.1 fc minimum
```

**Step 3: Add additional luminaires**
```
Try 5 luminaires:
Spacing: 100 / 5 = 20 ft on center
Worst case: 10 ft from nearest luminaire

Distance: d = √(9² + 10²) = √(81 + 100) = 13.45 ft
Angle: θ = arctan(10/9) = 48°

E = (150 × cos³(48°)) / 13.45²
E = (150 × 0.296) / 181
E = 0.245 fc ✓ Exceeds 0.1 fc minimum

Consider contribution from second-nearest luminaire:
Distance: d2 = √(9² + 30²) = 31.4 ft
Angle: θ2 = 73°
Additional E2 ≈ 0.015 fc

Total: 0.245 + 0.015 = 0.26 fc ✓ ACCEPTABLE
```

---

## 7. Lighting Controls and Zoning

### ASHRAE 90.1 & Energy Code Control Requirements

**ASHRAE 90.1-2022 Section 9.4 - Mandatory Lighting Controls**:

```
┌──────────────────────────────────────┬───────────────────────┐
│ Control Type                         │ Requirement           │
├──────────────────────────────────────┼───────────────────────┤
│ Automatic Shutoff                    │ REQUIRED              │
│  - Occupancy sensors                 │ All spaces ≤ 300 SF   │
│  - Time-switch                       │ Alternative method    │
│  - Other automatic control           │ Alternative method    │
│                                      │                       │
│ Space Control                        │ REQUIRED              │
│  - Each space ≤ 2,500 SF             │ Separate control      │
│  - Each space > 2,500 SF             │ Control per 2,500 SF  │
│                                      │                       │
│ Daylight Control                     │ REQUIRED              │
│  - Primary sidelighting zone         │ Within 15 ft of window│
│  - Secondary sidelighting zone       │ 15-20 ft from window  │
│  - Toplighting zone                  │ Under skylight + 0.7× │
│                                      │ ceiling height        │
│                                      │                       │
│ Manual Control                       │ REQUIRED              │
│  - Individual/multi-occupant         │ Within 20 ft of space │
│  - Partitioned areas                 │ Separate control      │
│                                      │                       │
│ Additional Reductions                │                       │
│  - Partial-OFF switching             │ Reduce by 50% minimum │
│  - Multi-level switching             │ Uniform reduction     │
└──────────────────────────────────────┴───────────────────────┘
```

### Occupancy Sensor Application

**Sensor Types**:
```
┌─────────────────────┬──────────────────┬────────────────────┐
│ Technology          │ Best Application │ Coverage           │
├─────────────────────┼──────────────────┼────────────────────┤
│ Passive Infrared    │ Closed rooms     │ 900-1,200 SF       │
│ (PIR)               │ with line of     │ 20-30 ft radius    │
│                     │ sight            │                    │
│                     │                  │                    │
│ Ultrasonic (US)     │ Partitioned      │ 800-1,000 SF       │
│                     │ spaces, high     │ Penetrates barriers│
│                     │ ceilings         │                    │
│                     │                  │                    │
│ Dual Technology     │ Reduce false     │ 600-900 SF         │
│ (PIR + US)          │ trips, critical  │ Most reliable      │
│                     │ applications     │                    │
│                     │                  │                    │
│ Microwave           │ Large open       │ 2,000+ SF          │
│                     │ spaces           │                    │
└─────────────────────┴──────────────────┴────────────────────┘

Time Delays:
- ON delay: 0-5 seconds (prevent false activation)
- OFF delay: 15-30 minutes typical (office, classroom)
- Restroom OFF delay: 5-10 minutes (shorter occupancy)
- Warehouse OFF delay: 30-60 minutes (slower movement)
```

### Daylight Harvesting

**Daylight Zones per ASHRAE 90.1**:

```
SIDELIGHTING (Vertical Windows):
┌────────────────────────────────────────────────────┐
│                    Room Interior                   │
│                                                    │
│  ┌─────────┬──────────────┬──────────────────────┐│
│  │ Primary │  Secondary   │   Non-daylit Zone    ││
│  │ Daylit  │  Daylit      │                      ││
│  │  Zone   │   Zone       │                      ││
│  │  0-15'  │   15-20'     │      > 20'           ││
│  │         │              │                      ││
│  │ 100%    │ 50%          │   0%                 ││
│  │ credit  │ credit       │   credit             ││
│  └─────────┴──────────────┴──────────────────────┘│
│  |← Window →|                                     │
└────────────────────────────────────────────────────┘

TOPLIGHTING (Skylights):
Daylight zone = Skylight area + 0.7 × ceiling height horizontally

Example:
4 ft × 8 ft skylight = 32 SF
Ceiling height = 20 ft
Zone radius = 0.7 × 20 = 14 ft each direction
Daylight zone = 32 + [(14 + 14) × (8 + 8)] = 32 + 448 = 480 SF
```

**Daylight Control Methods**:
```
1. Stepped Dimming:
   - Full output
   - 50% output
   - 25% output
   - OFF

2. Continuous Dimming (0-10V or DALI):
   - Smooth dimming from 100% to minimum (typically 10%)
   - Photosensor feedback loop
   - More expensive but better energy savings

3. Automatic ON/OFF:
   - Simple switching
   - Least expensive
   - Less occupant satisfaction
```

### Lighting Control System Architecture

```
BASIC RELAY PANEL SYSTEM:
┌────────────────────────────────────────────────┐
│         Lighting Control Panel                 │
│                                                │
│  Time Clock ──→ [CONTROLLER] ←── Photosensor  │
│                      ↓                         │
│              [8-CH RELAY MODULE]               │
│               ↓   ↓   ↓   ↓                   │
└───────────────┼───┼───┼───┼────────────────────┘
                ↓   ↓   ↓   ↓
            Zone1 Zone2 Zone3 Zone4
            (Lights) (Lights) (Lights) (Lights)

ADVANCED BMS-INTEGRATED SYSTEM:
┌─────────────────────────────────────────────────┐
│             Building Management System          │
│                  (BACnet/IP)                    │
│                      ↓                          │
│         ┌────────────┴───────────────┐         │
│         ↓            ↓               ↓         │
│   [Room Controllers] [Gateway] [Photosensors]  │
│         ↓                                       │
│   DALI Bus / 0-10V                             │
│         ↓                                       │
│   LED Drivers (Individual Control)             │
└─────────────────────────────────────────────────┘
```

---

## 8. Advanced Topics

### Luminaire Efficacy and L70 Ratings

**LED Performance Metrics**:
```
L70 = Time to 70% of initial lumen output (LED lifespan metric)
L80 = Time to 80% of initial lumen output
L90 = Time to 90% of initial lumen output

Typical L70 ratings:
- Standard LED: 50,000 hours
- High-performance LED: 100,000 hours
- Industrial/high-bay LED: 150,000 hours

Calculation of maintenance factor for LEDs:
At rated life (e.g., 50,000 hrs @ L70):
LLD = 0.70

At half rated life (25,000 hrs):
LLD = 0.85 (approximate linear degradation)
```

### Color Temperature and CRI Selection

```
CORRELATED COLOR TEMPERATURE (CCT):
┌──────────────┬─────────┬────────────────────────────┐
│ Description  │ CCT (K) │ Application                │
├──────────────┼─────────┼────────────────────────────┤
│ Warm White   │ 2700-   │ Residential, hospitality,  │
│              │ 3000    │ restaurants                │
│              │         │                            │
│ Neutral White│ 3500-   │ Offices, retail, general   │
│              │ 4000    │ commercial                 │
│              │         │                            │
│ Cool White   │ 5000-   │ Healthcare, industrial,    │
│              │ 6500    │ task lighting              │
└──────────────┴─────────┴────────────────────────────┘

COLOR RENDERING INDEX (CRI):
┌────────────┬─────────┬──────────────────────────────┐
│ CRI Range  │ Quality │ Application                  │
├────────────┼─────────┼──────────────────────────────┤
│ 90-100     │ Excellent│ Art galleries, retail        │
│            │         │ high-end displays            │
│ 80-89      │ Good    │ Offices, schools, general    │
│            │         │ commercial                   │
│ 70-79      │ Fair    │ Warehouses, parking, areas   │
│            │         │ where color is less critical │
│ < 70       │ Poor    │ Avoid for occupied spaces    │
└────────────┴─────────┴──────────────────────────────┘

Special CRI Metrics:
- R9 (Red): Important for food, retail, healthcare
- TM-30: Advanced color fidelity metric (Rf, Rg values)
```

### Glare Control

**Unified Glare Rating (UGR)**:
```
UGR = 8 log₁₀ [(0.25/Lb) × Σ(L²ω/p²)]

Where:
Lb = Background luminance
L = Luminance of luminaire
ω = Solid angle of luminaire
p = Position index

UGR Limits:
┌──────────────────────────┬─────────────┐
│ Space Type               │ Max UGR     │
├──────────────────────────┼─────────────┤
│ Technical drawing        │ UGR ≤ 16    │
│ Offices, CAD work        │ UGR ≤ 19    │
│ Conference rooms         │ UGR ≤ 19    │
│ Libraries                │ UGR ≤ 19    │
│ Classrooms               │ UGR ≤ 19    │
│ General circulation      │ UGR ≤ 22    │
│ Workshops, laboratories  │ UGR ≤ 22    │
│ Warehouses               │ UGR ≤ 25    │
└──────────────────────────┴─────────────┘
```

---

## 9. Calculation Examples

### Complete Design Example: Small Office

**Project Data**:
- Space: Open office, 30 ft × 40 ft = 1,200 SF
- Ceiling: 9 ft, white (80% reflectance)
- Walls: Light gray (50% reflectance)
- Floor: Medium carpet (20% reflectance)
- Task: Computer work
- Target: 35 fc maintained

**Step 1: Select luminaire**
```
Luminaire: 2×4 LED troffer
- Lumen output: 5,000 lumens
- Wattage: 40W
- Efficacy: 125 lm/W
- CRI: 82
- CCT: 4000K
- Distribution: Direct (0% up, 100% down)
```

**Step 2: Calculate room cavity ratio**
```
hrc = 9.0 - 2.5 = 6.5 ft
RCR = (5 × 6.5 × (30 + 40)) / (30 × 40)
RCR = 2,275 / 1,200 = 1.90 ≈ 2.0
```

**Step 3: Determine CU**
```
From manufacturer data:
RCR = 2, ρc = 80%, ρw = 50%
CU = 0.54
```

**Step 4: Calculate number of luminaires**
```
LLF = 0.85 (clean office)

N = (E × A) / (F × CU × LLF)
N = (35 × 1,200) / (5,000 × 0.54 × 0.85)
N = 42,000 / 2,295
N = 18.3 → 18 luminaires
```

**Step 5: Layout**
```
18 luminaires in 1,200 SF room
Layout: 3 rows × 6 columns = 18 total
Row spacing: 30 / 3 = 10 ft
Column spacing: 40 / 6 = 6.67 ft

Check spacing criteria:
Maximum spacing: 6.5 × 1.3 = 8.45 ft
Actual spacing: 10 ft (slightly exceeds, but acceptable for general office)
```

**Step 6: Verify illuminance**
```
E = (18 × 5,000 × 0.54 × 0.85) / 1,200
E = 41,310 / 1,200
E = 34.4 fc ≈ 35 fc ✓
```

**Step 7: Check LPD compliance (ASHRAE 90.1, Space-by-Space)**
```
Open office LPD limit: 0.61 W/ft²
Allowed power: 0.61 × 1,200 = 732W

Proposed power: 18 × 40W = 720W
Compliance: 720 < 732 ✓ COMPLIES
```

**Step 8: Lighting controls**
```
Required controls (ASHRAE 90.1):
1. Automatic shutoff: Occupancy sensors (space < 2,500 SF)
2. Manual control: Wall switch at entrance
3. Partial-OFF: Bi-level switching (alternate rows)

Proposed control strategy:
- 3 zones (1 row per zone)
- Each zone: Dual-technology occupancy sensor
- 30-minute time delay
- Manual override switches

Actual LPD with controls:
Base LPD: 720W / 1,200SF = 0.60 W/ft²
With occupancy sensors (-20% estimated): 0.48 W/ft² effective
```

---

## 10. Quality Assurance Checklist

### Design Phase QA

```
LIGHTING DESIGN CHECKLIST:

☐ Illuminance Calculations Complete
  ☐ Target illuminance determined per IES RP-1
  ☐ Maintained values calculated (with LLF)
  ☐ Uniformity ratio verified (3:1 typical)

☐ Luminaire Selection
  ☐ Appropriate lumen output
  ☐ Correct CCT for application (2700K-5000K)
  ☐ Adequate CRI (80+ for most spaces)
  ☐ Suitable distribution pattern
  ☐ Compatible with controls

☐ Energy Code Compliance
  ☐ LPD calculated (ASHRAE 90.1 or IECC)
  ☐ Building Area or Space-by-Space method selected
  ☐ Additional lighting power documented if applicable

☐ Lighting Controls
  ☐ Automatic shutoff specified
  ☐ Occupancy sensors located properly
  ☐ Daylight harvesting provided where required
  ☐ Manual controls accessible
  ☐ Bi-level or dimming capability provided

☐ Emergency/Egress Lighting
  ☐ 1 fc minimum along egress paths
  ☐ 90-minute battery backup specified
  ☐ Exit signs at all required locations
  ☐ Emergency luminaires on separate circuit

☐ Special Considerations
  ☐ Glare control addressed
  ☐ Disability glare minimized
  ☐ Vertical illuminance calculated (if required)
  ☐ Exterior lighting calculations complete

☐ Documentation
  ☐ Lighting layout drawings complete
  ☐ Calculation summary sheets attached
  ☐ Luminaire schedule with all specifications
  ☐ Control sequence narratives included
```

---

## Summary

This comprehensive guide provides the foundation for accurate lighting calculations following IES standards and energy code compliance per ASHRAE 90.1. Key principles include:

1. **Select appropriate illuminance targets** based on task, space type, and occupant age
2. **Use lumen method** for regular spaces and general calculations
3. **Apply point-by-point method** for irregular spaces and detailed analysis
4. **Verify energy code compliance** using Building Area or Space-by-Space LPD limits
5. **Design emergency/egress lighting** per IBC/NFPA 101 requirements
6. **Integrate lighting controls** for automatic shutoff, daylight harvesting, and manual control
7. **Document all calculations** with complete assumptions, formulas, and results

**Key References**:
- IES RP-1-21: Office Lighting
- ASHRAE 90.1-2022: Energy Standard for Buildings
- IECC 2021: International Energy Conservation Code
- IBC 2021: International Building Code
- NFPA 101: Life Safety Code
- NEC 2023: National Electrical Code

---

*Document maintained by: Lighting Design Engineering Team*
*Next review date: 2026-01-22*
