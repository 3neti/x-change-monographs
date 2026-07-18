#!/usr/bin/env python3

from __future__ import annotations

import argparse
import base64
import hashlib
import html
import importlib.util
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
from dataclasses import dataclass
from pathlib import Path


DOCUMENT_TITLE = "Thrift Bank Digital Banking Program Guide"
DOCUMENT_FORM = "x-change Banking Program Guide"
VERSION = "1.0"
PUBLICATION = "First Edition"
PUBLICATION_DATE = "July 2026"

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
TEMP_PDF_PATH = Path(tempfile.gettempdir()) / "x-change-monographs" / "pdfs"
MERMAID_CACHE_PATH = TEMP_PDF_PATH / "thrift-bank-mermaid-cache"


@dataclass(frozen=True)
class Edition:
    key: str
    label: str
    scope: str
    expected_final_section: str
    includes_appendices: bool


EDITIONS = {
    "executive": Edition(
        key="executive",
        label="Executive Edition",
        scope="Executive Summary and Sections 1–7",
        expected_final_section="Section 7 — Launching the Program",
        includes_appendices=False,
    ),
    "institutional-reference": Edition(
        key="institutional-reference",
        label="Institutional Reference Edition",
        scope="Executive Summary, Sections 1–7, and Appendices A–G",
        expected_final_section="Appendix G — Canonical Diagrams",
        includes_appendices=True,
    ),
}

APPENDIX_FILES = (
    "glossary.md",
    "governance.md",
    "commercial-waterfall.md",
    "treasury-grammar.md",
    "deployment-architecture.md",
    "faq.md",
    "diagrams.md",
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


def executive_scope(markdown: str) -> str:
    start_marker = "## Executive Summary"
    end_marker = "## Appendices"

    if start_marker not in markdown:
        raise ValueError("Executive Summary heading not found in canonical manuscript.")
    if end_marker not in markdown:
        raise ValueError("Appendices boundary not found in canonical manuscript.")

    scoped = markdown.split(start_marker, maxsplit=1)[1]
    scoped = f"{start_marker}\n{scoped.split(end_marker, maxsplit=1)[0].rstrip()}"
    headings = re.findall(r"^## (.+)$", scoped, flags=re.MULTILINE)
    expected = ["Executive Summary"] + [f"Section {index}" for index in range(1, 8)]
    if len(headings) != len(expected):
        raise ValueError(f"Expected 8 major publication sections; found {len(headings)}.")
    for expected_prefix, heading in zip(expected, headings, strict=True):
        if not heading.startswith(expected_prefix):
            raise ValueError(
                f"Unexpected publication sequence: expected {expected_prefix!r}, "
                f"found {heading!r}."
            )
    return scoped


def normalized_appendix(markdown: str) -> str:
    lines = markdown.splitlines()
    if not lines or not re.fullmatch(r"# Appendix [A-G] — .+", lines[0]):
        raise ValueError("Appendix does not begin with the canonical heading.")

    normalized: list[str] = []
    for index, line in enumerate(lines):
        if index == 0:
            normalized.append(f"#{line}")
        elif line.startswith("## "):
            normalized.append(f"#{line}")
        else:
            normalized.append(line)
    return "\n".join(normalized)


def institutional_reference_scope(markdown: str, source: Path) -> str:
    scope = executive_scope(markdown)
    appendix_path = source.parent.parent / "appendices"
    appendices: list[str] = []

    for filename in APPENDIX_FILES:
        path = appendix_path / filename
        if not path.is_file():
            raise FileNotFoundError(f"Canonical appendix not found: {path}")
        appendices.append(normalized_appendix(path.read_text(encoding="utf-8")))

    return "\n\n".join([scope, *appendices])


def extract_mermaid(markdown: str) -> tuple[str, list[str]]:
    diagrams: list[str] = []

    def replace(match: re.Match[str]) -> str:
        diagrams.append(match.group(1).strip())
        return f"\n\nMERMAIDDIAGRAM{len(diagrams) - 1:03d}\n\n"

    prepared = re.sub(
        r"```mermaid\s*\n(.*?)\n```",
        replace,
        markdown,
        flags=re.DOTALL,
    )
    return prepared, diagrams


def mermaid_svg(diagram: str, index: int, working_path: Path) -> str:
    executable = shutil.which("mmdc")
    if executable is None:
        raise RuntimeError("Mermaid CLI (mmdc) not found on PATH.")

    source = working_path / f"diagram-{index:02d}.mmd"
    config = working_path / "mermaid-config.json"
    digest = hashlib.sha256(diagram.encode("utf-8")).hexdigest()[:16]
    MERMAID_CACHE_PATH.mkdir(parents=True, exist_ok=True)
    output = MERMAID_CACHE_PATH / f"{digest}-svg-text.svg"
    source.write_text(diagram, encoding="utf-8")
    config.write_text('{"flowchart":{"htmlLabels":false}}', encoding="utf-8")
    if not output.is_file():
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
                f"Unable to render Mermaid diagram {index}: {result.stderr.strip()}"
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
            f'<tspan x="{width / 2:.3f}" y="{first_y + offset * line_height:.3f}">'
            f"{html.escape(line)}</tspan>"
            for offset, line in enumerate(lines)
        )
        return (
            f'<text text-anchor="middle" dominant-baseline="middle" '
            f'fill="#17283b" font-family="Arial, sans-serif" font-size="13">'
            f"{tspans}</text>"
        )

    rendered = re.sub(
        r'<foreignObject width="([^"]+)" height="([^"]+)">.*?'
        r'<p>(.*?)</p>.*?</foreignObject>',
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
            lambda match: f"diagram-{index:02d}-{match.group(0)}", rendered
        )
    return re.sub(r"^<\?xml[^>]+>\s*", "", rendered)


