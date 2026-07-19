#!/usr/bin/env python3

from __future__ import annotations

import argparse
import base64
import hashlib
import html
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

from pypdf import PdfReader


PROPOSAL_TITLE = "Provisional License and Proof of Concept"
PROGRAM_TITLE = "Thrift Bank Digital Banking Program"
INSTITUTION = "AllBank"
SUBMITTED_BY = "Open Disbursement Technologies, Inc. (ODTI)"
PROPOSAL_NUMBER = "ODTI-2026-001"
PROPOSAL_DATE = "20 July 2026"
PROPOSAL_DATE_ISO = "2026-07-20"
VALID_UNTIL = "19 August 2026"
VALID_UNTIL_ISO = "2026-08-19"
REVISION = "1.0"
STATUS = "Submitted"
CONFIDENTIALITY = "Confidential Commercial Information"
EXPECTED_SOURCE_SHA256 = (
    "50cab1e8f0fd076e9c8e4c13fc9a171981b53618589b55b6592e97c97ecb68cc"
)
EXPECTED_ATTACHMENT_SOURCE_SHA256 = (
    "f0bca701d7bcc817d21c42ce032bd0ef853dc76be99d6517d1d36282b07bd9e2"
)
EXPECTED_ATTACHMENT_PDF_SHA256 = (
    "a06b70cadcd5fa6c73b2ebb8e86acb7979731fc972da11039a5f29c988528210"
)

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
BASE_PUBLISHER_PATH = REPOSITORY_ROOT / "scripts" / "publish-rbap-program-guide.py"
LOGO_PATH = (
    REPOSITORY_ROOT
    / "resources"
    / "publication-assets"
    / "brand"
    / "x-change-logo-orange.png"
)
ATTACHMENT_SOURCE = (
    REPOSITORY_ROOT
    / "docs"
    / "institutions"
    / "allbank"
    / "executive-edition"
    / "allbank-edition-executive-v1.0.md"
)
ATTACHMENT_PDF = (
    REPOSITORY_ROOT
    / "build"
    / "pdf"
    / "thrift-bank-digital-banking-program-guide-allbank-edition-executive-first-edition-v1.0.pdf"
)

OUTPUT_STEM = "allbank-provisional-license-and-poc-proposal-v1.0"


