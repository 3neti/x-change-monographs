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


PROGRAM_TITLE = "Thrift Bank Digital Banking Program"
DOCUMENT_TITLE = "AllBank Institution Edition"
EDITION = "Research Edition"
VERSION = "0.9"
PUBLICATION_DATE = "July 2026"
PUBLICATION_BASIS = "Prepared from Publicly Available Information"
SHORT_TITLE = "AllBank Institution Edition"

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
BASE_STYLESHEET_PATH = (
    REPOSITORY_ROOT
    / "resources"
    / "publication-assets"
    / "styles"
    / "program-guide.css"
)
EDITION_STYLESHEET_PATH = (
    REPOSITORY_ROOT
    / "resources"
    / "publication-assets"
    / "styles"
    / "institution-edition.css"
)
LOGO_PATH = (
    REPOSITORY_ROOT
    / "resources"
    / "publication-assets"
    / "brand"
    / "x-change-logo-orange.png"
)

PULL_QUOTE_PREFIXES = (
    "The question raised by this Research Edition is therefore not whether AllBank should become digital.",
    "The bank brings the authority and the rails.",
)

EVIDENCE_CLASSES = {
    "Observed.": "evidence-observed",
    "Inferred.": "evidence-inferred",
    "Recommended.": "evidence-recommended",
    "Unknown.": "evidence-unknown",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def slugify(value: str) -> str:
    ascii_value = value.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", ascii_value.lower()).strip("-")


def render_inline(value: str) -> str:
    escaped = html.escape(value, quote=False)
    escaped = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", escaped)
    escaped = re.sub(r"`([^`]+)`", r'<code class="inline-code">\1</code>', escaped)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    return re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", escaped)


def clean_emphasis(value: str) -> str:
    return value.replace("**", "").replace("*", "").strip()


def publication_parts(markdown: str) -> tuple[str, str]:
    notice_marker = "## Publication Status"
    foreword_marker = "## Foreword"

    if notice_marker not in markdown or foreword_marker not in markdown:
        raise ValueError("The frozen manuscript is missing required publication markers.")

    title_block = markdown.split("---", maxsplit=1)[0]
    required_identity = (
        "# Thrift Bank Digital Banking Program",
        "## AllBank Institution Edition",
        "### Research Edition",
        "Version 0.9",
    )
    for value in required_identity:
        if value not in title_block:
            raise ValueError(f"The frozen manuscript identity is incomplete: {value}")

    after_notice = markdown.split(notice_marker, maxsplit=1)[1]
    notice = after_notice.split("---", maxsplit=1)[0].strip()
    main = markdown.split(foreword_marker, maxsplit=1)[1]
    main = f"{foreword_marker}\n{main.strip()}"

    chapter_headings = re.findall(r"^# (Chapter \d+ — .+)$", main, flags=re.MULTILINE)
    expected = [f"Chapter {number}" for number in range(1, 8)]
    if len(chapter_headings) != len(expected):
        raise ValueError(f"Expected 7 chapters; found {len(chapter_headings)}.")
    for expected_prefix, heading in zip(expected, chapter_headings):
        if not heading.startswith(expected_prefix):
            raise ValueError(
                f"Unexpected chapter sequence: expected {expected_prefix}, found {heading}."
            )
    if "# Conclusion" not in main:
        raise ValueError("The frozen manuscript conclusion is missing.")

    return notice, main


def split_table_row(value: str) -> list[str]:
    return [cell.strip() for cell in value.strip().strip("|").split("|")]


def render_table(lines: list[str], index: int) -> tuple[str, int]:
    rows: list[list[str]] = []
    while index < len(lines) and lines[index].lstrip().startswith("|"):
        rows.append(split_table_row(lines[index]))
        index += 1

    if len(rows) < 2:
        raise ValueError("Markdown table is missing its separator row.")
    if not all(re.fullmatch(r":?-{3,}:?", cell) for cell in rows[1]):
        raise ValueError("Markdown table separator row is malformed.")

    header = "".join(f"<th>{render_inline(cell)}</th>" for cell in rows[0])
    body = "".join(
        "<tr>" + "".join(f"<td>{render_inline(cell)}</td>" for cell in row) + "</tr>"
        for row in rows[2:]
    )
    return (
        '<div class="table-wrap"><table><thead><tr>'
        f"{header}</tr></thead><tbody>{body}</tbody></table></div>",
        index,
    )


def paragraph_class(value: str, opening: bool) -> str:
    plain = clean_emphasis(value)
    classes: list[str] = []
    if opening:
        classes.append("opening-lede")
    for label, class_name in EVIDENCE_CLASSES.items():
        if plain.startswith(label):
            classes.extend(("evidence-statement", class_name))
            break
    if any(plain.startswith(prefix) for prefix in PULL_QUOTE_PREFIXES):
        classes.append("pull-quote")
    if plain == "The next step is therefore not immediate implementation.":
        classes.append("closing-anchor")
    if plain == "It is institutional dialogue.":
        classes.extend(("closing-anchor", "closing-anchor-final"))
    return f' class="{" ".join(classes)}"' if classes else ""


def render_blocks(lines: list[str], *, notice: bool = False) -> str:
    rendered: list[str] = []
    index = 0
    opening = False

    while index < len(lines):
        line = lines[index]
        if not line.strip() or line.strip() == "---":
            index += 1
            continue

        heading = re.match(r"^(#{3,4})\s+(.+)$", line)
        if heading:
            level = len(heading.group(1))
            label = heading.group(2).strip()
            rendered.append(
                f'<h{level - 1} class="notice-subheading">{render_inline(label)}</h{level - 1}>'
            )
            index += 1
            continue

        if line.lstrip().startswith("|"):
            table, index = render_table(lines, index)
            rendered.append(table)
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
            rendered.append(
                f'<pre class="standalone-code">{html.escape(chr(10).join(code_lines), quote=False)}</pre>'
            )
            continue

        paragraph_lines = [line]
        index += 1
        while index < len(lines) and lines[index].strip():
            next_line = lines[index]
            if (
                re.match(r"^#{1,4}\s+", next_line)
                or next_line.startswith("- ")
                or re.match(r"^\d+\. ", next_line)
                or next_line.lstrip().startswith("|")
                or next_line.startswith("```")
                or next_line.strip() == "---"
            ):
                break
            paragraph_lines.append(next_line)
            index += 1

        paragraph = " ".join(part.strip() for part in paragraph_lines)
        class_attribute = ' class="notice-paragraph"' if notice else paragraph_class(paragraph, opening)
        rendered.append(f"<p{class_attribute}>{render_inline(paragraph)}</p>")
        opening = False

    return "\n".join(rendered)


def render_main(markdown: str) -> tuple[str, list[tuple[str, str, str]]]:
    lines = markdown.splitlines()
    rendered: list[str] = []
    contents: list[tuple[str, str, str]] = []
    used_ids: set[str] = set()
    section_open = False
    opening_paragraph_pending = False
    index = 0

    while index < len(lines):
        line = lines[index]
        if not line.strip() or line.strip() == "---":
            index += 1
            continue

        major_match = re.match(r"^(#|##)\s+(Foreword|Executive Summary|Chapter \d+ — .+|Conclusion)$", line)
        if major_match:
            label = major_match.group(2)
            if section_open:
                rendered.append("</section>")
            section_open = True
            opening_paragraph_pending = True
            anchor = slugify(label)
            if anchor in used_ids:
                raise ValueError(f"Duplicate major-section anchor: {anchor}")
            used_ids.add(anchor)

            chapter_match = re.fullmatch(r"Chapter (\d+) — (.+)", label)
            if chapter_match:
                number, title = chapter_match.groups()
                marker = number
                display_title = title
                kicker = f"Chapter {number}"
                running = f"CHAPTER {number} · {title.upper()}"
                class_name = "major-section chapter-section"
            elif label == "Executive Summary":
                marker = "ES"
                display_title = label
                kicker = "Executive briefing"
                running = "EXECUTIVE SUMMARY"
                class_name = "major-section executive-summary"
            elif label == "Foreword":
                marker = "F"
                display_title = label
                kicker = "Research Edition"
                running = "FOREWORD"
                class_name = "major-section foreword-section"
            else:
                marker = "C"
                display_title = label
                kicker = "Closing assessment"
                running = "CONCLUSION"
                class_name = "major-section conclusion-section"

            contents.append((marker, display_title, anchor))
            rendered.append(
                f'<section class="{class_name}" id="{anchor}">'
                f'<div class="section-number">{html.escape(kicker)}</div>'
                f'<h1 data-running="{html.escape(running, quote=True)}">'
                f"{render_inline(display_title)}</h1>"
            )
            index += 1
            continue

        subheading = re.match(r"^(##|###)\s+(.+)$", line)
        if subheading:
            level = 2 if subheading.group(1) == "##" else 3
            label = subheading.group(2).strip()
            anchor = slugify(label)
            suffix = 2
            while anchor in used_ids:
                anchor = f"{slugify(label)}-{suffix}"
                suffix += 1
            used_ids.add(anchor)
            rendered.append(
                f'<h{level} id="{anchor}" class="subheading">{render_inline(label)}</h{level}>'
            )
            index += 1
            continue

        if line.lstrip().startswith("|"):
            table, index = render_table(lines, index)
            rendered.append(table)
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
                item = re.sub(r"^\d+\.\s+", "", lines[index])
                items.append(f"<li>{render_inline(item)}</li>")
                index += 1
            rendered.append(f'<ol class="editorial-list discussion-list">{"".join(items)}</ol>')
            continue

        if line.startswith("```"):
            index += 1
            code_lines: list[str] = []
            while index < len(lines) and not lines[index].startswith("```"):
                code_lines.append(lines[index])
                index += 1
            if index < len(lines):
                index += 1
            rendered.append(
                f'<pre class="standalone-code">{html.escape(chr(10).join(code_lines), quote=False)}</pre>'
            )
            continue

        paragraph_lines = [line]
        index += 1
        while index < len(lines) and lines[index].strip():
            next_line = lines[index]
            if (
                re.match(r"^#{1,3}\s+", next_line)
                or next_line.startswith("- ")
                or re.match(r"^\d+\. ", next_line)
                or next_line.lstrip().startswith("|")
                or next_line.startswith("```")
                or next_line.strip() == "---"
            ):
                break
            paragraph_lines.append(next_line)
            index += 1

        paragraph = " ".join(part.strip() for part in paragraph_lines)
        class_attribute = paragraph_class(paragraph, opening_paragraph_pending)
        rendered.append(f"<p{class_attribute}>{render_inline(paragraph)}</p>")
        opening_paragraph_pending = False

    if section_open:
        rendered.append("</section>")

    if len(contents) != 10:
        raise ValueError(f"Expected 10 major contents entries; found {len(contents)}.")
    return "\n".join(rendered), contents


def render_contents(contents: list[tuple[str, str, str]]) -> str:
    items: list[str] = []
    for marker, title, anchor in contents:
        display = (
            f'<span class="toc-number">{html.escape(marker)}</span>'
            f'<span class="toc-title">{html.escape(title)}</span>'
        )
        items.append(f'<li><a href="#{anchor}">{display}</a></li>')
    return "\n".join(items)


def publication_html(markdown: str, source: Path) -> str:
    for path in (BASE_STYLESHEET_PATH, EDITION_STYLESHEET_PATH, LOGO_PATH):
        if not path.is_file():
            raise FileNotFoundError(f"Required publication asset not found: {path}")

    notice_markdown, main_markdown = publication_parts(markdown)
    notice = render_blocks(notice_markdown.splitlines(), notice=True)
    manuscript, contents = render_main(main_markdown)
    toc = render_contents(contents)
    stylesheet = "\n".join(
        (
            BASE_STYLESHEET_PATH.read_text(encoding="utf-8"),
            EDITION_STYLESHEET_PATH.read_text(encoding="utf-8"),
        )
    )
    logo_data = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    logo_uri = f"data:image/png;base64,{logo_data}"
    source_display = source.relative_to(REPOSITORY_ROOT)

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="x-change">
  <meta name="description" content="AllBank Institution Edition Research Edition prepared from publicly available information">
  <meta name="document-type" content="Institution Edition">
  <meta name="edition" content="{EDITION}">
  <meta name="version" content="{VERSION}">
  <meta name="status" content="In Review">
  <meta name="source" content="{html.escape(str(source_display), quote=True)}">
  <title>{PROGRAM_TITLE} — {DOCUMENT_TITLE} — {EDITION}</title>
  <style>
{stylesheet}
  </style>
</head>
<body>
  <section class="cover-page institution-cover" aria-label="Cover">
    <div class="cover-frame">
      <div class="cover-kicker">Institution Edition</div>
      <div class="cover-rule"></div>
      <h1>{PROGRAM_TITLE}</h1>
      <p class="cover-subtitle">{DOCUMENT_TITLE}</p>
      <div class="cover-edition">{EDITION} · Version {VERSION}</div>
      <p class="cover-basis">{PUBLICATION_BASIS}</p>
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

  <section class="version-page" aria-label="Publication information and version">
    <div class="version-kicker">Publication information</div>
    <h1>{DOCUMENT_TITLE}</h1>
    <p class="version-subtitle">{PROGRAM_TITLE}</p>

    <dl class="publication-record">
      <div><dt>Edition</dt><dd>{EDITION}</dd></div>
      <div><dt>Version</dt><dd>{VERSION}</dd></div>
      <div><dt>Status</dt><dd>In Review</dd></div>
      <div><dt>Basis</dt><dd>{PUBLICATION_BASIS}</dd></div>
      <div><dt>Publication date</dt><dd>{PUBLICATION_DATE}</dd></div>
      <div><dt>Prepared by</dt><dd>x-change</dd></div>
      <div><dt>Editorial source</dt><dd>{html.escape(str(source_display))}</dd></div>
    </dl>

    <div class="copyright-note">
      <p>Copyright © 2026 x-change.</p>
      <p>This Research Edition supports executive discussion and institutional discovery. It is not a proposal, a Confirmed Edition, or an implementation plan.</p>
    </div>
  </section>

  <section class="editorial-notice-page" aria-label="Research Edition editorial notice">
    <div class="front-kicker">Research Edition</div>
    <h1>Editorial Notice</h1>
    <div class="editorial-notice">
{notice}
    </div>
  </section>

  <nav class="contents-page institution-contents" aria-label="Table of contents">
    <div class="front-kicker">{EDITION}</div>
    <h1>Contents</h1>
    <ol class="toc">
{toc}
    </ol>
  </nav>

  <main class="manuscript institution-manuscript">
{manuscript}
  </main>
</body>
</html>
"""


def pdf_page_count(path: Path) -> int:
    executable = shutil.which("pdfinfo")
    if executable is None:
        raise RuntimeError("pdfinfo not found on PATH.")
    result = subprocess.run(
        [executable, str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    match = re.search(r"^Pages:\s+(\d+)$", result.stdout, flags=re.MULTILINE)
    if match is None:
        raise RuntimeError("Unable to determine generated PDF page count.")
    return int(match.group(1))


def write_manifest(
    manifest_path: Path,
    source: Path,
    html_output: Path,
    pdf_output: Path | None,
) -> None:
    artifacts: dict[str, object] = {
        "html": {
            "path": str(html_output.relative_to(REPOSITORY_ROOT)),
            "sha256": sha256(html_output),
        }
    }
    page_count = None
    if pdf_output is not None:
        page_count = pdf_page_count(pdf_output)
        artifacts["pdf"] = {
            "path": str(pdf_output.relative_to(REPOSITORY_ROOT)),
            "sha256": sha256(pdf_output),
            "physical_pages": page_count,
        }

    manifest = {
        "program": PROGRAM_TITLE,
        "title": DOCUMENT_TITLE,
        "edition": EDITION,
        "version": VERSION,
        "status": "in_review",
        "publication_basis": PUBLICATION_BASIS,
        "publication_date": PUBLICATION_DATE,
        "source": {
            "path": str(source.relative_to(REPOSITORY_ROOT)),
            "sha256": sha256(source),
        },
        "artifacts": artifacts,
        "physical_page_count": page_count,
        "editorial_changes": False,
        "pdf_generated": pdf_output is not None,
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Publish the AllBank Institution Edition Research Edition."
    )
    parser.add_argument("source", type=Path)
    parser.add_argument("html_output", type=Path)
    parser.add_argument("--pdf", type=Path, dest="pdf_output")
    parser.add_argument("--manifest", type=Path, dest="manifest_output")
    args = parser.parse_args()

    source = args.source.resolve()
    html_output = args.html_output.resolve()
    pdf_output = args.pdf_output.resolve() if args.pdf_output is not None else None
    manifest_output = (
        args.manifest_output.resolve()
        if args.manifest_output is not None
        else html_output.parent / "publication-manifest.json"
    )

    markdown = source.read_text(encoding="utf-8")
    rendered = publication_html(markdown, source)
    html_output.parent.mkdir(parents=True, exist_ok=True)
    html_output.write_text(rendered, encoding="utf-8")

    if pdf_output is not None:
        weasyprint = shutil.which("weasyprint")
        if weasyprint is None:
            raise RuntimeError("weasyprint executable not found on PATH.")
        pdf_output.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [
                weasyprint,
                "--custom-metadata",
                str(html_output),
                str(pdf_output),
            ],
            check=True,
        )

    write_manifest(manifest_output, source, html_output, pdf_output)


if __name__ == "__main__":
    main()
