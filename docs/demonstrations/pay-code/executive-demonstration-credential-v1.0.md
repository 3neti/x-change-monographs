---
document_type: executive_demonstration_credential
title: Executive Demonstration Credential
instrument_type: demonstration_pay_code
edition: First Edition
version: "1.0"
status: production_baseline
publication_date: "2026-07-20"
layout: executive-card
orientation: front-back
branding:
  logo: resources/publication-assets/brand/x-change-logo-orange.png
  theme: orange
credentials:
  - recipient:
      name: Jesus Vicente Garcia
      title: President
      organization: AllBank
  - recipient:
      name: Digna Samonte
      title: Chief Technology Officer
      organization: AllBank
issuer:
  organization: Open Disbursement Technologies, Inc.
instrument:
  type: demonstration_pay_code
  instruction: Disbursable
  production_use: false
pay_code:
  value:
  handwritten: true
  render_style: canonical-double-bars
demonstration_value: 500
currency: PHP
redeem:
  qr: resources/publication-assets/demonstrations/x-change-disburse-qr.png
  url: https://redeem-x.laravel.cloud/disburse
render:
  hide_value_if_empty: true
  hide_recipient_if_empty: false
  credentials_per_print_sheet: 2
---

# Executive Demonstration Credential

## Front

Executive Demonstration

x-change

Payments take seconds.\
Work takes days.

Demonstration Pay Code

Instruction

Disbursable

Pay Code

```text
||                    ||
```

Demonstration Value

PHP 500

Prepared for

Each recipient in the credential set.

## Credential Set

1. Jesus Vicente Garcia, President, AllBank

2. Digna Samonte, Chief Technology Officer, AllBank

---

## Back

Redeem

Scan the QR Code

or visit

https://redeem-x.laravel.cloud/disburse

1. Enter the Pay Code.
2. Select **Redeem**.

Prepared exclusively for this submission.

Issued by

Open Disbursement Technologies, Inc.
