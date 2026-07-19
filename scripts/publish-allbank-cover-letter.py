#!/usr/bin/env python3

from __future__ import annotations

import argparse
import base64
import hashlib
import html
import json
import re
import shutil
import subprocess
from pathlib import Path

from pypdf import PdfReader


TITLE = "Submission of Proposal for a Provisional License and Proof of Concept"
DOCUMENT_TYPE = "Cover Letter"
EDITION = "First Edition"
VERSION = "1.0"
STATUS = "Submitted"
LETTER_DATE = "20 July 2026"
LETTER_DATE_ISO = "2026-07-20"
PROPOSAL_NUMBER = "ODTI-2026-001"
CONFIDENTIALITY = "Confidential Commercial Information"
LEGAL_ENTITY = "Open Disbursement Technologies, Inc."
ADDRESSEE = "Mr. Jesus Vicente Garcia"
ATTENTION = "Ms. Digna Samonte"
SIGNATORY = "Guido Alfredo A. Delgado"
EXPECTED_SOURCE_SHA256 = (
    "e7ee41e9bcd189cdf26a2b72ecd0fc9021a0647c5259d09faeb936696359dde4"
)
EXPECTED_PROPOSAL_PDF_SHA256 = (
    "f387400b6c23fc5e51a32a641e02657031baf08e7301b599795a6345ce68396f"
)
EXPECTED_ATTACHMENT_PDF_SHA256 = (
    "a06b70cadcd5fa6c73b2ebb8e86acb7979731fc972da11039a5f29c988528210"
)

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
LOGO_PATH = (
    REPOSITORY_ROOT
    / "resources"
    / "publication-assets"
    / "brand"
    / "x-change-logo-orange.png"
)
PROPOSAL_PDF = (
    REPOSITORY_ROOT
    / "build"
    / "pdf"
    / "allbank-provisional-license-and-poc-proposal-v1.0.pdf"
)
ATTACHMENT_PDF = (
    REPOSITORY_ROOT
    / "build"
    / "pdf"
    / "thrift-bank-digital-banking-program-guide-allbank-edition-executive-first-edition-v1.0.pdf"
)
OUTPUT_STEM = "allbank-cover-letter-v1.0"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def render_inline(value: str) -> str:
    escaped = html.escape(value, quote=False)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", escaped)
    return escaped


def render_block_lines(lines: list[str]) -> str:
    rendered: list[str] = []
    for line in lines:
        hard_break = line.endswith("\\") or line.endswith("  ")
        normalized = line.rstrip()
        if normalized.endswith("\\"):
            normalized = normalized[:-1]
        rendered.append(render_inline(normalized))
        rendered.append("<br>" if hard_break else " ")
    return "".join(rendered).rstrip()


def split_blocks(markdown: str) -> list[list[str]]:
    blocks: list[list[str]] = []
    current: list[str] = []
    for line in markdown.splitlines():
        if not line.strip():
            if current:
                blocks.append(current)
                current = []
            continue
        current.append(line)
    if current:
        blocks.append(current)
    return blocks


def validate_source(markdown: str) -> None:
    required = (
        "# OPEN DISBURSEMENT TECHNOLOGIES, INC.",
        "E1504 Philippine Stock Exchange Centre",
        "Exchange Road, Ortigas Center",
        "Pasig City 1605",
        LETTER_DATE,
        ADDRESSEE,
        "President\\\nAllBank",
        "**Attention:**",
        ATTENTION,
        "Chief Technology Officer",
        f"**Subject: {TITLE}**",
        "Dear Mr. Garcia,",
        "**Two Demonstration Pay Codes**",
        "**GUIDO ALFREDO A. DELGADO**",
        "President and Chief Executive Officer",
    )
    for value in required:
        if value not in markdown:
            raise ValueError(f"Required cover-letter record is missing: {value}")
    if "redemption" in markdown.lower():
        raise ValueError("The Cover Letter must not include redemption instructions.")
    if re.search(r"\b(?:test codes|sample codes|stubs)\b", markdown, re.IGNORECASE):
        raise ValueError("Demonstration Pay Codes are described using a prohibited term.")
    if len(re.findall(r"^\d+\. ", markdown, flags=re.MULTILINE)) != 6:
        raise ValueError("The two three-item enclosure lists are incomplete.")


