# Marketing Semantic Icon System

## Purpose

The Icon System defines the conceptual atoms from which x-change marketing illustrations are composed. It governs what an icon means, when it may appear, how it relates to other icons, and which interpretations it must avoid.

It does not define SVG paths, drawing style, stroke weight, color, dimensions, or software components.

## System rules

- An icon carries one stable meaning across publications.
- Context may narrow an icon's meaning but may not reverse it.
- Labels may confirm an icon during early prototyping; final comprehension must not depend on labels alone.
- Icons become explanatory only through governed relationships and movement.
- No icon may imply a regulated role that the represented actor does not hold.
- Brand marks are identity assets, not substitutes for semantic icons.

## Canonical vocabulary

### ICN-001 — Person

**Semantic meaning:** A known human participant acting with intention.

**Intended usage:** Sender, recipient, employee, beneficiary, claimant, borrower, customer, or another human role made clear by context.

**Relationships:** A Person may hold or present a Pay Code, initiate a Journey, approach a Destination, or receive Completion.

**Prohibited interpretations:** Anonymous target, unverified identity, demographic stereotype, faceless market segment, or decorative crowd.

### ICN-002 — Institution

**Semantic meaning:** An organization retaining authority, responsibility, or a defined service role.

**Intended usage:** Responsible institution, employer, public authority, insurer, lender, merchant, bank, EMI, or payment provider.

**Relationships:** An Institution may originate an Instruction, contain an Approval, offer a Destination, perform Settlement, or receive Evidence.

**Prohibited interpretations:** Generic building decoration, regulator unless explicitly governed, shared bank, or x-change acting as the financial institution.

### ICN-003 — Pay Code

**Semantic meaning:** A portable credential representing an authorized instruction.

**Intended usage:** The persistent object connecting Generate, Share, and Claim. Use the canonical double-bar motif where words are present: `|| PAY CODE ||`.

**Relationships:** A Pay Code originates from an Instruction, travels through Communication, and is presented by a Person during Claim.

**Prohibited interpretations:** Money, cash, coin, deposit, stored value, account, wallet balance, gift certificate, or guaranteed payment.

### ICN-004 — Instruction

**Semantic meaning:** The governed direction behind an intended payment or disbursement.

**Intended usage:** Quietly establish purpose, amount, intended recipient, and applicable conditions behind Generate.

**Relationships:** An Instruction originates within an Institution, receives Approval where required, and is represented by a Pay Code.

**Prohibited interpretations:** Money itself, informal message, recipient-created value, or uncontrolled command.

### ICN-005 — QR

**Semantic meaning:** One possible machine-readable presentation or communication form for a Pay Code.

**Intended usage:** Secondary channel cue within Share or presentation cue within Claim.

**Relationships:** A QR carries or presents the Pay Code; it may sit beside Communication or a Person.

**Prohibited interpretations:** The Pay Code's only form, a payment rail, proof of settlement, universal scanner compatibility, or decorative technology motif.

### ICN-006 — Receipt

**Semantic meaning:** Human-readable confirmation or record of an event.

**Intended usage:** Quiet completion acknowledgment or evidence artifact after an action.

**Relationships:** A Receipt may follow Completion and form part of Evidence.

**Prohibited interpretations:** Cash, authorization by itself, guaranteed finality, or an account statement unless specifically governed.

### ICN-007 — Approval

**Semantic meaning:** Required authority has permitted an instruction to proceed.

**Intended usage:** Nested within Generate when institutional authority must be visible.

**Relationships:** Approval applies to an Instruction inside an Institution before the Pay Code appears.

**Prohibited interpretations:** A public first-level journey step, regulatory endorsement, automatic eligibility, or approval performed by the Pay Code.

### ICN-008 — Validation

**Semantic meaning:** A governed check applied during presentation or execution.

**Intended usage:** Quiet checkpoint inside Claim.

**Relationships:** Validation sits after Pay Code presentation and before Completion; it may inspect conditions associated with the Instruction.

**Prohibited interpretations:** Guaranteed success, identity bypass, universal approval, or a decorative security badge.

### ICN-009 — Choice

**Semantic meaning:** Selection of one available supported path.

**Intended usage:** A bounded branch inside Claim, normally offering two or three generic destinations.

**Relationships:** Choice follows Pay Code presentation and leads to one selected Destination before Completion.

