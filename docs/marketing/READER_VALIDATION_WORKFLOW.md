# Reader Validation Workflow

## Purpose

This workflow governs unfamiliar-reader studies for Marketing Design System prototypes. It tests what participants understand, misunderstand, and remember. It does not ask participants to approve a visual identity.

Reader comprehension is the primary evidence. Preference is collected only after comprehension testing and remains secondary.

## Scope

The Milestone 6 VIS-001 study uses:

- D03 — Transit Map;
- D04 — Editorial Line;
- D05 — Pictographic Wayfinding;
- D06 — Modular Card; and
- D01 — Flat Geometric, when a neutral control is required.

D02 and D08 remain design influences. D07 remains on hold. No additional visual family may enter the study without a new prototype decision.

## Roles

| Role | Responsibility |
| --- | --- |
| Study owner | Approves the protocol, sample, and reporting boundary |
| Facilitator | Presents materials neutrally and records responses without correction |
| Observer | Records visible behavior separately from interpretation |
| Evidence custodian | Preserves forms, recordings, sketches, order assignments, and consent records |
| Analyst | Codes observations only after the session record is complete |
| Decision owner | Determines whether evidence is sufficient for convergence or another test cycle |

One person may hold more than one role, but the session record must identify who performed each function.

## Participant preparation

Recruit people who have not worked on the Marketing Design System and have not been briefed on VIS-001. Where practical, include institutional leaders, banking or payments practitioners, business users, and non-specialist readers.

Before the session:

1. assign a non-identifying participant ID;
2. record only profile information needed to interpret comprehension;
3. explain the session, recording method, voluntary nature, and right to stop;
4. obtain the required consent before recording audio, video, screen activity, or sketches;
5. confirm that the participant has not seen the candidate names or design rationale; and
6. avoid explaining x-change, Pay Code, or the intended sequence.

Do not collect unnecessary personal, financial, employment, or contact information.

## Materials preparation

Use the corrected Milestone 5.1 assets. Keep exposure time, physical size, viewing distance, medium, and surrounding copy consistent within a comparison.

Prepare:

- corrected candidates at the selected scale profile;
- label-free variants for the Caption Test;
- D01 control only when included in the approved session design;
- one randomized order assignment per participant;
- a neutral timing method;
- one interview template and one observation form per participant and direction;
- a blank sheet or digital canvas for recall; and
- an evidence folder identified by study ID and participant ID.

Before recruiting participants, create a completed [Reader Study Manifest](READER_STUDY_MANIFEST_TEMPLATE.md) and mark it **Precommitted**. Record the repository revision, asset checksums, participant and surface design, exposure and recall timing, randomization, stopping and retest rules, and evidence threshold for convergence. Later changes belong in the manifest's deviations log; they do not replace the original commitment.

Do not expose direction names such as “Transit Map” or “Modular Card.” Use blinded presentation codes that are mapped back to directions only in the study manifest.

## Presentation order

### Randomization

Generate the order before each session using a documented method. Preserve the assigned order even if the session ends early.

Across the study:

- distribute first position as evenly as practical;
- distribute each candidate across early, middle, and late positions;
- prevent the D01 control from always appearing first; and
- record deviations rather than silently correcting them after the session.

The randomization seed, draw record, shuffled list, or equivalent reproducible evidence must be retained in the study manifest.

### Standard exposure

For each direction:

1. show the visual for fifteen seconds;
2. remove it;
3. obtain the participant's unprompted first interpretation;
4. ask the standard semantic questions in order;
5. conduct the label-free test where assigned; and
6. move to the next direction without teaching the intended answer.

Conduct delayed recall only after a neutral interval. Comparative preference questions come last.

## Standard participant instruction

Use this wording or a faithful neutral equivalent:

> You will see several visual explanations. We are testing the visuals, not you. After each one, describe what you think it showed. There are no vocabulary requirements. Please say what you understood, even when you are uncertain.

Do not state the canonical message, three verbs, Pay Code definition, or correct institution role before comprehension testing ends.

## Observation protocol

Record:

- the participant's words verbatim where possible;
- visible behavior, such as first fixation, tracing, hesitation, or redraw order;
- the exact question that preceded a response;
- whether an answer was unprompted or followed a standard question;
- exposure and response timing where the protocol calls for it;
- material environmental interruptions; and
- sketches or redraws in their original form.

