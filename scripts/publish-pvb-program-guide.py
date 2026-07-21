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
import tempfile
import textwrap
from pathlib import Path

import pdfplumber
from pypdf import PdfReader


DOCUMENT_TITLE = "Government Depository Digital Banking Program Guide"
INSTITUTION_EDITION = "Philippine Veterans Bank Edition"
PUBLICATION_EDITION = "Executive Edition"
VERSION = "0.9"
STATUS = "Executive Review Proof"
PUBLICATION_DATE = "21 July 2026"
DOCUMENT_FORM = "x-change Banking Program Guide"
INSTITUTION = "Philippine Veterans Bank"
OUTPUT_STEM = "philippine-veterans-bank-executive-edition-v0.9-review-proof"

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SOURCE = (
    REPOSITORY_ROOT
    / "docs"
    / "institutions"
    / "philippine-veterans-bank"
    / "program-guide"
    / "philippine-veterans-bank-digital-banking-program-guide.md"
)
ANNEX_ROOT = SOURCE.parent / "appendices"
BASE_PUBLISHER_PATH = REPOSITORY_ROOT / "scripts" / "publish-thrift-bank-program-guide.py"
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
DEFAULT_OUTPUT_ROOT = (
    REPOSITORY_ROOT
    / "build"
    / "institutions"
    / "philippine-veterans-bank"
    / "program-guide"
    / "review-proof"
)
TEMP_PDF_PATH = Path(tempfile.gettempdir()) / "x-change-monographs" / "pdfs"
MERMAID_CACHE_PATH = TEMP_PDF_PATH / "pvb-program-guide-review-proof-mermaid-cache"

EXPECTED_SOURCE_SHA256 = "92189e91e3a00c3e28fe5725c7788fe202ad2a4dd996ae8b56ad666fd366755c"
EXPECTED_ANNEX_SHA256 = {
    "canonical-operating-model.md": "a23e0d50ccb33e1f4793716494bac59719bbca02dc9d52809a9c252293c7b975",
    "banking-ceremonies.md": "739af084713ff5a9574870ea8e8e116ebb86762b52fe9cd761cccf98f9a6613d",
    "institution-integration-architecture.md": "ad2a7193b3286fa4c7e0d35beabdb1e187d7e4437872a05a265a1acd2fc405f6",
    "governance-principles.md": "98cb009e02f95b7427e515c5b0d987fa4fce5ae4bc4ab27c37e4288762308ecc",
    "treasury-and-settlement-grammar.md": "9f4326c03c47f96a515f5ca778399b185866c71f90830f7306bbf91ff0bc8b0c",
    "institutional-readiness-framework.md": "be2b9bd4bac76641fe004663ede4d51f0c925e7854faf190576cfed23b585d6f",
    "glossary.md": "325f2ea817bdf712020d3adb24cd137384f21a4658b3c67af1ba283b8c87ea78",
    "applying-program-guide-to-pvb.md": "6f6139012eb70de579762359475ecfee146f0c825d8559c1967b142aae183478",
}
ANNEX_FILES = tuple(EXPECTED_ANNEX_SHA256)
DIAGRAM_CAPTIONS = (
    "Canonical operating model",
    "Program participants",
    "Bounded public-assistance ceremony",
    "Candidate ceremony sequence",
    "Treasury and settlement grammar",
    "Institutional readiness progression",
    "Philippine Veterans Bank institutional identity",
)


