# Drawing Type Classification System

## Overview

This document provides a comprehensive taxonomy of engineering drawing types for MEP systems, organized by drawing category, project phase, and sheet numbering standards. This classification enables automated drawing validation, completeness checks, and proper documentation organization.

---

## 1. Drawing Classification Hierarchy

### 1.1 Primary Classification Dimensions
1. **Drawing Category** - Plans, Diagrams, Details, Schedules, Specifications
2. **Discipline** - Architectural, Structural, Civil, Electrical, Mechanical, Plumbing, Fire Protection
3. **Project Phase** - SD, DD, CD, Bidding, ASB, Record
4. **Sheet Type** - Construction drawings, shop drawings, coordination drawings, as-builts

---

## 2. Drawing Categories

### 2.1 Plans (Floor-Based Drawings)
**Definition:** Horizontal cut drawings showing equipment, systems, and components at a specific floor level or elevation.

**Characteristics:**
- Drawn at building scale (1/8" = 1'-0", 1/4" = 1'-0" typical)
- Show walls, doors, and architectural context
- Include equipment locations, routing, and device placement
- Reference grid lines and dimensions

**Subcategories:**
- Floor Plans
- Reflected Ceiling Plans (RCP)
- Site Plans
- Roof Plans

---

### 2.2 Diagrams (Schematic Drawings)
**Definition:** Single-line or simplified drawings showing system relationships, connections, and flow without exact spatial layout.

**Characteristics:**
- Not to scale (schematic)
- Emphasize connectivity and system logic
- Use standardized symbols
- Show vertical or logical relationships

**Subcategories:**
- One-Line Diagrams (electrical power distribution)
- Riser Diagrams (vertical distribution)
- Control Diagrams (sequences of operation)
- Schematic Diagrams (system relationships)
- Flow Diagrams (piping and process)

---

### 2.3 Details (Enlarged Drawings)
**Definition:** Enlarged or sectional views showing specific construction, connections, or installation methods.

**Characteristics:**
- Large scale (1/2" = 1'-0", 1" = 1'-0", 3" = 1'-0", or full size)
- Show precise dimensions and materials
- Provide installation guidance
- Reference specific plan locations

**Subcategories:**
- Sections (vertical cuts)
- Enlarged Plans (zoom-in views)
- Typical Details (reusable details)
- Mounting Details
- Connection Details

---

### 2.4 Schedules (Tabular Data)
**Definition:** Tables listing equipment, devices, or components with specifications and characteristics.

**Characteristics:**
- Tabular format
- Columns for attributes and specifications
- Referenced by tags or marks on plans
- Provide procurement and installation data

**Subcategories:**
- Equipment Schedules
- Panel Schedules
- Lighting Fixture Schedules
- Plumbing Fixture Schedules
- Door/Window Schedules (Architectural)
- Valve Schedules
- Device Schedules

---

### 2.5 Sheets (Document Organization)
**Definition:** Complete drawing sheets combining multiple drawing types with titleblocks, borders, and legends.

**Characteristics:**
- Standard sheet sizes (24"×36", 30"×42", 36"×48")
- Titleblock with project information
- Sheet number and revision tracking
- Professional seal area

---

## 3. Drawing Types by Discipline

### 3.1 Architectural Drawings

#### 3.1.1 Plans
| Drawing Type | Sheet Prefix | Scale | Content |
|-------------|--------------|-------|---------|
| Site Plan | A-001 | 1" = 20', 1" = 40' | Building footprint, property lines, utilities, parking, landscaping |
| Floor Plans | A-101 to A-199 | 1/8" = 1'-0", 1/4" = 1'-0" | Walls, doors, windows, rooms, dimensions, door/window tags |
| Enlarged Floor Plans | A-101.1, A-101.2 | 1/4" = 1'-0", 1/2" = 1'-0" | Toilet rooms, detailed areas, casework |
| Reflected Ceiling Plans | A-201 to A-299 | 1/8" = 1'-0", 1/4" = 1'-0" | Ceiling grid, heights, soffits, architectural lighting |
| Roof Plan | A-301 | 1/8" = 1'-0", 1/16" = 1'-0" | Roof slopes, drains, equipment curbs, parapet heights |

