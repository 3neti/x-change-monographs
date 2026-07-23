# RV-001 — General Unfamiliar Readers

## Study status

**Prepared — not authorized; not yet precommitted.**

The research design below is fixed for review. Recruitment and evidence collection must not begin until the operational assignments in the launch gate are completed and the manifest is marked **Precommitted** in a new commit.

## Study identity

| Field | Precommitted value |
| --- | --- |
| Study ID | `RV-001` |
| Study title | General Unfamiliar Readers |
| Study version | `0.1` |
| Manifest status | Prepared |
| Preparation date | 2026-07-23 |
| Repository revision | `af01da6752d53fe609f682194cf26381047c53c5` |
| Protocol | `docs/marketing/READER_VALIDATION_WORKFLOW.md` at repository revision above |
| Coding | `docs/marketing/DESIGN_VALIDATION.md` at repository revision above |
| Canonical composition | `docs/marketing/compositions/VIS-001.md` at repository revision above |
| Prototype revision | Milestone 5.1 corrected candidates at repository revision above |

The study ID is immutable. A stopped, materially changed, or repeated study receives a new study ID or a separately versioned follow-up manifest; this record is not overwritten.

## Research question and boundary

Primary question:

> Which VIS-001 candidate characteristics help unfamiliar readers understand and remember Generate → Share → Claim without creating a material doctrinal misunderstanding?

Secondary questions:

- What does the participant first believe the visual represents?
- What appears to move?
- Is the Pay Code understood as a credential rather than money?
- Does the recipient act and choose inside Claim?
- Does one destination receive money?
- Does the participant perceive a participating institution or provider as completing the financial part?
- Which three-step sequence is retained after a delay?

Out of scope:

- selecting a production identity;
- approving color, typography, or finished artwork;
- statistically generalizing beyond the observed participants;
- testing product usability or implementation architecture; and
- changing canonical VIS-001 semantics.

## Candidate manifest

Direction names remain concealed from participants. The blinded-code mapping is retained here for auditability.

| Blinded code | Direction | Label-free asset and SHA-256 | Corrected asset and SHA-256 | Page preview and SHA-256 |
| --- | --- | --- | --- | --- |
| `K2` | D03 — Transit Map | `assets/marketing/prototypes/milestone-5.1/vis-001/d03-transit-map/label-free.svg` — `db43d6e5f2e161952eb78fd845270343fa4064071a388950d566d5fb2be414f3` | `assets/marketing/prototypes/milestone-5.1/vis-001/d03-transit-map/corrected.svg` — `16cecc0510e955b62ad4024bd54de59c1045885654c19dee612bb130fdcd7d5a` | `assets/marketing/prototypes/milestone-5.1/vis-001/d03-transit-map/previews/page-1200x650.png` — `67825f03483b55ba442bccd02af8e3022bd9a126d45e22bf96f294bcaa6ac0f3` |
| `M7` | D04 — Editorial Line | `assets/marketing/prototypes/milestone-5.1/vis-001/d04-editorial-line/label-free.svg` — `40ab4670bae1c155656aedb5149a3be0a0698e533f8a4cc07c2283c7f15ecc71` | `assets/marketing/prototypes/milestone-5.1/vis-001/d04-editorial-line/corrected.svg` — `cb53ab90ea6815f2777ce087d805f094d793b13c5316df629e98a0134ac7726c` | `assets/marketing/prototypes/milestone-5.1/vis-001/d04-editorial-line/previews/page-1200x650.png` — `a4a84884c66560d9d0f2cc3e972af5d12c623291bdf44c862d463b553208005a` |
| `R4` | D05 — Pictographic Wayfinding | `assets/marketing/prototypes/milestone-5.1/vis-001/d05-wayfinding/label-free.svg` — `ef8b9b60140d248be921eda448bfcc7f26d6a33ce508b20eb1962cbebc90d0ce` | `assets/marketing/prototypes/milestone-5.1/vis-001/d05-wayfinding/corrected.svg` — `67c0dc7235d04f1ff44262b58cec545da0ddf106e815bb41f5fca67ee1864bec` | `assets/marketing/prototypes/milestone-5.1/vis-001/d05-wayfinding/previews/page-1200x650.png` — `8f6fa0c072256e0f6c73afc65d38e72dcb04aac80fa5a94b1b4225c843655a76` |
| `T9` | D06 — Modular Card | `assets/marketing/prototypes/milestone-5.1/vis-001/d06-modular-card/label-free.svg` — `c9ed13ccb89ea78ab51d4f3a02a2cebdc83aef665eded57fcbc0a847c12ff830` | `assets/marketing/prototypes/milestone-5.1/vis-001/d06-modular-card/corrected.svg` — `d63273195d5bd20bf899e43fea7f003fc510b1c71f433c4b3fcea952fbb54430` | `assets/marketing/prototypes/milestone-5.1/vis-001/d06-modular-card/previews/page-1200x650.png` — `cce2460899e864464aae7d02f089fe10ad655a4584442ff226539a3c7ff53982` |

