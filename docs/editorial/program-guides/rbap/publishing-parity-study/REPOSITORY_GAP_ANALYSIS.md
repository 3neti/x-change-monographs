# RBAP Repository Gap Analysis

## Purpose

This analysis compares the live RBAP repository organization with the completed Thrift publishing program. It addresses source-to-build separation, edition organization, traceability, navigation, and reproducibility without proposing doctrinal changes.

## Current RBAP Inventory

### Canonical and governance sources

- [Canonical manuscript](../rbap-digital-banking-program-guide.md)
- [Metadata](../metadata.yaml)
- [Program Guide README](../README.md)
- [Canonical guide architecture](../../CANONICAL_BANKING_PROGRAM_GUIDE.md)
- [Cross-program parity checklist](../../PROGRAM_GUIDE_PARITY_CHECKLIST.md)
- [Editorial Decision Register](../../../decisions/EDITORIAL_DECISION_REGISTER.md)
- [Separate strategic white paper](../../../rbap/00-modernizing-rural-banks.md)

### Publication assets and automation

- [RBAP publishing script](../../../../../scripts/publish-rbap-program-guide.py)
- [Shared Program Guide stylesheet](../../../../../resources/publication-assets/styles/program-guide.css)
- [Existing x-change brand asset](../../../../../resources/publication-assets/brand/x-change-logo-orange.png)

### Generated artifacts

- [Edition 1 PDF](../../../../../build/pdf/rbap-digital-banking-program-guide-edition-1.pdf)
- [Edition 1 HTML](../../../../../build/program-guides/rbap/edition-1/rbap-digital-banking-program-guide-edition-1.html)

The repository correctly keeps canonical Markdown and YAML outside `build/` and treats PDF and HTML as generated artifacts.

## Thrift Benchmark Inventory

In addition to equivalent manuscript, metadata, README, publisher, PDF, and HTML files, Thrift has:

- separate authoritative study and doctrine records;
- two canonical manuscript compositions;
- a shared appendix directory containing A–G;
- separate metadata for the Institutional Reference Edition;
- [Editorial Acceptance](../../thrift-bank/EDITORIAL_ACCEPTANCE.md);
- [Edition Comparison](../../thrift-bank/expanded-edition/EDITION_COMPARISON.md);
- [publication-specific Parity Report](../../thrift-bank/expanded-edition/PARITY_REPORT.md);
- edition-specific HTML directories and PDF names; and
- edition-aware publishing automation.

## Repository Gap Classification

| Repository area | Classification | RBAP finding | Recommended future state |
| --- | --- | --- | --- |
| Canonical manuscript location | Already satisfied | One clear canonical Program Guide source exists. | Preserve. |
| Source/build separation | Already satisfied | Markdown and YAML are source; PDF and HTML are under `build/`. | Preserve. |
| Shared house stylesheet | Already satisfied | RBAP originated the shared Program Guide stylesheet. | Reuse without modification unless QA finds a cross-edition defect. |
| Brand asset | Already satisfied | Existing logo asset is available and used. | Reuse. |
| Executive PDF and HTML companions | Already satisfied for first freeze | Both exist and are reproducible through the current script. | Preserve as legacy, then create canonical edition-named successors. |
| Appendix source directory | Required for parity | Appendices exist only as placeholders inside the main manuscript. | Create canonical Appendix A–G sources under the RBAP directory. |
| Institutional Reference source composition | Required for parity | No source composition exists. | Compose from the frozen narrative plus approved appendices. |
| Edition-specific metadata | Required for parity | One basic metadata file describes “Edition 1.” | Extend Executive metadata and add Institutional Reference metadata. |
| Editorial Acceptance | Required for parity | Missing. | Add after final lock and verification. |
| Edition Comparison | Required for parity | Missing. | Add with the two-edition implementation. |
| Publication parity report | Required for parity | Only cross-program parity exists. | Add an edition-specific completion report. |
| Edition-specific artifact paths | Required for parity | Current paths use `edition-1`. | Add explicit `executive-edition` and `institutional-reference-edition` paths; do not overwrite legacy artifacts. |
| Artifact page and hash records | Required for parity | Current RBAP metadata omits both. | Record after final builds. |
| Diagram source files | Required for parity | Appendix G and seven body illustrations remain placeholders. | Add governed source diagrams and render them through the pipeline. |
| Navigation | Required for parity | Current READMEs link only Edition 1. | Update existing indexes after acceptance; do not create a parallel index system. |
| Separate artifact registry | Recommended | No registry exists. | Use edition metadata first; introduce a catalogue only if later publication scale requires it. |
| Shared publisher library | Recommended | Thrift currently imports and extends the RBAP publisher. | Characterize both builds before extracting common code. |
| Dedicated inspection-study index | Optional | No established inspection-workflow index exists. | Keep this study self-contained; do not modify editorial indexes during inspection. |

