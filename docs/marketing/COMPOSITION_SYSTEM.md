# Marketing Composition System

## Purpose

The Composition System governs reusable visual arguments assembled from canonical illustrations. It makes Composition a first-class layer between Illustration and Publication.

A publication selects compositions. It does not reconstruct their meaning.

## Composition philosophy

A composition is not a layout template. It is a governed relationship among illustrations, messages, actors, and attention.

An illustration answers one question. A composition arranges one or more illustrations into one memorable argument. A publication assembles those arguments for a particular audience and experience surface.

```text
Concept
   ↓
Semantic Icon
   ↓
Illustration
   ↓
Visual Composition
   ↓
Publication
   ↓
Experience Surface
   ↓
Rendered Asset
```

Each layer may adapt the layer above it. It may not redefine it.

## Composition anatomy

Every canonical composition records:

- **Composition ID** — stable `VIS-###` identifier;
- **Name** — short human-readable title;
- **Question answered** — the single reader question served;
- **Core insight** — the idea a viewer should retain;
- **Source illustrations** — governed `ILL-###` components;
- **Semantic icon dependencies** — conceptual atoms required;
- **Reading order** — the relationship among moments;
- **Primary hierarchy** — what the viewer should notice first, second, and third;
- **Nested complexity** — important detail that must not become a peer step;
- **Permitted adaptations** — rearrangements that preserve meaning;
- **Prohibited mutations** — changes that would alter doctrine or identity;
- **Accessibility summary** — a complete nonvisual description;
- **Validation profile** — required design tests; and
- **Lifecycle status** — current governance state.

## Composition hierarchy

### Primary compositions

Primary compositions explain the Pay Code idea itself. They may lead a publication.

- VIS-001 — Core Pay Code Journey
- VIS-005 — Problem Before Solution

### Detail compositions

Detail compositions enlarge one part of a primary composition without creating a competing journey.

- VIS-006 — Recipient Choice Within Claim

### Supporting compositions

Supporting compositions answer a follow-up institutional or application question after the primary story is understood.

- VIS-002 — Institutional Network
- VIS-003 — Everyday Applications
- VIS-004 — Public Purpose

A supporting composition must not displace VIS-001 when a publication's first responsibility is to explain Pay Code.

## Canonical registry

| ID | Name | Class | Principal sources | Status |
| --- | --- | --- | --- | --- |
| VIS-001 | Core Pay Code Journey | Primary | ILL-002, ILL-003, ILL-004; ILL-005 nested | Canonical concept |
| VIS-002 | Institutional Network | Supporting | ILL-002, ILL-006, ILL-004 | Canonical concept |
| VIS-003 | Everyday Applications | Supporting | ILL-007, ILL-009, ILL-010, ILL-011, ILL-013, ILL-014 | Canonical concept |
| VIS-004 | Public Purpose | Supporting | ILL-008, ILL-012 | Canonical concept |
| VIS-005 | Problem Before Solution | Primary | ILL-001, VIS-001 | Canonical concept |
| VIS-006 | Recipient Choice Within Claim | Detail | ILL-004, ILL-005 | Canonical concept |

The authoritative specifications live under [`compositions/`](compositions/README.md).

## Naming

- Use stable identifiers in the form `VIS-###`.
- Use names that describe the visual argument, not a publication or medium.
- Do not encode audience, institution, format, orientation, or campaign into a canonical composition name.
- A format-specific crop or arrangement retains the same VIS ID when meaning is unchanged.
- A materially different visual argument requires a new VIS ID.

## Composition relationships

```text
VIS-005 Problem Before Solution
    ├── ILL-001 Unknown Recipient Destination
    └── VIS-001 Core Pay Code Journey
            ├── ILL-002 Generate
            ├── ILL-003 Share
            └── ILL-004 Claim
                    └── VIS-006 Recipient Choice Within Claim

VIS-002 explains institutional support after VIS-001.
VIS-003 and VIS-004 demonstrate application breadth after VIS-001.
```

Compositions may contain illustrations or subordinate compositions. Circular dependencies are prohibited.

## Composition reuse

A publication references a composition by ID and declares its role.