#### 3.1.2 Elevations and Sections
| Drawing Type | Sheet Prefix | Scale | Content |
|-------------|--------------|-------|---------|
| Exterior Elevations | A-301 to A-399 | 1/8" = 1'-0", 1/4" = 1'-0" | Building facades, materials, fenestration, heights |
| Interior Elevations | A-401 to A-499 | 1/4" = 1'-0", 3/8" = 1'-0" | Interior walls, casework, finishes, door swings |
| Building Sections | A-401 to A-499 | 1/8" = 1'-0", 1/4" = 1'-0" | Vertical cuts, floor-to-floor heights, structure visibility |
| Wall Sections | A-501 to A-599 | 3/4" = 1'-0", 1-1/2" = 1'-0" | Wall assembly, insulation, flashing, details |

#### 3.1.3 Details and Schedules
| Drawing Type | Sheet Prefix | Scale | Content |
|-------------|--------------|-------|---------|
| Details | A-501 to A-599 | 1/2" = 1'-0" to full size | Stair details, guardrail, millwork, typical conditions |
| Door Schedule | A-601 | N/A | Door size, material, fire rating, hardware sets |
| Window Schedule | A-601 | N/A | Window size, type, glazing, operation |
| Finish Schedule | A-601 | N/A | Room-by-room floor, base, wall, ceiling finishes |

---

### 3.2 Electrical Drawings

#### 3.2.1 Plans
| Drawing Type | Sheet Prefix | Scale | Content |
|-------------|--------------|-------|---------|
| Symbols and Legends | E-001 | N/A | Electrical symbols, abbreviations, general notes |
| Site Electrical Plan | E-002 | 1" = 20', 1" = 40' | Site lighting, utility service, grounding, exterior equipment |
| Power Plans | E-101 to E-199 | 1/8" = 1'-0", 1/4" = 1'-0" | Panelboards, receptacles, equipment connections, home runs |
| Lighting Plans | E-201 to E-299 | 1/8" = 1'-0", 1/4" = 1'-0" | Lighting fixtures, switches, circuiting, occupancy sensors |
| Fire Alarm Plans | E-301 to E-399 | 1/8" = 1'-0", 1/4" = 1'-0" | Devices (smoke, heat, pull stations), notification devices, FACP |
| Low Voltage Plans | E-351 to E-399 | 1/8" = 1'-0", 1/4" = 1'-0" | Data outlets, AV, security cameras, access control |

#### 3.2.2 Diagrams
| Drawing Type | Sheet Prefix | Scale | Content |
|-------------|--------------|-------|---------|
| One-Line Diagram | E-401 to E-499 | Not to scale | Utility service, transformers, switchgear, panels, feeders |
| Riser Diagrams | E-401 to E-499 | Not to scale | Vertical distribution, panel feed locations, wire sizes |
| Control Diagrams | E-401 to E-499 | Not to scale | Lighting control logic, emergency power sequences |
| Fire Alarm Riser | E-401 to E-499 | Not to scale | FACP, zones, NAC circuits, device wiring |

#### 3.2.3 Schedules and Details
| Drawing Type | Sheet Prefix | Scale | Content |
|-------------|--------------|-------|---------|
| Panel Schedules | E-501 to E-599 | N/A | Circuit-by-circuit listing: breaker size, load, notes |
| Lighting Fixture Schedule | E-501 to E-599 | N/A | Fixture type, lamp, voltage, mounting, manufacturer |
| Equipment Schedule | E-501 to E-599 | N/A | Equipment tag, voltage, phases, FLA, MCA, MOP |
| Details | E-601 to E-699 | Various | Grounding details, panel mounting, typical connections |

---

### 3.3 Mechanical Drawings

#### 3.3.1 Plans
| Drawing Type | Sheet Prefix | Scale | Content |
|-------------|--------------|-------|---------|
| Symbols and Legends | M-001 | N/A | Mechanical symbols, abbreviations, general notes |
| Site Mechanical Plan | M-002 | 1" = 20', 1" = 40' | Outdoor equipment (cooling towers, generators), gas/fuel lines |
| HVAC Plans | M-101 to M-199 | 1/8" = 1'-0", 1/4" = 1'-0" | Equipment locations, ductwork layout, diffusers/grilles, thermostats |
| Enlarged HVAC Plans | M-101.1 | 1/4" = 1'-0" | Mechanical rooms, complex duct routing, equipment details |
| Hydronic Piping Plans | M-201 to M-299 | 1/8" = 1'-0", 1/4" = 1'-0" | Chilled water, hot water, condenser water piping, valves, pumps |

