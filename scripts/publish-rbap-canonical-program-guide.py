#!/usr/bin/env python3

from __future__ import annotations

import argparse
import base64
import hashlib
import html
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
from dataclasses import dataclass
from pathlib import Path

import yaml


DOCUMENT_TITLE = "RBAP Digital Banking Program"
DOCUMENT_FORM = "Program Guide"
SUBTITLE = "A Collective Modernization Initiative for Philippine Rural Banks"
PUBLICATION_ROLE = "Institutional Reference Publication"
PUBLICATION_DATE = "July 2026"
VERIFICATION_DATE = "2026-07-18"
PDF_IDENTIFIER = "urn:x-change:rbap-digital-banking-program-guide:institutional-reference"

DETERMINISTIC_WEASYPRINT_SCRIPT = """
import builtins
import logging
import sys

from weasyprint import HTML
import weasyprint.pdf.tags as tags

identifiers = {}


def stable_box_identifier(box):
    object_identifier = builtins.id(box)
    return identifiers.setdefault(object_identifier, 1_000_000_000 + len(identifiers))


tags.id = stable_box_identifier
logging.getLogger("weasyprint").setLevel(logging.ERROR)
HTML(filename=sys.argv[1]).write_pdf(
    sys.argv[2],
    pdf_variant="pdf/ua-1",
    pdf_tags=True,
    custom_metadata=True,
    pdf_identifier=sys.argv[3],
    srgb=True,
)
"""

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
BASE_PUBLISHER_PATH = REPOSITORY_ROOT / "scripts" / "publish-rbap-program-guide.py"
METADATA_PATH = (
    REPOSITORY_ROOT / "docs" / "editorial" / "program-guides" / "rbap" / "metadata.yaml"
)
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
TEMP_PDF_PATH = Path(tempfile.gettempdir()) / "x-change-monographs" / "pdfs"
MERMAID_CACHE_PATH = TEMP_PDF_PATH / "rbap-program-guide-mermaid-cache"

PROTECTED_LEGACY_PATHS = {
    (REPOSITORY_ROOT / "build" / "pdf" / "rbap-digital-banking-program-guide-edition-1.pdf").resolve(),
    (
        REPOSITORY_ROOT
        / "build"
        / "program-guides"
        / "rbap"
        / "edition-1"
        / "rbap-digital-banking-program-guide-edition-1.html"
    ).resolve(),
}

BODY_FIGURE_MAP = {
    "Familiar Remittance Pattern": "Familiar Remittance Pattern",
    "Operating Perspectives": "Operating Perspectives",
    "Operating Flow": "Source-to-Settlement Operating Flow",
    "End-to-End Banking Activity": "End-to-End Banking Activity",
    "Manager's Check and Pay Code Remittance": "Manager's Check and Pay Code Customer Journey",
    "Behind the Counter": "Behind the Counter",
    "Operating Model": "Funding Event to Execution Lifecycle",
}


@dataclass(frozen=True)
class Diagram:
    title: str
    source: str
    caption: str


