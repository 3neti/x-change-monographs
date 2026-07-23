# Reader Study Manifest Template

## Purpose

Every reader study begins with a completed copy of this manifest. It fixes the study design before the first participant session and preserves the information required to reproduce, audit, or distinguish the study later.

Complete all precommitment fields before evidence collection. Replace blanks with `Not applicable` and a reason rather than silently omitting a field.

## Study identity

| Field | Precommitted value |
| --- | --- |
| Study ID | |
| Study title | |
| Study version | |
| Manifest status | Draft / Precommitted / Closed |
| Precommitment date and time | |
| Precommitment owner | |
| Repository revision | |
| Protocol version or repository path | |
| Coding version or repository path | |
| Canonical composition revision | |
| Prototype revision | |

Once the manifest is marked **Precommitted**, changes are recorded as deviations. Do not replace the original value.

## Research question and boundary

Primary comprehension question:

> 

Secondary questions:

> 

Out of scope:

> 

The study observes comprehension, misunderstanding, and memory. Preference remains secondary and cannot establish convergence on its own.

## Candidate manifest

| Blinded code | Direction | Canonical asset path | Asset SHA-256 | Labels shown? | Label-free asset path and SHA-256 | Scale profile |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

### Candidate-set decisions

| Decision | Precommitted value |
| --- | --- |
| Candidate directions | |
| Does every participant see every candidate? | Yes / No — explain |
| Label-free variants used? | |
| D01 control included? | Yes / No |
| Reason for including or excluding D01 | |
| Candidate omissions | |

D01 is an optional neutral control, not a mandatory candidate. If included, use its corrected, label-free, and scale-matched Milestone 5.1 assets under `assets/marketing/prototypes/milestone-5.1/vis-001/d01-control/`.

## Participant precommitment

| Field | Precommitted value |
| --- | --- |
| Target participant count | |
| Minimum usable participant count | |
| Target profile categories | |
| Target distribution across profiles | |
| Inclusion criteria | |
| Exclusion criteria | |
| Prior-exposure screening | |
| Recruitment method | |
| Compensation, if any | |
| Replacement rule for unusable sessions | |

Do not change participant targets because early results appear attractive or unfavorable. Record any change as a dated deviation with its reason.

## Presentation precommitment

| Field | Precommitted value |
| --- | --- |
| Surface being tested | Print / screen / event-distance / other |
| Reader-testing scale | |
| Device, paper, or display specification | |
| Viewing distance | |
| Viewing environment | |
| Exposure duration | |
| Labels-present condition | |
| Label-free condition | |
| Delayed recall interval | |
| Neutral activity during delay | |
| Question order | Canonical / approved variation |
| Preference questions timing | After all comprehension and memory tests |

## Randomization precommitment

| Field | Precommitted value |
| --- | --- |
| Randomization method | |
| Tool or procedure | |
| Seed or draw-record location | |
| Balance rule | |
| Assignment generated before sessions? | |
| Treatment of early termination | Preserve assigned order and record missing exposures |

### Presentation-order assignments

Populate before the corresponding participant session begins.

| Participant ID | Ordered blinded codes | Assignment evidence reference |
| --- | --- | --- |
| | | |

## Roles and logistics

| Field | Precommitted value |
| --- | --- |
| Study owner | |
| Facilitator | |
| Observer | |
| Evidence custodian | |
| Analyst | |
| Decision owner | |
| Planned dates | |
| Location or session channel | |
| Accessibility accommodations | |

## Consent and recording

| Field | Precommitted value |
| --- | --- |
| Participant information sheet version | |
| Consent approach | Written / recorded verbal / other |
| Session notes | Yes / No |
| Audio recording | Yes / No |
| Video recording | Yes / No |
| Screen recording | Yes / No |
| Sketch retention | Yes / No |
| Quotations permitted | Attributed / anonymous / not permitted |
| Withdrawal method and deadline | |

No recording begins before the relevant consent is confirmed.

## Evidence operations

| Field | Precommitted value |
| --- | --- |
| Raw evidence storage location | |
| Consent-record storage location | |
| Participant-key storage location, if any | |
| Interview-form storage location | |
| Observation-form storage location | |
| Sketch storage location | |
| Access-authorized roles or named people | |
| Backup method | |
| File-naming convention | |
| Evidence integrity method | |

Raw participant materials, consent records, recordings, and identity keys remain outside public source control. Only appropriately de-identified study manifests, aggregate summaries, and governed research conclusions may enter the repository.

## Retention precommitment

| Record class | Retention period or deletion event | Access | Disposition |
| --- | --- | --- | --- |
| Contact or identity key | | | Delete / return / other |
| Consent record | | | |
| Audio or video recording | | | |
| Verbatim notes | | | |
| Sketches | | | |
| Coded observations | | | |
| De-identified aggregate summary | | | |

Retention may not exceed the consent granted for the study. If no duration is stated in consent, the study must define a limited period before recruitment begins.

## Analysis precommitment

| Field | Precommitted value |
| --- | --- |
| Evidence codes | `C`, `P`, `M`, `N` unless an approved version is identified |
| Unit of analysis | Participant-by-direction observation |
| Count denominator | Participants actually exposed to that direction |
| Handling of partial sessions | |
| Handling of contradictory evidence | Preserve and report |
| Analysis rule | |
| Stopping rule | |
| Retest criteria | |
| Evidence threshold for a convergence candidate | |
| Evidence threshold for correction or pause | |
| Preference review point | After semantic analysis is complete |

An evidence threshold must identify the required observation pattern, denominator, conditions, and doctrine boundary. It must not be invented after results are reviewed.

## Stopping and safety rules

Precommit when the study or a direction pauses because of:

- recurring doctrine misunderstanding;
- participant distress or withdrawal;
- compromised consent or recording;
- corrupted or missing evidence;
- material protocol deviation;
- prototype or display failure; or
- achievement of the approved stopping rule.

Study-specific stopping rule:

> 

## Known pre-study limitations

> 

## Deviations log

Do not edit the precommitted value. Record what changed, why, when, who authorized it, and whether affected evidence remains comparable.

| Deviation ID | Date and time | Original commitment | Actual condition | Reason | Authorized by | Evidence affected | Comparability decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

## Study close

Complete after the final session.

| Field | Closing record |
| --- | --- |
| Actual participant count | |
| Usable sessions | |
| Study end date | |
| Evidence inventory complete? | |
| Deviations reconciled? | |
| Retention schedule activated? | |
| Summary path | |
| Convergence entries created | None unless evidence supports them |
| Production identity selected | No unless separately authorized |
| Closed by and date | |

