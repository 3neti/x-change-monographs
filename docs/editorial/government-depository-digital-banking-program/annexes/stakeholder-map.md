# Annex B — Stakeholder Architecture

## Purpose

This annex explains the institutions and people that may participate in a Government Depository Digital Banking Program, what each needs from the Program, where authority resides, and how participation changes across the lifecycle.

It does not assign statutory authority, establish a procurement relationship, or describe the organization of a named institution. Actual roles must be confirmed from applicable authority, policy, agreement, and operating design.

## Stakeholder System

```text
Public authority and oversight
        ↓
Government entity and accountable officials
        ↔
Government depository institution
        ↔
Regulated settlement and service providers
        ↔
ODTI, engineering, and DevOps providers
        ↓
Beneficiaries, payers, personnel, suppliers, and other participants
        ↓
Evidence, reconciliation, audit, and public accountability
```

No stakeholder can be understood only by its place in a technical sequence. Each enters with its own authority, interests, dependencies, records, and obligations.

## Lifecycle Participation

| Lifecycle stage | Principal stakeholders | Required interaction |
| --- | --- | --- |
| Program authorization | Board, Management, public-sector banking, responsible government sponsor | Establish purpose, scope, sponsorship, authority boundaries, and resources |
| Authority and suitability | Government legal and program officials, bank Legal, Risk, Compliance, Treasury, Finance, regulator where applicable | Determine whether the proposed relationship may proceed to design |
| Ceremony definition | Government program owner, bank Business and Operations, Treasury, participant representatives | Define the public outcome, banking service, evidence, conditions, and exception treatment |
| Architecture and discovery | Bank Technology and Security, ODTI, engineering provider, DevOps provider, settlement provider, government technology team | Establish systems, data, deployment, driver, provider, and control boundaries |
| Controlled testing | Operations, Technology, provider teams, Risk, Compliance, Finance, reconciliation owners | Test the complete ceremony, including ambiguity and failure |
| Readiness | Responsible public and banking authorities, control functions, Internal Audit where applicable | Decide whether evidence supports bounded production |
| Pilot | Program and banking operators, participants, support, providers, oversight functions | Operate within approved scope and collect pre-agreed evidence |
| Evidence review | Board or delegated authority, Management, government sponsor, control functions | Proceed, Correct, Extend, or Pause |
| Continuing operation | Service owners, Operations, Treasury, Technology, providers, audit and regulatory functions | Maintain performance, controls, records, reconciliation, continuity, and change governance |

## Public Authorities and Policy Institutions

### Executive and legislative authorities

Their interest is the lawful, effective, and accountable use of public money. They may establish mandates, appropriations, policy, oversight, or institutional authority according to the applicable framework.

They depend on reliable government administration, qualified financial institutions, credible evidence, and effective independent oversight. They do not delegate policy or statutory authority to the Program merely by supporting digital execution.

Across the lifecycle, they may define the governing mandate, approve or oversee policy, receive reports, and respond to audit or performance findings. Their role is not ordinarily to operate the software.

### Finance, budget, and treasury authorities

Their interests include fiscal discipline, cash management, account structure, release authority, timing, reporting, reconciliation, and unresolved public obligations.

They establish or administer applicable funding and treasury rules within their authority. They depend on accurate institutional records, accountable approvals, timely evidence, and explicit fund characterization.

Their participation may extend from workflow assessment through account and funding design, readiness review, reconciliation, and continuing reporting. x-change Treasury remains an operational view and does not replace their official records or authority.

## Government Entities

### Program owner or implementing agency

The government entity owns or administers the public purpose, participant basis, approved funding, conditions, accountable officials, communications, reporting, and public obligations within its mandate.

Its interest is not merely successful payment. It needs the authorized public outcome to occur with evidence, participant recourse, visible exceptions, and records suitable for accounting and oversight.

It depends on lawful authority, qualified providers, a capable depository institution, accurate participant and program data, support arrangements, and reconciliation. It interacts with the Program during service definition, approval, testing, pilot, evidence review, and continuing operation.

### Local Government Unit

An LGU may act as collector, employer, program sponsor, disbursing entity, grant administrator, disaster responder, or service provider under applicable authority.

Its interests include accessible local service, accurate attribution, timely disbursement, practical field operation, and records that survive personnel and administration changes. It depends on approved accounts, local operating capacity, reliable participant data, depository support, and clear escalation.

LGU participation must reflect the specific workflow and authority. The Program does not treat all LGUs as possessing identical systems, procurement routes, or operating capacity.

### Disbursing, payroll, treasury, and accounting officials

These officials translate institutional authority into accountable operating action. Their interests include correct preparation, segregation of duties, approvals, participant attribution, timing, records, exception resolution, and reconciliation.

They depend on authoritative program and personnel data, documented procedures, clear system roles, appropriate access, and evidence that can be related to official records.

They participate heavily in ceremony definition, acceptance testing, readiness, daily operation, exception handling, and evidence review. Automation supports their duties; it does not erase them.

## Government Depository Institution

### Board and executive leadership

The Board and executive leadership determine whether the institution should establish the Capability and assume the proposed banking responsibility. Their interests include mandate fit, public trust, strategy, risk appetite, financial sustainability, operating capacity, reputation, and accountable growth.

They depend on reliable evidence from Management and control functions. Board authorization begins the Program. It does not approve a government program or place a service into production.

### Public-sector banking and relationship functions

These functions define the institutional proposition, government relationship, banking service, approved commercial treatment, and service ownership.

