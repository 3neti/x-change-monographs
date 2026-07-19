# Render Verification Report

- Publication: Executive Demonstration Credential, First Edition, Version 1.0
- Instrument type: Demonstration Pay Code
- Canonical source SHA-256: `c197bf039d19b1894c4a1de88602ad81e2a0bec02c939cab3ca7614bf05365d2`
- Pay Code presentation: `|| {PAY CODE} ||`; blank write-in field rendered
- Demonstration Value: PHP 500
- QR destination: `https://redeem-x.laravel.cloud/disburse`
- Supplied QR artwork SHA-256: `a6c5569bf5f48fcbd6994e66b0884b3dcc059bd59e3968bc029e61e325a38619`; unchanged during publication
- Supplied QR artwork and all three rendered back PNG profiles decoded successfully: Passed
- Printed redemption URL exactly matches canonical metadata, including scheme: Passed
- Blank Pay Code field contains canonical double bars and no divider or guide: Passed
- Empty Demonstration Value and recipient validation rendering collapses both blocks: Passed
- Print-sheet personalization: 2 copies for Jesus Vicente Garcia, as specified by canonical Markdown
- Executive, business-card, and wallet-card front/back generation: Passed
- Publication PDFs: 2 pages per size profile
- A4 duplex print sheet: 2 pages, 2 credentials
- Protected Cover Letter, Commercial Proposal, and Program Guide hashes: Unchanged
- Canonical Markdown source freeze: Passed
- Page-by-page visual inspection: Passed — all eight PDF pages, the contact sheet, and the blank-optional-fields validation rendering were inspected; no clipping, overflow, unintended guides, margin defects, or duplex-placement discrepancies were found