def load_base_publisher():
    spec = importlib.util.spec_from_file_location(
        "rbap_program_guide_publisher", BASE_PUBLISHER_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load base publisher: {BASE_PUBLISHER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


sys.dont_write_bytecode = True
BASE = load_base_publisher()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", ascii_value.lower()).strip("-")


def render_inline(value: str) -> str:
    escaped = html.escape(value, quote=False)
    escaped = re.sub(r"`([^`]+)`", r'<code class="inline-code">\1</code>', escaped)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", escaped)
    return escaped.replace("  ", "<br>")


BASE.render_inline = render_inline


def validate_source(markdown: str) -> None:
    required_values = (
        "# PROPOSAL",
        f"## {PROPOSAL_TITLE}",
        f"### {PROGRAM_TITLE}",
        f"#### {INSTITUTION}",
        f"| Proposal Number | {PROPOSAL_NUMBER} |",
        f"| Proposal Date | {PROPOSAL_DATE} |",
        f"| Valid Until | {VALID_UNTIL} |",
        f"| Proposal Revision | {REVISION} |",
        f"| Status | {STATUS} |",
        "| Fee Applicable to this Proposal | **WAIVED** |",
        "within two (2) to four (4) weeks after all required prerequisites",
        "initial driver enablement is included",
        "Each subsequent stage shall require separate written approval",
        f"valid until **{VALID_UNTIL}**",
    )
    for value in required_values:
        if value not in markdown:
            raise ValueError(f"Required proposal record is missing: {value}")

    headings = re.findall(r"^## (\d+\. .+)$", markdown, flags=re.MULTILINE)
    if [int(heading.split(".", 1)[0]) for heading in headings] != list(range(1, 13)):
        raise ValueError("Proposal sections must appear once in canonical order 1-12.")
    if "3neti" in markdown:
        raise ValueError("3neti must not be identified in the ODTI commercial proposal.")
    if re.search(r"\b(?:email|mobile|telephone|phone)\b", markdown, re.IGNORECASE):
        raise ValueError("Personal contact fields are not permitted in this proposal.")


def render_body(markdown: str) -> tuple[str, list[tuple[str, str]]]:
    start = "## 1. Purpose"
    if start not in markdown:
        raise ValueError("Section 1 boundary not found.")
    lines = markdown[markdown.index(start) :].splitlines()
    rendered: list[str] = []
    contents: list[tuple[str, str]] = []
    section_open = False
    index = 0

    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue

        heading = re.match(r"^(#{2,3})\s+(.+)$", line)
        if heading:
            level = len(heading.group(1))
            label = heading.group(2).strip()
            anchor = slugify(label)
            if level == 2:
                if section_open:
                    rendered.append("</section>")
                section_open = True
                number, title = label.split(". ", 1)
                contents.append((label, anchor))
                rendered.append(
                    f'<section class="proposal-section section-{number}" id="{anchor}">'
                    f'<h2><span>{html.escape(number)}</span>{render_inline(title)}</h2>'
                )
            else:
                rendered.append(f'<h3 id="sub-{anchor}">{render_inline(label)}</h3>')
            index += 1
            continue

        if line.lstrip().startswith("|"):
            block, index = BASE.render_table(lines, index)
            rendered.append(block)
            continue

        if line.startswith("- "):
            items: list[str] = []
            while index < len(lines) and lines[index].startswith("- "):
                items.append(f"<li>{render_inline(lines[index][2:])}</li>")
                index += 1
            rendered.append(f'<ul class="proposal-list">{"".join(items)}</ul>')
            continue

        if line.startswith("```"):
            index += 1
            code_lines: list[str] = []
            while index < len(lines) and not lines[index].startswith("```"):
                code_lines.append(lines[index])
                index += 1
            if index < len(lines):
                index += 1
            code = html.escape("\n".join(code_lines), quote=False)
            rendered.append(f'<pre class="engagement-path">{code}</pre>')
            continue

        paragraph_lines = [line]
        index += 1
        while index < len(lines) and lines[index].strip():
            next_line = lines[index]
            if (
                re.match(r"^#{2,3}\s+", next_line)
                or next_line.startswith("- ")
                or next_line.lstrip().startswith("|")
                or next_line.startswith("```")
            ):
                break
            paragraph_lines.append(next_line)
            index += 1
        paragraph_parts: list[str] = []
        for part in paragraph_lines:
            hard_break = part.endswith("  ") or part.endswith("\\")
            normalized_part = part.rstrip()
            if normalized_part.endswith("\\"):
                normalized_part = normalized_part[:-1]
            paragraph_parts.append(render_inline(normalized_part))
            paragraph_parts.append("<br>" if hard_break else " ")
        paragraph = "".join(paragraph_parts).rstrip()
        rendered.append(f"<p>{paragraph}</p>")

    if section_open:
        rendered.append("</section>")
    if len(contents) != 12:
        raise ValueError(f"Expected 12 proposal sections; found {len(contents)}.")
    return "\n".join(rendered), contents


def publication_html(markdown: str, canonical_source: str) -> str:
    if not LOGO_PATH.is_file():
        raise FileNotFoundError(f"Logo asset not found: {LOGO_PATH}")
    body, _contents = render_body(markdown)
    logo_data = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    logo_uri = f"data:image/png;base64,{logo_data}"

    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="{SUBMITTED_BY}">
  <meta name="description" content="Commercial proposal for a provisional x-change platform license and controlled Proof of Concept for AllBank">
  <meta name="proposal-number" content="{PROPOSAL_NUMBER}">
  <meta name="proposal-date" content="{PROPOSAL_DATE_ISO}">
  <meta name="valid-until" content="{VALID_UNTIL_ISO}">
  <meta name="revision" content="{REVISION}">
  <meta name="status" content="{STATUS}">
  <meta name="confidentiality" content="{CONFIDENTIALITY}">
  <meta name="canonical-source" content="{html.escape(canonical_source, quote=True)}">
  <title>{PROPOSAL_TITLE} — {INSTITUTION} — {PROPOSAL_NUMBER}</title>
  <style>
    :root {{
      --ink: #172533;
      --muted: #68747e;
      --line: #cfd5d9;
      --panel: #f4f5f4;
      --accent: #e6691c;
      --accent-soft: #fff4ec;
    }}
    @page {{
      size: A4;
      margin: 14mm 16.5mm 16mm;
      @top-left {{
        content: "{INSTITUTION} · PROVISIONAL LICENSE AND PROOF OF CONCEPT";
        color: #68747e;
        font-family: "Avenir Next", Avenir, sans-serif;
        font-size: 6.6pt;
        letter-spacing: 0.07em;
      }}
      @top-right {{
        content: "{PROPOSAL_NUMBER}";
        color: #68747e;
        font-family: "Avenir Next", Avenir, sans-serif;
        font-size: 6.6pt;
      }}
      @bottom-left {{
        content: "{CONFIDENTIALITY} · {PROPOSAL_NUMBER} · REVISION {REVISION}";
        color: #68747e;
        font-family: "Avenir Next", Avenir, sans-serif;
        font-size: 6.4pt;
        letter-spacing: 0.04em;
      }}
      @bottom-right {{
        content: "PAGE " counter(page) " OF " counter(pages);
        color: #68747e;
        font-family: "Avenir Next", Avenir, sans-serif;
        font-size: 6.4pt;
      }}
    }}
    @page:first {{
      margin-top: 13mm;
      @top-left {{ content: none; }}
      @top-right {{ content: none; }}
    }}
    * {{ box-sizing: border-box; }}
    html {{ color: var(--ink); font-family: Charter, Georgia, serif; }}
    body {{ margin: 0; font-size: 8.65pt; line-height: 1.32; }}
    .proposal-front {{ position: relative; margin-bottom: 5mm; }}
    .proposal-brand {{ display: block; }}
    .proposal-kicker {{
      color: var(--accent);
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 7.4pt;
      font-weight: 700;
      letter-spacing: 0.19em;
    }}
    .proposal-brand img {{
      position: absolute;
      top: 0;
      right: 0;
      width: 6.5mm;
      height: 16mm;
      object-fit: contain;
    }}
    .proposal-rule {{ width: 19mm; margin: 1mm 0 4mm; border-top: 1.35pt solid var(--accent); }}
    h1 {{
      max-width: 145mm;
      margin: 0;
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 22pt;
      font-weight: 600;
      letter-spacing: -0.025em;
      line-height: 1.08;
    }}
    .program-title {{ margin: 2.4mm 0 0; color: var(--muted); font-size: 11.2pt; font-style: italic; }}
    .institution {{
      margin: 5mm 0 0;
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 12.2pt;
      font-weight: 600;
    }}
    .submitted-by {{ margin: 1mm 0 4mm; color: var(--muted); font-size: 7.9pt; }}
    .administration {{ margin-top: 3mm; }}
    .administration table {{ font-size: 7.25pt; }}
    .administration th {{ width: 30%; }}
    .proposal-section {{ margin: 0 0 3.3mm; }}
    h2 {{
      display: flex;
      gap: 3mm;
      align-items: baseline;
      margin: 5mm 0 2mm;
      padding-top: 2mm;
      border-top: 0.45pt solid var(--line);
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 12.2pt;
      font-weight: 600;
      line-height: 1.15;
      break-after: avoid;
    }}
    h2 span {{ color: var(--accent); font-size: 7pt; font-weight: 700; }}
    h3 {{
      margin: 3.1mm 0 1.2mm;
      color: #344451;
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 8.8pt;
      font-weight: 700;
      break-after: avoid;
    }}
    p {{ margin: 0 0 1.7mm; text-align: justify; orphans: 3; widows: 3; }}
    strong {{ font-weight: 700; }}
    .proposal-list {{
      margin: 1mm 0 2mm 4.5mm;
      padding: 0;
      columns: 2;
      column-gap: 8mm;
    }}
    .proposal-list li {{ margin: 0 0 0.7mm 3mm; padding-left: 0.5mm; break-inside: avoid; }}
    .proposal-list li::marker {{ color: var(--accent); }}
    .table-wrap {{ margin: 1.5mm 0 2.5mm; break-inside: avoid; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 7.65pt; line-height: 1.24; }}
    th {{
      padding: 1.7mm 2.2mm;
      border-bottom: 0.75pt solid var(--accent);
      background: var(--panel);
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 6.55pt;
      font-weight: 700;
      letter-spacing: 0.035em;
      text-align: left;
      text-transform: uppercase;
    }}
    td {{ padding: 1.5mm 2.2mm; border-bottom: 0.35pt solid var(--line); vertical-align: top; }}
    .section-4 .table-wrap:first-of-type td:last-child {{ font-family: "Avenir Next", Avenir, sans-serif; font-weight: 700; }}
    .section-4 p, .section-5 p {{ font-size: 8.15pt; line-height: 1.23; margin-bottom: 1.15mm; }}
    .section-4 h3, .section-5 h3 {{ margin-top: 2.5mm; }}
    .section-4 .table-wrap, .section-5 .table-wrap {{ margin-bottom: 1.8mm; }}
    .section-5 .proposal-list {{ font-size: 8.1pt; line-height: 1.24; margin-bottom: 1.4mm; }}
    #sub-6-2-odti {{ break-before: page; page-break-before: always; }}
    .engagement-path {{
      margin: 2mm 0 3mm;
      padding: 3mm 4mm;
      border-left: 1.25pt solid var(--accent);
      background: var(--panel);
      color: #344451;
      font-family: Menlo, Monaco, monospace;
      font-size: 6.7pt;
      line-height: 1.35;
      text-align: center;
      white-space: pre-wrap;
      break-inside: avoid;
    }}
    .section-7 h3 {{ display: inline; margin-right: 1mm; }}
    .section-7 h3 + p {{ display: inline; }}
    .section-7 h3 + p::after {{ content: ""; display: block; margin-bottom: 1.5mm; }}
    .section-10 {{ break-before: page; }}
    .section-10 h3 {{ margin-top: 6mm; }}
    .section-10 p {{ margin-bottom: 4.5mm; text-align: left; }}
    .section-11 p, .section-12 p {{ text-align: left; }}
    .section-12 {{ margin-bottom: 0; }}
  </style>
</head>
<body>
  <header class="proposal-front">
    <div class="proposal-brand">
      <div>
        <div class="proposal-kicker">PROPOSAL</div>
        <div class="proposal-rule"></div>
      </div>
      <img src="{logo_uri}" alt="x-change logo">
    </div>
    <h1>{PROPOSAL_TITLE}</h1>
    <p class="program-title">{PROGRAM_TITLE}</p>
    <p class="institution">{INSTITUTION}</p>
    <p class="submitted-by">Submitted by {SUBMITTED_BY}</p>
    <div class="administration table-wrap">
      <table aria-label="Proposal information">
        <tbody>
          <tr><th>Proposal Number</th><td>{PROPOSAL_NUMBER}</td><th>Proposal Date</th><td>{PROPOSAL_DATE}</td></tr>
          <tr><th>Proposal Revision</th><td>{REVISION}</td><th>Valid Until</th><td>{VALID_UNTIL}</td></tr>
          <tr><th>Status</th><td>{STATUS}</td><th>Submitted To</th><td>{INSTITUTION}</td></tr>
          <tr><th>Classification</th><td colspan="3">{CONFIDENTIALITY}</td></tr>
        </tbody>
      </table>
    </div>
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
        f"urn:odti:{PROPOSAL_NUMBER.lower()}:{REVISION}:{profile}",
    ]
    if profile == "publication":
        command.extend(("--pdf-version", "1.7", "--full-fonts", "--hinting"))
    elif profile == "print":
        command.extend(("--pdf-variant", "pdf/a-2u", "--full-fonts", "--hinting"))
    elif profile == "screen":
        command.extend(("--pdf-version", "1.7", "--optimize-images", "--dpi", "150"))
    else:
        raise ValueError(f"Unsupported profile: {profile}")
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    command.extend((str(html_path), str(pdf_path)))
    subprocess.run(command, check=True)


def render_cover(pdf_path: Path, cover_path: Path) -> None:
    executable = shutil.which("pdftoppm")
    if executable is None:
        raise RuntimeError("pdftoppm executable not found on PATH.")
    cover_path.parent.mkdir(parents=True, exist_ok=True)
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
            str(cover_path.with_suffix("")),
        ],
        check=True,
    )


