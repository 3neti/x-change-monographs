#!/usr/bin/env python3

from __future__ import annotations

import argparse
import base64
import html
import importlib.util
import re
import shutil
import subprocess
from pathlib import Path


DOCUMENT_TITLE = "Thrift Bank Digital Banking Program"
DOCUMENT_FORM = "Program Guide"
SUBTITLE = "A Canonical Implementation Guide for Philippine Thrift Banks"
EDITION = "First Edition"
VERSION = "1.0"
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


def load_base_publisher():
    spec = importlib.util.spec_from_file_location("rbap_program_guide_publisher", BASE_PUBLISHER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load base Program Guide publisher: {BASE_PUBLISHER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE = load_base_publisher()


def render_inline(value: str) -> str:
    escaped = html.escape(value, quote=False)
    escaped = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", escaped)
    escaped = re.sub(r"`([^`]+)`", r'<code class="inline-code">\1</code>', escaped)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    return re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", escaped)


def extract_publication_scope(markdown: str) -> str:
    start_marker = "## Executive Summary"
    end_marker = "## Appendices"

    if start_marker not in markdown:
        raise ValueError("Executive Summary heading not found in canonical manuscript.")
    if end_marker not in markdown:
        raise ValueError("Appendices boundary not found in canonical manuscript.")

    scoped = markdown.split(start_marker, maxsplit=1)[1]
    scoped = f"{start_marker}\n{scoped.split(end_marker, maxsplit=1)[0].rstrip()}"

    if re.search(r"^## Appendix\b", scoped, flags=re.MULTILINE):
        raise ValueError("First Edition scope unexpectedly contains an appendix.")

    headings = re.findall(r"^## (.+)$", scoped, flags=re.MULTILINE)
    expected = ["Executive Summary"] + [f"Section {index}" for index in range(1, 8)]
    if len(headings) != len(expected):
        raise ValueError(f"Expected 8 major publication sections; found {len(headings)}.")
    for expected_prefix, heading in zip(expected, headings):
        if not heading.startswith(expected_prefix):
            raise ValueError(
                f"Unexpected publication sequence: expected {expected_prefix!r}, found {heading!r}."
            )

    return scoped


BASE.render_inline = render_inline
BASE.extract_publication_scope = extract_publication_scope
BASE.PULL_QUOTES = {
    "The bank brings the authority and the rails. x-change brings the operating grammar. The bank-specific driver connects them.",
    "The customer requested a banking outcome. The bank arranged it.",
}


def apply_publication_balance(manuscript: str) -> str:
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


def publication_html(markdown: str, canonical_source: str) -> str:
    if not STYLESHEET_PATH.is_file():
        raise FileNotFoundError(f"Program Guide stylesheet not found: {STYLESHEET_PATH}")
    if not LOGO_PATH.is_file():
        raise FileNotFoundError(f"Publication logo not found: {LOGO_PATH}")

    manuscript, contents = BASE.render_manuscript(markdown)
    manuscript = apply_publication_balance(manuscript)
    stylesheet = STYLESHEET_PATH.read_text(encoding="utf-8")
    toc = BASE.render_contents(contents)
    logo_data = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    logo_uri = f"data:image/png;base64,{logo_data}"

    thrift_overrides = """
@page version {
  @bottom-left { content: "THRIFT BANK DIGITAL BANKING PROGRAM"; }
}
@page contents {
  @bottom-left { content: "THRIFT BANK DIGITAL BANKING PROGRAM"; }
}
@page body {
  @bottom-left { content: "THRIFT BANK DIGITAL BANKING PROGRAM · FIRST EDITION"; }
}
.cover-page h1 { max-width: 148mm; font-size: 31pt; }
.cover-subtitle { max-width: 132mm; }
.inline-code {
  padding: 0.05em 0.24em;
  border-radius: 2px;
  background: var(--accent-soft);
  color: var(--ink);
  font-family: "SFMono-Regular", Consolas, monospace;
  font-size: 0.84em;
}
.standalone-code {
  width: 100%;
  padding: 4mm 7mm;
  border-left: 1.2pt solid var(--accent);
  background: var(--panel);
  font-size: 8.1pt;
  line-height: 1.34;
  text-align: center;
}
.publication-balance-break { break-before: page; }
"""

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="x-change">
  <meta name="document-type" content="Banking Program Guide">
  <meta name="edition" content="{EDITION}">
  <meta name="version" content="{VERSION}">
  <meta name="canonical-source" content="{html.escape(canonical_source, quote=True)}">
  <title>{DOCUMENT_TITLE} - {DOCUMENT_FORM}</title>
  <style>
{stylesheet}
{thrift_overrides}
  </style>
</head>
<body>
  <section class="cover-page" aria-label="Cover">
    <div class="cover-frame">
      <div class="cover-kicker">{DOCUMENT_FORM}</div>
      <div class="cover-rule"></div>
      <h1>{DOCUMENT_TITLE}</h1>
      <p class="cover-subtitle">{SUBTITLE}</p>
      <div class="cover-edition">{EDITION} · Version {VERSION}</div>
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
    <p class="version-subtitle">{DOCUMENT_FORM} · {SUBTITLE}</p>

    <dl class="publication-record">
      <div><dt>Edition</dt><dd>{EDITION}</dd></div>
      <div><dt>Version</dt><dd>{VERSION}</dd></div>
      <div><dt>Publication date</dt><dd>{PUBLICATION_DATE}</dd></div>
      <div><dt>Prepared by</dt><dd>x-change</dd></div>
      <div><dt>Edition scope</dt><dd>Executive Summary and Sections 1–7</dd></div>
      <div><dt>Canonical source</dt><dd>{html.escape(canonical_source)}</dd></div>
    </dl>

    <div class="copyright-note">
      <p>Copyright © 2026 x-change.</p>
      <p>This First Edition is prepared as an executive Board paper. Appendices A–G are reserved for a future Expanded Edition.</p>
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
        description="Publish the Thrift Bank Digital Banking Program Guide First Edition."
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
        subprocess.run([weasyprint, str(args.html_output), str(args.pdf_output)], check=True)


if __name__ == "__main__":
    main()
