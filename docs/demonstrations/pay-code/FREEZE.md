# Executive Demonstration Credential Publication Freeze

## Publication status

| Field | Value |
| --- | --- |
| Publication | Executive Demonstration Credential |
| Edition | First Edition |
| Version | 1.0 |
| Status | Production Baseline |
| State | Frozen |
| Freeze date | 19 July 2026 |
| Git tag | `executive-demonstration-credential-v1.0` |

## Rationale

Version 1.0 completed editorial review, renderer verification, production verification, and recipient-set implementation. It is the permanent production baseline for the Executive Demonstration Credential publication family.

The doctrine, publication grammar, canonical Markdown structure, recipient-set architecture, renderer behavior, visual identity, print layouts, and output profiles recorded by this version are frozen.

## Canonical artifacts

The following records collectively define Version 1.0.

### Source and governance

- `docs/demonstrations/pay-code/executive-demonstration-credential-v1.0.md`
- `docs/demonstrations/pay-code/metadata.yaml`
- `docs/demonstrations/pay-code/FREEZE.md`
- `docs/demonstrations/DEMONSTRATION_ARCHITECTURE.md`
- `docs/demonstrations/DEMONSTRATION_GRAMMAR.md`
- `scripts/publish-executive-demonstration-credential.py`

### Publication records and generated assets

- `build/demonstrations/pay-code/executive-demonstration-credential-v1.0/publication-manifest.json`
- `build/demonstrations/pay-code/executive-demonstration-credential-v1.0/render-verification-report.md`
- `build/demonstrations/pay-code/executive-demonstration-credential-v1.0/SHA256SUMS.txt`
- `build/demonstrations/pay-code/executive-demonstration-credential-v1.0/executive-demonstration-credential-v1.0-contact-sheet.png`
- `build/pdf/executive-demonstration-credential-v1.0.pdf`
- `build/pdf/executive-demonstration-credential-v1.0-executive-card.pdf`
- `build/pdf/executive-demonstration-credential-v1.0-business-card.pdf`
- `build/pdf/executive-demonstration-credential-v1.0-wallet-card.pdf`
- `build/pdf/executive-demonstration-credential-v1.0-print-sheet.pdf`
- Recipient-specific Garcia and Samonte publication, executive-card, business-card, and wallet-card PDFs recorded in the publication manifest.
- Recipient-specific SVG, PNG, and HTML assets recorded in the publication manifest.

The supplied QR artwork at `resources/publication-assets/demonstrations/x-change-disburse-qr.png` is part of the baseline and remains byte-preserved.

## Reproducibility

Rebuild Version 1.0 from the repository root with:

```text
python3 scripts/publish-executive-demonstration-credential.py
```

Verify the governed source and generated assets with:

```text
shasum -a 256 -c build/demonstrations/pay-code/executive-demonstration-credential-v1.0/SHA256SUMS.txt
```

The publication manifest records the source hash, renderer pipeline, recipient set, output profiles, QR hash, and generated artifact hashes. The Git tag identifies the complete frozen repository tree.

## Version history

### Version 1.0

Initial production release.

Introduced:

- canonical Markdown source;
- renderer architecture;
- recipient-set rendering;
- executive-card, business-card, and wallet-card profiles;
- duplex print-sheet generation;
- canonical Pay Code rendering;
- conditional rendering for optional sections;
- byte-preserved QR integration; and
- deterministic rendering and checksum verification.

## Future versioning policy

Version 1.0 is immutable and must not be overwritten.

Any future visual, typographic, metadata, renderer, branding, layout, profile, field, or publication-feature change requires a new version, such as Version 1.1 or Version 2.0. Future work must branch from this baseline while preserving the frozen Version 1.0 source, renderer, and artifacts.
