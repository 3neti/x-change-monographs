# Submission Grammar

## Submission

A curated set of approved publications prepared for a specific institution or recipient group.

## Submission Portfolio

The complete recipient deliverable containing screen, print, navigation, provenance, and verification artifacts.

## Screen Profile

Approved files intended for electronic reading, internal circulation, and presentation. Screen files favor searchable text, links, bookmarks, normal RGB rendering, and a practical electronic file size.

## Print Profile

Approved files intended for physical production. A print profile may use a distinct print master or an imposed production layout, such as a duplex credential sheet.

## Submission Manifest

The canonical declaration of a portfolio's identity, contents, order, recipients, source paths, publication versions, page counts, and governed checksums.

## Source Artifact

An approved publication output included in the portfolio. A Source Artifact retains its own edition, version, status, doctrine, and governance. Packaging does not alter those properties.

## Packaging Derivative

A file created only to navigate, assemble, verify, or deliver a Submission Portfolio, such as the portfolio README, status record, source-artifact record, checksum manifest, or ZIP archive.

A Packaging Derivative is not a new edition of an included publication.

## Canonical rules

1. A portfolio packages approved publications; it does not reopen them.
2. Existing approved PDFs are copied byte-for-byte.
3. Screen and print profiles remain visibly separate.
4. Recipient-facing filenames are ordered, stable, and free from development terminology.
5. The institution manifest drives the build.
6. Source checksums and packaged checksums must match for copied artifacts.
7. Frozen source publications retain their original governance state.
8. A portfolio may be rebuilt without modifying its source publications.