Candidate-set decisions:

| Decision | Value |
| --- | --- |
| Every participant sees every candidate | Yes |
| Label-free condition | First exposure for every candidate |
| Corrected labeled condition | Shown only after the label-free response for that candidate is complete |
| D01 control included | No |
| D01 rationale | Excluded from the first cycle to reduce session burden; its operationally equivalent assets remain available for a separately precommitted study |

## Participant precommitment

| Field | Value |
| --- | --- |
| Target participant count | 8 |
| Minimum usable participant count | 5 |
| Target profiles | 2 banking or finance professionals; 1 business executive; 1 engineer or technical professional; 2 ordinary consumers without payments-industry roles; 1 student or younger adult; 1 non-payments professional |
| Inclusion criteria | Adult; unfamiliar with x-change; able to view the chosen page-scale surface and respond in the session language |
| Exclusion criteria | Worked on x-change, the Marketing Design System, or these prototypes; previously briefed on VIS-001; unable to provide informed consent |
| Recruitment method | Direct invitation outside the design team; no public claims of product testing |
| Compensation | None unless disclosed and added before precommitment |
| Replacement rule | Replace a session only when consent is withdrawn, exposure materially fails, recording is unusable for the approved evidence method, or eligibility screening was incorrect; retain the failed-session record without participant data in the deviations log |

Do not change the target because early responses appear favorable or unfavorable.

## Presentation precommitment

| Field | Value |
| --- | --- |
| Surface | Page-scale digital presentation |
| Asset condition | 1200 × 650 composition fitted consistently within one display viewport |
| Device | One study device and display configuration for all sessions; exact model, resolution, browser or viewer, zoom, and brightness recorded before precommitment |
| Viewing distance | Ordinary seated reading distance; material deviations recorded |
| Exposure | 15 seconds per label-free candidate |
| Label sequence | Label-free first; corrected labeled asset only after the first interpretation and semantic questions for that candidate |
| Delayed recall | One redraw or verbal reconstruction after all four candidates and a five-minute neutral task |
| Preference | Asked only after comprehension and delayed recall are complete |
| Standard prompts | `docs/marketing/READER_INTERVIEW_TEMPLATE.md` at the precommitted repository revision |

## Randomization precommitment

Use the following balanced four-sequence assignment twice. It balances each blinded code across presentation positions. Participant IDs are assigned in recruitment order and do not change after assignment.

| Participant ID | Ordered blinded codes |
| --- | --- |
| `RV-001-P01` | `K2 → M7 → T9 → R4` |
| `RV-001-P02` | `M7 → R4 → K2 → T9` |
| `RV-001-P03` | `R4 → T9 → M7 → K2` |
| `RV-001-P04` | `T9 → K2 → R4 → M7` |
| `RV-001-P05` | `K2 → M7 → T9 → R4` |
| `RV-001-P06` | `M7 → R4 → K2 → T9` |
| `RV-001-P07` | `R4 → T9 → M7 → K2` |
| `RV-001-P08` | `T9 → K2 → R4 → M7` |

If a session ends early, preserve its assigned order and record unshown candidates as missing exposures.

## Consent, recording, and retention

