# RBAP Edition Strategy

## Decision to Be Reviewed

RBAP should adopt two canonical publication editions derived from the same frozen Program Guide doctrine:

```text
Canonical RBAP Program Guide
        ├── Executive Edition
        └── Institutional Reference Edition
```

Neither edition should supersede the other. They should serve different reading and governance purposes while remaining source-traceable to the same accepted RBAP narrative.

## Executive Edition Strategy

### Finding

The existing RBAP First Edition already functions as the Executive Edition.

It was deliberately published as a self-contained Board paper. Its scope is:

- cover and publication information;
- table of contents;
- Executive Summary; and
- Sections 1–7.

It excludes Appendices A–G. This is the same functional boundary used by the completed Thrift Executive Edition.

Publishing parity is not a page-count or manuscript-length exercise. The existing RBAP edition should therefore not be rewritten or compressed merely to resemble the physical extent of the Thrift edition.

### Required changes before canonicalization

| Potential change | Assessment |
| --- | --- |
| Classification as Executive Edition | Required. |
| RBAP-specific two-edition EDR | Required. |
| Executive Summary revalidation | Required under EDR-012 after A–G are complete. |
| Canonical Version 1.0 metadata | Required. |
| Editorial Acceptance | Required. |
| Edition-specific HTML and PDF names | Required for canonical traceability. |
| Preservation of current Edition 1 artifacts | Required. |
| Frozen Section 1–7 rewriting | Not required and prohibited absent a factual or governance defect. |
| Limited editorial restructuring | Not recommended. Only permitted factual, typographical, cadence, or cross-reference corrections may be considered under existing controls. |
| New HTML companion | Not conceptually required because one already exists; a canonical edition-named rebuild is required. |

### Canonical publication identity

Recommended future identity:

```text
RBAP Digital Banking Program
Program Guide
Executive Edition
First Edition
Version 1.0
```

The exact cover hierarchy should preserve the approved RBAP title and subtitle.

### Legacy treatment

The current files should remain immutable:

- `build/pdf/rbap-digital-banking-program-guide-edition-1.pdf`
- `build/program-guides/rbap/edition-1/rbap-digital-banking-program-guide-edition-1.html`

Metadata should later identify them as preserved first-editorial-freeze artifacts. Canonical Executive Edition artifacts should use new edition-specific names rather than overwriting them.

## Institutional Reference Edition Strategy

### Recommendation

RBAP should receive an Institutional Reference Edition.

### Intended audience

- RBAP Board and executive leadership;
- participating rural-bank presidents and executive sponsors;
- Program governance and administration;
- Operations, Treasury, Risk, Compliance, Legal, and Technology leaders;
- implementation and DevOps providers acting within delegated scopes;
- settlement and strategic partners requiring an authoritative operating reference.

### Recommended scope

- the same revalidated Executive Summary;
- the same frozen Sections 1–7;
- substantive Appendices A–G;
- canonical diagrams; and
- edition-specific front matter, contents, metadata, and running identity.

### Source materials that can be reused

- the complete frozen [RBAP Program Guide](../rbap-digital-banking-program-guide.md);
- EDR-007 through EDR-012;
- the [Canonical Banking Program Guide](../../CANONICAL_BANKING_PROGRAM_GUIDE.md);
- the [Program Guide Parity Checklist](../../PROGRAM_GUIDE_PARITY_CHECKLIST.md);
- approved Treasury and operational-sovereignty sources already represented in the frozen guide;
- existing roles, governance, commercial, deployment, and FAQ questions in the guide; and
- the shared publication stylesheet and brand asset.

The Thrift appendices may provide structural and publishing examples. Their institution-specific language is not an RBAP source.

### Content requiring development

The principal new editorial work belongs in Appendices A–G:

- controlled glossary definitions;
- detailed Program governance and decision boundaries;
- conceptual Commercial Waterfall;
- Treasury grammar reference;
- deployment and responsibility architecture;
- complete FAQ answers; and
- RBAP-specific canonical diagram sources.

These should explain and organize existing doctrine. They must not extend it silently.

### Separate expanded body manuscript

A separate expanded Sections 1–7 manuscript is not currently justified. The canonical narrative already answers the seven required executive questions and contains substantial operating explanation. An expanded body should be considered only if appendix review proves that a mandatory business question remains unanswered and cannot be resolved through a reference appendix.

Any such expansion would require a separate editorial proposal, doctrine traceability, and review. It must not become an automatic consequence of copying the Thrift repository structure.

## Relationship Between Editions

| Dimension | Executive Edition | Institutional Reference Edition |
| --- | --- | --- |
| Primary role | Board and executive decision paper | Comprehensive institutional operating and implementation reference |
| Narrative source | Frozen canonical guide | Same frozen canonical guide |
| Executive Summary | Revalidated and locked | Same approved Summary |
| Sections 1–7 | Included unchanged | Included unchanged |
| Appendices A–G | Excluded | Included |
| Diagrams | Approved body illustrations only | Body illustrations plus Appendix G canonical diagrams |
| Doctrine | Frozen | Inherited without modification |
| Supersession | Does not supersede Reference Edition | Does not supersede Executive Edition |

## Edition Acceptance Criteria

The editions should not be canonicalized until:

- the two-edition EDR is accepted;
- Appendices A–G are substantively complete and approved;
- all required canonical diagrams exist;
- the Executive Summary is revalidated and locked under EDR-012;
- source composition is deterministic;
- both HTML and PDF artifacts pass publication QA;
- page counts and SHA-256 values are recorded;
- Edition Comparison and publication parity records are complete; and
- Editorial Acceptance records the final lock and future-change rules.

## Edition Strategy Conclusion

The recommended strategy is classification and completion, not reconstruction:

- canonicalize the existing Board-paper scope as the Executive Edition after EDR-012 is satisfied; and
- create the Institutional Reference Edition by adding approved reference apparatus to the same frozen narrative.
