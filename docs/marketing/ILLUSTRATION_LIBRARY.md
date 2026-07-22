# Marketing Illustration Library

## Purpose

The Illustration Library registers reusable conceptual artwork before final graphics are produced. Publications reference illustration IDs so the same visual idea can be refined once and reused across formats.

All illustrations are **Conceptual** in this milestone. No graphic asset is yet approved or frozen.

| ID | Name | Core visual story | Required elements | Must avoid | Status |
| --- | --- | --- | --- | --- | --- |
| ILL-001 | Unknown Recipient Destination | A sender knows the person and intended outcome but not where the person banks or receives money | Sender, recipient, unanswered destination symbols, human connection | Portraying the recipient as unidentified or unverified | Conceptual |
| ILL-002 | Generate Pay Code | A responsible institution turns an authorized instruction into a portable credential | Institution boundary, authorized instruction, Pay Code tile | Code created without authority; money placed inside code | Conceptual |
| ILL-003 | Share Pay Code | The credential moves from sender to recipient through an ordinary communication path | Sender, Pay Code, secure neutral communication path, recipient | Product UI, public posting, insecure broadcast | Conceptual |
| ILL-004 | Claim Money | The recipient claims the Pay Code, chooses an available supported destination, and completes the approved journey | Recipient, Pay Code, nested choice, quiet validation, completion | Direct code-to-cash arrow; guaranteed completion | Conceptual |
| ILL-005 | Recipient Choice | A reusable detail within Claim showing a limited set of supported destinations | Recipient, supported branch, two or three neutral destinations | Separate first-level step; infinite or universal provider availability | Conceptual |
| ILL-006 | Participating Institutions | Distinct institutions cooperate around a common instruction while retaining their roles | Responsible institution, x-change operating layer, participating providers, boundaries | Shared bank, pooled custody, x-change as regulator or financial institution | Conceptual |
| ILL-007 | Payroll | An employer-authorized salary instruction reaches an employee through a supported journey | Employer, authorized payroll, Pay Code, employee, supported provider | Claim of live payroll deployment | Conceptual |
| ILL-008 | Government Benefits | A responsible public institution authorizes assistance and the intended beneficiary presents the credential | Public authority, purpose, beneficiary, condition gate, participating provider | Political branding, entitlement guarantee, x-change as public authority | Conceptual |
| ILL-009 | Insurance Claims | An approved claim becomes a portable instruction for the claimant | Insurer, approved claim, Pay Code, claimant, supported destination | Pay Code deciding claim eligibility | Conceptual |
| ILL-010 | Merchant Refunds | A merchant-authorized refund reaches a customer without requiring the merchant to preselect the customer's destination | Merchant, refund instruction, Pay Code, customer, supported destination | Universal acceptance or chargeback equivalence | Conceptual |
| ILL-011 | Remittance | A sender requests a governed remittance; the recipient presents the Pay Code through a supported channel | Sender, responsible institution, Pay Code, recipient, provider completion | Unlicensed direct remittance or custody by x-change | Conceptual |
| ILL-012 | Emergency Assistance | An authorized assistance instruction reaches an eligible person through a controlled, observable journey | Responsible authority, urgency, recipient, conditions, provider, evidence | Bypassed controls, guaranteed eligibility, disaster spectacle | Conceptual |
| ILL-013 | Loan Proceeds | Approved loan proceeds are made available to the borrower or another authorized recipient through a supported journey | Lender, approved proceeds, Pay Code, recipient, supported destination | Pay Code approving the loan; automatic availability | Conceptual |
| ILL-014 | Incentives | An organization issues an approved incentive that the intended recipient claims through a supported journey | Organization, earned or approved incentive, Pay Code, recipient | Gaming imagery, speculative reward, universal redemption | Conceptual |

## Standard alt-text descriptions

- **ILL-001:** A sender wants to provide money to a known recipient but does not know which bank, wallet, or provider the recipient uses.
- **ILL-002:** A responsible institution represents an authorized financial instruction as a Pay Code credential; the code does not contain money.
- **ILL-003:** A sender securely communicates a Pay Code credential to the intended recipient.
- **ILL-004:** A recipient claims a Pay Code, chooses among available supported destinations, and completes the approved journey after quiet validation.
- **ILL-005:** Within the Claim moment, a recipient chooses among available supported destinations.
- **ILL-006:** Independent institutions retain their authority and financial roles while x-change coordinates the operating instruction between them.
- **ILL-007:** An employer authorizes payroll, an employee receives a Pay Code, and a participating provider completes the supported salary journey.
- **ILL-008:** A public institution authorizes a benefit or assistance instruction that an eligible recipient presents through a supported channel.
- **ILL-009:** An insurer-approved claim is represented by a Pay Code that the claimant presents through an available supported journey.
- **ILL-010:** A merchant issues an authorized refund instruction without first requiring the customer's bank or wallet details.
- **ILL-011:** A sender arranges a remittance and the recipient presents its Pay Code through a supported channel.
- **ILL-012:** A responsible institution authorizes emergency assistance and retains conditions, evidence, and accountability through completion.
- **ILL-013:** A lender makes approved loan proceeds available through a Pay Code that the borrower or another authorized recipient claims through a supported destination.
- **ILL-014:** An organization represents an approved incentive as a Pay Code that the intended recipient claims through a supported journey.

## Composition sets

| Set | Illustration sequence | Intended use |
| --- | --- | --- |
| VIS-001 Core Pay Code | ILL-002 → ILL-003 → ILL-004, with ILL-005 nested inside Claim | Flyer, landing-page hero, conference sheet |
| VIS-002 Institutional Network | ILL-002 → ILL-006 → ILL-004 | Executive collateral |
| VIS-003 Everyday Uses | ILL-007 + ILL-009 + ILL-010 + ILL-011 + ILL-013 + ILL-014 | Brochure use-case panel |
| VIS-004 Public Purpose | ILL-008 + ILL-012 | Government and public-finance collateral |

## Asset governance

Future artwork should be stored as separately governed vector masters under the publication-asset hierarchy, with derivative PNG or format-specific exports under `build/`. An approved asset must record its illustration ID, version, source path, alt text, dimensions, palette, and checksum.

Changing the meaning of an approved illustration requires a new version. Cropping, responsive rearrangement, or output conversion may not alter the registered visual story.