def load_base_publisher():
    spec = importlib.util.spec_from_file_location(
        "rbap_program_guide_base_publisher", BASE_PUBLISHER_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load base publisher: {BASE_PUBLISHER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


sys.dont_write_bytecode = True
BASE = load_base_publisher()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_text(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))


def render_inline(value: str) -> str:
    escaped = html.escape(value, quote=False)
    escaped = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", escaped)
    escaped = re.sub(r"`([^`]+)`", r'<code class="inline-code">\1</code>', escaped)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    return re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", escaped)


BASE.render_inline = render_inline


def load_locked_metadata() -> dict[str, object]:
    metadata = yaml.safe_load(METADATA_PATH.read_text(encoding="utf-8"))
    if metadata.get("status") != "canonical":
        raise ValueError("RBAP metadata does not identify a canonical source.")
    if metadata.get("canonical_state") != "locked":
        raise ValueError("RBAP metadata does not identify a locked canonical state.")
    editorial = metadata.get("editorial", {})
    if not isinstance(editorial, dict):
        raise ValueError("RBAP editorial metadata is malformed.")
    if editorial.get("executive_summary_status") != "Locked":
        raise ValueError("The Executive Summary is not locked in metadata.")
    if editorial.get("appendices_status") != "Canonical and Locked":
        raise ValueError("Appendices A-G are not locked in metadata.")
    return metadata


def canonical_scope(markdown: str) -> str:
    start_marker = "## Executive Summary"
    if start_marker not in markdown:
        raise ValueError("Executive Summary heading not found in canonical manuscript.")
    scope = f"{start_marker}\n{markdown.split(start_marker, maxsplit=1)[1].rstrip()}"
    headings = re.findall(r"^## (.+)$", scope, flags=re.MULTILINE)
    expected_prefixes = (
        ["Executive Summary"]
        + [f"Section {index}" for index in range(1, 8)]
        + [f"Appendix {letter}" for letter in "ABCDEFG"]
    )
    if len(headings) != len(expected_prefixes):
        raise ValueError(
            f"Expected {len(expected_prefixes)} major sections; found {len(headings)}."
        )
    for expected, heading in zip(expected_prefixes, headings):
        if not heading.startswith(expected):
            raise ValueError(
                f"Unexpected publication sequence: expected {expected!r}, found {heading!r}."
            )
    if "_Placeholder._" in scope:
        raise ValueError("An appendix placeholder remains in the canonical scope.")
    return scope


def extract_diagrams(scope: str) -> dict[str, Diagram]:
    appendix_g = scope.split("## Appendix G — Program Diagrams", maxsplit=1)[1]
    pattern = re.compile(
        r"^#### (?P<title>.+?)\n\n```mermaid\n(?P<source>.*?)\n```\n\n"
        r"\*Caption: (?P<caption>.*?)\*$",
        flags=re.MULTILINE | re.DOTALL,
    )
    diagrams: dict[str, Diagram] = {}
    for match in pattern.finditer(appendix_g):
        diagram = Diagram(
            title=match.group("title").strip(),
            source=match.group("source").strip(),
            caption=match.group("caption").strip(),
        )
        if diagram.title in diagrams:
            raise ValueError(f"Duplicate diagram title: {diagram.title}")
        diagrams[diagram.title] = diagram
    if len(diagrams) != 25:
        raise ValueError(f"Expected 25 governed diagrams; found {len(diagrams)}.")
    missing = sorted(set(BODY_FIGURE_MAP.values()) - set(diagrams))
    if missing:
        raise ValueError(f"Body placeholder mappings are missing sources: {missing}")
    return diagrams


def prepare_publication_markdown(
    scope: str, diagrams: dict[str, Diagram]
) -> tuple[str, dict[str, Diagram]]:
    tokens: dict[str, Diagram] = {}

    def replace_body_placeholder(match: re.Match[str]) -> str:
        placeholder = match.group("title").strip()
        source_title = BODY_FIGURE_MAP.get(placeholder)
        if source_title is None:
            raise ValueError(f"Unmapped frozen body placeholder: {placeholder}")
        token = f"PUBLICATIONFIGUREBODY{len(tokens):03d}"
        tokens[token] = diagrams[source_title]
        return f"\n{token}\n"

    prepared = re.sub(
        r'^> \*\*Visual placeholder — (?P<title>.+?)\*\*\n(?:^>.*(?:\n|$))*',
        replace_body_placeholder,
        scope,
        flags=re.MULTILINE,
    )
    if "Visual placeholder" in prepared:
        raise ValueError("A frozen body placeholder was not substituted for publication.")
    if len([token for token in tokens if token.startswith("PUBLICATIONFIGUREBODY")]) != 7:
        raise ValueError("Expected seven frozen body placeholder substitutions.")

    appendix_pattern = re.compile(
        r"^#### (?P<title>.+?)\n\n```mermaid\n(?P<source>.*?)\n```\n\n"
        r"\*Caption: (?P<caption>.*?)\*$",
        flags=re.MULTILINE | re.DOTALL,
    )

    def replace_appendix_figure(match: re.Match[str]) -> str:
        title = match.group("title").strip()
        diagram = diagrams.get(title)
        if diagram is None:
            raise ValueError(f"Unknown Appendix G diagram: {title}")
        if diagram.source != match.group("source").strip():
            raise ValueError(f"Diagram source changed during preparation: {title}")
        if diagram.caption != match.group("caption").strip():
            raise ValueError(f"Diagram caption changed during preparation: {title}")
        token = f"PUBLICATIONFIGUREAPPENDIX{len(tokens):03d}"
        tokens[token] = diagram
        return f"#### {title}\n\n{token}"

    appendix_marker = "## Appendix G — Program Diagrams"
    before_appendix, appendix_body = prepared.split(appendix_marker, maxsplit=1)
    appendix_body = appendix_pattern.sub(replace_appendix_figure, appendix_body)
    prepared = f"{before_appendix}{appendix_marker}{appendix_body}"
    appendix_tokens = [
        token for token in tokens if token.startswith("PUBLICATIONFIGUREAPPENDIX")
    ]
    if len(appendix_tokens) != 25:
        raise ValueError(f"Expected 25 Appendix G figure tokens; found {len(appendix_tokens)}.")
    if "```mermaid" in prepared:
        raise ValueError("A Mermaid source block remains unprepared.")
    return prepared, tokens


def mermaid_svg_source(diagram: Diagram, working_path: Path) -> str:
    executable = shutil.which("mmdc")
    if executable is None:
        raise RuntimeError("Mermaid CLI (mmdc) not found on PATH.")

    digest = sha256_text(diagram.source)[:20]
    MERMAID_CACHE_PATH.mkdir(parents=True, exist_ok=True)
    output = MERMAID_CACHE_PATH / f"{digest}-neutral.svg"
    if not output.is_file():
        source = working_path / f"{digest}.mmd"
        config = working_path / "mermaid-config.json"
        source.write_text(diagram.source, encoding="utf-8")
        config.write_text(
            json.dumps(
                {
                    "flowchart": {"htmlLabels": False, "curve": "linear"},
                    "themeVariables": {
                        "fontFamily": "Avenir Next, Avenir, Arial, sans-serif",
                        "fontSize": "13px",
                        "primaryColor": "#f7f5f0",
                        "primaryTextColor": "#17283b",
                        "primaryBorderColor": "#947553",
                        "lineColor": "#697077",
                        "secondaryColor": "#f2eee7",
                        "tertiaryColor": "#fffefa",
                        "background": "#fffefa",
                    },
                },
                sort_keys=True,
            ),
            encoding="utf-8",
        )
        result = subprocess.run(
            [
                executable,
                "-i",
                str(source),
                "-o",
                str(output),
                "-c",
                str(config),
                "-b",
                "transparent",
                "-t",
                "neutral",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError(
                f"Unable to render Mermaid diagram {diagram.title!r}: "
                f"{result.stderr.strip()}"
            )
    rendered = output.read_text(encoding="utf-8")

    def replace_foreign_object(match: re.Match[str]) -> str:
        width = float(match.group(1))
        height = float(match.group(2))
        label = html.unescape(re.sub(r"<[^>]+>", "", match.group(3))).strip()
        lines = textwrap.wrap(
            label,
            width=max(10, int(width / 7)),
            break_long_words=False,
            break_on_hyphens=False,
        ) or [label]
        line_height = 14
        first_y = (height / 2) - ((len(lines) - 1) * line_height / 2)
        tspans = "".join(
            f'<tspan x="{width / 2:.3f}" '
            f'y="{first_y + offset * line_height:.3f}">{html.escape(line)}</tspan>'
            for offset, line in enumerate(lines)
        )
        return (
            '<text text-anchor="middle" dominant-baseline="middle" '
            'fill="#17283b" font-family="Arial, sans-serif" font-size="13">'
            f"{tspans}</text>"
        )

    rendered = re.sub(
        r'<foreignObject width="([^"]+)" height="([^"]+)">.*?'
        r"<p>(.*?)</p>.*?</foreignObject>",
        replace_foreign_object,
        rendered,
        flags=re.DOTALL,
    )
    return re.sub(r"^<\?xml[^>]+>\s*", "", rendered)


def namespace_svg(rendered: str, figure_number: int) -> str:
    identifiers = sorted(
        set(re.findall(r'\bid="([^"]+)"', rendered)), key=len, reverse=True
    )
    if identifiers:
        pattern = re.compile("|".join(re.escape(value) for value in identifiers))
        rendered = pattern.sub(
            lambda match: f"figure-{figure_number:02d}-{match.group(0)}", rendered
        )
    return rendered


def render_figure(
    diagram: Diagram, figure_number: int, working_path: Path
) -> str:
    rendered = namespace_svg(mermaid_svg_source(diagram, working_path), figure_number)
    title_id = f"figure-{figure_number:02d}-title"
    description_id = f"figure-{figure_number:02d}-description"
    def replace_svg_tag(match: re.Match[str]) -> str:
        attributes = re.sub(r'\srole="[^"]*"', "", match.group(1))
        return (
            f'<svg{attributes} role="img" '
            f'aria-labelledby="{title_id} {description_id}" focusable="false">'
            f'<title id="{title_id}">{html.escape(diagram.title)}</title>'
            f'<desc id="{description_id}">{html.escape(diagram.caption)}</desc>'
        )

    rendered = re.sub(r"<svg\b([^>]*)>", replace_svg_tag, rendered, count=1)
    svg_uri = "data:image/svg+xml;base64," + base64.b64encode(
        rendered.encode("utf-8")
    ).decode("ascii")
    caption_id = f"figure-{figure_number:02d}-caption"
    alternative = f"{diagram.title}. {diagram.caption}"
    return (
        f'<figure class="publication-figure" id="figure-{figure_number:02d}">'
        f'<div class="figure-number">Figure {figure_number}</div>'
        f'<img class="figure-svg" src="{svg_uri}" '
        f'alt="{html.escape(alternative, quote=True)}" '
        f'aria-describedby="{caption_id}">'
        f'<figcaption id="{caption_id}">'
        f'<strong>{html.escape(diagram.title)}</strong> — '
        f"{html.escape(diagram.caption)}"
        "</figcaption></figure>"
    )


def render_manuscript(
    prepared: str, tokens: dict[str, Diagram], working_path: Path
) -> tuple[str, list[tuple[str, str]], int]:
    lines = prepared.splitlines()
    rendered: list[str] = []
    contents: list[tuple[str, str]] = []
    used_ids: set[str] = set()
    current_section = ""
    opening_paragraph_pending = False
    section_open = False
    figure_number = 0
    index = 0

    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue

        if line in tokens:
            figure_number += 1
            rendered.append(render_figure(tokens[line], figure_number, working_path))
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
                opening_paragraph_pending = label == "Executive Summary"
                contents.append((label, anchor))
                section_match = re.fullmatch(r"Section (\d+) — (.+)", label)
                appendix_match = re.fullmatch(r"Appendix ([A-G]) — (.+)", label)
                if section_match:
                    number, title = section_match.groups()
                    running = f"SECTION {number} · {title.upper()}"
                    rendered.append(
                        f'<section class="major-section" id="{anchor}">'
                        f'<div class="section-number">Section {number}</div>'
                        f'<h2 data-running="{html.escape(running, quote=True)}">'
                        f"{render_inline(title)}</h2>"
                    )
                elif appendix_match:
                    letter, title = appendix_match.groups()
                    running = f"APPENDIX {letter} · {title.upper()}"
                    rendered.append(
                        f'<section class="major-section appendix-section" id="{anchor}">'
                        f'<div class="section-number">Appendix {letter}</div>'
                        f'<h2 data-running="{html.escape(running, quote=True)}">'
                        f"{render_inline(title)}</h2>"
                    )
                elif label == "Executive Summary":
                    rendered.append(
                        f'<section class="major-section executive-summary" id="{anchor}">'
                        '<div class="section-number">Board briefing</div>'
                        '<h2 data-running="EXECUTIVE SUMMARY">Executive Summary</h2>'
                    )
                else:
                    raise ValueError(f"Unsupported major heading: {label}")
            else:
                class_name = " section-summary" if label == "Section Summary" else ""
                rendered.append(
                    f'<h{level} id="{anchor}" class="subheading{class_name}">'
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
                next_line in tokens
                or re.match(r"^#{2,4}\s+", next_line)
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
    if current_section != "Appendix G — Program Diagrams":
        raise ValueError(f"Publication ended at unexpected section: {current_section}")
    if figure_number != 32:
        raise ValueError(f"Expected 32 placed figures; found {figure_number}.")
    return "\n".join(rendered), contents, figure_number


def render_contents(contents: list[tuple[str, str]]) -> str:
    items: list[str] = []
    for label, anchor in contents:
        section_match = re.fullmatch(r"Section (\d+) — (.+)", label)
        appendix_match = re.fullmatch(r"Appendix ([A-G]) — (.+)", label)
        if section_match:
            marker, title = section_match.groups()
        elif appendix_match:
            marker, title = appendix_match.groups()
        else:
            marker, title = "ES", "Executive Summary"
        items.append(
            f'<li><a href="#{anchor}"><span class="toc-number">{marker}</span>'
            f'<span class="toc-title">{html.escape(title)}</span></a></li>'
        )
    return "\n".join(items)


def publication_html(
    markdown: str,
    canonical_source: Path,
    metadata: dict[str, object],
    source_revision: str,
) -> tuple[str, int, list[Diagram]]:
    if not STYLESHEET_PATH.is_file():
        raise FileNotFoundError(f"Stylesheet not found: {STYLESHEET_PATH}")
    if not LOGO_PATH.is_file():
        raise FileNotFoundError(f"Logo not found: {LOGO_PATH}")

    scope = canonical_scope(markdown)
    diagrams = extract_diagrams(scope)
    prepared, tokens = prepare_publication_markdown(scope, diagrams)
    TEMP_PDF_PATH.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=TEMP_PDF_PATH) as temporary:
        manuscript, contents, figure_count = render_manuscript(
            prepared, tokens, Path(temporary)
        )

    version = str(metadata["version"])
    publication = "First Edition"
    stylesheet = STYLESHEET_PATH.read_text(encoding="utf-8")
    toc = render_contents(contents)
    logo_data = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    logo_uri = f"data:image/png;base64,{logo_data}"
    source_hash = sha256_text(markdown)
    footer = "RBAP DIGITAL BANKING PROGRAM · INSTITUTIONAL REFERENCE"

    overrides = f"""
@page version {{ @bottom-left {{ content: "{footer}"; }} }}
@page contents {{ @bottom-left {{ content: "{footer}"; }} }}
@page body {{ @bottom-left {{ content: "{footer}"; }} }}
.cover-page h1 {{ max-width: 150mm; font-size: 32pt; }}
.cover-subtitle {{ max-width: 138mm; }}
.cover-publication-role {{
  margin-top: 9mm;
  color: var(--ink);
  font-family: "Avenir Next", Avenir, sans-serif;
  font-size: 9pt;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}}
.cover-edition {{ margin-top: 4mm; }}
.appendix-section h2 {{ max-width: 150mm; }}
.appendix-section .table-wrap {{ break-inside: auto; }}
.appendix-section table {{ font-size: 7.35pt; }}
.appendix-section h3.subheading {{ margin-top: 7mm; }}
.publication-figure {{
  margin: 5mm 0 8mm;
  padding: 4mm 4.5mm;
  border: 0.45pt solid var(--rule);
  background: #fbfaf7;
  break-inside: avoid;
  text-align: center;
}}
.publication-figure .figure-number {{
  margin-bottom: 2.5mm;
  color: var(--accent);
  font-family: "Avenir Next", Avenir, sans-serif;
  font-size: 6.4pt;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-align: left;
  text-transform: uppercase;
}}
.publication-figure .figure-svg {{
  display: block;
  width: 100%;
  height: auto;
  max-height: 145mm;
  margin: 0 auto;
}}
.publication-figure figcaption {{
  margin-top: 3mm;
  color: var(--muted);
  font-family: "Avenir Next", Avenir, sans-serif;
  font-size: 7.2pt;
  line-height: 1.4;
  text-align: left;
}}
.publication-figure figcaption strong {{ font-weight: 600; }}
h4.subheading + .publication-figure {{ margin-top: 2mm; }}
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
  padding: 4mm 7mm;
  border-left: 1.2pt solid var(--accent);
  background: var(--panel);
  font-size: 8.1pt;
  line-height: 1.34;
  text-align: center;
}}
"""

    html_output = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="x-change">
  <meta name="description" content="{SUBTITLE}">
  <meta name="keywords" content="RBAP, rural banking, digital banking, program guide">
  <meta name="document-type" content="Banking Program Guide">
  <meta name="publication-role" content="{PUBLICATION_ROLE}">
  <meta name="publication" content="{publication}">
  <meta name="version" content="{html.escape(version, quote=True)}">
  <meta name="canonical-source" content="{html.escape(str(canonical_source), quote=True)}">
  <meta name="canonical-source-sha256" content="{source_hash}">
  <meta name="source-revision" content="{html.escape(source_revision, quote=True)}">
  <title>{DOCUMENT_TITLE} — {PUBLICATION_ROLE}</title>
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
      <p class="cover-subtitle">{SUBTITLE}</p>
      <div class="cover-publication-role">{PUBLICATION_ROLE}</div>
      <div class="cover-edition">{publication} · Version {html.escape(version)}</div>
      <div class="cover-recipient">
        <span>Prepared for</span>
        <strong>Rural Bankers Association of the Philippines</strong>
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
    <p class="version-subtitle">{PUBLICATION_ROLE} · {SUBTITLE}</p>

    <dl class="publication-record">
      <div><dt>Publication role</dt><dd>{PUBLICATION_ROLE}</dd></div>
      <div><dt>Publication</dt><dd>{publication}</dd></div>
      <div><dt>Version</dt><dd>{html.escape(version)}</dd></div>
      <div><dt>Publication date</dt><dd>{PUBLICATION_DATE}</dd></div>
      <div><dt>Prepared for</dt><dd>Rural Bankers Association of the Philippines</dd></div>
      <div><dt>Prepared by</dt><dd>x-change</dd></div>
      <div><dt>Scope</dt><dd>Executive Summary, Sections 1–7, and Appendices A–G</dd></div>
      <div><dt>Canonical source</dt><dd>{html.escape(str(canonical_source))}</dd></div>
      <div><dt>Source revision</dt><dd>{html.escape(source_revision)}</dd></div>
      <div><dt>Source SHA-256</dt><dd>{source_hash}</dd></div>
    </dl>

    <div class="copyright-note">
      <p>Copyright © 2026 x-change.</p>
      <p>This publication is rendered from the locked canonical Markdown source. Figures are deterministic publication renderings of the governed Mermaid sources. Historical Edition 1 artifacts remain separate and unchanged.</p>
    </div>
  </section>

  <nav class="contents-page" aria-label="Table of contents">
    <div class="front-kicker">{PUBLICATION_ROLE}</div>
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
    return html_output, figure_count, list(diagrams.values())


def command_version(command: list[str]) -> str:
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return (result.stdout or result.stderr).strip().splitlines()[0]


def pdf_page_count(path: Path) -> int:
    executable = shutil.which("pdfinfo")
    if executable is None:
        raise RuntimeError("pdfinfo not found on PATH.")
    result = subprocess.run(
        [executable, str(path)], check=True, capture_output=True, text=True
    )
    match = re.search(r"^Pages:\s+(\d+)$", result.stdout, flags=re.MULTILINE)
    if match is None:
        raise RuntimeError("Unable to determine PDF page count.")
    return int(match.group(1))


def protected_output(path: Path) -> None:
    if path.resolve() in PROTECTED_LEGACY_PATHS:
        raise ValueError(f"Refusing to overwrite protected historical artifact: {path}")


def build_manifest(
    source: Path,
    metadata: dict[str, object],
    source_revision: str,
    html_output: Path,
    pdf_output: Path,
    diagrams: list[Diagram],
    figure_count: int,
) -> dict[str, object]:
    return {
        "title": DOCUMENT_TITLE,
        "document_form": DOCUMENT_FORM,
        "subtitle": SUBTITLE,
        "publication_role": PUBLICATION_ROLE,
        "publication": "First Edition",
        "version": str(metadata["version"]),
        "publication_date": PUBLICATION_DATE,
        "verification_date": VERIFICATION_DATE,
        "canonical_source": str(source),
        "canonical_source_sha256": sha256_bytes(source.read_bytes()),
        "metadata_source": str(METADATA_PATH.relative_to(REPOSITORY_ROOT)),
        "metadata_sha256": sha256_bytes(METADATA_PATH.read_bytes()),
        "source_revision": source_revision,
        "scope": "Executive Summary, Sections 1-7, and Appendices A-G",
        "governed_mermaid_sources": len(diagrams),
        "placed_publication_figures": figure_count,
        "diagram_sources": [
            {
                "title": diagram.title,
                "sha256": sha256_text(diagram.source),
                "caption": diagram.caption,
            }
            for diagram in diagrams
        ],
        "renderer": {
            "publisher": str(Path(__file__).relative_to(REPOSITORY_ROOT)),
            "weasyprint": command_version(["weasyprint", "--version"]),
            "mermaid_cli": command_version(["mmdc", "--version"]),
            "diagram_format": "SVG image resources (vector)",
            "deterministic_pdf": True,
            "stable_tag_identifiers": True,
            "pdf_variant": "PDF/UA-1",
            "pdf_tags": True,
        },
        "accessibility": {
            "html_language": "en",
            "toc_navigation": True,
            "figure_alt_text": True,
            "figure_caption_associations": True,
            "figure_captions": True,
            "pdf_tagging_requested": True,
            "pdf_tagged_figures": True,
        },
        "artifacts": {
            "html": {
                "path": str(html_output.resolve().relative_to(REPOSITORY_ROOT)),
                "sha256": sha256_bytes(html_output.read_bytes()),
            },
            "pdf": {
                "path": str(pdf_output.resolve().relative_to(REPOSITORY_ROOT)),
                "sha256": sha256_bytes(pdf_output.read_bytes()),
                "page_count": pdf_page_count(pdf_output),
            },
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Publish the complete canonical RBAP Digital Banking Program Guide."
    )
    parser.add_argument("source", type=Path)
    parser.add_argument("html_output", type=Path)
    parser.add_argument("--pdf", type=Path, required=True, dest="pdf_output")
    parser.add_argument("--manifest", type=Path, required=True, dest="manifest_output")
    args = parser.parse_args()

    protected_output(args.html_output)
    protected_output(args.pdf_output)
    metadata = load_locked_metadata()
    source_revision = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=REPOSITORY_ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    markdown = args.source.read_text(encoding="utf-8")
    rendered, figure_count, diagrams = publication_html(
        markdown, args.source, metadata, source_revision
    )

    args.html_output.parent.mkdir(parents=True, exist_ok=True)
    args.html_output.write_text(rendered, encoding="utf-8")

    weasyprint = shutil.which("weasyprint")
    if weasyprint is None:
        raise RuntimeError("weasyprint executable not found on PATH.")
    shebang = Path(weasyprint).read_text(encoding="utf-8").splitlines()[0]
    if not shebang.startswith("#!/"):
        raise RuntimeError("Unable to identify the WeasyPrint Python interpreter.")
    weasyprint_python = Path(shebang[2:])
    if not weasyprint_python.is_file():
        raise RuntimeError(
            f"WeasyPrint Python interpreter not found: {weasyprint_python}"
        )
    args.pdf_output.parent.mkdir(parents=True, exist_ok=True)
    environment = os.environ.copy()
    environment.setdefault("SOURCE_DATE_EPOCH", "1784332800")
    environment.setdefault("PYTHONHASHSEED", "0")
    subprocess.run(
        [
            str(weasyprint_python),
            "-c",
            DETERMINISTIC_WEASYPRINT_SCRIPT,
            str(args.html_output),
            str(args.pdf_output),
            PDF_IDENTIFIER,
        ],
        check=True,
        env=environment,
    )

    manifest = build_manifest(
        args.source,
        metadata,
        source_revision,
        args.html_output,
        args.pdf_output,
        diagrams,
        figure_count,
    )
    args.manifest_output.parent.mkdir(parents=True, exist_ok=True)
    args.manifest_output.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
