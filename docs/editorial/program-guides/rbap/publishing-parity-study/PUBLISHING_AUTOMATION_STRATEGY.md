# RBAP Publishing Automation Strategy

## Purpose

This strategy recommends a reproducible two-edition publishing approach while protecting the accepted Thrift publications. No script, stylesheet, template, HTML, or PDF is changed during this study.

## Current Pipeline Findings

### RBAP publisher

The [RBAP publisher](../../../../../scripts/publish-rbap-program-guide.py):

- defines one fixed identity, **Edition 1**;
- scopes the manuscript from the Executive Summary through Section 7;
- rejects any appendix entering that scope;
- renders Markdown structures, tables, callouts, and textual visual placeholders;
- uses the shared Program Guide stylesheet and logo; and
- can generate HTML and an optional PDF through WeasyPrint.

It does not support edition selection, appendix aggregation, Mermaid extraction, SVG rendering, canonical edition names, or edition-specific output validation.

### Thrift publisher

The [Thrift publisher](../../../../../scripts/publish-thrift-bank-program-guide.py):

- imports the RBAP publisher as a base renderer;
- adds explicit Executive and Institutional Reference configurations;
- loads seven shared appendix files in canonical order;
- extracts Mermaid source and renders native SVG;
- validates edition scope and final section;
- changes cover, contents, and running identity by edition; and
- produces separate edition-specific HTML and PDF artifacts.

This implementation is proven by accepted artifacts and recorded hashes. Its dependency on the RBAP script also means an apparently local RBAP refactor could silently alter Thrift rendering.

### Shared assets

The [Program Guide stylesheet](../../../../../resources/publication-assets/styles/program-guide.css) and [x-change logo](../../../../../resources/publication-assets/brand/x-change-logo-orange.png) are already shared publication assets. No separate RBAP visual system is required.

## Options Considered

| Option | Advantages | Risks | Recommendation |
| --- | --- | --- | --- |
| Modify the current RBAP script directly into a shared framework | Centralizes behavior quickly. | Thrift imports it; changes could silently alter accepted Thrift output. | Do not use as the first step. |
| Copy the entire Thrift script for RBAP | Fast and isolates Thrift. | Duplicates a large publisher, preserves hidden coupling, and encourages doctrine-specific assumptions. | Reject. |
| Extend the RBAP script with RBAP-only edition code while preserving existing functions | Limits initial scope. | Still affects the module imported by Thrift unless additions are strictly non-breaking. | Use only with characterization checks and no changed existing behavior. |
| Create a new RBAP two-edition publisher using controlled reuse of proven rendering functions | Protects accepted Thrift artifacts and permits explicit RBAP configuration. | Temporary duplication of selected functions until consolidation. | Recommended for initial implementation. |
| Extract a common Program Guide publishing library first | Best long-term architecture. | Highest immediate regression risk and broadest change before RBAP requirements are proven. | Recommended only after both programs have characterization coverage. |

## Recommended Implementation Approach

### Stage 1 — Characterize accepted builds

Before changing publishing code:

- record current HTML and PDF hashes for RBAP and both Thrift editions;
- capture page counts, contents entries, section sequence, link counts, and expected artifact names;
- establish source-scope checks for each edition;
- retain the accepted Thrift hashes as protected regression evidence; and
- determine which generated variability, if any, prevents byte-identical PDF regeneration.

The characterization work should verify behavior without modifying accepted sources or artifacts.

### Stage 2 — Implement an isolated RBAP edition publisher

Create an RBAP-specific edition entry point or module that:

- accepts `--edition executive` or `--edition institutional-reference`;
- reads edition configuration rather than embedding one global edition label;
- derives the Executive scope from the canonical manuscript;
- composes the Institutional Reference scope from the same manuscript plus approved A–G sources;
- validates all expected major sections and appendix order;
- fails if placeholder markers remain in a canonical build;
- renders approved Mermaid sources to native SVG;
- writes only to edition-specific build paths; and
- produces deterministic publication identity for metadata verification.

Controlled reuse of small, proven rendering functions is preferable to copying the entire Thrift publisher.

### Stage 3 — Publish and verify RBAP

Generate both RBAP editions only after editorial sources are locked. Record:

- source revision;
- edition and version;
- renderer and relevant tool versions;
- input paths;
- output paths;
- physical page count;
- SHA-256;
- verification date; and
- verification result.

### Stage 4 — Consider common-framework extraction

After both programs have stable characterization coverage, evaluate extraction of a shared Program Guide publishing library with declarative edition configuration.

The extraction should be accepted only if:

- all source-scope tests pass;
- accepted Thrift HTML is unchanged or any change is explicitly approved;
- accepted Thrift PDF composition is visually unchanged;
- no artifact is silently overwritten;
- RBAP output remains unchanged; and
- both publishers become simpler rather than merely moving duplication.

## Recommended Configuration Boundary

The common framework should eventually own:

- Markdown structure rendering;
- table, callout, quote, and contents behavior;
- front matter and page furniture;
- appendix composition rules;
- Mermaid-to-SVG rendering;
- link and heading validation;
- placeholder detection;
- HTML and PDF execution; and
- artifact verification hooks.

Edition configuration should own:

- title and subtitle;
- edition and publication labels;
- audience and role;
- manuscript and appendix paths;
- expected section sequence;
- pull-quote selection;
- output paths; and
- edition-specific exclusions.

Doctrine must remain entirely in Markdown and governance sources, never in rendering conditionals.

## Reproducibility Requirements

A canonical build should fail rather than continue when:

- a required source is missing;
- an appendix is out of order;
- an expected heading is absent;
- a placeholder remains;
- a Mermaid diagram fails to render;
- an Executive build accidentally includes an appendix;
- a Reference build omits an appendix;
- the requested output path targets a preserved legacy artifact; or
- metadata identifies a different edition or version from the requested build.

Verification should include:

- clean source-to-build execution;
- HTML link resolution;
- PDF page size and page count;
- contents and running-page sequence;
- absence of clipping, overflow, isolated headings, or accidental blank pages;
- visual inspection of every page;
- extractable text and expected link annotations;
- SHA-256 calculation; and
- a final worktree review proving that only intended source, governance, and generated artifacts changed.

## Accepted Thrift Safeguard

No RBAP implementation task should modify:

- the accepted Thrift manuscripts;
- Thrift appendices or diagrams;
- Thrift metadata or governance;
- accepted Thrift HTML or PDFs; or
- the behavior of the Thrift publisher without explicit scope and regression verification.

If common-framework work changes an accepted Thrift artifact, the change must stop for editorial review. A technically equivalent rebuild is not automatically an authorized canonical change.

## Automation Conclusion

The safest immediate approach is an isolated RBAP two-edition publisher using controlled reuse of proven rendering behavior. Shared-framework consolidation is the appropriate long-term direction, but only after accepted Thrift and new RBAP builds are protected by characterization and visual-regression evidence.