#### 3.3.2 Diagrams
| Drawing Type | Sheet Prefix | Scale | Content |
|-------------|--------------|-------|---------|
| HVAC Riser Diagrams | M-401 to M-499 | Not to scale | Vertical ductwork distribution, shaft sizes, floor-by-floor connections |
| Piping Riser Diagrams | M-401 to M-499 | Not to scale | Hydronic piping vertical distribution, expansion tanks, air separators |
| Control Diagrams | M-301 to M-399 | Not to scale | Sequences of operation, control logic, BAS architecture |
| Flow Diagrams | M-401 to M-499 | Not to scale | Chilled water loop, condenser water loop, system flow paths |

#### 3.3.3 Details and Schedules
| Drawing Type | Sheet Prefix | Scale | Content |
|-------------|--------------|-------|---------|
| Equipment Schedule | M-601 to M-699 | N/A | Tag, type, capacity (CFM, GPM, tons, HP), voltage, weight |
| Details | M-501 to M-599 | Various | Equipment mounting, vibration isolation, duct/pipe connections |
| Diffuser/Grille Schedule | M-601 to M-699 | N/A | Size, CFM, type, mounting, neck size |

---

### 3.4 Plumbing Drawings

#### 3.4.1 Plans
| Drawing Type | Sheet Prefix | Scale | Content |
|-------------|--------------|-------|---------|
| Symbols and Legends | P-001 | N/A | Plumbing symbols, abbreviations, general notes |
| Site Plumbing Plan | P-002 | 1" = 20', 1" = 40' | Water service, sanitary sewer, storm drain, site utilities |
| Domestic Water Plans | P-101 to P-199 | 1/8" = 1'-0", 1/4" = 1'-0" | Cold water, hot water, HW return piping, valves, water heaters |
| Sanitary Plans | P-201 to P-299 | 1/8" = 1'-0", 1/4" = 1'-0" | Sanitary drain and vent piping, cleanouts, floor drains |
| Storm Drain Plans | P-301 to P-399 | 1/8" = 1'-0", 1/4" = 1'-0" | Roof drains, storm piping, area drains |
| Enlarged Plumbing Plans | P-101.1 | 1/4" = 1'-0", 1/2" = 1'-0" | Toilet rooms, mechanical rooms, detailed fixture rough-in |

#### 3.4.2 Diagrams
| Drawing Type | Sheet Prefix | Scale | Content |
|-------------|--------------|-------|---------|
| Domestic Water Risers | P-401 to P-499 | Not to scale | Vertical water distribution, pressure zones, booster pumps |
| Sanitary/Vent Risers | P-401 to P-499 | Not to scale | Vertical drain and vent stacks, floor connections |
| Storm Drain Risers | P-401 to P-499 | Not to scale | Vertical storm distribution, roof drain leaders |
| Piping Schematics | P-401 to P-499 | Not to scale | Water heater piping, recirculation loops, medical gas zones |

#### 3.4.3 Details and Schedules
| Drawing Type | Sheet Prefix | Scale | Content |
|-------------|--------------|-------|---------|
| Plumbing Fixture Schedule | P-601 to P-699 | N/A | Fixture type, mounting, faucet, GPM/GPF, ADA compliance |
| Equipment Schedule | P-601 to P-699 | N/A | Water heaters, pumps, capacity, fuel, efficiency |
| Details | P-501 to P-599 | Various | Fixture mounting, typical connections, pipe support |

---

### 3.5 Fire Protection Drawings

#### 3.5.1 Plans
| Drawing Type | Sheet Prefix | Scale | Content |
|-------------|--------------|-------|---------|
| Symbols and Legends | FP-001 | N/A | Fire protection symbols, abbreviations, general notes |
| Fire Sprinkler Plans | FP-101 to FP-199 | 1/8" = 1'-0", 1/4" = 1'-0" | Sprinkler heads, piping layout, risers, FDCs |
| Enlarged Sprinkler Plans | FP-101.1 | 1/4" = 1'-0", 1/2" = 1'-0" | Complex areas, obstructions, detailed head placement |
| Standpipe Plans | FP-201 to FP-299 | 1/8" = 1'-0", 1/4" = 1'-0" | Standpipe risers, hose valves, hose cabinets |

