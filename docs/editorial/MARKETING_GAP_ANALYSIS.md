# Marketing Gap Analysis

## Scope

This analysis compares the repository's inspected state on 15 July 2026 with the capabilities required for a complete, governed marketing publication program. It recommends priorities but does not define directories, create infrastructure, or draft collateral.

Priority meanings:

- **P0 — prerequisite:** must be resolved before marketing collateral can be treated as authoritative;
- **P1 — foundation:** required to produce the first governed collateral safely and coherently;
- **P2 — scale:** required for repeatability across formats, audiences, and campaigns; and
- **P3 — optimization:** improves discovery, measurement, and long-term operational efficiency after the foundation works.

## Ranked gap summary

| Rank | Gap | Priority | Principal dependencies |
| ---: | --- | --- | --- |
| 1 | Populated editorial authorities | P0 | Approved canon and specification content |
| 2 | Canonical source corpus and anchor texts | P0 | Recovery/import and authority confirmation |
| 3 | Claims, evidence, and approval authority | P0 | Canonical corpus; accountable reviewers |
| 4 | Messaging architecture | P1 | Editorial authorities; claims boundary |
| 5 | Audience grammar | P1 | Messaging architecture; business/audience decisions |
| 6 | Vocabulary authority | P1 | Editorial canon; messaging; legal/financial review |
| 7 | Canonical story and proof library | P1 | Source corpus; claims authority; audience grammar |
| 8 | Campaign and collateral governance | P1 | Messaging, audiences, stories, approval states |
| 9 | Publication profiles and visual language | P2 | Canon/specification; collateral types; brand decisions |
| 10 | Asset provenance and rights discipline | P2 | Visual language; plates; release workflow |
| 11 | Publication-master, rendering, and QA pipeline | P2 | Profiles; metadata schema; approved source artifacts |
| 12 | Release catalogue and discovery automation | P3 | Stable lifecycle, pipeline, and collateral inventory |

## 1. Populated editorial authorities

**Observed gap.** `editorial-canon-v2.md` and `editorial-manuscript-specification-v1.md` are designated as canonical authorities, but both contain `TODO` placeholders. The accepted decisions cover source separation, Git history, and movements; they do not establish a complete editorial standard.

**Why it matters.** Marketing work needs a stable answer to who may speak, which voice governs, how source becomes approved copy, how exceptions are handled, and what makes an editorial artifact ready. Without populated authorities, individual collateral can become de facto policy through repetition.

**Dependencies.** This gap has no marketing-system dependency and should precede the messaging, audience, vocabulary, campaign, and publication-profile layers. The authorities should remain consistent with the three accepted decisions.

**Suggested priority.** **P0, rank 1.** Confirm and place the already-approved content referenced by the placeholders, or explicitly establish its actual approval state before any new marketing authority is created.

## 2. Canonical source corpus and anchor texts

**Observed gap.** Volume I is represented by metadata and directory notices; its metadata says it was typeset outside the scaffold. Volume II's author manuscript and first movement are titled placeholders. No substantive founder writings, white papers, execution memoranda, briefs, financial-planning materials, investor materials, or `resources/knowledge` corpus is present.

**Why it matters.** Marketing collateral must derive propositions, stories, claims, and language from authoritative source texts. Titles alone can establish themes but cannot supply nuance, evidence, exclusions, or approved wording. Creating collateral before the corpus exists would force the marketing layer to invent institutional meaning.

**Dependencies.** Recovery or confirmation of existing source and editorial manuscripts; clarification of whether externally held Volume I materials are authoritative; alignment with the source/editorial/master distinction.

**Suggested priority.** **P0, rank 2.** Establish the evidence base immediately after or alongside completion of the editorial authorities.

## 3. Claims, evidence, and approval authority

**Observed gap.** No artifact maps institutional or product claims to evidence, qualifies financial-settlement language, identifies prohibited assertions, records approval owners, or distinguishes founder thesis from verified organizational fact.

**Why it matters.** Marketing turns editorial ideas into public assertions. In financial and institutional contexts, an attractive phrase can imply capabilities, outcomes, availability, legal status, or certainty that the underlying text did not establish. A claims boundary protects credibility and lets reviewers distinguish expressive thesis from supportable fact.

**Dependencies.** Canonical source texts; editorial authority; identified legal, financial, operational, and founder review responsibilities where relevant.

**Suggested priority.** **P0, rank 3.** Define the authority model before messages are reused across collateral.

## 4. Messaging architecture

**Observed gap.** The repository has a promising thesis title—*When Money Adapts to People*—but no hierarchy linking institutional purpose, category position, audience problem, value, supporting ideas, reasons to believe, and calls to action.

**Why it matters.** A messaging architecture prevents each brochure, brief, or teaser from reinterpreting the institution independently. It also makes clear which ideas are universal, which are contextual, and which remain hypotheses.

**Dependencies.** Populated editorial authorities, canonical corpus, and claims/evidence boundaries.

**Suggested priority.** **P1, rank 4.** Establish a stable message hierarchy before segment-specific copy or campaign planning.

## 5. Audience grammar

**Observed gap.** No artifact defines audiences, their contexts, level of prior knowledge, concerns, desired relief, institutional role, or appropriate relationship to x-change. Metadata has author identity but no reader or audience fields.

**Why it matters.** The same thesis must often be explained differently to businesses, financial institutions, participants, investors, regulators, partners, or general readers. Audience grammar preserves one institutional meaning while changing emphasis, proof depth, vocabulary, and invitation.

**Dependencies.** A stable core message; business decisions about whom the publication program must serve; claims and review boundaries.

**Suggested priority.** **P1, rank 5.** Define audience distinctions before campaign or collateral types are selected.

## 6. Vocabulary authority

