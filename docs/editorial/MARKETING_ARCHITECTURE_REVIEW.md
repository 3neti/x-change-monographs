# Marketing Publication Architecture Review

## Scope and evidence basis

This review describes the repository as inspected on 15 July 2026. It separates implemented behavior from declared intent:

- **Implemented** means a file, directory, command, test, or populated field exists in the repository.
- **Declared** means a governance document or README assigns a role to an artifact or location.
- **Planned** means the location exists but the artifact is empty, represented by `.gitkeep`, or contains a `TODO` placeholder.

This document is descriptive. Recommendations appear only in `MARKETING_GAP_ANALYSIS.md` and `MARKETING_ROADMAP.md`.

## Current operating model

The repository is a Laravel application being used primarily as a version-controlled publishing system for **The x-change Monographs**. Its publishing model has three implemented characteristics:

1. Markdown files hold governance and intended prose sources.
2. YAML files hold volume-level metadata.
3. Git holds revision history and is explicitly designated as the canonical publishing history.

The architecture declares five distinct layers:

1. Editorial governance
2. Author manuscripts
3. Editorial manuscripts
4. Publication masters
5. Generated builds or released editions

The first three layers have directory representation, although much of their content remains placeholder material. Publication masters do not yet have an identified location or file convention. Generated build directories exist but contain no publication output.

## Overall directory organization

```text
.
├── app/Console/Commands/                 Laravel publishing automation
├── build/monographs/                     Generated-output boundary
│   ├── volume-1/                         Empty except for .gitkeep
│   └── volume-2/                         Empty except for .gitkeep
├── docs/editorial/                       Editorial governance and decisions
│   └── decisions/                        Numbered accepted decisions
├── resources/monographs/                 Canonical monograph source tree
│   ├── volume-1/
│   │   ├── editorial/                    Editorial composition location
│   │   ├── metadata/                     YAML volume record
│   │   ├── plates/                       Visual-asset location
│   │   └── source/                       Preserved author-source location
│   └── volume-2/                         Same volume-level organization
├── scripts/                              Reserved; empty except for .gitkeep
└── tests/Feature/                        Scaffold and command checks
```

The standard Laravel application, configuration, database, web, and frontend directories are also present. They retain starter-kit behavior and do not currently publish or render monographs.

## Publishing-related directories

### `docs/editorial/`

This is the declared source location for editorial governance. It contains:

- a directory README defining the roles of the canon, manuscript specification, and decisions;
- `editorial-canon-v2.md`, currently a titled `TODO` placeholder;
- `editorial-manuscript-specification-v1.md`, currently a titled `TODO` placeholder; and
- three numbered, accepted editorial decisions.

The directory explicitly excludes generated files.

### `resources/monographs/`

This is the declared source location for monograph material. Its README establishes a volume-per-directory model and distinguishes preserved author source from approved editorial composition. Both existing volumes use the same four child directories: `source`, `editorial`, `metadata`, and `plates`.

The two volumes are at different scaffold states:

- **Volume 1** has metadata and directory notices but no `source/manuscript.md` and no editorial composition file. Its metadata says the volume was editorially typeset outside this initial scaffold.
- **Volume 2** has metadata, a source-manuscript path, and one movement path. Both referenced Markdown content files are placeholders rather than populated manuscripts.

### `build/monographs/`

This is the declared destination for generated DOCX, PDF, and other builds. It has per-volume directories, each containing only `.gitkeep`. There are no generated publications, manifests, checksums, or release records in the current tree.

### `scripts/`

This location is reserved but contains only `.gitkeep`. No rendering, validation, conversion, packaging, or release script is present.

### `resources/knowledge/`

No `resources/knowledge` directory exists in the inspected repository. Consequently, there is no implemented knowledge-base organization, engagement tree, financial-planning corpus, story library, or cross-publication source collection under that name.

## Editorial and publication directories

The repository uses **editorial** in two different but compatible scopes:

- `docs/editorial/` governs the publishing system as a whole.
- `resources/monographs/<volume>/editorial/` is intended to hold an individual volume's approved editorial composition.

The repository uses **publication** as a conceptual stage, but there is no directory named `publication`, no publication-master file, and no released-edition manifest. The accepted separation decision names both “Publication Master” and “Released Edition”; their representation is not yet implemented.

The `plates` directories are designated for image plates and placed visual assets. No actual media or asset metadata is present.

## Rendering pipeline

### Declared editorial flow

The governance documents imply this sequence:

```text
Preserved author manuscript
        ↓
Editorial composition, reviewed movement by movement
        ↓
Publication master
        ↓
Released edition / generated build
```

The accepted decisions establish two important boundaries within that flow:

- editorial changes must not overwrite the author's original manuscript; and
- page composition and typography occur after movement-level editorial composition.

### Implemented rendering behavior

There is no monograph rendering pipeline. No command or script converts Markdown and YAML into HTML, DOCX, PDF, or another publication format. There are no templates, print stylesheets, publication profiles, layout specifications, or renderer configuration files.

The Vite configuration builds the Laravel starter frontend from `resources/css/app.css` and `resources/js/app.ts`. That web-asset pipeline is separate from the publishing architecture: it neither reads `resources/monographs/` nor writes `build/monographs/`. The existing `/` route renders the starter `Welcome` page, not a publication.

## Laravel publication infrastructure

The implemented publication-specific Laravel surface is intentionally narrow:

- `app/Console/Commands/MonographStatusCommand.php` defines `monograph:status`.
- The command scans immediate directories under `resources/monographs/`, sorts them, and reports whether each has:
  - `metadata/monograph.yaml`;
  - `source/manuscript.md`; and
  - an `editorial` directory.