#### 3.5.2 Diagrams
| Drawing Type | Sheet Prefix | Scale | Content |
|-------------|--------------|-------|---------|
| Sprinkler Riser Diagrams | FP-301 to FP-399 | Not to scale | Vertical sprinkler distribution, riser locations, FDC connections |
| Standpipe Riser Diagrams | FP-301 to FP-399 | Not to scale | Vertical standpipe distribution, hose connections by floor |
| Flow Diagrams | FP-301 to FP-399 | Not to scale | Water supply, fire pump, backflow preventer, system flow |

#### 3.5.3 Calculations and Schedules
| Drawing Type | Sheet Prefix | Scale | Content |
|-------------|--------------|-------|---------|
| Hydraulic Calculations | FP-401 to FP-499 | N/A | NFPA 13 calculations, most remote area, system demand curve |
| Sprinkler Head Schedule | FP-501 to FP-599 | N/A | Head type, K-factor, temperature, finish, coverage |
| Equipment Schedule | FP-501 to FP-599 | N/A | Fire pumps, backflow preventers, valves |
| Details | FP-501 to FP-599 | Various | Riser assembly, seismic bracing, typical sprinkler details |

---

## 4. Sheet Numbering Standards

### 4.1 Standard Numbering Format
```
[DISCIPLINE]-[SERIES][NUMBER].[SUBSERIES]
```

**Examples:**
- E-201 = Electrical, Lighting Plans, Sheet 01
- M-101.1 = Mechanical, HVAC Plans, Subseries 1 (enlarged)
- FP-401 = Fire Protection, Hydraulic Calculations

### 4.2 Series Numbering Convention
| Series | Range | Drawing Type |
|--------|-------|-------------|
| 000-099 | General | Symbols, legends, site plans, general notes |
| 100-199 | Plans 1 | Floor plans, power plans, HVAC plans, domestic water plans |
| 200-299 | Plans 2 | RCPs, lighting plans, hydronic piping plans, sanitary plans |
| 300-399 | Plans 3 | Fire alarm plans, storm drain plans |
| 400-499 | Diagrams | One-lines, risers, control diagrams, flow diagrams |
| 500-599 | Details | Typical details, mounting details, connections |
| 600-699 | Schedules | Equipment, panels, fixtures, devices |

### 4.3 Discipline Prefixes
| Prefix | Discipline | Color Code (Optional) |
|--------|-----------|----------------------|
| A | Architecture | Black |
| S | Structural | Red |
| C | Civil | Brown |
| E | Electrical | Blue |
| M | Mechanical | Green |
| P | Plumbing | Yellow |
| FP or F | Fire Protection | Orange |
| L | Landscape | Light Green |

### 4.4 Sheet Numbering Examples by Discipline
| Discipline | Sheet Number | Drawing Type |
|-----------|--------------|-------------|
| Architectural | A-001 | Site Plan |
| Architectural | A-101 | First Floor Plan |
| Architectural | A-201 | First Floor Reflected Ceiling Plan |
| Architectural | A-301 | Exterior Elevations |
| Architectural | A-401 | Building Sections |
| Architectural | A-501 | Details |
| Architectural | A-601 | Door/Window/Finish Schedules |
| Electrical | E-001 | Symbols and General Notes |
| Electrical | E-101 | First Floor Power Plan |
| Electrical | E-201 | First Floor Lighting Plan |
| Electrical | E-301 | First Floor Fire Alarm Plan |
| Electrical | E-401 | One-Line Diagram |
| Electrical | E-501 | Panel Schedules |
| Mechanical | M-001 | Symbols and General Notes |
| Mechanical | M-101 | First Floor HVAC Plan |
| Mechanical | M-201 | First Floor Hydronic Piping Plan |
| Mechanical | M-301 | Control Diagrams |
| Mechanical | M-401 | HVAC Riser Diagrams |
| Mechanical | M-501 | Details |
| Mechanical | M-601 | Equipment Schedules |
| Plumbing | P-001 | Symbols and General Notes |
| Plumbing | P-101 | First Floor Domestic Water Plan |
| Plumbing | P-201 | First Floor Sanitary Plan |
| Plumbing | P-301 | First Floor Storm Drain Plan |
| Plumbing | P-401 | Plumbing Riser Diagrams |
| Plumbing | P-501 | Details |
| Plumbing | P-601 | Fixture and Equipment Schedules |
| Fire Protection | FP-001 | Symbols and General Notes |
| Fire Protection | FP-101 | First Floor Sprinkler Plan |
| Fire Protection | FP-301 | Sprinkler Riser Diagram |
| Fire Protection | FP-401 | Hydraulic Calculations |
| Fire Protection | FP-501 | Details and Schedules |

