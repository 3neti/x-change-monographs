#!/usr/bin/env python3

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path


TITLE = "Where Financial Activity Begins"
DOCUMENT_TYPE = "Executive Reading Note No. 001"
VERSION = "1.0"


def render_inline(value: str) -> str:
    escaped = html.escape(value, quote=False)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)


def render_blocks(markdown: str) -> str:
    lines = markdown.splitlines()
    rendered: list[str] = []
    index = 0

    while index < len(lines):
        line = lines[index]

        if not line.strip():
            index += 1
            continue

        if line == "---":
            rendered.append('<hr class="section-break">')
            index += 1
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            level = len(heading.group(1))
            rendered.append(f"<h{level}>{render_inline(heading.group(2))}</h{level}>")
            index += 1
            continue

        if line.startswith(">"):
            quote_lines: list[str] = []
            while index < len(lines) and (lines[index].startswith(">") or not lines[index].strip()):
                current = lines[index]
                if current.startswith(">"):
                    quote_lines.append(current[1:].lstrip())
                elif quote_lines and quote_lines[-1] != "":
                    quote_lines.append("")
                index += 1

            paragraphs = "\n".join(quote_lines).strip().split("\n\n")
            quote_body = "".join(
                f"<p>{render_inline(' '.join(part.splitlines()))}</p>"
                for part in paragraphs
                if part.strip()
            )
            rendered.append(f"<blockquote>{quote_body}</blockquote>")
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
            if (
                next_line == "---"
                or next_line.startswith(">")
                or next_line.startswith("- ")
                or re.match(r"^#{1,6}\s+", next_line)
            ):
                break
            paragraph_lines.append(next_line)
            index += 1

        paragraph = " ".join(part.strip() for part in paragraph_lines)
        rendered.append(f"<p>{render_inline(paragraph)}</p>")

    return "\n".join(rendered)


def publication_html(markdown: str, canonical_source: str) -> str:
    body = render_blocks(markdown)
    body = body.replace(
        "<p>What matters strategically is not the Pay Code itself, but the activity that may follow a trusted financial commitment.</p>",
        '<p class="transaction-gravity-opening">What matters strategically is not the Pay Code itself, but the activity that may follow a trusted financial commitment.</p>',
    )
    first_break = body.find('<hr class="section-break">')

    if first_break == -1:
        raise ValueError("The publication source must contain a masthead separator.")

    masthead = body[:first_break]
    article = body[first_break:]

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="document-type" content="Executive Reading Note">
  <meta name="version" content="{VERSION}">
  <meta name="canonical-source" content="{html.escape(canonical_source, quote=True)}">
  <title>{TITLE} — {DOCUMENT_TYPE}</title>
  <style>
    :root {{
      --ink: #17283b;
      --text: #25282c;
      --accent: #947553;
      --muted: #6e7479;
      --paper: #fffefa;
    }}

    @page {{
      size: A4;
      margin: 14mm 21mm 16mm;

      @bottom-left {{
        content: "WHERE FINANCIAL ACTIVITY BEGINS";
        color: var(--accent);
        font-family: "Avenir Next", Avenir, sans-serif;
        font-size: 6.5pt;
        font-weight: 500;
        letter-spacing: 0.08em;
      }}

      @bottom-center {{
        content: "VERSION 1.0";
        color: var(--muted);
        font-family: "Avenir Next", Avenir, sans-serif;
        font-size: 6.5pt;
        letter-spacing: 0.08em;
      }}

      @bottom-right {{
        content: "PAGE " counter(page) " OF " counter(pages);
        color: var(--muted);
        font-family: "Avenir Next", Avenir, sans-serif;
        font-size: 6.5pt;
        letter-spacing: 0.08em;
      }}
    }}

    * {{
      box-sizing: border-box;
    }}

    html {{
      background: #e8e8e6;
    }}

    body {{
      width: 210mm;
      margin: 0 auto;
      background: var(--paper);
      color: var(--text);
      font-family: "New York", Charter, Baskerville, Georgia, serif;
      font-size: 9.7pt;
      line-height: 1.34;
    }}

    .publication {{
      padding: 14mm 21mm 16mm;
    }}

    .masthead {{
      margin: 0 0 7mm;
      padding: 4mm 0 3mm;
      text-align: center;
    }}

    h1, h2, h3 {{
      color: var(--ink);
      margin: 0;
    }}

    h1 {{
      font-size: 25pt;
      font-weight: 600;
      letter-spacing: -0.018em;
      line-height: 1.06;
    }}

    h2 {{
      margin-top: 4mm;
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 8pt;
      font-weight: 600;
      letter-spacing: 0.13em;
      line-height: 1.25;
      text-transform: uppercase;
    }}

    h3 {{
      margin-top: 2.2mm;
      font-size: 10.5pt;
      font-style: italic;
      font-weight: 400;
      line-height: 1.25;
    }}

    .masthead p {{
      margin-top: 4.2mm;
      color: var(--accent);
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 7.3pt;
      letter-spacing: 0.12em;
      text-transform: uppercase;
    }}

    main p {{
      margin: 0 0 1.75mm;
      orphans: 3;
      widows: 3;
    }}

    main > p:first-of-type {{
      font-size: 10.2pt;
      line-height: 1.38;
    }}

    .section-break {{
      width: 13mm;
      height: 0;
      margin: 4mm auto;
      border: 0;
    }}

    .masthead + main > .section-break:first-child {{
      margin-top: 0;
    }}

    blockquote {{
      margin: 3mm 12mm 4mm;
      color: var(--ink);
      font-size: 10.8pt;
      line-height: 1.36;
      text-align: center;
      break-inside: avoid;
    }}

    blockquote p {{
      margin-bottom: 1mm;
    }}

    ul {{
      margin: 1.5mm 0 2mm 5mm;
      padding-left: 4mm;
    }}

    li {{
      margin-bottom: 0.8mm;
      padding-left: 1mm;
    }}

    main h3 {{
      margin: 0 0 2.4mm;
      font-size: 14pt;
      font-style: normal;
      font-weight: 600;
      text-align: left;
    }}

    strong {{
      color: var(--ink);
      font-weight: 600;
    }}

    .transaction-gravity-opening {{
      break-before: page;
    }}

    .screen-footer {{
      display: flex;
      justify-content: space-between;
      margin-top: 8mm;
      padding-top: 3mm;
      border-top: 0.35pt solid #d6d1c8;
      color: var(--muted);
      font-family: "Avenir Next", Avenir, sans-serif;
      font-size: 7pt;
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }}

    @media print {{
      html, body {{
        width: auto;
        background: white;
      }}

      .publication {{
        padding: 0;
      }}

      .screen-footer {{
        display: none;
      }}
    }}

    @media screen {{
      body {{
        min-height: 297mm;
        box-shadow: 0 1.5mm 7mm rgba(14, 24, 34, 0.16);
      }}
    }}
  </style>
</head>
<body>
  <article class="publication">
    <header class="masthead">
{masthead}
    </header>
    <main>
{article}
    </main>
    <footer class="screen-footer" aria-label="Publication metadata">
      <span>{TITLE}</span>
      <span>Version {VERSION}</span>
    </footer>
  </article>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish an Executive Reading Note as HTML.")
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    markdown = args.source.read_text(encoding="utf-8")
    rendered = publication_html(markdown, str(args.source))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
