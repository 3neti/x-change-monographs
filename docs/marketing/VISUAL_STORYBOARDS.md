# Marketing Visual Storyboards

## Purpose

These storyboards record the narrative studies from which the canonical compositions were promoted. The authoritative reusable objects now live in the [Composition System](COMPOSITION_SYSTEM.md) and [`compositions/`](compositions/README.md). This document remains the cross-composition narrative overview; it does not supersede an individual VIS specification.

## VIS-001 — Core Pay Code Journey

### Question answered

How can I send without knowing where the recipient banks or which provider they use?

### Visual argument

```text
GENERATE                         SHARE                          CLAIM

intended payment                portable credential           intended recipient
      ↓                                  ↓                           ↓
┌───────────────┐              || PAY CODE ||              ┌────────────────┐
│ institution   │ ───────────→ ordinary channel ─────────→ │ choose one     │
│ instruction   │                                          │ supported path │
└───────────────┘                                          └───────┬────────┘
                                                                     ↓
                                                                completion
```

### Story beats

| Beat | Illustration | What must be understood | What remains nested |
| --- | --- | --- | --- |
| 1. Generate | ILL-002 | The Pay Code originates from an intended payment under institutional authority | Authorization |
| 2. Share | ILL-003 | The credential can travel through an ordinary appropriate channel | Channel selection |
| 3. Claim | ILL-004 | The recipient presents the code and completes one supported journey | Choice, validation, settlement |
| Claim detail | ILL-005 | One Pay Code supports a bounded choice among available destinations | Only one destination is selected |

### Composition hierarchy

1. The three human verbs: Generate, Share, Claim.
2. One continuous Pay Code journey.
3. Recipient Choice discovered within Claim.
4. Institutional and validation cues, visible but quiet.

### Continuity rules

- Generate, Share, and Claim are equal first-level moments.
- No fourth step may sit beside them.
- The same Pay Code tile travels across all three moments.
- The recipient appears only after sharing begins and remains the active subject of Claim.
- Choice branches only inside the Claim frame and returns to one completion.
- Money never travels inside the Pay Code or communication channel.

### Caption relationship

The preferred labels are only:

```text
Generate.        Share.        Claim.
```

If supporting captions are used, they confirm rather than explain:

```text
Create the Pay Code.   Send it.   The recipient chooses.
```

### Format adaptations

| Format | Arrangement | Protected behavior |
| --- | --- | --- |
| Wide display | Three horizontal frames | Claim remains a single frame with nested choice |
| A4 portrait | Three stacked frames | Reading order remains top to bottom |
| Tri-fold | One frame per successive panel | Fold order must preserve Generate → Share → Claim |
| Landing page | Hero summary followed by one expanded frame per scroll section | The expanded sequence may not introduce new first-level steps |
| Presentation | One build per verb | Recipient Choice appears only when Claim is revealed |
| Social card | One compact triptych | Secondary institutional detail may be omitted, but actor roles may not change |

### Fifteen-second test

A first-time viewer should be able to repeat: “Create the code, send it, and the recipient claims it through a supported provider they choose.”

## VIS-002 — Institutional Network

### Question answered

How can different institutions participate without becoming one institution?

### Visual argument

```text
GENERATE                  OPERATING COORDINATION                  CLAIM
ILL-002                         ILL-006                         ILL-004

responsible institution ── governed instruction ── participating provider
       separate authority      x-change supports       separate responsibility
```

### Story beats

1. A responsible institution generates the credential for an authorized instruction.
2. A common operating layer coordinates the instruction without taking custody or authority.
3. A participating provider completes its part of the supported Claim journey.

### Composition hierarchy

The institutions remain visually stronger than the operating layer. The Pay Code remains the human-facing credential; the institutional diagram explains what supports it.

### Use boundary

VIS-002 belongs after VIS-001 in public collateral. It answers the institutional follow-up question and should not displace the human journey as the opening explanation.

## VIS-003 — Everyday Uses

### Question answered

Can the same simple journey apply to familiar payments and disbursements?

### Conceptual study

Use a shared three-part skeleton for every scenario:

```text
responsible source → || PAY CODE || → intended recipient
                      one grammar
```

