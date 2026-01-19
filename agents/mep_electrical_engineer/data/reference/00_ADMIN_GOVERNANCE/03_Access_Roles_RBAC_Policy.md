# Access Roles and RBAC Policy

**Document ID**: ADMIN-GOV-03
**Version**: 1.0.0
**Last Updated**: 2025-10-22
**Author**: MEP Security & Access Control Team
**Status**: Approved

## Table of Contents

1. [Purpose and Scope](#purpose-and-scope)
2. [RBAC Principles and Framework](#rbac-principles-and-framework)
3. [Role Definitions](#role-definitions)
4. [Permission Matrices](#permission-matrices)
5. [Data Classification](#data-classification)
6. [Authentication and Authorization](#authentication-and-authorization)
7. [Access Request Procedures](#access-request-procedures)
8. [Access Revocation](#access-revocation)
9. [Audit and Compliance](#audit-and-compliance)
10. [Special Access Scenarios](#special-access-scenarios)

---

## Purpose and Scope

### Purpose

This document establishes Role-Based Access Control (RBAC) policies for the MEP Engineering Knowledge Base. It defines:

- **User Roles**: Standardized roles with defined responsibilities
- **Access Permissions**: Granular controls on read, write, modify, delete operations
- **Data Classification**: Sensitivity levels determining access restrictions
- **Procedures**: Processes for requesting, granting, and revoking access
- **Audit Requirements**: Logging and monitoring for security and compliance

### Scope

**In Scope**:
- All content in MEP Engineering Knowledge Base
- All users (employees, contractors, partners, students)
- All access methods (web portal, API, Git repository, exports)
- All operations (read, write, modify, delete, download, share)

**Out of Scope**:
- Project-specific repositories with separate access controls
- Personal workspaces and draft areas
- External websites and third-party resources (linked but not controlled)

### Compliance Requirements

This RBAC policy supports compliance with:
- **SOC 2 Type II**: Access controls and audit trails
- **ISO 27001**: Information security management
- **NIST Cybersecurity Framework**: Identity management and access control
- **State PE Licensing Requirements**: Protection of engineering work products
- **Client Contractual Requirements**: Confidentiality and data protection clauses

---

## RBAC Principles and Framework

### Core RBAC Principles

#### 1. Least Privilege

**Definition**: Users receive minimum permissions necessary to perform their job functions

**Application**:
- Default access level is **Viewer** (read-only)
- Elevated permissions granted only when justified
- Temporary elevated access expires automatically
- Periodic review to revoke unused permissions

#### 2. Separation of Duties

**Definition**: Critical operations require involvement of multiple roles

**Application**:
- Content creator cannot self-approve (requires reviewer)
- Reviewer cannot publish (requires knowledge manager)
- System administrator cannot delete audit logs
- Financial or contractual content requires additional approval

#### 3. Role-Based Assignment

**Definition**: Permissions tied to roles, not individuals

**Application**:
- Users assigned to predefined roles
- Role changes automatically update permissions
- Custom permissions prohibited (use roles only)
- Role descriptions clearly define responsibilities

#### 4. Need-to-Know Basis

**Definition**: Access granted only for information required for job function

**Application**:
- Discipline-specific access (electrical engineers access electrical content)
- Project-based access (team members access project files)
- Time-limited access for temporary assignments
- Confidential data restricted to authorized personnel

### RBAC Architecture

```
User → Assigned Role(s) → Role Permissions → Resource Access
```

**Components**:
- **User**: Individual with unique identity (employee, contractor, partner)
- **Role**: Named set of permissions (Viewer, Contributor, Reviewer, etc.)
- **Permission**: Specific operation on resource type (Read:Document, Write:Calculation)
- **Resource**: Content object (document, folder, dataset, code repository)

**Example**:
```
Jane Doe → Electrical Engineer (Contributor) → Write:Electrical-Content → Can edit E_CALC_042
```

---

## Role Definitions

### Role Hierarchy

```
System Administrator
    ├── Knowledge Manager
    │   ├── QA Reviewer
    │   └── Technical Reviewer
    │       └── Contributor
    │           └── Viewer
    └── Security Auditor (parallel)
```

**Inheritance**: Higher roles inherit all permissions of lower roles.

---

### Role 1: Viewer

**Description**: Read-only access to approved content in knowledge base

**Typical Users**:
- All employees and authorized contractors (default role)
- Students and interns
- External partners (limited scope)
- New hires during onboarding

**Responsibilities**:
- Browse and search knowledge base
- Read approved documents
- Download content for internal use (per license terms)
- Provide feedback via comments or forms

**Permissions**:
- ✅ Read APPROVED content (PUBLIC and INTERNAL classification)
- ✅ Search and filter content
- ✅ Export/print for personal use
- ✅ Submit feedback or error reports
- ❌ No write, modify, or delete access
- ❌ Cannot access DRAFT or REVIEW content
- ❌ Cannot access CONFIDENTIAL content

**Access Scope**:
- Approved content in assigned discipline(s)
- Public and internal classification only
- No access to draft, review, or archived versions

**Default Restrictions**:
- Cannot comment on documents (read-only)
- Cannot share externally
- No API access

---

### Role 2: Contributor

**Description**: Create and submit new content for knowledge base

**Typical Users**:
- Engineers (PE or EIT)
- Senior designers
- Subject matter experts
- Technical writers

**Responsibilities**:
- Draft new content following standards
- Submit content for review
- Respond to reviewer feedback
- Maintain assigned content

**Permissions**:
- ✅ All Viewer permissions (inherited)
- ✅ Create new documents in assigned discipline
- ✅ Edit own DRAFT and REVIEW content
- ✅ Submit content for review
- ✅ Respond to reviewer comments
- ✅ Upload supporting files (images, data, code)
- ❌ Cannot approve or publish content
- ❌ Cannot edit others' content without co-author assignment
- ❌ Cannot delete published content

**Access Scope**:
- Create content in assigned discipline(s)
- Edit own drafts and content under review
- Read DRAFT content they created or are assigned to
- Internal and public classification

**Approval Requirements**:
- Manager approval for Contributor role assignment
- Technical competency verification (PE license, experience, training)

---

### Role 3: Technical Reviewer

**Description**: Evaluate content for technical accuracy and code compliance

**Typical Users**:
- Licensed Professional Engineers (PE)
- Senior engineers with 10+ years experience
- Discipline leads and technical managers
- Subject matter experts in specific areas

**Responsibilities**:
- Review assigned content for technical correctness
- Verify calculations and code compliance
- Provide constructive feedback
- Recommend approve/revise/reject decisions

**Permissions**:
- ✅ All Contributor permissions (inherited)
- ✅ Read DRAFT and REVIEW content in assigned discipline
- ✅ Comment on and annotate content under review
- ✅ Request revisions or reject content
- ✅ Recommend approval (not final approval)
- ✅ Access to review workflow tools
- ❌ Cannot publish content (requires Knowledge Manager)
- ❌ Cannot modify content under review (comments only)

**Access Scope**:
- Review content in assigned discipline(s)
- DRAFT and REVIEW content assigned for review
- All classification levels (per need-to-know)

**Approval Requirements**:
- PE license (required) OR 10+ years relevant experience
- Technical competency assessment
- Training on review standards and procedures

---

### Role 4: QA Reviewer

**Description**: Ensure content meets quality, governance, and legal standards

**Typical Users**:
- Quality assurance specialists
- Technical editors
- Compliance officers
- Knowledge management staff

**Responsibilities**:
- Review content for governance compliance
- Verify metadata, formatting, and style
- Check copyright and licensing compliance
- Recommend approve/revise/reject decisions

**Permissions**:
- ✅ All Viewer permissions (inherited)
- ✅ Read DRAFT and REVIEW content (all disciplines)
- ✅ Comment on content under review
- ✅ Request revisions or reject content
- ✅ Recommend approval (not final approval)
- ✅ Access to review workflow tools
- ✅ Run automated validation tools
- ❌ Cannot publish content (requires Knowledge Manager)
- ❌ Cannot modify technical content

**Access Scope**:
- Review content in all disciplines
- DRAFT and REVIEW content in workflow
- All classification levels

**Approval Requirements**:
- QMS training and certification
- Knowledge of copyright law and documentation standards
- Training on knowledge base governance

---

### Role 5: Knowledge Manager

**Description**: Oversee knowledge base operations, approve content for publication

**Typical Users**:
- Knowledge management lead (typically 1-2 people)
- Information architects
- Senior technical editors

**Responsibilities**:
- Coordinate content workflows
- Assign document IDs
- Grant final approval for publication
- Manage content lifecycle
- Resolve escalations
- Generate reports and metrics

**Permissions**:
- ✅ All Technical Reviewer and QA Reviewer permissions
- ✅ Publish approved content to main repository
- ✅ Edit metadata and document properties
- ✅ Move content between lifecycle states
- ✅ Retire or archive content
- ✅ Assign reviewers and manage workflows
- ✅ Access all content (including CONFIDENTIAL)
- ✅ Generate access and usage reports
- ❌ Cannot delete published content (requires System Administrator)

**Access Scope**:
- Full read/write access to all content
- All disciplines and classification levels
- Workflow management tools
- Reporting and analytics dashboards

**Approval Requirements**:
- Experience in knowledge management or technical documentation
- Training on all governance policies
- Background check (handles sensitive content)

---

### Role 6: System Administrator

**Description**: Manage technical infrastructure, access controls, and system security

**Typical Users**:
- IT systems administrators
- DevOps engineers
- Infrastructure team

**Responsibilities**:
- Maintain version control systems
- Configure access permissions and RBAC
- Implement security controls
- Perform backups and disaster recovery
- Troubleshoot technical issues
- Monitor system security and performance

**Permissions**:
- ✅ Full system access (read, write, delete, configure)
- ✅ Manage user accounts and role assignments
- ✅ Configure security settings and access controls
- ✅ Access audit logs (read-only)
- ✅ Perform system maintenance and upgrades
- ✅ Delete content (with approval and audit trail)
- ❌ Cannot delete or modify audit logs
- ❌ Require approval for bulk deletions or major changes

**Access Scope**:
- Full administrative access to all systems
- All content and configuration
- System logs and security monitoring

**Approval Requirements**:
- IT security clearance
- Background check
- Training on security policies and incident response

---

### Role 7: Security Auditor

**Description**: Monitor compliance, conduct audits, investigate security incidents

**Typical Users**:
- Information security team
- Internal audit staff
- Compliance officers

**Responsibilities**:
- Conduct security audits
- Review access logs
- Investigate security incidents
- Ensure RBAC policy compliance
- Report findings to management

**Permissions**:
- ✅ Read-only access to all content
- ✅ Full access to audit logs
- ✅ Access to user activity reports
- ✅ Generate compliance reports
- ❌ No write or delete access to content
- ❌ No modification of system configuration

**Access Scope**:
- Read-only access to all systems and content
- Full audit log access
- User and permission reports

**Approval Requirements**:
- Information security certification (CISSP, CISM, or equivalent)
- Background check
- Training on audit procedures

---

## Permission Matrices

### Content Operations Permission Matrix

| Operation | Viewer | Contributor | Tech Reviewer | QA Reviewer | Knowledge Mgr | Sys Admin |
|-----------|--------|-------------|---------------|-------------|---------------|-----------|
| **Read APPROVED content** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Read DRAFT (own)** | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ |
| **Read DRAFT (others)** | ❌ | ❌ | ✅* | ✅* | ✅ | ✅ |
| **Read REVIEW content** | ❌ | ❌ | ✅* | ✅* | ✅ | ✅ |
| **Read CONFIDENTIAL** | ❌ | ❌ | ❌** | ❌** | ✅ | ✅ |
| **Create new content** | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ |
| **Edit own DRAFT** | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ |
| **Edit others' DRAFT** | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| **Comment on content** | ❌ | ❌ | ✅* | ✅* | ✅ | ❌ |
| **Submit for review** | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ |
| **Approve content** | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| **Publish content** | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| **Retire content** | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| **Delete content** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅*** |
| **Export/download** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Share externally** | ❌ | ❌ | ❌ | ❌ | ❌**** | ✅**** |

**Legend**:
- ✅ = Permitted
- ❌ = Not permitted
- \* = Only for assigned reviews
- \*\* = Only with specific authorization
- \*\*\* = Requires approval and audit trail
- \*\*\*\* = Requires executive approval

### Administrative Operations Matrix

| Operation | Viewer | Contributor | Tech Reviewer | QA Reviewer | Knowledge Mgr | Sys Admin | Auditor |
|-----------|--------|-------------|---------------|-------------|---------------|-----------|---------|
| **Assign document IDs** | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |
| **Assign reviewers** | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |
| **Manage workflows** | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |
| **Grant access** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| **Revoke access** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| **View audit logs** | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| **Generate reports** | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| **Modify RBAC policies** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| **System configuration** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| **Conduct audits** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

### Discipline-Specific Access Matrix

| Discipline | Viewer | Contributor | Tech Reviewer | QA Reviewer | Knowledge Mgr |
|------------|--------|-------------|---------------|-------------|---------------|
| **Electrical (E)** | All | Elec only* | Elec only* | All | All |
| **Mechanical (M)** | All | Mech only* | Mech only* | All | All |
| **Plumbing (P)** | All | Plumb only* | Plumb only* | All | All |
| **Fire Protection (FP)** | All | FP only* | FP only* | All | All |
| **Multi-Discipline (MEP)** | All | All | All | All | All |
| **Administrative (ADMIN)** | Restricted** | Restricted** | N/A | All | All |

**Legend**:
- \* = Write access restricted to qualified personnel in that discipline
- \*\* = Only management and knowledge management staff

---

## Data Classification

### Classification Levels

#### Level 1: PUBLIC

**Definition**: Content suitable for public dissemination

**Examples**:
- General educational guides
- Public domain references
- Open source code and tools
- Non-proprietary methodologies

**Access Control**:
- All roles (Viewer and above)
- No authentication required for viewing
- May be shared externally

**Marking**: No special marking required

#### Level 2: INTERNAL

**Definition**: Content for internal use within [Organization Name]

**Examples**:
- Engineering calculations and methods
- Technical specifications
- Standard operating procedures
- Training materials

**Access Control**:
- All authenticated users (Viewer role minimum)
- Employees and authorized contractors only
- Not for external distribution

**Marking**: "Internal Use Only" footer

#### Level 3: CONFIDENTIAL

**Definition**: Sensitive content with restricted access

**Examples**:
- Proprietary calculation methods
- Client-specific designs
- Financial or business-sensitive information
- Pre-publication research

**Access Control**:
- Knowledge Manager approval required
- Need-to-know basis only
- Specific authorization for each access
- No export/download without approval

**Marking**: "CONFIDENTIAL - Restricted Access" header/footer

#### Level 4: CLIENT-SPECIFIC

**Definition**: Content tied to specific client projects or contracts

**Examples**:
- Project-specific drawings
- Client confidential specifications
- Contract deliverables

**Access Control**:
- Project team members only
- Client authorization may be required
- Typically managed outside general knowledge base

**Marking**: "CLIENT CONFIDENTIAL - [Client Name]" header

### Classification Marking Requirements

**Document Header Template**:
```markdown
# [Document Title]

**Classification**: [PUBLIC | INTERNAL | CONFIDENTIAL | CLIENT-SPECIFIC]
**Document ID**: [XXX-XXX-XXX]
**Access Restrictions**: [None | Internal Only | Authorized Personnel Only]
```

**Document Footer Template**:
```
Classification: [LEVEL] | © 2025 [Organization Name] | [Access Restrictions]
```

### Reclassification Procedures

**Upgrading Classification** (e.g., INTERNAL → CONFIDENTIAL):
1. Knowledge Manager or System Administrator initiates
2. Document rationale for upgrade
3. Update classification metadata and markings
4. Revoke access for users not authorized for new level
5. Notify affected users

**Downgrading Classification** (e.g., CONFIDENTIAL → INTERNAL):
1. Request must be approved by original classifier or Knowledge Manager
2. Verify no restrictions prevent downgrade (client contracts, etc.)
3. Update classification metadata and markings
4. Grant access to appropriate roles

---

## Authentication and Authorization

### Authentication Methods

#### Single Sign-On (SSO)

**Primary Method**: SAML 2.0 or OAuth 2.0 integration with corporate identity provider

**Supported Providers**:
- Active Directory / Azure AD
- Okta
- Google Workspace
- OneLogin

**Benefits**:
- Centralized credential management
- Multi-factor authentication (MFA)
- Automatic provisioning/deprovisioning
- Audit trail integration

#### Multi-Factor Authentication (MFA)

**Requirement**: MFA **required** for:
- System Administrators
- Knowledge Managers
- Access to CONFIDENTIAL content
- Remote access

**Methods**:
- Time-based One-Time Password (TOTP) apps (Authy, Google Authenticator)
- SMS codes (fallback only)
- Hardware tokens (YubiKey, etc.)
- Biometrics (if supported)

#### API Authentication

**Method**: API keys or OAuth 2.0 tokens

**Requirements**:
- API keys tied to user accounts
- Keys expire after 90 days (auto-renewal available)
- Separate keys for different access levels
- Rate limiting enforced

### Authorization Workflow

```
1. User authenticates (SSO + MFA)
    ↓
2. System retrieves user's assigned role(s)
    ↓
3. User requests resource access
    ↓
4. System checks:
   - User's role permissions
   - Resource classification level
   - Any explicit access grants/denials
    ↓
5. ALLOW or DENY access
    ↓
6. Log access attempt (success or failure)
```

### Session Management

**Session Timeout**:
- Web portal: 8 hours of inactivity
- API: Token expiration per OAuth settings (typically 1 hour)
- Administrative sessions: 2 hours of inactivity

**Concurrent Sessions**:
- Viewers: Unlimited
- Contributors/Reviewers: Up to 3 concurrent sessions
- Administrators: 1 concurrent session only

**Lockout Policy**:
- 5 failed authentication attempts → 15-minute lockout
- 10 failed attempts in 24 hours → Account disabled, notify security team

---

## Access Request Procedures

### Standard Access Request

#### Step 1: Submit Request

**Requester** submits Access Request Form via:
- Knowledge management portal
- Email to knowledge-manager@[organization].com
- IT service desk ticket

**Required Information**:
- Requester name and employee ID
- Role requested (Viewer, Contributor, Reviewer, etc.)
- Discipline(s) if applicable
- Justification (business need)
- Manager approval (attached or forwarded)
- Duration (permanent or temporary)

#### Step 2: Manager Approval

**Requester's Manager** reviews and approves/denies request:
- Verify business need
- Confirm role appropriate for job function
- Ensure compliance with least privilege principle

**Approval Methods**:
- Digital approval via portal
- Email confirmation
- Signature on printed form

#### Step 3: Knowledge Manager Review

**Knowledge Manager** reviews request:
- Verify manager approval
- Confirm role assignment is appropriate
- Check for any conflicts or concerns
- Approve or escalate to System Administrator

#### Step 4: Provisioning

**System Administrator**:
- Create or update user account
- Assign approved role(s)
- Set discipline restrictions if applicable
- Configure MFA if required
- Send welcome email with access instructions

**SLA**: Access provisioned within 2 business days of approval

#### Step 5: Confirmation

**Requester** receives:
- Access confirmation email
- Login credentials or SSO instructions
- Link to user guide and training materials
- Contact information for support

### Elevated Access Request

**For**: Temporary elevated permissions (e.g., Contributor → Reviewer for specific review)

**Additional Requirements**:
- Specific justification for elevated access
- Time-limited (specify start and end dates)
- Technical competency verification (if applicable)
- Sponsor approval (Knowledge Manager or higher)

**Auto-Expiration**: Elevated access automatically revoked at end date

### Emergency Access

**For**: Urgent situations requiring immediate access

**Procedure**:
1. Requester contacts System Administrator directly
2. Explain emergency situation and business impact
3. Temporary access granted for 24 hours
4. Formal access request must be submitted within 2 business days
5. Access revoked if formal request not approved

**Examples**:
- Production issue requiring immediate content update
- Critical client deliverable deadline
- Security incident response

**Audit**: All emergency access logged and reviewed

---

## Access Revocation

### Triggers for Revocation

**Automatic Revocation**:
- Employee termination
- Contractor assignment completion
- Temporary access expiration
- Role change (may reduce permissions)

**Manual Revocation**:
- Policy violation
- Security incident
- Misuse of access
- No longer needs access (periodic review)

### Revocation Procedures

#### Immediate Revocation (Termination or Security Incident)

**Timeline**: Within 1 hour of notification

**Actions**:
1. HR or Security notifies System Administrator
2. System Administrator disables account immediately
3. Revoke all access (portal, API, Git, etc.)
4. Invalidate active sessions
5. Review recent activity for anomalies
6. Document revocation in access log
7. Notify Knowledge Manager

#### Scheduled Revocation (Temporary Access Expiration)

**Timeline**: Automatic at end of access period

**Actions**:
1. System automatically revokes access at end date
2. Send notification to user 3 days prior
3. Send confirmation email upon revocation
4. Provide instructions for renewal if needed

#### Voluntary Revocation (User Request)

**Timeline**: Within 2 business days of request

**Actions**:
1. User submits revocation request
2. System Administrator processes request
3. Revoke specified access
4. Send confirmation to user
5. Update access logs

### Exit Checklist

**For Departing Employees/Contractors**:

- [ ] Revoke knowledge base access (all roles)
- [ ] Delete or reassign pending content
- [ ] Transfer ownership of approved content
- [ ] Revoke API keys and tokens
- [ ] Remove from distribution lists
- [ ] Retrieve any downloaded sensitive content
- [ ] Update audit logs with departure date
- [ ] Notify Knowledge Manager of content orphaned by departure

---

## Audit and Compliance

### Audit Logging Requirements

**All access must be logged** with following details:

**Log Attributes**:
- Timestamp (UTC)
- User ID and display name
- User role(s)
- Action performed (read, write, delete, download, etc.)
- Resource accessed (document ID, file path)
- Resource classification
- Source IP address
- Client application (web, API, Git)
- Result (success, denied, error)
- Reason for denial (if applicable)

**Log Retention**: Minimum 7 years (per compliance requirements)

**Log Protection**: Immutable, cannot be deleted or modified by any user including administrators

### Audit Log Examples

**Successful Read**:
```json
{
  "timestamp": "2025-10-22T14:32:15Z",
  "user_id": "jdoe",
  "user_name": "Jane Doe",
  "roles": ["Contributor", "Electrical"],
  "action": "READ",
  "resource": "E_CALC_042_transformer_sizing_v1-2-0.xlsx",
  "classification": "INTERNAL",
  "ip_address": "192.168.1.100",
  "client": "Web Portal",
  "result": "SUCCESS"
}
```

**Denied Access**:
```json
{
  "timestamp": "2025-10-22T14:35:42Z",
  "user_id": "bsmith",
  "user_name": "Bob Smith",
  "roles": ["Viewer"],
  "action": "WRITE",
  "resource": "E_CALC_042_transformer_sizing_v1-2-0.xlsx",
  "classification": "INTERNAL",
  "ip_address": "192.168.1.105",
  "client": "Git",
  "result": "DENIED",
  "reason": "Insufficient permissions (Viewer role)"
}
```

### Access Reviews

#### Quarterly Access Review

**Frequency**: Every 3 months

**Scope**: Review all user accounts and role assignments

**Procedure**:
1. System Administrator generates user access report
2. Knowledge Manager reviews report
3. Identify users with:
   - Inactive accounts (no activity in 90 days)
   - Elevated permissions no longer needed
   - Pending temporary access expirations
4. Notify managers of users flagged for review
5. Managers confirm access still required or request revocation
6. Update access as needed
7. Document review findings

**Output**: Access review report submitted to management

#### Annual Comprehensive Audit

**Frequency**: Annually

**Scope**: Complete audit of RBAC implementation and compliance

**Procedure**:
1. Security Auditor conducts audit
2. Review all access policies and procedures
3. Test access controls (attempt unauthorized access)
4. Review audit logs for anomalies
5. Interview sample of users about access appropriateness
6. Identify gaps or weaknesses
7. Recommend improvements
8. Present findings to executive management

**Output**: Audit report with findings and recommendations

### Compliance Monitoring

**Continuous Monitoring**:
- Failed access attempts (spike detection)
- Unusual access patterns (time, volume, resources)
- Privileged account activity
- CONFIDENTIAL content access
- External sharing attempts

**Alerts**:
- 5 failed login attempts → Alert user and System Administrator
- Access to CONFIDENTIAL content → Log and alert Security Auditor
- Bulk download (>10 documents in 10 minutes) → Alert Knowledge Manager
- Administrative action → Alert Security Auditor

**Incident Response**:
- Security team investigates alerts
- Determine if access was legitimate or malicious
- Take corrective action (revoke access, reset credentials, etc.)
- Document incident and response

---

## Special Access Scenarios

### External Partners and Clients

**Scenario**: Grant client or partner limited access to knowledge base

**Requirements**:
- Non-Disclosure Agreement (NDA) signed
- Approval from executive management
- Limited to specific content (create dedicated folder or classification)
- Time-limited access (specify end date)
- External user role (restricted Viewer permissions)

**Procedure**:
1. Business sponsor submits external access request
2. Legal reviews and approves (confirm NDA in place)
3. Executive management approves
4. System Administrator creates external user account
5. Assign External Viewer role with limited scope
6. Set automatic expiration date
7. Provide access instructions (no SSO, unique credentials)
8. Monitor access closely

**Restrictions**:
- No access to INTERNAL content (only PUBLIC or specifically authorized)
- No download/export capabilities
- No API access
- Watermarked content (if possible)

### Students and Interns

**Scenario**: Grant students/interns educational access

**Requirements**:
- Academic institution affiliation or internship agreement
- Faculty sponsor or intern supervisor approval
- Limited to PUBLIC and selected INTERNAL educational content
- Time-limited (semester or internship duration)

**Procedure**:
1. Sponsor submits access request
2. Knowledge Manager approves
3. System Administrator creates student account
4. Assign Student Viewer role (subset of Viewer)
5. Set automatic expiration at end of semester/internship
6. Provide access instructions and usage guidelines

**Restrictions**:
- No access to project-specific or client content
- No contribution or review capabilities
- Usage monitored and reviewed

### Service Accounts (Automation)

**Scenario**: Automated systems or scripts require API access

**Requirements**:
- Owned by specific department or project
- Clear business justification
- Named owner responsible for service account
- Separate credentials (not tied to individual user)

**Procedure**:
1. Service account owner submits request
2. Describe automation purpose and required access
3. Knowledge Manager approves
4. System Administrator creates service account
5. Assign appropriate role (typically Viewer or limited Contributor)
6. Generate API key with restricted scope
7. Document service account purpose and owner

**Restrictions**:
- No interactive login (API only)
- Rate limiting enforced
- Cannot access CONFIDENTIAL content
- Regular review of continued need

---

## Appendix A: Access Request Form Template

```markdown
# Knowledge Base Access Request Form

**Request Date**: _____________________
**Requested By**: _____________________
**Employee ID**: _____________________
**Department**: _____________________
**Manager**: _____________________

## Access Details

**Role Requested**: [Select One]
- [ ] Viewer
- [ ] Contributor
- [ ] Technical Reviewer
- [ ] QA Reviewer
- [ ] Knowledge Manager
- [ ] Other: _______________

**Discipline(s)**: [Select All That Apply]
- [ ] Electrical
- [ ] Mechanical
- [ ] Plumbing
- [ ] Fire Protection
- [ ] Multi-Discipline
- [ ] Administrative

**Access Duration**:
- [ ] Permanent (tied to job role)
- [ ] Temporary (specify dates): From __________ To __________

**Classification Levels Needed**:
- [ ] PUBLIC only
- [ ] INTERNAL
- [ ] CONFIDENTIAL (requires additional justification)

## Justification

**Business Need**: [Explain why access is required]

**Job Function**: [Describe how access relates to job responsibilities]

**Specific Content**: [If requesting access to specific content only, list here]

## Approvals

**Manager Approval**:
- [ ] Approved  - [ ] Denied
- **Signature**: _____________________ **Date**: __________

**Knowledge Manager Approval**:
- [ ] Approved  - [ ] Denied  - [ ] Escalated to System Administrator
- **Signature**: _____________________ **Date**: __________

**System Administrator** (if escalated):
- [ ] Approved  - [ ] Denied
- **Signature**: _____________________ **Date**: __________

## Provisioning (For System Administrator Use)

**User Account Created**: [ ] Yes  [ ] No
**Username**: _____________________
**Role(s) Assigned**: _____________________
**Discipline(s)**: _____________________
**MFA Configured**: [ ] Yes  [ ] No
**Access Granted Date**: _____________________
**Expiration Date** (if temporary): _____________________

**Provisioned By**: _____________________ **Date**: __________
```

---

## Appendix B: Role Comparison Quick Reference

| Feature | Viewer | Contributor | Tech Reviewer | QA Reviewer | Knowledge Mgr |
|---------|--------|-------------|---------------|-------------|---------------|
| Read approved content | ✅ | ✅ | ✅ | ✅ | ✅ |
| Create new content | ❌ | ✅ | ✅ | ❌ | ✅ |
| Edit own drafts | ❌ | ✅ | ✅ | ❌ | ✅ |
| Review content | ❌ | ❌ | ✅ | ✅ | ✅ |
| Approve content | ❌ | ❌ | ❌ | ❌ | ✅ |
| Publish content | ❌ | ❌ | ❌ | ❌ | ✅ |
| Access confidential | ❌ | ❌ | ❌* | ❌* | ✅ |
| Manage workflows | ❌ | ❌ | ❌ | ❌ | ✅ |
| MFA required | ❌ | ❌ | ❌ | ❌ | ✅ |

\* With specific authorization only

---

**End of Document**

**Approval Signatures**:
- Information Security Officer: __________________ Date: __________
- Knowledge Manager: ___________________________ Date: __________
- Executive Sponsor: ____________________________ Date: __________
