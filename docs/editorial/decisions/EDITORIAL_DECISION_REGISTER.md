# Editorial Decision Register

## Status

Canonical

## Purpose

The Editorial Decision Register records accepted editorial and architectural decisions that govern the x-change publishing system.

Governance documents explain the current rules. This register records why those rules exist, what they affect, whether they remain active, and what is required to revise or supersede them.

The register preserves institutional memory. Editors, contributors, and AI agents must not reopen a settled question without identifying the governing decision and an explicit reason for reconsideration.

## Authority and Use

An accepted decision remains authoritative until explicitly superseded. Current governance documents should implement accepted decisions without duplicating their full history.

Codex and other contributors must consult this register before changing Program Guide structure, canonical terminology, or editorial workflow. If a current instruction conflicts with an accepted decision, the conflict must be reported rather than resolved silently.

## Status Model

| Status | Meaning |
| --- | --- |
| Proposed | The decision is under consideration and is not authoritative. |
| Accepted | The decision is approved and remains authoritative until explicitly superseded. |
| Superseded | A later accepted decision has replaced this decision. The replacement decision must be identified. |
| Rejected | The proposal was considered and not accepted. It remains recorded for institutional memory. |
| Deferred | Consideration has been postponed. The decision is not authoritative unless later accepted. |

Only these statuses may be used in this register.

## Required Decision Fields

Every decision entry must contain:

- Decision ID;
- Title;
- Status;
- Date;
- Context;
- Decision;
- Rationale;
- Consequences;
- Affected Documents;
- Supersedes;
- Superseded By; and
- Notes.

Decision IDs use the stable `EDR-NNN` sequence and are never reused.

## Register Governance

1. New decisions must be appended rather than introduced by silently rewriting historical entries.
2. Accepted decisions may be clarified without changing their substance.
3. A material change requires a new decision that identifies the earlier decision under `Supersedes`.
4. Rejected and deferred decisions remain recorded for institutional memory.
5. Every structural deviation from the Canonical Banking Program Guide must cite a decision ID.
6. Codex must consult this register before changing Program Guide structure, terminology, or editorial workflow.
7. If current instructions conflict with an accepted decision, Codex must flag the conflict rather than silently choose one.

A decision marked `Superseded` must identify its replacement under `Superseded By`. The replacement decision must identify the earlier decision under `Supersedes`.

## Existing Accepted Decision Records

The repository's earlier accepted decisions remain authoritative in their original files. They are not renumbered or duplicated in this register.

| Legacy decision | Status | Subject |
| --- | --- | --- |
| [0001 — Use Git as Publishing History](0001-use-git-as-publishing-history.md) | Accepted | Git as the canonical history of revisions, releases, and editorial change. |
| [0002 — Separate Author Manuscript, Editorial Manuscript, and Publication Master](0002-separate-author-manuscript-editorial-manuscript-and-publication-master.md) | Accepted | Separation of source, editorial, master, and released artifacts. |
| [0003 — Use Movements as Editorial Composition Units](0003-use-movements-as-editorial-composition-units.md) | Accepted | Movements as the primary unit of editorial composition and review. |

## Decision Index

