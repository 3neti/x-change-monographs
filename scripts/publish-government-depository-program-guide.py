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
from pathlib import Path


DOCUMENT_TITLE = "Government Depository Digital Banking Program Guide"
DOCUMENT_FORM = "x-change Banking Program Guide"
SUBTITLE = "A Canonical Implementation Guide for Philippine Government Depository Institutions"
VERSION = "0.9"
PUBLICATION_STATUS = "Editorial Review Proof"
PUBLICATION_DATE = "July 2026"

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
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
TEMP_PDF_PATH = Path(tempfile.gettempdir()) / "x-change-monographs" / "pdfs"
MERMAID_CACHE_PATH = TEMP_PDF_PATH / "government-depository-review-proof-mermaid-cache"


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
BASE.BASE.PULL_QUOTES = {
    "The government entity brings lawful purpose and instruction. The depository institution brings banking authority and the approved rails. x-change brings the operating grammar. The institution-specific driver connects them.",
    "The public institution authorized an outcome. The depository institution arranged its accountable execution.",
}

EDITION = BASE.Edition(
    key="review-proof",
    label=PUBLICATION_STATUS,
    scope="Executive Summary, Sections 1–7, and Appendices A–G",
    expected_final_section="Appendix G — Canonical Diagrams",
    includes_appendices=True,
)


def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


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
    for expected_prefix, heading in zip(expected, headings):
        if not heading.startswith(expected_prefix):
            raise ValueError(
                f"Unexpected publication sequence: expected {expected_prefix!r}, "
                f"found {heading!r}."
            )
    return scoped


def review_scope(markdown: str, source: Path) -> str:
    scope = executive_scope(markdown)
    appendix_path = source.parent / "appendices"
    appendices: list[str] = []

    for filename in BASE.APPENDIX_FILES:
        path = appendix_path / filename
        if not path.is_file():
            raise FileNotFoundError(f"Canonical appendix not found: {path}")
        appendices.append(BASE.normalized_appendix(path.read_text(encoding="utf-8")))

    publication = "\n\n".join([scope, *appendices])
    headings = [
        line[3:]
        for line in publication.splitlines()
        if line.startswith("## ")
    ]
    expected = (
        ["Executive Summary"]
        + [f"Section {index}" for index in range(1, 8)]
        + [f"Appendix {letter}" for letter in "ABCDEFG"]
    )
    if len(headings) != len(expected):
        raise ValueError(
            f"Expected {len(expected)} major publication sections; found {len(headings)}."
        )
    for prefix, heading in zip(expected, headings):
        if not heading.startswith(prefix):
            raise ValueError(
                f"Unexpected publication sequence: expected {prefix!r}, found {heading!r}."
            )
    return publication


