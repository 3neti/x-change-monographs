# Executive Demonstration Credential

The Executive Demonstration Credential is the canonical experiential artifact for a controlled x-change customer journey. Its instrument type is **Demonstration Pay Code**.

## Source records

- [Canonical Markdown](executive-demonstration-credential-v1.0.md)
- [Metadata](metadata.yaml)
- [Publication Freeze](FREEZE.md)
- [Demonstration Architecture](../DEMONSTRATION_ARCHITECTURE.md)
- [Demonstration Grammar](../DEMONSTRATION_GRAMMAR.md)

**Edition:** First Edition

**Version:** 1.0

**Status:** Production Baseline

**State:** Frozen

The source contains no generated Pay Code. The write-in area is intentionally blank and always retains the canonical double bars. The approved Demonstration Value is PHP 500. The A4 print sheet contains two credentials for the AllBank submission.

Generated SVG, PNG, PDF, print-sheet, manifest, checksum, and verification assets are maintained under `build/demonstrations/pay-code/executive-demonstration-credential-v1.0/` and `build/pdf/`.

## Version history

### Version 1.0

Initial production release. It introduced the canonical Markdown source, renderer architecture, recipient-set rendering, executive-card, business-card, and wallet-card profiles, duplex print-sheet generation, canonical Pay Code rendering, conditional optional sections, byte-preserved QR integration, and deterministic checksum verification.

Version 1.0 is immutable. Future changes require a new explicitly versioned publication.
