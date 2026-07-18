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
| 5. Governance | Complete | Complete | Planned | Planned | RBAP Section 2 and Appendix B complete association, bank, provider, pilot, incident, and change-governance coverage. |
| 6. Licensing or participation model | Complete | Complete | Planned | Planned | Thrift Section 2 defines institution-specific licensing and agreement boundaries without pricing. |
| 7. Operating sovereignty | Complete | Complete | Planned | Planned | Thrift Sections 3 and 4 preserve institutional ownership and control. |
| 8. DevOps model | Complete | Complete | Planned | Planned | Thrift Section 2, Section 4, and Appendix B define delegated DevOps responsibility. |
| 9. Settlement model | Complete | Complete | Planned | Planned | Thrift Section 4 preserves the bank-owned settlement relationship and introduces no NetBank dependency. |
| 10. Custody and authority boundaries | Complete | Complete | Planned | Planned | Thrift Section 4 and Appendices B and E preserve custody and authority. |
| 11. Funding Events | Complete | Complete | Planned | Planned | Thrift Section 4 and Appendix D provide the canonical treatment. |
| 12. Treasury | Complete | Complete | Planned | Planned | RBAP Section 4 and Appendix D complete the institutional Treasury grammar without changing custody or legal fund character. |
| 13. Facilities | Complete | Complete | Planned | Planned | Thrift Section 4 preserves Facility ownership of commercial meaning. |
| 14. Settlement Envelopes | Complete | Complete | Planned | Planned | Thrift Section 4 defines evidence and condition responsibility. |
| 15. Pay Codes | Complete | Complete | Planned | Planned | Thrift Sections 4 and 5 preserve Pay Code as credential. |
| 16. Execution | Complete | Complete | Planned | Planned | Thrift Section 4 defines execution through `emi-core` and the bank-specific driver. |
| 17. Representative banking workflows | Complete | Complete | Planned | Planned | Thrift Section 5 presents remittance and five related services. |
| 18. Business case | Complete | Complete | Planned | Planned | Thrift Section 6 establishes the institutional and commercial case. |
| 19. Costs of participation | Complete | Complete | Planned | Planned | Thrift Section 6 and Appendix C identify cost categories without inventing prices. |
| 20. Revenue or economic opportunities | Complete | Complete | Planned | Planned | Thrift Section 6 identifies possible value without automatic-return claims. |
| 21. Commercial Waterfall | Complete | Complete | Planned | Planned | RBAP Sections 2 and 6 and Appendix C complete the principles-level accountability model without prescribing prices. |
| 22. Pilot | Complete | Complete | Planned | Planned | Thrift Section 7 defines a bounded controlled-production pilot. |
| 23. Phased rollout | Complete | Complete | Planned | Planned | Thrift Section 7 defines evidence-based expansion. |
| 24. Success metrics | Complete | Complete | Planned | Planned | Thrift Section 7 defines evidence categories without prescribing targets. |
| 25. FAQ | Complete | Complete | Planned | Planned | RBAP Appendix F answers all reserved questions and the additional institutional questions required for role and approval clarity. |
| 26. Glossary | Complete | Complete | Planned | Planned | RBAP Appendix A defines the Program's banking, operational, technical, commercial, and publication terms with appropriate legal qualifications. |
| 27. Deployment architecture | Complete | Complete | Planned | Planned | RBAP Appendix E completes bank-controlled environment, delegated DevOps, release, data, settlement, handover, and portability boundaries. |

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

Appendix G implements the shared registry for canonical program diagrams. The RBAP Program Guide contains locked Mermaid source for every registry diagram and the frozen narrative's editorial illustrations. Final figure rendering and placement remain publication-workflow matters. Diagram parity is reviewed separately from the 27 mandatory business-coverage categories.

| Canonical diagram | Registry status | RBAP | Thrift Banks | Government Depository Banks | Notes |
| --- | --- | --- | --- | --- | --- |
| Program Participants | Complete | Complete | Complete | Planned | RBAP Appendix G preserves association administration, bank authority, delegated operations, and regulated settlement responsibility. |
| Funding Event | Complete | Complete | Complete | Planned | RBAP Appendix G records recognition of an external financial event without creating value. |
| Treasury | Complete | Complete | Complete | Planned | RBAP Appendix G distinguishes recognized, available, reserved, outstanding, unresolved, and resolved operational state. |
| Banking Operating Model | Complete | Complete | Complete | Planned | RBAP Appendix G connects request, bank authority, Facility, conditions, credential, execution, settlement, and reconciliation. |
| Deposit Flow | Complete | Complete | Complete | Planned | RBAP Appendix G preserves the bank-customer deposit relationship and operational recognition boundary. |
| Payroll Flow | Complete | Complete | Complete | Planned | RBAP Appendix G preserves employer authority, bank governance, attribution, execution, outcomes, and reconciliation. |
| Merchant Flow | Complete | Complete | Complete | Planned | RBAP Appendix G preserves the bank-governed Facility and direct settlement arrangement. |
| Government Disbursement Flow | Complete | Complete | Complete | Planned | RBAP Appendix G preserves agency authority, bank governance, beneficiary conditions, and reconciliation. |
| Commercial Waterfall | Complete | Complete | Complete | Planned | RBAP Appendix G expresses an accountability sequence separate from custody and settlement and contains no prices. |
| Deployment Architecture | Complete | Complete | Complete | Planned | RBAP Appendix G preserves separate bank deployments, delegated operations, credentials, accounts, and authority. |

A future guide satisfies diagram parity by referencing the approved canonical diagram. It must not recreate or redefine a canonical diagram without an accepted editorial decision authorizing the deviation.

## Program Records

| Program | Guide path | Current stage |
| --- | --- | --- |
| RBAP Digital Banking Program | `docs/editorial/program-guides/rbap/rbap-digital-banking-program-guide.md` | The Executive Summary was revalidated under EDR-012 and locked without wording changes. Sections 1–7 and Appendices A–G remain canonical and locked; all mandatory coverage categories and diagram-registry requirements remain Complete. The complete editorial source is canonical and locked. Final publication governance, figure rendering, accessibility tagging, placement, and pagination remain pending. |
| Thrift Bank Digital Banking Program | `docs/editorial/program-guides/thrift-bank/thrift-bank-program-guide.md` | Canonical and editorially locked under the [Editorial Acceptance](thrift-bank/EDITORIAL_ACCEPTANCE.md). EDR-005 editorial work is complete for this implementation; future work proceeds through institution-specific editions. Executive Summary, Sections 1–7, and Appendices A–G are complete. No publication build is authorized. The separate [Phase 1 Institutional Study](../thrift-bank-digital-banking-program/README.md) remains the authoritative doctrinal source. |
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
