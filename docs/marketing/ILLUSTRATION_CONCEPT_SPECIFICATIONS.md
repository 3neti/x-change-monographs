# Marketing Illustration Concept Specifications

## Purpose

These specifications define the first canonical visual vocabulary for Pay Code. They govern meaning, sequence, and relationships before artwork is produced.

The studies are deliberately medium-neutral. They describe what a viewer must understand, not how a particular illustrator should draw it.

Each study composes concepts from the canonical [Semantic Icon System](ICON_SYSTEM.md). The icon IDs govern meaning; they do not prescribe visible glyphs.

## Shared visual syntax

Every illustration uses the same small set of semantic elements.

| Element | Meaning | Consistent treatment |
| --- | --- | --- |
| Person | A known sender or intended recipient | Human figure with clear direction of attention; never an anonymous silhouette when identity matters |
| Governed frame | Institutional responsibility | A restrained boundary, counter, or structural frame; never the x-change mark alone |
| Instruction | The authorized purpose behind the journey | A subtle document or line originating inside the governed frame |
| Pay Code | Portable credential | A distinct tile using the double-bar motif: `|| PAY CODE ||` |
| Communication path | Portability between people | A neutral path that may carry channel cues without becoming a product interface |
| Supported destination | An available participating institution or channel | Two or three neutral, bounded choices; never an endless logo field |
| Checkpoint | Validation or applicable conditions | A quiet gate or check mark within the governed journey |
| Completion | The intended outcome has reached an approved end state | Calm confirmation near the recipient; never cash bursting from the credential |
| Evidence trace | Status, receipt, or reconciliation | A dotted return line or restrained receipt mark |

Across the system, solid arrows show progression, branches show choice only within Claim, dotted lines show evidence, and enclosing lines show institutional responsibility.

## Semantic icon composition

| Illustration | Primary semantic icons | Nested or supporting icons |
| --- | --- | --- |
| ILL-001 Unknown Recipient Destination | ICN-001 Person, ICN-011 Destination | ICN-002 Institution |
| ILL-002 Generate Pay Code | ICN-002 Institution, ICN-004 Instruction, ICN-003 Pay Code | ICN-007 Approval |
| ILL-003 Share Pay Code | ICN-001 Person, ICN-003 Pay Code, ICN-013 Communication | ICN-005 QR |
| ILL-004 Claim | ICN-001 Person, ICN-003 Pay Code, ICN-009 Choice, ICN-011 Destination | ICN-008 Validation, ICN-014 Settlement, ICN-015 Completion |
| ILL-005 Recipient Choice | ICN-003 Pay Code, ICN-009 Choice, ICN-011 Destination | ICN-008 Validation, ICN-015 Completion |
| ILL-006 Participating Institutions | ICN-002 Institution, ICN-004 Instruction, ICN-014 Settlement | ICN-012 Evidence, ICN-006 Receipt |

## ILL-001 — Unknown Recipient Destination

### Question answered

Why should the sender need a Pay Code?

### Viewer takeaway

The sender knows the recipient, but does not know which bank, wallet, or provider the recipient uses.

### Conceptual frame

```text
KNOWN SENDER                         KNOWN RECIPIENT
     ● ─────────────────────────────────── ●
      knows the person and purpose
                                                ┌──────┐
                                  destination ? │ BANK │
                                                │ EMI  │
                                                │ ...  │
                                                └──────┘
```

The human connection is direct and unambiguous. The uncertainty appears only beside the destination options, not around the recipient.

### Composition hierarchy

1. The two people and their clear relationship.
2. The unresolved destination beside the recipient.
3. A small set of generic destination cues.

### Semantic notes

- Keep the recipient visually specific and intended.
- Place the question mark over the destination cluster, never over the person.
- The sender may hold an intended payment instruction, but no Pay Code appears yet.
- Destination cues may suggest a bank, wallet, or provider without using brands.

### Must not imply

- an unknown or unverified recipient;
- that the sender is searching for a person;
- that every destination participates; or
- that lack of destination data removes identity or compliance requirements.

### Fifteen-second test

Without a caption, a viewer should say: “They know who should receive, but not where that person receives money.”

## ILL-002 — Generate Pay Code

### Question answered

Where does a Pay Code come from?

### Viewer takeaway

A responsible institution represents an intended, authorized payment as a portable credential.

### Conceptual frame

```text
┌──────── RESPONSIBLE INSTITUTION ────────┐
│ intended payment → authorized instruction│
│                              ↓           │
│                      || PAY CODE ||      │
└──────────────────────────────────────────┘
```

The Pay Code originates inside the governed institutional frame. The intended payment precedes the credential.

### Composition hierarchy

1. The intended payment or disbursement.
2. The responsible institutional boundary.
3. The Pay Code emerging from the authorized instruction.

### Semantic notes

- Show authorization as a quiet part of Generate, not as a public fourth step.
- Keep the instruction visually behind or immediately before the credential.
- Use the canonical double-bar motif consistently.
- The credential may leave the institutional frame; money does not appear inside it.

### Must not imply

- spontaneous or user-invented value;
- cash, balance, or stored value inside the Pay Code;
- x-change acting as the responsible institution; or
- an unauthorized code-generation utility.

### Fifteen-second test

Without a caption, a viewer should say: “A payment instruction becomes a Pay Code under an institution’s authority.”

## ILL-003 — Share Pay Code

### Question answered

How does the Pay Code reach the recipient?

### Viewer takeaway

The same credential can travel through an ordinary, appropriate communication channel.

### Conceptual frame