---

## 5. Drawing Organization by Project Phase

### 5.1 Schematic Design (SD) - 15-30% Complete
**Purpose:** Establish basic design concepts, system selection, and preliminary layouts.

**Typical Drawings:**
- Site plans with utility connections
- Single-line floor plans showing major equipment only
- System diagrams (one-lines, risers) showing overall distribution concepts
- Preliminary equipment schedules
- No details or full schedules

**Drawing Status:** "SCHEMATIC DESIGN - NOT FOR CONSTRUCTION"

---

### 5.2 Design Development (DD) - 50-65% Complete
**Purpose:** Refine systems, establish sizing, coordinate with other disciplines.

**Typical Drawings:**
- Floor plans with equipment locations and preliminary routing
- RCPs with lighting layouts and device locations
- One-line diagrams with feeder sizes
- Riser diagrams with shaft sizes
- Preliminary equipment schedules with major specifications
- Key details for unusual conditions

**Drawing Status:** "DESIGN DEVELOPMENT - NOT FOR CONSTRUCTION"

**Coordination Required:**
- MEP equipment clearances with architectural layouts
- Ductwork/piping routing with structural framing
- Panel locations and working clearances
- Shaft and chase sizes

---

### 5.3 Construction Documents (CD) - 90-100% Complete
**Purpose:** Provide complete, coordinated, code-compliant drawings for permitting, bidding, and construction.

**Typical Drawings:**
- Complete floor plans with all equipment, devices, routing, circuiting
- Complete RCPs with all fixtures, controls, switching
- Detailed one-line diagrams with all equipment specifications
- Complete riser diagrams with sizes, elevations, connections
- All details required for construction
- Complete equipment schedules with full specifications
- Panel schedules with circuit-by-circuit information
- General notes, specifications, and code compliance documentation

**Drawing Status:** "FOR PERMIT" or "FOR BIDDING" or "FOR CONSTRUCTION"

**Required Elements:**
- Professional engineer's seal and signature
- Code compliance statements
- Complete dimensions and elevations
- Material specifications
- Installation requirements

---

### 5.4 Addenda/Supplemental Bulletins (ASB)
**Purpose:** Issue changes, clarifications, or corrections during bidding or construction.

**Typical Formats:**
- **Addenda:** Formal changes during bidding phase
  - Sheet replacement or overlay markings
  - Specification revisions
  - Answers to RFIs

- **Supplemental Bulletins (ASB):** Changes during construction
  - Revised details
  - Field condition resolutions
  - Value engineering alternates

**Drawing Status:** "ADDENDUM #1", "ADDENDUM #2", "ASB #1"

**Revision Tracking:**
- Delta symbols (Δ) or clouds around changed areas
- Revision description in titleblock
- Revision date

---

### 5.5 Record Drawings (As-Builts)
**Purpose:** Document final as-installed conditions for facility management and future renovations.

**Typical Markups:**
- Equipment relocations
- Field routing changes
- Size changes
- Final device locations
- Underground utility as-built locations

**Drawing Status:** "RECORD DRAWINGS" or "AS-BUILT"

**Format:**
- Red-line markups on original CDs
- Or fully revised CAD/BIM drawings incorporating changes

---

## 6. Drawing Completeness Checklists

### 6.1 Electrical Drawing Set Completeness
- [ ] E-001: Symbols, Legends, General Notes
- [ ] E-002: Site Electrical Plan (if applicable)
- [ ] E-1XX: Power Plans (all floor levels)
- [ ] E-2XX: Lighting Plans (all floor levels)
- [ ] E-3XX: Fire Alarm Plans (all floor levels)
- [ ] E-4XX: One-Line Diagrams (utility service through panels)
- [ ] E-4XX: Riser Diagrams (power, fire alarm)
- [ ] E-5XX: Panel Schedules (all panels)
- [ ] E-5XX: Lighting Fixture Schedule
- [ ] E-5XX: Equipment Connection Schedule
- [ ] E-6XX: Details (grounding, typical installations)

