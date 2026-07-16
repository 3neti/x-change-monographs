#!/usr/bin/env python3

from __future__ import annotations

import argparse
import html
import importlib.util
import re
from pathlib import Path
from types import ModuleType


DOCUMENT_TITLE = "Modernizing Public Finance Through Trusted Government Depository Banking"
SHORT_TITLE = "Trusted Government Depository Banking"
SUBTITLE = "A Strategic White Paper for Authorized Government Depository Banks in the Philippines"
MOVEMENT = "Movement IV"
EDITION = "First Edition"
VERSION = "1.2"
BASE_PUBLISHER = Path(__file__).with_name("publish-movement-iii-thrift-banks.py")


def load_house_publisher() -> ModuleType:
    spec = importlib.util.spec_from_file_location("xchange_house_publisher", BASE_PUBLISHER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load house publisher: {BASE_PUBLISHER}")

    publisher = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(publisher)
    return publisher


def render_inline(value: str) -> str:
    rendered: list[str] = []
    cursor = 0

    for match in re.finditer(r"\[([^\]]+)\]\((https?://[^)]+)\)", value):
        rendered.append(html.escape(value[cursor : match.start()], quote=False))
        label = html.escape(match.group(1), quote=False)
        target = html.escape(match.group(2), quote=True)
        rendered.append(f'<a href="{target}">{label}</a>')
        cursor = match.end()

    rendered.append(html.escape(value[cursor:], quote=False))
    joined = "".join(rendered)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", joined)


def configure_publisher(publisher: ModuleType) -> None:
    publisher.DOCUMENT_TITLE = DOCUMENT_TITLE
    publisher.SHORT_TITLE = SHORT_TITLE
    publisher.SUBTITLE = SUBTITLE
    publisher.MOVEMENT = MOVEMENT
    publisher.EDITION = EDITION
    publisher.VERSION = VERSION
    publisher.render_inline = render_inline


def apply_movement_iv_treatment(document: str) -> str:
    opening = render_inline(
        "Every peso entrusted to the Government of the Republic of the Philippines carries an expectation that extends far beyond accounting."
    )
    document = document.replace(f"<p>{opening}</p>", f'<p class="opening-lede">{opening}</p>')

    trust_sequence = [
        ("Public money deserves public trust.", "trust-sequence trust-sequence-start"),
        ("Trust requires accountability.", "trust-sequence"),
        ("Accountability requires evidence.", "trust-sequence"),
        ("Evidence requires modern infrastructure.", "trust-sequence trust-sequence-end"),
    ]
    for statement, classes in trust_sequence:
        rendered = render_inline(statement)
        document = document.replace(
            f"<p>{rendered}</p>",
            f'<p class="{classes}">{rendered}</p>',
        )

    shared_infrastructure = render_inline(
        "Technology can be shared without the institution becoming shared."
    )
    document = document.replace(
        f"<p>{shared_infrastructure}</p>",
        f'<p class="pull-quote">{shared_infrastructure}</p>',
    )

    closing_line = render_inline(
        "Modernizing them is an investment in public trust—and in the Republic itself."
    )
    document = document.replace(
        f"<p>{closing_line}</p>",
        f'<p class="closing-line">{closing_line}</p>',
    )

    document = document.replace(
        "Prepared for the executive leadership of<br>Philippine thrift banks",
        "Prepared for the leadership of<br>Authorized Government Depository Banks<br>and Philippine public-finance institutions",
    )
    document = document.replace(
        "Publish Movement III as print HTML.",
        "Publish Movement IV as print HTML.",
    )

    movement_styles = """
    .cover-title {
      max-width: 166mm;
      font-size: 27.5pt;
      line-height: 1.075;
    }

    .manuscript a {
      color: var(--ink);
      text-decoration-color: var(--rule);
      text-decoration-thickness: 0.45pt;
      text-underline-offset: 1.5pt;
    }

    .manuscript .trust-sequence {
      max-width: 118mm;
      margin: 0 auto 0.8mm;
      color: var(--ink);
      font-size: 10.9pt;
      font-style: italic;
      line-height: 1.28;
      text-align: center;
      hyphens: none;
      break-inside: avoid;
    }

    .manuscript .trust-sequence-start {
      margin-top: 6.5mm;
    }

    .manuscript .trust-sequence-end {
      margin-bottom: 6.5mm;
    }

    .manuscript h1[id="authorities-and-notes"] {
      break-before: page;
      margin-top: 14mm;
    }

    .manuscript h1[id="authorities-and-notes"] ~ ul {
      color: #45494d;
      font-size: 8.7pt;
      line-height: 1.38;
    }

    .manuscript .closing-line {
      margin-top: -0.28em;
      margin-bottom: 0;
      break-before: avoid;
    }

    .manuscript h1[id="movement-x-strengthening-the-institutions-of-public-trust"] ~ p {
      margin-bottom: 0.18em;
      line-height: 1.36;
    }
"""
    return document.replace("  </style>", f"{movement_styles}  </style>")


def publication_html(markdown: str, canonical_source: str) -> str:
    publisher = load_house_publisher()
    configure_publisher(publisher)
    document = publisher.publication_html(markdown, canonical_source)
    return apply_movement_iv_treatment(document)


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish Movement IV as print HTML.")
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    markdown = args.source.read_text(encoding="utf-8")
    rendered = publication_html(markdown, str(args.source))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
