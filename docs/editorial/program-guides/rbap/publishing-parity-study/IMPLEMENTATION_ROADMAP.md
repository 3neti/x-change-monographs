# RBAP Publishing Parity Implementation Roadmap

## Status

This roadmap is a reviewable recommendation. It does not authorize implementation or change current editorial status.

Each phase has an explicit governance prerequisite and review gate. A phase may prepare evidence for the next phase, but it must not silently grant the authority that the next phase requires.

## Implementation Update — 18 July 2026

The appendix-completion assignment authorized the reference material while deferring the separate Executive Edition and the two-edition EDR. Formal review accepted Appendices A–G as canonical and locked institutional reference source material, with governed diagram source embedded in Appendix G. The Executive Summary was subsequently revalidated under EDR-012 and locked without wording changes. The complete editorial source is now canonical and locked. Final publication governance, rendering, accessibility tagging, frozen-body substitution, and pagination remain pending.

## Phase 1 — Approve the Publication Architecture

**Objective:** Decide whether RBAP should adopt the Executive Edition and Institutional Reference Edition model described in this study.

**Files affected:** This study only during review. No canonical source changes.

**Governance prerequisite:** Editorial review of all eight study documents.

**Verification:** Confirm the proposed roles, source relationship, legacy treatment, appendix model, and automation boundary are understood.

**Principal risks:** Treating structural similarity to Thrift as sufficient authority; importing Thrift doctrine; assuming a separate expanded body is required.

**Review gate:** Written approval, rejection, or requested revision of the proposed architecture.

## Phase 2 — Record the Two-Edition Decision

**Objective:** Establish binding RBAP publication authority and change controls.

**Likely files affected:**

- `docs/editorial/decisions/EDITORIAL_DECISION_REGISTER.md`
- `docs/editorial/program-guides/rbap/README.md`
- `docs/editorial/program-guides/rbap/metadata.yaml`

**Governance prerequisite:** Phase 1 approval and confirmation of the next available EDR identifier.

**Verification:** Confirm that the decision defines both editions, neither-supersedes relationship, source lineage, Executive Summary sequence, appendix model, legacy-artifact preservation, and future-change policy.

**Principal risks:** Ambiguous naming; accidental canonicalization of incomplete sources; implied authority from EDR-013.

**Review gate:** Accepted RBAP two-edition EDR. Metadata may record an approved architecture but must not yet claim publication completion.

## Phase 3 — Establish Appendix and Diagram Sources

**Objective:** Create governed, separately reviewable source locations for Appendices A–G and body illustrations.

**Likely files affected:**

- new `docs/editorial/program-guides/rbap/appendices/*.md` sources;
- the main manuscript only for permitted appendix-registry cross-references;
- the cross-program parity checklist as individual sources are approved.

**Governance prerequisite:** Accepted two-edition EDR and approved appendix-source model.

**Verification:** Confirm every new source has a declared purpose, canonical-source citations, status, and owner; confirm Sections 1–7 are otherwise unchanged.

**Principal risks:** Doctrine leakage, duplicated appendix content, source ambiguity, and treating diagrams as decoration rather than governed records.

**Review gate:** Appendix and diagram source scaffold approved. Placeholders remain clearly non-canonical until substantive review.

## Phase 4 — Complete and Lock Appendices A–G

**Status:** Complete — Appendices A–G are canonical and locked as institutional reference source material. Appendix G rendering and placement remain publication-workflow matters.

**Objective:** Complete all mandatory reference coverage and canonical diagrams without extending doctrine.

**Likely files affected:** Appendix and diagram sources; parity checklist status records.

**Governance prerequisite:** Approved source scaffold and appendix-by-appendix editorial assignments.

**Verification:**

- trace every substantive statement to frozen RBAP sources or accepted EDRs;
- answer all required FAQ questions;
- complete all ten canonical diagram requirements or record an approved deviation;
- confirm controlled terminology across A–G; and
- perform separate Governance, Treasury, Commercial, Deployment, FAQ, Glossary, and Diagram reviews.

**Principal risks:** Silent new doctrine, inconsistent Treasury terms, shared-tenancy implications, invented commercial terms, or copying Thrift-specific examples.

**Review gate:** Each appendix locked individually, followed by a complete Appendix A–G parity review.

## Phase 5 — Revalidate and Lock the Executive Summary

**Status:** Complete — Outcome A. The Executive Summary was revalidated against the locked narrative and Appendices A–G and locked without wording changes.

**Objective:** Satisfy EDR-012 after all required supporting material is complete.

**Likely files affected:** The Executive Summary only if claim, terminology, or cross-reference correction is necessary; metadata and workflow status after approval.

**Governance prerequisite:** All Appendices A–G substantively complete and locked.

**Verification:** Map every Summary claim to Sections 1–7 or approved appendices; confirm no new concept is introduced; confirm all terms match the final glossary and diagrams.