def publication_html(markdown: str, source: Path) -> str:
    if not STYLESHEET_PATH.is_file():
        raise FileNotFoundError(f"Program Guide stylesheet not found: {STYLESHEET_PATH}")
    if not LOGO_PATH.is_file():
        raise FileNotFoundError(f"Publication logo not found: {LOGO_PATH}")

    scope = review_scope(markdown, source)
    TEMP_PDF_PATH.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=TEMP_PDF_PATH) as temporary:
        manuscript, contents = BASE.render_manuscript(
            scope, EDITION, Path(temporary)
        )

    stylesheet = STYLESHEET_PATH.read_text(encoding="utf-8")
    toc = BASE.render_contents(contents)
    logo_data = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    logo_uri = f"data:image/png;base64,{logo_data}"
    source_hash = sha256(source.read_bytes())
    footer = "GOVERNMENT DEPOSITORY PROGRAM GUIDE · REVIEW PROOF · VERSION 0.9"

    overrides = f"""
@page version {{ @bottom-left {{ content: "{footer}"; }} }}
@page contents {{ @bottom-left {{ content: "{footer}"; }} }}
@page body {{ @bottom-left {{ content: "{footer}"; }} }}
.cover-page h1 {{ max-width: 153mm; font-size: 29pt; }}
.cover-subtitle {{ max-width: 142mm; font-style: normal; font-weight: 600; }}
.cover-proof-label {{
  margin-top: 8mm;
  color: var(--accent);
  font-family: "Avenir Next", Avenir, sans-serif;
  font-size: 7.4pt;
  font-weight: 600;
  letter-spacing: 0.14em;
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
  padding: 4mm 7mm;
  border-left: 1.2pt solid var(--accent);
  background: var(--panel);
  font-size: 8.1pt;
  line-height: 1.34;
  text-align: center;
}}
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
#appendix-b-governance .table-wrap {{
  break-inside: auto;
}}
#appendix-b-governance table {{
  font-size: 7.35pt;
  line-height: 1.28;
}}
#appendix-b-governance th {{
  padding: 2.2mm 2.7mm;
}}
#appendix-b-governance td {{
  padding: 1.8mm 2.7mm;
}}
#appendix-d-treasury-grammar h3.subheading {{
  margin-top: 6mm;
}}
#appendix-d-treasury-grammar .standalone-code {{
  padding: 3mm 5mm;
  line-height: 1.24;
}}
#appendix-d-treasury-grammar .editorial-list {{
  margin-top: 1mm;
  margin-bottom: 2mm;
}}
#appendix-d-treasury-grammar .editorial-list li {{
  margin-bottom: 0.55mm;
  padding-left: 0.5mm;
  line-height: 1.35;
}}
"""

    canonical_source = source.resolve().relative_to(REPOSITORY_ROOT)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="x-change">
  <meta name="document-type" content="Banking Program Guide">
  <meta name="publication-status" content="{PUBLICATION_STATUS}">
  <meta name="version" content="{VERSION}">
  <meta name="canonical-source" content="{html.escape(str(canonical_source), quote=True)}">
  <meta name="canonical-source-sha256" content="{source_hash}">
  <title>{DOCUMENT_TITLE} — Version {VERSION} Review Proof</title>
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
      <div class="cover-proof-label">Version {VERSION} · {PUBLICATION_STATUS}</div>
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

  <section class="version-page" aria-label="Publication information">
    <div class="version-kicker">Publication record</div>
    <h1>{DOCUMENT_TITLE}</h1>
    <p class="version-subtitle">{SUBTITLE}</p>

    <dl class="publication-record">
      <div><dt>Status</dt><dd>{PUBLICATION_STATUS}</dd></div>
      <div><dt>Version</dt><dd>{VERSION}</dd></div>
      <div><dt>Publication date</dt><dd>{PUBLICATION_DATE}</dd></div>
      <div><dt>Prepared by</dt><dd>x-change</dd></div>
      <div><dt>Proof scope</dt><dd>{EDITION.scope}</dd></div>
      <div><dt>Canonical source</dt><dd>{html.escape(str(canonical_source))}</dd></div>
      <div><dt>Source SHA-256</dt><dd><code>{source_hash}</code></dd></div>
    </dl>

    <div class="copyright-note">
      <p>Copyright © 2026 x-change.</p>
      <p>This artifact is an editorial review proof. It is not Version 1.0, a First Edition, a final publication, or a publication freeze record.</p>
      <p>The canonical Markdown and appendices remain the source of truth.</p>
    </div>
  </section>

  <nav class="contents-page" aria-label="Table of contents">
    <div class="front-kicker">Version {VERSION} · {PUBLICATION_STATUS}</div>
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
        description="Publish the Government Depository Program Guide review proof."
    )
    parser.add_argument("source", type=Path)
    parser.add_argument("html_output", type=Path)
    parser.add_argument("--pdf", type=Path, dest="pdf_output")
    args = parser.parse_args()

    source_before = args.source.read_bytes()
    markdown = source_before.decode("utf-8")
    rendered = publication_html(markdown, args.source)

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

    if args.source.read_bytes() != source_before:
        raise RuntimeError("Canonical manuscript changed during publication rendering.")


if __name__ == "__main__":
    main()
