#!/usr/bin/env python3

from __future__ import annotations

import argparse
import html
import re
import unicodedata
from pathlib import Path


DOCUMENT_TITLE = "Modernizing Philippine Thrift Banks for the Digital Economy"
SHORT_TITLE = "Modernizing Thrift Banks"
SUBTITLE = "A Strategic White Paper for Philippine Thrift Banks"
MOVEMENT = "Movement III"
EDITION = "First Edition"
VERSION = "1.1"
LOGO_PATH = (
    Path(__file__).resolve().parent.parent
    / "resources"
    / "publication-assets"
    / "brand"
    / "x-change-logo-orange.png"
)


def render_inline(value: str) -> str:
    escaped = html.escape(value, quote=False)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", ascii_value.lower()).strip("-")


def source_body(markdown: str) -> str:
    separator = "\n---\n"
    if separator not in markdown:
        raise ValueError("The publication source must contain a masthead separator.")
    return markdown.split(separator, maxsplit=1)[1].strip()


def render_manuscript(markdown: str) -> tuple[str, list[tuple[str, str]]]:
    lines = source_body(markdown).splitlines()
    rendered: list[str] = []
    contents: list[tuple[str, str]] = []
    used_ids: set[str] = set()
    index = 0

    while index < len(lines):
        line = lines[index]

        if not line.strip():
            index += 1
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            level = len(heading.group(1))
            label = heading.group(2).strip()
            anchor = slugify(label)
            suffix = 2
            while anchor in used_ids:
                anchor = f"{slugify(label)}-{suffix}"
                suffix += 1
            used_ids.add(anchor)
            contents.append((label, anchor))
            heading_text = render_inline(label)
            if label == "Chapter 10 — Strengthening Institutions That Strengthen Communities":
                heading_text = heading_text.replace(
                    " That Strengthen Communities",
                    "<br>That Strengthen Communities",
                )
            rendered.append(f'<h{level} id="{anchor}">{heading_text}</h{level}>')
            index += 1
            continue

        if line.startswith("- "):
            items: list[str] = []
            while index < len(lines) and lines[index].startswith("- "):
                items.append(f"<li>{render_inline(lines[index][2:])}</li>")
                index += 1
            rendered.append(f"<ul>{''.join(items)}</ul>")
            continue

        paragraph_lines = [line]
        index += 1
        while index < len(lines) and lines[index].strip():
            next_line = lines[index]
            if next_line.startswith("- ") or re.match(r"^#{1,6}\s+", next_line):
                break
            paragraph_lines.append(next_line)
            index += 1

        paragraph = " ".join(part.strip() for part in paragraph_lines)
        classes: list[str] = []
        if paragraph == "This is not a paper about technology.":
            classes.append("opening-lede")
        if paragraph in {
            "Technology should adapt to financial institutions—not require institutions to reorganize themselves around technology.",
            "Technology can be shared without the bank becoming shared.",
        }:
            classes.append("pull-quote")
        class_attribute = f' class="{" ".join(classes)}"' if classes else ""
        rendered.append(f"<p{class_attribute}>{render_inline(paragraph)}</p>")

    return "\n".join(rendered), contents


def render_contents(contents: list[tuple[str, str]]) -> str:
    return "\n".join(
        f'<li><a href="#{anchor}">{html.escape(label)}</a></li>'
        for label, anchor in contents
    )


