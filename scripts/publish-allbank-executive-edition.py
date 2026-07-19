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
from pathlib import Path

from pypdf import PdfReader


DOCUMENT_TITLE = "Thrift Bank Digital Banking Program Guide"
INSTITUTION_EDITION = "AllBank Edition"
PUBLICATION_EDITION = "Executive Edition"
PRINTING = "First Edition"
VERSION = "1.0"
STATUS = "Approved"
EDITORIAL_STATE = "Frozen"
PUBLICATION_DATE = "July 2026"
DOCUMENT_FORM = "x-change Banking Program Guide"
INSTITUTION = "AllBank (A Thrift Bank), Inc."
EXPECTED_MANUSCRIPT_SHA256 = (
    "f0bca701d7bcc817d21c42ce032bd0ef853dc76be99d6517d1d36282b07bd9e2"
)

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
BASE_PUBLISHER_PATH = REPOSITORY_ROOT / "scripts" / "publish-rbap-program-guide.py"
STYLESHEET_PATH = (
    REPOSITORY_ROOT
    / "resources"
    / "publication-assets"
    / "styles"
    / "program-guide.css"
)
LOGO_PATH = (
    REPOSITORY_ROOT
    / "resources"
    / "publication-assets"
    / "brand"
    / "x-change-logo-orange.png"
)

OUTPUT_STEM = (
    "thrift-bank-digital-banking-program-guide-allbank-edition-"
    "executive-first-edition-v1.0"
)