def render_letter(markdown: str) -> str:
    blocks = split_blocks(markdown)
    rendered: list[str] = []
    enclosure_list_seen = 0

    for block_index, lines in enumerate(blocks):
        text = "\n".join(lines)
        if block_index in {0, 1}:
            continue
        if text == "---":
            rendered.append('<div class="enclosure-rule"></div>')
            continue
        if all(re.match(r"^\d+\. ", line) for line in lines):
            enclosure_list_seen += 1
            list_class = "package-list" if enclosure_list_seen == 1 else "enclosure-list"
            items = "".join(
                f"<li>{render_inline(re.sub(r'^\d+\.\s+', '', line))}</li>"
                for line in lines
            )
            rendered.append(f'<ol class="{list_class}">{items}</ol>')
            continue

        content = render_block_lines(lines)
        plain = re.sub(r"\*\*|\\", "", text)
        class_name = "letter-paragraph"
        tag = "p"
        if plain == LETTER_DATE:
            class_name = "letter-date"
        elif plain.startswith(ADDRESSEE):
            class_name = "recipient"
            tag = "address"
        elif plain.startswith("Attention:"):
            class_name = "attention"
            tag = "div"
        elif plain.startswith("Subject:"):
            class_name = "subject"
            tag = "div"
        elif plain == "Dear Mr. Garcia,":
            class_name = "salutation"
        elif plain == "Very truly yours,":
            class_name = "closing"
        elif plain.startswith("GUIDO ALFREDO A. DELGADO"):
            class_name = "signature"
            tag = "div"
        elif plain == "Enclosures":
            class_name = "enclosures-heading"
            tag = "div"
        rendered.append(f'<{tag} class="{class_name}">{content}</{tag}>')

    if enclosure_list_seen != 2:
        raise ValueError("Expected introductory and final enclosure lists.")
    return "\n".join(rendered)


def publication_html(markdown: str, canonical_source: str) -> str:
    if not LOGO_PATH.is_file():
        raise FileNotFoundError(f"Logo asset not found: {LOGO_PATH}")
    body = render_letter(markdown)
    logo_data = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    logo_uri = f"data:image/png;base64,{logo_data}"

    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="{LEGAL_ENTITY}">
  <meta name="description" content="Formal cover letter accompanying the AllBank commercial submission package">
  <meta name="document-type" content="{DOCUMENT_TYPE}">
  <meta name="edition" content="{EDITION}">
  <meta name="version" content="{VERSION}">
  <meta name="status" content="{STATUS}">
  <meta name="letter-date" content="{LETTER_DATE_ISO}">
  <meta name="proposal-number" content="{PROPOSAL_NUMBER}">
  <meta name="confidentiality" content="{CONFIDENTIALITY}">
  <meta name="canonical-source" content="{html.escape(canonical_source, quote=True)}">
  <title>{TITLE} — AllBank</title>
  <style>
    :root {{
      --ink: #172533;
      --muted: #68747e;
      --line: #cfd5d9;
      --accent: #e6691c;
      --panel: #f4f5f4;
    }}
    @page {{
      size: A4;
      margin: 13.5mm 20mm 14mm;
      @bottom-left {{
        content: "{CONFIDENTIALITY} · {PROPOSAL_NUMBER}";
        color: #68747e;
        font-family: "Avenir Next", Avenir, sans-serif;
        font-size: 6.25pt;
        letter-spacing: 0.035em;
      }}
      @bottom-right {{
        content: "COVER LETTER · VERSION {VERSION} · PAGE " counter(page) " OF " counter(pages);
        color: #68747e;
        font-family: "Avenir Next", Avenir, sans-serif;
        font-size: 6.25pt;
        letter-spacing: 0.035em;
      }}
    }}
    * {{ box-sizing: border-box; }}
    html {{ color: var(--ink); font-family: Charter, Georgia, serif; }}
    body {{ margin: 0; font-size: 8.75pt; line-height: 1.28; }}
    .letterhead {{
      position: relative;
      min-height: 21mm;
      margin-bottom: 4mm;
      padding-bottom: 3.2mm;
      border-bottom: 0.65pt solid var(--line);
    }}
    .letterhead h1 {{
      margin: 0 0 1.5mm;
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 11.2pt;
      font-weight: 700;
      letter-spacing: 0.035em;
    }}
    .letterhead address {{ color: var(--muted); font-size: 7.55pt; font-style: normal; line-height: 1.3; }}
    .letterhead img {{
      position: absolute;
      top: 0;
      right: 0;
      width: 6mm;
      height: 17mm;
      object-fit: contain;
    }}
    .letter-date {{ margin: 0 0 3mm; }}
    .recipient {{ margin: 0 0 2.2mm; font-style: normal; }}
    .attention {{
      float: right;
      width: 70mm;
      margin-top: -13.5mm;
      padding-left: 7mm;
      border-left: 0.75pt solid var(--accent);
      line-height: 1.34;
    }}
    .subject {{
      clear: both;
      margin: 4mm 0 3mm;
      padding: 2.4mm 3.2mm;
      border-left: 1.2pt solid var(--accent);
      background: var(--panel);
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 8.2pt;
      line-height: 1.25;
    }}
    .salutation {{ margin: 0 0 2.2mm; }}
    .letter-paragraph {{ margin: 0 0 2.2mm; text-align: justify; orphans: 3; widows: 3; }}
    .package-list {{ margin: 0.5mm 0 2.2mm 5.8mm; padding: 0; }}
    .package-list li {{ margin: 0 0 0.6mm 2.5mm; padding-left: 0.8mm; }}
    .package-list li::marker {{ color: var(--accent); font-family: "Avenir Next", Avenir, sans-serif; font-weight: 700; }}
    .closing {{ margin: 3mm 0 9mm; }}
    .signature {{ font-size: 8.1pt; line-height: 1.35; }}
    .signature strong {{ font-family: "Avenir Next", Avenir, sans-serif; font-size: 8.5pt; letter-spacing: 0.025em; }}
    .enclosure-rule {{ margin: 4mm 0 2.2mm; border-top: 0.55pt solid var(--line); }}
    .enclosures-heading {{
      margin-bottom: 1mm;
      color: var(--muted);
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 6.6pt;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
    }}
    .enclosure-list {{ margin: 0 0 0 4.5mm; padding: 0; columns: 2; column-gap: 9mm; font-size: 6.85pt; line-height: 1.24; }}
    .enclosure-list li {{ margin: 0 0 0.6mm 2.5mm; padding-left: 0.6mm; break-inside: avoid; }}
    .enclosure-list li::marker {{ color: var(--accent); font-family: "Avenir Next", Avenir, sans-serif; font-weight: 700; }}
  </style>
