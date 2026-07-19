# Demonstration Grammar

## Canonical terms

Use:

- **Executive Demonstration Credential** — the publication artifact;
- **Demonstration Pay Code** — the instrument type;
- **Pay Code** — the credential presented within the artifact; and
- **Demonstration Value** — an optional declared value used only when supplied by the canonical source.

Do not use:

- demo card;
- Pay Code stub;
- sample voucher;
- sample Pay Code;
- voucher;
- coupon; or
- gift certificate.

## Pay Code invariant

The Pay Code always uses the canonical double-bar presentation:

```text
|| {PAY CODE} ||
```

If `pay_code.value` is empty, the renderer must preserve the two double bars and provide an unlabelled light write-in field:

```text
||                    ||
```

It must not insert placeholder text, Xs, dashes, or an invented code.

## Conditional regions

### Demonstration Value

If `demonstration_value` is empty, the renderer removes the entire Demonstration Value region. It must not display a zero value, dash, currency-only label, or empty placeholder.

### Recipient

If all recipient fields are empty, the renderer removes the entire personalization region and collapses the layout. It must not display an empty “Prepared for” label.

### Pay Code

A supplied Pay Code is normalized to uppercase and grouped exactly as recorded in the canonical source. The renderer adds the double bars; the source value must not include them.

## Redemption invariant

The redemption URL is read from `redeem.url`. The QR path is read from `redeem.qr`. The renderer must verify that the QR decodes to the same URL before publication.

The back uses only the following operating direction:

1. Enter the Pay Code.
2. Select **Redeem**.

Do not add promotional claims, security claims, “easy steps,” or implementation explanation.

## Presentation rule

Typography, physical size, color, spacing, QR placement, crop treatment, and print imposition are renderer responsibilities. The canonical Markdown must not be altered to solve a layout issue.
