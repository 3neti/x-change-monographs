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
| [EDR-013](#edr-013--institutional-reference-edition) | Institutional Reference Edition | Accepted | 2026-07-18 | None | None |
| [EDR-014](#edr-014--institution-intelligence-framework-is-canonical) | Institution Intelligence Framework Is Canonical | Accepted | 2026-07-18 | None | None |
| [EDR-015](#edr-015--institution-intelligence-framework-final-lock-and-allbank-phase-1-authorization) | Institution Intelligence Framework Final Lock and AllBank Phase 1 Authorization | Accepted | 2026-07-18 | None | None |

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

On 18 July 2026, the Editorial Board accepted the [Thrift Bank Digital Banking Program Guide](../program-guides/thrift-bank/thrift-bank-program-guide.md) as the canonical implementation guide for the thrift-bank track. Its [Editorial Acceptance](../program-guides/thrift-bank/EDITORIAL_ACCEPTANCE.md) records the completed lock, frozen doctrine, canonical document hierarchy, and institution-specific-edition rule. This acceptance completes the thrift-bank implementation of EDR-005; it does not alter the cross-program architecture established by this decision.

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

The RBAP Executive Summary completed EDR-012 revalidation on 18 July 2026 after Appendices A–G were locked. The review reached Outcome A: no wording changes were required. The Executive Summary is canonical and locked. This implementation record does not authorize a separate Executive Edition, a two-edition publication model, or final publication rendering.

## EDR-013 — Institutional Reference Edition

**Decision ID:** `EDR-013`

**Title:** Institutional Reference Edition

**Status:** Accepted

**Date:** 2026-07-18

### Context

The published First Edition of the Thrift Bank Digital Banking Program Guide is editorially, architecturally, and canonically correct. It functions well as a concise Board paper. Comparison with the RBAP Digital Banking Program Guide nevertheless showed a material difference in explanatory depth, institutional reasoning, governance discussion, operational walkthroughs, and implementation guidance.

The difference did not indicate an error in the First Edition. It identified a second legitimate reading need: a comprehensive institutional implementation reference that rewards closer study by executive sponsors and responsible bank functions. The resulting Expanded Edition has completed editorial review.

### Decision

The First Edition must remain unchanged and valid as published.

A separate edition was authorized and developed under the working name **Expanded Edition**. It inherits the frozen doctrine, architecture, institutional boundaries, operating grammar, Treasury grammar, Transaction Gravity, readiness doctrine, and driver lifecycle from the accepted thrift-bank sources.

That manuscript is accepted and locked as the canonical **Institutional Reference Edition**, First Edition, Version 1.0.

The existing concise publication is named the canonical **Executive Edition**, First Edition, Version 1.0. It remains unchanged.

Neither edition supersedes the other. Both derive from the same frozen Institutional Study and Program Guide doctrine. The Executive Edition serves Board and executive decision-making. The Institutional Reference Edition serves executive leadership and the responsible technology, Operations, Treasury, Risk, Compliance, implementation, and partner functions.

### Rationale

Different executive and implementation contexts require different depths of explanation. Preserving two editions allows the publishing system to serve both needs without weakening the First Edition through retrospective expansion or treating length as a correction to settled doctrine.

Parity is measured by institutional maturity and the business questions answered, not by matching RBAP wording, headings, page count, or word count.

### Consequences

- The locked First Edition manuscript and publication artifacts remain unchanged.
- The Institutional Reference Edition is maintained as a separate canonical source with separate metadata.
- Both editions remain doctrinally traceable to the Institutional Study and canonical First Edition.
- Shared canonical Appendices A–G form part of the Institutional Reference Edition without duplication or redesign.
- Both editions are canonical publications serving different reading purposes.
- Any proposed doctrinal or architectural change requires a separate Editorial Decision Record.
- Future work proceeds through institution-specific editions unless explicit editorial governance reopens canonical doctrine.

### Affected Documents

- [Thrift Bank Digital Banking Program Guide](../program-guides/thrift-bank/thrift-bank-program-guide.md)
- [Institutional Reference Edition source](../program-guides/thrift-bank/expanded-edition/thrift-bank-program-guide-expanded-edition.md)
- [Institutional Reference Edition metadata](../program-guides/thrift-bank/expanded-edition/metadata.yaml)
- [Edition comparison](../program-guides/thrift-bank/expanded-edition/EDITION_COMPARISON.md)
- [RBAP parity report](../program-guides/thrift-bank/expanded-edition/PARITY_REPORT.md)
- [Thrift Bank Program Guide index](../program-guides/thrift-bank/README.md)

### Supersedes

None.

### Superseded By

None.

### Notes

Active and complete. The initial proposal requested `EDR-006`, but that identifier already belongs to the accepted decision **Program Guides Must Answer Executive Questions Directly**. Register governance prohibited reuse, so the next available stable identifier, `EDR-013`, was used. The manuscript developed under the working name Expanded Edition is now published under its canonical name, Institutional Reference Edition.

## EDR-014 — Institution Intelligence Framework Is Canonical

**Decision ID:** `EDR-014`

**Title:** Institution Intelligence Framework Is Canonical

**Status:** Accepted

**Date:** 2026-07-18

### Context

The x-change publishing program has completed its canonical Movements, Institutional Studies, and current banking Program Guides. Future work now applies established doctrine to real institutions. Without a frozen methodology, contributors could begin with persuasive prose, mix observation with assumption, or allow institution-specific work to redefine canonical architecture.

The Institution Intelligence Framework has completed editorial review. It establishes evidence controls, analytical stages, editorial mapping, institution-edition boundaries, proposal separation, implementation sequencing, and a reusable template repository.

### Decision

The Institution Intelligence Framework is accepted as the canonical research and editorial methodology for institution-specific editions within the x-change publishing program.

Future institution-specific work must follow this sequence:

```text
Canonical Doctrine
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
Implementation
```

The framework informs institution-specific application. It does not alter canonical doctrine.

Institution Intelligence must distinguish **Observed**, **Inferred**, and **Recommended** statements. Inference must never be presented as fact.

The following agent rule is canonical:

> If sufficient evidence is unavailable, the research agent shall explicitly identify the gap rather than compensate with unsupported prose.

### Rationale

Institution-specific editions require a disciplined bridge between canonical doctrine and a real institution. Beginning with evidence protects factual integrity. Separating intelligence, analysis, mapping, writing, proposal, and implementation protects the authority and purpose of each artifact.

A frozen methodology also allows future institution work to become comparable without forcing institutions into unsupported assumptions or changing canonical doctrine through local adaptation.

### Consequences

- The Institution Intelligence Framework, policies, standards, workflow, and template structure are canonical and locked.
- Future institution work begins with Institution Intelligence rather than manuscript writing.
- Strategic Gap Analysis must compare institutional evidence with identified canonical doctrine.
- Editorial Mapping must precede an Institution Edition.
- Commercial proposals and implementation work remain downstream artifacts.
- Missing evidence must remain visible and may not be repaired through unsupported prose.
- Institution-specific work may adapt examples, priorities, language, ceremonies, and sequence within approved boundaries; it may not create doctrine.
- Framework changes require an explicit accepted Editorial Decision Record.
- Future work proceeds through evidence-based institution engagement, beginning with AllBank Institution Intelligence.

The framework occupies this place in the publishing system:

```text
Movement
   ↓
Institutional Study
   ↓
Program Guide
   ↓
Institution Intelligence
   ↓
Institution Edition
   ↓
Commercial Proposal
   ↓
Implementation
```

### Affected Documents

- [Institution Intelligence index](../../institutions/README.md)
- [Institution Intelligence Framework](../../institutions/FRAMEWORK.md)
- [Public Source Policy](../../institutions/PUBLIC_SOURCE_POLICY.md)
- [Research Workflow](../../institutions/RESEARCH_WORKFLOW.md)
- [Institution Intelligence Standard](../../institutions/INSTITUTION_INTELLIGENCE_STANDARD.md)
- [Strategic Gap Analysis Standard](../../institutions/STRATEGIC_GAP_ANALYSIS_STANDARD.md)
- [Editorial Mapping Standard](../../institutions/EDITORIAL_MAPPING_STANDARD.md)
- [Institution Edition Standard](../../institutions/INSTITUTION_EDITION_STANDARD.md)
- [Commercial Proposal Standard](../../institutions/COMMERCIAL_PROPOSAL_STANDARD.md)
- [Implementation Roadmap Standard](../../institutions/IMPLEMENTATION_ROADMAP_STANDARD.md)
- [Institution template](../../institutions/template/README.md)
- [Editorial Acceptance](../../institutions/EDITORIAL_ACCEPTANCE.md)
- All future institution-specific research, editions, proposals, and implementation roadmaps

### Supersedes

None.

### Superseded By

None.

### Notes

Active and complete. After several institution-intelligence projects have been completed, editorial governance may consider a future `CANONICAL_INSTITUTION_INTELLIGENCE_TAXONOMY.md` to standardize cross-institution comparison across ownership, business model, customer segments, products, channels, Treasury, payments, consumer banking, SME banking, housing, merchant services, technology, partnerships, financial indicators, strategic themes, and implementation signals.

That taxonomy is a deferred recommendation only. EDR-014 does not authorize its creation.

## EDR-015 — Institution Intelligence Framework Final Lock and AllBank Phase 1 Authorization

**Decision ID:** `EDR-015`

**Title:** Institution Intelligence Framework Final Lock and AllBank Phase 1 Authorization

**Status:** Accepted

**Date:** 2026-07-18

### Context

EDR-014 accepted the Institution Intelligence Framework as the canonical research and editorial methodology for institution-specific editions. The framework has completed editorial review, and the publishing program is ready to move from methodology design to evidence-based work with real institutions.

AllBank is the first authorized institution-specific application. The work must begin with public-source Institution Intelligence rather than manuscript writing, sales positioning, architecture design, or implementation planning.

### Decision

The canonical lock established by EDR-014 is confirmed as final. The Institution Intelligence Framework, Public Source Policy, Research Workflow, standards, and template repository structure remain canonical and locked. Framework changes require an explicit accepted Editorial Decision Record.

Phase 1 — AllBank Institution Intelligence is authorized as the first application of the framework. It must follow this sequence:

```text
Canonical Doctrine
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
Implementation
```

The AllBank research base must distinguish **Observed**, **Inferred**, **Recommended**, and **Unknown** statements. It must record every material public source and preserve claim traceability.

The canonical agent rule remains active:

> If sufficient evidence is unavailable, the research agent shall explicitly identify the gap rather than compensate with unsupported prose.

This decision does not authorize an AllBank Institution Edition, AllBank Program Guide, commercial proposal, pricing, implementation plan, production architecture, or readiness conclusion.

### Rationale

The framework becomes institutionally useful through disciplined application. AllBank provides the first opportunity to establish an attributable evidence base, identify strategic questions, and prepare an editorial mapping without allowing institution-specific research to alter thrift-bank doctrine.

Separating research from later writing protects the institution from unsupported claims and preserves the authority of the canonical Thrift Bank Institutional Study and Program Guide.

### Consequences

- The framework-design phase is complete.
- Future framework changes require an explicit accepted Editorial Decision Record.
- AllBank Institution Intelligence becomes the first canonical framework application.
- Public sources and material claims must remain traceable through separate source and evidence registers.
- Missing evidence must become an Unknown and, where material, a management question.
- The AllBank Institution Intelligence may advance to analysis when it satisfies the framework’s evidence gate.
- Strategic Gap Analysis and Editorial Mapping remain review artifacts until their respective gates are accepted.
- Institution Edition drafting remains unauthorized until Editorial Mapping explicitly authorizes it.
- The expected next governance activity is AllBank Editorial Mapping Review.

### Affected Documents

- [Institution Intelligence index](../../institutions/README.md)
- [Framework metadata](../../institutions/metadata.yaml)
- [Framework Editorial Acceptance](../../institutions/EDITORIAL_ACCEPTANCE.md)
- [AllBank Institution Intelligence repository](../../institutions/allbank/README.md)
- [AllBank metadata](../../institutions/allbank/metadata.yaml)
- [AllBank Public Source Register](../../institutions/allbank/PUBLIC_SOURCE_REGISTER.md)
- [AllBank Evidence Register](../../institutions/allbank/EVIDENCE_REGISTER.md)
- [AllBank Institution Intelligence Report](../../institutions/allbank/INSTITUTION_INTELLIGENCE_REPORT.md)
- [AllBank Digital Maturity Assessment](../../institutions/allbank/DIGITAL_MATURITY_ASSESSMENT.md)
- [AllBank Strategic Gap Analysis](../../institutions/allbank/STRATEGIC_GAP_ANALYSIS.md)
- [AllBank Editorial Mapping](../../institutions/allbank/EDITORIAL_MAPPING.md)
- [AllBank Questions for Management](../../institutions/allbank/QUESTIONS_FOR_MANAGEMENT.md)

### Supersedes

None. EDR-014 remains the governing framework-acceptance decision.

### Superseded By

None.

### Notes

Active and complete. The framework sources and template standards were not changed by this decision.

The proposed cross-institution taxonomy remains deferred under EDR-014. EDR-015 does not authorize its creation.