def pdf_record(path: Path, profile: str) -> dict[str, object]:
    reader = PdfReader(path)

    def count_outline(items: list[object]) -> int:
        return sum(
            count_outline(item) if isinstance(item, list) else 1
            for item in items
        )

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


def write_submission_package(
    package_directory: Path,
    proposal_pdf: Path,
) -> list[Path]:
    cover_letter_directory = package_directory / "01-cover-letter"
    proposal_directory = package_directory / "02-commercial-proposal"
    attachment_directory = package_directory / "03-attachment-a"
    for directory in (
        cover_letter_directory,
        proposal_directory,
        attachment_directory,
    ):
        directory.mkdir(parents=True, exist_ok=True)

    package_readme = package_directory / "README.md"
    cover_readme = cover_letter_directory / "README.md"
    package_proposal = (
        proposal_directory
        / "AllBank-Provisional-License-and-Proof-of-Concept.pdf"
    )
    legacy_package_proposal = (
        proposal_directory / "AllBank-Provisional-License-and-POC-Proposal.pdf"
    )
    package_attachment = (
        attachment_directory
        / "Thrift-Bank-Digital-Banking-Program-Guide-AllBank-Edition.pdf"
    )

    if legacy_package_proposal.is_file():
        legacy_package_proposal.unlink()
    shutil.copy2(proposal_pdf, package_proposal)
    shutil.copy2(ATTACHMENT_PDF, package_attachment)
    package_readme.write_text(
        "# AllBank submission package\n\n"
        f"Proposal: {PROPOSAL_NUMBER}, Revision {REVISION}\n\n"
        f"Proposal Date: {PROPOSAL_DATE}\n\n"
        f"Valid Until: {VALID_UNTIL}\n\n"
        "The commercial proposal and Attachment A are separate PDF records. "
        "The cover letter remains pending and is not included as a PDF.\n",
        encoding="utf-8",
    )
    cover_readme.write_text(
        "# Cover letter placeholder\n\n"
        "The separate cover letter remains pending. No draft or blank PDF has been created.\n",
        encoding="utf-8",
    )
    return [package_readme, cover_readme, package_proposal, package_attachment]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Publish ODTI Proposal ODTI-2026-001 for AllBank."
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
            / "proposal"
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
            "Canonical proposal source hash mismatch. Refusing publication: "
            f"{source_hash_before}"
        )
    if sha256(ATTACHMENT_SOURCE) != EXPECTED_ATTACHMENT_SOURCE_SHA256:
        raise ValueError("Frozen AllBank Program Guide source hash mismatch.")
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
    cover_path = output_directory / f"{OUTPUT_STEM}-cover.png"
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
    render_cover(publication_pdf, cover_path)

    package_records = write_submission_package(package_directory, publication_pdf)
    source_hash_after = sha256(source)
    if source_hash_after != source_hash_before:
        raise RuntimeError("Canonical proposal source changed during publication.")
    if sha256(ATTACHMENT_SOURCE) != EXPECTED_ATTACHMENT_SOURCE_SHA256:
        raise RuntimeError("Frozen AllBank Program Guide source changed during publication.")

    pdfs = [
        pdf_record(publication_pdf, "publication"),
        pdf_record(print_pdf, "print_pdfa_2u"),
        pdf_record(screen_pdf, "screen_optimized"),
    ]
    package = [
        {
            "path": str(path.relative_to(REPOSITORY_ROOT)),
            "sha256": sha256(path),
            "bytes": path.stat().st_size,
        }
        for path in package_records
    ]
    manifest = {
        "title": PROPOSAL_TITLE,
        "program": PROGRAM_TITLE,
        "institution": INSTITUTION,
        "proposal_number": PROPOSAL_NUMBER,
        "proposal_revision": REVISION,
        "status": STATUS,
        "submitted_by": SUBMITTED_BY,
        "proposal_date": PROPOSAL_DATE_ISO,
        "valid_until": VALID_UNTIL_ISO,
        "validity_days": 30,
        "confidentiality": CONFIDENTIALITY,
        "canonical_source": canonical_source,
        "canonical_source_sha256": source_hash_after,
        "renderer": "WeasyPrint 66.0",
        "html": {
            "path": str(html_path.relative_to(REPOSITORY_ROOT)),
            "sha256": sha256(html_path),
            "bytes": html_path.stat().st_size,
        },
        "cover": {
            "path": str(cover_path.relative_to(REPOSITORY_ROOT)),
            "sha256": sha256(cover_path),
            "bytes": cover_path.stat().st_size,
        },
        "pdfs": pdfs,
        "attachment": {
            "canonical_source_sha256": EXPECTED_ATTACHMENT_SOURCE_SHA256,
            "publication_pdf_sha256": EXPECTED_ATTACHMENT_PDF_SHA256,
            "copied_byte_for_byte": True,
        },
        "submission_package": package,
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

    checksum_records = [source, html_path, cover_path, publication_pdf, print_pdf, screen_pdf]
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
        f"- Proposal: {PROPOSAL_NUMBER}, Revision {REVISION}\n"
        f"- Proposal Date: {PROPOSAL_DATE}\n"
        f"- Valid Until: {VALID_UNTIL}\n"
        f"- Canonical source SHA-256: `{source_hash_after}`\n"
        f"- AllBank Program Guide source SHA-256: `{EXPECTED_ATTACHMENT_SOURCE_SHA256}`\n"
        f"- AllBank Program Guide PDF SHA-256: `{EXPECTED_ATTACHMENT_PDF_SHA256}`\n"
        f"- Publication pages: {pdfs[0]['physical_pages']}\n"
        "- Automated source, sequence, date, identity, attachment, and PDF-generation checks: Passed\n"
        "- Page-by-page visual inspection: Pending\n",
        encoding="utf-8",
    )

    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
