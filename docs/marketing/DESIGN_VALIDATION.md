# Marketing Design Validation

## Purpose

This document establishes a repeatable validation method for concepts, semantic icons, illustrations, compositions, publications, experience-surface adaptations, and rendered assets.

Validation asks whether the visual communicates the intended meaning truthfully and memorably. It does not score aesthetic preference.

## Evidence record

Each formal validation should record:

- object ID and version;
- object layer;
- lifecycle state;
- experience surface, if applicable;
- date;
- reviewer or participant profile;
- test performed;
- evidence observed;
- result: Pass, Pass with correction, or Fail;
- required correction; and
- decision owner.

An informal editorial check may precede formal testing, but it does not replace recorded evidence at approval or freeze gates.

## VAL-001 — Fifteen-Second Test

### Purpose

Determine whether a first-time viewer understands the primary idea almost immediately.

### Execution

1. Show the object once for no more than fifteen seconds in a context approximating its intended surface.
2. Remove it.
3. Ask: “What did this show?”
4. Record the participant's own words without prompting or correcting.

### Pass criteria

- The participant identifies the intended human action or problem.
- For VIS-001, the participant recalls Generate, Share, and Claim in the correct order or expresses their clear equivalents.
- No material doctrinal misunderstanding appears.

### Failure examples

- “The QR sends the money.”
- “The code is a wallet.”
- “It connects to every bank.”
- The participant notices provider icons but cannot describe the journey.
- The participant adds unrelated process steps.

### Appropriate milestones

Concept review, composition review, publication review, surface adaptation, and rendered-asset approval.

## VAL-002 — Caption Test

### Purpose

Determine whether the visual explains its intended idea without relying on prose.

### Execution

1. Remove or conceal the title, caption, labels, and explanatory copy.
2. Show the remaining visual.
3. Ask the participant to describe actors, action, order, and outcome.
4. Compare the response with the object's canonical question and accessibility summary.

### Pass criteria

- Actor roles are materially correct.
- Direction and sequence are understood.
- The human outcome remains clear.
- Captions would confirm rather than repair the visual.

### Failure examples

- Sender and recipient are confused.
- The Pay Code appears to be cash or a balance.
- Choice is mistaken for several payouts.
- Institutional boxes are understood only after reading labels.

### Appropriate milestones

Illustration concepts, compositions, prototypes, and rendered assets.

## VAL-003 — Doctrine Test

### Purpose

Confirm that simplification has not changed architectural truth or institutional roles.

### Execution

Review the object against canonical Editorial doctrine, Marketing Grammar, Visual Principles, Icon System, Visual Grammar, Spatial Grammar, and Motion Grammar. Test both what the object states and what a reasonable viewer could infer.

### Pass criteria

The object does not imply:

- stored value or wallet balance;
- money creation;
- money held inside the Pay Code;
- x-change as a financial institution, authority, or custodian;
- universal interoperability or acceptance;
- bypassed identity, eligibility, compliance, or service conditions;
- duplicated redemption or multiple payouts; or
- guaranteed completion.

Institutional responsibility, recipient agency, and singular completion remain intact.

### Failure examples

- Coins animate out of the Pay Code.
- The x-change mark encloses funds or institutions.
- One credential branches into several completed destinations.
- Provider choice appears limitless.
- Authorization disappears in a way that suggests anyone creates value.

### Appropriate milestones

Every lifecycle state from Conceptual onward. Mandatory before publication approval and freeze.

## VAL-004 — Memory Test

### Purpose

Determine whether the visual language is memorable rather than merely complete.

### Execution

1. Show the composition once in its intended context.
2. Remove it and introduce a brief neutral delay.
3. Ask the participant to sketch or describe the journey from memory.
4. Do not provide the words Generate, Share, Claim.

### Pass criteria for VIS-001

The response preserves:

```text
Generate → Share → Claim
                     └ choice
```

Equivalent human language is acceptable. Exact drawing style and wording are not required.

### Failure examples

- More than three first-level steps are remembered.
- Choose appears beside Claim rather than inside it.
- The participant sketches a platform hub surrounded by banks.
- The QR or Pay Code is remembered as the hero while the human action is lost.
- Several destination paths remain completed.

### Appropriate milestones

Canonical composition review, first-reader publication review, experience-surface validation, and frozen-asset approval.

## Supplemental checks

### Question Test

Can the viewer state the single question the object answers? Use during concept and illustration review.

### Focus Test

Does the human intention or outcome receive attention before technology and infrastructure? Use during composition and publication review.

### Singular-Outcome Test

Does one Pay Code result in one selected path and one completion? Use whenever Choice appears.

### Static-Equivalence Test

Does a motion composition retain the same meaning in a static or reduced-motion state? Use for motion and interactive surfaces.

### Accessibility Test

Does the accessible description convey purpose, actors, sequence, choice, and critical distinctions without duplicating decorative detail? Use before publication approval.

## Validation by layer

| Layer | Required validation |
| --- | --- |
| Concept | Question Test, Doctrine Test |
| Semantic Icon | Doctrine Test, relationship review |
| Illustration | Caption Test, Doctrine Test, Fifteen-Second Test where primary |
| Composition | Caption Test, Doctrine Test, Fifteen-Second Test; Memory Test for primary compositions |
| Publication | Fifteen-Second Test, Doctrine Test, Focus Test, accessibility review |
| Experience Surface | Fifteen-Second Test, Memory Test where VIS-001 leads, Static-Equivalence Test where motion exists |
| Rendered Asset | All tests required by its governed sources plus technical QA |

## Validation gates

### Before canonical-concept status

- Canonical question and core insight are stable.
- Source relationships are complete.
- Doctrine Test passes.
- Required comprehension tests have a defined method.

### Before prototype review

- The prototype is traceable to a canonical object.
- Captions and labels can be removed for testing.
- No visual style decision changes semantic meaning.

### Before approval

- Required tests have recorded evidence.
- Failures have been corrected and retested.
- Accessibility description is complete.
- Experience-surface adaptations preserve the source composition.

### Before freeze

- Approved source and rendered assets are versioned.
- Validation evidence is retained.
- Checksums and manifests exist where required.
- Future changes require explicit versioning.

## Failure handling

When a test fails, identify the failing layer.

- If an icon is ambiguous, correct the icon concept or its relationship.
- If an illustration answers several questions, divide or simplify it.
- If a composition is forgotten, reduce its hierarchy.
- If a publication competes with its primary composition, remove competing messages.
- If a renderer changes meaning, correct the renderer rather than rewriting the canonical source.

Do not add explanatory prose as the default repair for a failed visual.

## Governing principle

The objective is not unanimous aesthetic preference. The objective is consistent comprehension, memorability, accessibility, and doctrinal truth.
