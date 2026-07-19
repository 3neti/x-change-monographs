# Annex E — Publication Architecture

## Purpose

This annex defines the publication system through which Government Depository doctrine becomes an executive guide, controlled derivatives, evidence-led institution editions, commercial proposals, and reproducible submission portfolios.

It preserves the distinction between source and derivative, sector doctrine and institution evidence, editorial approval and commercial offer, and canonical publication and generated artifact.

## Canonical Publication Lineage

```text
Movement IV — Institutional Study and canonical doctrine
                         ↓
Government Depository Program foundation
                         ↓
Government Depository Program Guide
                         ↓
Approved Program derivatives and executive publications
                         ↓
Institution Intelligence
                         ↓
Strategic Gap Analysis and Editorial Mapping
                         ↓
Institution Edition
                         ↓
Commercial Proposal and Demonstration Materials
                         ↓
Submission Portfolio
                         ↓
Publication Freeze and explicit Version History
```

Each layer answers a different question. Later documents inherit from earlier ones; they do not silently replace them.

## Canonical Publications

### Movement IV — Institutional Study

Movement IV establishes the strategic doctrine: public trust, stewardship, institutional sovereignty, accountable execution, and the opportunity for capable depository institutions to participate more credibly in public finance.

It answers why the sector matters. It does not serve as a Program Guide, institution assessment, proposal, or implementation plan.

### Government Depository Program Foundation

The Program Foundation defines the sector field, purpose, target institutions, operating and commercial boundaries, publication grammar, adoption roadmap, parity position, and research gates.

Its specification, Compass, Roadmap, parity report, metadata, and supporting Annexes A–G form the governed Program source. They do not state what a named institution currently operates or intends.

### Government Depository Program Guide

The Guide translates the Program Foundation into the canonical EDR-005 Board-paper structure:

- Executive Summary;
- Section 1 — Why This Program?;
- Section 2 — What Is the Program?;
- Section 3 — Why Should the Institution Proceed?;
- Section 4 — How Does the Program Work?;
- Section 5 — Banking in Action;
- Section 6 — The Institutional Case;
- Section 7 — Launching the Program; and
- canonical Guide Appendices A–G.

The Guide explains the institutional proposition and implementation logic. It does not become a legal agreement, financial proposal, technical build specification, or proof of institution readiness.

## Supporting Program References

The Foundation Annexes provide architecture, stakeholder, workflow, responsibility, publication, research, and readiness depth. The Guide's canonical Appendices provide glossary, governance, Commercial Waterfall, Treasury grammar, deployment architecture, FAQ, and diagrams.

The two annex sets are complementary:

| Reference set | Function | Must not become |
| --- | --- | --- |
| Program Foundation Annexes A–G | Cross-publication institutional and implementation references | A replacement for the EDR-005 Guide appendices |
| Program Guide Appendices A–G | Canonical reader verification for terms, governance, economics, Treasury, deployment, FAQ, and diagrams | A second Program Foundation or technical manual |

## Derivative Publications

Derivatives compress or reframe approved canonical material for a specific decision. They must identify their source and may not become independent doctrine.

### Program Overview

Introduces the Program's purpose, audience, institutional boundaries, primary product, and intended outcomes. It should orient, not substitute for the Guide.

### Program in One Page

Provides a one-page decision map showing the institutional problem, proposed Capability, authority boundaries, representative ceremony, value case, and next step. Its brevity does not permit unqualified claims.

### Executive Summary or Board Brief

Supports readers who need the complete institutional decision in a short form. It must derive from a completed source and preserve material qualifications.

### Institutional Benefits

Explains the prospective value for eligible government depository institutions: reusable capability, stronger evidence, operating adaptability, government relationships, and conditional public-finance opportunity.

### Technical Overview

Explains canonical architecture, separate deployments, institution-controlled infrastructure, `emi-core`, driver discovery, provider boundaries, and readiness distinctions at an executive-technical level.

### Commercial Overview

Explains license, implementation, driver, maintenance, infrastructure, DevOps, provider, support, and internal cost categories without inventing pricing or guaranteed outcomes.

## Stakeholder Briefs

Stakeholder briefs adapt the same doctrine to the questions of a defined audience.

| Brief | Governing question |
| --- | --- |
| Board and executive brief | What institutional capability and responsibility is being considered? |
| Government entity or LGU brief | How could the arrangement support an authorized public workflow while preserving public control? |
| Treasury and finance brief | Where do funds, accounts, operational state, evidence, and reconciliation reside? |
| Operations brief | How will the complete ceremony be supervised, supported, and resolved? |
| Technology and DevOps brief | What must the institution own or control, and what may be delegated? |
| Risk, Compliance, Legal, and Security brief | Which authorities, controls, data, provider, and readiness questions require review? |
| Auditor and regulator brief | What evidence and responsibility boundaries remain available for independent examination? |
| Public-interest brief | How are accessibility, privacy, service quality, recourse, resilience, and accountability protected? |
| Investor or funding brief | How is sustainable capability financed without changing public or banking authority? |

A stakeholder brief may change emphasis. It may not change doctrine.

## Financial Briefs