def publication_html(markdown: str, canonical_source: str) -> str:
    manuscript, contents = render_manuscript(markdown)
    toc = render_contents(contents)

    if not LOGO_PATH.is_file():
        raise FileNotFoundError(f"Publication logo not found: {LOGO_PATH}")

    logo_uri = LOGO_PATH.as_uri()

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="x-change">
  <meta name="document-type" content="Strategic White Paper">
  <meta name="movement" content="{MOVEMENT}">
  <meta name="edition" content="{EDITION}">
  <meta name="version" content="{VERSION}">
  <meta name="canonical-source" content="{html.escape(canonical_source, quote=True)}">
  <title>{DOCUMENT_TITLE}</title>
  <style>
    :root {{
      --ink: #17283b;
      --text: #25282c;
      --accent: #947553;
      --muted: #6e7479;
      --rule: #d8d2c8;
      --paper: #fffefa;
    }}

    @page cover {{
      size: A4;
      margin: 20mm 23mm;
    }}

    @page blank {{
      size: A4;
      margin: 0;
    }}

    @page title {{
      size: A4;
      margin: 24mm 25mm;
    }}

    @page contents {{
      size: A4;
      margin: 25mm 25mm 24mm;
    }}

    @page body {{
      size: A4;
      margin: 22mm 22mm 23mm;

      @bottom-center {{
        content: counter(page);
        color: var(--muted);
        font-family: "Avenir Next", Avenir, sans-serif;
        font-size: 7pt;
      }}
    }}

    @page body:left {{
      @top-left {{
        content: "{SHORT_TITLE.upper()}";
        color: var(--accent);
        font-family: "Avenir Next", Avenir, sans-serif;
        font-size: 6.7pt;
        font-weight: 500;
        letter-spacing: 0.09em;
      }}
    }}

    @page body:right {{
      @top-right {{
        content: "{SHORT_TITLE.upper()}";
        color: var(--accent);
        font-family: "Avenir Next", Avenir, sans-serif;
        font-size: 6.7pt;
        font-weight: 500;
        letter-spacing: 0.09em;
      }}
    }}

    @page:nth(5) {{
      counter-reset: page 1;
    }}

    * {{
      box-sizing: border-box;
    }}

    html, body {{
      margin: 0;
      padding: 0;
      background: var(--paper);
      color: var(--text);
    }}

    body {{
      font-family: Charter, Baskerville, Georgia, serif;
      font-size: 10.15pt;
      line-height: 1.44;
    }}

    .cover-page {{
      page: cover;
      height: 257mm;
      display: flex;
      flex-direction: column;
      position: relative;
      break-after: page;
    }}

    .cover-kicker {{
      margin-top: 17mm;
      color: var(--accent);
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 7.5pt;
      font-weight: 500;
      letter-spacing: 0.16em;
      text-align: center;
      text-transform: uppercase;
    }}

    .cover-rule {{
      width: 13mm;
      margin: 7mm auto 20mm;
      border-top: 0.5pt solid var(--accent);
    }}

    .cover-title {{
      max-width: 160mm;
      margin: 0 auto;
      color: var(--ink);
      font-family: Charter, Baskerville, Georgia, serif;
      font-size: 29.5pt;
      font-weight: 600;
      letter-spacing: -0.018em;
      line-height: 1.08;
      text-align: center;
      bookmark-level: none;
    }}

    .cover-subtitle {{
      max-width: 128mm;
      margin: 12mm auto 0;
      color: var(--muted);
      font-size: 12pt;
      font-style: italic;
      line-height: 1.38;
      text-align: center;
    }}

    .cover-version {{
      margin-top: 10mm;
      color: var(--accent);
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 7.3pt;
      letter-spacing: 0.12em;
      text-align: center;
      text-transform: uppercase;
    }}

    .cover-credit {{
      position: absolute;
      right: 0;
      bottom: 5mm;
      left: 0;
      text-align: center;
    }}

    .cover-credit-label {{
      display: block;
      margin-bottom: 2.8mm;
      color: var(--muted);
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 6.8pt;
      letter-spacing: 0.11em;
      text-transform: uppercase;
    }}

    .cover-brand {{
      font-size: 0;
      text-align: center;
      white-space: nowrap;
    }}

    .cover-logo {{
      display: inline-block;
      width: 6.2mm;
      height: auto;
      margin-right: 3mm;
      vertical-align: middle;
    }}

    .cover-wordmark {{
      display: inline-block;
      color: var(--ink);
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 12pt;
      font-weight: 600;
      letter-spacing: 0.015em;
      vertical-align: middle;
    }}

    .blank-verso {{
      page: blank;
      height: 297mm;
      break-after: page;
    }}

    .title-page {{
      page: title;
      height: 249mm;
      display: flex;
      flex-direction: column;
      break-after: page;
    }}

    .title-page__series {{
      margin-top: 24mm;
      color: var(--accent);
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 7.2pt;
      letter-spacing: 0.14em;
      text-transform: uppercase;
    }}

    .title-page h1 {{
      max-width: 150mm;
      margin: 12mm 0 0;
      color: var(--ink);
      font-family: Charter, Baskerville, Georgia, serif;
      font-size: 25pt;
      font-weight: 600;
      letter-spacing: -0.012em;
      line-height: 1.12;
    }}

    .title-page__subtitle {{
      max-width: 125mm;
      margin: 8mm 0 0;
      color: var(--muted);
      font-size: 11.5pt;
      font-style: italic;
      line-height: 1.4;
    }}

    .title-page__meta {{
      margin-top: auto;
      color: var(--muted);
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 8pt;
      line-height: 1.75;
    }}

    .title-page__meta strong {{
      color: var(--ink);
      font-weight: 600;
    }}

    .contents-page {{
      page: contents;
      min-height: 248mm;
      break-after: page;
    }}

    .contents-page h1 {{
      margin: 13mm 0 15mm;
      color: var(--ink);
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 18pt;
      font-weight: 500;
      letter-spacing: 0.02em;
    }}

    .toc {{
      margin: 0;
      padding: 0;
      list-style: none;
    }}

    .toc li {{
      margin: 0 0 5.4mm;
      break-inside: avoid;
    }}

    .toc a {{
      display: block;
      color: var(--text);
      font-size: 10.3pt;
      text-decoration: none;
    }}

    .toc a::after {{
      content: leader(".") target-counter(attr(href), page);
      color: var(--muted);
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 8pt;
    }}

    .manuscript {{
      page: body;
      text-align: justify;
      hyphens: auto;
    }}

    .manuscript p {{
      margin: 0 0 0.62em;
      orphans: 3;
      widows: 3;
    }}

    .manuscript .opening-lede {{
      margin-top: 8mm;
      color: var(--ink);
      font-size: 11.2pt;
      line-height: 1.42;
    }}

    .manuscript h1 {{
      margin: 11.5mm 0 5.2mm;
      color: var(--ink);
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 17pt;
      font-weight: 500;
      letter-spacing: -0.006em;
      line-height: 1.2;
      text-align: left;
      hyphens: none;
      break-after: avoid;
      orphans: 3;
      widows: 3;
      bookmark-level: 1;
    }}

    .manuscript strong {{
      color: var(--ink);
      font-weight: 600;
    }}

    .manuscript .pull-quote {{
      max-width: 128mm;
      margin: 7mm auto;
      color: var(--ink);
      font-size: 11.7pt;
      font-style: italic;
      line-height: 1.38;
      text-align: center;
      hyphens: none;
      break-inside: avoid;
    }}

    .manuscript ul {{
      margin: 0 0 0.8em 6mm;
      padding-left: 4mm;
      text-align: left;
    }}

    .manuscript li {{
      margin-bottom: 0.35em;
    }}
  </style>
