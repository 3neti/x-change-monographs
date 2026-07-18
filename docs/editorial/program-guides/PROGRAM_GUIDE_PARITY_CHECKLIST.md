# Banking Program Guide Parity Checklist

## Authority

This checklist implements the [Canonical Banking Program Guide](CANONICAL_BANKING_PROGRAM_GUIDE.md). It must be reviewed during drafting, editorial review, approval, and publication preparation.

The [Editorial Decision Register](../decisions/EDITORIAL_DECISION_REGISTER.md) records why the governing rules exist. Any structural deviation or supersession claim must cite the applicable decision ID.

Every parity review has two required dimensions:

1. **Architectural completeness** — the canonical sections and coverage categories are present; and
2. **Business-question completeness** — each section answers its Executive Question and supports its Executive Decision.

Neither dimension can compensate for the other.

## Status Rules

| Status | Meaning |
| --- | --- |
| Complete | The guide answers the requirement and its related business question sufficiently for its current editorial stage. |
| Planned | The approved architecture reserves the requirement, but substantive coverage has not yet been written. |
| Missing | The requirement is neither answered nor reserved in the guide. |
| Not Applicable | The requirement does not apply; the Notes cell must explain why. |
| Deviation Approved | An accepted editorial decision authorizes the departure; the Notes cell must cite it. |

`Not Applicable` without an explanation is incomplete. `Deviation Approved` without an accepted editorial decision reference is incomplete.

`Complete` is a parity-coverage status, not an editorial lock state. Sector metadata and the Program Records table identify whether a complete section is editorially locked.

## Cross-Program Matrix

The RBAP and Thrift Banks columns record current guide coverage against the frozen architecture. The Government Depository Banks column remains a planning entry.

| Canonical Requirement | RBAP | Thrift Banks | Government Depository Banks | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| 1. Opportunity | Complete | Complete | Planned | Planned | Thrift Section 1 answers the institution-specific opportunity; the government implementation remains planned. |
| 2. Program definition | Complete | Complete | Planned | Planned | Thrift Section 2 distinguishes the Program from the enduring Capability. |
| 3. Institutional benefits | Complete | Complete | Planned | Planned | Thrift Section 3 establishes operating leverage and institutional benefit. |
| 4. Roles and responsibilities | Complete | Complete | Planned | Planned | Thrift Section 2 and Appendix B assign institutional and provider responsibilities. |
| 5. Governance | Planned | Complete | Planned | Planned | Thrift Section 2 and Appendix B complete governance coverage; RBAP Appendix B remains planned. |
| 6. Licensing or participation model | Complete | Complete | Planned | Planned | Thrift Section 2 defines institution-specific licensing and agreement boundaries without pricing. |
| 7. Operating sovereignty | Complete | Complete | Planned | Planned | Thrift Sections 3 and 4 preserve institutional ownership and control. |
| 8. DevOps model | Complete | Complete | Planned | Planned | Thrift Section 2, Section 4, and Appendix B define delegated DevOps responsibility. |
| 9. Settlement model | Complete | Complete | Planned | Planned | Thrift Section 4 preserves the bank-owned settlement relationship and introduces no NetBank dependency. |
| 10. Custody and authority boundaries | Complete | Complete | Planned | Planned | Thrift Section 4 and Appendices B and E preserve custody and authority. |
| 11. Funding Events | Complete | Complete | Planned | Planned | Thrift Section 4 and Appendix D provide the canonical treatment. |
| 12. Treasury | Planned | Complete | Planned | Planned | Thrift Section 4 and Appendix D complete Treasury coverage; RBAP Appendix D remains planned. |
| 13. Facilities | Complete | Complete | Planned | Planned | Thrift Section 4 preserves Facility ownership of commercial meaning. |
| 14. Settlement Envelopes | Complete | Complete | Planned | Planned | Thrift Section 4 defines evidence and condition responsibility. |
| 15. Pay Codes | Complete | Complete | Planned | Planned | Thrift Sections 4 and 5 preserve Pay Code as credential. |
| 16. Execution | Complete | Complete | Planned | Planned | Thrift Section 4 defines execution through `emi-core` and the bank-specific driver. |
| 17. Representative banking workflows | Complete | Complete | Planned | Planned | Thrift Section 5 presents remittance and five related services. |
| 18. Business case | Complete | Complete | Planned | Planned | Thrift Section 6 establishes the institutional and commercial case. |
| 19. Costs of participation | Complete | Complete | Planned | Planned | Thrift Section 6 and Appendix C identify cost categories without inventing prices. |
| 20. Revenue or economic opportunities | Complete | Complete | Planned | Planned | Thrift Section 6 identifies possible value without automatic-return claims. |
| 21. Commercial Waterfall | Planned | Complete | Planned | Planned | Thrift Section 6 and Appendix C complete the conceptual waterfall; RBAP Appendix C remains planned. |
| 22. Pilot | Complete | Complete | Planned | Planned | Thrift Section 7 defines a bounded controlled-production pilot. |
| 23. Phased rollout | Complete | Complete | Planned | Planned | Thrift Section 7 defines evidence-based expansion. |
| 24. Success metrics | Complete | Complete | Planned | Planned | Thrift Section 7 defines evidence categories without prescribing targets. |
| 25. FAQ | Planned | Complete | Planned | Planned | Thrift Appendix F answers the required questions; RBAP Appendix F remains planned. |
| 26. Glossary | Planned | Complete | Planned | Planned | Thrift Appendix A defines the canonical terms; RBAP Appendix A remains planned. |
| 27. Deployment architecture | Planned | Complete | Planned | Planned | Thrift Appendix E completes the responsibility and deployment boundaries. |

