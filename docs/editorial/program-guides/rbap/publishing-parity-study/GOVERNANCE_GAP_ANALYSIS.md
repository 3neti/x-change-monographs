# RBAP Governance Gap Analysis

## Purpose

This analysis identifies the governance records required to move the RBAP Digital Banking Program from its first editorial freeze to two canonical publication editions. It does not grant authority, allocate a decision identifier, or change any editorial state.

## Existing Governance That Must Be Preserved

| Existing authority | Current effect | Treatment |
| --- | --- | --- |
| [Canonical Banking Program Guide](../../CANONICAL_BANKING_PROGRAM_GUIDE.md) | Governs the seven-section architecture and mandatory coverage categories. | Preserve and reference; do not duplicate. |
| [Program Guide Parity Checklist](../../PROGRAM_GUIDE_PARITY_CHECKLIST.md) | Records RBAP coverage and diagram status. | Update only during later implementation reviews. |
| [EDR-007](../../../decisions/EDITORIAL_DECISION_REGISTER.md#edr-007--rbap-is-the-program-protagonist) | Establishes RBAP as sponsor, convenor, steward, and administrator without making it a bank or settlement operator. | Frozen doctrine. |
| [EDR-008](../../../decisions/EDITORIAL_DECISION_REGISTER.md#edr-008--every-participating-bank-owns-its-digital-bank) | Establishes separate participating-bank deployments and operational sovereignty. | Frozen doctrine. |
| [EDR-009](../../../decisions/EDITORIAL_DECISION_REGISTER.md#edr-009--funds-remain-under-bank-custody) | Preserves bank custody and settlement authority. | Frozen doctrine. |
| [EDR-010](../../../decisions/EDITORIAL_DECISION_REGISTER.md#edr-010--funding-event-is-the-entry-point-to-treasury) | Establishes the approved Treasury entry point. | Frozen doctrine. |
| EDR-011 | Establishes **The Institutional Case** as the canonical Section 6 title. | Preserve. |
| [EDR-012](../../../decisions/EDITORIAL_DECISION_REGISTER.md#edr-012--executive-summary-review-follows-the-frozen-narrative) | Permits Executive Summary review now but prohibits final lock before substantive appendix completion and revalidation. | Mandatory sequencing control. |
| [RBAP metadata](../metadata.yaml) | Records the first editorial freeze and section locks. | Update later rather than replace. |
| [RBAP README](../README.md) | Records the canonical manuscript and current Edition 1 scope. | Update later rather than replace. |

EDR-013 is evidence of a successful two-edition decision for Thrift. It is not authority for RBAP and must not be applied by implication.

## Governance Gaps

| Gap | Classification | Why it matters | Required treatment |
| --- | --- | --- | --- |
| RBAP two-edition decision | Required for parity | No decision authorizes two canonical RBAP editions or defines their relationship. | Adopt the next available EDR only after this study is approved. |
| Edition roles and audiences | Required for parity | “Edition 1” does not distinguish Board use from institutional reference use. | Define Executive and Institutional Reference roles in the EDR and metadata. |
| Canonical source lineage | Required for parity | RBAP has no separate Institutional Study or Canonical Thesis equivalent. | Record the existing RBAP governance and frozen Program Guide as the controlling lineage; do not invent a new study solely for symmetry. |
| Legacy First Edition treatment | Required for parity | Renaming or overwriting the current artifact would obscure publication history. | Preserve existing PDF and HTML unchanged as first-freeze artifacts. |
| Executive Summary final lock | Required for parity | Canonicalization before appendix completion would violate EDR-012. | Complete A–G, revalidate the Summary, then record its lock. |
| Institutional Reference acceptance | Required for parity | No authority currently accepts a complete reference composition. | Perform a final lock ceremony and Editorial Acceptance after review and publication QA. |
| Edition Comparison | Required for parity | Readers need to know that neither edition supersedes the other. | Create a concise comparison record during implementation. |
| Publication-specific parity report | Required for parity | The cross-program checklist does not prove publication completeness. | Create an RBAP report tying mandatory coverage to final sources and artifacts. |
| Permitted future-change policy | Required for parity | Canonical publications need controlled correction and supersession rules. | Limit changes to factual/typographical corrections, navigation, artifact regeneration, or explicit EDR authority. |
| Artifact provenance fields | Required for parity | Current metadata omits approval, page count, hash, and canonical artifact state. | Extend edition metadata after final builds. |
| Editorial Acceptance | Required for parity | Section locks do not equal acceptance of two publication editions. | Create one RBAP acceptance record covering both editions. |
| Artifact registry as a separate file | Recommended | Metadata can already hold artifact identity and hashes. | Prefer metadata as the registry unless future scale justifies a separate catalogue. |
| Separate lock-ceremony document | Optional | Acceptance can record the lock ceremony without another file. | Add only if editorial practice requires an auditable pre-acceptance review record. |

## Recommended Two-Edition Decision Contents

The future RBAP decision should record:

1. the Executive Edition and Institutional Reference Edition as separate canonical publications;
2. the existing First Edition as the functional predecessor of the Executive Edition;
3. preservation of the existing First Edition PDF and HTML as legacy first-freeze artifacts;
4. the frozen canonical RBAP narrative as the shared doctrinal source;
5. the Executive Edition scope as front matter, Executive Summary, and Sections 1–7;
6. the Institutional Reference Edition scope as the same narrative plus substantive Appendices A–G;
7. the audiences and institutional purposes of each edition;
8. that neither edition supersedes the other;
9. that the editions may differ in supporting depth but may not differ in doctrine;
10. that EDR-007 through EDR-012 remain authoritative;
11. the approved appendix-source and diagram-source model;
12. the final-lock and artifact-verification requirements; and
13. the rule that future doctrinal change requires a new EDR.

The next available identifier appears to be `EDR-014`, but this study does not reserve or allocate it.

## Canonical Lineage Recommendation

RBAP should not manufacture an Institutional Study solely to reproduce the Thrift folder structure. The repository already distinguishes the [strategic rural-bank white paper](../../../rbap/00-modernizing-rural-banks.md) from the Program Guide. That white paper supplies strategic context but should not silently become the operational doctrinal authority.

The future decision should expressly record this lineage:

```text
Canonical Banking Program Guide architecture
                +
RBAP decisions EDR-007 through EDR-012
                +
Frozen RBAP Program Guide narrative
                ↓
        RBAP publication editions
```

Any additional Treasury or cross-corpus authority used in the appendices should be cited explicitly rather than treated as implied doctrine.

## Acceptance and Lock Procedure

The final governance sequence should be:

1. approve the two-edition architecture;
2. complete and approve Appendix sources A–G;
3. revalidate and lock the Executive Summary under EDR-012;
4. confirm Sections 1–7 remain unchanged except for permitted factual, typographical, or cross-reference corrections;
5. approve edition-specific metadata and source composition;
6. generate and verify both editions;
7. record page counts and SHA-256 values;
8. complete publication-specific parity review;
9. perform the RBAP lock ceremony; and
10. adopt Editorial Acceptance and update navigation.

## Governance Balk Rule

Publication must stop if any of the following is true:

- an appendix remains a placeholder;
- a required FAQ remains unanswered;
- a required canonical diagram is absent;
- the Executive Summary has not been revalidated after appendix completion;
- the edition relationship lacks EDR authority;
- a publication source introduces doctrine not traceable to the frozen narrative or an accepted decision;
- an artifact lacks final metadata, page count, or hash; or
- implementation would modify the accepted Thrift publication without a separate approved change.

## Governance Conclusion

The most important governance gap is the absence of an RBAP-specific decision authorizing and bounding the two-edition model. Appendix completion and publishing work should not begin as canonical publication work until that decision has been reviewed and accepted.