def load_base_publisher():
    spec = importlib.util.spec_from_file_location(
        "rbap_program_guide_publisher", BASE_PUBLISHER_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(
            f"Unable to load base Program Guide publisher: {BASE_PUBLISHER_PATH}"
        )
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


def render_inline(value: str) -> str:
    escaped = html.escape(value, quote=False)
    escaped = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", escaped)
    escaped = re.sub(r"`([^`]+)`", r'<code class="inline-code">\1</code>', escaped)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    return re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", escaped)


BASE.render_inline = render_inline
BASE.PULL_QUOTES = {
    "The bank brings the authority and the rails. x-change brings the operating grammar. The bank-specific driver connects them.",
    "The customer requested a banking outcome. The bank arranged it.",
}


def publication_scope(markdown: str) -> str:
    required_identity = (
        "# Thrift Bank Digital Banking Program Guide",
        "## AllBank Edition",
        "### Executive Edition",
        "Version 1.0",
    )
    title_block = markdown.split("## Foreword", maxsplit=1)[0]
    for value in required_identity:
        if value not in title_block:
            raise ValueError(f"The frozen manuscript identity is incomplete: {value}")

    start_marker = "## Foreword"
    if start_marker not in markdown:
        raise ValueError("Foreword heading not found in frozen manuscript.")
    scope = f"{start_marker}\n{markdown.split(start_marker, maxsplit=1)[1].strip()}"

    headings = re.findall(r"^## (.+)$", scope, flags=re.MULTILINE)
    expected = (
        ["Foreword", "Executive Summary"]
        + [f"Section {index}" for index in range(1, 8)]
        + ["Annexes"]
        + [f"Annex {letter}" for letter in "ABCDEFGH"]
    )
    if len(headings) != len(expected):
        raise ValueError(
            f"Expected {len(expected)} major publication sections; found {len(headings)}."
        )
    for expected_prefix, heading in zip(expected, headings, strict=True):
        if not heading.startswith(expected_prefix):
            raise ValueError(
                f"Unexpected publication sequence: expected {expected_prefix!r}, "
                f"found {heading!r}."
            )
    return scope


def major_section(label: str, anchor: str) -> tuple[str, str | None, str | None]:
    section_match = re.fullmatch(r"Section (\d+) — (.+)", label)
    annex_match = re.fullmatch(r"Annex ([A-H]) — (.+)", label)

    if section_match:
        number, title = section_match.groups()
        running = f"SECTION {number} · {title.upper()}"
        opening = (
            f'<section class="major-section" id="{anchor}">'
            f'<div class="section-number">Section {number}</div>'
            f'<h2 data-running="{html.escape(running, quote=True)}">'
            f"{render_inline(title)}</h2>"
        )
        return opening, number, title

    if annex_match:
        letter, title = annex_match.groups()
        running = f"ANNEX {letter} · {title.upper()}"
        opening = (
            f'<section class="major-section annex-section" id="{anchor}">'
            f'<div class="section-number">Annex {letter}</div>'
            f'<h2 data-running="{html.escape(running, quote=True)}">'
            f"{render_inline(title)}</h2>"
        )
        return opening, letter, title

    if label == "Foreword":
        return (
            f'<section class="major-section foreword-section" id="{anchor}">'
            '<div class="section-number">AllBank Edition</div>'
            '<h2 data-running="FOREWORD">Foreword</h2>',
            "F",
            "Foreword",
        )

    if label == "Executive Summary":
        return (
            f'<section class="major-section executive-summary" id="{anchor}">'
            '<div class="section-number">Board briefing</div>'
            '<h2 data-running="EXECUTIVE SUMMARY">Executive Summary</h2>',
            "ES",
            "Executive Summary",
        )

    if label == "Annexes":
        return (
            f'<section class="major-section annexes-overview" id="{anchor}">'
            '<div class="section-number">Institutional reference</div>'
            '<h2 data-running="ANNEXES">Annexes</h2>',
            None,
            None,
        )

    raise ValueError(f"Unsupported major publication heading: {label}")


def render_manuscript(markdown: str) -> tuple[str, list[tuple[str, str, str]]]:
    lines = publication_scope(markdown).splitlines()
    rendered: list[str] = []
    contents: list[tuple[str, str, str]] = []
    used_ids: set[str] = set()
    section_open = False
    opening_paragraph_pending = False
    current_section = ""
    index = 0

    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue

        heading = re.match(r"^(#{2,4})\s+(.+)$", line)
        if heading:
            level = len(heading.group(1))
            label = heading.group(2).strip()
            anchor = BASE.slugify(label)
            suffix = 2
            while anchor in used_ids:
                anchor = f"{BASE.slugify(label)}-{suffix}"
                suffix += 1
            used_ids.add(anchor)

            if level == 2:
                if section_open:
                    rendered.append("</section>")
                section_open = True
                current_section = label
                opening_paragraph_pending = label in {"Foreword", "Executive Summary"}
                opening, marker, title = major_section(label, anchor)
                rendered.append(opening)
                if marker is not None and title is not None:
                    contents.append((marker, title, anchor))
            else:
                rendered.append(
                    f'<h{level} id="{anchor}" class="subheading">'
                    f"{render_inline(label)}</h{level}>"
                )
            index += 1
            continue

        if line.startswith(">"):
            block, index = BASE.render_quote(lines, index)
            rendered.append(block)
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
            rendered.append(f'<ul class="editorial-list">{"".join(items)}</ul>')
            continue

        if re.match(r"^\d+\. ", line):
            items: list[str] = []
            while index < len(lines) and re.match(r"^\d+\. ", lines[index]):
                value = re.sub(r"^\d+\.\s+", "", lines[index])
                items.append(f"<li>{render_inline(value)}</li>")
                index += 1
            rendered.append(f'<ol class="editorial-list">{"".join(items)}</ol>')
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
            rendered.append(f'<pre class="standalone-code">{code}</pre>')
            continue

        paragraph_lines = [line]
        index += 1
        while index < len(lines) and lines[index].strip():
            next_line = lines[index]
            if (
                re.match(r"^#{2,4}\s+", next_line)
                or next_line.startswith(">")
                or next_line.startswith("- ")
                or re.match(r"^\d+\. ", next_line)
                or next_line.lstrip().startswith("|")
                or next_line.startswith("```")
            ):
                break
            paragraph_lines.append(next_line)
            index += 1

        paragraph = " ".join(part.strip() for part in paragraph_lines)
        rendered.append(BASE.render_paragraph(paragraph, opening_paragraph_pending))
        opening_paragraph_pending = False

    if section_open:
        rendered.append("</section>")
    if current_section != "Annex H — Applying This Program Guide to AllBank":
        raise ValueError(f"Publication ended at unexpected section: {current_section}")
    if len(contents) != 17:
        raise ValueError(f"Expected 17 linked contents entries; found {len(contents)}.")
    return "\n".join(rendered), contents


def render_contents(contents: list[tuple[str, str, str]]) -> str:
    items: list[str] = []
    annex_started = False
    for marker, title, anchor in contents:
        if marker == "A" and not annex_started:
            annex_started = True
            items.append('<li class="toc-group-label">Annexes</li>')
        display = (
            f'<span class="toc-number">{html.escape(marker)}</span>'
            f'<span class="toc-title">{html.escape(title)}</span>'
        )
        items.append(f'<li><a href="#{anchor}">{display}</a></li>')
    return "\n".join(items)


def publication_html(markdown: str, canonical_source: str) -> str:
    for path in (STYLESHEET_PATH, LOGO_PATH):
        if not path.is_file():
            raise FileNotFoundError(f"Required publication asset not found: {path}")

    manuscript, contents = render_manuscript(markdown)
    stylesheet = STYLESHEET_PATH.read_text(encoding="utf-8")
    toc = render_contents(contents)
    logo_data = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    logo_uri = f"data:image/png;base64,{logo_data}"
    footer = "ALLBANK EDITION · EXECUTIVE EDITION · VERSION 1.0"

    overrides = f"""
@page version {{ @bottom-left {{ content: "{footer}"; }} }}
@page contents {{ @bottom-left {{ content: "{footer}"; }} }}
@page body {{ @bottom-left {{ content: "{footer}"; }} }}
.cover-page h1 {{ max-width: 152mm; font-size: 30pt; }}
.cover-subtitle {{
  max-width: 142mm;
  margin-top: 10mm;
  color: var(--ink);
  font-size: 18pt;
  font-style: normal;
  font-weight: 600;
  line-height: 1.2;
}}
.cover-edition {{ line-height: 1.55; }}
.manuscript {{ font-size: 9.65pt; line-height: 1.48; }}
.foreword-section h2,
.annex-section h2 {{ max-width: 151mm; }}
.annexes-overview .editorial-list {{
  margin-top: 8mm;
  columns: 2;
  column-gap: 13mm;
}}
.annexes-overview .editorial-list li {{ break-inside: avoid; margin-bottom: 2.3mm; }}
.toc a {{ padding: 3.05mm 0; }}
.toc-title {{ font-size: 9.75pt; }}
.toc-group-label {{
  padding: 4.5mm 0 2.2mm;
  border-top: 0.7pt solid var(--accent) !important;
  color: var(--accent);
  font-family: "Avenir Next", Avenir, sans-serif;
  font-size: 6.8pt;
  font-weight: 600;
  letter-spacing: 0.13em;
  text-transform: uppercase;
}}
.inline-code {{
  padding: 0.05em 0.24em;
  border-radius: 2px;
  background: var(--accent-soft);
  color: var(--ink);
  font-family: "SFMono-Regular", Consolas, monospace;
  font-size: 0.84em;
}}
.standalone-code {{
  width: 100%;
  margin: 5mm 0 7mm;
  padding: 4mm 6mm;
  border-left: 1.2pt solid var(--accent);
  background: var(--panel);
  color: #293847;
  font-family: Menlo, Monaco, "Courier New", monospace;
  font-size: 7.35pt;
  line-height: 1.3;
  text-align: center;
  white-space: pre-wrap;
  break-inside: avoid;
}}
#section-7-launching-the-program h2 {{ margin-bottom: 8mm; }}
#section-7-launching-the-program .executive-callout {{
  margin-bottom: 2.5mm;
  padding-top: 3mm;
  padding-bottom: 3mm;
}}
#section-7-launching-the-program .executive-decision {{ margin-bottom: 6mm; }}
#annex-a-canonical-operating-model h2 {{ margin-bottom: 8mm; }}
#annex-a-canonical-operating-model .standalone-code {{
  margin-top: 3mm;
  margin-bottom: 5mm;
  padding-top: 3mm;
  padding-bottom: 3mm;
  line-height: 1.24;
}}
#annex-g-glossary h2 {{ margin-bottom: 7mm; }}
#annex-g-glossary p {{ margin-bottom: 0.34em; }}
.table-wrap {{ break-inside: auto; }}
.annex-section table {{ font-size: 7.45pt; line-height: 1.3; }}
.annex-section th {{ padding: 2.5mm 2.7mm; }}
.annex-section td {{ padding: 2.25mm 2.7mm; }}
"""

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="x-change">
  <meta name="description" content="Canonical client-facing AllBank Executive Edition of the Thrift Bank Digital Banking Program Guide">
  <meta name="document-type" content="Banking Program Guide">
  <meta name="institution-edition" content="{INSTITUTION_EDITION}">
  <meta name="edition" content="{PUBLICATION_EDITION}">
  <meta name="publication" content="{PRINTING}">
  <meta name="version" content="{VERSION}">
  <meta name="status" content="{STATUS}">
  <meta name="editorial-state" content="{EDITORIAL_STATE}">
  <meta name="canonical-source" content="{html.escape(canonical_source, quote=True)}">
  <title>{DOCUMENT_TITLE} — {INSTITUTION_EDITION} — {PUBLICATION_EDITION}</title>
  <style>
{stylesheet}
{overrides}
  </style>
</head>
<body>
  <section class="cover-page" aria-label="Cover">
    <div class="cover-frame">
      <div class="cover-kicker">{DOCUMENT_FORM}</div>
      <div class="cover-rule"></div>
      <h1>{DOCUMENT_TITLE}</h1>
      <p class="cover-subtitle">{INSTITUTION_EDITION}</p>
      <div class="cover-edition">{PUBLICATION_EDITION}<br>{PRINTING} · Version {VERSION}</div>
      <div class="cover-recipient">
        <span>Prepared for</span>
        <strong>{INSTITUTION}</strong>
      </div>
      <div class="cover-imprint">
        <img src="{logo_uri}" alt="x-change logo">
        <span>x-change</span>
      </div>
    </div>
  </section>

  <section class="version-page" aria-label="Copyright and publication information">
    <div class="version-kicker">Publication record</div>
    <h1>{DOCUMENT_TITLE}</h1>
    <p class="version-subtitle">{INSTITUTION_EDITION} · {PUBLICATION_EDITION}</p>

    <dl class="publication-record">
      <div><dt>Institution edition</dt><dd>{INSTITUTION_EDITION}</dd></div>
      <div><dt>Publication</dt><dd>{PUBLICATION_EDITION}</dd></div>
      <div><dt>Printing</dt><dd>{PRINTING}</dd></div>
      <div><dt>Version</dt><dd>{VERSION}</dd></div>
      <div><dt>Status</dt><dd>{STATUS}</dd></div>
      <div><dt>Publication date</dt><dd>{PUBLICATION_DATE}</dd></div>
      <div><dt>Prepared for</dt><dd>{INSTITUTION}</dd></div>
      <div><dt>Prepared by</dt><dd>x-change</dd></div>
      <div><dt>Edition scope</dt><dd>Foreword, Executive Summary, Sections 1–7, and Annexes A–H</dd></div>
      <div><dt>Canonical source</dt><dd>{html.escape(canonical_source)}</dd></div>
    </dl>

    <div class="copyright-note">
      <p>Copyright © 2026 x-change.</p>
      <p>This manuscript is the frozen canonical First Edition. Subsequent wording corrections are governed as errata or future editions.</p>
    </div>
  </section>

  <nav class="contents-page" aria-label="Table of contents">
    <div class="front-kicker">{INSTITUTION_EDITION} · {PUBLICATION_EDITION}</div>
    <h1>Contents</h1>
    <ol class="toc">
{toc}
    </ol>
  </nav>

  <main class="manuscript">
{manuscript}
  </main>
</body>
</html>
"""


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
        f"urn:sha256:{EXPECTED_MANUSCRIPT_SHA256}:{profile}",
    ]
    if profile == "publication":
        command.extend(("--pdf-version", "1.7", "--full-fonts", "--hinting"))
    elif profile == "print":
        command.extend(
            ("--pdf-variant", "pdf/a-2u", "--full-fonts", "--hinting")
        )
    elif profile == "screen":
        command.extend(("--pdf-version", "1.7", "--optimize-images", "--dpi", "150"))
    else:
        raise ValueError(f"Unsupported PDF profile: {profile}")

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
    return {
        "profile": profile,
        "path": str(path.relative_to(REPOSITORY_ROOT)),
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
        "physical_pages": len(reader.pages),
        "bookmarks": len(reader.outline),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Publish the frozen AllBank Executive Edition First Edition."
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
            / "executive-edition"
            / "first-edition"
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
    if source_hash_before != EXPECTED_MANUSCRIPT_SHA256:
        raise ValueError(
            "Frozen manuscript hash mismatch. Refusing to publish an altered source: "
            f"{source_hash_before}"
        )

    markdown = source.read_text(encoding="utf-8")
    canonical_source = str(source.relative_to(REPOSITORY_ROOT))
    rendered = publication_html(markdown, canonical_source)

    output_directory = args.output_directory.resolve()
    pdf_directory = args.pdf_directory.resolve()
    output_directory.mkdir(parents=True, exist_ok=True)
    pdf_directory.mkdir(parents=True, exist_ok=True)

    html_path = output_directory / f"{OUTPUT_STEM}.html"
    cover_path = output_directory / f"{OUTPUT_STEM}-cover.png"
    manifest_path = output_directory / "publication-manifest.json"
    publication_pdf = pdf_directory / f"{OUTPUT_STEM}.pdf"
    print_pdf = pdf_directory / f"{OUTPUT_STEM}-print.pdf"
    screen_pdf = pdf_directory / f"{OUTPUT_STEM}-screen.pdf"

    html_path.write_text(rendered, encoding="utf-8")
    run_weasyprint(html_path, publication_pdf, "publication")
    run_weasyprint(html_path, print_pdf, "print")
    run_weasyprint(html_path, screen_pdf, "screen")
    render_cover(publication_pdf, cover_path)

    source_hash_after = sha256(source)
    if source_hash_after != source_hash_before:
        raise RuntimeError("Frozen manuscript changed during publication.")

    manifest = {
        "title": DOCUMENT_TITLE,
        "institution_edition": INSTITUTION_EDITION,
        "publication": PUBLICATION_EDITION,
        "printing": PRINTING,
        "version": VERSION,
        "status": STATUS,
        "editorial_state": EDITORIAL_STATE,
        "publication_state": "Typesetting",
        "publication_date": PUBLICATION_DATE,
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
        "pdfs": [
            pdf_record(publication_pdf, "publication"),
            pdf_record(print_pdf, "print_pdfa_2u"),
            pdf_record(screen_pdf, "screen_optimized"),
        ],
        "accessibility": {
            "tagged_pdf": True,
            "language": "en",
            "bookmarks": True,
            "linked_table_of_contents": True,
            "logical_html_landmarks": True,
        },
    }
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
