# Canonical Banking Program Guide

## Status

Canonical — Version 1.0

## Purpose

A banking Program Guide is the canonical commercial handbook for a banking-sector modernization program. It explains the program as a durable institutional proposition before approval, supports evaluation and implementation during approval, and remains a reference after launch.

It is not:

- a white paper;
- a product brochure;
- a technical manual;
- a legal agreement; or
- a bank-specific financial proposal.

The guide must explain:

- the opportunity;
- the program;
- the participating institution's benefits;
- the operating model;
- representative workflows;
- the business case; and
- the launch path.

The guide must answer the reader's business questions directly. Polished prose does not compensate for an unanswered question.

## Source-of-Truth Rule

This document is the source of truth for banking Program Guide structure. Each sector-specific Program Guide is an implementation of this architecture.

Sector guides may adapt:

- tone;
- motivation;
- institutional examples;
- banking ceremonies;
- regulatory context;
- commercial emphasis; and
- audience language.

They may not casually redefine:

- Pay Code;
- Facility;
- Settlement Envelope;
- Treasury;
- Funding Event;
- Execution Engine;
- Execution Driver;
- custody boundaries;
- software ownership; or
- settlement responsibility.

Those concepts must remain aligned with the canonical x-change and Treasury grammar. If the applicable canonical grammar does not resolve a term, the guide must flag the ambiguity for editorial decision rather than create a sector-specific definition.

## Canonical Section Architecture

The Executive Summary appears before the numbered sections but is written last. It is unnumbered.

| Canonical component | Business question | Required purpose |
| --- | --- | --- |
| Executive Summary | What decision is this guide asking the reader to consider? | Summarize the completed guide without introducing new claims. |
| Section 1 — Why This Program? | Why should the sector body launch this program? | Establish the opportunity, collective need, institutional sponsor, and timing. |
| Section 2 — What Is the Program? | What exactly is the sector body being invited to launch? | Define the program, participants, roles, governance, licensing or participation model, and commercial model at an appropriate level. |
| Section 3 — Why Should a Bank Participate? | What does an individual bank gain? | Explain institutional benefits while preserving the bank's identity, governance, customer relationship, and independence. |
| Section 4 — How Does the Program Work? | How does the operating model work? | Explain bank ownership, operating sovereignty, DevOps, settlement, custody, authority, Treasury, Funding Events, Facilities, Settlement Envelopes, Pay Codes, and Execution. |
| Section 5 — Banking in Action | Show me how it actually works. | Present representative banking workflows through concise prose and diagrams. |
| Section 6 — The Business Case | Is this commercially worthwhile? | Explain comparative cost, participation economics, shared investment, revenue opportunities, the Commercial Waterfall, and ecosystem sustainability. |
| Section 7 — Launching the Program | What happens after approval? | Define the pilot, phased rollout, success metrics, ecosystem growth, and next steps. |
| Appendices | Where can the reader verify terms and supporting operating detail? | Provide the glossary, governance, Commercial Waterfall, Treasury grammar, deployment architecture, and frequently asked questions. |

The architecture is stable even when the sector narrative changes. A guide may combine closely related coverage within the approved section architecture, but it must not silently omit a mandatory category.

## Mandatory Cross-Program Parity

Every banking-sector Program Guide must implement the canonical section architecture unless an explicit editorial decision record approves a deviation.

The currently anticipated implementations are:

- RBAP Digital Banking Program;
- Thrift Bank Digital Banking Program; and
- Government Depository Banking Program.

Their sector narratives will differ:

- rural banking emphasizes community modernization and collective participation;
- thrift banking emphasizes deposit growth, SMEs, retail banking, lending, and competitive digital services; and
- government depository banking emphasizes public trust, custody, accountability, public-finance workflows, and evidentiary controls.

Those differences do not alter the canonical business questions or required coverage.

## Mandatory Coverage Register

| No. | Canonical requirement | Expected location |
| ---: | --- | --- |
| 1 | Opportunity | Section 1 |
| 2 | Program definition | Section 2 |
| 3 | Institutional benefits | Section 3 |
| 4 | Roles and responsibilities | Section 2 |
| 5 | Governance | Section 2 and Appendix B |
| 6 | Licensing or participation model | Section 2 |
| 7 | Operating sovereignty | Sections 3 and 4 |
| 8 | DevOps model | Section 4 |
| 9 | Settlement model | Section 4 |
| 10 | Custody and authority boundaries | Section 4 |
| 11 | Funding Events | Section 4 |
| 12 | Treasury | Section 4 and Appendix D |
| 13 | Facilities | Section 4 |
| 14 | Settlement Envelopes | Section 4 |
| 15 | Pay Codes | Section 4 and representative workflows |
| 16 | Execution | Section 4 |
| 17 | Representative banking workflows | Section 5 |
| 18 | Business case | Section 6 |
| 19 | Costs of participation | Section 6 |
| 20 | Revenue or economic opportunities | Section 6 |
| 21 | Commercial Waterfall | Section 6 and Appendix C |
| 22 | Pilot | Section 7 |
| 23 | Phased rollout | Section 7 |
| 24 | Success metrics | Section 7 |
| 25 | FAQ | Appendix F |
| 26 | Glossary | Appendix A |
| 27 | Deployment architecture | Appendix E |

## Parity-Check Rule

Every guide must be assessed against `PROGRAM_GUIDE_PARITY_CHECKLIST.md` while it is drafted, reviewed, approved, and prepared for publication.

Permitted statuses are:

- **Complete** — the guide answers the requirement sufficiently for its current editorial stage;
- **Planned** — the approved architecture contains a placeholder, but substantive coverage has not yet been written;
- **Missing** — the guide neither answers nor reserves an approved place for the requirement;
- **Not Applicable** — the requirement does not apply and the matrix records a written explanation; and
- **Deviation Approved** — the guide departs from the canonical architecture under an identified editorial decision record.

`Not Applicable` is invalid without a written explanation. `Deviation Approved` is invalid without a reference to an accepted editorial decision record.

## Agent Balk Rule

When drafting, reviewing, or publishing a banking Program Guide, Codex must not silently proceed if a canonical section or mandatory coverage category is missing.

Codex must report:

1. the missing requirement;
2. why it is part of the canonical architecture;
3. whether the omission appears intentional;
4. the recommended remediation; and
5. whether an editorial decision record is required.

The report must identify the unanswered business question, not merely count missing headings.

Use language such as:

> Canonical Program Guide parity is incomplete. The proposed guide does not yet address the settlement operating model and commercial participation structure. These are mandatory coverage areas unless a documented editorial deviation is approved.

Codex must not manufacture missing content to satisfy the checklist. It must flag the gap and await an editorial decision when the missing coverage cannot be restored from approved source material.

## Review and Publication Gate

A guide may move from skeleton to drafting while requirements are `Planned`. It may not be described as editorially complete while any requirement is `Planned` or `Missing`.

A publication build may proceed only when every requirement is:

- `Complete`;
- `Not Applicable` with a written explanation; or
- `Deviation Approved` with an accepted editorial decision reference.

The parity matrix is an editorial control, not a substitute for editorial judgment, legal review, technical validation, or commercial approval.

## Change Control

The canonical architecture may be changed only through an explicit editorial revision to this document. A sector-specific deviation requires an accepted decision record under `docs/editorial/decisions/`.

A deviation record must identify:

- the affected guide;
- the canonical requirement affected;
- the business question that will be answered differently or not answered;
- the reason for the deviation; and
- the consequences for cross-program comparability.
