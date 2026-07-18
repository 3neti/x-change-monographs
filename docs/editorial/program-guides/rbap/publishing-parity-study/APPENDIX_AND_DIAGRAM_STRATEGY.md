# RBAP Appendix and Diagram Strategy

## Purpose

This strategy defines how the unfinished RBAP appendices and visual placeholders should be completed without reopening the frozen Sections 1–7 or importing Thrift doctrine. It authorizes no drafting or diagram production.

## Implementation Update — 18 July 2026

The subsequent appendix-completion assignment authorized Appendices A–G while explicitly deferring the separate Executive Edition and its governance. The approved low-risk source decision was to populate the appendix area already reserved inside the canonical manuscript rather than reorganize or duplicate it. Appendix G now contains the governed Mermaid source. Sections 1–7 remain byte-preserved, so their seven literal visual-placeholder labels remain in the frozen narrative; Appendix G supplies the completed corresponding figures for later renderer substitution.

## Sequencing Rule

All required Appendices A–G must be substantively complete before the Executive Summary can be revalidated and locked.

This follows [EDR-012](../../../decisions/EDITORIAL_DECISION_REGISTER.md#edr-012--executive-summary-review-follows-the-frozen-narrative), which permits review of the Summary after the numbered sections are frozen but requires appendix completion before final claim, terminology, and cross-reference validation.

The Executive Edition may exclude the appendices from its published scope. Their completion is nevertheless a prerequisite to locking its Executive Summary because they complete the guide's required coverage and terminology.

## Appendix Strategy

| Appendix | Current state | Executive Edition | Institutional Reference Edition | Source strategy | New work required |
| --- | --- | --- | --- | --- | --- |
| A — Glossary | Complete | Exclude | Include | Controlled terms derived from the frozen guide, canonical architecture, and accepted EDRs. | Eligible for appendix review. |
| B — Program Governance | Complete | Exclude | Include | Roles, decision rights, exclusions, and gates derived from Sections 2, 4, and 7 and EDR-007 through EDR-009. | Eligible for appendix review. |
| C — Commercial Waterfall | Complete | Exclude | Include | Principles-level accountability model derived from Sections 2 and 6 without prices. | Eligible for commercial-boundary review. |
| D — Treasury Grammar | Complete | Exclude | Include | Institutional reference derived from Section 4 and EDR-010. | Eligible for Treasury review. |
| E — Deployment Architecture | Complete | Exclude | Include | Responsibility, tenancy, credential, data, CI/CD, audit, settlement, and portability boundaries. | Eligible for architecture review. |
| F — Frequently Asked Questions | Complete | Exclude | Include | All reserved and necessary institutional questions answered from frozen doctrine. | Eligible for appendix review. |
| G — Program Diagrams | Complete source | Exclude as an appendix | Include | Twenty-five RBAP-specific Mermaid sources governed by the parity registry and frozen narrative. | Rendering and body placement remain future publication work. |

### Appendix source location

The implementation keeps Appendices A–G embedded in the appendix area already reserved by the canonical manuscript. This avoids reorganizing the source, prevents duplicated appendix text, and allows the complete reference source to remain one canonical Markdown document. Mermaid blocks in Appendix G are the governed diagram source. Future publication automation may extract or render them without moving the canonical content.

The separate appendix-directory model remains a valid future publishing option only if explicit governance later requires reusable source composition. It is not required for the present appendix-completion state.

### Appendix drafting control

For every appendix, the editor should maintain a traceability table during review:

| Proposed statement | Frozen RBAP source or accepted EDR | New doctrine? | Resolution |
| --- | --- | --- | --- |

Any statement that lacks a source must be removed, qualified as an open decision, or submitted for explicit governance. It must not be introduced merely because an analogous statement exists in the Thrift appendices.

## Diagram Classification

RBAP currently has two distinct visual classes.

### Canonical diagrams

The [parity checklist](../../PROGRAM_GUIDE_PARITY_CHECKLIST.md#canonical-diagram-parity) identifies ten canonical diagram requirements:

1. Program Participants
2. Funding Event
3. Treasury
4. Banking Operating Model
5. Deposit Flow
6. Payroll Flow
7. Merchant Flow
8. Government Disbursement Flow
9. Commercial Waterfall
10. Deployment Architecture

These belong in Appendix G of the Institutional Reference Edition. They are governed representations of roles, states, responsibilities, or flows and should be reviewed as canonical sources rather than decoration.

### Editorial illustrations

The frozen body contains seven labelled visual placeholders:

1. Familiar Remittance Pattern
2. Operating Perspectives
3. Operating Flow
4. End-to-End Banking Activity
5. Manager's Check and Pay Code Remittance
6. Behind the Counter
7. Operating Model

These are explanatory illustrations embedded in the narrative. They should appear in both editions because they belong to Sections 4 and 5. They do not independently define doctrine and must remain subordinate to the surrounding prose.

Before canonical publication, each placeholder should be either:

- converted into an approved publication figure that expresses exactly the existing source; or
- expressly accepted as a restrained textual schematic under the publication system.

The label “Visual placeholder” should not remain in a final canonical publication unless Editorial Acceptance explicitly permits it.

## Edition Placement

| Visual class | Executive Edition | Institutional Reference Edition |
| --- | --- | --- |
| Body editorial illustrations | Include in their existing narrative positions after approval. | Include in the same positions. |
| Appendix G canonical diagrams | Exclude. | Include in full. |
| New decorative diagrams | Exclude. | Exclude unless separately approved. |
| Thrift-specific diagrams | Exclude. | Exclude as sources; use only as layout and rendering references. |

## Diagram Source and Styling Recommendation

Use text-based diagram sources, preferably Mermaid where it can express the concept cleanly. Render them as native SVG through the publishing pipeline. Reuse the established diagram typography, monochrome palette, spacing, and print rules from the Thrift publication system.

Shared components may include:

- font and stroke treatment;
- node spacing and print-safe sizing;
- figure captions;
- page-break behavior;
- SVG text preservation; and
- accessibility descriptions.

The diagram content must be RBAP-specific. In particular, Deployment Architecture and Program Participants must preserve:

- separate bank-owned or bank-controlled deployments;
- separate databases, credentials, release approvals, CI/CD, records, and audit trails;
- each bank's customer and deposit relationships;
- each bank's direct settlement relationship and authority;
- RBAP's program-administration role;
- ODTI's software-licensing and maintenance role;
- delegated DevOps responsibility; and
- the distinction between shared settlement infrastructure and shared software tenancy.

## Diagram Lock Requirements

Before Appendix G can be marked complete:

- all ten registry diagrams must exist or have an approved deviation;
- every diagram must be traceable to the frozen guide or accepted EDR;
- terminology must match the canonical Treasury grammar;
- diagram source must remain in the editorial source tree, not only inside generated HTML or SVG;
- diagrams must render legibly in A4 PDF and HTML;
- captions and text alternatives must be present;
- no diagram may imply shared custody, shared tenancy, RBAP settlement operation, or bank authority held by x-change; and
- the publication-specific parity report must identify the exact source file for each diagram.

## Appendix and Diagram Conclusion

Appendices A–G are required completion work, even though only the Institutional Reference Edition will publish them. The body illustrations and canonical diagrams should share a visual language but remain different governance classes: illustrations explain the narrative; canonical diagrams record the approved operating model.
