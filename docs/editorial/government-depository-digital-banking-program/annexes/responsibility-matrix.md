# Annex D — Responsibility Matrix

## Purpose and Limitation

This annex is the canonical sector-level reference for responsibility boundaries in the Government Depository Digital Banking Program.

It is not a legal RACI, procurement allocation, service-level agreement, outsourcing opinion, or statement about a named institution. Actual responsibility must be established from applicable law, regulation, charter, policy, appropriation or funding authority, procurement or engagement instrument, account structure, contract, operating procedure, and approved implementation design.

## Responsibility Principles

1. Public authority remains with the authorized public institution and officials.
2. Banking authority, custody, accounts, production, and settlement relationships remain with the depository institution.
3. x-change expresses approved operating state and responsibility; it is not a legal actor.
4. ODTI licenses and maintains software; it does not become the government entity or bank.
5. A regulated provider performs its approved service; connectivity does not create the complete banking ceremony.
6. Delegated DevOps changes who performs a technical task, not who owns institutional accountability.
7. Audit and regulatory judgment remain independent.
8. Beneficiaries and other participants retain the right to clear treatment, evidence, support, and recourse under the applicable arrangement.
9. Technical certification is evidence. Readiness is an institutional decision.
10. Unknown responsibility must remain visible until the authorized institutions resolve it.

## Role Charters

### Government agency or public entity

The government entity establishes or administers public purpose, authority, funding basis, participants, approvals, conditions, communications, official records, reporting, and public accountability within its mandate.

It is accountable for the public program. It is not ordinarily responsible for maintaining the bank's platform, production credentials, settlement account, or banking controls.

### Authorized government treasury, finance, budget, and accounting functions

These functions govern public funding, cash, accounts, release, accounting, reporting, and reconciliation according to their authority. In this annex, **government Treasury** means those institutional authorities and records. It is distinct from **x-change Treasury**, which is the platform's operational financial-state view.

They determine or approve the applicable public-finance treatment. Software state does not make that determination.

### Authorized Government Depository Bank or institution

The AGDB or other eligible depository institution provides the regulated banking service. It owns or establishes the relevant accounts, custody, policies, controls, infrastructure, credentials, settlement relationships, participant treatment, operations, support, reconciliation, provider oversight, production decisions, and institutional readiness.

Eligibility does not establish selection or readiness for every workflow.

### Regulated settlement or financial-service provider

The provider performs the regulated or contracted service accepted under its relationship with the depository institution. It controls its own systems, credentials, provider records, and obligations.

It does not define the public program, own the banking relationship, or determine the institution's complete operating readiness.

### x-change

x-change is the licensed software system and canonical operating grammar. It represents Funding Events, Treasury state, Liens, Facilities, Settlement Envelopes, Pay Codes, execution progression, and evidence according to approved configuration.

x-change is not a corporation, authority, custodian, account, settlement provider, auditor, or decision owner. Responsibility attributed to the software is performed institutionally by its operator, maintainer, or authorized user.

### ODTI

ODTI licenses and maintains x-change, `emi-core`, supported components, documentation, reference architecture, testing capability, and agreed institution-specific driver work.

ODTI is responsible for obligations within the agreed software, maintenance, implementation, or support scope. It does not provide public authority, depository authority, custody, settlement access, procurement approval, or production authorization.

### DevOps or implementation provider

The provider performs delegated engineering or operating tasks such as discovery, configuration, deployment, observability, backup, recovery, release support, incident work, and driver implementation.

Its authority must be explicit, limited, logged, reviewable, and revocable. It does not own the institution's environment, data, credentials, provider accounts, or release decision.

### Auditor

The auditor examines authority, records, controls, performance, exceptions, and reconciliation under the applicable mandate. The auditor depends on complete, attributable, durable evidence and institutional explanations.

Audit independence must be preserved. The auditor does not become the operator or allow platform status to replace professional judgment.

### Regulator or oversight authority

The regulator or oversight authority supervises or reviews matters within its mandate, which may include banking safety, public accountability, consumer or participant protection, outsourcing, financial crime, data, records, and operational resilience.

The Program does not expand or limit that authority.

### Beneficiary, payer, personnel member, supplier, or other participant

The participant supplies or receives information, authority, funds, conditions, credentials, service, or evidence according to the workflow. The participant is responsible only for obligations properly assigned under the applicable program and service.

The participant should receive clear instructions, appropriate privacy, accurate status, usable evidence, support, and a fair path for correction or recourse.

## Responsibility Allocation Matrix

