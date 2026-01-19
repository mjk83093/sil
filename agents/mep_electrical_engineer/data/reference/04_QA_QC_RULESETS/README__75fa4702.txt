# QA/QC Rulesets

## Overview

This directory contains YAML-formatted validation rules for automated quality assurance and quality control (QA/QC) checks on engineering drawings. Rules are organized by category and discipline.

## Directory Structure

- **Core/** - Universal rules applicable to all drawing types (title blocks, revisions, legends)
- **Electrical/** - Electrical drawing-specific rules (NEC compliance, panel schedules, circuits)
- **Mechanical/** - HVAC/mechanical drawing rules (ventilation, equipment clearances, CFM ratings)
- **Plumbing/** - Plumbing system rules (fixture counts, backflow prevention, sizing)
- **Fire_Protection/** - Fire protection rules (sprinkler density, device spacing, hydraulic calcs)
- **Low_Voltage/** - Telecommunications and low-voltage system rules (grounding, clearances, cable types)

## Rule File Naming Convention

Format: `QA_[Category]_[Description].yaml`

Examples:
- `QA_TitleBlock_Completeness.yaml`
- `QA_Panel_Working_Clearance.yaml`
- `QA_Sprinkler_Density_Application.yaml`

## Rule ID Numbering System

| Range | Category | Discipline |
|-------|----------|------------|
| QA-001 to QA-050 | Title Block | All |
| QA-051 to QA-100 | Revision Control | All |
| QA-101 to QA-150 | Legend and Symbols | All |
| QA-151 to QA-200 | Cross-References | All |
| QA-201 to QA-299 | Electrical | ELEC |
| QA-301 to QA-399 | Mechanical | MECH |
| QA-401 to QA-499 | Plumbing | PLMB |
| QA-501 to QA-599 | Fire Protection | FP |
| QA-601 to QA-699 | Low Voltage/ICT | LV |
| QA-701 to QA-799 | Structural | STRUC |
| QA-801 to QA-899 | Civil | CIVIL |
| QA-901 to QA-999 | Custom/Project-Specific | PROJ |

## Severity Levels

- **critical** - Code violations, safety issues, missing required information (stop work)
- **high** - Important standards compliance, major drawing errors (requires correction before approval)
- **medium** - Best practices, completeness checks (should be addressed)
- **low** - Cosmetic issues, optional improvements (nice to have)

## Using Rules

Rules are loaded by the QA/QC validation engine and applied to extracted drawing data in JSON format. Each rule defines:
- **What to check** (fields, conditions)
- **How to validate** (check type, logic)
- **What constitutes failure** (condition not met)
- **Reporting details** (severity, category, description)

## Rule Development Workflow

1. **Identify requirement** - What standard/code requires this check?
2. **Define acceptance criteria** - What data indicates compliance?
3. **Write YAML rule** - Use schema from `qa_rules_schema.md`
4. **Test with sample data** - Verify rule catches known issues
5. **Document rationale** - Add comments explaining why rule exists
6. **Version and commit** - Track changes in changelog

## Testing Rules

Before deploying rules to production:
1. Create test cases with known pass/fail scenarios
2. Run validation engine with test data
3. Verify expected results match actual results
4. Document edge cases and limitations

## Maintenance

- **Quarterly Review**: Check for code updates (NEC, IBC, etc.)
- **Amendment Tracking**: Update rules when jurisdiction requirements change
- **False Positive Analysis**: Refine rules based on feedback
- **Performance Monitoring**: Ensure rules execute within time budgets (<5s per sheet)

## Contributing

When adding or modifying rules:
1. Follow the schema defined in `qa_rules_schema.md`
2. Use clear, descriptive rule IDs and descriptions
3. Include rationale and code references in comments
4. Add test cases
5. Update changelog

## Resources

- **Schema Documentation**: `../../references/qa_rules_schema.md`
- **Data Format**: `../../references/data_format_examples.md`
- **Glossary**: `../17_GLOSSARY_AND_TAXONOMY/Acronyms_Glossary.md`

---

**Last Updated**: 2025-01-22
**Curator**: EE_AI Platform Reference Library