Financial briefs explain economic questions without presenting unsupported assumptions as results.

They may address:

- the cost of repeated institution-specific engineering;
- software license, implementation, driver, infrastructure, DevOps, support, security, and provider costs;
- internal governance, operations, Treasury, Finance, reconciliation, and assurance effort;
- public-program administration and participant-support costs;
- service income or fee structures under actual authority and agreement;
- deposits and liquidity associated with actual program structures;
- recurring transaction activity;
- relationship and institutional value;
- scenario sensitivity and dependencies; and
- the Commercial Waterfall.

Every amount or scenario must identify its period, unit, source, assumption, scope, and approval status. A financial brief is not a price proposal unless it is explicitly governed as one.

## Executive Publications

Executive publications are accepted, typeset editions intended for formal circulation. Their source must be editorially approved and locked before publication production.

The publication system may later support an Executive Edition and an Institutional Reference Edition if editorial governance approves both purposes. Edition naming must describe reading purpose, not imply doctrinal supersession.

## Institution Intelligence and Institution Editions

Named-institution work begins with evidence, not adaptation.

Institution Intelligence records Observed, Inferred, Recommended, Unknown, and Institution-Provided material. Strategic Gap Analysis relates that evidence to the canonical Program. Editorial Mapping decides which claims, examples, ceremonies, priorities, and terminology may enter an Institution Edition.

An Institution Edition adapts the Program Guide to one institution. It may change emphasis, examples, sequencing, and institution-specific detail supported by evidence. It must not introduce new canonical architecture.

## Commercial Proposal

A proposal defines the proposed engagement: scope, deliverables, responsibilities, dependencies, exclusions, validity, commercial categories or prices, legal treatment, acceptance, and next decision.

It derives institutional context from approved research and editorial sources. It does not retroactively change them. A proposal is not an adoption record or production authorization.

## Demonstration and POC Materials

Demonstration credentials and controlled Proof-of-Concept materials support understanding and evaluation. They must identify their non-production status, source metadata, recipient or use context, and relationship to the proposal.

A demonstration proves only the behavior tested under defined conditions. It does not establish institutional readiness or public authority.

## Submission Portfolio

The Submission Portfolio packages approved artifacts for a defined recipient and purpose.

Its manifest should identify:

- Program and institution;
- recipient and submission purpose;
- artifact order and attachment relationship;
- source file, edition, version, and status;
- expected page count and checksum;
- screen or print profile;
- confidentiality and validity metadata where applicable;
- QR or demonstration verification where applicable; and
- output archive identity.

The existing manifest-driven submission builder should be reused. It should copy approved publications byte-for-byte, reject missing or mismatched inputs, create deterministic packages, verify extraction equivalence, and preserve frozen baselines.

## Source and Derivative Rules

1. Markdown and YAML remain canonical for editorial and governance sources.
2. PDFs, HTML, rendered diagrams, images, contact sheets, and ZIP files are generated artifacts.
3. A derivative must identify its governing source.
4. A shorter document may omit detail only when it preserves material qualifications and points to the source.
5. Institution-specific evidence must not be introduced into a sector source.
6. A commercial proposal must not become research evidence.
7. A generated artifact must not silently modify frozen wording.
8. Layout corrections belong to the renderer unless source correction is separately authorized.

## Publication States

| State | Meaning | Permitted action |
| --- | --- | --- |
| Draft | Content is being developed | Editorial work may continue |
| In Review | Content is complete enough for formal review | Corrections and approved refinement may proceed |
| Approved | Editorial authority accepts the content | Publication planning may begin |
| Locked | Canonical source is frozen for the edition | Only governed errata or later versioning may change it |
| Typesetting | Renderer is producing publication artifacts | No silent editorial change |
| Published | Accepted artifacts and metadata exist | Distribute according to approved purpose |
| Production Baseline | Version is immutable and reproducible | Future change requires a new version |
| Superseded | A later governed version replaces the artifact for its stated purpose | Preserve historical artifact and relationship |

Repository conventions prevail where a workstream uses more specific values. Metadata must never claim approval, lock, or publication that has not occurred.

## Publication and Freeze Package

An accepted publication should record:

- canonical title, edition, version, status, and audience;
- canonical Markdown and metadata paths;
- appendix and diagram sources;
- renderer and stylesheet;
- build command and dependency assumptions;
- output PDF, HTML, and other governed artifacts;
- page count, bookmarks, links, and accessibility capabilities;
- source and artifact SHA-256 checksums;
- page-by-page visual QA findings;
- acceptance and freeze record; and
- future versioning policy.

A frozen version must remain recoverable and reproducible. It must not be overwritten by a later refinement.

## Reuse Rule

The Government Depository workstream should reuse the established Program Guide house style, diagram pipeline, Submission Portfolio architecture, checksum practices, QA conventions, Institution Intelligence methodology, demonstration-credential grammar, and versioning patterns.

It must not copy institution-specific facts, claims, commercial terms, recipient data, or imagery from another banking track. Where the repository lacks a shared stakeholder-brief or financial-brief standard, that format should be governed once and reused rather than independently reinvented for each institution.