| Responsibility area | Accountable institution or authority | Responsible operating party | Supporting parties | Independent or participant interest |
| --- | --- | --- | --- | --- |
| Public purpose and program authority | Government agency or authorized public authority | Authorized public officials and program owner | Government Treasury, Legal, policy, and implementing functions | Auditor, oversight body, beneficiaries, and public-interest stakeholders |
| Funding authority and public accounting treatment | Authorized government treasury, budget, finance, and accounting functions | Designated public officials | Government agency, AGDB Finance and Treasury | Auditor and oversight authority |
| Eligibility and participant basis | Government agency within applicable authority | Program administrators and authorized data owners | AGDB applies banking and transaction controls; technology supports approved rules | Participant needs correction and recourse; auditor examines evidence |
| Depository banking service | AGDB | Public-sector banking, Operations, Treasury, Technology, and other bank functions | Government entity, ODTI, DevOps, settlement providers | Regulator, auditor, participants |
| Funds, custody, and bank accounts | AGDB and applicable public account authority according to the arrangement | AGDB Treasury, Operations, Finance, and authorized account personnel | Settlement provider and government finance functions | Auditor and regulator |
| Government records and source data | Government entity | Authorized program, payroll, treasury, procurement, or accounting data owners | AGDB receives only approved data; technology providers process under authority | Participants may have correction rights; privacy and audit functions oversee |
| Institution data, deployment, and credentials | AGDB | Technology, Security, Privacy, Operations, and authorized administrators | DevOps provider under delegation; ODTI within support scope | Regulator, Internal Audit, external auditor where applicable |
| Funding Event and Treasury configuration | AGDB, informed by authoritative public instructions and account treatment | AGDB Treasury, Finance, Product, Operations, and Technology | ODTI or implementation provider configures approved behavior | Audit and reconciliation functions review evidence |
| Facility and banking-service definition | AGDB | Business or public-sector banking with Operations, Treasury, Risk, Compliance, Legal, Finance, and Technology | Government entity supplies public-program requirements; ODTI supports representation | Board or delegated authority approves material scope; participants need clear service terms |
| Settlement Envelope and conditions | Government entity for public conditions; AGDB for banking execution conditions | Authorized public and banking officials | Technology and providers implement approved rules | Auditor, regulator, and participants require legibility and fair treatment |
| Pay Code or approved presentation | AGDB within the approved ceremony | AGDB channels and Operations; x-change generates or validates approved credentials | Government entity and implementation provider support presentation and communications | Participant uses the credential and needs support; audit may examine evidence |
| `emi-core` and canonical execution contract | ODTI within the license and maintenance scope | ODTI software-maintenance function | AGDB approves use; engineering provider supports testing | AGDB remains accountable for production use |
| Institution-specific driver | AGDB approves; ODTI or appointed provider is accountable within agreed engineering scope | Driver engineering and maintenance team | Settlement provider supplies interface evidence; AGDB supplies requirements and test access | Security, Risk, Compliance, Internal Audit, and regulator review as applicable |
| Execution authorization | Government entity for public instruction; AGDB for banking execution | Authorized officials, AGDB systems, Operations, and Treasury | x-change coordinates; driver and provider perform approved technical functions | Participant receives outcome; audit and regulator examine evidence |
| Regulated financial movement | AGDB under its approved account and provider relationship | Regulated settlement or payment provider within accepted scope | Driver submits approved instruction; AGDB monitors and reconciles | Regulator oversees within mandate; auditor examines records |
| Evidence and reconciliation | Government entity for public records; AGDB for banking and provider reconciliation | Program accounting, AGDB Operations, Treasury, Finance, and reconciliation owners | Providers return evidence; x-change preserves operating references; ODTI supports defects | Auditor and oversight functions require durable records; participant needs outcome evidence |
| Exceptions, reversals, and unresolved outcomes | AGDB and government entity within their respective responsibilities | Operations, Treasury, Finance, program administrators, and provider support | ODTI and DevOps address technical causes within scope | Participant needs timely resolution; auditors examine aging and closure |
| Security, privacy, and records | Each institution for its environment and obligations | Government and AGDB Security, Privacy, Technology, records, and business owners | Providers comply with assigned controls | Regulator, auditor, and affected participants retain applicable interests |
| Deployment and release | AGDB | Technology, Security, release management, and authorized DevOps personnel | ODTI supplies maintained release and evidence | Internal Audit and regulator may review; public entity approves its interface changes |
| Continuity and incident response | Each institution for its services and public obligations | Government program continuity, AGDB service continuity, provider incident teams | ODTI and DevOps support within scope | Participants need alternatives and communication; oversight functions review material events |
| Driver certification | AGDB under agreed provider and security criteria | ODTI or engineering provider produces test evidence; AGDB validates | Settlement provider supports applicable certification | Certification does not decide operational readiness |
| Operational readiness | AGDB and responsible government authorities for their respective decisions | Management and accountable control and operating functions | Providers supply evidence only | Board or delegated authority, audit, regulator, and participants have distinct interests |
| Production and expansion approval | Required public and AGDB authorities | Management and approved operators execute the decision | Providers implement the approved scope | Oversight continues; participants must receive appropriate treatment |

## Interaction Model

Responsibility crosses five recurring handoffs:

1. **Public instruction to banking service** — The government entity supplies valid authority, program data, conditions, and funding basis. The AGDB accepts only the banking responsibility it has approved.
2. **Banking service to software configuration** — The AGDB translates institutional policy into a Facility, Settlement Envelope, Treasury treatment, and participant journey. ODTI and implementation providers represent—not invent—those decisions.
3. **Operating grammar to provider execution** — `emi-core` and the institution-specific driver address the approved provider interface. The AGDB remains the execution authority under its account relationship.
4. **Provider result to institutional evidence** — Provider references and statuses return to x-change and institutional records. Government and bank reconciliation owners resolve differences.
5. **Operating evidence to readiness and oversight** — Management, control functions, auditors, regulators, and public authorities use evidence according to their mandates. No technical artifact decides for them.

## Responsibility Resolution Rule

An institution-specific responsibility matrix must replace generic stakeholder classes with actual legal entities, accountable offices, named decision roles, governing instruments, and escalation paths.

For every responsibility, the implementation record must identify:

- the accountable authority;
- the responsible operator;
- supporting and consulted parties;
- required evidence;
- applicable agreement or policy;
- escalation and exception owner;
- continuity owner; and
- unresolved matters.

An unresolved allocation must remain **Unknown**, **Institution-Provided**, or **Decision Required**. Polished prose, technical configuration, or a vendor assumption must not be used to conceal it.
