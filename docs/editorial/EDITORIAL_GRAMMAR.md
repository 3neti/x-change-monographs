# Editorial Grammar

## Method and confidence

This document infers the editorial grammar visible in the repository on 15 July 2026. The available corpus is small: three accepted decisions contain substantive editorial reasoning, while the canon, manuscript specification, Volume II source manuscript, and first editorial movement are placeholders. Volume I's prose is not present.

Observations are therefore marked by confidence:

- **Strong** — repeated or explicitly established by accepted decisions and repository policy.
- **Moderate** — supported by titles, metadata, and directory conventions but not yet by a body of finished prose.
- **Insufficient evidence** — the repository does not support a reliable inference.

## Editorial voice

### Governance voice — strong evidence

The developed voice in the repository is editorial-governance prose. It is:

- **plain and declarative** — decisions use direct verbs such as “Use,” “Separate,” and “Preserve”;
- **institutional without bureaucracy** — the writing explains durable responsibilities in short sentences rather than policy jargon;
- **consequence-aware** — choices are justified by what they protect or make possible;
- **archival** — revision history, source preservation, traceability, regeneration, and release identity are treated as editorial concerns;
- **restrained** — claims are narrow and practical, with no promotional intensifiers or aspirational sales language; and
- **future-conscious** — decisions are designed to make later revision, design change, and release work possible without corrupting prior layers.

The pacing is compact. Each accepted decision moves from a concrete problem, to one durable rule, to a short list of consequences. Sentences typically carry one idea. Lists are used to name layers and outcomes.

### Founder-author voice — moderate evidence

The planned authorial voice is visible primarily through titles and metadata:

- *A Founder's Update* suggests direct communication from founder to reader.
- *A Founder's Discovery Thesis* frames the work as an observed and developing argument, not a finished doctrine.
- *When Money Adapts to People* makes a human-centered proposition.
- *On the Future of Financial Settlement* places that proposition in an institutional and systems context.
- “Movement I — The Observation” begins with attention and discovery rather than a product claim.

These signals suggest a founder-led, reflective, thesis-driven voice that moves from observation toward insight. There is not enough manuscript prose to establish its sentence rhythm, storytelling method, level of technical detail, or commercial register.

### Commercial style — insufficient evidence

No marketing collateral or commercial manuscript is present. The repository does not yet establish how editorial ideas become offers, benefits, calls to action, claims, or audience-specific language. The governance prose favors credibility and continuity over persuasion, but it should not be treated as a complete marketing style.

### Institutional style — strong structural evidence

Institutional character arises less from formal vocabulary than from disciplined distinctions:

- author and editor are not collapsed into one role;
- source, composition, master, and release are not treated as one file;
- history is reviewable;
- consequences are recorded;
- design is downstream of editorial meaning; and
- generated output is replaceable while sources remain durable.

The resulting style is accountable, calm, and stewardship-oriented.

## Recurring themes

### Human systems should adapt to people — moderate evidence

The clearest thematic proposition is the Volume II title, *When Money Adapts to People*. Its secondary subtitle locates the proposition in financial settlement. Because the manuscript is a placeholder, the precise meaning and approved supporting claims are not yet available.

### Discovery begins with observation — moderate evidence

The sequence “Discovery Thesis” and “Movement I — The Observation” frames the intellectual method as noticing before declaring. The use of “movement” implies an argument that unfolds, pivots, and develops rather than merely itemizing topics.

### Stewardship of source and history — strong evidence

The repository repeatedly protects the author's original text, editorial traceability, durable decisions, and the ability to regenerate publication artifacts. Stewardship is implemented as architecture, not merely named as a value.

### Separation preserves integrity — strong evidence

Editorial governance, author source, editorial composition, publication master, released edition, and generated build are treated as distinct stages. The recurring principle is that clarity of custody makes revision safer and meaning more durable.

### Execution before surface treatment — strong evidence

The decisions place movement-level composition before page composition and typography. The system gives conceptual and editorial sequence priority over final visual form.

### Institutional responsibility — moderate evidence

Accepted decisions record why choices were made and what follows from them. This implies an institution responsible to future editors and releases, even though no explicit responsibility doctrine is present.

