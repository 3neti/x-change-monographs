# Editorial Inventory

## Scope

This inventory records editorial and publishing-governance artifacts present in the repository on 15 July 2026. Each path appears once. Laravel starter documentation, dependency files, generated Wayfinder files, and agent skill instructions are outside the editorial inventory.

Maturity labels describe the artifact's **current contents**, not the authority implied by its filename:

- **draft** — incomplete, placeholder, or not yet ready to govern publication;
- **working** — populated and operational but not explicitly approved as a durable authority;
- **approved** — explicitly accepted or approved for use;
- **canonical** — explicitly established as a durable source of truth.

Where a file is intended to become canonical but is still a placeholder, its maturity is `draft (canonical role declared)`.

## Repository and editorial architecture

| Title | Canonical path | Purpose | Intended audience | Maturity |
| --- | --- | --- | --- | --- |
| x-change Monographs Repository | `AGENTS.md` | Defines repository purpose, source-of-truth boundaries, publishing layers, scaffold, and development constraints. | Repository maintainers and automated contributors | canonical |
| Editorial System | `docs/editorial/README.md` | Identifies the governance directory and assigns roles to the canon, manuscript specification, and editorial decisions. | Editors and repository maintainers | working |
| Monographs | `resources/monographs/README.md` | Defines volume organization and the separation between author source, editorial manuscript, and generated output. | Authors, editors, and publishing maintainers | working |

## Editorial authorities

| Title | Canonical path | Purpose | Intended audience | Maturity |
| --- | --- | --- | --- | --- |
| The x-change Monographs — Editorial Canon v2.0 | `docs/editorial/editorial-canon-v2.md` | Reserved authority for the series' canonical editorial principles. | Editors, authors, reviewers, and publication producers | draft (canonical role declared) |
| The x-change Monographs — Editorial Manuscript Specification v1.0 | `docs/editorial/editorial-manuscript-specification-v1.md` | Reserved specification for the canonical editorial-manuscript artifact. | Editors and publication producers | draft (canonical role declared) |

Both files contain only their title, a one-line role statement, and a `TODO` instruction to paste approved content.

## Accepted editorial decisions

| Title | Canonical path | Purpose | Intended audience | Maturity |
| --- | --- | --- | --- | --- |
| 0001 — Use Git as Publishing History | `docs/editorial/decisions/0001-use-git-as-publishing-history.md` | Establishes Git commits, branches, tags, and diffs as the record of revisions, authorship, editorial change, releases, and historical decisions. | Editors, reviewers, release managers, and repository maintainers | canonical |
| 0002 — Separate Author Manuscript, Editorial Manuscript, and Publication Master | `docs/editorial/decisions/0002-separate-author-manuscript-editorial-manuscript-and-publication-master.md` | Establishes distinct author, editorial, publication-master, and released-edition artifacts. | Authors, editors, designers, and publication producers | canonical |
| 0003 — Use Movements as Editorial Composition Units | `docs/editorial/decisions/0003-use-movements-as-editorial-composition-units.md` | Establishes movements as the primary unit of editorial composition and independent review. | Editors, reviewers, and publication designers | canonical |

Each decision is explicitly marked `Accepted` and uses the same status/context/decision/consequences structure.

## Founder's writings and monographs

### Volume I

| Title | Canonical path | Purpose | Intended audience | Maturity |
| --- | --- | --- | --- | --- |
| Volume I metadata — *x-change: A Founder's Update* | `resources/monographs/volume-1/metadata/monograph.yaml` | Identifies the first monograph's series, order, title, subtitle, author, scaffold status, and external-typesetting note. | Editors, cataloguers, and future publication automation | draft |
| Volume 1 Source | `resources/monographs/volume-1/source/README.md` | Marks the location intended to preserve the Volume I author manuscript. | Authors, editors, and repository maintainers | working |
| Volume 1 Editorial | `resources/monographs/volume-1/editorial/README.md` | Marks the location intended for the Volume I editorial manuscript and composition files. | Editors and publication producers | working |
| Volume 1 Plates | `resources/monographs/volume-1/plates/README.md` | Marks the location intended for Volume I image plates and placed visual assets. | Editors, designers, and publication producers | working |

