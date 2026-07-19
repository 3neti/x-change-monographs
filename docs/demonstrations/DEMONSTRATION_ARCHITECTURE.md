# Demonstration Architecture

## Purpose

The x-change demonstration architecture governs controlled experiential artifacts. A demonstration artifact may help a recipient understand a customer journey, but it does not establish stored value, a claim against funds, production authority, implementation approval, or a commercial commitment.

The first implementation is the **Executive Demonstration Credential**, whose instrument type is **Demonstration Pay Code**.

## Publication layers

```text
Canonical Markdown
        ↓
Structured front matter
        ↓
Deterministic renderer
        ↓
SVG publication master
        ↓
PNG · PDF · print sheet
```

The Markdown record contains publication identity, recipient information, instrument data, redemption metadata, and human-readable front and back content. The renderer controls dimensions, typography, spacing, conditional regions, and imposition.

No manually edited graphic is canonical.

## Governed assets

The renderer may place separately governed brand and machine-readable assets referenced by the Markdown:

- the approved x-change logo;
- the canonical disbursement QR artwork; and
- future approved experiential-publication assets.

The QR artwork remains a separate asset so that its encoded destination can be verified independently. The canonical Markdown references the asset and records the corresponding redemption URL. Publication must stop if the encoded QR destination and the metadata URL differ.

## Size profiles

One source renders to three controlled profiles:

| Profile | Finished size | Purpose |
|---|---:|---|
| Executive card | 150 × 90 mm | Primary executive presentation artifact |
| Business card | 90 × 55 mm | Compact presentation format |
| Wallet card | 85.60 × 53.98 mm | ISO ID-1-compatible carrying format |

Each profile has a front and back. The A4 duplex print sheet contains two Executive-card credentials, matching the two Demonstration Pay Codes identified in the AllBank submission.

## Publication boundary

The Demonstration Pay Code is a controlled demonstration instrument. It is not a production credential, voucher, coupon, gift certificate, negotiable instrument, or promise of payment. A rendered credential must remain visibly identifiable as a demonstration.

The renderer must not invent a Pay Code or Demonstration Value. Empty values invoke the conditional rules defined in the [Demonstration Grammar](DEMONSTRATION_GRAMMAR.md).

## Change control

Changes to wording, grammar, conditional behavior, encoded destination, or canonical sizes require a source or governance revision. Layout corrections that do not alter the canonical content may be made in the renderer and must be recorded in the render verification report.