**Observed gap.** Current files establish publishing terms such as `movement`, `author manuscript`, and `publication master`, but do not govern public language for x-change, x-change OS, money, settlement, participation, membership, customers, businesses, institutions, or investors. There is no preferred, conditional, deprecated, or prohibited vocabulary list.

**Why it matters.** Vocabulary is where editorial continuity most often erodes across short-form material. A controlled authority can preserve important distinctions without forcing every piece to repeat the same sentences.

**Dependencies.** Editorial canon, messaging architecture, audience grammar, and any applicable legal or financial review.

**Suggested priority.** **P1, rank 6.** Establish alongside messaging and audience work, then treat it as a shared authority rather than a campaign preference.

## 7. Canonical story and proof library

**Observed gap.** No reusable stories, observed situations, founder anecdotes, customer evidence, case studies, examples, quotations, data points, or approved proof records exist. The repository contains no substantive “ordinary life” scenes from which collateral could draw.

**Why it matters.** A marketing program needs more than abstract propositions. Canonical stories make ideas legible while preventing anecdote drift, invented detail, or inconsistent attribution. Proof records connect stories to claims and make reuse reviewable.

**Dependencies.** Canonical source corpus, claims/evidence authority, audience grammar, consent and provenance where real people or organizations are involved.

**Suggested priority.** **P1, rank 7.** Curate only after the message and evidence boundaries are known, but before drafting the first brochure.

## 8. Campaign and collateral governance

**Observed gap.** There is no campaign concept, collateral index, document owner, audience assignment, approval state, source linkage, publication status, supersession rule, or relationship between long-form monographs and short-form marketing pieces.

**Why it matters.** The accepted publishing decisions protect monograph layers, but a marketing program introduces many related artifacts and variants. Without governance, old collateral can remain apparently current, derivatives can lose their source, and campaign urgency can bypass editorial review.

**Dependencies.** Messaging architecture, audience grammar, story library, claims authority, and a lifecycle vocabulary.

**Suggested priority.** **P1, rank 8.** Define the organizing and status model before the first collateral family is commissioned; do not wait until many pieces exist.

## 9. Publication profiles and visual language

**Observed gap.** The repository anticipates plates, typography, page composition, DOCX, and PDF, but specifies no format profiles or visual system. No print geometry, web semantics, hierarchy, typography, palette, imagery treatment, caption grammar, data-visualization style, accessibility rule, or relationship between monograph and marketing formats exists.

**Why it matters.** Editorial source must be able to become different outputs without each output redefining the institution. Publication profiles translate the editorial system into explicit format constraints; visual language gives the family recognizable continuity.

**Dependencies.** Editorial manuscript specification, known collateral types and audiences, brand decisions, and accessibility/production requirements.

**Suggested priority.** **P2, rank 9.** Define after content architecture but before designing a production brochure or institutional brief.

## 10. Asset provenance and rights discipline

**Observed gap.** Plate directories exist, but they contain only READMEs. No asset identifiers, captions, credits, rights, licenses, source files, transformations, alt text, approval status, or usage restrictions are recorded.

**Why it matters.** Marketing assets are frequently reused and transformed. Provenance protects legal use, correct attribution, accessibility, quality, and the ability to regenerate publications from canonical assets.

**Dependencies.** Visual-language decisions, plate conventions, publication profiles, and release governance.

**Suggested priority.** **P2, rank 10.** Establish before importing or commissioning a substantial visual library.

## 11. Publication-master, rendering, and QA pipeline

**Observed gap.** The architecture names publication masters and builds but does not implement the publication-master layer. `scripts/` and build directories are empty; no renderer reads monograph sources; no output manifest or publication QA exists. The Vite pipeline only builds the starter web application.

**Why it matters.** Once collateral is approved, reproducible generation preserves the source/master/build separation already accepted by the repository. QA is needed to verify links, metadata, typography, image quality, accessibility, pagination, and output identity across formats.

**Dependencies.** Stable source artifacts, metadata schema, publication profiles, asset conventions, approval lifecycle, and chosen output formats.

**Suggested priority.** **P2, rank 11.** Automate after one or more publication profiles have been proven manually; automation should encode a known process rather than decide it.

## 12. Release catalogue and discovery automation

**Observed gap.** `monograph:status` reports only three structural checks. There is no authoritative catalogue of publications and collateral, no edition/release metadata, no tag convention, no supersession state, and no automated detection of missing references or placeholder content.

**Why it matters.** A complete program needs to answer what exists, which edition is current, who it serves, what source it derives from, and whether it is approved for use. Discovery automation becomes especially important as audiences, formats, and campaigns multiply.

**Dependencies.** Stable metadata and lifecycle conventions, collateral governance, release workflow, and rendering pipeline.

**Suggested priority.** **P3, rank 12.** Expand discovery only after the underlying states and records are authoritative.

## Dependency sequence

```text
Populated editorial authorities ─┐
                                ├─> Claims and evidence authority
Canonical source corpus ────────┘              │
                                               ├─> Messaging architecture
                                               │          │
                                               │          ├─> Audience grammar
                                               │          └─> Vocabulary authority
                                               │                    │
                                               └─> Story/proof library
                                                            │
                                  Campaign and collateral governance
                                                            │
                                  Publication profiles and visual language
                                                            │
                                       Asset provenance and rights
                                                            │
                                 Publication master, rendering, and QA
                                                            │
                                      Release catalogue and discovery
```

## Principal conclusion

The primary gap is not a lack of brochure files. It is the absence of populated authorities and source texts from which brochures could responsibly derive. The repository already has the correct instinct—separate source, editorial intervention, master, and build—but marketing needs its own governed message, audience, evidence, story, visual, and release layers before collateral can become a durable part of the same publishing system.
