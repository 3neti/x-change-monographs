#!/usr/bin/env python3

from __future__ import annotations

import argparse
import base64
import html
import re
import shutil
import subprocess
import unicodedata
from pathlib import Path


DOCUMENT_TITLE = "RBAP Digital Banking Program"
DOCUMENT_FORM = "Program Guide"
SUBTITLE = "A Collective Modernization Initiative for Philippine Rural Banks"
SHORT_TITLE = "RBAP Digital Banking Program"
EDITION = "Edition 1"
PUBLICATION_DATE = "July 2026"

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
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

PULL_QUOTES = {
    "The customer requested a banking outcome. The bank arranged it.",
    "Participating banks compete independently while modernizing collectively.",
}


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", ascii_value.lower()).strip("-")


def render_inline(value: str) -> str:
    escaped = html.escape(value, quote=False)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    return re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", escaped)


def clean_emphasis(value: str) -> str:
    return value.replace("**", "").replace("*", "").strip()


def extract_publication_scope(markdown: str) -> str:
    start_marker = "## Executive Summary"
    end_marker = "## Appendix A — Glossary"

    if start_marker not in markdown:
        raise ValueError("Executive Summary heading not found in canonical manuscript.")
    if end_marker not in markdown:
        raise ValueError("Appendix A boundary not found in canonical manuscript.")

    scoped = markdown.split(start_marker, maxsplit=1)[1]
    scoped = f"{start_marker}\n{scoped.split(end_marker, maxsplit=1)[0].rstrip()}"

    if re.search(r"^## Appendix\b", scoped, flags=re.MULTILINE):
        raise ValueError("Publication scope unexpectedly contains an appendix.")

    headings = re.findall(r"^## (.+)$", scoped, flags=re.MULTILINE)
    expected = ["Executive Summary"] + [f"Section {index}" for index in range(1, 8)]
    if len(headings) != len(expected):
        raise ValueError(f"Expected 8 major publication sections; found {len(headings)}.")
    for expected_prefix, heading in zip(expected, headings, strict=True):
        if not heading.startswith(expected_prefix):
            raise ValueError(
                f"Unexpected publication sequence: expected {expected_prefix!r}, found {heading!r}."
            )

    return scoped


def split_table_row(value: str) -> list[str]:
    return [cell.strip() for cell in value.strip().strip("|").split("|")]


def render_table(lines: list[str], index: int) -> tuple[str, int]:
    rows: list[list[str]] = []
    while index < len(lines) and lines[index].lstrip().startswith("|"):
        rows.append(split_table_row(lines[index]))
        index += 1

    if len(rows) < 2:
        raise ValueError("Markdown table is missing its separator row.")

    separator = rows[1]
    if not all(re.fullmatch(r":?-{3,}:?", cell) for cell in separator):
        raise ValueError("Markdown table separator row is malformed.")

    header = rows[0]
    body = rows[2:]
    header_html = "".join(f"<th>{render_inline(cell)}</th>" for cell in header)
    body_html = "".join(
        "<tr>" + "".join(f"<td>{render_inline(cell)}</td>" for cell in row) + "</tr>"
        for row in body
    )
    return (
        '<div class="table-wrap"><table><thead><tr>'
        f"{header_html}</tr></thead><tbody>{body_html}</tbody></table></div>",
        index,
    )