They depend on confirmed authority, public-program requirements, operating feasibility, Treasury, provider capability, and a defensible financial case. They connect the public need to the institution's actual banking responsibility throughout discovery, design, launch, and relationship management.

### Operations and participant support

Operations defines supervision, procedures, service windows, support, escalation, complaints, exception decisions, reversals, evidence, and reconciliation practice.

Its interest is a complete ceremony that can be operated under ordinary and adverse conditions. It depends on clear authority, trained personnel, usable tools, observable status, provider escalation, and accountable owners.

### Treasury, Finance, and Accounting

These functions govern liquidity, accounts, provider positions, operational reservations, accounting treatment, financial reporting, charge treatment, and reconciliation.

They depend on explicit fund and account structures, complete references, durable records, timing rules, and ownership of unresolved items. Platform state supports their work; it does not determine legal or accounting treatment.

### Technology, Information Security, and Privacy

These functions govern architecture, systems, integration, identity, access, environments, data, security, observability, resilience, release, and incident management.

They depend on authorized discovery, accurate provider documentation, clear data flows, institution-controlled credentials, test environments, and maintainable service boundaries. They participate from architecture assessment through continuing change control.

### Risk, Compliance, Legal, and Internal Audit

These functions examine authority, legal form, procurement or engagement, financial crime, consumer or participant treatment, data, outsourcing, controls, evidence, and assurance according to their mandates.

They depend on complete and candid design information. They must be able to distinguish technical certification from operational readiness and a Program proposal from legal authority.

Internal Audit retains independent assurance. It does not become an implementation owner.

## Technology and Financial-Service Providers

### ODTI and the x-change software boundary

ODTI's interest is the integrity, maintainability, licensed use, and supported evolution of x-change, `emi-core`, documentation, reference architecture, and agreed driver work.

ODTI depends on defined scope, institution-approved requirements, controlled access, provider documentation, timely defect and change information, and clear acceptance criteria.

ODTI licenses and maintains software. It does not become the government entity, bank, custodian, settlement provider, auditor, or readiness authority. x-change is the operating system within the approved institutional boundary; it is not a legal actor.

### Engineering and driver provider

The engineering provider performs discovery, API mapping, implementation, testing, certification support, and maintenance for `3neti/emi-{institution}` where engaged.

It depends on approved documentation, test access, credentials under controlled use, representative cases, provider support, and change notices. Certification evidences agreed technical behavior. It does not authorize production.

### DevOps or managed-service provider

The DevOps provider may perform delegated provisioning, deployment, observability, backup, recovery, release support, and incident work.

It depends on explicit access, service levels, runbooks, escalation paths, security controls, and institution-owned decisions. Its access must be limited, logged, reviewable, and revocable. It does not own the environment, data, credentials, billing relationship, or release authority.

### Regulated settlement and payment providers

These providers execute the regulated or contracted portion of financial movement and return provider evidence under their relationship with the depository institution.

They depend on authorized accounts, valid credentials, supported messages, limits, operational funding, and clear exception procedures. They do not define the public program, own the banking relationship, or provide the complete ceremony.

## Oversight and Public-Interest Stakeholders

### Regulator

The regulator's interests include safety, soundness, lawful banking, consumer or participant protection, outsourcing, operational resilience, financial crime controls, and responsible institutional conduct within its mandate.

The regulator depends on accurate institutional disclosures, records, governance, and access under applicable authority. Integration does not diminish regulatory authority.

### Auditor and oversight body

Auditors and oversight bodies examine legality, prudence, records, segregation, performance, exceptions, and reconciliation within their mandates.

They depend on traceable authority, complete records, unresolved-item visibility, and institutional explanations. Platform evidence supports examination; it does not automate audit judgment.

### Public-interest and civil-society stakeholders

Their interests may include integrity, inclusion, accessibility, privacy, transparency, service quality, resilience, and public accountability.

They depend on truthful public communication, fair participant treatment, working recourse, and evidence that public value is not reduced to transaction volume.

## Participants

### Beneficiaries, pensioners, personnel, payees, and suppliers

Recipients need correct value, clear instructions, practical access, privacy, status, support, and fair resolution when something goes wrong.

They depend on accurate eligibility and identity data, accessible channels, dependable institutional support, and clear evidence. They are not required to understand the platform architecture to receive a lawful service.

### Taxpayers, fee payers, employers, merchants, and collecting parties

Payers and collecting parties need correct attribution, accepted channels, timely recognition, receipts or evidence, correction paths, and finality they can understand.

They depend on accurate obligations, references, account mapping, channel availability, and reconciliation between banking and government records.

## Stakeholder Interaction Questions

Every Institution Edition, proposal, and implementation design must answer:

1. Who possesses authority to establish the public purpose and workflow?
2. Which institution provides the banking service?
3. Who owns or controls accounts, funds, data, infrastructure, credentials, and approvals?
4. Which provider performs each regulated, technical, or operational function?
5. Who decides technical, operational, public-program, pilot, and production readiness?
6. Who receives, reconciles, preserves, and reviews execution evidence?
7. Who manages participant support, complaints, reversals, continuity events, and control failures?
8. Which dependencies cross institutional boundaries?
9. What remains Unknown or dependent on institution-provided evidence?
10. Which authority or agreement must resolve each open responsibility?

## Stakeholder-Briefing Rule

A common architecture does not justify a common explanation. Board members, government officials, Treasury and finance functions, operators, technologists, auditors, regulators, providers, and public participants require different decisions and levels of detail.

Future briefs may adapt emphasis and language. They must remain traceable to the same approved Program doctrine, and they must not alter authority, custody, settlement, readiness, or accountability boundaries.