### 6.2 Mechanical Drawing Set Completeness
- [ ] M-001: Symbols, Legends, General Notes
- [ ] M-002: Site Mechanical Plan (if applicable)
- [ ] M-1XX: HVAC Plans (all floor levels)
- [ ] M-2XX: Hydronic Piping Plans (if applicable)
- [ ] M-3XX: Control Diagrams and Sequences
- [ ] M-4XX: HVAC Riser Diagrams
- [ ] M-4XX: Piping Riser Diagrams (if applicable)
- [ ] M-5XX: Details (equipment mounting, connections)
- [ ] M-6XX: Equipment Schedules
- [ ] M-6XX: Diffuser/Grille Schedules

### 6.3 Plumbing Drawing Set Completeness
- [ ] P-001: Symbols, Legends, General Notes
- [ ] P-002: Site Plumbing Plan
- [ ] P-1XX: Domestic Water Plans (all floor levels)
- [ ] P-2XX: Sanitary Plans (all floor levels)
- [ ] P-3XX: Storm Drain Plans (roof and applicable floors)
- [ ] P-4XX: Domestic Water Riser Diagrams
- [ ] P-4XX: Sanitary/Vent Riser Diagrams
- [ ] P-4XX: Storm Drain Riser Diagrams
- [ ] P-5XX: Details (fixture mounting, connections)
- [ ] P-6XX: Plumbing Fixture Schedule
- [ ] P-6XX: Equipment Schedule (water heaters, pumps)

### 6.4 Fire Protection Drawing Set Completeness
- [ ] FP-001: Symbols, Legends, General Notes
- [ ] FP-1XX: Fire Sprinkler Plans (all floor levels)
- [ ] FP-2XX: Standpipe Plans (if applicable)
- [ ] FP-3XX: Sprinkler Riser Diagrams
- [ ] FP-3XX: Standpipe Riser Diagrams (if applicable)
- [ ] FP-4XX: Hydraulic Calculations (sealed by fire protection engineer)
- [ ] FP-5XX: Sprinkler Head Schedule
- [ ] FP-5XX: Equipment Schedule (fire pumps, backflow preventers)
- [ ] FP-5XX: Details (riser assembly, seismic bracing)

---

## 7. Drawing Content Standards

### 7.1 Title Block Requirements
| Element | Description | Required |
|---------|-------------|----------|
| Project Name | Full project name | Yes |
| Project Address | Street address, city, state | Yes |
| Owner/Client | Building owner or client name | Yes |
| Architect/Engineer | Firm name and address | Yes |
| Discipline | Electrical, Mechanical, Plumbing, etc. | Yes |
| Drawing Title | Descriptive title (e.g., "First Floor Power Plan") | Yes |
| Sheet Number | Per numbering standard | Yes |
| Scale | Graphic and written scale | Yes |
| Date | Issue date | Yes |
| Revision | Revision number/letter and date | If revised |
| Project Number | Internal project tracking number | Optional |
| Professional Seal | PE/RA seal and signature (CD phase) | Yes (CD phase) |

### 7.2 General Notes Standards
**Location:** Typically on sheet E-001, M-001, P-001, FP-001

**Categories:**
1. **Code Compliance:**
   - "All work shall comply with NEC 2020, IMC 2018, IPC 2018, NFPA 13 2019, and all applicable local codes."

2. **Standards and Specifications:**
   - "Install all equipment and materials per manufacturer's instructions."
   - "Coordinate all work with other trades."

3. **Abbreviations and Symbols:**
   - Reference to legend sheet
   - Discipline-specific abbreviations

4. **Submittal Requirements:**
   - "Submit shop drawings and product data for approval prior to procurement."

5. **Testing and Commissioning:**
   - "Test and balance all HVAC systems per ASHRAE standards."
   - "Provide system commissioning per specifications."

### 7.3 Legend and Symbol Standards
**Required Symbols:**
- Equipment symbols with tags
- Piping/ductwork with material designations
- Control devices
- Connection symbols (flanged, threaded, welded)
- Line types (existing, new, demolition, future)

---

## 8. Drawing Coordination Requirements

### 8.1 Plan View Coordination
| Item | Disciplines Involved | Coordination Required |
|------|---------------------|----------------------|
| Ceiling Heights | Arch, Mech, Elec, FP | Verify adequate space for ductwork, piping, lights, sprinklers |
| Equipment Locations | Arch, Mech, Elec, Plumb | Verify access, clearances, structural support |
| Wall Penetrations | All disciplines | Coordinate pipe/duct/conduit penetrations, maintain fire ratings |
| Door Swings | Arch, Elec | Verify electrical panel clearances (NEC 110.26) |
| Fire-Rated Assemblies | All disciplines | Maintain ratings at penetrations per IBC 714 |