def render_quote(lines: list[str], index: int) -> tuple[str, int]:
    quote_lines: list[str] = []
    while index < len(lines) and lines[index].startswith(">"):
        quote_lines.append(lines[index][1:].lstrip())
        index += 1

    first = quote_lines[0] if quote_lines else ""
    visual_match = re.fullmatch(r"\*\*Visual placeholder — (.+?)\*\*", first)
    if visual_match:
        title = html.escape(visual_match.group(1), quote=False)
        code_lines = quote_lines[1:]
        while code_lines and not code_lines[0]:
            code_lines.pop(0)
        if code_lines and code_lines[0].startswith("```"):
            code_lines = code_lines[1:]
            if code_lines and code_lines[-1].strip() == "```":
                code_lines = code_lines[:-1]
            code = html.escape("\n".join(code_lines).rstrip(), quote=False)
            return (
                '<figure class="visual-placeholder">'
                f'<figcaption><span>Figure placeholder</span>{title}</figcaption>'
                f"<pre>{code}</pre></figure>",
                index,
            )
        return (
            '<div class="visual-heading">'
            f'<span>Comparison</span>{title}</div>',
            index,
        )

    executive_match = re.fullmatch(
        r"\*\*(Executive question|Key message|Executive decision):\*\*\s*(.+)",
        first,
    )
    if executive_match:
        label = executive_match.group(1)
        value = executive_match.group(2)
        class_name = slugify(label)
        return (
            f'<aside class="executive-callout {class_name}">'
            f'<div class="executive-callout__label">{html.escape(label)}</div>'
            f'<div class="executive-callout__text">{render_inline(value)}</div>'
            "</aside>",
            index,
        )

    dialogue_match = re.fullmatch(r"\*\*(Customer|Teller):\*\*\s*(.+)", first)
    if dialogue_match:
        return (
            '<blockquote class="dialogue">'
            f'<span>{html.escape(dialogue_match.group(1))}</span>'
            f'<p>{render_inline(dialogue_match.group(2))}</p>'
            "</blockquote>",
            index,
        )

    plain = " ".join(part for part in quote_lines if part).strip()
    if clean_emphasis(plain) == "Proceed • Correct • Extend • Pause":
        return (
            '<blockquote class="decision-strip">'
            f"{render_inline(plain)}</blockquote>",
            index,
        )

    paragraphs: list[str] = []
    current: list[str] = []
    for part in quote_lines:
        if part:
            current.append(part)
        elif current:
            paragraphs.append(" ".join(current))
            current = []
    if current:
        paragraphs.append(" ".join(current))

    quote_html = "".join(f"<p>{render_inline(part)}</p>" for part in paragraphs)
    return f'<blockquote class="editorial-quote">{quote_html}</blockquote>', index


def render_paragraph(value: str, is_opening_lede: bool) -> str:
    plain = clean_emphasis(value)
    classes: list[str] = []
    if is_opening_lede:
        classes.append("opening-lede")
    if plain in PULL_QUOTES:
        classes.append("pull-quote")
    if value.startswith("Common software does not create a common bank."):
        classes.append("anchor-paragraph")

    rendered = render_inline(value)
    anchor = "Common software does not create a common bank."
    if value.startswith(anchor):
        rendered = rendered.replace(
            html.escape(anchor),
            f'<span class="anchor-sentence">{html.escape(anchor)}</span>',
            1,
        )

    class_attribute = f' class="{" ".join(classes)}"' if classes else ""
    return f"<p{class_attribute}>{rendered}</p>"


def render_manuscript(markdown: str) -> tuple[str, list[tuple[str, str]]]:
    lines = extract_publication_scope(markdown).splitlines()
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
            anchor = slugify(label)
            suffix = 2
            while anchor in used_ids:
                anchor = f"{slugify(label)}-{suffix}"
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
                if section_match:
                    number, title = section_match.groups()
                    running = f"SECTION {number} · {title.upper()}"
                    rendered.append(
                        f'<section class="major-section" id="{anchor}">'
                        f'<div class="section-number">Section {number}</div>'
                        f'<h2 data-running="{html.escape(running, quote=True)}">'
                        f"{render_inline(title)}</h2>"
                    )
                else:
                    rendered.append(
                        f'<section class="major-section executive-summary" id="{anchor}">'
                        f'<div class="section-number">Board briefing</div>'
                        f'<h2 data-running="EXECUTIVE SUMMARY">{render_inline(label)}</h2>'
                    )
            else:
                class_name = " section-summary" if label == "Section Summary" else ""
                rendered.append(
                    f'<h{level} id="{anchor}" class="subheading{class_name}">'
                    f"{render_inline(label)}</h{level}>"
                )
            index += 1
            continue

        if line.startswith(">"):
            block, index = render_quote(lines, index)
            rendered.append(block)
            continue

        if line.lstrip().startswith("|"):
            block, index = render_table(lines, index)
            rendered.append(block)
            continue

        if line.startswith("- "):
            items: list[str] = []
            while index < len(lines) and lines[index].startswith("- "):
                items.append(f"<li>{render_inline(lines[index][2:])}</li>")
                index += 1
            rendered.append(f'<ul class="editorial-list">{"".join(items)}</ul>')
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
                or next_line.lstrip().startswith("|")
                or next_line.startswith("```")
            ):
                break
            paragraph_lines.append(next_line)
            index += 1

        paragraph = " ".join(part.strip() for part in paragraph_lines)
        rendered.append(render_paragraph(paragraph, opening_paragraph_pending))
        opening_paragraph_pending = False

    if section_open:
        rendered.append("</section>")

    if current_section != "Section 7 — Launching the Program":
        raise ValueError("Publication did not terminate at Section 7 as expected.")

    return "\n".join(rendered), contents


