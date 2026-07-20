# Philippine Veterans Bank Executive Submission Suite

## Publication Review Report

**Status:** Version 0.9 Executive Review Proof

**Publication date:** 20 July 2026

**Scope:** Board Paper, Executive Summary, and One-Page Decision Memo only

## Canonical source control

| Source | SHA-256 |
| --- | --- |
| `docs/institutions/philippine-veterans-bank/PHILIPPINE_VETERANS_BANK_MODERNIZATION_PROGRAM.md` | `6430e06d522f350148c420aa5dbc71e2e3a2a88abdc7ab38c361e73ffad27962` |
| `docs/institutions/philippine-veterans-bank/executive-submission/BOARD_PAPER.md` | `a08ad9d9f8a64c45096a4ff1ca89b6c72a61bf2b0a2d2604e58585f79acc62ee` |
| `docs/institutions/philippine-veterans-bank/executive-submission/EXECUTIVE_SUMMARY.md` | `6f0140a57ac5d6f9e9ca80e01f958f98e429cf3c2ab164b2b4168cb7bf9aec74` |
| `docs/institutions/philippine-veterans-bank/executive-submission/ONE_PAGE_DECISION_MEMO.md` | `865288642af7beccd2db1758fcb5f5cb9d96e43463a97c3770e51f979e1d49e7` |

All four hashes were verified before and after rendering. No canonical source changed.

## Generated artifacts

| Publication | Format | Pages | SHA-256 |
| --- | --- | ---: | --- |
| Board Paper | PDF | 3 | `8c4be44adec5bf0b7331b96b4b6d874b147cc7aa6d9fd7702681b4abb9cb2cd8` |
| Board Paper | HTML | — | `eb3fdede34d4213a6c144c7cf80dac8d50be0cf60bb547147a5836adf62992df` |
| Executive Summary | PDF | 2 | `43c31fdf91de01c6694f572336e3721b89ecb12127c087be773a8e6c52daf3aa` |
| Executive Summary | HTML | — | `b383cadab0ee552b99fbef6a256d6c09554ac0a1a294b7fc9968fccc72fcfe4d` |
| One-Page Decision Memo | PDF | 1 | `80b13ff1db927e44e10b86de8f2776a6b1f7d655156efbf6790763ca07c27608` |
| One-Page Decision Memo | HTML | — | `2da50b7d168a9600720c7cf7fe67da53b1dbb97e95b033643d61ec2c7d78d083` |

The machine-readable artifact record is preserved in `publication-manifest.json`.

## Publication system

- **Renderer:** WeasyPrint 66.0
- **Geometry:** A4, 595.28 × 841.89 points
- **Body typography:** Charter with Baskerville fallback
- **Executive hierarchy:** Avenir Next
- **Palette:** restrained x-change navy, warm neutral, and orange identity mark
- **Proof marking:** Version 0.9 Executive Review Proof on every physical page
- **Running elements:** publication identity, derivative status, and sequential page numbering
- **PDF metadata:** title, author, subject, version context, source identification, and source hashes

All fonts are embedded. The PDF font resources contain embedded Charter, Baskerville, and Avenir Next programs.

## Wordmark correction

The initial proofs allowed the masthead wordmark to inherit the proof label's uppercase transformation and to wrap after the hyphen. This produced `X-` and `CHANGE` on separate lines.

The correction was applied at the reusable rendering layer:

- `resources/publication-assets/styles/program-guide.css` now protects the Program Guide cover lockup and prepared-by wordmark with lowercase case preservation, non-wrapping flex behavior, fixed icon-to-wordmark grouping, and non-shrinking lockup elements. This shared stylesheet governs the RBAP, Thrift Bank, Government Depository, and AllBank Program Guide families.
- `scripts/publish-pvb-executive-submission.py` now emits the icon and wordmark as one structural `xchange-lockup`, with a protected lowercase `xchange-wordmark` child.
- The approved orange icon asset remains unchanged.

The white-paper and Movement templates already use a non-wrapping `cover-brand` container and lowercase `cover-wordmark`. Commercial proposal and cover-letter templates use the icon without a reconstructed wordmark. No additional template migration is required for the currently identified publication families.

## Navigation and links

- The Board Paper contains 10 bookmark entries: the document title and nine numbered sections.
- The Executive Summary contains one document-level bookmark.
- The Decision Memo contains six section bookmarks.
- Each HTML proof contains a repository-relative link to the canonical Modernization Program; the target resolves successfully.
- Each PDF contains one canonical-parent link annotation resolving to the same repository source in the review environment.

## Visual inspection

Every physical page was rendered to PNG and inspected at publication resolution.

The first page of each PVB artifact was re-inspected after regeneration. In every case, the icon and lowercase `x-change` wordmark remain grouped on one line, the hyphen is visible, and the lockup is clear of titles, metadata, margins, and page edges.

### Board Paper

- Three pages with a formal decision-paper rhythm.
- The decision request, institutional basis, Capability, discovery candidate, Management-validation requirements, governance boundary, return requirement, and illustrative resolution are clearly differentiated.
- The illustrative resolution remains intact and visibly separated from the legal and governance disclaimer.
- No isolated headings, clipped text, overflow, or accidental blank pages were found.

### Executive Summary

- Two pages with a spacious narrative rhythm.
- The page transition occurs after the institutional response and before the primary discovery candidate, preserving the approved progression.
- The bounded three-part decision is presented as a restrained executive panel.
- No clipping, overflow, broken paragraphs, or unreadable text was found.

### One-Page Decision Memo

- Exactly one A4 page.
- Body text renders at 9.15 points without artificial compression.
- Two governed reading columns preserve the canonical section order and keep each decision block intact.
- The decision requested, authorization boundary, Management return, and decision principle remain immediately scannable.
- No clipping, overflow, or unreadable text was found.

## Geometry and extraction checks

- Six physical pages were checked programmatically.
- No extracted word occupied coordinates outside an A4 media box.
- Page counts are 3, 2, and 1 respectively.
- No tables, diagrams, stock imagery, presentation slides, or commercial material were introduced.

## Shared-template regression check

The AllBank Executive Edition was rebuilt in a temporary QA location using the corrected shared Program Guide stylesheet.

- The cover lockup renders as lowercase `x-change` on one line.
- The icon and wordmark remain centered, proportional, unclipped, and visually grouped.
- Physical pagination remains 29 pages, matching the approved publication manifest.
- No unrelated title, cover, footer, or manuscript text changed.
- No regression artifact was added to the canonical build tree.

## Publication-only observations

- No textual issue was discovered that requires reopening a canonical source.
- The wordmark-wrap defect was confined to publication rendering. No manuscript or institutional content was changed.
- The PDF reader used for manifest inspection emitted a non-blocking font-table diagnostic for the fully embedded macOS fonts. Font embedding, text extraction, and visual rendering were verified and are unaffected.
- These PDFs are review proofs. They are not Version 1.0, First Editions, Board-approved publications, or publication-freeze artifacts.

## Recommendation

The three written proofs are ready for human visual review. No presentation deck or later-stage artifact should be generated until these proofs are accepted.
