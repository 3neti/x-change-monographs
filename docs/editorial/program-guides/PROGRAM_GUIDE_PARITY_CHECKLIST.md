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

The RBAP, Thrift Banks, and Government Depository Banks columns record current guide coverage against the frozen architecture. The Government Depository Guide is editorially complete at the canonical Version 0.9 review baseline. `Complete` records substantive coverage; it does not imply publication freeze or Version 1.0 approval.

| Canonical Requirement | RBAP | Thrift Banks | Government Depository Banks | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| 1. Opportunity | Complete | Complete | Complete | Complete | Government Depository Section 1 establishes the public-trust and reusable-capability opportunity without implying authority or selection. |
| 2. Program definition | Complete | Complete | Complete | Complete | Government Depository Section 2 distinguishes the Program from the enduring Capability. |
| 3. Institutional benefits | Complete | Complete | Complete | Complete | Government Depository Section 3 establishes institutional operating leverage and conditional public-finance positioning. |
| 4. Roles and responsibilities | Complete | Complete | Complete | Complete | Government Depository Section 2 and Appendix B distinguish public, banking, provider, and oversight responsibilities. |
| 5. Governance | Complete | Complete | Complete | Complete | Government Depository Section 2 and Appendix B define responsibility and decision gates without assigning legal authority through the Guide. |
| 6. Licensing or participation model | Complete | Complete | Complete | Complete | Government Depository Section 2 distinguishes license, implementation, driver, operations, and provider arrangements without pricing. |
| 7. Operating sovereignty | Complete | Complete | Complete | Complete | Government Depository Sections 3 and 4 preserve separate institutional deployment, data, credentials, relationships, and authority. |
| 8. DevOps model | Complete | Complete | Complete | Complete | Government Depository Sections 2 and 4 and Appendices B and E define delegated DevOps within institution-controlled boundaries. |
| 9. Settlement model | Complete | Complete | Complete | Complete | Government Depository Section 4 and Appendix E preserve institution-owned or established settlement relationships and no exclusive provider. |
| 10. Custody and authority boundaries | Complete | Complete | Complete | Complete | Government Depository Section 4 and Appendices B, D, and E keep public authority, banking custody, and software state distinct. |
| 11. Funding Events | Complete | Complete | Complete | Complete | Government Depository Section 4 and Appendix D retain the canonical recognition boundary. |
| 12. Treasury | Complete | Complete | Complete | Complete | Government Depository Section 4 and Appendix D preserve operational state without changing custody, appropriation, trust, or accounting character. |
| 13. Facilities | Complete | Complete | Complete | Complete | Government Depository Section 4 preserves service meaning while keeping public authority outside the Facility. |
| 14. Settlement Envelopes | Complete | Complete | Complete | Complete | Government Depository Section 4 assigns conditions and evidence without making the Envelope a settlement mechanism. |
| 15. Pay Codes | Complete | Complete | Complete | Complete | Government Depository Sections 4 and 5 and Appendix F preserve Pay Code as credential and vouchers as presentation only. |
| 16. Execution | Complete | Complete | Complete | Complete | Government Depository Section 4 defines execution through `emi-core`, the institution-specific driver, and approved provider relationships. |
| 17. Representative banking workflows | Complete | Complete | Complete | Complete | Government Depository Section 5 presents LGU assistance and seven related public-finance service domains. |
| 18. Business case | Complete | Complete | Complete | Complete | Government Depository Section 6 establishes the institutional and commercial case without guaranteed public business. |
| 19. Costs of participation | Complete | Complete | Complete | Complete | Government Depository Section 6 and Appendix C identify cost categories without inventing prices. |
| 20. Revenue or economic opportunities | Complete | Complete | Complete | Complete | Government Depository Section 6 identifies conditional service, deposit, activity, efficiency, and relationship value. |
| 21. Commercial Waterfall | Complete | Complete | Complete | Complete | Government Depository Section 6 and Appendix C provide a principles-level accountability model without prescribing prices or public fees. |
| 22. Pilot | Complete | Complete | Complete | Complete | Government Depository Section 7 defines a bounded pilot subject to public and banking authority. |
| 23. Phased rollout | Complete | Complete | Complete | Complete | Government Depository Section 7 defines evidence-based, non-automatic expansion. |
| 24. Success metrics | Complete | Complete | Complete | Complete | Government Depository Section 7 defines authority, attribution, execution, reconciliation, service, security, and control evidence without fixed targets. |
| 25. FAQ | Complete | Complete | Complete | Complete | Government Depository Appendix F answers role, authority, custody, credential, driver, deployment, settlement, and readiness questions. |
| 26. Glossary | Complete | Complete | Complete | Complete | Government Depository Appendix A defines canonical terms and public-finance qualifications without changing the shared grammar. |
| 27. Deployment architecture | Complete | Complete | Complete | Complete | Government Depository Appendix E preserves institution-controlled deployment, separate tenancy, delegated DevOps, integration, government-system, settlement, and production boundaries. |

The cross-program matrix remains the architectural parity control. The following business-question review supplements it without replacing or reorganizing its 27 mandatory coverage categories.

## Business-Question Completeness Matrix

