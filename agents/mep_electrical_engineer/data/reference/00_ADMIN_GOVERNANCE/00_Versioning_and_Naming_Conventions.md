# Versioning and Naming Conventions

**Document ID**: ADMIN-GOV-00
**Version**: 1.0.0
**Last Updated**: 2025-10-22
**Author**: MEP Knowledge Management Team
**Status**: Approved

## Table of Contents

1. [Purpose](#purpose)
2. [File Naming Standards](#file-naming-standards)
3. [Version Numbering Scheme](#version-numbering-scheme)
4. [Document Lifecycle States](#document-lifecycle-states)
5. [Metadata Requirements](#metadata-requirements)
6. [Examples by File Type](#examples-by-file-type)
7. [Special Cases](#special-cases)
8. [Compliance and Enforcement](#compliance-and-enforcement)

---

## Purpose

This document establishes mandatory standards for naming files and versioning documents within the MEP Engineering Knowledge Base. Consistent naming and versioning enable:

- **Traceability**: Clear audit trails for document evolution
- **Discovery**: Efficient search and retrieval across the knowledge base
- **Collaboration**: Reduced confusion in multi-contributor environments
- **Automation**: Programmatic parsing of filenames for tooling integration
- **Compliance**: Regulatory and quality management system (QMS) requirements

---

## File Naming Standards

### General Principles

All filenames must adhere to these principles:

1. **No Spaces**: Use underscores (`_`) or hyphens (`-`) as separators
2. **Lowercase Preferred**: Use lowercase for consistency (exceptions: acronyms)
3. **Descriptive**: Names should convey content without reading the file
4. **Concise**: Maximum 64 characters (excluding extension)
5. **No Special Characters**: Avoid `!@#$%^&*()+=[]{}|;:'"<>?,/\`

### Standard Naming Pattern

```
{DisciplinePrefix}_{DocumentType}_{SerialNumber}_{Title}_{VersionTag}.{extension}
```

**Components**:

- **DisciplinePrefix**: 1-2 character code (E, M, P, FP, A, S, C)
- **DocumentType**: Abbreviated type (DWG, SPEC, CALC, RPT, SOP, GUIDE)
- **SerialNumber**: Zero-padded numeric (001-999)
- **Title**: Short descriptive title (snake_case or kebab-case)
- **VersionTag**: Optional version identifier (v1-0-0, DRAFT, FINAL)
- **Extension**: Standard file extension (.md, .pdf, .dwg, .xlsx)

### Discipline Prefixes

| Prefix | Discipline                 | Example Usage               |
|--------|----------------------------|-----------------------------|
| E      | Electrical                 | E_CALC_001_voltage_drop.xlsx|
| M      | Mechanical                 | M_DWG_025_hvac_layout.dwg   |
| P      | Plumbing                   | P_SPEC_010_pipe_material.md |
| FP     | Fire Protection            | FP_RPT_003_sprinkler_calc.pdf|
| A      | Architectural (reference)  | A_DWG_100_floor_plan.dwg    |
| S      | Structural (reference)     | S_CALC_050_beam_schedule.xlsx|
| C      | Civil (reference)          | C_DWG_200_site_plan.dwg     |
| MEP    | Multi-Discipline           | MEP_SOP_001_coordination.md |
| ADMIN  | Administrative/Governance  | ADMIN_GOV_00_versioning.md  |

### Document Type Codes

| Code    | Document Type              | Extensions          |
|---------|----------------------------|---------------------|
| DWG     | Engineering Drawing        | .dwg, .dxf, .pdf    |
| SPEC    | Specification              | .md, .pdf, .docx    |
| CALC    | Calculation Sheet          | .xlsx, .pdf, .md    |
| RPT     | Report/Analysis            | .pdf, .md, .docx    |
| SOP     | Standard Operating Proc    | .md, .pdf           |
| GUIDE   | Reference Guide            | .md, .pdf           |
| STD     | Standard/Policy            | .md, .pdf           |
| FORM    | Template/Form              | .xlsx, .docx, .pdf  |
| CODE    | Code Snippet/Script        | .py, .js, .json     |
| DATA    | Dataset/Reference Data     | .json, .csv, .xlsx  |

### Serial Numbering Scheme

- **Range**: 001-999 per discipline and document type
- **Padding**: Always 3 digits with leading zeros
- **Assignment**: Sequential, managed by Knowledge Management Team
- **Gaps**: Acceptable; retired documents retain their numbers
- **Reuse**: Prohibited for 5 years after document retirement

---

## Version Numbering Scheme

### Semantic Versioning (MAJOR.MINOR.PATCH)

We follow **Semantic Versioning 2.0.0** principles adapted for engineering documentation:

```
MAJOR.MINOR.PATCH
```

**Format**: `v{MAJOR}.{MINOR}.{PATCH}`
**Example**: `v2.3.1`

### Version Component Definitions

#### MAJOR Version (X.0.0)

Increment when:
- **Breaking Changes**: Changes that invalidate previous versions
- **Code Compliance**: Updates for new code adoption (NEC 2023 → 2026)
- **Methodology Changes**: Fundamental approach alterations
- **Standard Revisions**: Major updates to referenced standards

**Examples**:
- Switching from NEC 2020 to NEC 2023 calculations
- Complete redesign of calculation methodology
- Incorporation of new regulatory requirements

**Impact**: Users must review entire document; previous versions may be obsolete.

#### MINOR Version (x.Y.0)

Increment when:
- **New Content**: Adding sections, chapters, or examples
- **Feature Additions**: New calculation methods or tools
- **Clarifications**: Significant expansions of existing content
- **Reference Updates**: Adding new citations or resources

**Examples**:
- Adding a new section on voltage drop calculations
- Including additional worked examples
- Expanding the scope to cover additional equipment types

**Impact**: Backward compatible; users can adopt incrementally.

#### PATCH Version (x.y.Z)

Increment when:
- **Error Corrections**: Typos, grammar, formatting fixes
- **Minor Clarifications**: Reworded sentences for clarity
- **Non-Substantive Updates**: Metadata, links, references
- **Cosmetic Changes**: Formatting, styling, layout

**Examples**:
- Fixing calculation errors in examples
- Correcting broken hyperlinks
- Updating contact information

**Impact**: No functional changes; safe to apply immediately.

### Pre-Release and Build Metadata

#### Pre-Release Versions

Format: `v1.0.0-alpha.1`, `v1.0.0-beta.2`, `v1.0.0-rc.1`

**Stages**:
- **alpha**: Internal development, incomplete features
- **beta**: Feature complete, undergoing testing
- **rc** (release candidate): Final testing before release

**Examples**:
```
v2.0.0-alpha.1   # First alpha of version 2.0.0
v2.0.0-beta.1    # First beta of version 2.0.0
v2.0.0-rc.1      # Release candidate 1
v2.0.0           # Official release
```

#### Build Metadata

Format: `v1.0.0+20251022`, `v1.0.0+build.123`

Use for internal tracking; does not affect version precedence.

### Version Precedence

Order (ascending):
```
v1.0.0-alpha.1 < v1.0.0-alpha.2 < v1.0.0-beta.1 < v1.0.0-rc.1 < v1.0.0 < v1.0.1 < v1.1.0 < v2.0.0
```

---

## Document Lifecycle States

Every document progresses through defined lifecycle states, tracked via metadata and workflow tools.

### State Definitions

#### 1. DRAFT

**Description**: Initial creation, not reviewed
**Visibility**: Author and assigned reviewers only
**Filename Suffix**: `_DRAFT` or version `v0.1.0`
**Approval**: None required
**Usage**: Internal development only

**Example**: `E_CALC_042_transformer_sizing_DRAFT.xlsx`

#### 2. REVIEW

**Description**: Submitted for peer or technical review
**Visibility**: Review team and stakeholders
**Filename Suffix**: `_REVIEW` or version `v0.9.0`
**Approval**: At least one technical reviewer
**Usage**: Review and comment only; not for production

**Example**: `M_SPEC_018_duct_material_v0-9-0_REVIEW.md`

#### 3. APPROVED

**Description**: Reviewed, approved, ready for use
**Visibility**: All users (per RBAC policy)
**Filename Suffix**: None (clean version number)
**Approval**: Technical Lead + QA Reviewer
**Usage**: Production-ready, official reference

**Example**: `P_SOP_005_pipe_sizing_v1-0-0.md`

#### 4. SUPERSEDED

**Description**: Replaced by newer version, archived
**Visibility**: Archive access only
**Filename Suffix**: `_SUPERSEDED` or moved to archive folder
**Approval**: Automatic upon new version approval
**Usage**: Historical reference only; not for new work

**Example**: `FP_RPT_010_hydraulic_calc_v2-1-0_SUPERSEDED.pdf`

#### 5. OBSOLETE

**Description**: No longer applicable, retained for audit
**Visibility**: Archive access only
**Filename Suffix**: `_OBSOLETE`
**Approval**: Knowledge Management Team
**Usage**: Audit trail only; not referenced in new work

**Example**: `E_CALC_001_old_nec2017_method_OBSOLETE.xlsx`

### State Transition Workflow

```
DRAFT → REVIEW → APPROVED → SUPERSEDED → OBSOLETE
   ↓       ↓
 (revise) (reject → DRAFT)
```

**Rules**:
- Only APPROVED documents can be SUPERSEDED
- DRAFT and REVIEW documents can be deleted without archiving
- SUPERSEDED and OBSOLETE documents must retain audit trail

---

## Metadata Requirements

All documents must include structured metadata in a consistent format.

### Standard Metadata Block (Markdown)

Place at the top of every Markdown document:

```markdown
# Document Title

**Document ID**: {Discipline}-{Type}-{SerialNumber}
**Version**: {MAJOR.MINOR.PATCH}
**Status**: {DRAFT | REVIEW | APPROVED | SUPERSEDED | OBSOLETE}
**Last Updated**: {YYYY-MM-DD}
**Author**: {Full Name or Team Name}
**Reviewer**: {Full Name} (if applicable)
**Approver**: {Full Name} (if applicable)
**NEC Version**: {2020 | 2023 | 2026} (if applicable)
**Related Docs**: {comma-separated document IDs}
**Keywords**: {comma-separated keywords}

## Revision History

| Version | Date       | Author      | Changes                          |
|---------|------------|-------------|----------------------------------|
| 1.0.0   | 2025-10-22 | J. Smith    | Initial release                  |
| 1.1.0   | 2025-11-15 | J. Smith    | Added section on grounding       |
```

### Extended Metadata (YAML Front Matter)

For tools that support YAML front matter:

```yaml
---
document_id: E-CALC-042
title: Transformer Sizing Calculator
version: 1.2.0
status: APPROVED
date_created: 2025-09-01
date_updated: 2025-10-22
author: Jane Doe
reviewers:
  - John Smith
  - Alice Johnson
approver: Robert Brown
discipline: Electrical
document_type: Calculation
nec_version: 2023
related_documents:
  - E-SPEC-010
  - E-GUIDE-005
keywords:
  - transformer
  - sizing
  - kVA
  - NEC 450
classification: Internal
copyright: © 2025 Company Name. All rights reserved.
license: Internal Use Only
---
```

### Metadata for Non-Text Files

For binary files (PDF, Excel, CAD), embed metadata using:

- **PDF**: Document Properties (Title, Author, Subject, Keywords, Custom Fields)
- **Excel**: File Properties (Title, Author, Comments, Custom Properties)
- **AutoCAD**: Drawing Properties (Title, Author, Keywords, Custom tab)

**Excel Custom Properties Example**:
```
Property Name       | Value
--------------------|------------------
DocumentID          | E-CALC-042
Version             | 1.2.0
Status              | APPROVED
NECVersion          | 2023
RelatedDocuments    | E-SPEC-010, E-GUIDE-005
```

---

## Examples by File Type

### Engineering Drawings

**Standard Format**:
```
{Discipline}_DWG_{SerialNumber}_{Title}_{VersionTag}.{extension}
```

**Examples**:
```
E_DWG_101_single_line_diagram_v1-0-0.dwg
M_DWG_025_hvac_riser_diagram_v2-1-0.pdf
P_DWG_050_plumbing_isometric_v1-3-2.dwg
FP_DWG_010_sprinkler_layout_v3-0-0.pdf
MEP_DWG_001_coordination_plan_v1-0-0.dwg
```

### Specifications

**Standard Format**:
```
{Discipline}_SPEC_{SerialNumber}_{Title}_v{Version}.md
```

**Examples**:
```
E_SPEC_010_cable_tray_material_v1-0-0.md
M_SPEC_018_duct_insulation_v2-0-0.md
P_SPEC_005_pipe_fittings_v1-2-0.md
FP_SPEC_003_sprinkler_heads_v1-0-0.md
```

### Calculation Sheets

**Standard Format**:
```
{Discipline}_CALC_{SerialNumber}_{Title}_v{Version}.xlsx
```

**Examples**:
```
E_CALC_042_transformer_sizing_v1-2-0.xlsx
E_CALC_033_voltage_drop_feeder_v3-0-0.xlsx
M_CALC_015_cooling_load_psychrometric_v2-1-0.xlsx
P_CALC_008_water_pressure_loss_v1-0-0.xlsx
FP_CALC_001_hydraulic_calculation_v2-0-0.xlsx
```

### Reports and Analysis

**Standard Format**:
```
{Discipline}_RPT_{SerialNumber}_{Title}_v{Version}.pdf
```

**Examples**:
```
E_RPT_020_arc_flash_study_v1-0-0.pdf
M_RPT_012_airflow_analysis_v2-0-0.pdf
P_RPT_005_water_quality_report_v1-1-0.pdf
FP_RPT_003_sprinkler_design_report_v1-0-0.pdf
```

### Standard Operating Procedures

**Standard Format**:
```
{Discipline}_SOP_{SerialNumber}_{Title}_v{Version}.md
```

**Examples**:
```
E_SOP_001_load_calculation_workflow_v1-0-0.md
M_SOP_003_duct_sizing_procedure_v2-1-0.md
MEP_SOP_010_coordination_workflow_v1-0-0.md
ADMIN_SOP_005_document_review_process_v1-0-0.md
```

### Reference Guides

**Standard Format**:
```
{Discipline}_GUIDE_{SerialNumber}_{Title}_v{Version}.md
```

**Examples**:
```
E_GUIDE_015_nec_article_220_summary_v1-0-0.md
M_GUIDE_008_ashrae_90_1_compliance_v2-0-0.md
P_GUIDE_012_ipc_fixture_units_v1-0-0.md
FP_GUIDE_005_nfpa_13_design_criteria_v1-0-0.md
```

### Code and Scripts

**Standard Format**:
```
{Discipline}_CODE_{SerialNumber}_{Title}_v{Version}.{py|js|json}
```

**Examples**:
```
E_CODE_005_nec_table_lookup_v1-0-0.py
M_CODE_010_psychrometric_calculator_v2-0-0.js
MEP_CODE_001_coordinate_clash_checker_v1-0-0.py
```

### Reference Data

**Standard Format**:
```
{Discipline}_DATA_{SerialNumber}_{Title}_v{Version}.{json|csv|xlsx}
```

**Examples**:
```
E_DATA_050_conductor_ampacity_nec2023_v1-0-0.json
M_DATA_025_refrigerant_properties_v1-0-0.csv
P_DATA_015_pipe_friction_factors_v1-0-0.xlsx
```

---

## Special Cases

### Multi-Discipline Documents

Use `MEP` prefix for documents covering multiple disciplines:

```
MEP_SOP_010_bim_coordination_v1-0-0.md
MEP_GUIDE_005_energy_modeling_workflow_v2-0-0.md
```

### Administrative Documents

Use `ADMIN` prefix for governance and management:

```
ADMIN_GOV_00_versioning_conventions_v1-0-0.md
ADMIN_SOP_003_access_request_process_v1-0-0.md
```

### Date-Stamped Documents

For reports tied to specific dates or events:

```
E_RPT_030_arc_flash_study_2025-10-22_v1-0-0.pdf
M_RPT_018_commissioning_report_2025-11-01_v1-0-0.pdf
```

### Client or Project-Specific Documents

Include project code after serial number:

```
E_CALC_055_PRJ2024_transformer_sizing_v1-0-0.xlsx
M_DWG_120_BLDG5_hvac_layout_v2-0-0.dwg
```

**Note**: Project-specific documents may not be included in the general knowledge base.

### Localized or Language Variants

Append language code (ISO 639-1):

```
E_GUIDE_015_nec_article_220_summary_v1-0-0_en.md
E_GUIDE_015_nec_article_220_summary_v1-0-0_es.md
```

---

## Compliance and Enforcement

### Version Control System Integration

- **Git Tagging**: Tag releases with version numbers (`v1.0.0`, `v1.1.0`)
- **Commit Messages**: Reference document IDs and versions
- **Branch Naming**: Use `feature/{DocID}-{description}`, `fix/{DocID}-{issue}`

**Example Git Workflow**:
```bash
# Create feature branch
git checkout -b feature/E-CALC-042-add-load-diversity

# Commit changes
git commit -m "E-CALC-042 v1.2.0: Add load diversity factors per NEC 220.40"

# Tag release
git tag -a v1.2.0 -m "E-CALC-042 Release v1.2.0"
git push origin v1.2.0
```

### Automated Validation

Implement pre-commit hooks or CI/CD checks to validate:
- Filename format compliance
- Metadata presence and format
- Version number validity (no skipped versions)
- Document ID uniqueness

### Non-Compliance Handling

**Severity Levels**:

1. **Critical**: Missing version number, duplicate document ID
   - **Action**: Block commit/upload until corrected

2. **Major**: Incorrect filename format, missing required metadata
   - **Action**: Warning with 48-hour correction period

3. **Minor**: Inconsistent capitalization, suboptimal naming
   - **Action**: Advisory notice, correct at next update

### Exceptions and Waivers

Request exceptions via Knowledge Management Team:
- **Justification**: Required for approval
- **Duration**: Temporary (expires after 6 months) or permanent
- **Documentation**: Exception logged in `ADMIN_REGISTER_001_exceptions.md`

---

## Appendix A: Quick Reference

### Filename Checklist

- [ ] Discipline prefix present and correct
- [ ] Document type code present
- [ ] Serial number is 3 digits with leading zeros
- [ ] Title is descriptive and concise (≤40 characters)
- [ ] Version tag included for final versions
- [ ] No spaces or special characters
- [ ] File extension is standard

### Version Increment Decision Tree

```
Is this a breaking change or major methodology update?
  YES → Increment MAJOR version (X.0.0)
  NO  ↓

Are you adding new sections or features?
  YES → Increment MINOR version (x.Y.0)
  NO  ↓

Are you fixing errors or making minor updates?
  YES → Increment PATCH version (x.y.Z)
```

### Common Mistakes to Avoid

1. **Spaces in filenames**: Use underscores or hyphens
2. **Skipping versions**: Follow semantic versioning strictly
3. **Inconsistent prefixes**: Use standard discipline codes
4. **Missing metadata**: Include all required fields
5. **Vague titles**: Be specific about content
6. **Reusing serial numbers**: Each document gets unique ID

---

## Appendix B: Metadata Templates

### Minimal Metadata (Quick Documents)

```markdown
**Document ID**: E-CALC-042
**Version**: 1.0.0
**Last Updated**: 2025-10-22
**Author**: Jane Doe
**Status**: APPROVED
```

### Standard Metadata (Most Documents)

```markdown
**Document ID**: E-CALC-042
**Version**: 1.2.0
**Status**: APPROVED
**Last Updated**: 2025-10-22
**Author**: Jane Doe
**Reviewer**: John Smith
**Approver**: Robert Brown
**NEC Version**: 2023
**Related Docs**: E-SPEC-010, E-GUIDE-005
**Keywords**: transformer, sizing, kVA, NEC 450

## Revision History

| Version | Date       | Author   | Changes                     |
|---------|------------|----------|-----------------------------|
| 1.0.0   | 2025-09-01 | J. Doe   | Initial release             |
| 1.1.0   | 2025-09-15 | J. Doe   | Added diversity factors     |
| 1.2.0   | 2025-10-22 | J. Doe   | Updated for NEC 2023        |
```

---

**End of Document**

**Approval Signatures**:
- Technical Lead: ___________________________ Date: __________
- QA Reviewer: ______________________________ Date: __________
- Knowledge Manager: ________________________ Date: __________
