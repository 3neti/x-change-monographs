# RBAP Publishing Parity Assessment

## Study Status

- **Inspection phase:** Preliminary, inspection only
- **Inspection date:** 18 July 2026
- **Live repository revision:** `aa8eda4`
**Implementation authority:** None

This assessment determines whether the completed Thrift Bank two-edition publishing architecture is appropriate for the RBAP Digital Banking Program. It records findings and recommendations only. It does not change RBAP doctrine, editorial status, edition identity, metadata, publication scripts, or generated artifacts.

The detailed companion studies are:

- [Governance Gap Analysis](GOVERNANCE_GAP_ANALYSIS.md)
- [Repository Gap Analysis](REPOSITORY_GAP_ANALYSIS.md)
- [Edition Strategy](EDITION_STRATEGY.md)
- [Appendix and Diagram Strategy](APPENDIX_AND_DIAGRAM_STRATEGY.md)
- [Publishing Automation Strategy](PUBLISHING_AUTOMATION_STRATEGY.md)
- [Implementation Roadmap](IMPLEMENTATION_ROADMAP.md)
- [Risks and Safeguards](RISKS_AND_SAFEGUARDS.md)

## Inspection Basis

The live repository is the source of truth. The supplied review ZIP was unavailable at its stated `/mnt/data` location, so the identically named review ZIP in `~/Downloads` was inspected. Its fourteen entries match their live-repository counterparts byte for byte. The ZIP is therefore reliable evidence of the completed Thrift publication package, but it is not a complete source archive.

The inspection covered:

- the [canonical RBAP manuscript](../rbap-digital-banking-program-guide.md), [metadata](../metadata.yaml), and [README](../README.md);
- the [canonical guide architecture](../../CANONICAL_BANKING_PROGRAM_GUIDE.md) and [parity checklist](../../PROGRAM_GUIDE_PARITY_CHECKLIST.md);
- the [Editorial Decision Register](../../../decisions/EDITORIAL_DECISION_REGISTER.md), especially EDR-007 through EDR-013;
- the [Thrift Program Guide publishing directory](../../thrift-bank/README.md), both edition metadata files, Editorial Acceptance, Edition Comparison, Parity Report, appendix sources, and diagram sources;
- the [RBAP publisher](../../../../../scripts/publish-rbap-program-guide.py), [Thrift publisher](../../../../../scripts/publish-thrift-bank-program-guide.py), and [shared Program Guide stylesheet](../../../../../resources/publication-assets/styles/program-guide.css);
- generated PDF and HTML artifacts, build paths, names, pagination, hashes, navigation, and visual page composition; and
- the Git history that introduced the RBAP first publication and the subsequent Thrift edition architecture.

The comparison is limited to publishing-program maturity. It does not evaluate or compare banking doctrine, institutional strategy, target-audience substance, operating assumptions, product positioning, or manuscript length.

## High-Level Verdict

The two-edition architecture is appropriate for RBAP, subject to an RBAP-specific governance decision.

The existing RBAP First Edition already performs the functional role of an Executive Edition: it is a self-contained Board paper consisting of front matter, the Executive Summary, and Sections 1–7, with appendices excluded. It should be canonicalized through classification, governance, final Executive Summary revalidation, edition metadata, and renamed publication artifacts. Frozen Sections 1–7 do not require restructuring.

RBAP should also receive an Institutional Reference Edition. The safest source model is the same frozen canonical narrative plus completed Appendices A–G. A separate expanded body manuscript should not be presumed necessary. It should be created only if a later, explicit review identifies an unanswered implementation question that cannot be resolved in the appendices without reopening the frozen narrative.

## Current RBAP State

### Canonical and frozen

- The [RBAP Digital Banking Program Guide manuscript](../rbap-digital-banking-program-guide.md) is the canonical guide source.
- Sections 1–7 are editorially complete, locked, and frozen.
- The approved title hierarchy, seven-section architecture, executive questions, and canonical narrative are frozen.
- EDR-007 through EDR-010 preserve the RBAP protagonist, bank-owned deployments, custody boundaries, and Treasury entry point.
- EDR-011 preserves the canonical Section 6 title, **The Institutional Case**.

### Still in review or planned

- The Executive Summary is complete but remains **In Review** under EDR-012.
- EDR-012 requires it to be revalidated and locked only after all required appendices are substantively complete.
- Appendices A–E contain placeholders.
- Appendix F contains twelve unanswered questions.
- Appendix G is structurally present, but its canonical diagrams have not been created.
- The parity checklist still marks Governance, Treasury, Commercial Waterfall, FAQ, Glossary, and Deployment Architecture as Planned for RBAP.

