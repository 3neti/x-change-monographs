# Annex A — Program Architecture

## Purpose

This annex is the executive architecture reference for the Government Depository Digital Banking Program. It explains how public authority, banking responsibility, licensed software, institution-controlled operation, regulated settlement, and evidentiary accountability fit together.

It is not an institution-specific solution design, legal opinion, procurement specification, security architecture, or production authorization. Those require separate evidence and approval.

## Canonical Architecture Map

```text
Canonical x-change doctrine and Treasury grammar
                    ↓
Government Depository Digital Banking Program
                    ↓
Government Depository Program Guide
                    ↓
Institution Intelligence and Strategic Gap Analysis
                    ↓
Institution Edition and approved implementation scope
                    ↓
Commercial Proposal, discovery, and controlled implementation
```

The Program applies one canonical platform to a distinct institutional context. Public purpose changes. Participants and evidence change. The platform grammar does not.

## Institutional Boundary Map

```text
Government entity
Public purpose • authority • funding basis • participant rules • approvals • accountability
                                ↓
Government depository institution
Banking authority • custody • accounts • policy • production • settlement • reconciliation
                                ↓
x-change operating layer
Funding state • service meaning • conditions • credential • execution • evidence
                                ↓
Institution-specific execution layer
emi-core • 3neti/emi-{institution} • approved APIs • credentials
                                ↓
Regulated settlement and service providers
Accounts • rails • provider records • supported financial movement
```

No layer acquires the authority of the layer above it merely because information or instructions pass through it.

## Operating Layers

| Layer | Institutional function | Principal owner or authority | Boundary |
| --- | --- | --- | --- |
| Public authority | Establishes lawful purpose, funding basis, participants, conditions, approvals, reporting, and public accountability | Government entity and authorized officials | Cannot be delegated to software |
| Depository banking service | Defines the banking responsibility, accounts, policy, controls, participant treatment, support, and settlement arrangement | Government depository institution | Does not replace the public program |
| Licensed operating grammar | Represents recognized funding, service meaning, conditions, credentials, execution, and evidence | Institution operates licensed x-change software; ODTI maintains the software within scope | Does not hold funds or confer authority |
| Common execution contract | Provides the maintained interface between the operating grammar and institution-specific execution behavior | `emi-core`, maintained within the licensed software boundary | Does not contain the Facility's public or commercial meaning |
| Institution-specific driver | Maps the common contract to approved institutional API behavior | Institution approves; ODTI or appointed engineering provider implements and maintains within scope | Is not automatically available and is not readiness by itself |
| Regulated execution and settlement | Performs supported financial movement and returns provider evidence | Depository institution and its approved regulated providers | Connectivity does not create the complete banking service |
| Evidence and reconciliation | Relates instruction, conditions, provider result, exception, accounting, and final resolution | Responsible government and banking institutions | Platform records do not replace accounting or audit judgment |

## Canonical Operating Grammar

```text
Authorized public-finance instruction
                    ↓
Funding Event
                    ↓
Settlement Resources recognized by Treasury
                    ↓
Lien reserves resources for an authorized purpose
                    ↓
Facility defines the banking service
                    ↓
Settlement Envelope carries evidence and conditions
                    ↓
Pay Code or approved presentation carries the credential
                    ↓
Execution Engine and institution-specific driver
                    ↓
Approved settlement or service provider
                    ↓
Evidence, exception resolution, and reconciliation
```

### Funding Event

Records an external financial event through which Settlement Resources enter or become recognized by Treasury. It records recognition. It does not appropriate, create, or legally characterize public funds.

### Treasury and Lien

Treasury provides an operational view of recognized, available, reserved, outstanding, unresolved, and resolved resources. A Lien reserves capacity for an authorized purpose. Neither is the government account, bank account, appropriation record, trust record, or general ledger.

### Facility and Settlement Envelope

The Facility defines the banking service, participants, policy, limits, approved commercial treatment, and institutional responsibility. The governing government program remains the source of public authority. The Settlement Envelope carries the evidence and conditions that must be satisfied before an instruction proceeds.

### Pay Code and Presentation

A Pay Code is the credential to an authorized instruction. A voucher, claim stub, QR image, reference, or other approved presentation may carry or resolve to it. Presentation does not create a second balance, Treasury, Facility, or execution model.

### Execution and Evidence

The Execution Engine coordinates the approved progression. `emi-core` invokes the applicable institution-specific driver. The provider performs the supported financial movement. Institutional and provider references, statuses, exceptions, and evidence return for support and reconciliation.

## Software Ownership and Licensing Boundaries