Only the source, purpose cue, and recipient context change.

| Illustration | Source and purpose cue | Recipient moment | Semantic boundary |
| --- | --- | --- | --- |
| ILL-007 Payroll | Employer and approved payroll | Employee claims salary through a supported provider | The Pay Code does not calculate or authorize payroll |
| ILL-009 Insurance Claims | Insurer and approved claim | Claimant chooses a supported way to receive | The Pay Code does not decide claim eligibility |
| ILL-010 Merchant Refunds | Merchant and authorized refund | Customer receives without giving destination details upfront | Not chargeback processing or universal acceptance |
| ILL-011 Remittance | Sender with a responsible institution | Recipient presents the Pay Code through a supported channel | Not unlicensed direct remittance |
| ILL-013 Loan Proceeds | Lender and approved proceeds | Borrower or authorized recipient claims through a supported destination | The Pay Code does not approve the loan |
| ILL-014 Incentives | Organization and earned or approved incentive | Intended recipient claims once | Not speculative reward or stored value |

### Storyboard grid

```text
┌────────────┐  ┌────────────┐  ┌────────────┐
│ Payroll    │  │ Claim      │  │ Refund     │
│ source→code│  │ source→code│  │ source→code│
│ →recipient │  │ →recipient │  │ →recipient │
└────────────┘  └────────────┘  └────────────┘

┌────────────┐  ┌────────────┐  ┌────────────┐
│ Remittance │  │ Loan       │  │ Incentive  │
│ source→code│  │ source→code│  │ source→code│
│ →recipient │  │ →recipient │  │ →recipient │
└────────────┘  └────────────┘  └────────────┘
```

The repetition is intentional. It proves that the operating grammar remains stable while the institutional purpose changes.

### Composition rules

- Use the same Pay Code, arrow direction, and recipient posture in every tile.
- Give each use one recognizable purpose cue, not a detailed scene.
- Do not rank, feature, or enlarge one commercial use unless the publication has an approved audience reason.
- A small-format composition may show four representative tiles. The full conceptual study retains all six registered everyday-use illustrations.

## VIS-004 — Public Purpose

### Question answered

Can the same visual language support accountable public assistance?

### Conceptual study

```text
GOVERNMENT BENEFIT                          EMERGENCY ASSISTANCE
public authority                            responsible authority
      ↓                                            ↓
purpose + eligibility                       urgent purpose + conditions
      ↓                                            ↓
|| PAY CODE || → beneficiary                || PAY CODE || → recipient
      ↓                                            ↓
supported completion + evidence             controlled completion + evidence
```

### Composition rules

- Keep public authority, purpose, and accountability visible.
- Use urgency only in the emergency-assistance purpose cue; do not use disaster spectacle.
- Preserve the same recipient dignity used across the universal system.
- Evidence may be slightly more visible here, but it remains secondary to the human outcome.

## Full everyday-application proof

The complete Milestone 2 study combines VIS-003 and VIS-004 to cover all eight intended examples:

```text
Payroll · Government Benefits · Insurance Claims · Loan Proceeds
Merchant Refunds · Incentives · Remittances · Emergency Assistance
```

The eight scenarios are not eight product claims. Together they demonstrate that one visual grammar can represent different authorized institutional purposes.

## Illustration relationships

```text
ILL-001  establishes the human problem
   ↓
VIS-001  explains the public journey
   ├── ILL-002  Generate
   ├── ILL-003  Share
   └── ILL-004  Claim
          └── ILL-005  Recipient Choice
   ↓
ILL-006 / VIS-002  explains institutional participation
   ↓
VIS-003 + VIS-004  demonstrate application breadth
```

This hierarchy is canonical. A format may omit later layers for brevity, but it must not reorder them in a way that makes architecture precede the human idea.

## Storyboard approval criteria

A storyboard is ready for visual prototyping when:

- the question answered by each frame is singular and clear;
- the primary story remains Generate → Share → Claim;
- nested complexity has not become a public step;
- the same visual syntax works across all eight applications;
- the sequence remains understandable without captions; and
- doctrinal boundaries are carried by composition rather than warning text.

These storyboards do not constitute approved artwork, layout, branding, or rendered collateral.