```yaml
composition:
  - id: VIS-005
    role: opening
  - id: VIS-001
    role: primary_journey
  - id: VIS-003
    role: application_breadth
```

The publication may add governed message blocks, calls to action, reading order, and experience surfaces. It may not redraw the composition as a different process.

Reuse means preserving:

- the question answered;
- source-illustration roles;
- sequence and direction;
- nested relationships;
- singular outcome;
- accessibility meaning; and
- doctrinal boundaries.

Reuse does not require identical geometry, scale, typography, or visible detail.

## Permitted adaptation

A publication or renderer may:

- arrange a composition horizontally or vertically;
- reveal its moments progressively;
- reduce secondary detail for distance or small formats;
- isolate a registered detail composition;
- adapt whitespace and emphasis to an experience surface; or
- use a static equivalent of governed motion.

It may not:

- add a first-level step to VIS-001;
- make authorization a peer of Generate;
- make Recipient Choice a peer of Claim;
- show one Pay Code producing several completions;
- place infrastructure ahead of the human problem;
- change the credential into money; or
- imply universal provider participation.

## Composition lifecycle

| State | Meaning | Permitted action |
| --- | --- | --- |
| Proposed | A communication need has been identified | Explore relationships without publication use |
| Conceptual | Meaning and sources are documented | Conduct semantic and doctrine review |
| Canonical concept | Semantics, relationships, and validation profile are approved | Reference from draft publications and prototypes |
| Prototype review | One or more noncanonical visual studies exist | Test comprehension without changing canonical meaning |
| Approved | A governed visual master has passed review | Use in approved publications |
| Frozen | Versioned composition and assets form a publication baseline | Change only through explicit versioning |
| Superseded | A later composition replaces its role | Retain history and reference replacement |

Milestone 4 establishes canonical concepts only. It does not approve visual masters or rendered assets.

## Change control

### Revision within the same VIS ID

The following may remain within one composition version when semantic meaning is unchanged:

- clearer wording in the accessibility summary;
- removal of redundant secondary detail;
- clarified permitted adaptations;
- stronger validation criteria; or
- corrected cross-references.

### New version or composition required

Explicit review is required when a change affects:

- the question answered;
- source illustration roles;
- first-level sequence;
- choice behavior;
- institutional responsibility;
- credential-versus-money meaning; or
- the expected remembered sketch.

A new audience crop is not a new composition. A new argument is.

## Experience surfaces

An Experience Surface is the context in which a publication is encountered. It is distinct from file format and renderer.

| Surface ID | Surface | Typical behavior |
| --- | --- | --- |
| `print` | Handheld or placed physical publication | Self-contained, stable reading order |
| `presentation` | Facilitated executive or public explanation | Progressive reveal with presenter control |
| `web` | Responsive, scroll-led or interactive reading | Layered disclosure with static equivalence |
| `event` | Distance viewing or brief in-person encounter | Immediate recognition and minimal text |
| `motion` | Time-based explanation | Governed sequence and reduced-motion equivalent |
| `social` | Brief small-screen encounter | One composition or one registered detail |
| `email` | Message-led introduction | Compact visual preview linked to deeper material |
| `documentation` | Governed reference and implementation context | Complete semantic explanation and traceability |

A publication may target more than one surface. The surface influences attention and adaptation; it does not redefine the composition.

## Publication declaration examples

```text
Conference Banner
    = VIS-001
    + headline
    + primary message

Flyer
    = VIS-001
    + primary message
    + invitation

Brochure
    = VIS-005
    + VIS-001
    + VIS-003 / VIS-004
    + invitation

Landing Page
    = VIS-005
    ↓ VIS-001
    ↓ VIS-002
    ↓ VIS-003 / VIS-004
    ↓ invitation
```

These equations declare composition. They do not prescribe layout.

## Validation requirement

Every new or revised composition must use the canonical [Design Validation](DESIGN_VALIDATION.md) profile appropriate to its lifecycle. VIS-001 always requires the Fifteen-Second, Caption, Doctrine, and Memory Tests.

## Governing principle

Publications should become recognizable because they share visual arguments, not because they repeat one layout.