def render_manuscript(
    markdown: str, edition: Edition, working_path: Path
) -> tuple[str, list[tuple[str, str]]]:
    prepared, diagrams = extract_mermaid(markdown)
    lines = prepared.splitlines()
    rendered: list[str] = []
    contents: list[tuple[str, str]] = []
    used_ids: set[str] = set()
    current_section = ""
    opening_paragraph_pending = False
    section_open = False
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
                        f'<h2 data-running="EXECUTIVE SUMMARY">{render_inline(label)}</h2>'
                    )
                else:
                    raise ValueError(f"Unsupported major publication heading: {label}")
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
            items = []
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
    if current_section != edition.expected_final_section:
        raise ValueError(
            f"Publication ended at {current_section!r}; expected "
            f"{edition.expected_final_section!r}."
        )

    manuscript = "\n".join(rendered)
    for diagram_index, diagram in enumerate(diagrams):
        token = f"<p>MERMAIDDIAGRAM{diagram_index:03d}</p>"
        svg = mermaid_svg(diagram, diagram_index, working_path)
        replacement = f'<figure class="canonical-diagram">{svg}</figure>'
        if manuscript.count(token) != 1:
            raise ValueError(f"Unable to place Mermaid diagram {diagram_index}.")
        manuscript = manuscript.replace(token, replacement, 1)

    return manuscript, contents


def render_contents(contents: list[tuple[str, str]]) -> str:
    items: list[str] = []
    for label, anchor in contents:
        section_match = re.fullmatch(r"Section (\d+) — (.+)", label)
        appendix_match = re.fullmatch(r"Appendix ([A-G]) — (.+)", label)
        if section_match:
            number, title = section_match.groups()
            marker = number
        elif appendix_match:
            letter, title = appendix_match.groups()
            marker = letter
        else:
            marker = "ES"
            title = "Executive Summary"
        display = (
            f'<span class="toc-number">{html.escape(marker)}</span>'
            f'<span class="toc-title">{html.escape(title)}</span>'
        )
        items.append(f'<li><a href="#{anchor}">{display}</a></li>')
    return "\n".join(items)


def apply_executive_balance(manuscript: str) -> str:
    break_markers = (
        "Open Disbursement Technologies, Inc. (ODTI) licenses and maintains x-change",
        "The Capability supports adaptability.",
        "Certification is a technical gate.",
    )
    for marker in break_markers:
        original = f"<p>{marker}"
        replacement = f'<p class="publication-balance-break">{marker}'
        if manuscript.count(original) != 1:
            raise ValueError(f"Unable to apply publication balance marker: {marker}")
        manuscript = manuscript.replace(original, replacement, 1)
    return manuscript