### Themes not evidenced in the current repository

The inspected files do not substantiate the phrases “Participation before membership,” “Businesses buy relief,” “Execution before expansion,” or “Ordinary Tuesdays.” They may exist in an external x-change corpus, but they are not part of this repository's current editorial evidence and therefore are not adopted here as recurring themes.

## Vocabulary

### Preferred or structurally authoritative terms

| Term | Observed use and implication | Confidence |
| --- | --- | --- |
| **The x-change Monographs** | Formal series identity; consistently capitalized in headings and metadata | strong |
| **author manuscript / source manuscript** | Preserved author text before editorial composition | strong |
| **editorial manuscript / editorial composition** | Approved literary source produced through editorial work | strong |
| **publication master** | A later, regenerable stage separate from manuscript and release | strong, but no artifact exists |
| **released edition** | A publication state distinct from the master | strong, but no artifact exists |
| **generated build / build output** | Derived DOCX, PDF, or other artifact that is not canonical source | strong |
| **movement** | Primary unit of editorial composition, review, cadence, and thought | strong |
| **plate** | Image or placed visual asset associated with a volume | strong as a directory convention |
| **canonical** | Durable source-of-truth or authority status | strong |
| **preserve / trace / regenerate** | Verbs expressing editorial custody and reversibility | strong |
| **founder** | Explicit authorial and institutional position in both volume identities | moderate |
| **discovery thesis** | Form of inquiry assigned to Volume II | moderate |
| **financial settlement** | System domain assigned to Volume II | moderate |

### Terminology displaced or constrained by the architecture

The repository does not contain an explicit prohibited-words list. It does, however, make several terminological distinctions intentional:

- **Chapter** is not the primary composition term for the Founder's Discovery Thesis; **movement** is.
- **Generated output** must not be described as the source of truth.
- **Editorial manuscript** and **author manuscript** are not interchangeable.
- **Publication master** and **released edition** are not interchangeable.
- **Typography** and **page composition** are not treated as the source of editorial rhythm.

There is insufficient evidence to infer avoided brand adjectives, prohibited financial terminology, rules for `x-change` versus `x-change OS`, or preferences among customer, member, participant, business, investor, and institutional-audience labels.

## Document architecture

### Accepted-decision pattern — strong evidence

All three decisions use the same architecture:

1. Numbered declarative title
2. `Status`
3. `Context`
4. `Decision`
5. `Consequences`

This pattern moves from problem to authority to implications. It is the repository's most mature recurring document form.

### Monograph identity pattern — moderate evidence

Volume II uses a three-level title stack:

1. Main proposition — *When Money Adapts to People*
2. Form and authorial stance — *A Founder's Discovery Thesis*
3. Domain — *On the Future of Financial Settlement*

Volume I uses a shorter title/subtitle form: *x-change: A Founder's Update*.

### Movement pattern — moderate evidence

The movement decision describes an internal movement as having an opening, development, pivot, insight, and cadence. The repository has only the heading for the first movement, so this is an approved compositional premise rather than a demonstrated manuscript pattern.

### README pattern — strong evidence

Local READMEs are brief boundary documents. They name a directory, state what belongs there, and sometimes state what belongs elsewhere. They do not provide procedural detail.

### Patterns not yet present

There is no demonstrated recurring use of executive summaries, audience statements, narrative openings, principles sections, implications sections, calls to action, claims and evidence, next actions, footnotes, citations, legal disclaimers, or approval blocks in editorial manuscripts.

## Metadata conventions

Metadata is YAML stored one record per volume at `resources/monographs/<volume>/metadata/monograph.yaml`.

Observed conventions are:

- lower-case snake-case keys;
- a shared `series` string and numeric `volume`;
- title layers represented by `title`, `subtitle`, and optionally `secondary_subtitle`;
- nested `author`, `source`, and `editorial` maps;
- repository-relative paths to canonical components;
- a free-text `status`; and
- optional notes and author affiliation.

The two records are not field-identical, and no schema declares which differences are intentional. The values `placeholder` and `editorial-composition` demonstrate workflow language but not a complete controlled lifecycle.

