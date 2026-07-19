# Annex E — Publication Architecture

## Purpose

This annex defines the publication lineage for the Government Depository Digital Banking Program. It preserves the distinction between doctrine, program documentation, institution evidence, commercial instruments, and generated publications.

## Canonical Lineage

```text
Movement IV — Institutional Study and canonical doctrine
                         ↓
Government Depository Program foundation
                         ↓
Formal EDR-005 Program Guide
                         ↓
Approved program derivatives and executive publications
                         ↓
Institution Intelligence
                         ↓
Strategic Gap Analysis and Editorial Mapping
                         ↓
Institution Edition
                         ↓
Commercial Proposal and Demonstration Materials
                         ↓
Submission Portfolio
                         ↓
Publication Freeze and explicit version history
```

## Document Classes

| Class | Purpose | Canonical source status |
| --- | --- | --- |
| Institutional Study | Establishes the sector thesis and doctrine | Movement IV is approved and frozen |
| Program foundation | Defines the program field, inherited architecture, governance, annexes, gaps, and roadmap | Established by this Phase 1 package |
| Program Guide | Answers the canonical business questions through Executive Summary, Sections 1–7, and Appendices A–G | Planned; must follow EDR-005 |
| Program derivative | Provides a controlled executive, technical, commercial, stakeholder, financial, or one-page view | Planned; must derive from approved sources |
| Institution Intelligence | Records public evidence and classified findings about a named institution | Required before institution writing |
| Institution Edition | Applies, but does not redesign, canonical doctrine for one institution | Deferred until research gates pass |
| Commercial Proposal | Defines a proposed engagement, scope, terms, and commercial structure | Deferred until institution and engagement evidence exists |
| Demonstration material | Provides an approved experience or credential supporting dialogue | Reuse governed assets; institution-specific generation requires authorization and metadata |
| Submission Portfolio | Packages controlled artifacts with a manifest, validation, and review record | Reuse the canonical Submission Architecture and builder |
| Publication build | Renders a frozen source to PDF, HTML, diagrams, and other generated outputs | Generated only after publication authorization |

## Source and Derivative Rule

Markdown and YAML in the approved editorial and program hierarchy remain canonical. PDFs, HTML, rendered diagrams, contact sheets, and ZIP packages are generated artifacts. A layout issue must be corrected in the renderer or reported; it must not cause an unauthorized silent change to a frozen manuscript.

## Edition and Freeze Rule

An approved edition must record its title, edition, version, status, source, artifacts, checksums, renderer, and freeze decision. A frozen version remains reproducible and must not be overwritten. Future changes require an explicit new version and, when doctrine changes, an Editorial Decision Record.

## Reuse Rule

The Government Depository workstream should reuse the established Program Guide house style, diagram pipeline, Submission Portfolio architecture, checksum practices, QA conventions, Institution Intelligence methodology, and demonstration-credential grammar. It must not copy institution-specific facts, claims, commercial terms, or imagery from another banking track.