def publication_html(
    markdown: str, canonical_source: str, source: Path, edition: Edition
) -> str:
    if not STYLESHEET_PATH.is_file():
        raise FileNotFoundError(f"Program Guide stylesheet not found: {STYLESHEET_PATH}")
    if not LOGO_PATH.is_file():
        raise FileNotFoundError(f"Publication logo not found: {LOGO_PATH}")

    scope = (
        institutional_reference_scope(markdown, source)
        if edition.includes_appendices
        else executive_scope(markdown)
    )
    TEMP_PDF_PATH.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=TEMP_PDF_PATH) as temporary:
        manuscript, contents = render_manuscript(scope, edition, Path(temporary))
    if edition.key == "executive":
        manuscript = apply_executive_balance(manuscript)

    stylesheet = STYLESHEET_PATH.read_text(encoding="utf-8")
    toc = render_contents(contents)
    logo_data = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    logo_uri = f"data:image/png;base64,{logo_data}"
    footer = f"THRIFT BANK PROGRAM GUIDE · {edition.label.upper()}"

    overrides = f"""
@page version {{ @bottom-left {{ content: "{footer}"; }} }}
@page contents {{ @bottom-left {{ content: "{footer}"; }} }}
@page body {{ @bottom-left {{ content: "{footer}"; }} }}
.cover-page h1 {{ max-width: 150mm; font-size: 30pt; }}
.cover-subtitle {{ max-width: 138mm; font-style: normal; font-weight: 600; }}
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
.publication-balance-break {{ break-before: page; }}
.appendix-section h2 {{ max-width: 150mm; }}
.canonical-diagram {{
  margin: 4mm 0 8mm;
  padding: 4mm;
  border: 0.45pt solid var(--rule);
  background: #fbfaf7;
  break-inside: avoid;
  text-align: center;
}}
.canonical-diagram svg {{
  width: 100%;
  height: auto;
  max-height: 145mm;
}}
"""

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="x-change">
  <meta name="document-type" content="Banking Program Guide">
  <meta name="edition" content="{edition.label}">
  <meta name="publication" content="{PUBLICATION}">
  <meta name="version" content="{VERSION}">
  <meta name="canonical-source" content="{html.escape(canonical_source, quote=True)}">
  <title>{DOCUMENT_TITLE} — {edition.label}</title>
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
      <p class="cover-subtitle">{edition.label}</p>
      <div class="cover-edition">{PUBLICATION} · Version {VERSION}</div>
      <div class="cover-recipient">
        <span>Prepared by</span>
        <strong>x-change</strong>
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
    <p class="version-subtitle">{edition.label}</p>

    <dl class="publication-record">
      <div><dt>Edition</dt><dd>{edition.label}</dd></div>
      <div><dt>Publication</dt><dd>{PUBLICATION}</dd></div>
      <div><dt>Version</dt><dd>{VERSION}</dd></div>
      <div><dt>Publication date</dt><dd>{PUBLICATION_DATE}</dd></div>
      <div><dt>Prepared by</dt><dd>x-change</dd></div>
      <div><dt>Edition scope</dt><dd>{edition.scope}</dd></div>
      <div><dt>Canonical source</dt><dd>{html.escape(canonical_source)}</dd></div>
    </dl>

    <div class="copyright-note">
      <p>Copyright © 2026 x-change.</p>
      <p>Both canonical editions derive from the same frozen Institutional Study and Program Guide doctrine. Neither edition supersedes the other.</p>
    </div>
  </section>

  <nav class="contents-page" aria-label="Table of contents">
    <div class="front-kicker">{edition.label}</div>
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


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Publish a canonical Thrift Bank Digital Banking Program Guide edition."
    )
    parser.add_argument("source", type=Path)
    parser.add_argument("html_output", type=Path)
    parser.add_argument("--edition", choices=EDITIONS, default="executive")
    parser.add_argument("--pdf", type=Path, dest="pdf_output")
    args = parser.parse_args()

    edition = EDITIONS[args.edition]
    markdown = args.source.read_text(encoding="utf-8")
    rendered = publication_html(markdown, str(args.source), args.source, edition)

    args.html_output.parent.mkdir(parents=True, exist_ok=True)
    args.html_output.write_text(rendered, encoding="utf-8")

    if args.pdf_output is not None:
        weasyprint = shutil.which("weasyprint")
        if weasyprint is None:
            raise RuntimeError("weasyprint executable not found on PATH.")
        args.pdf_output.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [weasyprint, str(args.html_output), str(args.pdf_output)], check=True
        )


if __name__ == "__main__":
    main()
