# Annex A — Program Architecture Map

## Purpose

This map locates the Government Depository Digital Banking Program within the canonical x-change architecture. It is a governance map, not a deployment diagram and not an institution-specific design.

## Architectural Lineage

```text
Canonical x-change doctrine and Treasury grammar
                    ↓
Government Depository Digital Banking Program
                    ↓
Formal Government Depository Program Guide
                    ↓
Institution Intelligence and Strategic Gap Analysis
                    ↓
Institution Edition
                    ↓
Commercial Proposal and Implementation
```

The sector Program applies existing doctrine to public-finance responsibilities. It does not create a parallel product architecture.

## Program Layers

| Layer | Institutional purpose | Authority and ownership boundary |
| --- | --- | --- |
| Government authority | Defines lawful purpose, appropriation or program authority, eligible participants, conditions, approvals, reporting, and public accountability | Remains with the authorized public institution and responsible officials |
| Depository institution | Provides the lawful banking service, holds or administers accounts as authorized, approves operations, manages institutional risk, and remains responsible for its customers and government relationships | Remains with the participating institution |
| x-change operating grammar | Represents governed funding, service, settlement, credential, execution, and evidence relationships through maintained licensed software | Does not confer authority, take custody, or become the bank |
| Institution-specific driver | Connects the canonical execution model to the institution's approved systems and providers | Requires discovery, mapping, implementation, certification, and continuing maintenance for that institution |
| Settlement and service providers | Perform the regulated or contracted function for which they are engaged | Do not inherit the institution's public mandate or decision authority |
| Evidence and reconciliation | Return execution results to the responsible institutions for accounting, exception handling, oversight, and audit | Remains governed by applicable institutional, legal, records, and audit requirements |

## Canonical Operating Chain

```text
Public authority and institutional instruction
                    ↓
Funding Event
                    ↓
Treasury and Lien
                    ↓
Facility
                    ↓
Settlement Envelope
                    ↓
Pay Code or approved presentation
                    ↓
Execution Engine and institution-specific driver
                    ↓
Approved settlement or service provider
                    ↓
Evidence, reconciliation, exception handling, and audit
```

The chain expresses responsibility and state. It does not imply that x-change holds funds, grants banking authority, supplies settlement access, or makes a public-policy decision.

## Institutional Sovereignty

Common licensed software does not create a common bank or a common government operating entity. Each participating institution may retain its own deployment, records, credentials, release controls, approvals, audit trail, provider relationships, settlement relationships, and production decision. Shared settlement infrastructure, where lawfully used, does not require shared software tenancy.

## No-Fork Invariants

The Government Depository Program must not casually redefine:

- Funding Event;
- Treasury;
- Lien;
- Facility;
- Settlement Envelope;
- Pay Code;
- Execution Engine;
- Execution Driver;
- custody and authority boundaries;
- settlement responsibility;
- software ownership; or
- institutional readiness.

A public voucher, claim stub, reference number, or other approved presentation may carry or resolve to a Pay Code. It does not replace the Pay Code's canonical role as the credential to a governed banking service.

## Architecture Review Gate

An institution-specific architecture may proceed only after the proposed workflow, authorities, participants, accounts, funds, data, systems, providers, evidence, reconciliation, security, continuity, and operating owners are known. Any proposed departure from the canonical invariants requires an explicit Editorial Decision Record before it enters a canonical publication.