The cross-program matrix remains the architectural parity control. The following business-question review supplements it without replacing or reorganizing its 27 mandatory coverage categories.

## Business-Question Completeness Matrix

| Section | Executive Question | Decision the section must enable | RBAP | Thrift Banks | Government Depository Banks | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Section 1 — Why This Program? | Why should the sector body launch this Program? | Decide whether the Program merits institutional consideration. | Complete | Complete | Planned | Planned | The thrift implementation adapts the question to one institution and supports formal evaluation. |
| Section 2 — What Is the Program? | What exactly is the sector body being invited to launch? | Decide whether the proposed Program merits institutional evaluation. | Complete | Complete | Planned | Planned | The thrift implementation defines Program, Capability, roles, licensing, governance, and boundaries. |
| Section 3 — Why Should a Bank Participate? | What does an individual bank gain? | Understand the institution's prospective benefit from participation. | Complete | Complete | Planned | Planned | The thrift implementation answers the institution-specific benefit question. |
| Section 4 — How Does the Program Work? | How does the operating model work? | Understand how the model preserves institutional independence while enabling modern digital banking. | Complete | Complete | Planned | Planned | The thrift implementation covers the complete operating and driver model. |
| Section 5 — Banking in Action | Show me how it actually works. | Assess the Program through representative banking workflows. | Complete | Complete | Planned | Planned | The thrift implementation uses remittance canonically and relates five further services. |
| Section 6 — The Institutional Case | What kind of institution can participation help the bank become? | Decide whether the institutional case merits detailed commercial and implementation evaluation. | Complete | Complete | Planned | Planned | The thrift implementation covers Transaction Gravity, adaptability, costs, opportunities, and sustainability. |
| Section 7 — Launching the Program | What happens after approval? | Decide whether to authorize or evaluate the proposed next step. | Complete | Complete | Planned | Planned | The thrift implementation defines discovery through controlled expansion. |

For a section to be `Complete`, reviewers must confirm all of the following:

- the Executive Question is present;
- the Key Message remains aligned with the approved architecture;
- the Executive Decision is stated immediately after the Key Message;
- the narrative directly answers the Executive Question;
- the narrative supports the Executive Decision; and
- stylistic polish does not conceal a missing answer, assumption, or approval dependency.

## Canonical Diagram Parity

Appendix G is the shared registry for canonical program diagrams. It is structurally present in the RBAP Program Guide as a placeholder; all canonical diagrams remain `Planned`. Diagram parity is reviewed separately from the 27 mandatory business-coverage categories.

| Canonical diagram | Registry status | RBAP | Thrift Banks | Government Depository Banks | Notes |
| --- | --- | --- | --- | --- | --- |
| Program Participants | Complete | Planned | Complete | Planned | Canonical source drafted in Thrift Appendix G; other guide integrations remain planned. |
| Funding Event | Complete | Planned | Complete | Planned | Canonical source drafted in Thrift Appendix G. |
| Treasury | Complete | Planned | Complete | Planned | Canonical source drafted in Thrift Appendix G. |
| Banking Operating Model | Complete | Planned | Complete | Planned | Canonical source drafted in Thrift Appendix G. |
| Deposit Flow | Complete | Planned | Complete | Planned | Canonical source drafted in Thrift Appendix G. |
| Payroll Flow | Complete | Planned | Complete | Planned | Canonical source drafted in Thrift Appendix G. |
| Merchant Flow | Complete | Planned | Complete | Planned | Canonical source drafted in Thrift Appendix G. |
| Government Disbursement Flow | Complete | Planned | Complete | Planned | Canonical source drafted for cross-program parity; use in a thrift service remains subject to bank approval. |
| Commercial Waterfall | Complete | Planned | Complete | Planned | Canonical conceptual source drafted without pricing. |
| Deployment Architecture | Complete | Planned | Complete | Planned | Canonical source drafted in Thrift Appendix G. |

A future guide satisfies diagram parity by referencing the approved canonical diagram. It must not recreate or redefine a canonical diagram without an accepted editorial decision authorizing the deviation.

## Program Records

| Program | Guide path | Current stage |
| --- | --- | --- |
| RBAP Digital Banking Program | `docs/editorial/program-guides/rbap/rbap-digital-banking-program-guide.md` | Sections 1–7 are editorially complete, locked, and frozen as the canonical narrative. The Executive Summary has a complete draft and remains in editorial review under EDR-012; lock requires revalidation after the appendices are complete. Future chapter changes are limited to factual or typographical corrections, whole-manuscript cadence review, and cross-reference updates. Appendices A–F remain planned; Appendix G is structurally present with all diagrams planned. |
| Thrift Bank Digital Banking Program | `docs/editorial/program-guides/thrift-bank/thrift-bank-program-guide.md` | Complete EDR-005 implementation in editorial review. Executive Summary, Sections 1–7, and Appendices A–G are populated; no section is yet locked and no publication build is authorized. The separate [Phase 1 institutional study](../thrift-bank-digital-banking-program/README.md) remains the approved doctrinal source. |
| Government Depository Banking Program | Not created | Anticipated. |

## Required Gap Report

When any architectural or business-question item becomes `Missing`, Codex must identify:

1. the missing canonical requirement;
2. the business question or Executive Decision left unsupported;
3. why the requirement is mandatory;
4. whether the omission appears intentional;
5. the recommended remediation; and
6. whether an editorial decision record is required.

Codex must not convert a `Missing` item to `Complete` by inventing program terms, economics, responsibilities, workflows, or operating arrangements.
