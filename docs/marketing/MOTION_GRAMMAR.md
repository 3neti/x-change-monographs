# Marketing Motion Grammar

## Purpose

The Motion Grammar defines what movement means in the x-change Marketing Design System. It governs temporal sequence and state change without prescribing animation software, duration, easing, frame rate, or output format.

Motion must explain the journey. It must not decorate it.

## Canonical movement

```text
Generate        Share          Claim

appears    →    moves     →    stops
                              choice expands
                              one path is selected
                              validation occurs
                              completion occurs
                              evidence returns
```

Generate, Share, and Claim remain the only first-level movements. Everything else is nested within them.

## Motion principles

### Intention precedes appearance

The Pay Code never appears from empty space. An intended payment and governed instruction are established first. The credential then appears as the visible result of Generate.

### The credential moves; money does not

During Share, the Pay Code moves between people through a communication path. Do not animate coins, cash, balances, or funds inside the credential or channel.

### Claim begins with stillness

The Pay Code reaches the recipient and stops. This pause separates communication from action and makes the recipient the agent of the next moment.

### Choice expands locally

Available supported destinations appear around or ahead of the recipient only after Claim begins. They do not expand across the whole composition or become a new stage.

### One path continues

After the recipient selects a destination, unselected paths recede. One path proceeds through validation and completion.

### Evidence returns quietly

Evidence may travel back as a dotted trace after completion. It does not reverse the financial journey and must not resemble a second payment.

## State model

| State | Visible meaning | Permitted transition | Prohibited implication |
| --- | --- | --- | --- |
| Intention | A person or institution has an intended payment outcome | To governed instruction | Money already moving |
| Governed instruction | Authority and purpose exist behind the journey | To Pay Code appearance | Pay Code creating authority |
| Generated | The credential is ready to communicate | To Share | Stored value loaded into code |
| In communication | The same credential moves through one channel | To recipient presentation | Money moving through messaging |
| Presented | Recipient holds or presents the credential | To bounded Choice or Validation | Automatic or anonymous redemption |
| Choice open | Supported destinations are visible | To one selected destination | Universal or simultaneous redemption |
| Selected | One route remains active | To Validation | Multiple payouts |
| Validated | Applicable checks permit continuation | To Settlement or Completion | Guaranteed approval in every case |
| Completed | The approved human outcome is reached | To Evidence | Pay Code remains reusable by implication |
| Evidenced | Status or record returns to the responsible context | End | Second financial movement |

## Verb semantics

### Generate

**Motion:** An intended payment becomes an instruction; the Pay Code appears once.

**Visual emphasis:** Emergence from a governed context.

**Nested movement:** Approval may resolve before appearance, but it does not receive a separate title or chapter.

**Must avoid:** Spawning, multiplying, filling with money, or appearing before intention.

### Share

**Motion:** The unchanged Pay Code travels from sender to recipient along one ordinary communication path.

**Visual emphasis:** Portability and continuity.

**Nested movement:** A channel cue may accompany the path.

**Must avoid:** Broadcasting, duplicating, transforming into money, or jumping through provider logos.

### Claim

**Motion:** The Pay Code stops with the recipient. Supported choices expand. One is selected. Validation and completion follow.

**Visual emphasis:** Human agency followed by calm completion.

**Nested movement:** Choice, presentation, validation, settlement, completion, and evidence.

**Must avoid:** A fourth public step, simultaneous destinations, explosive celebration, or direct code-to-cash transformation.

## Motion relationships

### Movement direction

Use one dominant reading direction within a composition. Horizontal and vertical arrangements are both valid when they preserve ordered progression.

Do not reverse direction merely for visual novelty. A returning evidence trace must be visually distinct from the forward journey.

### Continuity

The Pay Code must retain one visual identity throughout Generate, Share, and Claim. It may change scale for emphasis, but it must not change semantic form.

### Pauses

Pauses carry meaning:

- before Generate — intention exists;
- after Generate — the credential is ready;
- at the beginning of Claim — the recipient becomes active;
- after Choice — only one path continues; and
- after Completion — the outcome is allowed to register.

Continuous motion without pauses makes the journey feel automatic and removes human and institutional agency.

### Expansion and contraction

Expansion means bounded options becoming visible. Contraction means unselected options receding after one choice.

Expansion must never suggest an unlimited network. Contraction must never resemble value disappearing.

### Return motion

Only Evidence returns. Use a dotted or otherwise subordinate trace. The Pay Code, money, and completed outcome do not animate backward.

## Motion for everyday applications

Every application uses the same motion skeleton:

```text
purpose becomes instruction
        ↓
Pay Code appears
        ↓
Pay Code moves
        ↓
recipient claims through one supported path
        ↓
completion and evidence
```

Payroll, government benefits, insurance claims, loan proceeds, merchant refunds, incentives, remittances, and emergency assistance may change their purpose cue and actors. They may not change the underlying movement grammar.

## Temporal disclosure

A motion composition should reveal only the detail needed at each moment:

1. Establish the person and intention.
2. Reveal the Pay Code during Generate.
3. Move only the Pay Code during Share.
4. Stop at the recipient.
5. Reveal bounded choice inside Claim.
6. Continue one selected path.
7. Confirm completion.
8. Return evidence only if relevant.

Architecture must not appear before the human need. Provider detail must not appear before Claim. Evidence must not appear before completion.

## Static equivalence

Every motion sequence must have a truthful static equivalent. Pausing at any key state should produce a frame consistent with the Illustration Concept Specifications and VIS-001.

A renderer may use animation, slide builds, scroll progression, physical panels, or no motion at all. The semantic sequence remains the same.

## Accessibility and reduced motion

Motion may never be the sole carrier of meaning.

Every implementation must support:

- a static VIS-001 equivalent;
- logical reading order;
- descriptive text for the complete journey;
- sufficient pause or user control where interaction exists; and
- reduced-motion behavior that replaces travel and expansion with state changes without losing sequence.

## Motion tests

### Sequence Test

Does the viewer perceive Generate → Share → Claim in that order?

### Agency Test

Does motion stop long enough for institutional authority and recipient choice to remain meaningful?

### Singular-Outcome Test

After Choice expands, does exactly one path continue?

### Credential Test

Is it always clear that the Pay Code—not money—is what moves during Share?

### Memory Test

After one viewing, can the viewer reproduce the three actions and place Choice inside Claim?

If motion makes the system more impressive but less memorable, remove motion.

## Governance

New motion behavior requires a semantic reason. Transitions added only for novelty, spectacle, or brand energy are renderer embellishments and must not alter the canonical sequence.

This document approves movement meaning, not an animation or production technique.
