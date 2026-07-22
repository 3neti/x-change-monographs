# Marketing Publication Architecture

## Purpose

Marketing introduces x-change and Pay Code to a first-time reader in approximately 30 seconds to one minute. Its immediate task is comprehension, not institutional persuasion, technical explanation, or commercial conversion.

The reader should leave with four answers:

1. **What is it?** A Pay Code is a portable credential for an authorized instruction.
2. **Why does it exist?** The sender should not need to know where the recipient keeps or receives money.
3. **How does it work?** An instruction is authorized, represented by a Pay Code, presented through a supported journey, validated, and completed through participating financial infrastructure.
4. **Why does it matter?** The recipient can use a supported destination without forcing the sender to design the transaction around that destination in advance.

The public story is deliberately simpler than the operating lifecycle:

```text
Generate → Share → Claim
```

Generate contains authorization. Claim contains recipient choice, validation, and settlement. Those concepts remain governed without becoming additional first-level marketing steps.

## Publication-family boundary

```text
Marketing
    ↓
Program Guide
    ↓
Proposal
    ↓
Executive Submission Portfolio
    ↓
Proof of Concept
    ↓
Commercial Engagement
```

Marketing opens the door. It does not perform the work of the publications or engagements that follow.

| Family | Primary responsibility | Marketing boundary |
| --- | --- | --- |
| Editorial | Establish doctrine and institutional reasoning | Marketing compresses approved doctrine; it does not redefine it |
| Commercial | Establish a specific offer, price, term, or engagement path | Marketing contains no institution-specific commercial commitment |
| Experiential | Let a reader experience a governed customer journey | Marketing may reference the idea of a journey but does not issue a credential |
| Submission | Assemble approved artifacts for governed delivery | Marketing collateral may be included as a source artifact after approval |
| Correspondence | Preserve formal institutional communications | Marketing is not evidence that a communication was sent |

## Canonical source model

```text
Approved editorial doctrine
          ↓
Marketing Grammar + Visual Grammar
          ↓
Illustration Concepts + Storyboards + Wireframes
          ↓
Canonical Markdown publication
          ↓
Format-specific renderer
          ↓
PDF · HTML · SVG · print · web · presentation · social
```

Markdown owns message, sequence, illustration references, accessibility descriptions, and calls to action. YAML owns series metadata and render intent. Renderers own dimensions, typography, responsive behavior, imposition, and format-specific production details.

Illustration concept specifications own semantic anatomy and comprehension tests. Visual storyboards own frame order and illustration relationships. Layout wireframes own composition hierarchy across formats. None of these sources constitutes final artwork.

No manually edited render becomes canonical.

### Source conventions

- YAML front matter identifies the publication, version, status, governed message blocks, and illustration sets.
- Machine-readable enum values use lowercase `snake_case`; reader-facing labels retain natural capitalization.
- Versions and milestone numbers are quoted strings.
- The Markdown body contains public copy in reading order.
- Labels such as `Illustration`, `Illustration sequence`, and `Alt text` are production directives. A renderer replaces them with the governed asset and accessible description rather than printing the labels as body copy.
- Sections whose headings end in `— not publication copy` contain renderer or composition guidance and must be excluded from recipient-facing output.
- HTML comments may carry deployment guidance such as a future link destination and must not appear in rendered collateral.

## Universal and institution-specific layers

The first series is universal. It may be used across banks, electronic money issuers, FinTechs, payment providers, and public-finance institutions without naming or favoring any institution.

Future institution-specific collateral must inherit from the universal grammar. It may adapt audience language, examples, calls to action, and approved institutional context. It may not redefine Pay Code, custody, authority, settlement responsibility, or the role of x-change.

## Content composition

Every marketing publication assembles governed primitives:

- one primary message;
- one audience-appropriate headline;
- one explanation block;
- one visual sequence using registered illustration IDs;
- one restrained boundary statement where required; and
- one next-step invitation.

The target composition is approximately 80% illustration and 20% text. Text quantity may vary by medium, but the visual story must remain understandable without reading every sentence.

## Publication classes

| Class | Typical attention window | Primary purpose |
| --- | ---: | --- |
| Flyer | 20–30 seconds | Establish the core idea |
| Tri-fold brochure | 45–90 seconds | Explain the idea and representative uses |
| Conference sheet | 30–60 seconds | Support a brief in-person conversation |
| Landing page | 60–120 seconds | Introduce, demonstrate, and route to deeper material |
| Banner or display | 5–10 seconds | Create recognition and prompt a question |
| Social card | 3–8 seconds | Communicate one message block |
| Animation storyboard | 20–45 seconds | Show the instruction journey over time |

## Governance gates

Before publication, a marketing source must pass:

1. **Doctrine check** — every claim is traceable to approved x-change language.
2. **Message check** — one idea remains dominant.
3. **Boundary check** — the collateral does not imply that the Pay Code holds money, works everywhere, bypasses institutions, or guarantees an outcome.
4. **Visual check** — the illustration communicates the intended journey without UI screenshots or misleading fund flows.
5. **Accessibility check** — every illustration reference has a meaningful text alternative.
6. **Format check** — the renderer adapts to the source rather than rewriting it.
7. **Status check** — draft, review, approved, and frozen states are explicit.

## Change control

Changes to the primary message, canonical definitions, operating boundaries, or illustration semantics require review against the Editorial corpus. Format-specific layout corrections belong in renderers. Approved publication wording must not be silently changed during rendering.
