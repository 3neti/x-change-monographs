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

The RBAP column records current guide coverage against the frozen architecture. The Thrift Banks and Government Depository Banks columns are planning entries only; no guide has been created for either program.

| Canonical Requirement | RBAP | Thrift Banks | Government Depository Banks | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| 1. Opportunity | Complete | Planned | Planned | Planned | RBAP Section 1 is editorially complete; other implementations remain planned. |
| 2. Program definition | Complete | Planned | Planned | Planned | RBAP Section 2 defines the Program; other implementations remain planned. |
| 3. Institutional benefits | Complete | Planned | Planned | Planned | RBAP Section 3 is editorially complete and locked; other implementations remain planned. |
| 4. Roles and responsibilities | Complete | Planned | Planned | Planned | RBAP Section 2 assigns the program, technology, bank, settlement, DevOps, and service-provider roles. |
| 5. Governance | Planned | Planned | Planned | Planned | RBAP Section 2 establishes the governance model; Appendix B remains planned. |
| 6. Licensing or participation model | Complete | Planned | Planned | Planned | RBAP Section 2 provides the proposed group-licensing and bank-participation model. |
| 7. Operating sovereignty | Complete | Planned | Planned | Planned | RBAP Sections 3 and 4 provide the locked institutional-benefit and operating-model treatment. |
| 8. DevOps model | Complete | Planned | Planned | Planned | RBAP Section 4 defines the DevOps division of responsibility and is editorially locked. |
| 9. Settlement model | Complete | Planned | Planned | Planned | RBAP Section 4 defines the direct bank–settlement-institution relationship and is editorially locked. |
| 10. Custody and authority boundaries | Complete | Planned | Planned | Planned | RBAP Section 4 identifies where funds remain, where authority resides, and how settlement occurs. |
| 11. Funding Events | Complete | Planned | Planned | Planned | RBAP Section 4 provides the locked canonical treatment. |
| 12. Treasury | Planned | Planned | Planned | Planned | RBAP Section 4 provides the locked Program Guide treatment; Appendix D remains planned. |
| 13. Facilities | Complete | Planned | Planned | Planned | RBAP Section 4 provides the locked canonical treatment. |
| 14. Settlement Envelopes | Complete | Planned | Planned | Planned | RBAP Section 4 provides the locked canonical treatment. |
| 15. Pay Codes | Complete | Planned | Planned | Planned | RBAP Section 4 provides the locked canonical treatment, and locked Section 5 applies it through the remittance ceremony. |
| 16. Execution | Complete | Planned | Planned | Planned | RBAP Section 4 provides the locked canonical treatment. |
| 17. Representative banking workflows | Complete | Planned | Planned | Planned | RBAP Section 5 presents remittance as the locked canonical ceremony and relates it to additional banking services. |
| 18. Business case | Complete | Planned | Planned | Planned | Locked RBAP Section 6 establishes the institutional case and treats commercial sustainability as a supporting consequence. |
| 19. Costs of participation | Complete | Planned | Planned | Planned | Locked RBAP Section 6 addresses comparative cost at a principles level; institution-specific amounts remain part of later commercial evaluation. |
| 20. Revenue or economic opportunities | Complete | Planned | Planned | Planned | Locked RBAP Section 6 identifies relationship, service, and shared-engineering value without projections or automatic-return claims. |
| 21. Commercial Waterfall | Planned | Planned | Planned | Planned | Locked RBAP Section 6 establishes the allocation principle; Appendix C remains planned. |
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
| Section 3 — Why Should a Bank Participate? | What does an individual bank gain? | Understand the institution's prospective benefit from participation. | Complete | Planned | Planned | Planned | The RBAP narrative answers its Executive Question, supports its Executive Decision, and is editorially locked. |
| Section 4 — How Does the Program Work? | How does the operating model work? | Understand how the model preserves institutional independence while enabling modern digital banking. | Complete | Planned | Planned | Planned | The RBAP narrative answers its Executive Question, supports its Executive Decision, and is editorially locked. |
| Section 5 — Banking in Action | Show me how it actually works. | Assess the Program through representative banking workflows. | Complete | Planned | Planned | Planned | The RBAP remittance ceremony answers the business question, applies the locked Section 4 grammar, and is editorially locked. |
| Section 6 — The Institutional Case | What kind of institution can participation help the bank become? | Decide whether the institutional case merits detailed commercial and implementation evaluation. | Complete | Planned | Planned | Planned | The RBAP narrative answers its Executive Question, supports its Executive Decision, and is editorially locked. |
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
| RBAP Digital Banking Program | `docs/editorial/program-guides/rbap/rbap-digital-banking-program-guide.md` | Sections 1–6 are editorially complete and locked. Section 7 and Appendices A–F remain planned; Appendix G is structurally present with all diagrams planned. |
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
