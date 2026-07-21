# Correspondence Architecture

## Purpose

The Correspondence architecture preserves formal institutional communication as a governed historical layer within the x-change publishing system. It records what accompanied a submission, who received it, its delivery context, and the evidence available to verify the record.

## Dependency direction

```text
Approved Publications
        ↓
Submission Portfolio
        ↓
Correspondence
        ↓
Delivery Record
```

Correspondence may reference a Submission Portfolio and its included publications. It does not own, modify, supersede, or reproduce them.

## Canonical layers

1. **Approved Publications** retain their own doctrine, version, edition, and publication governance.
2. **Submission Portfolio** assembles approved publications for governed delivery.
3. **Correspondence** records the institutional communication accompanying or concerning that delivery.
4. **Delivery Record** preserves factual transmission context without unnecessary private routing data.

## Record classes

A correspondence record must identify itself as one of the following:

- exact sent correspondence;
- reconstructed sent correspondence;
- draft correspondence; or
- correspondence template.

Sent status and textual fidelity are separate assertions. Knowledge that a message was dispatched does not establish that a later reconstruction is a verbatim transcript.

## Canonical source and attachments

The Markdown correspondence record and its metadata are the canonical source. Referenced attachments remain in their governed publication or submission locations. The Correspondence source directory must not contain duplicate copies of the underlying submission archive.

## Governance rules

1. A sent record must never be silently rewritten.
2. Corrections to historical metadata must be documented in the record or commit history.
3. Editorial improvements belong in a template or later communication, not in an exact sent record.
4. Related submissions must be identified by title, version, and release tag where available.
5. A reconstructed message must remain explicitly distinguishable from an exact transcript.
6. Email addresses may remain blank when they are not safely available.
7. Delivery timestamps, addresses, headers, tokens, signatures, and routing metadata must not be invented or retained unnecessarily.
8. Correspondence does not change the status of an attached publication or submission.

## Change control

An exact sent record is immutable except for a documented correction to its historical representation. A reconstructed sent record may be replaced by an exact sent copy when verified evidence becomes available; the replacement must retain the provenance of the earlier reconstruction and record the change explicitly.