| Section | Executive Question | Decision the section must enable | RBAP | Thrift Banks | Government Depository Banks | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Section 1 — Why This Program? | Why should the sector body launch this Program? | Decide whether the Program merits institutional consideration. | Complete | Complete | Complete | Complete | The Government Depository implementation establishes the public-trust and institutional-capability opportunity. |
| Section 2 — What Is the Program? | What exactly is the sector body being invited to launch? | Decide whether the proposed Program merits institutional evaluation. | Complete | Complete | Complete | Complete | The Government Depository implementation defines Program, Capability, roles, licensing, governance, and authority boundaries. |
| Section 3 — Why Should a Bank Participate? | What does an individual bank gain? | Understand the institution's prospective benefit from participation. | Complete | Complete | Complete | Complete | The Government Depository implementation explains conditional institutional benefit without implying selection. |
| Section 4 — How Does the Program Work? | How does the operating model work? | Understand how the model preserves institutional independence while enabling modern digital banking. | Complete | Complete | Complete | Complete | The Government Depository implementation covers public authority, custody, operating grammar, deployment, driver, and settlement boundaries. |
| Section 5 — Banking in Action | Show me how it actually works. | Assess the Program through representative banking workflows. | Complete | Complete | Complete | Complete | The Government Depository implementation uses LGU assistance and relates seven further public-finance services. |
| Section 6 — The Institutional Case | What kind of institution can participation help the bank become? | Decide whether the institutional case merits detailed commercial and implementation evaluation. | Complete | Complete | Complete | Complete | The Government Depository implementation covers institutional positioning, adaptability, costs, economic opportunities, public value, and sustainability. |
| Section 7 — Launching the Program | What happens after approval? | Decide whether to authorize or evaluate the proposed next step. | Complete | Complete | Complete | Complete | The Government Depository implementation defines authority assessment through controlled expansion. |

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
| Program Participants | Complete | Complete | Complete | Complete | Government Depository Appendix G adds public authority and oversight while preserving institutional and provider boundaries. |
| Funding Event | Complete | Complete | Complete | Complete | Government Depository Appendix G records external-event recognition without creating or characterizing public funds. |
| Treasury | Complete | Complete | Complete | Complete | Government Depository Appendix G distinguishes recognized, available, reserved, outstanding, unresolved, and resolved state. |
| Banking Operating Model | Complete | Complete | Complete | Complete | Government Depository Appendix G connects public instruction, depository banking service, x-change, driver, API, account, and approved settlement. |
| Deposit Flow | Complete | Complete | Complete | Complete | Government Depository Appendix G preserves depository authority, account records, Funding Event recognition, and operational Treasury state. |
| Payroll Flow | Complete | Complete | Complete | Complete | Government Depository Appendix G preserves government-employer authority, personnel attribution, execution, outcomes, and reconciliation. |
| Merchant Flow | Complete | Complete | Complete | Complete | Government Depository Appendix G references the canonical merchant Facility and institution-approved settlement sequence without making it the sector thesis. |
| Government Disbursement Flow | Complete | Complete | Complete | Complete | Government Depository Appendix G preserves public authority, Facility, beneficiary conditions, institution-authorized execution, and reconciliation. |
| Commercial Waterfall | Complete | Complete | Complete | Complete | Government Depository Appendix G adds public-program obligations to the canonical accountability sequence and contains no prices. |
| Deployment Architecture | Complete | Complete | Complete | Complete | Government Depository Appendix G preserves separate institution deployments, credentials, APIs, accounts, and authority. |

A future guide satisfies diagram parity by referencing the approved canonical diagram. It must not recreate or redefine a canonical diagram without an accepted editorial decision authorizing the deviation.

## Program Records

| Program | Guide path | Current stage |
| --- | --- | --- |
| RBAP Digital Banking Program | `docs/editorial/program-guides/rbap/rbap-digital-banking-program-guide.md` | The Executive Summary was revalidated under EDR-012 and locked without wording changes. Sections 1–7 and Appendices A–G remain canonical and locked; all mandatory coverage categories and diagram-registry requirements remain Complete. The complete editorial source is canonical and locked. Final publication governance, figure rendering, accessibility tagging, placement, and pagination remain pending. |
| Thrift Bank Digital Banking Program | `docs/editorial/program-guides/thrift-bank/thrift-bank-program-guide.md` | Canonical and editorially locked under the [Editorial Acceptance](thrift-bank/EDITORIAL_ACCEPTANCE.md). EDR-005 editorial work is complete for this implementation; future work proceeds through institution-specific editions. Executive Summary, Sections 1–7, and Appendices A–G are complete. No publication build is authorized. The separate [Phase 1 Institutional Study](../thrift-bank-digital-banking-program/README.md) remains the authoritative doctrinal source. |
| Government Depository Banking Program | `docs/editorial/program-guides/government-depository/government-depository-digital-banking-program-guide.md` | Version 0.9 is the editorially complete canonical review baseline. The Executive Summary, Sections 1–7, Appendices A–G, all mandatory coverage categories, and canonical diagram registry are Complete for parity. The synchronized Editorial Review Proof is active; publication freeze and Version 1.0 remain pending. Its first evidence-led institution-specific application is the PVB Program Guide draft. |
| Philippine Veterans Bank Digital Banking Program | `docs/institutions/philippine-veterans-bank/program-guide/philippine-veterans-bank-digital-banking-program-guide.md` | Version 0.9 is a complete institution-specific editorial draft derived from the accepted PVB Modernization Program. Executive Summary, Sections 1–7, Appendices A–G, and all mandatory coverage categories are Complete for editorial review. PVB approval, editorial lock, publication generation, commercial work, and implementation remain pending. |

## Required Gap Report

When any architectural or business-question item becomes `Missing`, Codex must identify:

1. the missing canonical requirement;
2. the business question or Executive Decision left unsupported;
3. why the requirement is mandatory;
4. whether the omission appears intentional;
5. the recommended remediation; and
6. whether an editorial decision record is required.

Codex must not convert a `Missing` item to `Complete` by inventing program terms, economics, responsibilities, workflows, or operating arrangements.
