# RBAP Publishing Parity Risks and Safeguards

## Purpose

This register identifies risks that could compromise RBAP doctrine, edition integrity, repository history, accepted Thrift publications, or artifact reproducibility during a future two-edition implementation.

## Risk Register

| Risk | Likelihood | Impact | Safeguard | Stop condition |
| --- | --- | --- | --- | --- |
| Doctrine leakage from Thrift into RBAP | Medium | Critical | Treat Thrift as a publishing benchmark only. Require source traceability for every RBAP appendix statement and diagram. | Any proposed statement relies only on Thrift institution-specific doctrine. |
| Edition drift | Medium | High | Use one frozen narrative and shared appendix sources. Maintain an Edition Comparison and automated scope checks. | Editions express different authority, custody, settlement, Treasury, or Program roles. |
| Accidental rewriting of Sections 1–7 | Medium | Critical | Record baseline hash and diff the canonical manuscript after every task. Limit changes to approved factual, typographical, cadence, or cross-reference corrections. | A substantive body change lacks explicit editorial authority. |
| Premature Executive Summary lock | Medium | High | Enforce EDR-012: all required appendices complete, then claim and terminology revalidation. | Any Appendix A–G remains incomplete or a Summary claim lacks a source. |
| Ambiguous edition naming | High | High | Use explicit Executive Edition and Institutional Reference Edition labels, each with First Edition and Version 1.0. Preserve “Edition 1” as a legacy identity. | Metadata, cover, filename, and README disagree. |
| Legacy artifact overwrite | Medium | High | Write canonical editions to new paths. Treat current Edition 1 PDF and HTML as immutable. | A build target resolves to an existing legacy path. |
| Duplicated or fragile publishing scripts | High | Medium | Use an isolated RBAP edition publisher first; characterize both programs before shared-framework extraction. | Implementation copies the full Thrift publisher or changes shared behavior without regression evidence. |
| Silent changes to accepted Thrift publication | Medium | Critical | Record protected Thrift hashes and inspect worktree changes. Do not modify Thrift sources, metadata, or artifacts during RBAP implementation. | Any accepted Thrift source or artifact changes without separate approval. |
| Build/source mixing | Low | High | Keep Markdown, YAML, and diagram sources under editorial directories; keep HTML, PDF, and rendered SVG under `build/` or temporary build space. | Canonical content exists only in generated output. |
| Missing artifact provenance | High | High | Record source revision, version, edition, output path, page count, hash, pipeline, stylesheet, and approval date in metadata. | An artifact cannot be traced to a source composition and revision. |
| Incomplete benchmark ZIP | High | Medium | Use the live repository as source of truth; treat ZIPs as review packages only. | A decision is based on ZIP absence rather than live-source inspection. |
| Appendix inconsistency | High | High | Draft A–G separately, use controlled terminology, and perform cross-appendix parity review before Summary lock. | Two appendices define the same canonical term or responsibility differently. |
| Diagram inconsistency | High | High | Maintain governed text-based sources, trace each diagram to doctrine, and review diagrams separately from styling. | A diagram contradicts prose or implies an unapproved role or flow. |
| Shared settlement mistaken for shared tenancy | Medium | Critical | Require Deployment and Program Participants diagrams to show separate bank deployments, records, credentials, and authority. | Any representation suggests one shared RBAP production instance or database. |
| RBAP depicted as a bank, switch, or settlement operator | Low | Critical | Apply EDR-007 to all appendices, diagrams, covers, and summaries. | Publication assigns RBAP custody, settlement execution, or banking authority. |
| x-change depicted as providing banking authority | Low | Critical | Preserve the bank as protagonist and keep authority and settlement boundaries explicit. | Publication assigns banking authority or custody to the software or ODTI. |
| Treasury terminology drift | Medium | High | Use EDR-010 and approved Treasury grammar; lock Glossary and Treasury appendix together. | Funding Event, Treasury, Lien, Facility, Settlement Envelope, Pay Code, or Execution is redefined casually. |
| Invented commercial commitments | Medium | High | Keep Commercial Waterfall conceptual; prohibit invented prices, participation costs, shares, or guaranteed returns. | Appendix C states an unapproved commercial term or automatic outcome. |
| Reference edition becomes a second doctrine source | Medium | High | State that the edition operationalizes and references frozen doctrine; require EDR for any new proposition. | Reference prose cannot be traced to the Program Guide or accepted governance. |
| Navigation ambiguity | Medium | Medium | Update existing READMEs and indexes only after acceptance; distinguish current canonical editions from legacy artifacts. | Multiple links appear current without status or role. |
| PDF/HTML divergence | Medium | Medium | Generate both from the same deterministic composition and compare headings, links, diagrams, and scope. | HTML and PDF represent different source content. |
| Non-reproducible diagram rendering | Medium | Medium | Record renderer configuration and retain Mermaid sources; preserve SVG text where possible. | A canonical diagram cannot be regenerated from repository sources. |
| Accessibility omission | High | Medium | Provide semantic HTML, descriptive captions, and text alternatives; assess tagged PDF support as a later publication enhancement. | Essential meaning exists only in an image without textual equivalent. |

## Safeguard Controls by Workflow Stage

### Before drafting

- approve the two-edition architecture and source lineage;
- define appendix purposes and owners;
- record baseline manuscript and artifact hashes; and
- prohibit changes to accepted Thrift files.

### During appendix and diagram work

- require source traceability;
- review one appendix at a time;
- maintain a controlled vocabulary;
- balk on missing doctrine rather than manufacture content; and
- separate editorial illustrations from canonical diagrams.

### Before Executive Summary lock

- confirm A–G are complete;
- map Summary claims to approved sources;
- confirm no appendix introduced a contradiction; and
- record the revalidation decision under EDR-012.

### During automation

- characterize current outputs;
- use new edition-specific paths;
- fail on placeholders and incomplete scope;
- protect legacy and Thrift artifacts; and
- keep doctrine out of renderer conditionals.

### Before acceptance

- inspect every page of both PDFs;
- resolve every Markdown and HTML link;
- verify contents and page numbering;
- record page counts and hashes;
- confirm worktree isolation; and
- perform publication-specific parity review.

## Residual Risks

Even with these safeguards, three judgments remain editorial rather than mechanical:

1. whether an appendix explains existing doctrine or extends it;
2. whether a diagram merely clarifies the narrative or creates a new architectural assertion; and
3. whether a proposed correction to the frozen narrative is genuinely factual or governance-related rather than a reopening of style.

Those judgments require named editorial review and, where doctrine may change, an explicit Editorial Decision Record.

## Risk Conclusion

The greatest risk is not a failed build. It is a polished publication that appears canonical while silently changing the institutional model. Source traceability, EDR-012 sequencing, immutable legacy artifacts, and protected Thrift outputs are therefore mandatory controls rather than administrative preferences.