No dates, edition numbers, revision identifiers, reviewers, approvals, audience segments, abstracts, keywords, rights, claims, campaigns, publication profiles, asset manifests, or output formats are recorded.

## Publication assumptions

### Print orientation

Print is anticipated but not specified. The architecture names plates, page composition, typography, released editions, DOCX, and PDF. No page size, portrait/landscape choice, grid, margin, binding, color, bleed, accessibility, or prepress assumption is present.

### HTML publication

The Laravel application can render an Inertia/Vue web page, but the existing page is starter content and does not read monograph sources. No HTML publication route, Markdown parser, content template, semantic structure, or web publication profile exists. The presence of a web stack is not evidence of an approved HTML publishing format.

### PDF and DOCX publication

Both are named as future generated outputs in repository guidance. Neither has a renderer, template, sample artifact, build command, or validation process. Volume I metadata notes external typesetting but the resulting artifact is absent.

### Typography

One typographic principle is explicit: typography must not determine editorial rhythm, and page composition occurs after movement-level editorial composition. No publication typeface, scale, measure, hierarchy, caption treatment, or footnote convention is defined.

The Laravel starter UI uses Instrument Sans through the web build and references Inter on the starter page. Those are starter-application choices, not monograph typography authorities.

### Publication profiles

No print, screen, institutional brief, brochure, teaser, investor, legal, or audience-specific publication profile exists.

## Publishing Identity Assessment

### What kind of publisher is emerging?

If this repository were a publishing house, it would be a **founder-led institutional monograph press in formation**. Its defining instinct is not high-volume content production but controlled custody of ideas: preserve the originating text, make editorial intervention visible, compose arguments in movements, separate literary source from visual production, and retain history in Git.

It is closer to a small thesis press or institutional ideas office than to a campaign studio, newsroom, product-marketing team, or general corporate website. That identity is architecturally clear even though its catalogue is not yet present in full.

### Is there a recognizable editorial voice?

There is a recognizable **governance voice**: concise, calm, declarative, and accountable for consequences. There are also early signals of a **founder-thesis voice**: observational, human-centered, and interested in the future of systems. Because the founder manuscripts are absent or placeholders, the latter is an identity promise rather than a fully demonstrable prose voice.

### Are competing voices emerging?

No substantive conflict can yet be observed. Three registers are visible:

1. repository-policy instructions;
2. compact institutional decision records; and
3. founder-facing title language.

The first two align around stewardship and separation. The third introduces a more expansive intellectual proposition, but there is too little prose to determine whether it conflicts with the institutional register. The generic Laravel starter page is a separate software remnant, not an editorial voice of the publishing system.

### Which documents best represent the desired institutional tone?

The strongest examples are the accepted decisions, especially:

- `0002-separate-author-manuscript-editorial-manuscript-and-publication-master.md`, because it combines respect for authorship, editorial authority, regeneration, and visual independence; and
- `0001-use-git-as-publishing-history.md`, because it expresses accountability through concrete operating consequences.

`0003-use-movements-as-editorial-composition-units.md` adds the most distinctive literary sensibility: thought has cadence and pivots before it has pages.

The two titled editorial authorities cannot yet represent tone because their approved content has not been pasted into the files.

### Which documents are anchor texts for future marketing collateral?

There are two kinds of current anchor:

- **Governance anchors:** the three accepted decisions define how any collateral source, composition, design master, and release should relate without confusing roles or authority.
- **Thematic anchors:** the Volume II metadata and title stack provide the clearest current proposition—money adapting to people, approached as a founder's discovery thesis about financial settlement.

Neither type is yet a sufficient marketing source on its own. The governance anchors authorize process rather than claims; the thematic anchor names a thesis without supplying its argument or evidence. Volume I cannot serve as a repository anchor until its externally typeset or source material is available here.

### Which documents should influence future editorial work most?

For method, the accepted decisions should exert the greatest influence because they are the only substantive, explicitly accepted editorial authorities. For meaning, the eventual approved Volume I and Volume II author/editorial manuscripts should become primary influences once populated. The canon and manuscript specification are intended to govern all later work, but their current placeholder contents should not be treated as if they already carry that authority.