**Prohibited interpretations:** Infinite providers, simultaneous redemption, duplicated value, marketplace ranking, or freedom from conditions.

### ICN-010 — Journey

**Semantic meaning:** Ordered progression through governed human actions.

**Intended usage:** Connect Generate, Share, and Claim using directional continuity.

**Relationships:** Journey carries a Pay Code between People, Institutions, Communication, and Destination while preserving sequence.

**Prohibited interpretations:** Direct money transfer through the Pay Code, skipped institutional roles, circular repetition, or guaranteed speed.

### ICN-011 — Destination

**Semantic meaning:** An available supported institution, provider, or approved receiving channel.

**Intended usage:** One of a bounded set discovered during Claim.

**Relationships:** A Destination is offered by an Institution, selected through Choice, and participates in Completion.

**Prohibited interpretations:** Every bank or wallet, permanent availability, endorsement, or the recipient's identity.

### ICN-012 — Evidence

**Semantic meaning:** Observable status, trace, or record supporting accountability and reconciliation.

**Intended usage:** Secondary dotted trace or restrained record returning from execution.

**Relationships:** Evidence may connect Completion to the responsible Institution and may include a Receipt.

**Prohibited interpretations:** Marketing analytics, surveillance, money flow, or proof beyond what the underlying event establishes.

### ICN-013 — Communication

**Semantic meaning:** An ordinary supported way to convey the Pay Code to the intended recipient.

**Intended usage:** SMS, email, messaging, printed paper, or another approved channel cue inside Share.

**Relationships:** Communication carries the Pay Code between People without carrying money.

**Prohibited interpretations:** Product interface, public broadcast, guaranteed secure delivery, financial rail, or simultaneous use of every channel.

### ICN-014 — Settlement

**Semantic meaning:** Financial completion performed through responsible participating arrangements.

**Intended usage:** Quiet institutional consequence after validation, normally nested within Claim or an institutional composition.

**Relationships:** Settlement is performed by participating Institutions using supported resources; it precedes Completion and produces Evidence where applicable.

**Prohibited interpretations:** x-change custody, money inside the Pay Code, universal connectivity, direct code-to-cash conversion, or settlement performed by a communication channel.

### ICN-015 — Completion

**Semantic meaning:** The governed journey has reached its approved human outcome.

**Intended usage:** Calm confirmation beside the recipient or selected destination.

**Relationships:** Completion follows Validation, Choice where applicable, and Settlement. It may produce a Receipt or Evidence trace.

**Prohibited interpretations:** Guaranteed outcome, celebration of wealth, exploding coins, repeated payment, or the Pay Code itself becoming money.

## Canonical icon relationships

### Generate

```text
ICN-002 Institution
    └── ICN-004 Instruction
            └── ICN-007 Approval
                    └── ICN-003 Pay Code appears
```

### Share

```text
ICN-001 Person
    └── ICN-003 Pay Code
            └── ICN-013 Communication
                    └── ICN-001 Person
```

### Claim

```text
ICN-001 Person presents ICN-003 Pay Code
    └── ICN-009 Choice
            └── one ICN-011 Destination
                    └── ICN-008 Validation
                            └── ICN-014 Settlement
                                    └── ICN-015 Completion
                                            └── ICN-012 Evidence / ICN-006 Receipt
```

Approval is nested inside Generate. Choice, Validation, Settlement, Completion, Evidence, and Receipt are nested inside Claim. These relationships must not be promoted into a competing public sequence.

## Composition roles

| Role | Primary icons | Secondary icons |
| --- | --- | --- |
| Human problem | Person, Institution or Destination | Instruction |
| Generate | Instruction, Pay Code, Institution | Approval |
| Share | Pay Code, Person, Communication | QR |
| Claim | Person, Pay Code, Choice, Destination | Validation, Settlement, Completion |
| Institutional explanation | Institution, Instruction, Settlement | Evidence, Receipt |
| Public-purpose explanation | Institution, Person, Instruction | Approval, Validation, Evidence |

## Icon governance

Adding a new icon requires a semantic need that cannot be expressed by the existing vocabulary. A new visual appearance for an existing meaning is a style variant, not a new semantic icon.

An approved icon specification must preserve:

- its canonical ID;
- stable semantic meaning;
- permitted relationships;
- prohibited interpretations; and
- accessibility label appropriate to its role in the containing illustration.

No icon artwork is approved by this document.