## Recommended Future Directory Shape

The exact shape requires governance approval, but the following is consistent with the existing hierarchy:

```text
docs/editorial/program-guides/rbap/
├── rbap-digital-banking-program-guide.md
├── metadata.yaml
├── README.md
├── EDITORIAL_ACCEPTANCE.md
├── appendices/
│   ├── glossary.md
│   ├── governance.md
│   ├── commercial-waterfall.md
│   ├── treasury-grammar.md
│   ├── deployment-architecture.md
│   ├── faq.md
│   └── diagrams.md
└── institutional-reference-edition/
    ├── metadata.yaml
    ├── EDITION_COMPARISON.md
    └── PARITY_REPORT.md
```

The Institutional Reference source may be a deterministic composition of the canonical manuscript and appendices rather than a duplicated manuscript. If a material expanded narrative is later proposed, it should be separately reviewed and authorized.

Generated artifacts should follow explicit edition paths:

```text
build/program-guides/rbap/executive-edition/
build/program-guides/rbap/institutional-reference-edition/
build/pdf/rbap-digital-banking-program-guide-executive-edition-v1.pdf
build/pdf/rbap-digital-banking-program-guide-institutional-reference-edition-v1.pdf
```

The current `edition-1` HTML and PDF should remain unchanged.

## Git-History Findings

The relevant history confirms that the live architecture evolved incrementally:

- `9ee3db9` published the RBAP Edition 1, introduced the shared Program Guide stylesheet, and added the initial RBAP publisher.
- `546df5d` published the Thrift first edition using a Thrift-specific publisher built on the established Program Guide system.
- `90f98c8` added the Thrift expanded manuscript, edition comparison, parity report, and reference metadata.
- `aa8eda4` accepted and published the Thrift Executive and Institutional Reference editions, expanded the publisher, and recorded final metadata and governance.

This history argues against treating the Thrift directory shape as an original universal design. It is a proven implementation pattern that should be adapted deliberately to RBAP rather than copied mechanically.

## Artifact and Traceability Findings

| Artifact | Pages | SHA-256 recorded by inspection | Repository metadata state |
| --- | ---: | --- | --- |
| RBAP Edition 1 PDF | 39 | `083065b431cf886da8f8ac7349f8067b91911ad003390e1c3b5f328fb85f1ac1` | Path recorded; page count and hash absent. |
| Thrift Executive PDF | 16 | `cb4578ffeebbe7865e78ea38776f7cbe206fe8f1c339b285a74d98da77c5736f` | Path, page count, and hash recorded. |
| Thrift Institutional Reference PDF | 48 | `c9f7e0805f7b5684543a35febd855b6a1405f84782b91d8f9a241e6589143140` | Path, page count, and hash recorded. |

All three PDFs are A4, unencrypted, and visually consistent. All contain link annotations and extractable text. None is tagged for accessibility.

## Repository Conclusion

The most important repository gap is the absence of governed, reusable Appendix A–G and diagram sources from which an Institutional Reference Edition can be composed reproducibly. The current source/build separation and shared visual system are already sound and should not be redesigned.
