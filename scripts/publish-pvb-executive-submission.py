#!/usr/bin/env python3

from __future__ import annotations

import argparse
import base64
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SOURCE_ROOT = (
    REPOSITORY_ROOT
    / "docs"
    / "institutions"
    / "philippine-veterans-bank"
    / "executive-submission"
)
DEFAULT_OUTPUT_ROOT = (
    REPOSITORY_ROOT
    / "build"
    / "institutions"
    / "philippine-veterans-bank"
    / "executive-submission"
    / "review-proof"
)
LOGO_PATH = (
    REPOSITORY_ROOT
    / "resources"
    / "publication-assets"
    / "brand"
    / "x-change-logo-orange.png"
)

PROGRAM_TITLE = "Philippine Veterans Bank Modernization Program"
VERSION = "0.9"
STATUS = "Executive Review Proof"
PUBLICATION_DATE = "20 July 2026"
CANONICAL_PARENT = SOURCE_ROOT.parent / "PHILIPPINE_VETERANS_BANK_MODERNIZATION_PROGRAM.md"


@dataclass(frozen=True)
class Publication:
    key: str
    source_name: str
    title: str
    output_stem: str
    document_type: str


PUBLICATIONS = (
    Publication(
        key="board-paper",
        source_name="BOARD_PAPER.md",
        title="Board Paper — Authority for Management Validation",
        output_stem="pvb-board-paper-v0.9-review-proof",
        document_type="Board Paper",
    ),
    Publication(
        key="executive-summary",
        source_name="EXECUTIVE_SUMMARY.md",
        title="Executive Summary",
        output_stem="pvb-executive-summary-v0.9-review-proof",
        document_type="Executive Summary",
    ),
    Publication(
        key="decision-memo",
        source_name="ONE_PAGE_DECISION_MEMO.md",
        title="One-Page Decision Memo",
        output_stem="pvb-one-page-decision-memo-v0.9-review-proof",
        document_type="Decision Memo",
    ),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def slugify(value: str) -> str:
    value = value.replace("—", "-")
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def render_inline(value: str) -> str:
    escaped = html.escape(value, quote=False)
    escaped = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda match: (
            f'<a href="{html.escape(match.group(2), quote=True)}">'
            f"{match.group(1)}</a>"
        ),
        escaped,
    )
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    return re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", escaped)


def validate_source(publication: Publication, markdown: str) -> None:
    required = (
        f"# {PROGRAM_TITLE}",
        f"## {publication.title}",
        "**Audience:**",
        "**Derivative status:** Executive publication derived from the canonical Program",
        "**Canonical parent:** [Philippine Veterans Bank Modernization Program]",
    )
    for value in required:
        if value not in markdown:
            raise ValueError(f"{publication.source_name} is missing: {value}")

    forbidden_statuses = (
        "Version 1.0",
        "First Edition",
        "Board Approved",
        "Publication Freeze",
    )
    for value in forbidden_statuses:
        if value in markdown:
            raise ValueError(
                f"{publication.source_name} contains prohibited proof status: {value}"
            )

    if publication.key == "board-paper":
        required_resolution_language = (
            "illustrative wording is provided solely as a decision aid",
            "legal counsel",
            "Corporate Secretary",
            "established Board procedures",
        )
        for value in required_resolution_language:
            if value not in markdown:
                raise ValueError(f"Board resolution boundary is missing: {value}")


def split_source(
    publication: Publication, markdown: str
) -> tuple[list[tuple[str, str]], list[str]]:
    lines = markdown.splitlines()
    if lines[0] != f"# {PROGRAM_TITLE}" or lines[2] != f"## {publication.title}":
        raise ValueError(f"Unexpected title hierarchy in {publication.source_name}.")

    metadata: list[tuple[str, str]] = []
    body_start = 3
    index = 3
    while index < len(lines):
        line = lines[index].strip()
        if not line:
            index += 1
            continue
        match = re.fullmatch(r"\*\*([^*]+):\*\*\s*(.+)", line)
        if not match:
            body_start = index
            break
        metadata.append((match.group(1), match.group(2)))
        index += 1

    if not metadata:
        raise ValueError(f"Publication metadata not found in {publication.source_name}.")
    return metadata, lines[body_start:]


