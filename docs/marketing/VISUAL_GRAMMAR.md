# Marketing Visual Grammar

## Purpose

The Visual Grammar defines how marketing artwork explains Pay Code without relying on screenshots, interfaces, or institution-specific branding. The image should remain intelligible when most text is ignored.

The [Visual Principles](VISUAL_PRINCIPLES.md) govern design judgment. The [Icon System](ICON_SYSTEM.md) defines the semantic atoms used here. The [Illustration Concept Specifications](ILLUSTRATION_CONCEPT_SPECIFICATIONS.md) apply this grammar to ILL-001 through ILL-006. The [Composition System](COMPOSITION_SYSTEM.md) and [canonical VIS specifications](compositions/README.md) govern reusable visual arguments. The [Spatial Grammar](SPATIAL_GRAMMAR.md), [Motion Grammar](MOTION_GRAMMAR.md), and [Layout Wireframes](LAYOUT_WIREFRAMES.md) govern relationship, movement, and format adaptation. [Design Validation](DESIGN_VALIDATION.md) governs evaluation.

## Composition principle

Target approximately 80% illustration and 20% text. Use one visual argument per composition. Whitespace is part of the illustration system and should separate actors, moments, and choices.

## Canonical actors

| Actor | Visual role | Required distinction |
| --- | --- | --- |
| Sender | Authorizes or initiates the intended outcome | Must not appear to bypass institutional authority |
| Responsible institution | Governs the service, conditions, and instruction | Must not be replaced by the x-change logo |
| Pay Code | Human-readable uppercase alphanumeric credential framed by two parallel-line marks; persistent bridge between moments | Must never be drawn as a QR-only object, wallet, container of cash, or bank account |
| Recipient | Presents the credential and follows a supported journey | Must retain human agency without implying universal choice |
| Participating financial provider | Performs or supports regulated financial movement | Must remain visibly distinct from x-change software |
| Supported destination | An available bank, wallet, provider, or approved channel | Must be presented as supported, not unlimited |

## Canonical sequence

```text
Generate
    ↓
Share
    ↓
Claim
```

This is the public sequence. It describes the human experience.

VIS-001 is the canonical composition of this sequence. Its authoritative specification is [VIS-001 — Core Pay Code Journey](compositions/VIS-001.md). Publications adapt VIS-001; they do not invent parallel Pay Code journeys.

The richer lifecycle remains nested beneath it:

- **Generate** contains the authorized instruction and responsible institution.
- **Share** carries the credential from sender to recipient.
- **Claim** contains recipient choice, presentation, validation, and completion through a participating financial provider.

Authorization and Recipient Choice are important, but they are not additional first-level steps. The artwork should make the experience feel simple without contradicting the governance underneath it.

## Visual primitives

- **People:** simple, dignified figures without demographic caricature.
- **Institution:** a neutral governed-service frame, counter, seal, or structural gateway—not a specific bank façade.
- **Instruction:** a subtle line, document, or path behind the Pay Code.
- **Pay Code:** a distinct, legible alphanumeric credential framed by two parallel-line marks: `|| 7K9M-4R2P ||`. In visual studies, the sample is illustrative and non-functional. QR may accompany it only as a smaller optional encoding.
- **Choice:** a small set of clearly supported destinations discovered within Claim, never a separate first-level step or an infinite network.
- **Conditions:** a restrained checkpoint, verified mark, or ordered gate.
- **Completion:** a calm confirmation at the recipient; avoid exploding coins, celebratory cash, or speculative wealth imagery.
- **Evidence:** a quiet receipt or trace line when accountability matters.

## Arrow semantics

Arrows carry defined meaning:

- solid directional arrow — progression through a governed journey;
- branching arrow within Claim — recipient choice among supported options;
- dotted trace — evidence, status, or reconciliation;
- enclosing line — institutional responsibility or governed boundary.

Do not use an arrow from the Pay Code directly to cash. The credential enables presentation of an instruction; the participating financial provider performs the financial movement.

## Style

- timeless vector-style illustration;
- restrained geometry and line weight;
- warm paper or neutral background;
- approved x-change orange used as an accent, not a field of color;
- dark ink for institutional structure;
- limited secondary colors for human distinction and supported destinations;
- minimal gradients, shadows, dimensional effects, or decorative patterns.

## Prohibited visual shortcuts

Do not show:

- money stored inside a Pay Code;
- a Pay Code as a coin, account, wallet, gift certificate, or voucher balance;
- x-change taking custody of funds;
- a sender transferring directly to every bank or wallet in existence;
- unsupported institutional logos;
- screenshots or speculative product interfaces;
- a QR code alone labeled or moved as the Pay Code;
- QR larger than the framed alphanumeric credential or artwork implying that scanning is required;
- regulatory seals or approval marks;
- instant, guaranteed, universal, or frictionless completion;
- recipients avoiding identity, eligibility, compliance, or service conditions.

## Accessibility

Every illustration ID must include:

- a one-sentence functional description;
- the visual sequence it represents;
- any critical distinction that cannot be inferred from decorative artwork; and
- alt text suitable for the publication context.

Decorative repetition may be hidden from assistive technology, but the primary visual explanation may not.

## Responsive behavior

Renderers may rearrange a registered illustration from horizontal to vertical, simplify secondary detail, or divide it across panels. They may not change actor roles, arrow meaning, ordering, or the credential-versus-money distinction.

## VIS-001 publication parity

| Publication | Canonical use |
| --- | --- |
| Universal Pay Code Flyer | One dominant VIS-001 journey |
| Universal Pay Code Brochure | ILL-002, ILL-003, and ILL-004 occupy successive panels and reconstruct VIS-001 across the open spread |
| Universal Pay Code Landing Page | Compact VIS-001 hero followed by the same three moments in expanded reading order |
| Universal Pay Code Conference Sheet | One dominant VIS-001 journey supporting a brief conversation |
| Universal Pay Code Conference Banner | One distance-readable VIS-001 journey with no competing composition |

This parity is semantic rather than geometric. Each format may arrange the composition differently while preserving the same three actions, continuity, and nested Claim behavior.