### 8.2 Ceiling Coordination
| Item | Disciplines Involved | Coordination Required |
|------|---------------------|----------------------|
| Lighting Fixtures | Arch (RCP), Elec | Coordinate fixture locations with ceiling grid |
| Diffusers/Grilles | Arch (RCP), Mech | Coordinate with ceiling grid and lights |
| Sprinkler Heads | Arch (RCP), FP | 3" minimum clearance from lights/diffusers per NFPA 13 |
| Smoke Detectors | Arch (RCP), Elec | Coordinate with air patterns and obstructions |
| Access Panels | Arch, all MEP | Provide access to valves, dampers, junction boxes |

### 8.3 Vertical Coordination
| Item | Disciplines Involved | Coordination Required |
|------|---------------------|----------------------|
| Shaft Sizes | Arch, Struc, all MEP | Size shafts for all risers with access and clearances |
| Floor Penetrations | Struc, all MEP | Coordinate structural penetrations, fire-rated sleeves |
| Riser Routing | All MEP | Stack risers vertically, minimize offsets |
| Vertical Clearances | Struc, all MEP | Verify beam depths allow ductwork/piping routing |

---

## 9. Drawing Quality Validation Rules

### 9.1 Plan Drawing Validation
- [ ] Architectural background matches current architectural drawings
- [ ] Grid lines and column lines match structural drawings
- [ ] Scale is appropriate and noted on drawing
- [ ] North arrow present and oriented correctly
- [ ] All equipment has tags matching schedules
- [ ] All devices have circuit designations
- [ ] Home runs shown to panels
- [ ] Dimensions provided for equipment locations

### 9.2 Diagram Validation
- [ ] All equipment shown on plans appears in diagrams
- [ ] Sizes and ratings are consistent between diagrams and schedules
- [ ] Flow direction arrows shown
- [ ] Connections between equipment clearly indicated
- [ ] Elevations or floor levels noted on risers
- [ ] Legend provided for symbols used

### 9.3 Schedule Validation
- [ ] All equipment on plans has corresponding schedule entry
- [ ] All schedule entries have equipment shown on plans
- [ ] Required attributes populated (no blanks for required fields)
- [ ] Units specified (V, A, HP, CFM, GPM, etc.)
- [ ] Notes column used for special requirements

### 9.4 Detail Validation
- [ ] Scale appropriate for level of detail
- [ ] Dimensions provided
- [ ] Materials specified
- [ ] Reference to plan location provided
- [ ] Code compliance notes included
- [ ] Installation sequence clear

---

## 10. Drawing Revision and Change Management

### 10.1 Revision Tracking Methods
| Method | Description | When Used |
|--------|-------------|-----------|
| Revision Triangle (Δ) | Triangle symbol with revision number | Minor changes, individual items |
| Revision Cloud | Cloud outline around changed area | Moderate changes, groups of items |
| Full Sheet Replacement | Entire sheet reissued | Major changes affecting entire sheet |

### 10.2 Revision Log Format
| Rev | Date | Description | By |
|-----|------|-------------|-----|
| - | 2024-01-15 | Issued for Permit | JD |
| 1 | 2024-02-10 | Revised panel LP-2A location per RFI #5 | JD |
| 2 | 2024-03-05 | Added emergency lighting per code review comment | JD |

### 10.3 Revision Stages
| Stage | Code | Description |
|-------|------|-------------|
| Preliminary | PR | Early design, not for construction |
| Schematic Design | SD | Concept design |
| Design Development | DD | Design refinement |
| For Permit | FP | Submitted to building department |
| For Bidding | FB | Issued to contractors for pricing |
| For Construction | FC | Approved for construction |
| Addendum | AD-1, AD-2 | Changes during bidding |
| ASB | ASB-1, ASB-2 | Changes during construction |
| As-Built | AB | Final as-installed conditions |

---

## 11. Conclusion

This drawing type classification system provides:
- **Standardized organization** of all MEP drawing types
- **Consistent sheet numbering** across disciplines and projects
- **Clear definitions** of drawing content by type and phase
- **Comprehensive validation rules** for drawing completeness and quality
- **Coordination frameworks** for interdisciplinary drawing checks

This taxonomy enables automated drawing validation, completeness verification, and proper documentation management throughout the project lifecycle from schematic design through record drawings.