- `tests/Feature/MonographScaffoldTest.php` checks the presence of the two governance placeholders, selected Volume 2 paths, and the command's expected table.

The command checks structural presence only. It does not parse YAML, detect `TODO` content, validate metadata fields, inspect editorial files, verify plates, render publications, or assign maturity.

The general Laravel starter application still includes database, user model, Inertia, Vue, Wayfinder, and frontend assets. None is connected to the monograph source tree. Repository policy explicitly states that this is not primarily a conventional web application and prohibits adding web UI or application data structures unless requested.

## Metadata conventions

Metadata is stored at `resources/monographs/<volume>/metadata/monograph.yaml`.

Fields observed across both records are:

| Field | Volume 1 | Volume 2 | Observed role |
| --- | --- | --- | --- |
| `series` | present | present | Shared series title |
| `volume` | present | present | Numeric series order |
| `title` | present | present | Work title |
| `subtitle` | present | present | Primary subtitle |
| `secondary_subtitle` | absent | present | Additional title line |
| `status` | `placeholder` | `editorial-composition` | Free-text workflow state |
| `author.name` | present | present | Author identity |
| `author.affiliation` | absent | present | Institutional attribution |
| `source.manuscript` | absent | present | Repository-relative canonical source pointer |
| `editorial.movement_01` | absent | present | Repository-relative editorial component pointer |
| `notes` | present | absent | Free-text qualification |

The records use lower-case snake-case keys, quoted strings, integers for volume numbers, nested maps for people and artifact references, and repository-relative paths. No schema, required-field definition, controlled status vocabulary, dates, edition identifiers, audience fields, rights data, asset references, or output profiles are present.

## README hierarchy

There is no root `README.md`. Repository-level publishing identity and constraints are currently expressed in `AGENTS.md`.

Within the publishing tree, README files work as local boundary notices:

- `docs/editorial/README.md` explains editorial governance.
- `resources/monographs/README.md` explains the series-level source/editorial/build separation.
- volume-level `source`, `editorial`, and `plates` READMEs identify the intended contents of otherwise empty or partial directories.

The hierarchy moves from repository policy to editorial governance, then series organization, then artifact-container descriptions. It does not currently include per-volume top-level READMEs, build READMEs, contributor workflows, or release instructions.

## Naming conventions

Observed conventions include:

- lower-case kebab-case for Markdown governance filenames;
- numeric version suffixes for authorities, such as `-v2` and `-v1`;
- four-digit sequence prefixes for decisions, such as `0001-`;
- `volume-<number>` for volume directories;
- `movement-<two-digit-number>-<slug>.md` for editorial composition units;
- the stable metadata filename `monograph.yaml`;
- the stable author-source filename `manuscript.md` where implemented;
- upper-case underscore filenames for this review set, as explicitly requested; and
- title case in document headings, with em dashes in decision and movement titles.

The decision filenames encode both order and a concise decision statement. The Volume 2 movement filename encodes order and subject. No naming convention is implemented for publication masters, editions, campaigns, collateral, assets, or generated builds.

## Publication workflows

The repository records the following workflow assumptions:

1. Author text is preserved separately from editorial composition.
2. Editorial work proceeds movement by movement, each capable of independent review and approval.
3. Page composition and typography happen after editorial composition.
4. Publication masters are derived artifacts that can be regenerated without changing the manuscript.
5. Released editions and generated files are not the source of truth.
6. Git commits, branches, tags, and diffs carry revision and release history.

Only the structural status check is automated. No approval markers, review state transitions, edition tagging convention, release checklist, or build invocation is implemented in repository files.

## Canonical source locations

| Material | Canonical or declared location | Current state |
| --- | --- | --- |
| Editorial principles | `docs/editorial/editorial-canon-v2.md` | Declared canonical role; content is a `TODO` placeholder |
| Editorial manuscript specification | `docs/editorial/editorial-manuscript-specification-v1.md` | Declared canonical role; content is a `TODO` placeholder |
| Durable editorial decisions | `docs/editorial/decisions/` | Three accepted, substantive records |
| Author manuscripts | `resources/monographs/<volume>/source/` | Volume 1 has only a README; Volume 2 manuscript is a placeholder |
| Editorial manuscripts | `resources/monographs/<volume>/editorial/` | Volume 1 has only a README; Volume 2 has one placeholder movement |
| Monograph metadata | `resources/monographs/<volume>/metadata/monograph.yaml` | Populated for Volumes 1 and 2 |
| Plates and placed assets | `resources/monographs/<volume>/plates/` | READMEs only; no assets |
| Generated artifacts | `build/monographs/<volume>/` | Empty output boundary |
| Revision and release history | Git | Declared canonical mechanism; repository currently has three commits and no observed tagged editions |

## Existing publication automation

Publication-specific automation consists of:

- the `monograph:status` Artisan command; and
- Pest feature checks for scaffold presence and expected command output.

General CI installs dependencies, builds the starter web assets, performs static analysis, and runs tests. The linter workflow formats and lints application code and frontend resources. Neither workflow renders, packages, or releases publications.

No publication-related Composer or npm script exists. No document renderer, metadata validator, link checker, asset processor, PDF inspection step, or release automation is present.

## Current architectural character

The repository has a clear separation-of-concerns model and a small amount of enforcement, but it is still an initial scaffold. Its strongest implemented layer is decision history. Its declared source and output boundaries are consistent, while the prose authorities, manuscripts, publication-master layer, rendering layer, and released outputs remain largely unpopulated or unimplemented.
