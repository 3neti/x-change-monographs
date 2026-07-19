# Government Depository Digital Banking Program Roadmap

## Purpose

This Roadmap moves the Program from an accepted sector foundation to reproducible publications and, only after evidence, institution-specific implementation. It is a governance sequence rather than a calendar commitment.

## Roadmap Principles

1. Reuse canonical architecture and publishing infrastructure before creating a new component.
2. Complete sector doctrine and Program documentation before tailoring an institution.
3. Write the formal Program Guide one approved section at a time.
4. Derive executive and commercial materials from canonical sources.
5. Begin named-institution work with evidence, not manuscript writing.
6. Keep technical certification, operational readiness, and production approval distinct.
7. Freeze accepted versions and preserve reproducibility.

## Phase Summary

| Phase | Objective | Relative effort | Current status |
| --- | --- | --- | --- |
| 1 — Program Foundation | Establish the governable sector Program | Moderate | Approved |
| 2 — Program Publication Layer | Create and publish the formal Program Guide and core derivatives | Substantial | In progress — Guide draft complete for review |
| 3 — Stakeholder and Financial Layer | Provide evidence-led audience-specific decision material | Moderate to substantial | Planned |
| 4 — Executive Publication Layer | Prepare controlled executive and commercial publication forms | Moderate | Planned |
| 5 — Submission Architecture | Integrate deterministic institution selection and packaging | Small to moderate | Planned |
| 6 — Institution-Specific Programs | Apply the Program to researched institutions | Substantial per institution | Deferred pending research |

## Phase 1 — Program Foundation

### Objective

Define Government Depository Banking as a first-class sector Program without creating a second x-change architecture or making unsupported claims about a named institution.

### Deliverables

- canonical Program specification;
- documentation parity report;
- maintainable Program Compass;
- phased Roadmap;
- complete foundation Annexes A–G;
- Program metadata and README; and
- repository navigation.

### Acceptance gate

- all required sections and annexes are complete;
- internal links and Markdown structure validate;
- Movement IV and other frozen baselines remain unchanged;
- the formal Program Guide remains a separately governed future layer;
- architectural divergence review finds no unapproved fork; and
- Philippine Veterans Bank work remains explicitly deferred.

## Phase 2 — Program Publication Layer

### Objective

Create the canonical Government Depository Program Guide and the controlled derivatives needed to explain it consistently.

### Deliverables

- Program Overview;
- Program in One Page;
- formal Program Guide implementing Executive Summary, Sections 1–7, and Appendices A–G;
- Institutional Benefits;
- Technical Overview;
- Commercial Overview without unsupported institution pricing;
- canonical diagrams and placeholder-to-figure governance where required;
- publication metadata and navigation;
- publication renderer configuration reusing the established house style;
- PDF and HTML only after editorial authorization;
- page-by-page QA, checksums, acceptance record, freeze record, and version history.

### Sequence

1. Persist the formal Guide skeleton from the frozen canonical architecture.
2. Draft Sections 1–7 and place them under editorial review.
3. Complete the Guide's own Appendices A–G and all 27 mandatory coverage categories.
4. Draft the Executive Summary from the complete Guide.
5. Run cross-corpus doctrine, architecture, and parity review.
6. Derive the shorter publication forms.
7. Typeset only the accepted canonical sources.

### Acceptance gate

The Program Guide parity checklist is complete, any `Not Applicable` item is explained, any deviation has an EDR, and the accepted edition is reproducible from frozen source.

## Phase 3 — Stakeholder and Financial Layer

### Objective

Translate the approved Program into audience-specific decision material without changing doctrine or introducing speculative economics.

### Deliverables

- government-depository-institution brief;
- government-agency and LGU brief;
- public-interest brief;
- regulator and auditor brief;
- DevOps and technology-partner brief;
- investor or capital-provider brief where appropriate;
- financial briefs covering institution economics, workflow economics, cost categories, and scenario boundaries; and
- shared stakeholder and financial-brief standards if the repository still lacks them.

### Evidence rules