def render_body(lines: list[str]) -> str:
    rendered: list[str] = []
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
            rendered.append(
                f'<h{level} id="{anchor}">{render_inline(label)}</h{level}>'
            )
            index += 1
            continue

        if line.startswith(">"):
            quote_lines: list[str] = []
            while index < len(lines) and lines[index].startswith(">"):
                quote_lines.append(lines[index][1:].strip())
                index += 1
            rendered.append(
                '<blockquote><p>'
                + render_inline(" ".join(quote_lines))
                + "</p></blockquote>"
            )
            continue

        if line.startswith("- "):
            items: list[str] = []
            while index < len(lines) and lines[index].startswith("- "):
                items.append(f"<li>{render_inline(lines[index][2:])}</li>")
                index += 1
            rendered.append(f'<ul class="editorial-list">{"".join(items)}</ul>')
            continue

        if re.match(r"^\d+\. ", line):
            items = []
            while index < len(lines) and re.match(r"^\d+\. ", lines[index]):
                value = re.sub(r"^\d+\.\s+", "", lines[index])
                items.append(f"<li>{render_inline(value)}</li>")
                index += 1
            rendered.append(f'<ol class="editorial-list">{"".join(items)}</ol>')
            continue

        paragraph_lines = [line]
        index += 1
        while index < len(lines) and lines[index].strip():
            next_line = lines[index]
            if (
                re.match(r"^#{2,3}\s+", next_line)
                or next_line.startswith(">")
                or next_line.startswith("- ")
                or re.match(r"^\d+\. ", next_line)
            ):
                break
            paragraph_lines.append(next_line)
            index += 1
        paragraph = " ".join(part.strip() for part in paragraph_lines)
        classes = []
        if paragraph in {
            "The accepted institutional response is the **Philippine Veterans Bank Modernization Program**.",
            "The immediate decision is deliberately limited.",
        }:
            classes.append("editorial-anchor")
        class_attribute = f' class="{" ".join(classes)}"' if classes else ""
        rendered.append(f"<p{class_attribute}>{render_inline(paragraph)}</p>")

    return "\n".join(rendered)


def render_memo_body(lines: list[str]) -> str:
    sections: list[list[str]] = []
    current: list[str] = []
    for line in lines:
        if line.startswith("### ") and current:
            sections.append(current)
            current = []
        current.append(line)
    if current:
        sections.append(current)
    if len(sections) != 6:
        raise ValueError(
            f"Expected six Decision Memo sections; found {len(sections)}."
        )

    columns = []
    for section_group in (sections[:3], sections[3:]):
        rendered_sections = "\n".join(
            f'<section class="memo-section">{render_body(section)}</section>'
            for section in section_group
        )
        columns.append(f'<div class="memo-column">{rendered_sections}</div>')
    return "\n".join(columns)