Use the evidence codes defined in [Design Validation](DESIGN_VALIDATION.md): `C`, `P`, `M`, and `N`. Code only the stated semantic requirement. Do not infer correctness from confidence or preference.

## Interviewer neutrality

The facilitator must not:

- praise, defend, explain, or correct a direction;
- repeat a response with approving or disapproving emphasis;
- introduce canonical vocabulary that the participant has not used;
- ask “Don't you think...?” or another leading question;
- reveal how earlier participants responded;
- change exposure time to help a weaker direction; or
- treat visual preference as proof of comprehension.

Permitted neutral prompts include:

- “What makes you say that?”
- “What happened next?”
- “Can you point to what you mean?”
- “Is there anything else you remember?”

## Recording methodology

Each session produces four distinct record classes:

1. **Raw evidence** — recordings, verbatim notes, timing, sketches, and assigned order.
2. **Observed behavior** — factual session observations without explanation.
3. **Coded observation** — application of the approved evidence codes to a defined test.
4. **Research interpretation** — a later explanation of patterns, uncertainty, and possible design consequence.

Never overwrite raw evidence with a cleaned summary. Corrections to a form should retain the original entry, the correction, the author, and the date.

## Evidence preservation

The study manifest should record:

- study ID and version;
- canonical source and prototype versions;
- asset paths or checksums;
- participant IDs and profile categories;
- presentation-order assignments;
- session dates and conditions;
- consent status and permitted record uses;
- form and recording locations;
- coding version; and
- known deviations or missing evidence.

Store participant identity or contact details separately from research observations when identity must be retained at all. Raw participant materials, consent records, recordings, and identity keys remain outside public source control. Access is limited to the roles or named people precommitted in the study manifest. Each record class must have a retention period or deletion event stated before recruitment, and retention may not exceed the consent granted for the study.

Only appropriately de-identified manifests, aggregate summaries, and governed conclusions may enter the repository. At the end of the stated period, the evidence custodian deletes, returns, or irreversibly de-identifies the material as recorded in the manifest.

## Ethics and participant care

- Participation is voluntary.
- The participant may decline a question or end the session.
- Explain what is recorded and how it will be used.
- Avoid collecting sensitive data not required by the research question.
- Do not describe comprehension difficulty as participant failure.
- Report aggregate patterns without exposing an individual's identity.
- Preserve contradictory and negative evidence.
- Do not fabricate missing observations or reconstruct unrecorded responses from memory.

## Repeatability controls

### Study precommitment

Before the first session, freeze in the study manifest:

- participant count, profile, inclusion criteria, and replacement rule;
- candidate set and whether every participant sees every candidate;
- D01 control inclusion or exclusion;
- surface, scale, exposure duration, and label conditions;
- randomization and delayed recall timing;
- stopping and retest criteria; and
- analysis rule and evidence threshold for convergence.

Precommitment prevents study goals from moving after attractive or unfavorable results appear. A necessary change is permitted only as a dated deviation whose effect on comparability is explicitly assessed.

A repeated study must preserve or explicitly document changes to:

- prototype version;
- scale and surface;
- exposure time;
- question wording and order;
- participant eligibility;
- randomization method;
- evidence codes; and
- analysis threshold.

Evidence from materially different conditions may be compared, but it must not be silently pooled.

## Analysis and convergence boundary

Summarize observations by semantic question and direction before reviewing preference. Quantitative counts describe the sample observed; they do not establish population certainty.

Add a characteristic to the [Convergence Register](CONVERGENCE_REGISTER.md) only when recorded reader evidence identifies the characteristic, its source direction, and its observed benefit. Repeated preference without demonstrated comprehension is insufficient.

Do not declare a winning style during Milestone 6. The permitted output is an evidence-based preservation, correction, retest, or convergence hypothesis.

## Stop conditions

Pause a direction and review it when repeated evidence suggests money inside the Pay Code, completion during Share, choice outside Claim, several completed destinations, universal acceptance, or x-change as custodian or financial institution.

Correct the failing visual or test it again. Do not change canonical VIS-001 semantics to accommodate a misunderstanding.