</head>
<body>
  <section class="cover-page" aria-label="Cover">
    <div class="cover-kicker">{MOVEMENT}</div>
    <div class="cover-rule"></div>
    <h1 class="cover-title">{DOCUMENT_TITLE}</h1>
    <p class="cover-subtitle">{SUBTITLE}</p>
    <div class="cover-version">{EDITION} · Version {VERSION}</div>
    <div class="cover-credit">
      <span class="cover-credit-label">Prepared by</span>
      <div class="cover-brand">
        <img class="cover-logo" src="{logo_uri}" alt="x-change logo">
        <span class="cover-wordmark">x-change</span>
      </div>
    </div>
  </section>

  <section class="blank-verso" aria-label="Blank verso"></section>

  <section class="title-page" aria-label="Title page">
    <div class="title-page__series">The x-change Monographs · {MOVEMENT}</div>
    <h1>{DOCUMENT_TITLE}</h1>
    <p class="title-page__subtitle">{SUBTITLE}</p>
    <div class="title-page__meta">
      <div>Prepared for the executive leadership of<br>Philippine thrift banks</div>
      <div>Prepared by <strong>x-change</strong></div>
      <div>{EDITION}</div>
      <div>Version {VERSION}</div>
    </div>
  </section>

  <nav class="contents-page" aria-label="Table of contents">
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
    parser = argparse.ArgumentParser(description="Publish Movement III as print HTML.")
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    markdown = args.source.read_text(encoding="utf-8")
    rendered = publication_html(markdown, str(args.source))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