def stylesheet(publication: Publication) -> str:
    footer_title = {
        "board-paper": "PVB BOARD PAPER",
        "executive-summary": "PVB EXECUTIVE SUMMARY",
        "decision-memo": "PVB DECISION MEMO",
    }[publication.key]
    return f"""
:root {{
  --ink: #17283b;
  --text: #272b30;
  --accent: #947553;
  --accent-soft: #f2eee7;
  --muted: #697077;
  --rule: #d8d2c8;
  --paper: #fffefa;
  --panel: #f7f5f0;
}}

@page {{
  size: A4;
  margin: 18mm 21mm 19mm;
  @top-left {{
    content: "PHILIPPINE VETERANS BANK MODERNIZATION PROGRAM";
    color: var(--muted);
    font-family: "Avenir Next", Avenir, sans-serif;
    font-size: 5.9pt;
    letter-spacing: 0.075em;
  }}
  @top-right {{
    content: "VERSION {VERSION} · EXECUTIVE REVIEW PROOF";
    color: var(--accent);
    font-family: "Avenir Next", Avenir, sans-serif;
    font-size: 5.9pt;
    letter-spacing: 0.065em;
  }}
  @bottom-left {{
    content: "{footer_title} · DERIVATIVE PUBLICATION";
    color: var(--muted);
    font-family: "Avenir Next", Avenir, sans-serif;
    font-size: 5.8pt;
    letter-spacing: 0.065em;
  }}
  @bottom-right {{
    content: counter(page) " / " counter(pages);
    color: var(--muted);
    font-family: "Avenir Next", Avenir, sans-serif;
    font-size: 6.4pt;
  }}
}}

@page :first {{
  margin-top: 14mm;
  @top-left {{ content: none; }}
  @top-right {{ content: none; }}
}}

* {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; background: var(--paper); color: var(--text); }}
body {{
  font-family: Charter, Baskerville, Georgia, serif;
  font-size: 9.35pt;
  line-height: 1.43;
}}
a {{ color: inherit; text-decoration: none; }}
p {{ margin: 0 0 3.2mm; orphans: 3; widows: 3; }}
strong {{ color: var(--ink); font-weight: 700; }}

.publication-masthead {{
  padding-bottom: 6mm;
  border-bottom: 0.55pt solid var(--rule-dark, #b9b0a3);
}}
.proof-line {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: var(--accent);
  font-family: "Avenir Next", Avenir, sans-serif;
  font-size: 6.6pt;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}}
.xchange-lockup {{
  display: inline-flex;
  flex: 0 0 auto;
  flex-wrap: nowrap;
  align-items: center;
  gap: 2mm;
  min-width: 21mm;
  color: var(--ink);
  font-variant: normal;
  font-variant-caps: normal;
  letter-spacing: 0.015em;
  text-transform: none;
  white-space: nowrap;
}}
.xchange-lockup img {{ flex: 0 0 auto; width: 3.5mm; height: auto; }}
.xchange-wordmark {{
  display: inline-block;
  flex: 0 0 auto;
  font-variant: normal;
  font-variant-caps: normal;
  text-transform: none;
  white-space: nowrap;
}}
.program-title {{
  margin: 8mm 0 0;
  color: var(--muted);
  font-family: "Avenir Next", Avenir, sans-serif;
  font-size: 7.2pt;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}}
.artifact-title {{
  margin: 2.8mm 0 0;
  color: var(--ink);
  font-size: 25pt;
  font-weight: 600;
  letter-spacing: -0.022em;
  line-height: 1.06;
  bookmark-level: none;
}}
.publication-meta {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  column-gap: 10mm;
  margin: 5mm 0 0;
  font-family: "Avenir Next", Avenir, sans-serif;
  font-size: 6.8pt;
  line-height: 1.35;
}}
.publication-meta div {{ padding: 1.3mm 0; border-top: 0.35pt solid var(--rule); }}
.publication-meta dt {{ display: inline; color: var(--muted); font-weight: 500; }}
.publication-meta dd {{ display: inline; margin: 0 0 0 1.5mm; color: var(--ink); }}
.source-record {{
  margin-top: 2.2mm;
  color: var(--muted);
  font-family: "Avenir Next", Avenir, sans-serif;
  font-size: 5.45pt;
  letter-spacing: 0.012em;
  overflow-wrap: anywhere;
}}
.manuscript {{ margin-top: 7mm; text-align: justify; hyphens: auto; }}
h2, h3 {{ break-after: avoid; color: var(--ink); }}
h2 {{
  margin: 8mm 0 3.2mm;
  padding-top: 3mm;
  border-top: 0.55pt solid var(--rule);
  font-family: "Avenir Next", Avenir, sans-serif;
  font-size: 11pt;
  font-weight: 600;
  letter-spacing: -0.005em;
  line-height: 1.2;
}}
h2::first-letter {{ color: var(--accent); }}
h3 {{
  margin: 5.2mm 0 2.2mm;
  font-family: "Avenir Next", Avenir, sans-serif;
  font-size: 9.1pt;
  font-weight: 600;
  line-height: 1.2;
}}
.editorial-list {{ margin: 1.5mm 0 4mm; padding-left: 5.5mm; }}
.editorial-list li {{ margin: 0 0 1.2mm; padding-left: 1mm; break-inside: avoid; }}
.editorial-list li::marker {{ color: var(--accent); font-family: "Avenir Next", Avenir, sans-serif; font-weight: 600; }}
blockquote {{
  margin: 4mm 0 3mm;
  padding: 4.5mm 5.5mm;
  border-left: 1.4pt solid var(--accent);
  background: var(--panel);
  break-inside: avoid;
}}
blockquote p {{ margin: 0; color: var(--ink); font-size: 9.15pt; line-height: 1.42; }}
blockquote + p {{ color: var(--muted); font-size: 8.05pt; line-height: 1.38; }}
.editorial-anchor {{
  margin: 5mm 0;
  color: var(--ink);
  font-size: 10.15pt;
  line-height: 1.38;
}}

.artifact-executive-summary {{ font-size: 9.55pt; line-height: 1.47; }}
.artifact-board-paper .artifact-title,
.artifact-executive-summary .artifact-title {{ bookmark-level: 1; }}
.artifact-board-paper h2 {{ bookmark-level: 2; }}
.artifact-executive-summary .artifact-title {{ font-size: 27pt; }}
.artifact-executive-summary .manuscript {{ max-width: 158mm; margin-top: 8mm; }}
.artifact-executive-summary p {{ margin-bottom: 3.7mm; }}
.artifact-executive-summary ol {{
  margin: 4mm 0 5mm;
  padding: 4mm 6mm 3mm 10mm;
  border-top: 0.55pt solid var(--rule);
  border-bottom: 0.55pt solid var(--rule);
  background: var(--panel);
}}

.artifact-decision-memo {{ font-size: 9.15pt; line-height: 1.32; }}
.artifact-decision-memo .publication-masthead {{ padding-bottom: 3.4mm; }}
.artifact-decision-memo .proof-line {{ font-size: 6.05pt; }}
.artifact-decision-memo .program-title {{ margin-top: 4.4mm; font-size: 6.55pt; }}
.artifact-decision-memo .artifact-title {{ margin-top: 1.8mm; font-size: 20.5pt; }}
.artifact-decision-memo .publication-meta {{
  grid-template-columns: 1fr 1fr;
  column-gap: 8mm;
  margin-top: 3.2mm;
  font-size: 5.85pt;
}}
.artifact-decision-memo .publication-meta div {{ padding: 0.7mm 0; }}
.artifact-decision-memo .source-record {{ margin-top: 1mm; font-size: 4.8pt; }}
.artifact-decision-memo .manuscript {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  column-gap: 8mm;
  margin-top: 4.2mm;
  text-align: left;
}}
.artifact-decision-memo .memo-column {{ min-width: 0; }}
.artifact-decision-memo .memo-section {{ break-inside: avoid; }}
.artifact-decision-memo h3 {{
  margin: 3.3mm 0 1.4mm;
  padding-top: 2mm;
  border-top: 0.45pt solid var(--rule);
  font-size: 8.2pt;
  letter-spacing: 0.02em;
  text-transform: uppercase;
}}
.artifact-decision-memo h3:first-child {{ margin-top: 0; }}
.artifact-decision-memo p {{ margin-bottom: 2mm; }}
.artifact-decision-memo .editorial-list {{ margin: 1mm 0 2mm; padding-left: 4.5mm; }}
.artifact-decision-memo .editorial-list li {{ margin-bottom: 0.65mm; padding-left: 0.4mm; }}

@media screen {{
  body {{ max-width: 210mm; margin: 0 auto; padding: 14mm 21mm 19mm; box-shadow: 0 0 16px rgba(23, 40, 59, 0.12); }}
}}
"""