def render_contents(contents: list[tuple[str, str]]) -> str:
    items: list[str] = []
    for label, anchor in contents:
        section_match = re.fullmatch(r"Section (\d+) — (.+)", label)
        if section_match:
            number, title = section_match.groups()
            display = (
                f'<span class="toc-number">{html.escape(number)}</span>'
                f'<span class="toc-title">{html.escape(title)}</span>'
            )
        else:
            display = (
                '<span class="toc-number">ES</span>'
                '<span class="toc-title">Executive Summary</span>'
            )
        items.append(f'<li><a href="#{anchor}">{display}</a></li>')
    return "\n".join(items)


def publication_html(markdown: str, canonical_source: str) -> str:
    if not STYLESHEET_PATH.is_file():
        raise FileNotFoundError(f"Program Guide stylesheet not found: {STYLESHEET_PATH}")
    if not LOGO_PATH.is_file():
        raise FileNotFoundError(f"Publication logo not found: {LOGO_PATH}")

    manuscript, contents = render_manuscript(markdown)
    stylesheet = STYLESHEET_PATH.read_text(encoding="utf-8")
    toc = render_contents(contents)
    logo_data = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    logo_uri = f"data:image/png;base64,{logo_data}"

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="x-change">
  <meta name="document-type" content="Banking Program Guide">
  <meta name="edition" content="{EDITION}">
  <meta name="canonical-source" content="{html.escape(canonical_source, quote=True)}">
  <title>{DOCUMENT_TITLE} — {DOCUMENT_FORM}</title>
  <style>
{stylesheet}
  </style>
</head>
<body>
  <section class="cover-page" aria-label="Cover">
    <div class="cover-frame">
      <div class="cover-kicker">{DOCUMENT_FORM}</div>
      <div class="cover-rule"></div>
      <h1>{DOCUMENT_TITLE}</h1>
      <p class="cover-subtitle">{SUBTITLE}</p>
      <div class="cover-edition">{EDITION}</div>
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

  <section class="version-page" aria-label="Copyright and document version">
    <div class="version-kicker">Publication record</div>
    <h1>{DOCUMENT_TITLE}</h1>
    <p class="version-subtitle">{DOCUMENT_FORM} · {SUBTITLE}</p>

    <dl class="publication-record">
      <div><dt>Edition</dt><dd>{EDITION}</dd></div>
      <div><dt>Publication date</dt><dd>{PUBLICATION_DATE}</dd></div>
      <div><dt>Prepared for</dt><dd>Rural Bankers Association of the Philippines</dd></div>
      <div><dt>Prepared by</dt><dd>x-change</dd></div>
      <div><dt>Edition scope</dt><dd>Executive Summary and Sections 1–7</dd></div>
      <div><dt>Canonical source</dt><dd>{html.escape(canonical_source)}</dd></div>
    </dl>

    <div class="copyright-note">
      <p>Copyright © 2026 x-change.</p>
      <p>This first typeset edition is prepared as a Board paper. Appendices and canonical program diagrams are reserved for a future edition.</p>
    </div>
  </section>

  <nav class="contents-page" aria-label="Table of contents">
    <div class="front-kicker">Program Guide</div>
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
        description="Publish the RBAP Digital Banking Program Guide as Edition 1 HTML and PDF."
    )
    parser.add_argument("source", type=Path)
    parser.add_argument("html_output", type=Path)
    parser.add_argument("--pdf", type=Path, dest="pdf_output")
    args = parser.parse_args()

    markdown = args.source.read_text(encoding="utf-8")
    rendered = publication_html(markdown, str(args.source))

    args.html_output.parent.mkdir(parents=True, exist_ok=True)
    args.html_output.write_text(rendered, encoding="utf-8")

    if args.pdf_output is not None:
        weasyprint = shutil.which("weasyprint")
        if weasyprint is None:
            raise RuntimeError("weasyprint executable not found on PATH.")
        args.pdf_output.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [weasyprint, str(args.html_output), str(args.pdf_output)],
            check=True,
        )


if __name__ == "__main__":
    main()
