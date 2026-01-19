# Knowledge Management Standard Operating Procedure

**Document ID**: ADMIN-GOV-01
**Version**: 1.0.0
**Last Updated**: 2025-10-22
**Author**: MEP Knowledge Management Team
**Status**: Approved

## Table of Contents

1. [Purpose and Scope](#purpose-and-scope)
2. [Roles and Responsibilities](#roles-and-responsibilities)
3. [Content Addition Workflow](#content-addition-workflow)
4. [Review and Approval Process](#review-and-approval-process)
5. [Update and Maintenance Procedures](#update-and-maintenance-procedures)
6. [Retirement and Archival](#retirement-and-archival)
7. [Quality Gates and Validation](#quality-gates-and-validation)
8. [Content Classification Taxonomy](#content-classification-taxonomy)
9. [Tools and Systems](#tools-and-systems)
10. [Metrics and Performance](#metrics-and-performance)

---

## Purpose and Scope

### Purpose

This Standard Operating Procedure (SOP) establishes the mandatory processes for managing content within the MEP Engineering Knowledge Base. It ensures:

- **Quality**: All content meets technical accuracy and professional standards
- **Consistency**: Uniform structure, formatting, and metadata across documents
- **Traceability**: Complete audit trails for content lifecycle management
- **Accessibility**: Content is discoverable, retrievable, and usable
- **Compliance**: Adherence to licensing, copyright, and regulatory requirements

### Scope

This SOP applies to:

- All documents, datasets, code, and media in the knowledge base
- All contributors, reviewers, approvers, and administrators
- Content creation, modification, review, approval, publication, and retirement
- Both internal and external content sources

**Out of Scope**:
- Project-specific documents not intended for knowledge base
- Personal notes or drafts not submitted for inclusion
- External links to third-party resources (governed separately)

---

## Roles and Responsibilities

### Role Definitions

#### 1. Content Creator (Contributor)

**Description**: Creates or submits new content for knowledge base inclusion

**Responsibilities**:
- Draft content following style guide and formatting standards
- Conduct self-review using quality checklist
- Provide complete metadata and documentation
- Respond to reviewer feedback within defined timeframes
- Maintain versioning and change logs

**Qualifications**:
- Subject matter expertise in relevant discipline
- Familiarity with MEP engineering standards and codes
- Training on knowledge management tools and procedures

**Access Level**: Contributor (read/write to assigned content)

#### 2. Technical Reviewer

**Description**: Evaluates content for technical accuracy and completeness

**Responsibilities**:
- Review content for technical correctness and NEC/code compliance
- Verify calculations, formulas, and referenced data
- Assess clarity, completeness, and usability
- Provide constructive feedback within 5 business days
- Recommend approval, revision, or rejection

**Qualifications**:
- Professional Engineer (PE) or 10+ years MEP experience
- Deep expertise in discipline being reviewed
- Knowledge of relevant codes and standards

**Access Level**: Reviewer (read all, comment on assigned content)

#### 3. QA Reviewer

**Description**: Ensures content meets quality standards and governance requirements

**Responsibilities**:
- Verify compliance with versioning and naming conventions
- Check metadata completeness and accuracy
- Validate formatting, structure, and style guide adherence
- Confirm licensing and copyright compliance
- Approve or reject content for publication

**Qualifications**:
- Training in quality management systems (QMS)
- Familiarity with documentation standards
- Understanding of copyright and intellectual property law

**Access Level**: Reviewer (read all, comment on assigned content)

#### 4. Knowledge Manager

**Description**: Oversees knowledge base operations and governance

**Responsibilities**:
- Assign document IDs and serial numbers
- Coordinate review workflows and track progress
- Resolve conflicts and escalations
- Maintain content taxonomy and classification scheme
- Generate metrics and performance reports
- Conduct periodic audits and quality checks

**Qualifications**:
- Experience in knowledge management or information architecture
- Project management skills
- Technical writing and editorial expertise

**Access Level**: Administrator (full access, except deletion)

#### 5. System Administrator

**Description**: Manages technical infrastructure and access controls

**Responsibilities**:
- Maintain version control systems and repositories
- Configure access permissions and RBAC policies
- Implement backup and disaster recovery procedures
- Troubleshoot technical issues
- Ensure system security and data integrity

**Qualifications**:
- IT systems administration experience
- Familiarity with Git, Markdown, and documentation tools
- Information security awareness

**Access Level**: Administrator (full system access)

### Responsibilities Matrix (RACI)

| Activity                          | Creator | Tech Rev | QA Rev | KM   | Sys Admin |
|-----------------------------------|---------|----------|--------|------|-----------|
| Draft content                     | R       | C        | I      | I    | -         |
| Self-review and quality check     | R/A     | -        | I      | I    | -         |
| Submit for review                 | R       | I        | I      | A    | -         |
| Technical review                  | C       | R/A      | I      | I    | -         |
| QA review                         | C       | I        | R/A    | I    | -         |
| Approve for publication           | I       | C        | C      | R/A  | -         |
| Publish to knowledge base         | I       | I        | I      | R    | A         |
| Update existing content           | R       | C        | C      | A    | -         |
| Retire/archive content            | C       | C        | C      | R/A  | -         |
| Assign document IDs               | I       | -        | -      | R/A  | -         |
| Manage access permissions         | -       | -        | -      | C    | R/A       |
| System maintenance                | -       | -        | -      | I    | R/A       |

**Legend**: R = Responsible, A = Accountable, C = Consulted, I = Informed

---

## Content Addition Workflow

### Overview

The standard workflow for adding new content consists of 7 phases:

```
1. INITIATE → 2. DRAFT → 3. SELF-REVIEW → 4. SUBMIT → 5. REVIEW → 6. APPROVE → 7. PUBLISH
```

### Phase 1: INITIATE

**Objective**: Determine need and scope for new content

**Steps**:
1. Identify content gap or improvement opportunity
2. Check for existing similar content (avoid duplication)
3. Submit Content Proposal Form to Knowledge Manager
4. Receive document ID assignment and approval to proceed

**Duration**: 1-3 business days

**Outputs**:
- Approved Content Proposal Form
- Assigned Document ID (e.g., E-CALC-042)
- Designated Technical Reviewer

**Decision Point**: Knowledge Manager approves or rejects proposal

### Phase 2: DRAFT

**Objective**: Create initial content following standards

**Steps**:
1. Use appropriate template from knowledge base
2. Follow naming conventions and versioning standards
3. Include all required metadata fields
4. Cite sources and provide references
5. Create examples, diagrams, or calculations as needed
6. Start with version `v0.1.0` or suffix filename with `_DRAFT`

**Duration**: Varies by content complexity (1-20 business days typical)

**Outputs**:
- Draft document with complete structure
- Initial metadata and version control
- Supporting materials (if applicable)

**Best Practices**:
- Work in feature branch (Git: `feature/{DocID}-{description}`)
- Commit frequently with descriptive messages
- Save drafts in designated workspace (not main repository)

### Phase 3: SELF-REVIEW

**Objective**: Creator validates content before submission

**Steps**:
1. Complete Self-Review Checklist (see Quality Gates section)
2. Run automated validation tools (linters, spell check)
3. Verify calculations independently or with calculator tools
4. Proofread for grammar, clarity, and formatting
5. Confirm all citations and references are accurate
6. Update metadata and revision history

**Duration**: 0.5-2 business days

**Outputs**:
- Completed Self-Review Checklist
- Corrections and improvements incorporated
- Document ready for formal review

**Quality Gate**: All checklist items must pass before proceeding

### Phase 4: SUBMIT

**Objective**: Formally submit content for review

**Steps**:
1. Update document status to `REVIEW` and version to `v0.9.0`
2. Submit via knowledge management system (create pull request or review ticket)
3. Notify assigned Technical Reviewer and QA Reviewer
4. Provide context and highlight any areas needing special attention
5. Attach Self-Review Checklist and supporting materials

**Duration**: <1 business day

**Outputs**:
- Review request ticket/pull request
- Email notifications to reviewers
- Document status changed to `REVIEW`

**SLA**: Reviewers must acknowledge receipt within 1 business day

### Phase 5: REVIEW

**Objective**: Technical and QA reviewers evaluate content

**Steps**:

#### Technical Review:
1. Evaluate technical accuracy and code compliance
2. Verify calculations, formulas, and methodologies
3. Assess completeness and clarity
4. Provide inline comments and feedback
5. Recommend: Approve, Request Revisions, or Reject

#### QA Review (parallel to Technical Review):
1. Check versioning and naming convention compliance
2. Verify metadata completeness and format
3. Validate style guide adherence
4. Confirm licensing and copyright compliance
5. Recommend: Approve, Request Revisions, or Reject

**Duration**: 5 business days (standard) | 10 business days (complex)

**Outputs**:
- Technical Review Report
- QA Review Report
- Inline comments and suggested changes
- Recommendation (approve/revise/reject)

**Decision Points**:
- **Approve**: Both reviewers approve → Proceed to Phase 6
- **Revise**: Revisions needed → Return to Creator (iterate Phase 2-5)
- **Reject**: Fundamental issues → Return to Phase 1 or cancel

**SLA**: Reviewers complete review within 5 business days; Creator responds to feedback within 3 business days

### Phase 6: APPROVE

**Objective**: Knowledge Manager grants final approval for publication

**Steps**:
1. Knowledge Manager reviews Technical and QA recommendations
2. Verify all reviewer comments addressed
3. Confirm final version meets all quality gates
4. Update document status to `APPROVED`
5. Update version to `v1.0.0` (for new content) or increment appropriately
6. Sign off on approval (digital signature or approval record)

**Duration**: 1-2 business days

**Outputs**:
- Final approval record
- Document status changed to `APPROVED`
- Version incremented to release version

**Decision Point**: Knowledge Manager approves or requests additional changes

### Phase 7: PUBLISH

**Objective**: Make content available in knowledge base

**Steps**:
1. System Administrator or Knowledge Manager merges content to main repository
2. Tag release with version number (Git: `v1.0.0`)
3. Generate final PDF or compiled versions (if applicable)
4. Update knowledge base index and search catalog
5. Notify stakeholders and announce new content (if significant)
6. Archive draft and review artifacts

**Duration**: <1 business day

**Outputs**:
- Content published in main repository
- Version tag created
- Knowledge base updated
- Notification sent to relevant users

**Validation**: Verify content is accessible and displays correctly

---

## Review and Approval Process

### Review Criteria

#### Technical Review Criteria

Technical reviewers evaluate content against these criteria:

1. **Technical Accuracy** (Critical)
   - Calculations are correct and verifiable
   - Methods align with current NEC and industry standards
   - Data and tables are accurate and properly sourced
   - Engineering principles are correctly applied

2. **Code Compliance** (Critical)
   - NEC articles and sections correctly cited
   - Code requirements accurately interpreted
   - Exceptions and special conditions noted
   - Applicable code editions clearly identified

3. **Completeness** (Major)
   - All necessary information provided
   - Assumptions and limitations stated
   - Scope clearly defined
   - Examples cover typical use cases

4. **Clarity and Usability** (Major)
   - Content is understandable to target audience
   - Logical flow and organization
   - Adequate explanations and context
   - Graphics and diagrams enhance understanding

5. **References and Citations** (Minor)
   - All sources properly cited
   - Citations follow established format
   - External references are accessible
   - No copyright violations

#### QA Review Criteria

QA reviewers evaluate content against these criteria:

1. **Governance Compliance** (Critical)
   - Naming conventions followed
   - Versioning scheme correct
   - Metadata complete and accurate
   - Document ID properly assigned

2. **Style and Formatting** (Major)
   - Style guide standards followed
   - Markdown formatting consistent
   - Tables and lists properly formatted
   - Code blocks and examples correctly styled

3. **Legal Compliance** (Critical)
   - Copyright and licensing requirements met
   - No verbatim code reproduction
   - Attribution and fair use followed
   - Intellectual property rights respected

4. **Accessibility** (Minor)
   - Content is searchable and discoverable
   - Links and cross-references functional
   - Alternative text for images (if applicable)
   - Structure supports assistive technologies

### Feedback and Iteration

#### Providing Feedback

**Best Practices for Reviewers**:
- Be specific: Identify exact location and issue
- Be constructive: Suggest improvements, not just criticize
- Prioritize: Distinguish critical issues from minor suggestions
- Be timely: Complete reviews within SLA timeframes
- Be respectful: Maintain professional and collegial tone

**Feedback Format**:
```
[CRITICAL/MAJOR/MINOR] [Section/Line Number]
Issue: [Description of the problem]
Recommendation: [Suggested correction or improvement]
Rationale: [Why this matters or reference to standard]
```

**Example**:
```
[CRITICAL] Section 3.2, Equation (5)
Issue: Voltage drop calculation uses incorrect resistance value for aluminum conductors
Recommendation: Replace R = 0.0985 Ω with R = 0.0154 Ω per NEC Chapter 9 Table 9
Rationale: Current value is for copper; calculation specifies aluminum conductors
```

#### Responding to Feedback

**Best Practices for Creators**:
- Acknowledge all feedback
- Address critical and major issues first
- Provide rationale if disagreeing with feedback
- Document all changes in revision history
- Re-submit for review if substantial changes made

**Response Format**:
```
[Reviewer Name] - [Issue ID]
Response: [Explanation of how addressed or reason for not addressing]
Action Taken: [Description of change made]
Location: [Updated section/line number]
Status: [RESOLVED/DEFERRED/WONT-FIX]
```

**Example**:
```
[John Smith] - Issue #1
Response: Agreed, corrected resistance value for aluminum conductors
Action Taken: Updated Equation (5) and recalculated example
Location: Section 3.2, Line 145
Status: RESOLVED
```

### Escalation Process

If conflicts or issues arise during review:

**Level 1**: Creator and Reviewer discuss directly (most issues resolved here)
**Level 2**: Knowledge Manager mediates and facilitates resolution
**Level 3**: Technical Lead or Subject Matter Expert provides binding decision
**Level 4**: Review Board (for major disputes or policy questions)

**Escalation Triggers**:
- Unresolved technical disagreement after 2 iterations
- Suspected plagiarism or copyright violation
- Content involves sensitive or controversial topics
- Request for exception to governance standards

---

## Update and Maintenance Procedures

### Types of Updates

#### 1. Error Corrections (Patch Updates)

**Triggers**:
- Errors discovered in published content
- Broken links or references
- Typos or formatting issues

**Process**:
1. Create issue ticket describing error
2. Assign to original creator or qualified contributor
3. Make corrections (increment PATCH version)
4. Technical review required if error affects technical content
5. QA review for metadata/formatting changes only
6. Publish updated version

**Timeline**: 3-5 business days

**Example**: `v1.2.0` → `v1.2.1` (fixed typo in formula)

#### 2. Content Enhancements (Minor Updates)

**Triggers**:
- Adding new sections or examples
- Expanding explanations or coverage
- Updating for minor code changes
- User feedback requesting clarification

**Process**:
1. Submit Content Update Proposal
2. Receive approval from Knowledge Manager
3. Draft updates (increment MINOR version)
4. Full technical and QA review required
5. Publish updated version

**Timeline**: 10-15 business days

**Example**: `v1.2.1` → `v1.3.0` (added section on load diversity factors)

#### 3. Major Revisions (Major Updates)

**Triggers**:
- New code edition adopted (NEC 2023 → NEC 2026)
- Methodology changes or new standards
- Breaking changes that invalidate previous versions
- Complete restructuring or rewrite

**Process**:
1. Submit Major Revision Proposal (requires justification)
2. Approval from Technical Lead and Knowledge Manager
3. Draft updates (increment MAJOR version)
4. Full technical and QA review required
5. Extended review period (10 business days)
6. Announce to all users before publication
7. Previous version marked SUPERSEDED

**Timeline**: 20-30 business days

**Example**: `v1.3.0` → `v2.0.0` (updated for NEC 2026)

### Scheduled Maintenance Reviews

**Annual Review**: All documents reviewed annually for currency and accuracy
- Assigned to original creator or subject matter expert
- Confirm content still accurate and relevant
- Update references and citations
- Increment version if changes made

**Code Update Cycle**: Systematic review when new code editions published
- Prioritize documents heavily dependent on specific code articles
- Update calculations, tables, and references
- Major version increment required

**Compliance Audit**: Quarterly audit of random sample (10% of documents)
- Knowledge Manager conducts compliance checks
- Verify governance standards followed
- Identify and correct systemic issues

---

## Retirement and Archival

### Retirement Criteria

Content may be retired if:
- **Superseded**: Replaced by newer version
- **Obsolete**: No longer applicable due to code or technology changes
- **Duplicate**: Redundant with other content
- **Low Quality**: Does not meet current standards and not worth updating
- **Out of Scope**: No longer relevant to knowledge base mission

### Retirement Process

**Steps**:
1. Identify content for retirement (user feedback, audit findings, scheduled review)
2. Submit Retirement Proposal to Knowledge Manager
3. Knowledge Manager evaluates and approves/rejects
4. Update document status to `SUPERSEDED` or `OBSOLETE`
5. Add prominent notice to document header
6. Move to archive repository (retain for audit trail)
7. Remove from active search index (but keep accessible via direct link)
8. Update any documents that reference retired content
9. Log retirement in Content Lifecycle Register

**Timeline**: 5 business days

**Retention Period**:
- **SUPERSEDED**: Retain for 5 years or 2 code cycles (whichever longer)
- **OBSOLETE**: Retain for 10 years (regulatory compliance)

### Archival Storage

**Archive Repository Structure**:
```
archive/
├── by_year/
│   ├── 2023/
│   ├── 2024/
│   └── 2025/
├── by_discipline/
│   ├── electrical/
│   ├── mechanical/
│   └── plumbing/
└── by_reason/
    ├── superseded/
    ├── obsolete/
    └── out_of_scope/
```

**Metadata for Archived Content**:
- Retirement date and reason
- Superseding document ID (if applicable)
- Last approved version
- Historical usage statistics
- Retention expiration date

---

## Quality Gates and Validation

### Self-Review Checklist

Content creators must complete this checklist before submission:

#### Technical Quality
- [ ] All calculations verified and correct
- [ ] Code references accurate (NEC article, section, table)
- [ ] Methodology aligns with industry standards
- [ ] Assumptions and limitations clearly stated
- [ ] Examples are realistic and demonstrate typical use cases
- [ ] Units and conversions correct
- [ ] Formulas and equations properly formatted

#### Content Quality
- [ ] Title is descriptive and accurate
- [ ] Content is complete and addresses intended scope
- [ ] Logical flow and organization
- [ ] Clear and concise writing (active voice preferred)
- [ ] Technical terms defined or linked to glossary
- [ ] Graphics and diagrams enhance understanding (if applicable)
- [ ] No spelling or grammatical errors

#### Governance Compliance
- [ ] Filename follows naming conventions
- [ ] Version number assigned correctly
- [ ] All required metadata fields completed
- [ ] Document ID assigned and unique
- [ ] Revision history included
- [ ] Keywords relevant and comprehensive

#### Legal Compliance
- [ ] All sources properly cited
- [ ] No verbatim code or standard reproduction
- [ ] Copyright notices included (if applicable)
- [ ] Licensing terms specified
- [ ] Fair use doctrine respected

#### Formatting and Style
- [ ] Style guide standards followed
- [ ] Markdown formatting consistent
- [ ] Code blocks use proper syntax highlighting
- [ ] Tables formatted correctly
- [ ] Links and cross-references functional
- [ ] Section numbering sequential

### Automated Validation Tools

**Pre-Commit Hooks** (run automatically before Git commits):
- Filename format validation
- Metadata field presence check
- Markdown linting (formatting errors)
- Spell check (technical dictionary)
- Version number format validation

**CI/CD Pipeline Checks** (run on pull requests):
- Document ID uniqueness
- Version number sequence (no skipped versions)
- Broken link detection
- Copyright notice presence
- File size limits (flag large files)

**Periodic Audits** (manual or scripted):
- Cross-reference validation (all referenced docs exist)
- Metadata consistency across versions
- Naming convention drift detection
- Orphaned files (not linked from any document)

---

## Content Classification Taxonomy

### Classification Dimensions

#### 1. Discipline

- **Electrical (E)**: Power distribution, lighting, fire alarm, telecommunications
- **Mechanical (M)**: HVAC, plumbing, piping
- **Plumbing (P)**: Domestic water, sanitary, storm drainage
- **Fire Protection (FP)**: Sprinklers, standpipes, fire alarm
- **Multi-Discipline (MEP)**: Coordination, BIM, energy modeling
- **Administrative (ADMIN)**: Governance, procedures, training

#### 2. Document Type

- **DWG**: Engineering drawings, diagrams, schematics
- **SPEC**: Specifications, requirements, standards
- **CALC**: Calculation sheets, design tools
- **RPT**: Reports, analysis, studies
- **SOP**: Standard operating procedures
- **GUIDE**: Reference guides, how-tos, tutorials
- **STD**: Policies, standards, governance
- **FORM**: Templates, forms, checklists
- **CODE**: Scripts, tools, automation
- **DATA**: Reference data, tables, datasets

#### 3. Content Maturity

- **DRAFT**: In development, not reviewed
- **REVIEW**: Submitted for review
- **APPROVED**: Published and current
- **SUPERSEDED**: Replaced by newer version
- **OBSOLETE**: No longer applicable

#### 4. Complexity Level

- **Fundamental**: Basic concepts, introductory content
- **Intermediate**: Standard practice, typical applications
- **Advanced**: Complex scenarios, specialized topics
- **Expert**: Cutting-edge, research, rare situations

**Usage**: Tag content with complexity level to guide users to appropriate resources

#### 5. Code/Standard Basis

- **NEC 2020**: National Electrical Code 2020 edition
- **NEC 2023**: National Electrical Code 2023 edition
- **NEC 2026**: National Electrical Code 2026 edition (future)
- **IPC 2021**: International Plumbing Code 2021
- **IMC 2021**: International Mechanical Code 2021
- **NFPA 13**: Standard for Installation of Sprinkler Systems
- **ASHRAE 90.1**: Energy Standard for Buildings

**Usage**: Clearly identify which code/standard version content is based on

#### 6. Access Classification

- **Public**: Shareable outside organization (open source, educational)
- **Internal**: Organization use only, not proprietary
- **Confidential**: Sensitive, restricted distribution
- **Client-Specific**: Project or client restricted

**Usage**: Determines access permissions and sharing restrictions

### Taxonomy Application

**Metadata Tags Example**:
```yaml
discipline: Electrical
document_type: Calculation
content_maturity: APPROVED
complexity_level: Intermediate
code_basis: NEC 2023
access_classification: Internal
topics:
  - voltage drop
  - feeder sizing
  - conductor selection
applications:
  - commercial buildings
  - residential
target_audience:
  - electrical engineers
  - designers
```

---

## Tools and Systems

### Version Control System (Git)

**Primary Repository**: Git-based (GitHub, GitLab, Bitbucket)

**Branch Strategy**:
- `main`: Published content only (protected)
- `develop`: Integration branch for approved content
- `feature/{DocID}-{description}`: Individual content development
- `fix/{DocID}-{issue}`: Error corrections
- `release/{version}`: Staged releases

**Commit Message Format**:
```
{DocID} v{Version}: {Brief description}

{Detailed explanation if needed}
```

**Example**:
```
E-CALC-042 v1.2.0: Add load diversity factors

Added section 3.4 covering NEC 220.40 load diversity factors for commercial buildings. Includes worked examples for office and retail occupancies.
```

### Knowledge Management Platform

**Options**:
- **Confluence**: Wiki-style documentation
- **SharePoint**: Document management and collaboration
- **GitBook**: Git-backed documentation platform
- **Custom Portal**: Web interface to Git repository

**Features**:
- Full-text search across all content
- Faceted filtering by discipline, document type, tags
- User comments and feedback
- Analytics and usage tracking
- Access control integration (RBAC)

### Review and Workflow Tools

**Options**:
- **GitHub Pull Requests**: Code review for text documents
- **Jira/Asana**: Issue tracking and workflow management
- **ReviewBoard/Phabricator**: Dedicated code review platforms

**Workflow Configuration**:
- Review request triggers email notifications
- Automated assignment to reviewers based on discipline
- SLA reminders for overdue reviews
- Approval gates before merging to main branch

### Validation and Quality Tools

**Automated Tools**:
- **markdownlint**: Markdown syntax and style checking
- **vale**: Prose linting (style guide enforcement)
- **aspell/hunspell**: Spell checking with technical dictionaries
- **linkchecker**: Broken link detection
- **Custom scripts**: Filename validation, metadata extraction

**CI/CD Integration**:
```yaml
# Example GitHub Actions workflow
name: Document Validation
on: [pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run markdownlint
        run: markdownlint '**/*.md'
      - name: Check metadata
        run: python scripts/validate_metadata.py
      - name: Spell check
        run: aspell check --mode=markdown *.md
```

---

## Metrics and Performance

### Key Performance Indicators (KPIs)

#### 1. Content Quality Metrics

- **First-Pass Approval Rate**: % of submissions approved without revisions
  - **Target**: >70%
- **Average Review Iterations**: Number of review cycles before approval
  - **Target**: <2.0
- **Error Rate**: Errors discovered post-publication per 100 documents
  - **Target**: <5

#### 2. Process Efficiency Metrics

- **Average Time to Publish**: Days from initiation to publication
  - **Target**: <15 days (standard), <30 days (complex)
- **Review Turnaround Time**: Days from submission to review completion
  - **Target**: <5 days
- **SLA Compliance**: % of reviews completed within SLA
  - **Target**: >90%

#### 3. Content Utilization Metrics

- **Monthly Active Users**: Unique users accessing knowledge base
- **Most Accessed Documents**: Top 10 by page views
- **Search Effectiveness**: % of searches resulting in document access
  - **Target**: >60%
- **User Feedback Score**: Average rating from user surveys
  - **Target**: >4.0/5.0

#### 4. Content Health Metrics

- **Coverage Ratio**: % of identified topics with documentation
  - **Target**: >80%
- **Currency Rate**: % of documents reviewed in past 12 months
  - **Target**: >75%
- **Orphan Rate**: % of documents with no inbound links
  - **Target**: <10%

### Reporting and Dashboards

**Monthly Reports**:
- New content published (count, by discipline)
- Content updated (count, by type)
- Content retired (count, reasons)
- Review metrics (average time, SLA compliance)
- Top contributors and reviewers

**Quarterly Reviews**:
- KPI trends and analysis
- User feedback summary
- Compliance audit findings
- Improvement initiatives progress

**Annual Summary**:
- Total content inventory
- Growth rate
- User engagement trends
- Return on investment (ROI) analysis

---

## Appendix A: Content Proposal Form Template

```markdown
# Content Proposal Form

**Submitted By**: [Your Name]
**Date**: [YYYY-MM-DD]
**Discipline**: [Electrical/Mechanical/Plumbing/Fire Protection/MEP/Admin]

## Proposed Content

**Title**: [Descriptive title for content]
**Document Type**: [DWG/SPEC/CALC/RPT/SOP/GUIDE/STD/FORM/CODE/DATA]
**Complexity Level**: [Fundamental/Intermediate/Advanced/Expert]

## Justification

**Need**: [Why is this content needed? What gap does it fill?]
**Target Audience**: [Who will use this content?]
**Expected Usage**: [Estimated frequency of use]

## Scope and Outline

[Brief outline of proposed content structure]

## Related Existing Content

[List any existing documents that are related or similar]

## Resources Required

**Estimated Effort**: [Hours or days to create]
**Subject Matter Experts**: [Names of SMEs to consult]
**References Needed**: [Code sections, standards, external resources]

## Proposed Reviewers

**Technical Reviewer**: [Suggested name]
**QA Reviewer**: [Suggested name]

---

**Knowledge Manager Decision**:
- [ ] APPROVED - Assigned Document ID: ___________
- [ ] DEFERRED - Reason: ___________
- [ ] REJECTED - Reason: ___________

**Signature**: ___________________________ **Date**: __________
```

---

## Appendix B: Review Report Template

```markdown
# Technical/QA Review Report

**Document ID**: [E-CALC-042]
**Document Title**: [Transformer Sizing Calculator]
**Version Reviewed**: [v0.9.0]
**Reviewer Name**: [John Smith]
**Review Date**: [YYYY-MM-DD]

## Overall Recommendation

- [ ] APPROVE - Ready for publication
- [ ] APPROVE WITH MINOR CHANGES - Recommend approval after minor corrections
- [ ] REQUEST REVISIONS - Requires significant changes before approval
- [ ] REJECT - Fundamental issues, not suitable for knowledge base

## Review Checklist

### Technical Accuracy (Technical Review)
- [ ] Calculations verified and correct
- [ ] Code references accurate
- [ ] Methodology sound
- [ ] Assumptions stated

### Completeness
- [ ] All required sections present
- [ ] Scope adequately covered
- [ ] Examples sufficient

### Clarity and Usability
- [ ] Content understandable
- [ ] Logical organization
- [ ] Graphics enhance understanding

### Governance Compliance (QA Review)
- [ ] Naming conventions followed
- [ ] Versioning correct
- [ ] Metadata complete

### Legal Compliance (QA Review)
- [ ] Citations proper
- [ ] No copyright violations
- [ ] Licensing specified

## Detailed Feedback

### Critical Issues (Must Fix)

1. [Issue description, location, recommendation]
2. [...]

### Major Issues (Should Fix)

1. [Issue description, location, recommendation]
2. [...]

### Minor Issues (Suggested Improvements)

1. [Issue description, location, recommendation]
2. [...]

## Summary and Comments

[Overall assessment, strengths, areas for improvement]

---

**Reviewer Signature**: ___________________________ **Date**: __________
```

---

**End of Document**

**Approval Signatures**:
- Technical Lead: ___________________________ Date: __________
- QA Manager: ______________________________ Date: __________
- Knowledge Manager: ________________________ Date: __________
