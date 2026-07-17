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

## Cross-Program Matrix

The RBAP column records the current architecture-frozen skeleton. The Thrift Banks and Government Depository Banks columns are planning entries only; no guide has been created for either program.

| Canonical Requirement | RBAP | Thrift Banks | Government Depository Banks | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| 1. Opportunity | Complete | Planned | Planned | Planned | RBAP Section 1 is editorially complete; other implementations remain planned. |
| 2. Program definition | Complete | Planned | Planned | Planned | RBAP Section 2 defines the Program; other implementations remain planned. |
| 3. Institutional benefits | Planned | Planned | Planned | Planned | Section 3. |
| 4. Roles and responsibilities | Complete | Planned | Planned | Planned | RBAP Section 2 assigns the program, technology, bank, settlement, DevOps, and service-provider roles. |
| 5. Governance | Planned | Planned | Planned | Planned | RBAP Section 2 establishes the governance model; Appendix B remains planned. |
| 6. Licensing or participation model | Complete | Planned | Planned | Planned | RBAP Section 2 provides the proposed group-licensing and bank-participation model. |
| 7. Operating sovereignty | Planned | Planned | Planned | Planned | Sections 3 and 4. |
| 8. DevOps model | Planned | Planned | Planned | Planned | Section 4. |
| 9. Settlement model | Planned | Planned | Planned | Planned | Section 4. |
| 10. Custody and authority boundaries | Planned | Planned | Planned | Planned | Section 4. |
| 11. Funding Events | Planned | Planned | Planned | Planned | Section 4. |
| 12. Treasury | Planned | Planned | Planned | Planned | Section 4 and Appendix D. |
| 13. Facilities | Planned | Planned | Planned | Planned | Section 4. |
| 14. Settlement Envelopes | Planned | Planned | Planned | Planned | Section 4. |
| 15. Pay Codes | Planned | Planned | Planned | Planned | Section 4 and Section 5. |
| 16. Execution | Planned | Planned | Planned | Planned | Section 4. |
| 17. Representative banking workflows | Planned | Planned | Planned | Planned | Section 5. |
| 18. Business case | Planned | Planned | Planned | Planned | Section 6. |
| 19. Costs of participation | Planned | Planned | Planned | Planned | Section 6. |
| 20. Revenue or economic opportunities | Planned | Planned | Planned | Planned | Section 6. |
| 21. Commercial Waterfall | Planned | Planned | Planned | Planned | Section 6 and Appendix C. |
| 22. Pilot | Planned | Planned | Planned | Planned | Section 7. |
| 23. Phased rollout | Planned | Planned | Planned | Planned | Section 7. |
| 24. Success metrics | Planned | Planned | Planned | Planned | Section 7. |
| 25. FAQ | Planned | Planned | Planned | Planned | Appendix F. |
| 26. Glossary | Planned | Planned | Planned | Planned | Appendix A. |
| 27. Deployment architecture | Planned | Planned | Planned | Planned | Appendix E. |

The cross-program matrix remains the architectural parity control. The following business-question review supplements it without replacing or reorganizing its 27 mandatory coverage categories.

## Business-Question Completeness Matrix

| Section | Executive Question | Decision the section must enable | RBAP | Thrift Banks | Government Depository Banks | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Section 1 — Why This Program? | Why should the sector body launch this Program? | Decide whether the Program merits institutional consideration. | Complete | Planned | Planned | Planned | The RBAP narrative answers its Executive Question and supports its Executive Decision; other implementations remain planned. |
| Section 2 — What Is the Program? | What exactly is the sector body being invited to launch? | Decide whether the proposed Program merits institutional evaluation. | Complete | Planned | Planned | Planned | The RBAP narrative defines the Program and preserves the boundaries among program administration, bank authority, software, DevOps, and settlement. |
| Section 3 — Why Should a Bank Participate? | What does an individual bank gain? | Understand the institution's prospective benefit from participation. | Planned | Planned | Planned | Planned | Must preserve institutional identity, governance, customer relationships, and independence. |
| Section 4 — How Does the Program Work? | How does the operating model work? | Understand how the model preserves institutional independence while enabling modern digital banking. | Planned | Planned | Planned | Planned | Must address operating sovereignty, custody, authority, DevOps, and settlement. |
| Section 5 — Banking in Action | Show me how it actually works. | Assess the Program through representative banking workflows. | Planned | Planned | Planned | Planned | Diagrams and concise prose must answer the workflow question without inventing operating details. |
| Section 6 — The Business Case | Is this commercially worthwhile? | Decide whether the business case merits detailed commercial evaluation. | Planned | Planned | Planned | Planned | Must address participation costs, economic opportunity, and the Commercial Waterfall. |
| Section 7 — Launching the Program | What happens after approval? | Decide whether to authorize or evaluate the proposed next step. | Planned | Planned | Planned | Planned | Must address pilot, phased rollout, success metrics, and next steps. |

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
| Program Participants | Planned | Planned | Planned | Planned | Placeholder only. |
| Funding Event | Planned | Planned | Planned | Planned | Placeholder only. |
| Treasury | Planned | Planned | Planned | Planned | Placeholder only. |
| Banking Operating Model | Planned | Planned | Planned | Planned | Placeholder only. |
| Deposit Flow | Planned | Planned | Planned | Planned | Placeholder only. |
| Payroll Flow | Planned | Planned | Planned | Planned | Placeholder only. |
| Merchant Flow | Planned | Planned | Planned | Planned | Placeholder only. |
| Government Disbursement Flow | Planned | Planned | Planned | Planned | Placeholder only. |
| Commercial Waterfall | Planned | Planned | Planned | Planned | Placeholder only. |
| Deployment Architecture | Planned | Planned | Planned | Planned | Placeholder only. |

A future guide satisfies diagram parity by referencing the approved canonical diagram. It must not recreate or redefine a canonical diagram without an accepted editorial decision authorizing the deviation.

## Program Records

| Program | Guide path | Current stage |
| --- | --- | --- |
| RBAP Digital Banking Program | `docs/editorial/program-guides/rbap/rbap-digital-banking-program-guide.md` | Sections 1 and 2 editorially complete and locked. Sections 3–7 and Appendices A–F remain planned; Appendix G is structurally present with all diagrams planned. |
| Thrift Bank Digital Banking Program | Not created | Anticipated. |
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
