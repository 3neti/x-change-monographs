# Banking Program Guide Parity Checklist

## Authority

This checklist implements the [Canonical Banking Program Guide](CANONICAL_BANKING_PROGRAM_GUIDE.md). It must be reviewed during drafting, editorial review, approval, and publication preparation.

## Status Rules

| Status | Meaning |
| --- | --- |
| Complete | The guide answers the requirement sufficiently for its current editorial stage. |
| Planned | The approved architecture reserves the requirement, but substantive coverage has not yet been written. |
| Missing | The requirement is neither answered nor reserved in the guide. |
| Not Applicable | The requirement does not apply; the Notes cell must explain why. |
| Deviation Approved | An accepted editorial decision authorizes the departure; the Notes cell must cite it. |

`Not Applicable` without an explanation is incomplete. `Deviation Approved` without an accepted editorial decision reference is incomplete.

## Cross-Program Matrix

The RBAP column records the current architecture-frozen skeleton. The Thrift Banks and Government Depository Banks columns are planning entries only; no guide has been created for either program.

| Canonical Requirement | RBAP | Thrift Banks | Government Depository Banks | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| 1. Opportunity | Planned | Planned | Planned | Planned | Section 1. |
| 2. Program definition | Planned | Planned | Planned | Planned | Section 2. |
| 3. Institutional benefits | Planned | Planned | Planned | Planned | Section 3. |
| 4. Roles and responsibilities | Planned | Planned | Planned | Planned | Section 2. |
| 5. Governance | Planned | Planned | Planned | Planned | Section 2 and Appendix B. |
| 6. Licensing or participation model | Planned | Planned | Planned | Planned | Section 2. |
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

## Program Records

| Program | Guide path | Current stage |
| --- | --- | --- |
| RBAP Digital Banking Program | `docs/editorial/program-guides/rbap/rbap-digital-banking-program-guide.md` | Architecture frozen; substantive drafting not begun. |
| Thrift Bank Digital Banking Program | Not created | Anticipated. |
| Government Depository Banking Program | Not created | Anticipated. |

## Required Gap Report

When any cell becomes `Missing`, Codex must identify:

1. the missing canonical requirement;
2. the business question left unanswered;
3. why the requirement is mandatory;
4. whether the omission appears intentional;
5. the recommended remediation; and
6. whether an editorial decision record is required.

Codex must not convert a `Missing` item to `Complete` by inventing program terms, economics, responsibilities, workflows, or operating arrangements.
