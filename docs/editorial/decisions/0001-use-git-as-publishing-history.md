# 0001 — Use Git as Publishing History

## Status

Accepted

## Context

The x-change Monographs require a durable way to track revisions, authorship, editorial changes, releases, and historical decisions.

Rather than inventing a separate publication history mechanism, the repository will use Git as the primary record of change.

## Decision

Use Git commits, branches, tags, and diffs as the canonical publishing history.

## Consequences

- Manuscript changes are reviewable.
- Editorial changes are traceable.
- Releases can be tagged.
- Generated artifacts should not be treated as the source of truth.
