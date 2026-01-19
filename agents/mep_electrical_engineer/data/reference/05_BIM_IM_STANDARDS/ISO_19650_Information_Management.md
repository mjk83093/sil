# ISO 19650 Information Management for MEP Systems

**Document Version**: 2.0
**Agent**: BIM Process Specialist
**Last Updated**: 2025-10-22
**Integration Point**: Links to SKILL.md data format requirements and JSON extraction workflow

---

## Executive Summary

ISO 19650 is the international standard for managing information throughout the lifecycle of a built asset using Building Information Modeling (BIM). This document provides comprehensive guidance for implementing ISO 19650 principles within MEP (Mechanical, Electrical, Plumbing) engineering workflows, with specific integration to the engineering-drawing-qaqc skill.

**Key Standards Covered:**
- ISO 19650-1: Concepts and principles
- ISO 19650-2: Delivery phase of assets (design/construction)
- ISO 19650-3: Operational phase
- ISO 19650-4: Information exchange
- ISO 19650-5: Security-minded approach

---

## Table of Contents

1. [ISO 19650 Overview](#iso-19650-overview)
2. [Common Data Environment (CDE)](#common-data-environment-cde)
3. [Information Requirements Framework](#information-requirements-framework)
4. [Level of Information Need (LOIN)](#level-of-information-need-loin)
5. [BIM Execution Plan (BEP)](#bim-execution-plan-bep)
6. [Model Delivery Workflows](#model-delivery-workflows)
7. [Asset Information Model (AIM)](#asset-information-model-aim)
8. [Naming Conventions](#naming-conventions)
9. [Integration with QA/QC Workflow](#integration-with-qaqc-workflow)
10. [MEP-Specific Considerations](#mep-specific-considerations)

---

## ISO 19650 Overview

### Core Principles

ISO 19650 establishes a framework for information management based on:

1. **Information Requirements**: Define what information is needed, when, and by whom
2. **Structured Information Exchange**: Use standardized formats and protocols
3. **Collaborative Working**: Implement Common Data Environment for information sharing
4. **Information Lifecycle**: Manage information from design through operations
5. **Risk Management**: Identify and mitigate information-related risks

### Key Terminology

| Term | Definition | MEP Context Example |
|------|------------|---------------------|
| **Appointing Party** | Client or organization commissioning work | Building owner requesting MEP design |
| **Lead Appointed Party** | Main contractor or designer managing delivery | MEP engineering firm lead |
| **Appointed Party** | Task team member delivering information | Electrical subcontractor |
| **Information Model** | Digital representation of asset characteristics | Coordinated MEP 3D model |
| **Level of Information Need** | Framework defining granularity and detail | Electrical panel LOD 350 |
| **Information Container** | Discrete unit of information | Single Revit MEP model file |
| **Common Data Environment** | Central repository for project information | Project SharePoint or BIM 360 |

### ISO 19650 Parts Overview

#### Part 1: Concepts and Principles
- Establishes fundamental concepts and terminology
- Defines information lifecycle stages
- Introduces LOIN framework
- **MEP Application**: Foundation for all MEP information management

#### Part 2: Delivery Phase (Design/Construction)
- Covers project delivery workflows
- Details appointment and mobilization processes
- Specifies collaborative production workflows
- Information delivery milestones
- **MEP Application**: Design coordination, clash detection, submittal workflows

#### Part 3: Operational Phase
- Asset information requirements for O&M
- Transition from delivery to operations
- Asset Information Model management
- **MEP Application**: Equipment maintenance data, BMS integration, spare parts databases

#### Part 4: Information Exchange
- Standardized information exchange protocols
- COBie (Construction Operations Building Information Exchange)
- IFC (Industry Foundation Classes) requirements
- **MEP Application**: MEP equipment data export for facilities management

#### Part 5: Security-Minded Approach
- Information security management
- Sensitive information identification
- Access control and data protection
- **MEP Application**: Protecting security system layouts, critical infrastructure data

---

## Common Data Environment (CDE)

### CDE Structure and Purpose

The Common Data Environment is a central digital repository where all project information is stored, managed, and shared. For MEP systems, this includes models, drawings, specifications, calculations, and equipment data.

### CDE Container States

ISO 19650-2 defines four information container states:

```
┌─────────────────────────────────────────────────────────────────┐
│                    COMMON DATA ENVIRONMENT                       │
├─────────────────┬─────────────────┬─────────────────┬───────────┤
│   WIP (Work     │  SHARED         │  PUBLISHED      │  ARCHIVED │
│   In Progress)  │                 │                 │           │
├─────────────────┼─────────────────┼─────────────────┼───────────┤
│ • Individual    │ • Shared for    │ • Approved for  │ • Project │
│   work          │   coordination  │   client use    │   complete│
│ • Drafts        │ • For review    │ • Issued for    │ • Legal   │
│ • Local storage │ • Clash tests   │   construction  │   archive │
│ • Not shared    │ • Discipline    │ • Authorized    │ • Read-   │
│   externally    │   coordination  │   information   │   only    │
│                 │ • Suitability:  │ • Suitability:  │ • Long-   │
│                 │   S0-S4         │   A1-A7         │   term    │
└─────────────────┴─────────────────┴─────────────────┴───────────┘
```

#### WIP (Work in Progress)
**Purpose**: Individual task team workspace
**Access**: Task team members only
**Suitability**: Not applicable (work in progress)

**MEP Examples:**
- Electrical engineer drafting panel schedules in local Revit file
- Mechanical designer sizing ductwork before coordination
- Plumbing contractor developing preliminary riser diagrams

**Transition Trigger**: Model ready for coordination review → Move to SHARED

#### SHARED
**Purpose**: Interdisciplinary coordination and review
**Access**: All project team members
**Suitability Codes**: S0 (initial) through S4 (construction)

**MEP Examples:**
- Electrical model published for clash detection with architectural/structural
- Mechanical equipment locations shared for architectural coordination
- Fire protection layout reviewed by code consultant

**Suitability Codes:**
- **S0**: Initial status (just uploaded)
- **S1**: Suitable for coordination
- **S2**: Suitable for information
- **S3**: Suitable for review and comment
- **S4**: Suitable for Stage approval

**Transition Trigger**: Model approved by lead appointed party → Move to PUBLISHED

#### PUBLISHED
**Purpose**: Authorized information for client use
**Access**: Client, contractors, regulatory authorities
**Authorization Codes**: A1 through A7

**MEP Examples:**
- Electrical drawings issued for construction (IFC)
- Mechanical equipment schedules for procurement
- Plumbing shop drawings for fabrication

**Authorization Codes:**
- **A1**: Accepted
- **A2**: Accepted with comments
- **A3**: Rejected
- **A4**: Revise and resubmit
- **A5**: Information only
- **A6**: See comments
- **A7**: Approved for construction

**Transition Trigger**: Project substantially complete → Move to ARCHIVED

#### ARCHIVED
**Purpose**: Long-term legal and operational record
**Access**: Authorized personnel only, read-only
**Retention**: Per contractual/legal requirements

**MEP Examples:**
- As-built electrical models for facility operations
- Mechanical equipment O&M manuals with BIM links
- Fire protection system test and inspection records

### CDE Workflow Diagram

```
┌──────────────────────────────────────────────────────────────────┐
│                   MEP Design Team                                 │
│  (Electrical, Mechanical, Plumbing, Fire Protection Engineers)   │
└────────────┬─────────────────────────────────────────────────────┘
             │ 1. Create/Update Models
             ▼
    ┌────────────────┐
    │   WIP          │ ← Individual engineer workspace
    │   (Local)      │   • AutoCAD/Revit local files
    └────────┬───────┘   • Preliminary calculations
             │ 2. Publish to Shared (S1-S4)
             ▼
    ┌────────────────┐
    │   SHARED       │ ← Coordination platform
    │   (Team)       │   • Navisworks clash detection
    └────────┬───────┘   • Interdisciplinary reviews
             │ 3. Approve for Construction (A1-A7)
             ▼
    ┌────────────────┐
    │   PUBLISHED    │ ← Authorized construction docs
    │   (Client)     │   • Issued for construction (IFC)
    └────────┬───────┘   • Submittal packages
             │ 4. Project Closeout
             ▼
    ┌────────────────┐
    │   ARCHIVED     │ ← Asset Information Model (AIM)
    │   (Permanent)  │   • As-built records
    └────────────────┘   • O&M documentation
```

### CDE Naming Structure

```
[Project]-[Originator]-[Volume]-[Level]-[Type]-[Role]-[Number]-[Revision].[Extension]

Example:
HQ2024-MEP-01-GF-M3-ELE-0101-S2.rvt

Where:
- HQ2024: Project identifier
- MEP: Originating organization
- 01: Building/volume (Building 1)
- GF: Floor level (Ground Floor)
- M3: Model type (Federated coordination model)
- ELE: Discipline (Electrical)
- 0101: Sequential number
- S2: Suitability/authorization code
- rvt: Revit model file
```

### CDE Implementation Platforms

Common CDE platforms for MEP projects:

| Platform | Strengths | MEP Use Cases |
|----------|-----------|---------------|
| **Autodesk BIM 360** | Deep Revit integration | MEP model coordination, clash detection |
| **Procore** | Construction workflow focus | Submittal management, RFIs |
| **Aconex** | Document control | Specification management, transmittals |
| **Bentley ProjectWise** | Large infrastructure projects | Complex MEP systems, utilities coordination |
| **Trimble Connect** | Open BIM standards | IFC-based MEP coordination |

---

## Information Requirements Framework

### Three-Tier Requirements Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│  OIR (Organizational Information Requirements)              │
│  "What does the organization need to operate the asset?"    │
└───────────────────────────┬─────────────────────────────────┘
                            │ Informs
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  AIR (Asset Information Requirements)                       │
│  "What information is needed for specific assets/systems?"  │
└───────────────────────────┬─────────────────────────────────┘
                            │ Informs
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  EIR (Exchange Information Requirements)                    │
│  "What must be delivered at each project milestone?"        │
└─────────────────────────────────────────────────────────────┘
```

### OIR (Organizational Information Requirements)

High-level strategic information needs defined by the appointing party.

**MEP Example - Hospital Facilities Department:**
- **Objective**: Reduce emergency power system downtime to <4 hours/year
- **Information Need**: Generator maintenance schedules, fuel capacity, load transfer testing results
- **Delivery Format**: BIM-linked maintenance management system (CMMS)
- **Update Frequency**: Real-time sensor data, monthly inspection logs

### AIR (Asset Information Requirements)

Specific information needs for individual assets or systems derived from OIR.

**MEP Example - Emergency Power System:**
- **Asset**: Standby diesel generator 500kW
- **Required Information**:
  - Equipment nameplate data (manufacturer, model, serial number)
  - Performance specifications (rated output, fuel consumption)
  - Maintenance schedule (oil changes, load bank testing frequency)
  - Spare parts list with lead times
  - Operating manuals and single-line diagrams
  - Load transfer switch settings and testing procedures
- **LOIN**: LOD 400 (fabrication detail), LOG F (testing/commissioning data)

### EIR (Exchange Information Requirements)

Detailed specification of deliverables at each project stage.

**MEP Example - Electrical Design Deliverables:**

| Stage | Deliverable | Format | LOIN | Authorization |
|-------|-------------|--------|------|---------------|
| **Concept** | Single-line diagram | PDF | LOD 100 | S2 (information) |
| **Schematic Design** | Panel schedules (preliminary) | Revit/Excel | LOD 200 | S3 (review) |
| **Design Development** | Coordinated MEP model | Revit/IFC | LOD 300 | S4 (approval) |
| **Construction Documents** | Electrical drawings (IFC) | PDF/DWG | LOD 350 | A7 (construction) |
| **As-Built** | Panel schedules (final) | COBie/Excel | LOD 400 | A1 (accepted) |
| **O&M Handover** | Equipment maintenance data | BIM-linked CMMS | LOG F | A1 (accepted) |

### EIR Document Template

**Project**: Main HQ Electrical Upgrade
**Appointing Party**: Facilities Management Department
**Lead Appointed Party**: MEP Engineering Firm
**Date**: 2024-01-15

#### 1. Project Overview
- **Asset Type**: Commercial office building
- **GFA**: 45,000 sq ft
- **MEP Scope**: Complete electrical service upgrade, lighting retrofit, fire alarm modernization
- **Contract Value**: $1.2M

#### 2. Technical Requirements

**2.1 Information Standards**
- BIM Standard: ISO 19650-2
- File Formats: Revit 2024, IFC 4.0, PDF/A
- Coordinate System: State Plane NAD83
- Units: Imperial (feet/inches)

**2.2 Level of Information Need**
- Design Models: LOD 300
- Construction Models: LOD 350
- As-Built Models: LOD 400
- Level of Information (LOG): LOG E (construction), LOG F (O&M)

**2.3 Software Platforms**
- Authoring: Autodesk Revit 2024
- Coordination: Navisworks Manage 2024
- CDE: BIM 360 Docs
- Clash Detection: Weekly clash reports, <20 active clashes at IFC

**2.4 Data Drops (Information Exchanges)**
- **Drop 1 (SD)**: Week 6 - Electrical one-line, preliminary panel schedules
- **Drop 2 (DD)**: Week 12 - Coordinated MEP model, lighting layouts
- **Drop 3 (CD)**: Week 20 - Construction drawings, equipment schedules
- **Drop 4 (As-Built)**: Week 52 - As-built models, O&M manuals

#### 3. MEP-Specific Deliverables

**3.1 Electrical**
- Service entrance details with utility coordination
- Panel schedules with load calculations (NEC Article 220)
- Lighting plans with photometric calculations
- Fire alarm system riser diagrams
- Equipment cut sheets and shop drawings

**3.2 Mechanical**
- HVAC load calculations (Manual J/S)
- Equipment schedules with performance data
- Ductwork layouts with CFM ratings
- Hydronic piping schematics
- Vibration isolation specifications

**3.3 Plumbing**
- Fixture schedules with water consumption data
- Riser diagrams for domestic water and sanitary
- Hot water heater sizing calculations
- Backflow preventer locations

**3.4 Fire Protection**
- Sprinkler hydraulic calculations
- Fire pump specifications
- Standpipe system details
- Fire department connection locations

#### 4. Quality Assurance Requirements
- All models must pass QA validation per `engineering-drawing-qaqc` skill
- JSON extraction required for all issued drawings
- Minimum 95% pass rate on title block completeness checks
- Zero critical failures on cross-reference validation
- Equipment schedules must include all required fields (manufacturer, model, voltage, phase)

**Integration with SKILL.md**: All PUBLISHED drawings must be exported to JSON format per `data_format_examples.md` schema and validated using QA rules before client delivery.

#### 5. Security and Access
- CDE access: Role-based (engineers, contractors, client)
- Sensitive data: Electrical security systems restricted to authorized personnel
- Backup frequency: Daily incremental, weekly full backup
- Retention period: 7 years post-project completion

---

## Level of Information Need (LOIN)

### LOIN Framework

LOIN defines the granularity and detail of information required at each project stage. It consists of two complementary dimensions:

1. **Level of Detail (LOD)**: Geometric representation accuracy
2. **Level of Information (LOG)**: Non-geometric attribute completeness

### Level of Detail (LOD) - MEP Systems

#### LOD 100: Conceptual
**Representation**: Generic symbols or masses
**MEP Example**: Electrical service represented as single box labeled "Main Electrical Room"
**Uses**: Feasibility studies, space planning
**Typical Elements**: Electrical rooms, equipment rooms (no specific equipment)

#### LOD 200: Approximate Geometry
**Representation**: Generic systems with approximate size/location
**MEP Example**: Electrical panels shown as generic boxes with amperage rating
**Uses**: Preliminary design, early coordination
**Typical Elements**:
- Transformers (approximate footprint)
- Switchgear (approximate dimensions)
- Major ductwork runs (single-line representation)

#### LOD 300: Precise Geometry
**Representation**: Accurate size, shape, location, and orientation
**MEP Example**: Electrical panel with accurate dimensions, mounting height, clearance zones
**Uses**: Construction documentation, coordination
**Typical Elements**:
- Electrical panels with door swing
- HVAC diffusers with neck connections
- Plumbing fixtures with rough-in dimensions
- Fire protection sprinkler heads with coverage areas

**MEP LOD 300 Requirements:**
```
Electrical Panel Board:
- Width, height, depth ±2 inches
- Mounting height to centerline
- Door swing direction
- Conduit entry locations (top/bottom)
- Clearance zones per NEC 110.26 (36" working space)
- Amperage rating displayed
- Voltage/phase labeled
```

#### LOD 350: Precise Geometry with Connections
**Representation**: LOD 300 + interface connections to other systems
**MEP Example**: Electrical panel with conduits modeled to first junction box
**Uses**: Fabrication coordination, detailed clash detection
**Typical Elements**:
- Panels with conduit home runs modeled
- HVAC equipment with duct/pipe connections
- Plumbing risers with branch connections
- Sprinkler mains with branch line takeoffs

#### LOD 400: Fabrication
**Representation**: Complete fabrication, assembly, and detailing information
**MEP Example**: Electrical panel with internal bus arrangement, breaker positions, wire sizing
**Uses**: Shop drawings, prefabrication
**Typical Elements**:
- Electrical panels with internal one-line diagram
- HVAC sheet metal with seam types and fasteners
- Plumbing pipe with weld or flange details
- Fire protection underground piping with thrust blocks

#### LOD 500: As-Built
**Representation**: Field-verified representation of installed conditions
**MEP Example**: Electrical panel with as-installed conduit routes, final circuit assignments
**Uses**: Operations and maintenance, facility management
**Typical Elements**:
- Panels with final circuit directory
- Equipment with commissioned performance data
- Systems with test and balance results
- Devices with asset tags and warranty information

### Level of Information (LOG) - MEP Systems

LOG defines non-geometric attributes required:

#### LOG A: Identification
**Attributes**: Type, mark, tag
**MEP Example**: Electrical panel "LP-1"
**Data Fields**:
- Equipment ID
- System type
- Discipline

#### LOG B: Appearance
**Attributes**: Material, finish, color
**MEP Example**: Panel "NEMA 1 enclosure, white enamel finish"
**Data Fields**:
- Enclosure type
- Coating/finish
- Color

#### LOG C: Performance
**Attributes**: Technical specifications
**MEP Example**: Panel "208V/120V, 3-phase, 4-wire, 100A main"
**Data Fields**:
- Voltage
- Phase
- Ampacity
- Short-circuit rating (AIC)
- Bus material (aluminum/copper)

#### LOG D: Manufacture
**Attributes**: Manufacturer, model, supplier
**MEP Example**: Panel "Square D, Model NQOD430M100, Supplier: Graybar"
**Data Fields**:
- Manufacturer name
- Model number
- Catalog number
- Supplier/distributor
- Lead time

#### LOG E: Construction
**Attributes**: Installation instructions, code compliance
**MEP Example**: Panel "Install per NEC 110.26, maintain 36\" clearance, torque lugs to 35 ft-lbs"
**Data Fields**:
- Installation requirements
- Code references (NEC, IMC, IPC)
- Special instructions
- Testing requirements

#### LOG F: Operations/Maintenance
**Attributes**: O&M manuals, maintenance schedules, warranty
**MEP Example**: Panel "Annual thermographic scan, quarterly torque check, 5-year warranty"
**Data Fields**:
- Maintenance frequency
- Spare parts list
- Warranty period
- Expected service life
- Replacement cost

### LOIN Matrix for MEP Systems

| Project Stage | Electrical | Mechanical | Plumbing | Fire Protection |
|---------------|------------|------------|----------|-----------------|
| **Concept** | LOD 100, LOG A | LOD 100, LOG A | LOD 100, LOG A | LOD 100, LOG A |
| **Schematic Design** | LOD 200, LOG C | LOD 200, LOG C | LOD 200, LOG C | LOD 200, LOG C |
| **Design Development** | LOD 300, LOG D | LOD 300, LOG D | LOD 300, LOG D | LOD 300, LOG D |
| **Construction Docs** | LOD 350, LOG E | LOD 350, LOG E | LOD 350, LOG E | LOD 350, LOG E |
| **As-Built** | LOD 400, LOG F | LOD 400, LOG F | LOD 400, LOG F | LOD 400, LOG F |

---

## BIM Execution Plan (BEP)

### BEP Purpose and Scope

The BIM Execution Plan is a formal document describing how information will be produced, managed, and delivered throughout the project. It operationalizes the EIR requirements.

### Pre-Contract BEP (Initial BEP)

Developed during bid/proposal phase to demonstrate capability to meet EIR.

**Contents:**
1. Understanding of project information requirements
2. Proposed information delivery strategy
3. Software and technology platforms
4. Team structure and roles
5. Preliminary delivery schedule
6. Risk mitigation strategies

### Post-Contract BEP (Confirmed BEP)

Finalized after contract award with agreed-upon delivery plan.

**Contents:**
1. Detailed information production methods and procedures
2. Confirmed CDE structure and workflows
3. Roles and responsibilities matrix (RACI)
4. Detailed information delivery schedule (TIDP)
5. Model quality assurance procedures
6. Coordination and clash detection protocols
7. Change management procedures

### BEP Template Structure

---

**BIM EXECUTION PLAN**
Project: Main HQ Electrical Upgrade
Version: 2.0 (Post-Contract Confirmed)
Date: 2024-02-01

---

#### Section 1: Project Information

**1.1 Project Overview**
- Project Name: Main HQ Electrical Upgrade
- Project Number: HQ2024-ELEC
- Client: Corporate Facilities Management
- Lead Appointed Party: ABC MEP Engineering
- Contract Value: $1.2M
- Contract Duration: 12 months
- Substantial Completion: 2024-12-31

**1.2 Project Drivers**
- Replace aging 480V electrical service with new 480V/277V service
- Upgrade interior lighting to LED (energy code compliance)
- Modernize fire alarm system to addressable
- Reduce energy consumption by 30%

**1.3 Information Requirements**
- EIR Reference: HQ2024-ELEC-EIR-v1.0.pdf
- Key Deliverables: Coordinated MEP models (LOD 350), construction drawings, as-built data
- Critical Success Factor: Zero electrical design errors during construction

#### Section 2: Information Management Strategy

**2.1 Project Information Model (PIM) Overview**

```
Project Information Model Structure:
├── Architectural Model (Reference)
├── Structural Model (Reference)
├── MEP Model (Lead)
│   ├── Electrical Model (Primary responsibility)
│   ├── Mechanical Model (Coordination)
│   ├── Plumbing Model (Coordination)
│   └── Fire Protection Model (Primary responsibility)
└── Federated Coordination Model
```

**2.2 Software Ecosystem**
- **Authoring**: Autodesk Revit 2024 (Electrical and Fire Alarm)
- **Coordination**: Navisworks Manage 2024
- **Clash Detection**: Navisworks Clash Detective
- **Calculations**: SKM PowerTools (short circuit/coordination), AGi32 (lighting)
- **CDE Platform**: Autodesk BIM 360 Docs
- **Drawing Production**: Revit + AutoCAD 2024
- **QA Validation**: engineering-drawing-qaqc skill (JSON extraction + rule validation)

**2.3 Level of Information Need**
- Design Phase: LOD 300, LOG D
- Construction Phase: LOD 350, LOG E
- As-Built: LOD 400, LOG F

**2.4 File Formats and Standards**
- Native: Revit (.rvt), AutoCAD (.dwg)
- Exchange: IFC 4.0 (COBie 2.4 for O&M data)
- Deliverables: PDF/A (drawings), Excel/CSV (schedules), JSON (QA validation data)

#### Section 3: Roles and Responsibilities

**3.1 RACI Matrix**

| Task | Lead Electrical Engineer | Mechanical Coordinator | QA Manager | BIM Manager | Client |
|------|--------------------------|------------------------|------------|-------------|--------|
| Electrical model authoring | **R/A** | I | I | C | I |
| Lighting design | **R/A** | C | I | I | C |
| Panel schedules | **R/A** | I | C | I | A |
| Clash detection | C | C | I | **R/A** | I |
| MEP coordination meetings | **A** | **R** | I | C | I |
| Drawing QA validation | C | I | **R/A** | C | I |
| Model publication (SHARED) | **R** | I | C | **A** | I |
| IFC issuance | C | I | C | **R/A** | **A** |

**Legend**: R = Responsible, A = Accountable, C = Consulted, I = Informed

**3.2 Key Personnel**

| Role | Name | Organization | Contact | Responsibilities |
|------|------|--------------|---------|------------------|
| Lead Appointed Party | John Smith, PE | ABC MEP Eng | jsmith@abc.com | Overall project delivery |
| Electrical Lead | Jane Doe, PE | ABC MEP Eng | jdoe@abc.com | Electrical design and coordination |
| BIM Manager | Robert Lee | ABC MEP Eng | rlee@abc.com | Model coordination, CDE management |
| QA Manager | Sarah Johnson | ABC MEP Eng | sjohnson@abc.com | Drawing validation, code compliance |
| Client Representative | Mike Brown | Facilities Mgmt | mbrown@client.com | EIR acceptance, design approvals |

#### Section 4: Information Production Methods

**4.1 Model Development Workflow**

```
Week 1-4: Schematic Design (LOD 200)
├── Develop electrical one-line diagram
├── Size main service and distribution equipment
├── Preliminary panel locations
└── Lighting load calculations

Week 5-8: Design Development (LOD 300)
├── Refine panel locations with architectural input
├── Route major conduit/cable tray runs
├── Complete lighting layouts
├── Fire alarm device placement
└── First coordination with mechanical/plumbing

Week 9-16: Construction Documents (LOD 350)
├── Detailed conduit routing (home runs to first junction)
├── Final panel schedules with load calculations
├── Grounding and bonding details
├── Lighting control sequences
├── Complete fire alarm riser diagram
└── Weekly clash detection and resolution

Week 17-20: Construction Issuance
├── Final coordination model review
├── Drawing production from Revit
├── QA validation (engineering-drawing-qaqc)
├── IFC package assembly
└── Client authorization (A7)

Week 40-52: As-Built (LOD 400)
├── Field verification surveys
├── Update models with as-installed conditions
├── Populate O&M data (LOG F)
├── Final QA validation
└── AIM delivery to client
```

**4.2 Modeling Standards**

**Electrical Modeling Guidelines:**
- All electrical rooms modeled with NEC 110.26 working clearance zones
- Panels modeled with accurate door swings and required access
- Conduit home runs modeled to first junction box or pull point
- Lighting fixtures include photometric IES files
- Fire alarm devices modeled at mounting height with coverage zones
- Grounding electrodes and bonding jumpers modeled
- Equipment disconnects modeled at required locations

**Property Set Requirements (Electrical Panel Example):**
```
IFC Property Set: Pset_ElectricalDeviceCommon
- Manufacturer: [Text] "Square D"
- Model: [Text] "NQOD430M100"
- Voltage: [Real] 208
- PhaseReference: [Text] "3-phase, 4-wire"
- CurrentRating: [Real] 100
- ShortCircuitRating: [Real] 22000
- EnclosureType: [Text] "NEMA 1"
- MountingType: [Text] "Surface"

Custom Property Set: Pset_ElectricalPanel_LoadData
- TotalConnectedLoad_VA: [Real] 28500
- DemandLoad_VA: [Real] 21300
- LoadCalculationMethod: [Text] "NEC 220.82 Optional Method"
- DiversityFactor: [Real] 0.75
```

**4.3 Coordination Process**

**Weekly Clash Detection Protocol:**
1. **Monday AM**: All disciplines publish latest models to SHARED (S1)
2. **Tuesday**: BIM Manager runs clash detection in Navisworks
3. **Wednesday**: Coordination meeting to review clashes
   - **Hard clashes** (physical interference): Assign resolution responsibility
   - **Soft clashes** (clearance violations): Document for design review
   - **Workflow clashes** (sequencing issues): Flag for contractor input
4. **Thursday-Friday**: Disciplines resolve assigned clashes
5. **Friday PM**: Updated models published (S2)

**Clash Tolerance Thresholds:**
- Electrical conduit vs. structure: 2" minimum clearance
- Electrical panel vs. door swing: No interference
- Light fixture vs. HVAC diffuser: 4' minimum separation
- Fire alarm devices vs. obstructions: Per NFCA 72 spacing rules

**Target Clash Metrics:**
- New clashes per week: <10
- Resolved clashes per week: >15
- Active clashes at CD stage: <5 (all approved deviations)

#### Section 5: Common Data Environment (CDE) Implementation

**5.1 CDE Platform Configuration**

Platform: Autodesk BIM 360 Docs

**Folder Structure:**
```
HQ2024-Electrical/
├── 01_WIP/
│   ├── Electrical/
│   │   ├── Models/ (local Revit files)
│   │   ├── Calculations/ (SKM, AGi32)
│   │   └── References/ (equipment cut sheets)
│   ├── Mechanical/ (reference only)
│   └── Architectural/ (reference only)
├── 02_SHARED/
│   ├── Models/
│   │   ├── Electrical_DD_2024-03-15_S2.rvt
│   │   └── Federated_Coordination_2024-03-15_S2.nwf
│   ├── Clash_Reports/
│   │   └── Clash_Report_Week12_2024-03-18.html
│   └── Review_Comments/
├── 03_PUBLISHED/
│   ├── Drawings_IFC/
│   │   ├── E-301_Ground_Floor_Power_A7.pdf
│   │   └── E-101_Panel_Schedules_A7.pdf
│   ├── Specifications/
│   └── QA_Reports/
│       └── E-301_QA_Report_2024-06-01.csv
└── 04_ARCHIVED/
    └── As-Built/
        ├── Models/
        ├── O&M_Manuals/
        └── Commissioning_Reports/
```

**5.2 Model Publication Schedule (Task Information Delivery Plan - TIDP)**

| Week | Milestone | Deliverable | Container State | Authorization | Integration with SKILL.md |
|------|-----------|-------------|-----------------|---------------|---------------------------|
| 6 | SD Completion | One-line diagram, preliminary schedules | SHARED (S3) | Review | N/A (preliminary) |
| 12 | DD Completion | Coordinated MEP model (LOD 300) | SHARED (S4) | Approval | JSON export for early QA checks |
| 18 | 50% CD | Construction drawings (LOD 350) | SHARED (S3) | Review | Full QA validation with engineering-drawing-qaqc |
| 20 | 100% CD | Final construction drawings | PUBLISHED (A7) | Construction | **Mandatory QA validation, >95% pass rate required** |
| 24 | Issued for Construction | Addenda and RFI responses | PUBLISHED (A1/A2) | Information | QA validation for changed drawings |
| 52 | As-Built | As-built models and O&M data | ARCHIVED | Accepted | Final QA validation, JSON export to AIM |

**Integration Point**: All drawings in PUBLISHED state must pass QA validation using `engineering-drawing-qaqc` skill before client authorization. JSON extraction is performed using the schema defined in `data_format_examples.md`, and validation rules from `04_QA_QC_RULESETS` are applied. Reports are stored in `03_PUBLISHED/QA_Reports/`.

**5.3 Access Control Matrix**

| User Role | WIP | SHARED | PUBLISHED | ARCHIVED |
|-----------|-----|--------|-----------|----------|
| Electrical Engineer | Read/Write | Read/Write | Read | Read |
| Mechanical Engineer | No Access | Read | Read | Read |
| BIM Manager | Read | Read/Write | Read/Write | Read/Write |
| QA Manager | Read | Read | Read/Write | Read |
| Contractor | No Access | Read (S4 only) | Read | No Access |
| Client | No Access | No Access | Read | Read |

#### Section 6: Quality Assurance Procedures

**6.1 Model Quality Checks (Weekly)**

Performed before publishing to SHARED:
- [ ] Model opens without errors or warnings
- [ ] All elements on correct worksets and phases
- [ ] No duplicate or overlapping elements
- [ ] Coordinate system matches project base point
- [ ] Level names and elevations verified
- [ ] View templates applied consistently
- [ ] Unplaced elements resolved
- [ ] Model performance acceptable (<5 min open time)

**6.2 Drawing Quality Checks (Before IFC)**

Performed on all construction drawings before PUBLISHED:

**Title Block Validation:**
- [ ] Project name, number, and address correct
- [ ] Sheet title and number match sheet index
- [ ] Scale notation present and accurate
- [ ] Revision number and date current
- [ ] Drawn by and checked by initials present
- [ ] Professional engineer seal and signature (where required)

**Legend and Symbol Validation:**
- [ ] All symbols on drawing appear in legend
- [ ] Legend descriptions complete and accurate
- [ ] Symbol tags match equipment schedules
- [ ] No duplicate or conflicting symbol definitions

**Schedule Validation:**
- [ ] Panel schedules include load calculations
- [ ] Equipment schedules include all required fields (manufacturer, model, voltage, phase)
- [ ] Circuit directories match panel schedules
- [ ] No blank or placeholder entries

**Cross-Reference Validation:**
- [ ] All detail references point to valid sheet numbers
- [ ] Enlarged plan references accurate
- [ ] Related drawings listed in title block
- [ ] No references to deleted or superseded sheets

**Code Compliance Validation:**
- [ ] NEC working clearances shown (110.26)
- [ ] NFPA 70E arc flash boundaries labeled
- [ ] Fire alarm device spacing per NFCA 72
- [ ] Emergency lighting coverage per IBC/NFPA 101

**6.3 Automated QA Validation (Mandatory)**

All drawings in PUBLISHED state undergo automated validation using `engineering-drawing-qaqc` skill:

**Step 1**: Export drawing data to JSON format per `data_format_examples.md` schema
**Step 2**: Load QA rulesets from `04_QA_QC_RULESETS/Electrical/`
**Step 3**: Execute validation engine
**Step 4**: Generate compliance report (CSV + PDF)
**Step 5**: Review critical failures with design team
**Step 6**: Revalidate after corrections

**Acceptance Criteria:**
- Overall pass rate: ≥95%
- Critical failures: 0
- High-severity failures: ≤3 per sheet
- Medium-severity failures: ≤10 per sheet

**Sample QA Report Output:**
```csv
Sheet,Rule ID,Severity,Category,Status,Description,Details
E-301,QA-001,critical,title_block,PASS,Verify title block completeness,All required fields present
E-301,QA-102,high,legend,FAIL,Confirm symbols match legend,"Symbol 'LP-3' not found in legend"
E-301,QA-201-ELEC,critical,compliance,PASS,Verify panel load calculations included,Load calc present per NEC 220.82
E-302,QA-001,critical,title_block,PASS,Verify title block completeness,All required fields present
E-302,QA-103,medium,cross_reference,FAIL,Validate cross-sheet references,"Referenced sheet 'E-999' does not exist"
```

**6.4 Design Review Checkpoints**

| Review | Timing | Participants | Focus Areas | Deliverable |
|--------|--------|--------------|-------------|-------------|
| **Kickoff** | Week 1 | All disciplines + client | Confirm EIR understanding, review BEP | Signed BEP |
| **30% Design** | Week 6 | Lead engineers | Major system layouts, equipment sizing | SD approval (S3) |
| **60% Design** | Week 12 | All disciplines | Coordination clashes, space conflicts | DD approval (S4) |
| **90% Design** | Week 18 | All + contractor | Constructability, code compliance | 50% CD comments |
| **IFC Ready** | Week 20 | All + QA manager | Final QA validation, client approval | IFC authorization (A7) |

#### Section 7: Risk Management

**7.1 Information Management Risks**

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| Model coordination delays | Medium | High | Weekly clash detection, dedicated BIM coordinator |
| Software version incompatibility | Low | Medium | Standardize on Revit 2024, IFC export for exchange |
| Data loss (CDE failure) | Low | Critical | Daily BIM 360 backups, local backup copies |
| QA validation failures at IFC | Medium | High | Implement early QA checks at DD stage, iterative validation |
| Incomplete O&M data at closeout | High | Medium | Populate LOG F attributes during construction, not at end |
| Client rejection due to non-conformance | Low | Critical | Regular client reviews, strict adherence to EIR and BEP |

**7.2 Contingency Plans**

- **CDE Downtime**: Local file sync protocol, resume from last saved state
- **Clash Detection Failures**: Manual coordination using section views and schedules
- **QA Validation Tool Unavailable**: Manual checklist validation (slower, less consistent)
- **Late Design Changes**: Change order process with impact assessment on BIM deliverables

#### Section 8: Change Management

**8.1 BEP Change Control**

Changes to this BEP require:
1. Written change request to BIM Manager
2. Impact assessment (cost, schedule, deliverables)
3. Client approval for changes affecting EIR compliance
4. Updated BEP version with revision log

**8.2 Model Change Workflow**

For changes after IFC issuance:
1. Contractor submits RFI or ASI through CDE
2. Design team evaluates in coordination model
3. If approved, model updated and republished (new revision)
4. Affected drawings revised and reissued (PUBLISHED)
5. QA validation repeated for revised drawings
6. Change log updated in federated model

#### Section 9: Handover and Closeout

**9.1 Asset Information Model (AIM) Delivery**

Final deliverables to client:
- As-built Revit models (LOD 400, LOG F)
- IFC 4.0 export with COBie 2.4 data
- PDF drawing set with hyperlinked equipment schedules
- O&M manuals linked to equipment in model
- QA validation reports for all as-built drawings
- Equipment asset tags cross-referenced to model

**9.2 AIM Acceptance Criteria**

- All equipment includes manufacturer, model, serial number
- Maintenance schedules populated for all serviceable equipment
- Warranty information attached to equipment records
- Spare parts lists included for critical systems
- Test and balance reports linked to HVAC equipment
- Commissioning reports linked to electrical systems

---

**BEP Approval**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Lead Appointed Party | John Smith, PE | _____________ | 2024-02-01 |
| BIM Manager | Robert Lee | _____________ | 2024-02-01 |
| Client Representative | Mike Brown | _____________ | 2024-02-01 |

---

## Asset Information Model (AIM)

### AIM Overview

The Asset Information Model is the outcome of the design and construction process, containing all information required to operate and maintain the asset. It is derived from the Project Information Model (PIM) but focuses on operational needs rather than construction.

### PIM to AIM Transition

```
┌─────────────────────────────────────────────────────────────────┐
│               PROJECT INFORMATION MODEL (PIM)                    │
│  Design and construction information, including temporary works  │
├─────────────────────────────────────────────────────────────────┤
│  • Electrical construction details (conduit routing)             │
│  • Mechanical equipment installation sequences                   │
│  • Plumbing rough-in dimensions                                  │
│  • Fire protection test and flush procedures                     │
│  • Temporary power and HVAC                                      │
└───────────────────────────┬─────────────────────────────────────┘
                            │ Filter and refine
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│               ASSET INFORMATION MODEL (AIM)                      │
│  Operational information for facility management                 │
├─────────────────────────────────────────────────────────────────┤
│  • Electrical equipment with maintenance schedules               │
│  • Mechanical equipment with performance data                    │
│  • Plumbing fixtures with water consumption rates                │
│  • Fire protection test and inspection requirements              │
│  • Warranty and spare parts information                          │
└─────────────────────────────────────────────────────────────────┘
```

**Removed from AIM:**
- Construction sequencing information
- Temporary systems
- Unused design alternates
- Contractor-specific shop drawings

**Enhanced in AIM:**
- Equipment serial numbers and asset tags
- Commissioning and test results
- Warranty expiration dates
- Maintenance procedures and frequencies
- Energy performance data

### AIM Content Requirements - MEP Systems

#### Electrical Systems

**Equipment Included:**
- Service entrance equipment (transformers, switchgear)
- Distribution panels and sub-panels
- Lighting fixtures and controls
- Emergency and egress lighting
- Fire alarm system components
- Motor control centers
- Uninterruptible power supplies (UPS)
- Standby generators

**Required Attributes (LOG F):**
- Equipment nameplate data
- Commissioning test results
- Protective device settings (breaker trip curves, relay settings)
- Maintenance schedule (thermographic scans, torque checks)
- Spare breakers and fuses inventory
- Utility account numbers and contacts
- Single-line diagrams with protective device coordination
- Arc flash analysis labels

#### Mechanical Systems

**Equipment Included:**
- HVAC equipment (chillers, boilers, air handlers)
- Ductwork and air distribution devices
- Controls and building automation system (BAS)
- Exhaust fans and ventilation systems
- Pumps and hydronic piping

**Required Attributes:**
- Equipment performance data (tons, CFM, BTU/hr)
- Filter sizes and replacement schedules
- Belt sizes and tension specifications
- Vibration isolation details
- Test and balance reports
- BAS programming and control sequences
- Refrigerant type and charge quantities

#### Plumbing Systems

**Equipment Included:**
- Domestic water heaters
- Pumps (domestic, fire, sump)
- Fixtures and trim
- Backflow preventers
- Water treatment equipment

**Required Attributes:**
- Fixture flow rates and consumption data
- Backflow test and certification schedule
- Water heater capacity and energy factor
- Pump curves and operating points
- Plumbing fixture count (for water audit compliance)

#### Fire Protection Systems

**Equipment Included:**
- Sprinkler system piping and heads
- Fire pumps and controllers
- Standpipes and hose connections
- Fire department connections

**Required Attributes:**
- Hydraulic calculation reports
- Sprinkler head temperature ratings
- Fire pump flow test results
- ITM (Inspection, Testing, Maintenance) schedules per NFPA 25
- Impairment procedures

### AIM Integration with CMMS

The AIM should be integrated with the organization's Computerized Maintenance Management System (CMMS) for operational efficiency.

**Integration Workflow:**
1. Export equipment data from AIM (IFC or COBie format)
2. Import into CMMS (e.g., Maximo, eMaint, Fiix)
3. Link maintenance work orders to BIM equipment records
4. Update equipment records with service history
5. Generate replacement forecasts based on service life data

**Example COBie Export (Electrical Panel):**
```
Type.Name: Panelboard
Type.Manufacturer: Square D
Type.ModelNumber: NQOD430M100
Type.WarrantyStartDate: 2024-12-15
Type.WarrantyDuration: 5 years
Component.SerialNumber: SN123456789
Component.TagNumber: LP-1
Component.InstallationDate: 2024-12-15
Component.WarrantyStartDate: 2024-12-15
Space.Name: Electrical Room 101
Floor.Name: Ground Floor
Attribute.Name: Voltage
Attribute.Value: 208
Attribute.Unit: Volts
Attribute.Name: MainBreakerRating
Attribute.Value: 100
Attribute.Unit: Amperes
Task.Name: Thermographic Inspection
Task.Frequency: 12 months
Task.Duration: 1 hour
```

---

## Model Delivery Workflows

### Stage-Gate Information Delivery

Each project stage has specific information deliverables with defined acceptance criteria.

#### Stage 1: Concept Design

**Deliverables:**
- Space allocation diagrams (electrical rooms, equipment rooms)
- Preliminary load calculations
- Single-line diagrams (major distribution only)
- Estimated equipment sizes and capacities

**LOIN**: LOD 100, LOG A (identification only)

**Authorization**: S2 (suitable for information)

**QA Integration**: Not applicable (conceptual stage)

#### Stage 2: Schematic Design

**Deliverables:**
- Electrical one-line diagram with main switchgear and distribution
- Preliminary panel schedules
- Lighting layouts with fixture types
- Major mechanical equipment layouts
- Plumbing riser diagrams

**LOIN**: LOD 200, LOG C (performance data)

**Authorization**: S3 (suitable for review and comment)

**QA Integration**: Early JSON extraction to validate title block standards and basic completeness

#### Stage 3: Design Development

**Deliverables:**
- Coordinated MEP models (3D)
- Detailed panel schedules with load calculations
- Lighting photometric calculations
- Fire alarm riser diagrams
- Equipment schedules with manufacturer data

**LOIN**: LOD 300, LOG D (manufacture data)

**Authorization**: S4 (suitable for stage approval)

**QA Integration**: Full QA validation using `engineering-drawing-qaqc` skill
- Export drawings to JSON per `data_format_examples.md`
- Validate against standard rulesets in `04_QA_QC_RULESETS`
- Minimum 90% pass rate required for progression

#### Stage 4: Construction Documentation

**Deliverables:**
- Issued for Construction (IFC) drawings
- Coordinated MEP models with connections (LOD 350)
- Complete equipment schedules
- Specifications and technical provisions
- Short circuit and coordination studies
- Energy code compliance documentation

**LOIN**: LOD 350, LOG E (construction/installation data)

**Authorization**: A7 (approved for construction)

**QA Integration**: **Mandatory QA validation checkpoint**
- All drawings exported to JSON
- Automated validation against project-specific QA rules
- Zero critical failures allowed
- >95% overall pass rate required
- PDF compliance reports included in submittal package
- Client review of QA reports before authorization

#### Stage 5: Construction

**Deliverables:**
- RFI responses with model markups
- Addenda and revisions
- Submittal reviews
- Coordination updates (as conflicts arise)

**LOIN**: LOD 350-400 (fabrication detail for complex assemblies)

**Authorization**: A1/A2 (accepted/accepted with comments), A4 (revise and resubmit)

**QA Integration**: QA validation for all revised drawings before reissuance

#### Stage 6: As-Built/O&M Handover

**Deliverables:**
- As-built models reflecting field-verified conditions
- Equipment serial numbers and asset tags
- Commissioning reports
- O&M manuals linked to equipment
- Warranty documentation
- Training materials for facilities staff

**LOIN**: LOD 400, LOG F (operations and maintenance)

**Authorization**: A1 (accepted) → Transition to AIM

**QA Integration**: Final QA validation of as-built drawings, JSON export for AIM integration

---

## Naming Conventions

### File Naming Standard (ISO 19650-2 Compliant)

**Structure:**
```
[Project]-[Originator]-[Volume]-[Level]-[Type]-[Role]-[Number]-[Status].[Extension]

Components:
- Project: 6-character project code
- Originator: 3-character organization code
- Volume: 2-character building/volume identifier
- Level: 2-character level/floor identifier
- Type: 2-character document type
- Role: 3-character discipline role
- Number: 4-digit sequential number
- Status: Suitability/authorization code (S1-S4, A1-A7)
- Extension: File type (rvt, nwf, pdf, dwg, xlsx, json)
```

### MEP File Naming Examples

**Electrical Revit Model:**
```
HQ2024-ABC-01-GF-M3-ELE-0101-S4.rvt

Breakdown:
- HQ2024: Main HQ Electrical Upgrade project
- ABC: ABC MEP Engineering firm
- 01: Building 1
- GF: Ground floor
- M3: 3D design model
- ELE: Electrical discipline
- 0101: Model sequence 1
- S4: Suitable for stage approval
- .rvt: Revit model
```

**Electrical One-Line Diagram PDF:**
```
HQ2024-ABC-01-XX-DR-ELE-0201-A7.pdf

Breakdown:
- XX: Applies to all levels
- DR: Drawing document type
- 0201: Drawing number
- A7: Approved for construction
- .pdf: PDF document
```

**Panel Schedule Excel File:**
```
HQ2024-ABC-01-GF-SC-ELE-0105-A1.xlsx

Breakdown:
- SC: Schedule document type
- 0105: Schedule document 5
- A1: Accepted by client
- .xlsx: Excel spreadsheet
```

**QA Validation JSON Export:**
```
HQ2024-ABC-01-GF-QA-ELE-0101-A7.json

Breakdown:
- QA: Quality assurance data
- 0101: Matching drawing number
- A7: Corresponds to IFC drawing status
- .json: JSON data file (per data_format_examples.md schema)
```

### Document Type Codes

| Code | Type | MEP Examples |
|------|------|--------------|
| **M2** | 2D model | Electrical riser diagrams |
| **M3** | 3D model | MEP coordination models |
| **DR** | Drawing | Electrical power plans, HVAC plans |
| **SC** | Schedule | Panel schedules, equipment schedules |
| **RP** | Report | QA validation reports, energy models |
| **CA** | Calculation | Load calculations, short circuit studies |
| **SP** | Specification | Technical specifications |
| **QA** | QA data | JSON extraction for validation |

### Discipline Role Codes

| Code | Discipline | Description |
|------|------------|-------------|
| **ELE** | Electrical | Power, lighting, fire alarm |
| **MEC** | Mechanical | HVAC, ventilation |
| **PLU** | Plumbing | Domestic water, sanitary, storm |
| **FPR** | Fire Protection | Sprinklers, standpipes, fire pumps |
| **CON** | Controls | BAS, lighting controls, energy management |
| **COM** | Communications | Data, telecom, AV, security |

### Level Codes

| Code | Level | Description |
|------|-------|-------------|
| **XX** | All levels | Information applies to entire building |
| **GF** | Ground floor | First floor above grade |
| **01-99** | Numbered floors | 01 = 1st floor, 02 = 2nd floor, etc. |
| **RF** | Roof | Rooftop equipment |
| **B1-B9** | Basement levels | B1 = first basement, B2 = second basement, etc. |
| **MZ** | Mezzanine | Intermediate floor |

### Sheet Numbering Convention

Traditional discipline-based sheet numbering (for drawings):

**Electrical:**
- E-001 to E-099: General sheets (legends, symbols, notes)
- E-100 to E-199: Site and exterior
- E-200 to E-299: Power plans (by floor)
- E-300 to E-399: Lighting plans (by floor)
- E-400 to E-499: Schedules and details
- E-500 to E-599: Fire alarm and communications
- E-600 to E-699: Special systems

**Mechanical:**
- M-001 to M-099: General sheets
- M-100 to M-199: Site and exterior
- M-200 to M-299: HVAC plans (by floor)
- M-300 to M-399: Piping and hydronic plans
- M-400 to M-499: Schedules and details
- M-500 to M-599: Equipment and controls

**Plumbing:**
- P-001 to P-099: General sheets
- P-100 to P-199: Plumbing plans (by floor)
- P-200 to P-299: Riser diagrams
- P-300 to P-399: Schedules and details

**Fire Protection:**
- FP-001 to FP-099: General sheets
- FP-100 to FP-199: Sprinkler plans (by floor)
- FP-200 to FP-299: Riser diagrams and hydraulic calculations
- FP-300 to FP-399: Details and schedules

---

## Integration with QA/QC Workflow

### Data Flow: BIM → IFC → JSON → QA Validation

The ISO 19650 information management workflow integrates seamlessly with the `engineering-drawing-qaqc` skill through structured data extraction and validation.

**Workflow Integration:**

```
┌────────────────────────────────────────────────────────────────┐
│  Step 1: BIM Authoring (WIP → SHARED)                          │
│  - Electrical engineer creates panel schedules in Revit         │
│  - BIM Manager coordinates with other disciplines               │
│  - Model published to SHARED (S3) for review                    │
└─────────────────────────┬──────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────┐
│  Step 2: IFC Export (SHARED → Drawing Production)              │
│  - Approved model (S4) used to generate construction drawings   │
│  - Revit sheets exported to PDF                                 │
│  - Drawing data extracted to IFC 4.0 format                     │
└─────────────────────────┬──────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────┐
│  Step 3: JSON Extraction (IFC → Structured Data)               │
│  - IFC entities mapped to JSON schema (per data_format_examples)│
│  - Title blocks, legends, symbols, schedules extracted          │
│  - Cross-references and notes captured                          │
│  - JSON file: HQ2024-ABC-01-GF-QA-ELE-0101-S4.json             │
└─────────────────────────┬──────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────┐
│  Step 4: QA Validation (engineering-drawing-qaqc skill)        │
│  - Load JSON data and project QA rulesets                       │
│  - Execute validation engine (title block, legend, schedules)   │
│  - Generate compliance report (CSV + PDF)                       │
│  - Report: HQ2024-ABC-01-GF-RP-ELE-0101-S4_QA_Report.pdf       │
└─────────────────────────┬──────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────┐
│  Step 5: Review and Correction (Iterative)                     │
│  - QA Manager reviews report with design team                   │
│  - Critical failures: Model updated in WIP, re-publish SHARED   │
│  - Non-critical: Document as acceptable deviations              │
│  - Re-validate until pass rate ≥95%                             │
└─────────────────────────┬──────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────┐
│  Step 6: Authorization (SHARED → PUBLISHED)                    │
│  - Validated drawings authorized by client                      │
│  - Status updated to A7 (approved for construction)             │
│  - Published to CDE PUBLISHED folder                            │
│  - QA reports included in submittal package                     │
└────────────────────────────────────────────────────────────────┘
```

### IFC to JSON Mapping

The IFC entities from BIM models are mapped to the JSON schema expected by `engineering-drawing-qaqc` skill:

**IFC Electrical Panel → JSON Equipment Schedule:**

```
IFC Entity: IfcElectricDistributionBoard
├── Name: "LP-1"
├── ObjectType: "Panelboard"
├── Pset_ElectricalDeviceCommon
│   ├── Manufacturer: "Square D"
│   ├── Model: "NQOD430M100"
│   ├── Voltage: 208
│   ├── PhaseReference: "3-phase, 4-wire"
│   └── CurrentRating: 100
└── Pset_ElectricalPanel_LoadData (custom)
    ├── TotalConnectedLoad_VA: 28500
    ├── DemandLoad_VA: 21300
    └── LoadCalculationMethod: "NEC 220.82"

↓ Maps to JSON ↓

{
  "schedules": {
    "panel_schedule": {
      "panel_id": "LP-1",
      "voltage": 120/208,
      "phases": 3,
      "main_breaker": "100A",
      "total_connected_load": 28500,
      "demand_load": 21300,
      "load_calculation_included": true,
      "circuits": [ ... ]
    }
  }
}
```

### QA Validation Rules Aligned with ISO 19650

**Rule Category: Information Completeness (EIR Compliance)**

```yaml
- id: QA-001-ISO19650
  description: Verify title block includes all EIR-required fields
  severity: critical
  category: information_completeness
  check:
    type: field_presence
    fields:
      - title_block.project
      - title_block.sheet_title
      - title_block.scale
      - title_block.revision
      - title_block.discipline
      - title_block.drawn_by
      - title_block.checked_by
  rationale: ISO 19650-2 requires complete metadata for information containers
```

**Rule Category: Level of Information Need (LOIN Compliance)**

```yaml
- id: QA-002-LOIN
  description: Verify electrical panels include LOG D attributes (manufacturer data)
  severity: high
  category: loin_compliance
  check:
    type: field_presence
    fields:
      - schedules.panel_schedule.*.manufacturer
      - schedules.panel_schedule.*.model
      - schedules.panel_schedule.*.voltage
      - schedules.panel_schedule.*.phases
  rationale: Design Development stage requires LOG D (manufacture) data per BEP
```

**Rule Category: Authorization Status**

```yaml
- id: QA-003-AUTH
  description: Verify drawings for IFC have authorization code A7
  severity: critical
  category: authorization
  check:
    type: field_format
    field: title_block.revision
    pattern: "^.*A7.*$"
  rationale: Only A7 (approved for construction) drawings may be issued for construction per ISO 19650-2
```

### BEP Compliance Reporting

The QA validation reports directly support BEP compliance monitoring:

**BEP Requirement**: "All published drawings must pass QA validation with >95% pass rate"

**QA Report Output:**
```
Project: HQ2024-Electrical
Validation Date: 2024-06-01
Stage: Construction Documents (IFC)

Summary:
- Total Sheets: 12
- Total Rules: 50
- Total Evaluations: 600
- Passed: 582
- Failed: 18
- Pass Rate: 97.0% ✓ (exceeds 95% requirement)

Critical Failures: 0 ✓
High-Severity Failures: 2
- E-301: Symbol 'LP-3' not found in legend
- E-405: Panel LP-2 missing load calculation

Recommendation: Resolve high-severity failures before client authorization.
BEP Compliance Status: PASS (pending corrections)
```

---

## MEP-Specific Considerations

### Electrical System Information Requirements

**Critical Information for AIM:**
- Protective device coordination study (time-current curves)
- Arc flash analysis labels and incident energy levels
- Short circuit calculations with fault current at each panel
- Load calculations per NEC Article 220
- Emergency power system test and transfer procedures
- Grounding electrode system details and resistance test results

**LOIN Requirements:**
- LOD 350 minimum for service entrance equipment
- LOD 400 for custom switchgear or specialty systems
- LOG F mandatory for all distribution equipment (panels, transformers)

### Mechanical System Information Requirements

**Critical Information for AIM:**
- Equipment schedules with capacity and efficiency data
- Test and balance reports (air and water side)
- BAS/DDC point lists and control sequences
- Filter schedules with MERV ratings and sizes
- Refrigerant logs and leak detection system data
- Vibration isolation and seismic restraint details

**LOIN Requirements:**
- LOD 300 for standard HVAC equipment
- LOD 350 for air handlers and custom units
- LOG F for all equipment (maintenance schedules, filter sizes, belt specs)

### Plumbing System Information Requirements

**Critical Information for AIM:**
- Backflow preventer test and certification schedule
- Water heater capacity, recovery rate, and energy factor
- Fixture flow rates and water consumption data (LEED/green building tracking)
- Pump curves and operating points
- Water treatment system maintenance (softeners, filters)

**LOIN Requirements:**
- LOD 300 for standard plumbing fixtures
- LOD 350 for pumps and water heaters
- LOG F for all equipment requiring periodic maintenance

### Fire Protection System Information Requirements

**Critical Information for AIM:**
- Hydraulic calculation reports per NFPA 13
- Sprinkler head temperature ratings and coverage areas
- Fire pump flow test results and controller settings
- ITM schedules per NFPA 25 (inspection, testing, maintenance)
- Impairment procedures and emergency contacts

**LOIN Requirements:**
- LOD 350 for fire protection equipment
- LOG F mandatory for all components (inspection frequencies, test procedures)

---

## Appendix A: Suitability and Authorization Code Reference

### Suitability Codes (SHARED State)

| Code | Description | Typical Use |
|------|-------------|-------------|
| **S0** | Initial status | Just uploaded, not yet reviewed |
| **S1** | Suitable for coordination | Clash detection, interdisciplinary coordination |
| **S2** | Suitable for information | FYI to other parties, no approval needed |
| **S3** | Suitable for review and comment | Design reviews, client comments |
| **S4** | Suitable for stage approval | Stage gate approval (SD, DD, CD) |

### Authorization Codes (PUBLISHED State)

| Code | Description | Typical Use |
|------|-------------|-------------|
| **A1** | Accepted | Client accepts deliverable as-is |
| **A2** | Accepted with comments | Accepted but with minor comments to incorporate |
| **A3** | Rejected | Does not meet requirements, substantial rework needed |
| **A4** | Revise and resubmit | Corrections required, resubmit for approval |
| **A5** | Information only | For reference, no approval required |
| **A6** | See comments | Review comments provided, response required |
| **A7** | Approved for construction | Authorized for use in construction (IFC status) |

---

## Appendix B: Reference Documents

**ISO Standards:**
- ISO 19650-1:2018 - Organization and digitization of information about buildings and civil engineering works, including building information modelling (BIM) — Information management using building information modelling — Part 1: Concepts and principles
- ISO 19650-2:2018 - Part 2: Delivery phase of the assets
- ISO 19650-3:2020 - Part 3: Operational phase of the assets
- ISO 19650-4:2022 - Part 4: Information exchange
- ISO 19650-5:2020 - Part 5: Security-minded approach to information management

**Related Standards:**
- BS 1192:2007 - Collaborative production of architectural, engineering and construction information (superseded by ISO 19650)
- PAS 1192-2:2013 - Specification for information management for the capital/delivery phase of construction projects using BIM (superseded by ISO 19650-2)
- COBie (Construction Operations Building Information Exchange) - ISO 16739 IFC format

**Industry Guidance:**
- UK BIM Framework - ISO 19650 guidance and templates
- buildingSMART International - IFC and openBIM standards
- RICS (Royal Institution of Chartered Surveyors) - BIM implementation guidance

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-06-01 | BIM Process Specialist | Initial document creation |
| 2.0 | 2025-10-22 | BIM Process Specialist | Enhanced with QA/QC integration, MEP examples, BEP template |

**Next Review**: 2026-01-01

---

**End of Document**