| Field | Value |
| --- | --- |
| Participant information | `docs/marketing/READER_PARTICIPANT_INFORMATION_AND_CONSENT.md` at precommitted revision |
| Consent | Written or recorded verbal confirmation before the session begins |
| Required evidence | Facilitator notes, verbatim response capture, observation form, and redraw or verbal recall record |
| Audio | Optional; must be precommitted uniformly and separately consented |
| Video or screen recording | Not planned |
| Quotations | Anonymous only when consented |
| Raw evidence location | `private://marketing-reader-studies/RV-001/raw/` |
| Consent location | `private://marketing-reader-studies/RV-001/consent/` |
| Participant key | No identity key unless operationally necessary; if used, store at `private://marketing-reader-studies/RV-001/identity/` separately |
| Repository-safe evidence | De-identified manifest, aggregate summary, coded tables, evidence-backed convergence entries, and evidence-backed decisions only |
| Raw-material access | Named facilitator, observer, evidence custodian, and analyst assigned at launch gate |
| Retention | Raw notes, consent, audio if used, and redraws: 90 days after study close unless a shorter consent period applies; then delete or irreversibly de-identify. De-identified coded observations and aggregate summaries may be retained as institutional research history. |

No personal identifying information, consent signatures, raw recordings, private contact details, or unrestricted participant sketches enter public source control.

## Analysis precommitment

| Field | Value |
| --- | --- |
| Evidence codes | `C`, `P`, `M`, `N` |
| Unit of analysis | Participant-by-direction observation |
| Denominator | Participants actually exposed to that direction |
| Partial sessions | Count only completed direction exposures; report the denominator for every table |
| Contradictory evidence | Preserve verbatim and report without forced reconciliation |
| Preference review | After semantic coding and memory review |
| Qualitative boundary | Counts describe this sample only and are not statistically conclusive |

### Convergence threshold

A characteristic may become **Proposed from evidence** only when:

- at least six of eight participants demonstrate the same unprompted comprehension or recall benefit, with the actual exposed denominator reported;
- verbatim or behavioral evidence identifies the characteristic rather than only a preference;
- no recurring material Doctrine failure offsets the benefit; and
- limitations and contradictory observations are recorded.

The entry remains provisional until tested in another profile or surface condition. RV-001 cannot select a production identity.

When fewer than six usable participants complete the relevant exposure, RV-001 cannot promote a visual characteristic to **Proposed from evidence** based on this study alone. A smaller completed sample may document repeated misunderstandings, identify comprehension failures, support retesting, generate hypotheses, and produce a study report; it may not satisfy or retrospectively relax the six-participant convergence threshold.

### Correction and retest criteria

- Pause a direction when three of the first four exposed participants independently express the same material Doctrine failure.
- Recommend correction and a separately versioned retest when three or more participants across the usable sample show the same material misunderstanding.
- Recommend further study when a possible benefit appears in fewer than six participants, depends materially on labels, or conflicts across profile categories.

### Study stopping rule

Close after eight usable sessions. The minimum of five supports a report only if recruitment cannot reasonably complete and the reason is recorded; the evidence threshold must use the actual denominator and may not be relaxed. Stop earlier for compromised consent, persistent technical failure, or a direction-level pause under the rule above.

## Launch gate — required before precommitment

The following operational fields are intentionally not invented. Complete them before recruitment, then change the manifest status to **Precommitted** in a new commit without altering the fixed research design.

| Required field | Assignment |
| --- | --- |
| Study owner | Unassigned |
| Facilitator | Unassigned |
| Observer | Unassigned |
| Evidence custodian | Unassigned |
| Analyst | Unassigned |
| Decision owner | Unassigned |
| Session dates | Unscheduled |
| Location or session channel | Unassigned |
| Exact study device and display configuration | Unassigned |
| Private evidence workspace confirmed | Not confirmed |
| Audio-recording decision | Not fixed |
| Withdrawal contact and deadline | Unassigned |
| Consent form study-specific fields completed | No |

No participant session is authorized while any launch-gate field remains unresolved.

## Deviations log

| Deviation ID | Date | Original commitment | Actual condition | Reason | Authorized by | Evidence affected | Comparability decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

## Evidence state

No participant data exists. No observation has been recorded. No convergence entry or production decision is authorized by this prepared manifest.