The actual Volume I manuscript, editorial composition, typeset master, released edition, and plate files are not present. The metadata describes its status as `placeholder` and notes that it was editorially typeset outside the scaffold.

### Volume II

| Title | Canonical path | Purpose | Intended audience | Maturity |
| --- | --- | --- | --- | --- |
| Volume II metadata — *When Money Adapts to People: A Founder's Discovery Thesis* | `resources/monographs/volume-2/metadata/monograph.yaml` | Identifies the second monograph and points to its intended source manuscript and first editorial movement. | Editors, cataloguers, and future publication automation | working |
| *When Money Adapts to People: A Founder's Discovery Thesis — On the Future of Financial Settlement* | `resources/monographs/volume-2/source/manuscript.md` | Reserved canonical author-manuscript file for Volume II. | Editorial team and eventual monograph readers | draft |
| Volume 2 Editorial | `resources/monographs/volume-2/editorial/README.md` | Marks the location intended for approved Volume II editorial composition files. | Editors and publication producers | working |
| Editorial Composition — Movement I: The Observation | `resources/monographs/volume-2/editorial/movement-01-the-observation.md` | Reserved first movement of the Volume II editorial composition. | Editors, reviewers, and eventual monograph readers | draft |
| Volume 2 Plates | `resources/monographs/volume-2/plates/README.md` | Marks the location intended for Volume II image plates and placed visual assets. | Editors, designers, and publication producers | working |

The source manuscript and first movement contain titles plus `TODO` instructions, not substantive prose. No later movements or plate files are present.

## Publication assets

The repository has two asset-location documents:

- `resources/monographs/volume-1/plates/README.md`
- `resources/monographs/volume-2/plates/README.md`

They are inventoried with their respective volumes above. No image, illustration, chart, photograph, logo package, caption file, rights record, or other placed publication asset is present.

The generated-output locations `build/monographs/volume-1/` and `build/monographs/volume-2/` contain only `.gitkeep`. Those placeholders are not editorial documents and are therefore not separate inventory entries.

## Supporting publishing controls

These files are not editorial prose, but they materially describe or enforce the current publishing scaffold:

| Title | Canonical path | Purpose | Intended audience | Maturity |
| --- | --- | --- | --- | --- |
| Monograph Status Command | `app/Console/Commands/MonographStatusCommand.php` | Reports volume directories and the presence of metadata, source manuscript, and editorial directory. | Repository maintainers and editors operating the scaffold | working |
| Monograph Scaffold Feature Tests | `tests/Feature/MonographScaffoldTest.php` | Verifies selected governance and Volume II paths and the expected status-command table. | Developers and repository maintainers | working |

## Categories not represented by current artifacts

No document matching the following categories exists in the inspected tree:

- Execution Memorandum
- Execution Brief
- white paper outside the monograph series
- Treasury publication
- legal publication
- financial-planning publication
- investor material
- marketing collateral
- campaign brief
- audience guide
- messaging architecture
- story or proof library
- visual-language standard
- publication profile or rendering specification

These are absence statements for inventory completeness, not judgments about whether the repository should contain them.

## Inventory summary

| Category | Unique artifacts |
| --- | ---: |
| Repository and editorial architecture | 3 |
| Editorial authorities | 2 |
| Accepted editorial decisions | 3 |
| Volume I documents | 4 |
| Volume II documents | 5 |
| Supporting publishing controls | 2 |
| **Total inventoried paths** | **19** |

Of the 17 editorial or governance documents, three accepted decisions and the repository policy are substantive authorities. The remaining set consists of working boundary descriptions, metadata, and four titled placeholder documents. The two supporting control files implement and verify structural discovery.