```text
SENDER                PORTABLE CREDENTIAL                 RECIPIENT
  ●       ────────     || PAY CODE ||      ────────          ●
                      SMS · QR · email
                    message · printed paper
```

One Pay Code moves along one selected path. Channel cues surround the path as examples; they are not additional destinations or simultaneous transmissions.

### Composition hierarchy

1. The Pay Code moving from sender to intended recipient.
2. The continuity of the credential across the path.
3. Small, secondary channel cues.

### Semantic notes

- Preserve the Pay Code’s appearance from Generate through Share.
- Emphasize portability, not a particular app or device.
- Depict one active communication path at a time.
- Printed paper belongs to the same family as digital channels.

### Must not imply

- public posting or uncontrolled broadcast;
- that every communication channel is always approved;
- a product user interface; or
- money moving through SMS, email, QR, or messaging.

### Fifteen-second test

Without a caption, a viewer should say: “The sender can pass the same Pay Code to the recipient in an ordinary way.”

## ILL-004 — Claim

### Question answered

What does the recipient do?

### Viewer takeaway

The recipient presents the Pay Code, chooses an available supported destination, and completes the governed journey.

### Conceptual frame

```text
RECIPIENT
   ● + || PAY CODE ||
            ↓
      ┌──── CLAIM ────┐
      │ choose        │──┬── supported bank
      │ present       │  └── supported provider
      │ validate  ✓   │
      └──────┬────────┘
             ↓
        completion ✓
```

Claim is one coherent scene. Choice, presentation, validation, and completion remain nested inside it rather than becoming additional first-level steps.

### Composition hierarchy

1. The recipient presenting the Pay Code.
2. A bounded choice among supported destinations.
3. Quiet validation and completion.

### Semantic notes

- The recipient is active: presenting and choosing.
- Use no more than two or three destination branches.
- Rejoin the chosen branch before completion to show one claim and one outcome.
- Conditions may be visible as a quiet checkpoint, not a legal warning.
- Completion belongs at the provider side of the journey, not inside the Pay Code.

### Must not imply

- universal acceptance;
- simultaneous redemption at several institutions;
- duplicated value or repeated claims;
- guaranteed completion; or
- direct conversion of the code into cash without a participating provider.

### Fifteen-second test

Without a caption, a viewer should say: “The recipient presents the code and chooses one supported way to receive.”

## ILL-005 — Recipient Choice

### Question answered

How can the recipient choose without turning choice into another process step?

### Viewer takeaway

One Pay Code may be presented through one of several available supported destinations during Claim.

### Conceptual frame

```text
INSIDE CLAIM

|| PAY CODE || → choose one ──┬── BANK
                              ├── EMI
                              └── PROVIDER
                                      ↓
                                 one completion
```

This is a reusable detail, not an independent journey. It appears inside ILL-004 or as a close-up derived from it.

### Composition hierarchy

1. One Pay Code.
2. A visibly bounded choice.
3. One selected path continuing to completion.

### Semantic notes

- Keep unselected destinations visually available but quiet.
- Mark only one selected destination.
- Label the set as supported or participating when words are available.
- Use generic institution types rather than logos.

### Must not imply

- multiple redemptions;
- universal interoperability;
- a marketplace ranking providers;
- provider endorsement; or
- the absence of applicable conditions.

### Fifteen-second test

Without a caption, a viewer should say: “The recipient chooses one available participating institution.”

## ILL-006 — Participating Institutions

### Question answered

Who performs the financial service?

### Viewer takeaway

Independent institutions retain their roles while a common operating layer coordinates the instruction.

### Conceptual frame

```text
┌──────────────┐                         ┌─────────────────┐
│ RESPONSIBLE  │   governed instruction │ PARTICIPATING   │
│ INSTITUTION  │ ──────────────────────→ │ PROVIDER        │
└──────────────┘          ↕              └─────────────────┘
                    x-change operating
                         layer

          separate authority · separate responsibility
```

The institutional boxes remain dominant. The x-change operating layer connects the instruction without enclosing, owning, or replacing either institution.

### Composition hierarchy

1. Distinct responsible and participating institutions.
2. The governed instruction between them.
3. The quiet x-change operating layer supporting coordination.

### Semantic notes

- Keep institutional boundaries separate.
- Show the operating layer as connective, not custodial.
- Add a dotted evidence trace only when the publication needs accountability.
- In public compositions, use this illustration after the human journey has been understood.

### Must not imply

- a common bank or pooled institution;
- x-change taking custody or exercising banking authority;
- a universal switch or settlement network;
- regulatory status; or
- identical institutional roles.

### Fifteen-second test

Without a caption, a viewer should say: “Different institutions remain responsible for their roles while the instruction is coordinated between them.”

## Cross-illustration continuity

The same Pay Code tile must remain visually recognizable from ILL-002 through ILL-005. The recipient introduced in ILL-001 should remain the recipient in Share and Claim when the illustrations appear as one sequence. A change in format may rearrange the frames, but it may not change their semantic continuity.

```text
intended payment
       ↓
ILL-002 Generate ──→ ILL-003 Share ──→ ILL-004 Claim
                                              └── ILL-005 Recipient Choice

ILL-001 explains the problem before the journey.
ILL-006 explains the institutional support after the journey.
```

## Concept approval rule

An illustration concept is ready for prototype work only when:

- its question can be answered without relying on a caption;
- actor roles remain unambiguous;
- the Pay Code is visibly a credential rather than money;
- choice is bounded and nested within Claim;
- the visual survives horizontal and vertical arrangements; and
- its fifteen-second test can be passed by a first-time reader.

These specifications do not approve a drawing style, final composition, brand treatment, or production asset.
