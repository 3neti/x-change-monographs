# AllBank Executive Submission Portfolio

| Field | Value |
| --- | --- |
| Document type | Institution Submission Portfolio |
| Edition | First Edition |
| Version | 1.0 |
| Submission date | 20 July 2026 |
| Status | Production Submission |
| State | Ready for Delivery |

This portfolio assembles the approved AllBank cover letter, commercial proposal, AllBank Executive Edition Program Guide, and Executive Demonstration Credentials into separate screen and print profiles.

The [canonical submission manifest](submission.yaml) governs the recipients, delivery sequence, source paths, expected page counts, expected checksums, and packaged filenames. It does not change the edition, version, doctrine, or frozen status of any included publication.

## Build

From the repository root:

```text
python3 scripts/build-submission-portfolio.py docs/submissions/allbank/submission.yaml
```

The command writes the staged portfolio, deterministic ZIP archive, and external archive checksum to:

```text
build/submissions/allbank/
```

Generated delivery artifacts are intentionally excluded from repository history. The canonical manifest, shared builder, and governance documents are version-controlled.

## Related correspondence

Electronic delivery of this portfolio is recorded separately in the canonical outbound correspondence record:

- [Submission of the x-change Executive Portfolio for AllBank](../../correspondence/allbank/2026-07-20-executive-submission-email.md)

The correspondence record does not modify or reopen this frozen portfolio.