### Typeset and published

- [RBAP First Edition PDF](../../../../../build/pdf/rbap-digital-banking-program-guide-edition-1.pdf): 39 physical A4 pages; SHA-256 `083065b431cf886da8f8ac7349f8067b91911ad003390e1c3b5f328fb85f1ac1`.
- [RBAP First Edition HTML](../../../../../build/program-guides/rbap/edition-1/rbap-digital-banking-program-guide-edition-1.html).
- The publication uses the shared Program Guide stylesheet and has functional contents navigation, running elements, tables, callouts, and print composition.

These artifacts publish a first editorial freeze. They are not yet recorded as canonical, locked Version 1.0 editions.

## Thrift Benchmark State

The completed Thrift publishing program has:

- an authoritative Institutional Study, Canonical Thesis, Editorial Reconciliation, and Architectural Notes;
- a locked canonical Program Guide;
- a canonical Executive Edition;
- a canonical Institutional Reference Edition;
- shared substantive Appendices A–G;
- sixteen Mermaid diagram sources rendered as native SVG;
- edition-specific metadata with source lineage, audience, role, approval date, page count, hash, and artifact paths;
- [Editorial Acceptance](../../thrift-bank/EDITORIAL_ACCEPTANCE.md);
- [Edition Comparison](../../thrift-bank/expanded-edition/EDITION_COMPARISON.md);
- [publication-specific Parity Report](../../thrift-bank/expanded-edition/PARITY_REPORT.md);
- EDR-013 authority for the two-edition publication model;
- PDF and HTML companions for both editions; and
- a publisher with explicit `executive` and `institutional-reference` modes, appendix aggregation, and Mermaid-to-SVG rendering.

The Executive Edition is 16 A4 pages with SHA-256 `cb4578ffeebbe7865e78ea38776f7cbe206fe8f1c339b285a74d98da77c5736f`. The Institutional Reference Edition is 48 A4 pages with SHA-256 `c9f7e0805f7b5684543a35febd855b6a1405f84782b91d8f9a241e6589143140`.

## Publishing-Parity Classification

| Area | Classification | Finding |
| --- | --- | --- |
| Frozen seven-section narrative | Already satisfied | RBAP Sections 1–7 are canonical and frozen. |
| Executive-edition functional scope | Already satisfied | Existing First Edition already has the correct Board-paper scope. |
| House typography and page system | Already satisfied | RBAP and Thrift use the same shared stylesheet and visual family. |
| PDF and HTML companions | Already satisfied for the current freeze | Both exist, but their identity and records are not yet canonical edition records. |
| Two-edition decision authority | Required for parity | No RBAP decision currently authorizes two canonical editions. |
| Executive Summary final lock | Required for parity | EDR-012 sequencing is incomplete. |
| Substantive Appendices A–G | Required for parity | All remain incomplete or unanswered. |
| Canonical diagram sources | Required for parity | The registry is present, but RBAP sources are absent. |
| Institutional Reference Edition | Required for parity | No canonical source composition, metadata, or artifacts exist. |
| Edition-specific metadata and traceability | Required for parity | RBAP metadata lacks canonical state, approval, roles, page count, hash, and edition relationships. |
| Editorial Acceptance and lock ceremony | Required for parity | No final RBAP publication acceptance exists. |
| Edition Comparison and publication parity report | Required for parity | These records do not exist for RBAP. |
| Edition-aware automation | Required for parity | The RBAP publisher has one fixed scope. |
| Artifact registry | Recommended | Edition metadata can serve as the registry without a separate system. |
| Shared publishing framework | Recommended | Consolidation should follow characterization, not precede publication. |
| PDF accessibility tagging | Optional parity enhancement | All inspected Program Guide PDFs are presently untagged. |

## Appropriate RBAP Publication Model

```text
RBAP canonical doctrine and governance
                ↓
Canonical RBAP Program Guide
        ├── Executive Edition
        └── Institutional Reference Edition
```

The two editions should be publishing peers, not replacements:

- the Executive Edition supports Board and executive evaluation;
- the Institutional Reference Edition supports executive sponsors and responsible Program, Operations, Treasury, Risk, Compliance, Technology, implementation, and partner functions; and
- both remain traceable to the same frozen RBAP narrative and approved RBAP decisions.

## Principal Conclusion

RBAP does not need doctrinal modernization to achieve publishing parity. It needs completion and governance of the publication system around the doctrine it already has.

Implementation should not begin until the proposed edition roles, source relationship, appendix model, diagram authority, legacy-artifact treatment, and permitted future changes are approved through an explicit Editorial Decision Record.