| Concern | Program position |
| --- | --- |
| x-change intellectual property | Remains governed by the applicable ownership and license arrangements |
| Institution right to use | Defined by an institution-specific software license and approved scope |
| Canonical source and maintained releases | Supplied and maintained by ODTI within the agreed software boundary |
| Institution configuration | Approved by the institution and governed through its change process |
| Institution-specific driver | Requires separate discovery, mapping, implementation, certification, and maintenance scope |
| Government-program data | Remains governed by the responsible public and banking institutions under applicable authority and agreement |
| Production credentials and secrets | Remain under institution-approved control and do not belong in maintained source packages |
| Public or banking authority | Is never included in a software license |
| Settlement access | Is established by the institution through its approved accounts and provider relationships, not supplied by the license |

The license establishes a right to use maintained software. It does not confer depository status, procurement preference, public mandate, custody, settlement participation, or production approval.

## Operational Ownership

The participating institution remains accountable for the operating model it approves. Delegation may change who performs a task. It does not silently change who owns the responsibility.

| Operating concern | Institution-owned decision | Permitted delegated contribution |
| --- | --- | --- |
| Architecture | Approve environment, interfaces, security, resilience, and service boundary | Reference design, engineering analysis, and implementation support |
| Environments | Own or control approved cloud or hosting accounts and tenancy | Provisioning and administration under delegated access |
| CI/CD | Approve repository, pipeline, controls, promotion, and rollback | Pipeline implementation and release support |
| Production release | Decide whether and when a release enters production | Evidence preparation and execution of an approved release |
| Credentials | Approve issuance, storage, use, rotation, and revocation | Technical administration under logged access |
| Monitoring and incident response | Define service, escalation, evidence, and decision authority | Observability, alerting, investigation, and recovery support |
| Backup and recovery | Approve recovery objectives, retention, tests, and invocation authority | Operate backup and recovery procedures |
| Provider management | Select, contract, oversee, and exit providers | Supply technical and service evidence |
| Readiness | Decide whether the complete ceremony may proceed | Produce technical, operational, and provider evidence |

## Settlement Boundaries

The depository institution owns or establishes the applicable settlement account, provider relationship, participation, credentials, limits, routes, and execution authority. A regulated provider performs only the service accepted under its relationship with the institution.

Shared settlement infrastructure does not require shared software tenancy. Multiple institutions may ultimately address a common regulated provider while retaining separate deployments, records, approvals, credentials, accounts, reconciliation, and audit trails.

The legal account structure, attribution, ledger segregation, reconciliation, fund characterization, provider responsibility, and exception treatment must be explicit for each implementation. The Program does not infer them from connectivity.

## Deployment Model

The default model is a separate institution-controlled deployment.

```text
Institution-approved channels and government interfaces
                    ↓
Institution-controlled cloud or hosting account
                    ↓
Institution-specific x-change deployment and data
                    ↓
emi-core and institution-specific driver
                    ↓
Institution-approved API, credentials, and provider accounts
                    ↓
Institution settlement account and approved arrangement
```

The institution owns or controls, according to its approved architecture:

- cloud or hosting account and billing relationship;
- domains and network configuration;
- databases and institutional data;
- identity, access, encryption, and secrets;
- CI/CD, staging, production promotion, and rollback controls;
- logging, monitoring, evidence, and audit trail;
- backups, retention, recovery, and continuity tests;
- provider accounts, API credentials, certificates, and limits; and
- production authorization.

A DevOps provider may operate selected components through explicit, limited, logged, reviewable, and revocable authority. It does not own the environment or production decision.

## Institutional Sovereignty

> Technology can be shared without the institution becoming shared.

Common software does not create a common bank, government operating entity, customer base, beneficiary ledger, production account, credential store, release authority, or audit trail. The institution remains separately accountable for every responsibility it accepts.

## No-Fork Invariants

The Government Depository Program must not casually redefine:

- Funding Event;
- Treasury;
- Settlement Resources;
- Lien;
- Facility;
- Settlement Envelope;
- Pay Code;
- Execution Engine;
- Execution Driver;
- custody and public-authority boundaries;
- software ownership and licensing;
- settlement responsibility; or
- readiness as an institutional judgment.

If institution evidence appears to require a different canonical meaning, the work must stop at the conflict and identify whether an Editorial Decision Record is required.

## Architecture Review Package

Before an institution-specific design may proceed, the review package should establish:

1. applicable public and banking authority;
2. candidate workflow and public purpose;
3. parties, accountable owners, and approval boundaries;
4. funds, accounts, custody, and fund-characterization questions;
5. data sources, classifications, exchanges, retention, and records obligations;
6. channels, systems, APIs, providers, and known integration constraints;
7. deployment, CI/CD, credentials, monitoring, backup, and continuity boundaries;
8. driver discovery, mapping, certification, and maintenance responsibilities;
9. settlement, provider evidence, exceptions, and reconciliation model;
10. security, privacy, support, complaint, and incident responsibilities;
11. technical, operational, public-program, and production-readiness gates; and
12. unresolved matters that must remain Unknown or Institution-Provided.

The architecture review may conclude **Proceed to discovery**, **Proceed with stated constraints**, **Pause for evidence**, or **Deviation decision required**. It must not manufacture an institution-specific design from sector assumptions.