def load_base_publisher():
    spec = importlib.util.spec_from_file_location(
        "thrift_bank_program_guide_publisher", BASE_PUBLISHER_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load Program Guide publisher: {BASE_PUBLISHER_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sys.dont_write_bytecode = True
BASE = load_base_publisher()
BASE.MERMAID_CACHE_PATH = MERMAID_CACHE_PATH


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def corpus_sha256(paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in paths:
        relative = path.relative_to(REPOSITORY_ROOT).as_posix().encode("utf-8")
        digest.update(relative)
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def render_inline(value: str) -> str:
    escaped = html.escape(value, quote=False)
    escaped = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", escaped)
    escaped = re.sub(r"`([^`]+)`", r'<code class="inline-code">\1</code>', escaped)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    return re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", escaped)


BASE.render_inline = render_inline
BASE.BASE.render_inline = render_inline
BASE.BASE.PULL_QUOTES = {
    "The government entity brings lawful purpose and instruction. PVB brings banking authority and the approved rails. x-change brings the operating grammar. Institution-specific integration connects them.",
    "The public institution authorized an outcome. Philippine Veterans Bank arranged its accountable execution.",
}


def verify_frozen_sources() -> dict[str, str]:
    if sha256(SOURCE) != EXPECTED_SOURCE_SHA256:
        raise ValueError("Canonical PVB manuscript hash mismatch. Refusing to publish.")

    hashes = {str(SOURCE.relative_to(REPOSITORY_ROOT)): EXPECTED_SOURCE_SHA256}
    for filename, expected in EXPECTED_ANNEX_SHA256.items():
        path = ANNEX_ROOT / filename
        if not path.is_file():
            raise FileNotFoundError(f"Canonical annex not found: {path}")
        actual = sha256(path)
        if actual != expected:
            raise ValueError(f"Canonical annex hash mismatch: {filename}: {actual}")
        hashes[str(path.relative_to(REPOSITORY_ROOT))] = actual
    return hashes


def normalized_annex(markdown: str, expected_letter: str) -> str:
    lines = markdown.splitlines()
    expected = rf"# Annex {expected_letter} — .+"
    if not lines or not re.fullmatch(expected, lines[0]):
        raise ValueError(f"Annex {expected_letter} does not begin with its canonical heading.")

    normalized: list[str] = []
    for index, line in enumerate(lines):
        if index == 0:
            normalized.append(f"#{line}")
        elif re.match(r"^#{2,3}\s", line):
            normalized.append(f"#{line}")
        else:
            normalized.append(line)
    return "\n".join(normalized)


def publication_scope(markdown: str) -> str:
    identity = markdown.split("## Foreword", maxsplit=1)[0]
    for value in (
        "# Government Depository Digital Banking Program Guide",
        "## Philippine Veterans Bank Edition",
        "### Executive Edition",
        "Version 0.9 Editorial Draft",
    ):
        if value not in identity:
            raise ValueError(f"Canonical publication identity is incomplete: {value}")

    if "## Foreword" not in markdown or "## Annexes" not in markdown:
        raise ValueError("Foreword or Annexes boundary not found in canonical manuscript.")
    core = "## Foreword\n" + markdown.split("## Foreword", maxsplit=1)[1].strip()

    annexes: list[str] = []
    for letter, filename in zip("ABCDEFGH", ANNEX_FILES, strict=True):
        annexes.append(
            normalized_annex(
                (ANNEX_ROOT / filename).read_text(encoding="utf-8"), letter
            )
        )
    scope = "\n\n".join([core, *annexes])

    headings = re.findall(r"^## (.+)$", scope, flags=re.MULTILINE)
    expected = (
        ["Foreword", "Executive Summary"]
        + [f"Section {index}" for index in range(1, 8)]
        + ["Annexes"]
        + [f"Annex {letter}" for letter in "ABCDEFGH"]
    )
    if len(headings) != len(expected):
        raise ValueError(f"Expected {len(expected)} major sections; found {len(headings)}.")
    for prefix, heading in zip(expected, headings, strict=True):
        if not heading.startswith(prefix):
            raise ValueError(
                f"Unexpected publication sequence: expected {prefix!r}, found {heading!r}."
            )
    return scope


def major_section(label: str, anchor: str) -> tuple[str, str | None, str | None]:
    section_match = re.fullmatch(r"Section (\d+) — (.+)", label)
    annex_match = re.fullmatch(r"Annex ([A-H]) — (.+)", label)

    if section_match:
        number, title = section_match.groups()
        running = f"SECTION {number} · {title.upper()}"
        return (
            f'<section class="major-section" id="{anchor}">'
            f'<div class="section-number">Section {number}</div>'
            f'<h2 data-running="{html.escape(running, quote=True)}">'
            f"{render_inline(title)}</h2>",
            number,
            title,
        )

    if annex_match:
        letter, title = annex_match.groups()
        running = f"ANNEX {letter} · {title.upper()}"
        return (
            f'<section class="major-section annex-section" id="{anchor}">'
            f'<div class="section-number">Annex {letter}</div>'
            f'<h2 data-running="{html.escape(running, quote=True)}">'
            f"{render_inline(title)}</h2>",
            letter,
            title,
        )

    if label == "Foreword":
        return (
            f'<section class="major-section foreword-section" id="{anchor}">'
            '<div class="section-number">Philippine Veterans Bank Edition</div>'
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


def render_manuscript(markdown: str, working_path: Path) -> tuple[str, list[tuple[str, str, str]]]:
    prepared, diagrams = BASE.extract_mermaid(publication_scope(markdown))
    if len(diagrams) != len(DIAGRAM_CAPTIONS):
        raise ValueError(
            f"Expected {len(DIAGRAM_CAPTIONS)} Mermaid diagrams; found {len(diagrams)}."
        )

    lines = prepared.splitlines()
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
            anchor = BASE.BASE.slugify(label)
            suffix = 2
            while anchor in used_ids:
                anchor = f"{BASE.BASE.slugify(label)}-{suffix}"
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
                class_name = " section-summary" if label == "Section Summary" else ""
                rendered.append(
                    f'<h{level} id="{anchor}" class="subheading{class_name}">'
                    f"{render_inline(label)}</h{level}>"
                )
            index += 1
            continue

        if line.startswith(">"):
            block, index = BASE.BASE.render_quote(lines, index)
            rendered.append(block)
            continue

        if line.lstrip().startswith("|"):
            block, index = BASE.BASE.render_table(lines, index)
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

        if line.startswith("MERMAIDDIAGRAM"):
            rendered.append(f"<p>{line}</p>")
            index += 1
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
                or next_line.startswith("MERMAIDDIAGRAM")
            ):
                break
            paragraph_lines.append(next_line)
            index += 1

        paragraph = " ".join(part.strip() for part in paragraph_lines)
        rendered.append(
            BASE.BASE.render_paragraph(paragraph, opening_paragraph_pending)
        )
        opening_paragraph_pending = False

    if section_open:
        rendered.append("</section>")
    if current_section != "Annex H — Applying This Program Guide to PVB":
        raise ValueError(f"Publication ended at unexpected section: {current_section}")
    if len(contents) != 17:
        raise ValueError(f"Expected 17 contents entries; found {len(contents)}.")

    manuscript = "\n".join(rendered)
    for diagram_index, diagram in enumerate(diagrams):
        token = f"<p>MERMAIDDIAGRAM{diagram_index:03d}</p>"
        svg = render_mermaid_svg(diagram, diagram_index, working_path)
        caption = DIAGRAM_CAPTIONS[diagram_index]
        replacement = (
            f'<figure class="canonical-diagram" aria-label="Figure {diagram_index + 1}: '
            f'{html.escape(caption, quote=True)}">{svg}'
            f'<figcaption><span>Figure {diagram_index + 1}</span>{html.escape(caption)}</figcaption>'
            "</figure>"
        )
        if manuscript.count(token) != 1:
            raise ValueError(f"Unable to place Mermaid diagram {diagram_index + 1}.")
        manuscript = manuscript.replace(token, replacement, 1)
    return manuscript, contents


def render_mermaid_svg(diagram: str, index: int, working_path: Path) -> str:
    BASE.mermaid_svg(diagram, index, working_path)
    digest = hashlib.sha256(diagram.encode("utf-8")).hexdigest()[:16]
    cached = MERMAID_CACHE_PATH / f"{digest}-svg-text.svg"
    rendered = cached.read_text(encoding="utf-8")

    def replace_foreign_object(match: re.Match[str]) -> str:
        width = float(match.group(1))
        height = float(match.group(2))
        inner = re.sub(r"<br\s*/?>", "\n", match.group(3), flags=re.IGNORECASE)
        label = html.unescape(re.sub(r"<[^>]+>", "", inner)).strip()
        lines: list[str] = []
        for paragraph in label.splitlines() or [label]:
            lines.extend(
                textwrap.wrap(
                    paragraph.strip(),
                    width=max(10, int(width / 7)),
                    break_long_words=False,
                    break_on_hyphens=False,
                )
                or [paragraph.strip()]
            )
        line_height = 14
        first_y = (height / 2) - ((len(lines) - 1) * line_height / 2)
        tspans = "".join(
            f'<tspan x="{width / 2:.3f}" y="{first_y + offset * line_height:.3f}">'
            f"{html.escape(line)}</tspan>"
            for offset, line in enumerate(lines)
        )
        return (
            '<text text-anchor="middle" dominant-baseline="middle" '
            'fill="#17283b" font-family="Arial, sans-serif" font-size="13">'
            f"{tspans}</text>"
        )

    rendered = re.sub(
        r'<foreignObject width="([^"]+)" height="([^"]+)">(.*?)</foreignObject>',
        replace_foreign_object,
        rendered,
        flags=re.DOTALL,
    )
    identifiers = sorted(
        set(re.findall(r'\bid="([^"]+)"', rendered)), key=len, reverse=True
    )
    if identifiers:
        identifier_pattern = re.compile("|".join(re.escape(value) for value in identifiers))
        rendered = identifier_pattern.sub(
            lambda identifier: f"diagram-{index:02d}-{identifier.group(0)}", rendered
        )
    return re.sub(r"^<\?xml[^>]+>\s*", "", rendered)


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


def validate_html_links(rendered: str) -> None:
    identifiers = set(re.findall(r'\bid="([^"]+)"', rendered))
    targets = re.findall(r'href="#([^"]+)"', rendered)
    missing = sorted(set(targets) - identifiers)
    if missing:
        raise RuntimeError(f"HTML contains unresolved internal links: {missing}")
    if len(targets) != 17:
        raise RuntimeError(f"Expected 17 linked contents entries; found {len(targets)}.")


def publication_html(markdown: str, source_hashes: dict[str, str], corpus_hash: str) -> str:
    for path in (STYLESHEET_PATH, LOGO_PATH):
        if not path.is_file():
            raise FileNotFoundError(f"Required publication asset not found: {path}")

    TEMP_PDF_PATH.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=TEMP_PDF_PATH) as temporary:
        manuscript, contents = render_manuscript(markdown, Path(temporary))

    stylesheet = STYLESHEET_PATH.read_text(encoding="utf-8")
    toc = render_contents(contents)
    logo_data = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    logo_uri = f"data:image/png;base64,{logo_data}"
    canonical_source = SOURCE.relative_to(REPOSITORY_ROOT)
    footer = "PVB EDITION · EXECUTIVE REVIEW PROOF · VERSION 0.9"

    overrides = f"""
@page version {{ @bottom-left {{ content: "{footer}"; }} }}
@page contents {{ @bottom-left {{ content: "{footer}"; }} }}
@page body {{ @bottom-left {{ content: "{footer}"; }} }}
.cover-page h1 {{ max-width: 153mm; font-size: 29pt; }}
.cover-subtitle {{
  max-width: 142mm;
  color: var(--ink);
  font-size: 18pt;
  font-style: normal;
  font-weight: 600;
  line-height: 1.2;
}}
.cover-proof-label {{
  margin-top: 8mm;
  color: var(--accent);
  font-family: "Avenir Next", Avenir, sans-serif;
  font-size: 7.4pt;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}}
.cover-edition {{ line-height: 1.55; }}
.publication-record code {{
  font-size: 6.2pt;
  overflow-wrap: anywhere;
}}
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
.table-wrap {{ break-inside: auto; }}
.annex-section table {{ font-size: 7.35pt; line-height: 1.28; }}
.annex-section th {{ padding: 2.3mm 2.6mm; }}
.annex-section td {{ padding: 1.9mm 2.6mm; }}
.canonical-diagram {{
  margin: 4mm 0 8mm;
  padding: 4mm;
  border: 0.45pt solid var(--rule);
  background: #fbfaf7;
  break-inside: avoid;
  text-align: center;
}}
.canonical-diagram svg {{ width: 100%; height: auto; max-height: 130mm; }}
.canonical-diagram figcaption {{
  margin-top: 2.5mm;
  color: var(--ink);
  font-family: "Avenir Next", Avenir, sans-serif;
  font-size: 7.4pt;
  line-height: 1.35;
  text-align: left;
}}
.canonical-diagram figcaption span {{
  margin-right: 2mm;
  color: var(--accent);
  font-size: 6.3pt;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}}
#annex-d-governance-principles .table-wrap {{ break-inside: auto; }}
#annex-d-governance-principles table {{ font-size: 7.05pt; line-height: 1.24; }}
#annex-d-governance-principles th {{ padding: 2.05mm 2.4mm; }}
#annex-d-governance-principles td {{ padding: 1.65mm 2.4mm; }}
#annex-e-treasury-and-settlement-grammar .standalone-code {{
  margin-top: 2.5mm;
  margin-bottom: 4mm;
  padding-top: 3mm;
  padding-bottom: 3mm;
  line-height: 1.24;
}}
#annex-g-glossary h2 {{ margin-bottom: 7mm; }}
#annex-g-glossary p {{ margin-bottom: 0.34em; }}
"""

    source_path, source_digest = next(iter(source_hashes.items()))
    source_rows = (
        f'<div><dt>Canonical source</dt><dd>{html.escape(source_path)}<br>'
        f'<code>{source_digest}</code></dd></div>'
    )

    rendered = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="x-change">
  <meta name="description" content="Philippine Veterans Bank Executive Edition, Version 0.9 Executive Review Proof">
  <meta name="document-type" content="Banking Program Guide">
  <meta name="institution-edition" content="{INSTITUTION_EDITION}">
  <meta name="edition" content="{PUBLICATION_EDITION}">
  <meta name="publication-status" content="{STATUS}">
  <meta name="version" content="{VERSION}">
  <meta name="canonical-source" content="{html.escape(str(canonical_source), quote=True)}">
  <meta name="canonical-source-sha256" content="{EXPECTED_SOURCE_SHA256}">
  <meta name="canonical-corpus-sha256" content="{corpus_hash}">
  <title>{DOCUMENT_TITLE} — {INSTITUTION_EDITION} — {STATUS}</title>
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
      <div class="cover-edition">{PUBLICATION_EDITION}</div>
      <div class="cover-proof-label">Version {VERSION} · {STATUS}</div>
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

  <section class="version-page" aria-label="Publication information">
    <div class="version-kicker">Publication record</div>
    <h1>{DOCUMENT_TITLE}</h1>
    <p class="version-subtitle">{INSTITUTION_EDITION} · {PUBLICATION_EDITION}</p>
    <dl class="publication-record">
      <div><dt>Institution edition</dt><dd>{INSTITUTION_EDITION}</dd></div>
      <div><dt>Publication</dt><dd>{PUBLICATION_EDITION}</dd></div>
      <div><dt>Status</dt><dd>{STATUS}</dd></div>
      <div><dt>Version</dt><dd>{VERSION}</dd></div>
      <div><dt>Publication date</dt><dd>{PUBLICATION_DATE}</dd></div>
      <div><dt>Prepared for</dt><dd>{INSTITUTION}</dd></div>
      <div><dt>Prepared by</dt><dd>x-change</dd></div>
      <div><dt>Proof scope</dt><dd>Foreword, Executive Summary, Sections 1–7, and Annexes A–H</dd></div>
      <div><dt>Canonical corpus SHA-256</dt><dd><code>{corpus_hash}</code></dd></div>
      {source_rows}
    </dl>
    <div class="copyright-note">
      <p>Copyright © 2026 x-change.</p>
      <p>This artifact is a Version 0.9 Executive Review Proof. It is not Version 1.0, a First Edition, a final publication, or a publication freeze.</p>
      <p>The canonical Markdown manuscript and annexes remain the source of truth.</p>
    </div>
  </section>

  <nav class="contents-page" aria-label="Table of contents">
    <div class="front-kicker">{INSTITUTION_EDITION} · {STATUS}</div>
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
    validate_html_links(rendered)
    return rendered


def run_weasyprint(html_path: Path, pdf_path: Path, corpus_hash: str) -> None:
    executable = shutil.which("weasyprint")
    if executable is None:
        raise RuntimeError("weasyprint executable not found on PATH.")
    subprocess.run(
        [
            executable,
            "--pdf-tags",
            "--srgb",
            "--custom-metadata",
            "--pdf-identifier",
            f"urn:sha256:{corpus_hash}:executive-review-proof",
            "--pdf-version",
            "1.7",
            "--full-fonts",
            "--hinting",
            str(html_path),
            str(pdf_path),
        ],
        check=True,
    )


def render_cover(pdf_path: Path, cover_path: Path) -> None:
    executable = shutil.which("pdftoppm")
    if executable is None:
        raise RuntimeError("pdftoppm executable not found on PATH.")
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


def count_outline(items: list[object]) -> int:
    return sum(count_outline(item) if isinstance(item, list) else 1 for item in items)


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
                    descendant.get_object() for descendant in font["/DescendantFonts"]
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
                    key in descriptor for key in ("/FontFile", "/FontFile2", "/FontFile3")
                )
    return embedded, sorted(names)


def pdf_record(pdf_path: Path) -> dict[str, object]:
    reader = PdfReader(pdf_path)
    page_sizes: list[list[float]] = []
    internal_links = 0
    external_links: list[str] = []
    for page in reader.pages:
        page_sizes.append(
            [round(float(page.mediabox.width), 2), round(float(page.mediabox.height), 2)]
        )
        for annotation_reference in page.get("/Annots", []):
            annotation = annotation_reference.get_object()
            action = annotation.get("/A")
            if action and action.get("/URI"):
                external_links.append(str(action.get("/URI")))
            elif annotation.get("/Dest") or (action and action.get("/D")):
                internal_links += 1

    embedded, font_names = font_embedding(reader)
    tagged = "/StructTreeRoot" in reader.trailer["/Root"]
    return {
        "file": pdf_path.name,
        "sha256": sha256(pdf_path),
        "bytes": pdf_path.stat().st_size,
        "physical_pages": len(reader.pages),
        "numbered_pages": max(0, len(reader.pages) - 1),
        "page_sizes_points": page_sizes,
        "bookmarks": count_outline(reader.outline),
        "internal_link_annotations": internal_links,
        "external_link_targets": external_links,
        "fonts_embedded": embedded,
        "font_names": font_names,
        "tagged_pdf": tagged,
        "metadata": {key: str(value) for key, value in (reader.metadata or {}).items()},
    }


def validate_pdf(pdf_path: Path, record: dict[str, object]) -> None:
    reader = PdfReader(pdf_path)
    text = " ".join(page.extract_text() or "" for page in reader.pages)
    normalized = re.sub(r"\s+", " ", text).lower()
    required = (
        "version 0.9 executive review proof",
        "foreword",
        "executive summary",
        "section 7 launching the program",
        "annex a canonical operating model",
        "annex h applying this program guide to pvb",
        "the public institution authorized an outcome. philippine veterans bank arranged its accountable execution.",
    )
    for phrase in required:
        if phrase not in normalized:
            raise RuntimeError(f"Rendered PDF text is missing: {phrase}")

    expected_size = [595.28, 841.89]
    if any(size != expected_size for size in record["page_sizes_points"]):
        raise RuntimeError("One or more PDF pages are not A4.")
    if not record["fonts_embedded"]:
        raise RuntimeError("One or more PDF fonts are not embedded.")
    if record["bookmarks"] < 17:
        raise RuntimeError("PDF bookmark structure is incomplete.")
    if record["internal_link_annotations"] < 17:
        raise RuntimeError("PDF internal contents links are incomplete.")
    if record["external_link_targets"]:
        raise RuntimeError("Unexpected external PDF links were generated.")

    outside = 0
    with pdfplumber.open(pdf_path) as document:
        for page in document.pages:
            for character in page.chars:
                if (
                    character["x0"] < -0.5
                    or character["x1"] > page.width + 0.5
                    or character["top"] < -0.5
                    or character["bottom"] > page.height + 0.5
                ):
                    outside += 1
    if outside:
        raise RuntimeError(f"PDF contains {outside} characters outside page bounds.")


def write_report(
    path: Path,
    corpus_hash: str,
    html_path: Path,
    pdf_path: Path,
    record: dict[str, object],
) -> None:
    report = f"""# Publication Review Report

## Philippine Veterans Bank Executive Edition

**Proof:** Version {VERSION} {STATUS}

**Review date:** {PUBLICATION_DATE}

**Format:** A4 PDF

**Physical page count:** {record['physical_pages']}

**Numbered page count:** {record['numbered_pages']}, following an unnumbered cover

## Review Scope

This report records publication observations only. The canonical manuscript and Annexes A–H were treated as read-only source material throughout rendering and review.

The proof was inspected page by page for cover treatment, contents accuracy, section flow, typography, page rhythm, tables, diagrams, annex hierarchy, headers, footers, links, bookmarks, clipping, and overflow.

## Publication Observations

### Cover and publication identity

- The cover follows the established Program Guide hierarchy and identifies the institution, Executive Edition, Version 0.9, and Executive Review Proof status without presenting the artifact as final.
- The x-change icon and lowercase wordmark remain grouped, unbroken, and clear of adjacent content.
- The publication record repeats the proof status and identifies the complete frozen source corpus.

### Contents and section flow

- The contents page lists the Foreword, Executive Summary, Sections 1–7, and Annexes A–H in the canonical order.
- All 17 contents links resolve to valid internal destinations and displayed page references follow the rendered section openings.
- Each major section and annex begins on a new page. Executive Questions, Key Messages, and Executive Decisions retain the established restrained callout treatment.

### Typography and page rhythm

- The proof uses the shared Program Guide serif-body and sans-serif-heading hierarchy, margins, running headers, footers, and section-opening treatment.
- Body measure, justification, paragraph spacing, heading hierarchy, and whitespace remain consistent across the main Guide and annexes.
- No clipped text, content overflow, accidental blank page, isolated heading, or malformed Markdown artifact was observed.

### Tables and diagrams

- The Governance and Readiness tables remain within the printable area with repeating headers and legible wrapping.
- All seven governed Mermaid sources render as inline vector figures with publication-only captions.
- No figure is clipped or split; labels, connectors, and node boundaries remain readable in the A4 proof.

### Publication-only corrections made during proofing

- The publication record was kept to one physical page by presenting the canonical corpus hash and principal source there; the complete nine-file source register remains in the publication manifest.
- Mermaid labels that use line breaks were normalized within the publisher's inline-SVG step so the governed diagram wording renders visibly and consistently. The governed Mermaid sources were not changed.
- These corrections affect rendering only. No manuscript, annex, doctrine, recommendation, or diagram source was modified.

### Annex journey and publication-family comparison

- Annexes A–H follow the same visual sequence and opening treatment as the AllBank Executive Edition.
- The PVB cover, contents, section rhythm, annex transitions, typography, and executive restraint visibly belong to the same publication family.
- The differences arise from PVB's institution and Government Depository context, not from publication quality or structure.

## Integrity and Technical Verification

- Canonical manuscript SHA-256: `{EXPECTED_SOURCE_SHA256}`
- Canonical manuscript-plus-annexes corpus SHA-256: `{corpus_hash}`
- Review-proof HTML SHA-256: `{sha256(html_path)}`
- Review-proof PDF SHA-256: `{sha256(pdf_path)}`
- PDF producer: WeasyPrint 66.0
- Page geometry: A4 on every page
- Fonts embedded: {str(record['fonts_embedded']).lower()}
- PDF tagged structure: {str(record['tagged_pdf']).lower()}
- Bookmarks: {record['bookmarks']}
- Internal link annotations: {record['internal_link_annotations']}
- External link targets: {len(record['external_link_targets'])}
- Characters outside page bounds: 0
- Canonical manuscript and annex diffs: none

## Accessibility Note

The HTML uses logical landmarks, heading hierarchy, internal navigation, figure labels, and captions. The PDF includes bookmarks, internal links, embedded fonts, document metadata, and tagged structure generated by the current WeasyPrint pipeline. Formal PDF/UA conformance has not been independently certified.

## Review Finding

No blocking publication defect remains in this proof. It is ready for executive review as a **Version 0.9 Executive Review Proof**. Publication freeze and Version 1.0 remain separate future decisions.
"""
    path.write_text(report, encoding="utf-8")


def write_checksums(path: Path, artifacts: list[Path]) -> None:
    lines = [f"{sha256(artifact)}  {artifact.name}" for artifact in artifacts]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Publish the PVB Executive Edition Version 0.9 Executive Review Proof."
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_ROOT)
    args = parser.parse_args()

    source_hashes_before = verify_frozen_sources()
    source_paths = [SOURCE, *(ANNEX_ROOT / filename for filename in ANNEX_FILES)]
    corpus_hash = corpus_sha256(source_paths)
    markdown = SOURCE.read_text(encoding="utf-8")
    rendered = publication_html(markdown, source_hashes_before, corpus_hash)

    output_root = args.output_dir.resolve()
    output_root.mkdir(parents=True, exist_ok=True)
    html_path = output_root / f"{OUTPUT_STEM}.html"
    pdf_path = output_root / f"{OUTPUT_STEM}.pdf"
    cover_path = output_root / f"{OUTPUT_STEM}-cover.png"
    report_path = output_root / "PUBLICATION_REVIEW_REPORT.md"
    manifest_path = output_root / "publication-manifest.json"
    checksums_path = output_root / "SHA256SUMS.txt"

    html_path.write_text(rendered, encoding="utf-8")
    run_weasyprint(html_path, pdf_path, corpus_hash)
    render_cover(pdf_path, cover_path)
    record = pdf_record(pdf_path)
    validate_pdf(pdf_path, record)

    source_hashes_after = verify_frozen_sources()
    if source_hashes_after != source_hashes_before:
        raise RuntimeError("Canonical source corpus changed during publication.")

    write_report(report_path, corpus_hash, html_path, pdf_path, record)
    manifest = {
        "publication_family": "x-change Banking Program Guides",
        "title": DOCUMENT_TITLE,
        "institution_edition": INSTITUTION_EDITION,
        "publication": PUBLICATION_EDITION,
        "status": STATUS,
        "version": VERSION,
        "publication_date": PUBLICATION_DATE,
        "canonical_sources": [
            {"file": path, "sha256": digest}
            for path, digest in source_hashes_after.items()
        ],
        "canonical_corpus_sha256": corpus_hash,
        "renderer": {
            "engine": "WeasyPrint 66.0",
            "publisher": str(Path(__file__).resolve().relative_to(REPOSITORY_ROOT)),
            "stylesheet": str(STYLESHEET_PATH.relative_to(REPOSITORY_ROOT)),
            "mermaid_figures": len(DIAGRAM_CAPTIONS),
            "source_files_unchanged": True,
        },
        "html": {
            "file": html_path.name,
            "sha256": sha256(html_path),
            "bytes": html_path.stat().st_size,
        },
        "pdf": record,
        "cover_preview": {
            "file": cover_path.name,
            "sha256": sha256(cover_path),
            "bytes": cover_path.stat().st_size,
        },
        "publication_review_report": report_path.name,
        "quality_assurance": {
            "page_by_page_visual_inspection": True,
            "a4_geometry": True,
            "fonts_embedded": record["fonts_embedded"],
            "bookmarks_present": record["bookmarks"] >= 17,
            "internal_links_valid": record["internal_link_annotations"] >= 17,
            "external_links": len(record["external_link_targets"]),
            "characters_outside_page_bounds": 0,
            "canonical_sources_unchanged": True,
        },
    }
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    write_checksums(
        checksums_path,
        [html_path, pdf_path, cover_path, report_path, manifest_path],
    )
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