**Principal risks:** Premature lock, summary expansion, or using appendix detail to change the Board-level proposition.

**Review gate:** Formal Executive Summary lock under EDR-012. Any change to Sections 1–7 requires separate justification.

## Phase 6 — Canonicalize the Executive Edition

**Objective:** Convert the accepted First Edition scope into the canonical Executive Edition without rewriting the frozen narrative.

**Likely files affected:** Executive metadata, RBAP README, edition comparison draft, and future edition-specific build outputs. Existing Edition 1 artifacts remain unchanged.

**Governance prerequisite:** Accepted two-edition EDR and locked Executive Summary.

**Verification:** Confirm correct title hierarchy, edition label, First Edition, Version 1.0, source scope, audience, canonical role, and legacy-artifact references.

**Principal risks:** Overwriting Edition 1, ambiguous edition naming, or treating a rebuild as editorial acceptance.

**Review gate:** Executive Edition source composition and metadata approved for publication build.

## Phase 7 — Compose the Institutional Reference Edition

**Objective:** Define a deterministic source composition consisting of the same canonical narrative plus Appendices A–G.

**Likely files affected:** Institutional Reference metadata, edition comparison, publication parity report, and a composition manifest or reference source only if required by the approved architecture.

**Governance prerequisite:** Locked narrative, Summary, appendices, and diagrams.

**Verification:** Confirm no narrative fork, no duplicated appendix sources, correct appendix order, intended audience, and complete mandatory coverage.

**Principal risks:** Edition drift, unnecessary body expansion, contradictory summary text, or treating reference elaboration as new doctrine.

**Review gate:** Institutional Reference source composition approved for publication build.

## Phase 8 — Implement and Characterize Publishing Automation

**Objective:** Add reproducible edition-aware RBAP publication without changing accepted Thrift behavior.

**Likely files affected:** A new or carefully bounded RBAP edition publisher; automated checks if repository conventions support them. Shared stylesheet changes only if a demonstrated cross-edition defect requires them.

**Governance prerequisite:** Approved edition source compositions and [Publishing Automation Strategy](PUBLISHING_AUTOMATION_STRATEGY.md).

**Verification:** Characterize current RBAP and Thrift artifacts before changes; validate both RBAP edition scopes; confirm protected Thrift sources and artifacts remain unchanged.

**Principal risks:** Fragile script duplication, hidden RBAP-to-Thrift coupling, non-deterministic diagrams, or silent artifact replacement.

**Review gate:** Dry-run HTML output and source-scope validation reviewed before canonical PDF generation.

## Phase 9 — Generate and Verify Canonical Artifacts

**Objective:** Produce publication-quality HTML and PDF companions for both editions.

**Likely files affected:** Edition-specific files under `build/program-guides/rbap/` and `build/pdf/`; metadata only after final verification values are known.

**Governance prerequisite:** Approved sources, metadata, and publishing automation.

**Verification:**

- resolve all HTML links;
- verify A4 page geometry, contents, page numbering, headers, and footers;
- inspect every PDF page;
- confirm no placeholder, clipping, overflow, malformed table, isolated heading, or accidental blank page;
- confirm Executive scope excludes appendices;
- confirm Reference scope includes A–G;
- calculate page counts and SHA-256 values; and
- verify accepted Thrift artifacts remain unchanged.

**Principal risks:** Build/source mixing, missing provenance, accidental legacy overwrite, diagram rendering failure, and publication drift between HTML and PDF.

**Review gate:** Signed publication QA report with final artifact identifiers.

## Phase 10 — Editorial Acceptance and Final Lock

**Objective:** Accept both RBAP editions as canonical publications and complete navigation.

**Likely files affected:**

- new `EDITORIAL_ACCEPTANCE.md`;
- edition metadata;
- Edition Comparison;
- publication-specific Parity Report;
- RBAP README;
- Program Guide and editorial indexes;
- Editorial Decision Register status or notes, where required.

**Governance prerequisite:** Successful Phase 9 verification and no unresolved parity gap.

**Verification:** Confirm doctrine unchanged, editions correctly related, artifacts traceable, page counts and hashes accurate, all links valid, and permitted future changes explicit.

**Principal risks:** Accepting incomplete coverage, navigation pointing to legacy artifacts as current, or implying that one edition supersedes the other.

**Review gate:** Editorial Acceptance adopted; both editions marked canonical and locked; future work limited to approved corrections, publication maintenance, or explicit EDR authority.

## Recommended Next Implementation Task

After this inspection study is reviewed, the next task should be limited to **Phase 1: approve or revise the proposed RBAP publication architecture**.

It should not draft appendices, create diagrams, change metadata, or alter publishing code. Once the architecture is approved, a separate task may prepare the RBAP two-edition Editorial Decision Record for review.
