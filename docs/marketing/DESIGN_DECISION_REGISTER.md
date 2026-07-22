# Marketing Design Decision Register

## Purpose

This register preserves enduring semantic and visual decisions in the Marketing Design System. It records why the system communicates as it does and makes later changes traceable.

The register does not contain reader-study findings. Reader evidence belongs in study records and the [Convergence Register](CONVERGENCE_REGISTER.md).

## Status vocabulary

- **Accepted** — governs current design work.
- **Proposed** — awaiting review or evidence.
- **Superseded** — replaced by a referenced decision.
- **Rejected** — considered and not adopted.
- **Deferred** — intentionally postponed.

An Accepted decision remains authoritative until explicitly superseded.

## Decision record fields

Each decision records an ID, title, status, date, context, decision, rationale, consequences, governing sources, supersession links, and notes.

## MDDR-001 — Use Generate → Share → Claim as the public sequence

- **Status:** Accepted
- **Date:** 2026-07-23
- **Context:** The complete operating lifecycle contains more detail than a first-time marketing reader can retain as a top-level journey.
- **Decision:** The canonical public sequence is `Generate → Share → Claim`.
- **Rationale:** Three human actions explain the journey without replacing the governed lifecycle beneath it.
- **Consequences:** Publications and compositions may expand nested detail but may not add Authorize, Choose, Validate, Settle, or Receive as peer steps.
- **Governing sources:** `MARKETING_GRAMMAR.md`, `VISUAL_GRAMMAR.md`, `compositions/VIS-001.md`
- **Supersedes:** None
- **Superseded by:** None
- **Notes:** Equivalent human wording may be accepted in reader testing; the canonical publication labels remain governed.

## MDDR-002 — Keep Choice inside Claim

- **Status:** Accepted
- **Date:** 2026-07-23
- **Context:** Recipient choice is meaningful but presenting it as a fourth first-level step makes the public journey longer and can imply that choice precedes presentation and validation.
- **Decision:** Choice is visually and narratively nested inside Claim.
- **Rationale:** The recipient discovers and selects one supported destination while claiming; choice is not an independent journey before Claim.
- **Consequences:** Branches may appear only within the Claim field. The remembered sketch remains `Generate → Share → Claim`, with Choice subordinate to Claim.
- **Governing sources:** `MARKETING_GRAMMAR.md`, `VISUAL_GRAMMAR.md`, `compositions/VIS-001.md`
- **Supersedes:** None
- **Superseded by:** None
- **Notes:** A direction that repeatedly places Choice beside Claim fails canonical hierarchy.

## MDDR-003 — Show one persistent credential moving

- **Status:** Accepted
- **Date:** 2026-07-23
- **Context:** Separate Pay Code objects at each moment can appear to represent several credentials, duplicated value, or unrelated steps.
- **Decision:** VIS-001 shows one persistent Pay Code generated once, shared once, and arriving at Claim.
- **Rationale:** Credential continuity distinguishes portable instruction access from money movement and protects the singular journey.
- **Consequences:** Motion states may change outline, position, or emphasis, but they must remain recognizably the same credential. Claim terminates credential movement.
- **Governing sources:** `MOTION_GRAMMAR.md`, `compositions/VIS-001.md`, `prototypes/milestone-5.1/CORRECTION-BRIEF.md`
- **Supersedes:** None
- **Superseded by:** None
- **Notes:** This decision produced the Milestone 5.1 correction pass.

## MDDR-004 — Show one selected destination and one completion

- **Status:** Accepted
- **Date:** 2026-07-23
- **Context:** Several visible destinations can be mistaken for several payouts or universal distribution.
- **Decision:** Claim may reveal a bounded set of supported options, but the recipient selects one destination and the visual shows one completion.
- **Rationale:** Recipient agency does not create duplicated value or unlimited interoperability.
- **Consequences:** Unselected options remain visibly secondary. No composition may show one Pay Code completing into several destinations.
- **Governing sources:** `VISUAL_PRINCIPLES.md`, `VISUAL_GRAMMAR.md`, `compositions/VIS-001.md`
- **Supersedes:** None
- **Superseded by:** None
- **Notes:** The Destination Test and Doctrine Test validate this decision.

## MDDR-005 — Keep provider completion visually secondary

- **Status:** Accepted
- **Date:** 2026-07-23
- **Context:** A participating financial provider performs or supports regulated financial movement, but infrastructure can easily displace the human journey in marketing artwork.
- **Decision:** Provider completion remains present and truthful but visually secondary to Generate, Share, and recipient Claim.
- **Rationale:** The primary question concerns the human experience. Institutional responsibility must remain visible without becoming the visual hero.
- **Consequences:** Provider completion may use a restrained mark, dotted trace, or subordinate field after selection. It may not disappear or become x-change completion.
- **Governing sources:** `VISUAL_PRINCIPLES.md`, `VISUAL_GRAMMAR.md`, `compositions/VIS-001.md`
- **Supersedes:** None
- **Superseded by:** None
- **Notes:** The Institution Test validates whether this balance remains truthful.

## MDDR-006 — Never depict money inside the Pay Code

- **Status:** Accepted
- **Date:** 2026-07-23
- **Context:** A portable code can be misread as stored value, a wallet, voucher balance, or the money itself.
- **Decision:** The Pay Code is depicted as a portable credential for an authorized instruction. It never visually contains money.
- **Rationale:** The distinction protects architectural truth, institutional custody boundaries, and public understanding.
- **Consequences:** Do not place coins, currency, balances, or value gauges inside the credential. Do not draw money moving through the communication channel with it.
- **Governing sources:** `MARKETING_GRAMMAR.md`, `VISUAL_GRAMMAR.md`, `DESIGN_VALIDATION.md`
- **Supersedes:** None
- **Superseded by:** None
- **Notes:** A repeated stored-value interpretation is a Doctrine failure and a stop condition.

## Change control

A proposed change must identify the affected decision, canonical sources, evidence or doctrinal reason, consequences across compositions and publications, and whether a new reader study is required. Silent redefinition through a prototype or renderer is prohibited.