</head>
<body>
  <header class="letterhead">
    <h1>OPEN DISBURSEMENT TECHNOLOGIES, INC.</h1>
    <address>
      E1504 Philippine Stock Exchange Centre<br>
      Exchange Road, Ortigas Center<br>
      Pasig City 1605
    </address>
    <img src="{logo_uri}" alt="x-change logo">
  </header>
  <main>
{body}
  </main>
</body>
</html>
'''


def run_weasyprint(html_path: Path, pdf_path: Path, profile: str) -> None:
    executable = shutil.which("weasyprint")
    if executable is None:
        raise RuntimeError("weasyprint executable not found on PATH.")
    command = [
        executable,
        "--pdf-tags",
        "--srgb",
        "--custom-metadata",
        "--pdf-identifier",
        f"urn:odti:allbank-cover-letter:{VERSION}:{profile}",
    ]
    if profile == "publication":
        command.extend(("--pdf-version", "1.7", "--full-fonts", "--hinting"))
    elif profile == "print":
        command.extend(("--pdf-variant", "pdf/a-2u", "--full-fonts", "--hinting"))
    elif profile == "screen":
        command.extend(("--pdf-version", "1.7", "--optimize-images", "--dpi", "150"))
    else:
        raise ValueError(f"Unsupported PDF profile: {profile}")
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    command.extend((str(html_path), str(pdf_path)))
    subprocess.run(command, check=True)


def render_preview(pdf_path: Path, preview_path: Path) -> None:
    executable = shutil.which("pdftoppm")
    if executable is None:
        raise RuntimeError("pdftoppm executable not found on PATH.")
    preview_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            executable,
            "-f",
            "1",
            "-l",
            "1",
            "-r",
            "144",
            "-png",
            "-singlefile",
            str(pdf_path),
            str(preview_path.with_suffix("")),
        ],
        check=True,
    )


def count_outline(items: list[object]) -> int:
    return sum(
        count_outline(item) if isinstance(item, list) else 1
        for item in items
    )


def pdf_record(path: Path, profile: str) -> dict[str, object]:
    reader = PdfReader(path)
    return {
        "profile": profile,
        "path": str(path.relative_to(REPOSITORY_ROOT)),
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
        "physical_pages": len(reader.pages),
        "bookmarks": count_outline(reader.outline),
        "links": sum(1 for page in reader.pages if "/Annots" in page),
        "tagged": "/StructTreeRoot" in reader.trailer["/Root"],
    }


def update_submission_package(package_directory: Path, publication_pdf: Path) -> list[Path]:
    cover_directory = package_directory / "01-cover-letter"
    proposal_directory = package_directory / "02-commercial-proposal"
    attachment_directory = package_directory / "03-attachment-a"
    for directory in (cover_directory, proposal_directory, attachment_directory):
        if not directory.is_dir():
            raise FileNotFoundError(f"Submission-package directory missing: {directory}")

    cover_pdf = cover_directory / "AllBank-Cover-Letter.pdf"
    cover_readme = cover_directory / "README.md"
    package_readme = package_directory / "README.md"
    package_proposal = (
        proposal_directory / "AllBank-Provisional-License-and-Proof-of-Concept.pdf"
    )
    package_attachment = (
        attachment_directory
        / "Thrift-Bank-Digital-Banking-Program-Guide-AllBank-Edition.pdf"
    )

    if sha256(package_proposal) != EXPECTED_PROPOSAL_PDF_SHA256:
        raise ValueError("Submission-package Commercial Proposal hash mismatch.")
    if sha256(package_attachment) != EXPECTED_ATTACHMENT_PDF_SHA256:
        raise ValueError("Submission-package Attachment A hash mismatch.")

    shutil.copy2(publication_pdf, cover_pdf)
    cover_readme.write_text(
        "# AllBank Cover Letter\n\n"
        f"First Edition · Version {VERSION}\n\n"
        f"Letter Date: {LETTER_DATE}\n\n"
        "The publication PDF in this directory is the relationship document for "
        "the AllBank submission package.\n",
        encoding="utf-8",
    )
    package_readme.write_text(
        "# AllBank submission package\n\n"
        f"Proposal: {PROPOSAL_NUMBER}, Revision 1.0\n\n"
        f"Submission Date: {LETTER_DATE}\n\n"
        "The package contains the signed-ready Cover Letter, Commercial Proposal, "
        "and unchanged Program Guide attachment as separate PDF records. Two "
        "Demonstration Pay Codes are identified as separate enclosures; no Pay Code "
        "asset or redemption instruction is generated by this publishing task.\n",
        encoding="utf-8",
    )
    return [cover_readme, cover_pdf, package_readme, package_proposal, package_attachment]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Publish the AllBank Cover Letter First Edition."
    )
    parser.add_argument("source", type=Path)
    parser.add_argument(
        "--output-directory",
        type=Path,
        default=(
            REPOSITORY_ROOT
            / "build"
            / "institutions"
            / "allbank"
            / "commercial"
            / "cover-letter"
        ),
    )
    parser.add_argument(
        "--package-directory",
        type=Path,
        default=(
            REPOSITORY_ROOT
            / "build"
            / "institutions"
            / "allbank"
            / "commercial"
            / "submission-package"
        ),
    )
    parser.add_argument(
        "--pdf-directory",
        type=Path,
        default=REPOSITORY_ROOT / "build" / "pdf",
    )
    args = parser.parse_args()

    source = args.source.resolve()
    source_hash_before = sha256(source)
    if source_hash_before != EXPECTED_SOURCE_SHA256:
        raise ValueError(
            "Canonical Cover Letter source hash mismatch. Refusing publication: "
            f"{source_hash_before}"
        )
    if sha256(PROPOSAL_PDF) != EXPECTED_PROPOSAL_PDF_SHA256:
        raise ValueError("Committed Commercial Proposal PDF hash mismatch.")
    if sha256(ATTACHMENT_PDF) != EXPECTED_ATTACHMENT_PDF_SHA256:
        raise ValueError("Frozen AllBank Program Guide PDF hash mismatch.")

    markdown = source.read_text(encoding="utf-8")
    validate_source(markdown)
    canonical_source = str(source.relative_to(REPOSITORY_ROOT))
    rendered = publication_html(markdown, canonical_source)

    output_directory = args.output_directory.resolve()
    pdf_directory = args.pdf_directory.resolve()
    package_directory = args.package_directory.resolve()
    output_directory.mkdir(parents=True, exist_ok=True)
    pdf_directory.mkdir(parents=True, exist_ok=True)

    html_path = output_directory / f"{OUTPUT_STEM}.html"
    preview_path = output_directory / f"{OUTPUT_STEM}-preview.png"
    manifest_path = output_directory / "publication-manifest.json"
    checksums_path = output_directory / "SHA256SUMS.txt"
    report_path = output_directory / "render-verification-report.md"
    publication_pdf = pdf_directory / f"{OUTPUT_STEM}.pdf"
    print_pdf = pdf_directory / f"{OUTPUT_STEM}-print.pdf"
    screen_pdf = pdf_directory / f"{OUTPUT_STEM}-screen.pdf"

    html_path.write_text(rendered, encoding="utf-8")
    run_weasyprint(html_path, publication_pdf, "publication")
    run_weasyprint(html_path, print_pdf, "print")
    run_weasyprint(html_path, screen_pdf, "screen")
    render_preview(publication_pdf, preview_path)
    package_records = update_submission_package(package_directory, publication_pdf)

    source_hash_after = sha256(source)
    if source_hash_after != source_hash_before:
        raise RuntimeError("Canonical Cover Letter source changed during publication.")
    if sha256(PROPOSAL_PDF) != EXPECTED_PROPOSAL_PDF_SHA256:
        raise RuntimeError("Commercial Proposal PDF changed during publication.")
    if sha256(ATTACHMENT_PDF) != EXPECTED_ATTACHMENT_PDF_SHA256:
        raise RuntimeError("AllBank Program Guide PDF changed during publication.")

    pdfs = [
        pdf_record(publication_pdf, "publication"),
        pdf_record(print_pdf, "print_pdfa_2u"),
        pdf_record(screen_pdf, "screen_optimized"),
    ]
    if any(record["physical_pages"] != 1 for record in pdfs):
        raise ValueError("Every Cover Letter PDF profile must contain exactly one page.")

    manifest = {
        "title": TITLE,
        "document_type": DOCUMENT_TYPE,
        "edition": EDITION,
        "version": VERSION,
        "status": STATUS,
        "letter_date": LETTER_DATE_ISO,
        "submitted_by": LEGAL_ENTITY,
        "submitted_to": ADDRESSEE,
        "attention": ATTENTION,
        "signatory": SIGNATORY,
        "proposal_number": PROPOSAL_NUMBER,
        "confidentiality": CONFIDENTIALITY,
        "canonical_source": canonical_source,
        "canonical_source_sha256": source_hash_after,
        "renderer": "WeasyPrint 66.0",
        "html": {
            "path": str(html_path.relative_to(REPOSITORY_ROOT)),
            "sha256": sha256(html_path),
            "bytes": html_path.stat().st_size,
        },
        "preview": {
            "path": str(preview_path.relative_to(REPOSITORY_ROOT)),
            "sha256": sha256(preview_path),
            "bytes": preview_path.stat().st_size,
        },
        "pdfs": pdfs,
        "submission_package": [
            {
                "path": str(path.relative_to(REPOSITORY_ROOT)),
                "sha256": sha256(path),
                "bytes": path.stat().st_size,
            }
            for path in package_records
        ],
        "protected_artifacts": {
            "commercial_proposal_pdf_sha256": EXPECTED_PROPOSAL_PDF_SHA256,
            "program_guide_pdf_sha256": EXPECTED_ATTACHMENT_PDF_SHA256,
            "unchanged": True,
        },
        "accessibility": {
            "tagged_pdf": True,
            "language": "en",
            "bookmarks": True,
            "logical_html_landmarks": True,
        },
    }
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    checksum_records = [source, html_path, preview_path, publication_pdf, print_pdf, screen_pdf]
    checksum_records.extend(package_records)
    checksums_path.write_text(
        "".join(
            f"{sha256(path)}  {path.relative_to(REPOSITORY_ROOT)}\n"
            for path in checksum_records
        ),
        encoding="utf-8",
    )
    report_path.write_text(
        "# Render Verification Report\n\n"
        f"- Document: {DOCUMENT_TYPE}, {EDITION}, Version {VERSION}\n"
        f"- Letter Date: {LETTER_DATE}\n"
        f"- Canonical source SHA-256: `{source_hash_after}`\n"
        f"- Commercial Proposal PDF SHA-256: `{EXPECTED_PROPOSAL_PDF_SHA256}`\n"
        f"- AllBank Program Guide PDF SHA-256: `{EXPECTED_ATTACHMENT_PDF_SHA256}`\n"
        "- Publication pages: 1\n"
        "- Automated identity, addressee, attention, subject, signatory, enclosure, source-freeze, and PDF-generation checks: Passed\n"
        "- Page-by-page visual inspection: Pending\n",
        encoding="utf-8",
    )

    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