| Decision ID | Title | Status | Date | Supersedes | Superseded By |
| --- | --- | --- | --- | --- | --- |
| [EDR-001](#edr-001--program-guides-are-canonical-commercial-specifications) | Program Guides Are Canonical Commercial Specifications | Accepted | 2026-07-16 | None | None |
| [EDR-002](#edr-002--executive-summaries-are-written-last) | Executive Summaries Are Written Last | Superseded | 2026-07-16 | None | EDR-012 |
| [EDR-003](#edr-003--program-guides-are-drafted-and-locked-by-section) | Program Guides Are Drafted and Locked by Section | Accepted | 2026-07-16 | None | EDR-012 (timing only) |
| [EDR-004](#edr-004--facilities-own-commercial-semantics) | Facilities Own Commercial Semantics | Accepted | 2026-07-16 | None | None |
| [EDR-005](#edr-005--the-canonical-banking-program-guide-architecture-is-frozen) | The Canonical Banking Program Guide Architecture Is Frozen | Accepted | 2026-07-16 | None | None |
| [EDR-006](#edr-006--program-guides-must-answer-executive-questions-directly) | Program Guides Must Answer Executive Questions Directly | Accepted | 2026-07-16 | None | None |
| [EDR-007](#edr-007--rbap-is-the-program-protagonist) | RBAP Is the Program Protagonist | Accepted | 2026-07-16 | None | None |
| [EDR-008](#edr-008--every-participating-bank-owns-its-digital-bank) | Every Participating Bank Owns Its Digital Bank | Accepted | 2026-07-16 | None | None |
| [EDR-009](#edr-009--funds-remain-under-bank-custody) | Funds Remain Under Bank Custody | Accepted | 2026-07-16 | None | None |
| [EDR-010](#edr-010--funding-event-is-the-entry-point-to-treasury) | Funding Event Is the Entry Point to Treasury | Accepted | 2026-07-16 | None | None |
| [EDR-011](#edr-011--section-6-is-the-institutional-case) | Section 6 Is the Institutional Case | Accepted | 2026-07-18 | None | None |
| [EDR-012](#edr-012--executive-summary-review-follows-the-frozen-narrative) | Executive Summary Review Follows the Frozen Narrative | Accepted | 2026-07-18 | EDR-002; EDR-003 (timing only) | None |

## EDR-001 — Program Guides Are Canonical Commercial Specifications

**Decision ID:** `EDR-001`

**Title:** Program Guides Are Canonical Commercial Specifications

**Status:** Accepted

**Date:** 2026-07-16

### Context

The editorial corpus contains documents serving different institutional purposes. Without explicit boundaries, thought leadership, program definition, implementation detail, operations, legal obligations, and negotiated commercial terms can drift into one another.

### Decision

A banking Program Guide is the canonical commercial specification and commercial handbook for a banking modernization program.

It explains what is being proposed, how participation works, the operating model, representative workflows, the business case, and the launch path.

It is distinct from:

- a white paper;
- a technical architecture;
- a deployment guide;
- a legal agreement; and
- a bank-specific proposal.

### Rationale

Clear document boundaries allow each artifact to answer its governing institutional question without absorbing responsibilities that belong elsewhere.

### Consequences

- White papers answer why institutions should modernize.
- Program Guides answer what is being proposed.
- Technical architecture answers how the platform is implemented.
- Deployment guides answer how it is operated.
- Legal agreements define obligations.
- Bank-specific proposals contain financial terms and negotiated considerations.

### Affected Documents

- [Canonical Banking Program Guide](../program-guides/CANONICAL_BANKING_PROGRAM_GUIDE.md)
- [Banking Program Guide Parity Checklist](../program-guides/PROGRAM_GUIDE_PARITY_CHECKLIST.md)
- All current and future banking-sector Program Guides

### Supersedes

None.

### Superseded By

None.

### Notes

Active. A material change to these document boundaries requires a superseding decision.

## EDR-002 — Executive Summaries Are Written Last

**Decision ID:** `EDR-002`

**Title:** Executive Summaries Are Written Last

**Status:** Superseded

**Date:** 2026-07-16

### Context

An Executive Summary placed before an unfinished guide can anticipate conclusions or introduce claims not yet established by the substantive sections.

### Decision

The Executive Summary of a Program Guide must be drafted only after all numbered sections and required appendices are substantively complete.

### Rationale

The Executive Summary must compress the completed guide. It must not invent, anticipate, or introduce claims that have not already been established elsewhere.

### Consequences

- Program Guide skeletons may contain an Executive Summary placeholder.
- The Executive Summary remains incomplete while substantive sections are incomplete.
- Publication review must confirm that every Executive Summary claim is supported elsewhere in the guide.

### Affected Documents

- [Canonical Banking Program Guide](../program-guides/CANONICAL_BANKING_PROGRAM_GUIDE.md)
- [RBAP Digital Banking Program Guide](../program-guides/rbap/rbap-digital-banking-program-guide.md)
- All future banking-sector Program Guides

### Supersedes

None.

### Superseded By

EDR-012.

### Notes

Superseded by EDR-012. The principle that the Executive Summary must compress established material remains active; the sequencing rule now distinguishes drafting and review from final lock.

## EDR-003 — Program Guides Are Drafted and Locked by Section

**Decision ID:** `EDR-003`

**Title:** Program Guides Are Drafted and Locked by Section

**Status:** Accepted

**Date:** 2026-07-16

### Context

Program Guides are long-lived institutional documents that may pass between editors, contributors, and AI agents. Drafting without durable section boundaries increases narrative drift, inconsistent terminology, repeated handovers, and costly rework.

### Decision

Program Guides are drafted one complete numbered section at a time. Each section is reviewed, accepted, persisted, and treated as locked before substantive drafting proceeds to the next section.

### Rationale

Section-level drafting protects continuity and allows each section to function as a self-contained executive briefing.

### Consequences

- Codex should persist one approved section per drafting cycle.
- Codex should not independently rewrite previously locked sections.
- Reopening a locked section requires an architectural change, a discovered contradiction, or an explicit editorial decision.
- Executive Summary timing follows EDR-012.

### Affected Documents

- [Canonical Banking Program Guide](../program-guides/CANONICAL_BANKING_PROGRAM_GUIDE.md)
- [Banking Program Guide Parity Checklist](../program-guides/PROGRAM_GUIDE_PARITY_CHECKLIST.md)
- Program Guide drafting and review workflows

### Supersedes

None.

### Superseded By

EDR-012, only as to Executive Summary timing.

### Notes

Active. Editorial acceptance should identify the section and persisted revision being locked.

## EDR-004 — Facilities Own Commercial Semantics

**Decision ID:** `EDR-004`

**Title:** Facilities Own Commercial Semantics

**Status:** Accepted

**Date:** 2026-07-16

### Context

Banking workflows require commercial meaning without fragmenting a universal execution credential into sector- or workflow-specific credential classes.

### Decision

Commercial meaning belongs to the Facility.

Pay Codes remain generic portable execution credentials and must not be divided into sector- or workflow-specific Pay Code types merely to express business meaning.

### Rationale

Specialized Pay Code classes would leak commercial semantics into a universal execution credential and create unnecessary architectural proliferation.

### Consequences

- Examples may include Deposit Facility, Payroll Facility, Disbursement Facility, Settlement Facility, Collateral Facility, and Receivable Facility.
- Do not introduce Deposit Pay Code, Payroll Pay Code, Merchant Pay Code, or similar specialized Pay Code classes without an explicit superseding decision.
- Settlement Envelopes own evidence and conditions.
- Treasury owns financial state.
- Execution Engines and Drivers own execution.

### Affected Documents

- [Canonical Banking Program Guide](../program-guides/CANONICAL_BANKING_PROGRAM_GUIDE.md)
- [RBAP Digital Banking Program Guide](../program-guides/rbap/rbap-digital-banking-program-guide.md)
- Future Treasury grammar, glossary, workflow, and technical-architecture documents

### Supersedes

None.

### Superseded By

None.

### Notes

Active. New Facility examples do not create new Pay Code classes.

## EDR-005 — The Canonical Banking Program Guide Architecture Is Frozen

**Decision ID:** `EDR-005`

**Title:** The Canonical Banking Program Guide Architecture Is Frozen

**Status:** Accepted

**Date:** 2026-07-16

### Context

Rural Banking, Thrift Banking, Government Depository Banking, and future sector guides require a stable structure if they are to remain comparable and reviewable as one editorial system.

### Decision

The approved Banking Program Guide architecture is frozen as the canonical cross-program structure.

It consists of:

- an unnumbered Executive Summary;
- Sections 1–7;
- Appendices A–G;
- Executive Questions;
- Key Messages;
- Executive Decisions;
- architectural parity controls;
- business-question completeness controls; and
- canonical diagram parity.

### Rationale

A stable architecture preserves cross-program comparability while allowing each sector to express its own motivation and institutional context.

### Consequences

- Sector narratives may adapt motivation, examples, regulatory context, and commercial emphasis.
- Mandatory coverage may not be silently omitted.
- Structural deviation requires an accepted editorial decision record.
- Missing canonical coverage must trigger the Agent Balk Rule.

### Affected Documents

- [Canonical Banking Program Guide](../program-guides/CANONICAL_BANKING_PROGRAM_GUIDE.md)
- [Banking Program Guide Parity Checklist](../program-guides/PROGRAM_GUIDE_PARITY_CHECKLIST.md)
- [RBAP Digital Banking Program Guide](../program-guides/rbap/rbap-digital-banking-program-guide.md)
- All future banking-sector Program Guides

### Supersedes

None.

### Superseded By

None.

### Notes

Active. Any structural deviation must cite an accepted decision in this register.

## EDR-006 — Program Guides Must Answer Executive Questions Directly

**Decision ID:** `EDR-006`

**Title:** Program Guides Must Answer Executive Questions Directly

**Status:** Accepted

**Date:** 2026-07-16

### Context

A complete heading structure can still leave the reader's central business questions unanswered.

### Decision

Every numbered Program Guide section must directly answer its approved Executive Question and support its stated Executive Decision.

### Rationale

Polished prose cannot compensate for an unanswered business question. The Program Guide exists to support institutional understanding and decisions, not merely to present elegant writing.

### Consequences

A section may be marked complete only when:

- the Executive Question is present;
- the Key Message remains aligned;
- the Executive Decision is stated;
- the narrative answers the question;
- the narrative supports the decision; and
- unsupported assumptions and approval dependencies are visible.

### Affected Documents

- [Canonical Banking Program Guide](../program-guides/CANONICAL_BANKING_PROGRAM_GUIDE.md)
- [Banking Program Guide Parity Checklist](../program-guides/PROGRAM_GUIDE_PARITY_CHECKLIST.md)
- All current and future banking-sector Program Guides

### Supersedes

None.

### Superseded By

None.

### Notes

Active. Business-question completeness and architectural completeness are separate review requirements.

## EDR-007 — RBAP Is the Program Protagonist

**Decision ID:** `EDR-007`

**Title:** RBAP Is the Program Protagonist

**Status:** Accepted

**Date:** 2026-07-16

### Context

The RBAP Digital Banking Program requires a clear institutional protagonist without implying that RBAP assumes regulated banking, settlement, switching, or shared production responsibilities.

### Decision

The RBAP Digital Banking Program Guide must present RBAP as the sponsor, convenor, ecosystem steward, and program administrator.

RBAP must not be represented as:

- a bank;
- a settlement institution;
- a payment switch;
- a payment rail;
- a shared production operator; or
- a BancNet equivalent.

### Rationale

The Program is intended to enable collective modernization while preserving the independent authority and operations of participating rural banks.

### Consequences

- ODTI licenses and maintains the software.
- Participating rural banks own their production environments and customer relationships.
- Settlement institutions provide regulated accounts, rails, and APIs.
- DevOps providers operate only within delegated authority.
- RBAP may participate commercially through the Program and Commercial Waterfall without becoming a settlement operator.

### Affected Documents

- [RBAP Digital Banking Program Guide](../program-guides/rbap/rbap-digital-banking-program-guide.md)
- [RBAP Program Guide metadata](../program-guides/rbap/metadata.yaml)
- RBAP Program Guide drafting, review, and publication workflows

### Supersedes

None.

### Superseded By

None.

### Notes

Active. The listed role boundaries are editorial and architectural controls; applicable legal characterization remains subject to agreement and qualified review.

## EDR-008 — Every Participating Bank Owns Its Digital Bank

**Decision ID:** `EDR-008`

**Title:** Every Participating Bank Owns Its Digital Bank

**Status:** Accepted

**Date:** 2026-07-16

### Context

Collective modernization requires common software without common production tenancy or the surrender of institutional sovereignty.

### Decision

Each participating bank owns or controls its own:

- cloud account;
- domain;
- deployment;
- database;
- customer data;
- credentials;
- settlement account;
- provider API credentials;
- release approvals;
- backups;
- monitoring;
- security policy; and
- operating authority.

### Rationale

Common software must not require common production operations or the surrender of institutional sovereignty.

### Consequences

- ODTI provides licensed software and maintained releases.
- RBAP allocates or administers participation under the group program.
- DevOps providers operate but do not own the bank's infrastructure or data.
- There is no requirement for one common RBAP redemption website or one shared production database.
- A future federated discovery or routing layer remains separate future work unless explicitly approved.

### Affected Documents

- [Canonical Banking Program Guide](../program-guides/CANONICAL_BANKING_PROGRAM_GUIDE.md)
- [RBAP Digital Banking Program Guide](../program-guides/rbap/rbap-digital-banking-program-guide.md)
- Deployment Architecture appendix and future deployment guides

### Supersedes

None.

### Superseded By

None.

### Notes

Active. Shared settlement arrangements do not imply shared software tenancy.

## EDR-009 — Funds Remain Under Bank Custody

**Decision ID:** `EDR-009`

**Title:** Funds Remain Under Bank Custody

**Status:** Accepted

**Date:** 2026-07-16

### Context

Editorial language must distinguish regulated deposits and bank-held funds from instructions, evidence, reservations, and execution orchestration.

### Decision

x-change must not be described as receiving deposits, holding customer funds, issuing a wallet balance, or creating stored value.

The participating regulated bank remains custodian of the underlying funds and owner of the customer and deposit relationship.

x-change orchestrates authorized settlement under the bank's policies and authority.

### Rationale

Clear custody language protects the architectural distinction between regulated financial relationships and the software that coordinates authorized execution.

### Consequences

Preferred external language includes:

- bank-held funds;
- Settlement Resources;
- Treasury Inventory;
- Reservation;
- Allocation;
- available settlement authority;
- funded Facility; and
- authorized settlement instruction.

Avoid public-facing terms such as:

- x-change wallet;
- x-change balance;
- top-up;
- stored value; and
- deposit into x-change.

### Affected Documents

- [Canonical Banking Program Guide](../program-guides/CANONICAL_BANKING_PROGRAM_GUIDE.md)
- [RBAP Digital Banking Program Guide](../program-guides/rbap/rbap-digital-banking-program-guide.md)
- Banking-sector white papers, Program Guides, diagrams, glossaries, and commercial materials

### Supersedes

None.

### Superseded By

None.

### Notes

Active. This is an architectural and editorial rule, not a legal conclusion. Final legal and regulatory characterization remains subject to applicable law, agreements, and qualified counsel.

## EDR-010 — Funding Event Is the Entry Point to Treasury

**Decision ID:** `EDR-010`

**Title:** Funding Event Is the Entry Point to Treasury

**Status:** Accepted

**Date:** 2026-07-16

### Context

The Treasury grammar previously began with Inventory but did not explicitly explain the external event through which Inventory increased.

### Decision

A Funding Event represents the external financial event through which Settlement Resources enter or become recognized by Treasury.

### Rationale

Naming the Funding Event makes the entry point to Treasury explicit without assigning custody or commercial meaning to the execution credential.

### Consequences

Potential Funding Events may include:

- teller cash receipt;
- bank transfer;
- payroll funding;
- remittance funding;
- loan proceeds;
- government funding;
- merchant settlement; and
- receivable liquidation.

### Affected Documents

- [Canonical Banking Program Guide](../program-guides/CANONICAL_BANKING_PROGRAM_GUIDE.md)
- [RBAP Digital Banking Program Guide](../program-guides/rbap/rbap-digital-banking-program-guide.md)
- Future Treasury grammar, workflow, diagram, and technical-architecture documents

### Supersedes

None.

### Superseded By

None.

### Notes

Active. The precise effect of different Funding Events on Inventory, Reservations, and Allocations remains subject to further Treasury design.

## EDR-011 — Section 6 Is the Institutional Case

**Decision ID:** `EDR-011`

**Title:** Section 6 Is the Institutional Case

**Status:** Accepted

**Date:** 2026-07-18

### Context

The completed RBAP Section 6 evaluates what participation could enable the institution to become over time. Commercial sustainability remains necessary, but it supports a broader argument about banking relationships, adaptability, community service, collective modernization, and Board responsibility. The earlier title, **The Business Case**, implied a narrower emphasis than the chapter now carries.

### Decision

The canonical title of Section 6 is **The Institutional Case**.

Its governing cross-program question is:

> What kind of institution can participation help the bank become?

Section 6 must continue to address the business case, costs of participation, revenue or economic opportunities, and the Commercial Waterfall. Those mandatory coverage categories support the institutional case and are not removed or transferred by this title change.

### Rationale

Program participation is an institutional decision before it is a calculation of commercial return. The revised title accurately reflects the chapter's purpose while preserving the economic discipline required for an informed decision.

### Consequences

- Current and future banking Program Guides use **Section 6 — The Institutional Case**.
- Sector-specific Executive Questions may adapt the canonical question without narrowing the chapter to financial return alone.
- Commercial sustainability remains a required part of Section 6.
- Mandatory coverage categories 18–21 remain unchanged.
- The RBAP Section 6 may be locked under the revised canonical title.

### Affected Documents

- [Canonical Banking Program Guide](../program-guides/CANONICAL_BANKING_PROGRAM_GUIDE.md)
- [Banking Program Guide Parity Checklist](../program-guides/PROGRAM_GUIDE_PARITY_CHECKLIST.md)
- [RBAP Digital Banking Program Guide](../program-guides/rbap/rbap-digital-banking-program-guide.md)
- All future banking-sector Program Guides

### Supersedes

None.

### Superseded By

None.

### Notes

Active. This is the accepted editorial record required by EDR-005 for the canonical Section 6 refinement. It changes the Section 6 title and governing question only; the remaining canonical architecture and mandatory coverage register remain frozen.

## EDR-012 — Executive Summary Review Follows the Frozen Narrative

**Decision ID:** `EDR-012`

**Title:** Executive Summary Review Follows the Frozen Narrative

**Status:** Accepted

**Date:** 2026-07-18

### Context

EDR-002 required both the numbered sections and required appendices to be substantively complete before the Executive Summary could be drafted. The RBAP Program Guide has now frozen Sections 1–7 as its canonical narrative while its appendices and diagrams remain planned. Editorial review benefits from synthesizing that frozen narrative before supporting appendices are completed, provided the Summary is not treated as final and does not anticipate unfinished material.

### Decision

An Executive Summary may be drafted and reviewed after all numbered sections are editorially complete and frozen, even when required appendices remain incomplete.

The Executive Summary must:

- rely only on claims established in the frozen numbered sections;
- introduce no concepts from incomplete appendices or diagrams;
- remain **In Review** while any required appendix is incomplete; and
- be revalidated and locked only after all required appendices are substantively complete.

### Rationale

The numbered sections contain the canonical narrative that the Executive Summary must compress. Separating initial synthesis from final lock allows editorial review to proceed without treating incomplete supporting material as settled or publishable.

### Consequences

- The Executive Summary follows the frozen numbered narrative.
- Appendices and diagrams may be completed after the Summary enters review.
- Completion of the appendices triggers a final claim, terminology, and cross-reference review of the Summary.
- Publication review must reject an Executive Summary that is locked before this revalidation occurs.

### Affected Documents

- [Canonical Banking Program Guide](../program-guides/CANONICAL_BANKING_PROGRAM_GUIDE.md)
- [Banking Program Guide Parity Checklist](../program-guides/PROGRAM_GUIDE_PARITY_CHECKLIST.md)
- [RBAP Digital Banking Program Guide](../program-guides/rbap/rbap-digital-banking-program-guide.md)
- All current and future banking-sector Program Guides

### Supersedes

EDR-002 in full and EDR-003 only as to Executive Summary timing.

### Superseded By

None.

### Notes

Active. This decision changes workflow timing only. It does not alter the canonical section architecture, required appendix coverage, or the rule that an Executive Summary must introduce no new claims.