- distinguish sector logic from institution evidence;
- make all volume, deposit, revenue, cost, fee, and return assumptions visible;
- do not imply selection, eligibility, authority, or guaranteed economic results; and
- preserve the Commercial Waterfall and responsibility boundaries.

### Acceptance gate

Every claim traces to an approved Program source or identified evidence. The new formats are reusable across institutions and do not become Government Depository-only publishing infrastructure without reason.

## Phase 4 — Executive Publication Layer

### Objective

Prepare reusable, restrained publication forms for an authorized institution dialogue.

### Deliverables

- canonical Government Depository cover-letter template;
- provisional-license and proof-of-concept proposal template;
- demonstration-credential integration using the frozen credential grammar;
- executive portfolio structure;
- proposal and attachment relationship rules; and
- approval, confidentiality, validity, signature, and attachment metadata conventions.

### Acceptance gate

Templates contain no named-institution facts, prices, commitments, or legal conclusions. Any instance requires authorized institution evidence and engagement decisions.

## Phase 5 — Submission Architecture

### Objective

Integrate the Program with the existing metadata-driven Submission Portfolio system without duplicating the AllBank builder.

### Target interface

```text
publish:submission
    --program=government-depository
    --institution=<institution-slug>
```

The actual interface may follow repository conventions and need not use this exact command name.

### Deliverables

- Program and institution metadata mapping;
- reuse or generalization of the existing builder;
- deterministic artifact selection and ordering;
- manifest and attachment validation;
- checksums and source-to-artifact traceability;
- explicit draft, review, approved, submitted, and frozen states where applicable; and
- preservation of prior frozen portfolios.

### Acceptance gate

The builder rejects missing, stale, mismatched, or unapproved inputs; reproduces identical packages from identical frozen sources; and leaves the AllBank v1.0 baseline unchanged.

## Phase 6 — Institution-Specific Programs

### Objective

Apply canonical doctrine to a real institution through evidence-led research, assessment, editorial mapping, and authorized engagement.

### First expected institution

**Philippine Veterans Bank**, beginning only with a separately authorized Institution Intelligence workstream.

### Later candidates

- Al-Amanah Islamic Investment Bank of the Philippines;
- other institutions eligible under applicable government-depository authority; and
- selected government-owned banks where the Program is relevant and an authorized research question exists.

The candidate list is not an assertion of readiness, interest, qualification, or selection.

### Required sequence

```text
Research authorization
        ↓
Institution Intelligence
        ↓
Strategic Gap Analysis
        ↓
Editorial Mapping
        ↓
Institution Edition
        ↓
Commercial Proposal
        ↓
Demonstration or POC Package
        ↓
Submission Portfolio
        ↓
Institutional readiness and implementation decisions
```

### Acceptance gate

The applicable requirements in [Annex F](annexes/institution-specific-research-gate.md) and [Annex G](annexes/definition-of-institution-readiness.md) are satisfied. Unknowns remain visible. Canonical doctrine remains unchanged unless an explicit EDR authorizes a change.

## Dependencies and Decision Points

| Decision | Dependency | Consequence if unmet |
| --- | --- | --- |
| Accept Phase 1 foundation | Scope, link, no-fork, and frozen-asset verification | Do not begin the formal Guide |
| Begin Program Guide | EDR-005 architecture and approved editorial workflow | Do not draft derivatives as substitutes |
| Publish first Program edition | Locked source, complete parity, renderer QA, metadata, and freeze approval | Do not generate a canonical publication |
| Create stakeholder or financial brief | Approved source and reusable format | Report the format gap; do not improvise claims |
| Instantiate executive template | Authorized institution and engagement context | Keep templates generic |
| Generate submission portfolio | Approved artifacts and valid metadata | Builder must balk |
| Begin PVB edition or proposal | Research gate and editorial mapping | Continue research or explicitly pause |

## Roadmap Completion

The Program is not complete merely because Phase 1 exists. It becomes a publishing peer of the Thrift Bank track when the formal Guide, derivative family, executive layer, deterministic submission integration, freeze governance, and at least one evidence-led institution implementation chain have been completed without architectural divergence.
