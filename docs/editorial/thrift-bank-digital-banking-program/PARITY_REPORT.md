# Thrift Bank Digital Banking Program

## Parity Report

### Status

Complete — Phase 1 editorial parity review

## Review Scope

This report compares the Phase 1 institutional study against:

- *Movement III — Modernizing Philippine Thrift Banks for the Digital Economy*;
- the *RBAP Digital Banking Program Guide*;
- the Canonical Banking Program Guide governance boundary; and
- the frozen propositions in `CANONICAL_THESIS.md`.

The review tests conceptual continuity and required institutional differences. It does not certify technical implementation, legal sufficiency, commercial terms, or production readiness.

## Artifact Classification

The Phase 1 package is an institution-centric editorial study and source manuscript. It is not the formal Thrift Bank Digital Banking Program Guide implementation.

This distinction is required because EDR-005 freezes the actual Banking Program Guide architecture at an Executive Summary, Sections 1–7, and Appendices A–G. The Phase 1 assignment deliberately uses an eleven-part institutional-study architecture and a separate repository location.

No structural deviation from EDR-005 is claimed. The formal Thrift Bank Program Guide remains anticipated and must implement the frozen architecture unless a future accepted editorial decision authorizes a deviation.

## Required Assignment Parity

| Requirement | Status | Finding |
| --- | --- | --- |
| Institution-centric | Complete | The manuscript concerns one thrift bank, its Board, its executive management, and its institutional operating capability. |
| Removes RBAP governance | Complete | RBAP sponsorship, administration, license seats, member-bank governance, and program-level authority are absent. |
| Removes collective modernization | Complete | The central proposition is one institution establishing a reusable operating foundation, not many banks modernizing together. |
| Preserves banking authority | Complete | The bank’s license, policy, production authority, product authority, and settlement authority remain explicit. |
| Preserves customer ownership | Complete | The bank remains owner of the customer and deposit relationship; x-change is not another customer channel or intermediary. |
| Preserves settlement ownership | Complete | The bank brings or establishes its own settlement accounts, arrangements, credentials, and execution authority. |
| Introduces the bank-specific driver | Complete | `3neti/emi-{bank}` is defined as the maintained institution-specific implementation of the `emi-core` contract. |
| Distinguishes settlement connectivity from banking capability | Complete | Connectivity is treated as necessary execution capability; governed banking service includes purpose, policy, authority, readiness, evidence, support, exceptions, and reconciliation. |

## Movement III Reconciliation

| Movement III proposition | Phase 1 treatment | Status |
| --- | --- | --- |
| The thrift bank remains the protagonist | Preserved as the first immutable proposition and the manuscript’s governing perspective. | Aligned |
| Modernization is institutional strategy | Preserved through the Board-level institutional question and ten-year capability horizon. | Aligned |
| Common software can support independent institutions | Preserved as maintained software and reusable engineering within one bank’s sovereign operation. | Aligned |
| Existing institutional capability should not be diminished | Strengthened by presuming existing IT, channels, settlement accounts, ACH participation, and operations personnel. | Aligned |
| Regulated settlement roles must remain distinct | Preserved, but the assumption of an external initial settlement partner is removed. | Corrected for institution-centric scope |
| Modularity supports controlled adoption | Preserved through one bounded ceremony and evidence-based expansion. | Aligned |
| Future readiness means continued freedom to decide | Preserved in the ten-year institutional horizon. | Aligned |
| Technology should adapt to institutions and people | Preserved through the bank-first and customer-outcome framing. | Aligned |

## RBAP Program Guide Reconciliation

### Concepts preserved

The Phase 1 manuscript preserves the RBAP Guide’s stable institutional grammar:

- the customer requests a banking outcome and the bank arranges it;
- the banking service is the product;
- the Pay Code is the credential;
- Funding Events enter or become recognized by Treasury;
- Treasury maintains operational financial state;
- Liens reserve Settlement Resources;
- Facilities own commercial meaning;
- Settlement Envelopes own evidence and readiness conditions;
- Execution coordinates the authorized outcome;
- funds remain under bank custody;
- readiness is an institutional judgment;
- remittance is the canonical explanatory ceremony;
- Transaction Gravity concerns recurring institutional relevance; and
- resilience and adaptability remain distinct.

### Concepts removed or recast

