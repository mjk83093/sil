# Contributions Style Guide

**Document ID**: ADMIN-GOV-05
**Version**: 1.0.0
**Last Updated**: 2025-10-22
**Author**: MEP Technical Writing Team
**Status**: Approved

## Table of Contents

1. [Purpose and Principles](#purpose-and-principles)
2. [Writing Style Guidelines](#writing-style-guidelines)
3. [Markdown Formatting Standards](#markdown-formatting-standards)
4. [Code and Example Formatting](#code-and-example-formatting)
5. [Diagrams and Visual Content](#diagrams-and-visual-content)
6. [Tables and Data Presentation](#tables-and-data-presentation)
7. [Terminology and Consistency](#terminology-and-consistency)
8. [Document Structure Templates](#document-structure-templates)
9. [Review Checklist](#review-checklist)
10. [Common Mistakes to Avoid](#common-mistakes-to-avoid)

---

## Purpose and Principles

### Purpose

This style guide establishes standards for writing and formatting contributions to the MEP Engineering Knowledge Base. Consistent style ensures:

- **Clarity**: Content is easy to understand and follow
- **Professionalism**: Knowledge base maintains high quality standards
- **Usability**: Users can quickly find and apply information
- **Maintainability**: Content can be efficiently updated and revised
- **Accessibility**: Content is usable by diverse audiences and assistive technologies

### Core Writing Principles

#### 1. Clarity Over Cleverness

**Do**: Write straightforwardly and directly
- "Calculate the load by adding all connected loads"

**Don't**: Use unnecessarily complex or flowery language
- "Ascertain the electrical burden by performing the summation of all electrically connected apparatus"

#### 2. Active Voice Preferred

**Do**: Use active voice for directness and clarity
- "Size the conductor using NEC Table 310.16"

**Don't**: Overuse passive voice
- "The conductor should be sized by the engineer using what is found in NEC Table 310.16"

**Exception**: Passive voice acceptable when actor is unknown or unimportant
- "The code was updated in 2023" (who updated is less important than the fact)

#### 3. Conciseness Without Sacrificing Completeness

**Do**: Be concise but complete
- "NEC 210.19(A)(1) requires branch circuit conductors to have ampacity at least equal to the maximum load."

**Don't**: Be verbose or redundant
- "According to what is stated in the National Electrical Code in Article 210, Section 19, Subsection A, Paragraph 1, it is required that the conductors used for branch circuits must have an ampacity rating that is not less than the maximum load that will be served by the circuit."

#### 4. Technical Accuracy Over Simplification

**Do**: Use precise technical terminology
- "Conductor ampacity must account for ambient temperature correction factors"

**Don't**: Oversimplify at the cost of accuracy
- "Make the wire bigger if it's hot outside"

#### 5. Audience-Appropriate Complexity

**Match complexity to target audience**:
- **Fundamental**: Explain basic concepts, define terms
- **Intermediate**: Assume working knowledge, focus on application
- **Advanced**: Use technical shorthand, focus on edge cases and optimization
- **Expert**: Assume deep expertise, discuss cutting-edge topics

---

## Writing Style Guidelines

### Voice and Tone

#### Voice Characteristics

**Professional**: Maintain professional engineering standards
- Use proper terminology and technical language
- Avoid slang, colloquialisms, or humor (unless clearly appropriate)
- Respect industry conventions and practices

**Helpful**: Focus on enabling the reader to succeed
- Provide context and rationale, not just instructions
- Anticipate questions and address them proactively
- Include examples and practical applications

**Authoritative**: Write with confidence and expertise
- Make clear statements backed by code or engineering principles
- Use definitive language when appropriate ("must", "shall", "is required")
- Cite authoritative sources (NEC, standards, research)

**Respectful**: Acknowledge the reader's intelligence and expertise
- Don't talk down or over-explain obvious concepts
- Provide options and context for decision-making
- Avoid absolutist language when multiple approaches are valid

#### Tone Guidelines

**Do**:
- ✅ Be direct and clear
- ✅ Use inclusive language ("engineers", "we", "designers")
- ✅ Provide context for why something matters
- ✅ Acknowledge complexity when it exists

**Don't**:
- ❌ Be condescending or patronizing
- ❌ Use marketing speak or hype
- ❌ Overuse exclamation points or emphatic language
- ❌ Make unsupported claims or generalizations

### Grammar and Mechanics

#### Sentence Structure

**Prefer short to medium sentences**: 15-25 words average
- Break complex ideas into multiple sentences
- Use transitional phrases to connect ideas
- Vary sentence length for readability

**Example**:
```
✅ Good: NEC 210.19(A)(1) establishes minimum conductor ampacity. The ampacity
must meet or exceed the maximum load. This prevents conductor overheating.

❌ Too Long: NEC 210.19(A)(1) establishes minimum conductor ampacity requirements
whereby the ampacity must meet or exceed the maximum load to be served in order
to prevent conductor overheating which is a safety hazard.
```

#### Paragraphs

**One idea per paragraph**: 3-5 sentences typical
- Start with topic sentence stating main idea
- Follow with supporting details or examples
- End with transition or summary if appropriate

**Use short paragraphs**: 50-100 words
- Break up long blocks of text
- Use headings to organize sections
- Leave blank lines between paragraphs

#### Punctuation

**Oxford Comma**: Always use serial comma
- ✅ "conductors, conduits, and raceways"
- ❌ "conductors, conduits and raceways"

**Em Dash**: Use for emphasis or interjections
- "Conductor sizing—when done correctly—prevents overheating"
- No spaces around em dash (—)

**Colon**: Introduce lists, examples, or explanations
- "Three factors affect ampacity: temperature, insulation, and grouping"

**Semicolon**: Connect related independent clauses
- "Copper has higher conductivity; aluminum is lighter and less expensive"

#### Capitalization

**Title Case for Headings**: Capitalize major words
- ✅ "Voltage Drop Calculation Methods"
- ❌ "voltage drop calculation methods"

**Sentence Case for Most Text**: Capitalize only first word and proper nouns
- ✅ "The National Electrical Code requires..."
- ❌ "The national electrical code Requires..."

**Proper Nouns and Acronyms**: Always capitalize
- NEC, ASHRAE, IEEE, NFPA
- National Electrical Code, International Building Code
- AutoCAD, Revit, Python

**Code Sections**: Capitalize "Article", "Section", "Table" when referencing specific ones
- "NEC Article 220"
- "Section 210.19(A)(1)"
- "Table 310.16"

### Numbers and Units

#### Number Format

**Spell out one through nine**: Use numerals for 10 and above
- ✅ "three conductors", "15 circuits"
- **Exception**: Technical values always use numerals ("5 amperes", "2 volts")

**Use numerals for**:
- Technical measurements: "2.5 inches", "12 AWG", "240 volts"
- Percentages: "5%", "25% demand factor"
- Ranges: "10-20 amperes", "100-400 amp service"
- Code sections: "Article 220", "Section 210.19"

**Comma separator for thousands**:
- ✅ "1,000 VA", "250,000 square feet"
- ❌ "1000 VA", "250000 square feet"

#### Units and Measurements

**Always include units**: Never leave measurements ambiguous
- ✅ "100 amperes", "12 AWG", "240 volts"
- ❌ "100", "12", "240"

**Standard abbreviations**:
- Amperes: A (or amp when spelled out)
- Volts: V
- Watts: W
- Volt-Amperes: VA
- Kilowatts: kW
- Kilovolt-Amperes: kVA
- Feet: ft
- Inches: in
- Square feet: sq ft or ft²
- Temperature: °C, °F

**Space between number and unit**:
- ✅ "20 A", "240 V", "100 ft"
- ❌ "20A", "240V", "100ft"
- **Exception**: Degrees and percentages: "75°C", "25%"

**Use metric when specified**: Many codes reference both
- "10 AWG (5.26 mm²)"
- "100 ft (30.48 m)"

### Abbreviations and Acronyms

#### Define on First Use

**Pattern**: Full term (Acronym)
```
The National Electrical Code (NEC) establishes minimum safety standards.
The NEC is updated every three years.
```

**Exception**: Universally known acronyms may be used without definition
- HVAC, MEP, PE, OSHA, NFPA, IEEE, ASHRAE

#### Standard Abbreviations

**Electrical**:
- AWG: American Wire Gauge
- OCPD: Overcurrent Protective Device
- GFCI: Ground Fault Circuit Interrupter
- AFCI: Arc Fault Circuit Interrupter
- PV: Photovoltaic
- EVSE: Electric Vehicle Supply Equipment

**Mechanical**:
- CFM: Cubic Feet per Minute
- BTU: British Thermal Unit
- EER: Energy Efficiency Ratio
- SEER: Seasonal Energy Efficiency Ratio
- AHU: Air Handling Unit

**General**:
- NEC: National Electrical Code
- IBC: International Building Code
- IPC: International Plumbing Code
- IMC: International Mechanical Code
- NFPA: National Fire Protection Association
- ASHRAE: American Society of Heating, Refrigerating and Air-Conditioning Engineers

**Use glossary link for less common terms**:
```
The load diversity factor (see [Glossary: Load Diversity](../17_GLOSSARY_AND_TAXONOMY/glossary.md#load-diversity))
reduces the calculated load.
```

---

## Markdown Formatting Standards

### Heading Hierarchy

**Use hierarchical heading structure**: H1 → H2 → H3 → H4
- **H1 (`#`)**: Document title only (once per document)
- **H2 (`##`)**: Major sections
- **H3 (`###`)**: Subsections
- **H4 (`####`)**: Sub-subsections
- **Avoid H5/H6**: Restructure if you need more than 4 levels

**Example**:
```markdown
# Voltage Drop Calculator (H1 - Title)

## Purpose and Scope (H2 - Major Section)

### Calculation Method (H3 - Subsection)

#### Single-Phase Circuits (H4 - Sub-subsection)
```

**Skip no levels**: Don't jump from H2 to H4
- ✅ H2 → H3 → H4
- ❌ H2 → H4

### Emphasis and Formatting

**Bold**: Use for emphasis, important terms, labels
- `**This is bold**` → **This is bold**
- Use sparingly; overuse reduces impact

**Italic**: Use for subtle emphasis, variable names, first introduction of terms
- `*This is italic*` → *This is italic*
- "The *ampacity* of a conductor..."

**Code Formatting**: Use for code, commands, file names, technical values
- `` `inline code` `` → `inline code`
- "Use the `calculate_load()` function"
- "Edit the `.env` file"

**Strikethrough**: Use rarely, primarily for corrections in revision history
- `~~This is struck through~~` → ~~This is struck through~~

**Do not combine**: Avoid `***bold italic***` or other combinations

### Lists

#### Unordered Lists

**Use for**: Non-sequential items, options, features

**Format**:
```markdown
- First item
- Second item
- Third item
  - Nested item (2-space indent)
  - Another nested item
- Fourth item
```

**Rendered**:
- First item
- Second item
- Third item
  - Nested item
  - Another nested item
- Fourth item

#### Ordered Lists

**Use for**: Sequential steps, prioritized items, procedures

**Format**:
```markdown
1. First step
2. Second step
3. Third step
   1. Sub-step (3-space indent + number)
   2. Another sub-step
4. Fourth step
```

**Rendered**:
1. First step
2. Second step
3. Third step
   1. Sub-step
   2. Another sub-step
4. Fourth step

**Auto-numbering**: Use `1.` for all items; Markdown will auto-number
```markdown
1. First
1. Second (will display as "2.")
1. Third (will display as "3.")
```

#### Checklist Format

**Use for**: Tasks, requirements, validation items

**Format**:
```markdown
- [ ] Unchecked item
- [x] Checked item
- [ ] Another unchecked item
```

**Rendered**:
- [ ] Unchecked item
- [x] Checked item
- [ ] Another unchecked item

### Links and References

#### Internal Links (Cross-References)

**Format**: `[Link Text](relative/path/to/file.md#heading-anchor)`

**Examples**:
```markdown
See [Versioning Conventions](00_Versioning_and_Naming_Conventions.md)

Refer to [NEC Table Reference](../../01_CODES_AND_STANDARDS/NEC/tables.md#table-310-16)

Consult the [Glossary entry for Ampacity](../17_GLOSSARY_AND_TAXONOMY/glossary.md#ampacity)
```

**Best Practices**:
- Use relative paths (not absolute)
- Include heading anchors for specific sections
- Test links before publishing
- Use descriptive link text (not "click here")

#### External Links

**Format**: `[Link Text](https://full-url.com)`

**Examples**:
```markdown
[NFPA Website](https://www.nfpa.org/)

[NEC 2023 Free Access](https://www.nfpa.org/70)

[IEEE Standards](https://standards.ieee.org/)
```

**Best Practices**:
- Use HTTPS when available
- Link to stable, authoritative sources
- Avoid linking to paywalled content without noting
- Include access date for time-sensitive information: `(accessed 2025-10-22)`

#### Citations and References

**Inline Citation Format**:
```markdown
According to NEC 210.19(A)(1) [1], conductor ampacity must meet the maximum load.
```

**Reference Section Format**:
```markdown
## References

1. National Fire Protection Association. *NFPA 70, National Electrical Code*.
   2023 Edition. NFPA, Quincy, MA, 2022.

2. Institute of Electrical and Electronics Engineers. *IEEE Std 242-2001,
   IEEE Recommended Practice for Protection and Coordination*. IEEE, New York, NY, 2001.
```

### Block Quotes

**Use for**: Direct quotations, callouts, important notes

**Format**:
```markdown
> This is a block quote.
> It can span multiple lines.
>
> And multiple paragraphs.
```

**Rendered**:
> This is a block quote.
> It can span multiple lines.
>
> And multiple paragraphs.

**With Attribution**:
```markdown
> Conductor ampacity must not be less than the maximum load to be served.
>
> — NEC 210.19(A)(1), 2023 Edition
```

### Horizontal Rules

**Use for**: Separating major sections, visual breaks

**Format**: Three or more hyphens, asterisks, or underscores
```markdown
---
```

**Rendered**:

---

**Usage Guidelines**:
- Use sparingly (rely on headings for structure)
- Place blank lines before and after
- Prefer `---` for consistency

---

## Code and Example Formatting

### Inline Code

**Use for**: Function names, variable names, commands, file names, technical terms

**Format**: `` `code` ``

**Examples**:
```markdown
Call the `calculate_voltage_drop()` function.
Edit the `config.json` file.
The `ampacity` variable stores conductor ratings.
Run `npm install` to install dependencies.
```

### Code Blocks

**Use for**: Multi-line code, scripts, configuration files

**Format**: Triple backticks with language identifier
````markdown
```python
def calculate_voltage_drop(current, distance, resistance):
    """Calculate voltage drop using Ohm's Law."""
    voltage_drop = 2 * current * distance * resistance
    return voltage_drop
```
````

**Supported Languages**:
- `python`: Python code
- `javascript`: JavaScript code
- `json`: JSON data
- `yaml`: YAML configuration
- `bash`: Shell commands
- `sql`: SQL queries
- `markdown`: Markdown examples
- Leave blank for plain text

**Best Practices**:
- Include language identifier for syntax highlighting
- Add comments explaining non-obvious code
- Keep examples concise (< 30 lines typical)
- Use realistic examples from engineering practice

### Calculation Examples

**Format**: Use code blocks with clear structure

**Example**:
````markdown
```
Voltage Drop Calculation - Example 1

Given:
- Load: 20 A
- Voltage: 240 V
- Distance: 150 ft
- Conductor: 12 AWG copper
- Resistance: 1.98 Ω per 1000 ft (from NEC Table 9)

Calculation:
VD = 2 × I × L × R / 1000
VD = 2 × 20 A × 150 ft × 1.98 Ω/1000ft / 1000
VD = 11.88 V

Voltage Drop Percentage:
VD% = (VD / V) × 100%
VD% = (11.88 V / 240 V) × 100%
VD% = 4.95%

Result: 4.95% voltage drop (exceeds NEC 3% recommendation)
Recommendation: Increase conductor size to 10 AWG
```
````

**Structure**:
1. **Given**: List all input values with units
2. **Calculation**: Show step-by-step work
3. **Result**: State final answer with interpretation
4. **Recommendation**: Provide actionable guidance (if applicable)

### Command-Line Examples

**Format**: Use `bash` code blocks

**Example**:
````markdown
```bash
# Install dependencies
npm install

# Run voltage drop calculator
python voltage_drop.py --current 20 --distance 150 --conductor "12 AWG"

# View help
python voltage_drop.py --help
```
````

**Best Practices**:
- Include comments explaining each command
- Show expected output when relevant
- Use realistic examples
- Indicate optional vs. required parameters

---

## Diagrams and Visual Content

### When to Use Diagrams

**Use diagrams to**:
- Illustrate complex relationships or systems
- Show physical layouts or connections
- Visualize decision trees or workflows
- Simplify understanding of abstract concepts

**Don't use diagrams when**:
- Text is clearer and simpler
- Diagram would be overly complex
- Information changes frequently (maintenance burden)

### Diagram Types

#### Electrical Diagrams

**Single-Line Diagrams**:
- Show power distribution from source to loads
- Use standard electrical symbols
- Label all components with ratings

**Wiring Diagrams**:
- Show physical connections between components
- Include conductor sizes and types
- Label all terminals and connections

**Riser Diagrams**:
- Show vertical distribution (multi-floor buildings)
- Indicate panel locations and feeder sizes
- Label each floor/level

#### Flowcharts

**Use for**: Processes, decision trees, workflows

**Best Practices**:
- Use standard flowchart symbols (rectangle = process, diamond = decision)
- Flow top-to-bottom or left-to-right
- Label all decision branches (Yes/No, True/False)
- Keep simple (< 15 boxes typical)

#### Block Diagrams

**Use for**: System architecture, component relationships

**Best Practices**:
- Group related components
- Show data flow or connections
- Use consistent shapes and colors
- Label all components clearly

### Image Formats

**Preferred Formats**:
- **SVG**: Vector graphics, scales perfectly (diagrams, charts)
- **PNG**: Raster graphics with transparency (screenshots, photos)
- **JPG**: Photographs or complex images (use sparingly)

**Avoid**:
- **GIF**: Limited color palette, large file sizes
- **BMP**: Uncompressed, very large files

### Image Inclusion

**Format**:
```markdown
![Alt Text Description](path/to/image.png)

**Figure 1**: Caption describing the image content.
```

**Example**:
```markdown
![Single-line diagram showing service entrance, main panel, and branch circuits](images/single_line_example.svg)

**Figure 1**: Typical residential single-line diagram with 200A service and main panel
feeding lighting, receptacle, and appliance branch circuits.
```

**Best Practices**:
- **Alt text**: Describe image content for accessibility
- **Caption**: Provide context and explanation
- **Figure numbers**: Sequential numbering within document
- **File naming**: Descriptive, lowercase, underscores (e.g., `single_line_diagram_residential.svg`)
- **Image size**: Optimize for web (< 500 KB per image)
- **Placement**: Place images near referencing text

### Diagram Creation Tools

**Recommended Tools**:
- **draw.io** (diagrams.net): Free, web-based, exports SVG
- **Lucidchart**: Professional diagrams, electrical symbols library
- **Microsoft Visio**: Industry standard (requires license)
- **AutoCAD Electrical**: For professional electrical diagrams
- **PlantUML**: Text-based diagram generation (code-friendly)

---

## Tables and Data Presentation

### When to Use Tables

**Use tables for**:
- Comparing multiple items across several attributes
- Presenting structured data (reference tables, specifications)
- Showing calculation results with multiple variables

**Don't use tables when**:
- A simple list would suffice
- Table has only 1-2 columns (use list instead)
- Data is too complex (split into multiple tables)

### Table Formatting

**Basic Format**:
```markdown
| Column 1 Header | Column 2 Header | Column 3 Header |
|-----------------|-----------------|-----------------|
| Row 1, Cell 1   | Row 1, Cell 2   | Row 1, Cell 3   |
| Row 2, Cell 1   | Row 2, Cell 2   | Row 2, Cell 3   |
```

**Rendered**:
| Column 1 Header | Column 2 Header | Column 3 Header |
|-----------------|-----------------|-----------------|
| Row 1, Cell 1   | Row 1, Cell 2   | Row 1, Cell 3   |
| Row 2, Cell 1   | Row 2, Cell 2   | Row 2, Cell 3   |

**Alignment**:
```markdown
| Left Aligned | Center Aligned | Right Aligned |
|:-------------|:--------------:|--------------:|
| Text         | Text           | Text          |
```

**Rendered**:
| Left Aligned | Center Aligned | Right Aligned |
|:-------------|:--------------:|--------------:|
| Text         | Text           | Text          |

### Table Best Practices

**Headers**:
- Always include header row
- Use descriptive, concise headers
- Include units in headers (e.g., "Current (A)")

**Content**:
- Keep cell content concise (< 10 words typical)
- Use consistent formatting within columns
- Align numbers right, text left
- Use abbreviations consistently

**Size**:
- Limit to 8-10 columns (readability)
- If more columns needed, split into multiple tables or use different format
- No hard limit on rows, but consider pagination for very long tables

**Caption**:
```markdown
**Table 1**: Conductor ampacity for copper conductors with 75°C insulation

| Conductor Size | Ampacity (A) | Typical Use          |
|----------------|--------------|----------------------|
| 14 AWG         | 20           | Lighting circuits    |
| 12 AWG         | 25           | Receptacle circuits  |
| 10 AWG         | 35           | Small appliances     |
```

### Data Tables from NEC

**Paraphrase, don't copy verbatim**:

**❌ Prohibited**:
```markdown
<!-- Copying NEC table directly is copyright infringement -->
```

**✅ Permitted**:
```markdown
**Table 1**: Conductor ampacity reference (derived from NEC Table 310.16)

This table provides simplified ampacity values for common copper conductors with
75°C insulation in ambient temperatures up to 30°C. For complete ampacity tables
including all conditions, consult NEC Table 310.16.

| Conductor Size | Ampacity (75°C) |
|----------------|-----------------|
| 14 AWG         | 20 A            |
| 12 AWG         | 25 A            |
| 10 AWG         | 35 A            |

**Source**: Values derived from NFPA 70-2023, Table 310.16
```

---

## Terminology and Consistency

### Use the Glossary

**Link to glossary terms on first use** or when clarification needed:

```markdown
The [load diversity factor](../17_GLOSSARY_AND_TAXONOMY/glossary.md#load-diversity)
accounts for the fact that not all loads operate simultaneously.
```

### Standard Terminology

**Electrical Engineering**:
- **Ampacity** (not "ampere capacity" or "current rating")
- **Conductor** (not "wire" in formal writing)
- **Overcurrent Protective Device (OCPD)** (not "breaker" generically)
- **Ground Fault Circuit Interrupter (GFCI)** (not "GFI")
- **Service** (not "service entrance equipment" unless specific)
- **Feeder** vs. **Branch Circuit** (distinct terms, use correctly)

**Mechanical Engineering**:
- **Air Handling Unit (AHU)** (not "air handler")
- **Cubic Feet per Minute (CFM)** (not "airflow" without units)
- **British Thermal Unit (BTU)** (not "BTUs")
- **Coefficient of Performance (COP)** (not "efficiency" generically)

**General**:
- **Calculation** (not "calc" in formal writing)
- **Specification** (not "spec" unless space-constrained)
- **Drawing** (not "dwg" unless referring to file extension)

### Consistent Terminology Across Documents

**Create and use a project-specific term list**:

| Term | Use | Don't Use |
|------|-----|-----------|
| Ampacity | ✅ | Current capacity, ampere rating |
| Conductor | ✅ | Wire (in formal docs) |
| OCPD | ✅ | Breaker, fuse (unless specific) |
| Load diversity | ✅ | Demand diversity, load factor diversity |

**Check existing documents**: Use terminology consistent with knowledge base

---

## Document Structure Templates

### Standard Document Structure

```markdown
# Document Title

**Document ID**: {Discipline}-{Type}-{Number}
**Version**: {MAJOR.MINOR.PATCH}
**Last Updated**: {YYYY-MM-DD}
**Author**: {Author Name}
**Status**: {DRAFT | REVIEW | APPROVED}

## Table of Contents

1. [Purpose and Scope](#purpose-and-scope)
2. [Main Section 1](#main-section-1)
3. [Main Section 2](#main-section-2)
4. [References](#references)
5. [Appendices](#appendices)

---

## Purpose and Scope

### Purpose
[Why this document exists, what problem it solves]

### Scope
**In Scope**: [What is covered]
**Out of Scope**: [What is not covered]

---

## Main Sections

[Content organized logically with H2/H3/H4 headings]

---

## References

1. [Citation 1]
2. [Citation 2]

---

## Appendices

### Appendix A: [Title]

[Supplementary content]

---

**End of Document**
```

### Calculation Document Structure

```markdown
# [Calculation Title]

**Document ID**: {E/M/P}-CALC-{Number}
**Version**: {Version}
**Last Updated**: {Date}
**Author**: {Name}
**NEC Version**: {2020/2023/2026}

## Purpose

[What this calculation determines]

## Applicable Codes and Standards

- NEC Article {XXX}
- ASHRAE Standard {XXX} (if applicable)
- [Other standards]

## Input Parameters

| Parameter | Symbol | Unit | Typical Range |
|-----------|--------|------|---------------|
| [Param 1] | I      | A    | 10-100        |

## Calculation Method

### Step 1: [Description]

**Formula**:
```
[Formula in mathematical notation]
```

**Where**:
- `I` = Current (A)
- [Other variables]

**Example**:
```
[Worked example with realistic values]
```

### Step 2: [Continue...]

## Results Interpretation

[How to interpret calculated results]

## Limitations and Assumptions

- [Assumption 1]
- [Assumption 2]

## References

[Citations to NEC, standards, etc.]
```

### Guide Document Structure

```markdown
# [Guide Title]

**Document ID**: {Discipline}-GUIDE-{Number}
**Version**: {Version}
**Complexity Level**: {Fundamental | Intermediate | Advanced | Expert}

## Introduction

[Brief overview of what this guide covers]

## Prerequisites

[What the reader should know before using this guide]

## Section 1: [Topic]

[Content with examples]

## Section 2: [Next Topic]

[Content]

## Common Mistakes to Avoid

- [Mistake 1]
- [Mistake 2]

## Best Practices

1. [Practice 1]
2. [Practice 2]

## Additional Resources

- [Link to related documents]
- [External resources]

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0   | 2025-10-22 | Initial release |
```

---

## Review Checklist

Before submitting content, verify:

### Writing Style
- [ ] Active voice used where appropriate
- [ ] Clear, concise sentences (15-25 words average)
- [ ] One idea per paragraph
- [ ] Professional tone maintained
- [ ] Technical accuracy verified

### Formatting
- [ ] Heading hierarchy correct (no skipped levels)
- [ ] Lists properly formatted (bullets/numbers/checklists)
- [ ] Code blocks use language identifiers
- [ ] Tables have headers and are properly formatted
- [ ] Images have alt text and captions

### Terminology
- [ ] Terms defined on first use or linked to glossary
- [ ] Standard terminology used consistently
- [ ] Abbreviations expanded on first use
- [ ] Units included with all measurements

### Citations
- [ ] All sources cited properly
- [ ] No verbatim code reproduction
- [ ] Fair use principles followed
- [ ] References section complete

### Structure
- [ ] Metadata block present and complete
- [ ] Table of contents included (if >3 sections)
- [ ] Logical organization and flow
- [ ] Appropriate use of headings and sections

### Links and References
- [ ] All internal links functional
- [ ] External links to authoritative sources
- [ ] Cross-references accurate
- [ ] No broken links

### Technical Content
- [ ] Calculations verified
- [ ] Code references accurate (NEC articles/sections)
- [ ] Examples realistic and applicable
- [ ] Assumptions and limitations stated

### Legal Compliance
- [ ] Copyright compliance verified
- [ ] Attribution complete
- [ ] Licensing terms specified
- [ ] No plagiarism

---

## Common Mistakes to Avoid

### Writing Mistakes

**Passive Voice Overuse**:
- ❌ "The conductor shall be sized by the engineer using the NEC"
- ✅ "Size the conductor using NEC requirements"

**Unnecessary Complexity**:
- ❌ "It is necessary to perform a comprehensive evaluation of the electrical load"
- ✅ "Calculate the electrical load"

**Vague Language**:
- ❌ "Use an appropriate conductor size"
- ✅ "Use 12 AWG copper conductor for 20A circuits"

**Missing Units**:
- ❌ "The load is 150"
- ✅ "The load is 150 amperes"

### Formatting Mistakes

**Inconsistent Heading Levels**:
```markdown
❌ Bad:
# Title
### Skipping H2
#### Sub-section

✅ Good:
# Title
## Section
### Subsection
```

**Unformatted Code**:
```markdown
❌ Bad:
Call the calculate_load() function

✅ Good:
Call the `calculate_load()` function
```

**Missing Table Headers**:
```markdown
❌ Bad:
| 14 AWG | 20 A |
| 12 AWG | 25 A |

✅ Good:
| Conductor | Ampacity |
|-----------|----------|
| 14 AWG    | 20 A     |
| 12 AWG    | 25 A     |
```

### Technical Mistakes

**Incorrect Code Citations**:
- ❌ "According to the NEC..."
- ✅ "According to NEC 210.19(A)(1)..."

**Unsupported Claims**:
- ❌ "This is the best method for sizing conductors"
- ✅ "This method follows NEC Article 220 standard calculation procedure"

**Missing Assumptions**:
- ❌ Show calculation without stating assumptions
- ✅ State all assumptions (temperature, insulation type, etc.)

### Legal Mistakes

**Verbatim Code Reproduction**:
- ❌ Copy entire NEC article text
- ✅ Paraphrase requirements and cite section number

**Missing Attribution**:
- ❌ Include data without citing source
- ✅ "Source: NEC Table 310.16"

**No License Specified**:
- ❌ Publish without license information
- ✅ Include license in metadata

---

## Appendix: Quick Reference

### Markdown Cheat Sheet

| Element | Syntax |
|---------|--------|
| Heading 1 | `# H1` |
| Heading 2 | `## H2` |
| Heading 3 | `### H3` |
| Bold | `**bold**` |
| Italic | `*italic*` |
| Inline Code | `` `code` `` |
| Code Block | ` ```language ` |
| Link | `[text](url)` |
| Image | `![alt](url)` |
| Unordered List | `- item` |
| Ordered List | `1. item` |
| Checklist | `- [ ] item` |
| Table | `\| col1 \| col2 \|` |
| Blockquote | `> quote` |
| Horizontal Rule | `---` |

### Common Technical Abbreviations

| Abbreviation | Meaning |
|--------------|---------|
| A | Amperes |
| V | Volts |
| W | Watts |
| VA | Volt-Amperes |
| kW | Kilowatts |
| kVA | Kilovolt-Amperes |
| AWG | American Wire Gauge |
| OCPD | Overcurrent Protective Device |
| GFCI | Ground Fault Circuit Interrupter |
| AFCI | Arc Fault Circuit Interrupter |
| NEC | National Electrical Code |
| IBC | International Building Code |
| ASHRAE | American Society of Heating, Refrigerating and Air-Conditioning Engineers |

---

**End of Document**

**Approval Signatures**:
- Technical Writing Lead: _____________________ Date: __________
- Knowledge Manager: _________________________ Date: __________
- QA Reviewer: _______________________________ Date: __________