def publication_html(
    publication: Publication,
    markdown: str,
    source: Path,
    source_hash: str,
    output_root: Path,
) -> str:
    metadata, body_lines = split_source(publication, markdown)
    parent_href = Path(os.path.relpath(CANONICAL_PARENT, output_root)).as_posix()
    metadata_rows = []
    for label, value in metadata:
        if label == "Canonical parent":
            value = re.sub(r"\]\([^)]+\)", f"]({parent_href})", value)
        metadata_rows.append(
            f"<div><dt>{html.escape(label)}</dt><dd>{render_inline(value)}</dd></div>"
        )
    metadata_html = "\n".join(metadata_rows)
    logo_data = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    logo_uri = f"data:image/png;base64,{logo_data}"
    source_path = source.relative_to(REPOSITORY_ROOT)
    parent_hash = sha256(CANONICAL_PARENT)
    description = (
        f"{publication.document_type}; Version {VERSION} {STATUS}; "
        "derivative of the Philippine Veterans Bank Modernization Program"
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="x-change">
  <meta name="description" content="{html.escape(description, quote=True)}">
  <meta name="document-type" content="{html.escape(publication.document_type, quote=True)}">
  <meta name="publication-status" content="{STATUS}">
  <meta name="version" content="{VERSION}">
  <meta name="canonical-source" content="{html.escape(str(source_path), quote=True)}">
  <meta name="canonical-source-sha256" content="{source_hash}">
  <title>{html.escape(publication.title)} — Version {VERSION} {STATUS}</title>
  <style>{stylesheet(publication)}</style>
</head>
<body class="artifact-{publication.key}">
  <header class="publication-masthead" id="publication-record">
    <div class="proof-line">
      <span>Version {VERSION} · {STATUS}</span>
      <span class="xchange-lockup" aria-label="x-change"><img src="{logo_uri}" alt=""><span class="xchange-wordmark">x-change</span></span>
    </div>
    <div class="program-title">{PROGRAM_TITLE}</div>
    <h1 class="artifact-title">{html.escape(publication.title)}</h1>
    <dl class="publication-meta">{metadata_html}</dl>
    <div class="source-record">
      Source: {html.escape(str(source_path))} · Source SHA-256: {source_hash}<br>
      Canonical parent SHA-256: {parent_hash} · Publication date: {PUBLICATION_DATE}
    </div>
  </header>
  <main class="manuscript">
{render_memo_body(body_lines) if publication.key == "decision-memo" else render_body(body_lines)}
  </main>
</body>
</html>
"""


def run_weasyprint(html_path: Path, pdf_path: Path) -> None:
    executable = shutil.which("weasyprint")
    if executable is None:
        raise RuntimeError("weasyprint executable not found on PATH.")
    subprocess.run(
        [
            executable,
            "--pdf-version",
            "1.7",
            "--full-fonts",
            "--hinting",
            str(html_path),
            str(pdf_path),
        ],
        check=True,
    )


def count_outline(items: list[object]) -> int:
    return sum(
        count_outline(item) if isinstance(item, list) else 1 for item in items
    )


def font_embedding(reader: PdfReader) -> tuple[bool, list[str]]:
    embedded = True
    names: set[str] = set()
    for page in reader.pages:
        font_dictionary = page["/Resources"].get_object().get("/Font", {})
        if hasattr(font_dictionary, "get_object"):
            font_dictionary = font_dictionary.get_object()
        for reference in font_dictionary.values():
            font = reference.get_object()
            names.add(str(font.get("/BaseFont", "unknown")))
            candidates = []
            if font.get("/DescendantFonts"):
                candidates.extend(
                    descendant.get_object()
                    for descendant in font["/DescendantFonts"]
                )
            else:
                candidates.append(font)
            for candidate in candidates:
                descriptor = candidate.get("/FontDescriptor")
                if not descriptor:
                    embedded = False
                    continue
                descriptor = descriptor.get_object()
                embedded = embedded and any(
                    key in descriptor
                    for key in ("/FontFile", "/FontFile2", "/FontFile3")
                )
    return embedded, sorted(names)


def validate_pdf_text(publication: Publication, reader: PdfReader) -> None:
    extracted = " ".join(page.extract_text() or "" for page in reader.pages)
    normalized = re.sub(r"\s+", " ", extracted)
    shared = (
        "Executive publication derived from the canonical Program",
        "Philippine Veterans Bank Modernization Program",
    )
    publication_specific = {
        "board-paper": (
            "The requested authority is limited to institutional validation",
            "This illustrative wording is provided solely as a decision aid.",
            "Corporate Secretary",
        ),
        "executive-summary": (
            "The accepted institutional response is the Philippine Veterans Bank Modernization Program.",
            "The immediate decision is deliberately limited.",
            "This authorization would begin institutional learning.",
        ),
        "decision-memo": (
            "No implementation. No procurement. No contract.",
            "The first decision authorizes institutional learning.",
            "a separate recommendation for any later step.",
        ),
    }[publication.key]
    for phrase in (*shared, *publication_specific):
        if phrase not in normalized:
            raise RuntimeError(
                f"Rendered PDF text is missing required phrase in {publication.key}: "
                f"{phrase}"
            )


def pdf_record(path: Path) -> dict[str, object]:
    reader = PdfReader(path)
    pages = len(reader.pages)
    page_sizes = []
    annotations = 0
    link_targets = []
    for page in reader.pages:
        width = round(float(page.mediabox.width), 2)
        height = round(float(page.mediabox.height), 2)
        page_sizes.append([width, height])
        for annotation in page.get("/Annots", []):
            annotations += 1
            action = annotation.get_object().get("/A")
            if action and action.get("/URI"):
                link_targets.append(str(action.get("/URI")))
    embedded, font_names = font_embedding(reader)
    return {
        "file": path.name,
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
        "pages": pages,
        "page_sizes_points": page_sizes,
        "bookmarks": count_outline(reader.outline),
        "link_annotations": annotations,
        "link_targets": link_targets,
        "fonts_embedded": embedded,
        "font_names": font_names,
        "metadata": {
            key: str(value) for key, value in (reader.metadata or {}).items()
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Publish PVB Executive Submission Suite review proofs."
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_ROOT)
    args = parser.parse_args()

    if not LOGO_PATH.is_file():
        raise FileNotFoundError(f"Publication logo not found: {LOGO_PATH}")
    if not CANONICAL_PARENT.is_file():
        raise FileNotFoundError(f"Canonical parent not found: {CANONICAL_PARENT}")

    output_root = args.output_dir
    output_root.mkdir(parents=True, exist_ok=True)
    source_hashes_before = {
        publication.source_name: sha256(SOURCE_ROOT / publication.source_name)
        for publication in PUBLICATIONS
    }
    parent_hash_before = sha256(CANONICAL_PARENT)

    artifacts: list[dict[str, object]] = []
    for publication in PUBLICATIONS:
        source = SOURCE_ROOT / publication.source_name
        markdown = source.read_text(encoding="utf-8")
        validate_source(publication, markdown)
        source_hash = source_hashes_before[publication.source_name]

        html_path = output_root / f"{publication.output_stem}.html"
        pdf_path = output_root / f"{publication.output_stem}.pdf"
        html_path.write_text(
            publication_html(
                publication, markdown, source, source_hash, output_root
            ),
            encoding="utf-8",
        )
        run_weasyprint(html_path, pdf_path)

        reader = PdfReader(pdf_path)
        validate_pdf_text(publication, reader)

        record = {
            "key": publication.key,
            "source": str(source.relative_to(REPOSITORY_ROOT)),
            "source_sha256": source_hash,
            "html": {
                "file": html_path.name,
                "sha256": sha256(html_path),
                "bytes": html_path.stat().st_size,
            },
            "pdf": pdf_record(pdf_path),
        }
        if publication.key == "decision-memo" and record["pdf"]["pages"] != 1:
            raise RuntimeError(
                "The One-Page Decision Memo did not render to exactly one page."
            )
        artifacts.append(record)

    for publication in PUBLICATIONS:
        source = SOURCE_ROOT / publication.source_name
        if sha256(source) != source_hashes_before[publication.source_name]:
            raise RuntimeError(f"Canonical source changed during rendering: {source}")
    if sha256(CANONICAL_PARENT) != parent_hash_before:
        raise RuntimeError("Canonical Modernization Program changed during rendering.")

    manifest = {
        "publication_family": "Philippine Veterans Bank Executive Submission Suite",
        "status": STATUS,
        "version": VERSION,
        "publication_date": PUBLICATION_DATE,
        "canonical_parent": {
            "file": str(CANONICAL_PARENT.relative_to(REPOSITORY_ROOT)),
            "sha256": parent_hash_before,
        },
        "artifacts": artifacts,
        "source_files_unchanged": True,
        "presentation_generated": False,
    }
    manifest_path = output_root / "publication-manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    main()