| RBAP Guide concept | Phase 1 treatment | Reason |
| --- | --- | --- |
| RBAP as sponsor and administrator | Removed | The study concerns one institution. |
| Member banks | Removed | There is no multi-bank membership model. |
| Group license and license seats | Removed | No sector-level participation model is being proposed. |
| Common program governance | Recast as bank governance | Authority resides in the institution’s Board, management, and responsible functions. |
| NetBank as initial settlement institution | Removed | A thrift bank may already possess or establish its own settlement capability. |
| Common settlement arrangement | Removed | The bank uses its own approved accounts, credentials, and arrangements. |
| Collective rollout | Recast as controlled institutional adoption | Expansion occurs within the bank according to evidence and readiness. |
| Shared infrastructure as a sector program | Narrowed to shared engineering | Shared software and patterns do not imply shared funds, accounts, authority, balances, or production tenancy. |

## Settlement Thesis Review

The corrected thesis is present throughout the package:

> The bank brings the authority and the rails.
>
> x-change brings the operating grammar.
>
> The bank-specific driver connects them.

The manuscript does not state or imply that:

- x-change grants access to InstaPay or PESONet;
- NetBank is required;
- a thrift bank lacks settlement accounts or ACH participation;
- settlement connectivity is the same as customer-facing banking capability; or
- an integration test establishes institutional readiness.

## Shared-Infrastructure Boundary Review

The phrase **shared infrastructure** is constrained to maintained software, orchestration, engineering, integration patterns, deployment automation, testing, observability, documentation, and reusable banking grammar.

The package expressly excludes pooled funds, pooled settlement, shared banking authority, shared production accounts, shared customer balances, common production credentials, a common customer database, and a shared institutional audit trail.

Status: **Aligned**.

## Bank-Specific Driver Review

The package establishes:

- `emi-core` as the common maintained execution-integration contract;
- `3neti/emi-{bank}` as the institution-specific implementation;
- the bank as owner of the settlement relationship, credentials, production authority, and release decision;
- ODTI as developer and maintainer of the driver within agreed scope;
- the bank’s technology and control functions as participants in discovery, review, certification, and change governance; and
- driver certification as evidence of technical capability, not production readiness.

The lifecycle is documented as:

```text
Discovery
    ↓
Mapping
    ↓
Implementation
    ↓
Certification
    ↓
Maintenance
    ↓
Version Evolution
```

Status: **Complete for Phase 1 architecture**.

## Canonical Terminology Review

| Term | Review result |
| --- | --- |
| Funding Event | Used as the external event through which Settlement Resources enter or become recognized by Treasury. |
| Treasury | Used as the bank’s operational view of Settlement Resources, not as the bank account itself. |
| Lien | Used as the operational reservation for an authorized purpose. |
| Facility | Owns banking purpose, policy, participants, and commercial meaning. |
| Settlement Envelope | Owns evidence and conditions required before execution. |
| Pay Code | Remains a generic execution credential; no workflow-specific Pay Code classes are introduced. |
| Execution | Coordinates the authorized outcome through the bank’s approved settlement capability. |
| Custody | Remains with the regulated bank; no x-change wallet, balance, deposit, or stored-value claim is introduced. |

Status: **Aligned**.

## Business-Question Review

The Phase 1 manuscript answers the questions appropriate to an institutional study:

1. What is the institutional question?
2. What is the Program?
3. Why might it matter to the bank?
4. Which authority and relationships remain with the bank?
5. How does existing settlement capability become governed banking service?
6. How can one grammar support different services?
7. What does the operating model look like in action?
8. How can recurring usefulness deepen institutional relevance?
9. Who owns and governs each responsibility?
10. How does the bank determine readiness and adopt in controlled steps?
11. What capability should the institution preserve over the next decade?

Status: **Complete for Phase 1 editorial review**.

## Formal Program Guide Parity

The formal Thrift Bank Digital Banking Program Guide remains **Planned**.

This Phase 1 package does not satisfy or attempt to satisfy the Canonical Banking Program Guide’s formal structural parity because it is not that artifact. Before a formal Program Guide is described as created, editorial work must:

1. implement the frozen Executive Summary, Sections 1–7, and Appendices A–G architecture;
2. map the institution-centric thesis into all 27 mandatory coverage categories;
3. include the required Executive Question, Key Message, and Executive Decision for every numbered section;
4. establish the appropriate licensing or participation model, governance, costs, economic opportunities, and Commercial Waterfall from approved source material;
5. reserve and complete the required appendices; and
6. update the cross-program parity matrix as drafting proceeds.

No missing formal-guide coverage has been disguised with prose. The future guide remains a separate editorial task.

## Parity Decision

The Phase 1 package is internally consistent with Movement III and the stable banking grammar of the RBAP Program Guide while making the required institution-specific corrections.

It is ready for editorial review as a canonical study and source manuscript.

It is not yet a formal Banking Program Guide, legal proposal, commercial proposal, technical implementation specification, or publication master.
