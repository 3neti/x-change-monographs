# Submission Portfolio Architecture

## Purpose

The Submission Portfolio architecture converts a governed declaration of approved publications into a recipient-ready delivery package. It provides a stable reading sequence, separates screen and print use, records provenance, and makes the complete delivery checksum-verifiable.

The architecture does not rewrite, recompress, or supersede the included publications.

## Canonical layers

```text
Approved publication artifacts
             ↓
Canonical institution submission manifest
             ↓
Deterministic portfolio builder
             ↓
Staged Submission Portfolio
             ↓
Verified ZIP archive and external checksum
```

The institution manifest is the canonical declaration of the portfolio. The staged directory and ZIP are generated delivery artifacts.

## Portfolio structure

Every portfolio contains:

- a concise portfolio guide in PDF and plain text;
- a `SCREEN` profile for electronic reading and internal circulation;
- a `PRINT` profile for physical production;
- a `MANIFEST` profile containing the governed declaration, checksum manifest, submission status, and source-artifact provenance.

The manifest determines filenames, order, source paths, expected versions, expected page counts, and expected SHA-256 values. The builder refuses to package a source whose governed checksum or page count does not match.

## Publication boundaries

Approved source PDFs are copied byte-for-byte. A different packaged filename does not create a new publication, edition, or revision.

Packaging derivatives are limited to navigation and verification records, including the portfolio README, submission-status record, source-artifact record, checksum manifest, and ZIP archive. They must not modify publication doctrine or content.

## Reproducibility

The builder uses stable ordering, fixed archive timestamps, governed source checksums, and deterministic README rendering. A successful build verifies:

1. source presence and checksum;
2. declared publication version and page count;
3. packaged-copy identity;
4. expected portfolio contents;
5. PDF readability;
6. governed QR destination where declared;
7. checksum integrity; and
8. extraction equivalence between the ZIP and staged directory.

Generated portfolios and archives remain under `build/submissions/`. Repository history preserves the architecture, canonical manifests, and builder rather than release archives.

## Extension to future institutions

A future institution receives its own directory and manifest under `docs/submissions/<institution>/`. The common builder consumes that manifest. Institution-specific names, recipients, source artifacts, ordering, and dates belong in the manifest rather than in the builder.
