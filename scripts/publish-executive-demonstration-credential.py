#!/usr/bin/env python3

from __future__ import annotations

import argparse
import base64
import copy
import hashlib
import html
import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import Optional

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = (
    REPOSITORY_ROOT
    / "docs"
    / "demonstrations"
    / "pay-code"
    / "executive-demonstration-credential-v1.0.md"
)
DEFAULT_OUTPUT_DIRECTORY = (
    REPOSITORY_ROOT
    / "build"
    / "demonstrations"
    / "pay-code"
    / "executive-demonstration-credential-v1.0"
)
DEFAULT_PDF_DIRECTORY = REPOSITORY_ROOT / "build" / "pdf"
DEFAULT_PACKAGE_DIRECTORY = (
    REPOSITORY_ROOT
    / "build"
    / "institutions"
    / "allbank"
    / "commercial"
    / "submission-package"
)
TITLE = "Executive Demonstration Credential"
INSTRUMENT_TYPE = "Demonstration Pay Code"
OUTPUT_STEM = "executive-demonstration-credential-v1.0"
EXPECTED_COVER_PDF_SHA256 = (
    "4394c671af5ef8d92c07e298207f62f2cea3b7ae472963f7c8fcf7aeda0d0baf"
)
EXPECTED_PROPOSAL_PDF_SHA256 = (
    "f387400b6c23fc5e51a32a641e02657031baf08e7301b599795a6345ce68396f"
)
EXPECTED_PROGRAM_GUIDE_PDF_SHA256 = (
    "a06b70cadcd5fa6c73b2ebb8e86acb7979731fc972da11039a5f29c988528210"
)

PROFILE_DIMENSIONS = {
    "executive-card": (150.0, 90.0),
    "business-card": (90.0, 55.0),
    "wallet-card": (85.60, 53.98),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require_executable(name: str) -> str:
    executable = shutil.which(name)
    if executable is None:
        raise RuntimeError(f"Required executable is unavailable: {name}")
    return executable


def parse_source(path: Path) -> tuple[dict[str, object], str]:
    markdown = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", markdown, re.DOTALL)
    if match is None:
        raise ValueError("Canonical Markdown must contain YAML front matter.")
    metadata = yaml.safe_load(match.group(1))
    if not isinstance(metadata, dict):
        raise ValueError("Canonical front matter must be a mapping.")
    return metadata, match.group(2)


def nested(metadata: dict[str, object], *keys: str) -> object:
    value: object = metadata
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            raise ValueError(f"Required metadata field is missing: {'.'.join(keys)}")
        value = value[key]
    return value


def deep_merge(base: dict[str, object], overrides: dict[str, object]) -> dict[str, object]:
    merged = copy.deepcopy(base)
    for key, value in overrides.items():
        existing = merged.get(key)
        if isinstance(value, dict) and isinstance(existing, dict):
            merged[key] = deep_merge(existing, value)
        else:
            merged[key] = copy.deepcopy(value)
    return merged


def recipient_slug(recipient: dict[str, object], index: int) -> str:
    name = str(recipient.get("name", "")).strip()
    if not name:
        return f"credential-{index:02d}"
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return slug or f"credential-{index:02d}"


def resolve_credentials(metadata: dict[str, object]) -> list[dict[str, object]]:
    raw_credentials = metadata.get("credentials")
    if not isinstance(raw_credentials, list) or not raw_credentials:
        raise ValueError("Canonical metadata must define one or more credentials.")

    shared_metadata = copy.deepcopy(metadata)
    shared_metadata.pop("credentials", None)
    resolved: list[dict[str, object]] = []
    slugs: set[str] = set()
    for index, overrides in enumerate(raw_credentials, start=1):
        if not isinstance(overrides, dict):
            raise ValueError(f"Credential {index} must be a mapping.")
        credential_metadata = deep_merge(shared_metadata, overrides)
        recipient = credential_metadata.get("recipient")
        if not isinstance(recipient, dict):
            raise ValueError(f"Credential {index} must define a recipient mapping.")
        slug = recipient_slug(recipient, index)
        if slug in slugs:
            raise ValueError(f"Credential recipient slugs must be unique: {slug}")
        slugs.add(slug)
        resolved.append(
            {
                "slug": slug,
                "recipient": copy.deepcopy(recipient),
                "metadata": credential_metadata,
            }
        )
    return resolved


def validate_source(metadata: dict[str, object], body: str) -> None:
    expected = {
        "document_type": "executive_demonstration_credential",
        "title": TITLE,
        "instrument_type": "demonstration_pay_code",
        "edition": "First Edition",
        "version": "1.0",
        "status": "approved",
        "layout": "executive-card",
        "orientation": "front-back",
        "currency": "PHP",
    }
    for field, value in expected.items():
        if metadata.get(field) != value:
            raise ValueError(f"Canonical field {field!r} must equal {value!r}.")

    if nested(metadata, "pay_code", "render_style") != "canonical-double-bars":
        raise ValueError("The Pay Code render style must be canonical-double-bars.")
    if nested(metadata, "instrument", "production_use") is not False:
        raise ValueError("The credential must remain unavailable for production use.")
    if nested(metadata, "render", "credentials_per_print_sheet") != 2:
        raise ValueError("The A4 print-sheet layout must contain two credential slots.")

    credentials = resolve_credentials(metadata)

    required_body = (
        "# Executive Demonstration Credential",
        "## Front",
        "Executive Demonstration",
        "Payments take seconds.",
        "Work takes days.",
        "Demonstration Pay Code",
        "Disbursable",
        "||                    ||",
        "Demonstration Value",
        "PHP 500",
        "## Back",
        "Scan the QR Code",
        "https://redeem-x.laravel.cloud/disburse",
        "1. Enter the Pay Code.",
        "2. Select **Redeem**.",
        "Prepared exclusively for this submission.",
        "Open Disbursement Technologies, Inc.",
    )
    for value in required_body:
        if value not in body:
            raise ValueError(f"Canonical body record is missing: {value}")

    for credential in credentials:
        recipient = credential["recipient"]
        if not isinstance(recipient, dict):
            raise ValueError("Resolved credential recipient is malformed.")
        for field in ("name", "title", "organization"):
            value = str(recipient.get(field, "")).strip()
            if value and value not in body:
                raise ValueError(
                    f"Canonical body is missing credential recipient {field}: {value}"
                )

    prohibited = (
        "demo card",
        "pay code stub",
        "sample voucher",
        "sample pay code",
        "three easy steps",
        "safe and secure",
    )
    lowered = body.lower()
    for value in prohibited:
        if value in lowered:
            raise ValueError(f"Prohibited demonstration wording found: {value}")


def resolve_asset(relative_path: object) -> Path:
    if not isinstance(relative_path, str) or not relative_path:
        raise ValueError("Asset path must be a non-empty string.")
    path = (REPOSITORY_ROOT / relative_path).resolve()
    if REPOSITORY_ROOT.resolve() not in path.parents:
        raise ValueError(f"Asset must remain inside the repository: {relative_path}")
    if not path.is_file():
        raise FileNotFoundError(f"Publication asset not found: {path}")
    return path


def verify_qr(qr_png: Path, expected_url: str) -> str:
    zbarimg = require_executable("zbarimg")
    result = subprocess.run(
        [zbarimg, "--quiet", "--raw", str(qr_png)],
        check=True,
        capture_output=True,
        text=True,
    )
    decoded = result.stdout.strip()
    if decoded != expected_url:
        raise ValueError(
            f"QR destination mismatch: expected {expected_url!r}, decoded {decoded!r}."
        )
    return decoded


def image_data_uri(path: Path) -> str:
    media_type = "image/png" if path.suffix.lower() == ".png" else "image/svg+xml"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{media_type};base64,{encoded}"


def xml(value: object) -> str:
    return html.escape(str(value), quote=True)


def normalized_pay_code(value: object) -> Optional[str]:
    if value is None:
        return None
    result = str(value).strip().upper()
    if not result:
        return None
    if "|" in result:
        raise ValueError("pay_code.value must not contain the renderer-owned double bars.")
    return result


def recipient_lines(metadata: dict[str, object]) -> list[str]:
    recipient = metadata.get("recipient")
    if not isinstance(recipient, dict):
        return []
    return [
        str(recipient.get(field, "")).strip()
        for field in ("name", "title", "organization")
        if str(recipient.get(field, "")).strip()
    ]


def common_svg_style() -> str:
    return """
      .sans { font-family: 'Avenir Next', 'Helvetica Neue', Arial, sans-serif; }
      .serif { font-family: Charter, Georgia, 'Times New Roman', serif; }
      .mono { font-family: 'SFMono-Regular', Menlo, Consolas, monospace; }
      .caps { letter-spacing: 3.4px; text-transform: uppercase; }
    """


def front_svg(
    metadata: dict[str, object],
    width_mm: float,
    height_mm: float,
    logo_uri: str,
) -> str:
    pay_code = normalized_pay_code(nested(metadata, "pay_code", "value"))
    demonstration_value = metadata.get("demonstration_value")
    currency = str(metadata.get("currency", "")).strip()
    recipient = recipient_lines(metadata)
    instruction = nested(metadata, "instrument", "instruction")
    version = metadata["version"]
    edition = metadata["edition"]
    compact = width_mm < 100
    top_label_size = 25 if compact else 20
    slogan_size = 28 if compact else 24
    section_label_size = 24 if compact else 19
    small_label_size = 20 if compact else 15
    lower_label_size = 22 if compact else 17
    recipient_detail_size = 26 if compact else 22
    footer_size = 20 if compact else 13
    has_value = demonstration_value not in (None, "")
    has_recipient = bool(recipient)
    has_optional_content = has_value or has_recipient
    pay_label_y = 390 if has_optional_content else 410
    pay_field_y = 410 if has_optional_content else 430
    pay_field_height = 132 if has_optional_content else 220
    pay_code_baseline = 492 if has_optional_content else 565

    if pay_code is None:
        pay_code_content = f"""
          <text x="136" y="{pay_code_baseline}" class="mono" font-size="54" font-weight="600" fill="#d55f18">||</text>
          <text x="1276" y="{pay_code_baseline}" class="mono" font-size="54" font-weight="600" fill="#d55f18">||</text>
        """
    else:
        pay_code_content = f"""
          <text x="136" y="{pay_code_baseline}" class="mono" font-size="54" font-weight="600" fill="#d55f18">||</text>
          <text x="750" y="{pay_code_baseline}" class="mono" font-size="62" font-weight="700" text-anchor="middle" letter-spacing="7" fill="#172533">{xml(pay_code)}</text>
          <text x="1276" y="{pay_code_baseline}" class="mono" font-size="54" font-weight="600" fill="#d55f18">||</text>
        """

    value_content = ""
    if has_value:
        value_content = f"""
          <text x="100" y="657" class="sans caps" font-size="{lower_label_size}" font-weight="700" fill="#68747e">Demonstration Value</text>
          <text x="100" y="722" class="serif" font-size="49" font-weight="700" fill="#172533">{xml(currency)} {xml(demonstration_value)}</text>
        """

    recipient_content = ""
    if has_recipient:
        name = recipient[0]
        remaining = recipient[1:]
        recipient_x = 760 if has_value else 100
        recipient_content = f"""
          <text x="{recipient_x}" y="657" class="sans caps" font-size="{lower_label_size}" font-weight="700" fill="#68747e">Prepared for</text>
          <text x="{recipient_x}" y="708" class="serif" font-size="38" font-weight="700" fill="#172533">{xml(name)}</text>
        """
        if remaining:
            recipient_content += (
                f'<text x="{recipient_x}" y="746" class="sans" font-size="{recipient_detail_size}" fill="#52606b">'
                + xml(" | ".join(remaining))
                + "</text>"
            )

    optional_divider = (
        '<line x1="100" y1="602" x2="1400" y2="602" stroke="#d2ccc2" stroke-width="2"/>'
        if has_optional_content
        else ""
    )
    description = (
        f"{INSTRUMENT_TYPE} with canonical double bars and a blank handwritten Pay Code area."
        if pay_code is None
        else f"{INSTRUMENT_TYPE} displaying the supplied Pay Code within canonical double bars."
    )

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width_mm:g}mm" height="{height_mm:g}mm" viewBox="0 0 1500 900" role="img" aria-labelledby="title desc">
  <title id="title">{TITLE} front</title>
  <desc id="desc">{xml(description)}</desc>
  <metadata>{xml(json.dumps(metadata, ensure_ascii=False, sort_keys=True))}</metadata>
  <style>{common_svg_style()}</style>
  <rect width="1500" height="900" rx="34" fill="#f7f3eb"/>
  <rect width="18" height="900" fill="#ef6c1a"/>
  <path d="M18 0H1500V18H18Z" fill="#ef6c1a"/>
  <text x="100" y="98" class="sans caps" font-size="{top_label_size}" font-weight="700" fill="#68747e">Executive Demonstration</text>
  <text x="100" y="178" class="sans" font-size="56" font-weight="700" fill="#172533">x-change</text>
  <text x="100" y="225" class="serif" font-size="{slogan_size}" font-style="italic" fill="#52606b">Payments take seconds. Work takes days.</text>
  <image href="{logo_uri}" x="1342" y="60" width="52" height="130" preserveAspectRatio="xMidYMid meet"/>
  <line x1="100" y1="274" x2="1400" y2="274" stroke="#d2ccc2" stroke-width="2"/>
  <text x="100" y="332" class="sans caps" font-size="{section_label_size}" font-weight="700" fill="#d55f18">Demonstration Pay Code</text>
  <text x="1400" y="315" class="sans caps" font-size="{small_label_size}" font-weight="700" text-anchor="end" fill="#68747e">Instruction</text>
  <text x="1400" y="348" class="serif" font-size="26" font-weight="700" text-anchor="end" fill="#172533">{xml(instruction)}</text>
  <text x="100" y="{pay_label_y}" class="sans caps" font-size="{small_label_size}" font-weight="700" fill="#68747e">Pay Code</text>
  <rect x="100" y="{pay_field_y}" width="1300" height="{pay_field_height}" rx="16" fill="#fffaf0" stroke="#d9d2c6" stroke-width="2"/>
  {pay_code_content}
  {optional_divider}
  {value_content}
  {recipient_content}
  <line x1="100" y1="812" x2="1400" y2="812" stroke="#d2ccc2" stroke-width="2"/>
  <text x="100" y="854" class="sans caps" font-size="{footer_size}" font-weight="700" fill="#68747e">Controlled demonstration | Not for production use</text>
  <text x="1400" y="854" class="sans caps" font-size="{footer_size}" font-weight="700" text-anchor="end" fill="#68747e">{xml(edition)} | Version {xml(version)}</text>
</svg>
'''


def back_svg(
    metadata: dict[str, object],
    width_mm: float,
    height_mm: float,
    logo_uri: str,
    qr_uri: str,
) -> str:
    redeem_url = nested(metadata, "redeem", "url")
    issuer = nested(metadata, "issuer", "organization")
    version = metadata["version"]
    compact = width_mm < 100
    top_label_size = 26 if compact else 20
    direction_size = 28 if compact else 23
    minor_size = 23 if compact else 18
    url_size = 28 if compact else 22
    step_size = 36 if compact else 30
    prepared_size = 24 if compact else 15
    issuer_label_size = 22 if compact else 14
    issuer_size = 32 if compact else 25
    footer_size = 21 if compact else 13

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width_mm:g}mm" height="{height_mm:g}mm" viewBox="0 0 1500 900" role="img" aria-labelledby="title desc">
  <title id="title">{TITLE} back</title>
  <desc id="desc">QR redemption direction for the {INSTRUMENT_TYPE}; scan or visit {xml(redeem_url)}.</desc>
  <metadata>{xml(json.dumps(metadata, ensure_ascii=False, sort_keys=True))}</metadata>
  <style>{common_svg_style()}</style>
  <defs><clipPath id="qr-clip"><rect x="100" y="144" width="450" height="450" rx="18"/></clipPath></defs>
  <rect width="1500" height="900" rx="34" fill="#172533"/>
  <rect x="0" y="0" width="18" height="900" fill="#ef6c1a"/>
  <text x="100" y="98" class="sans caps" font-size="{top_label_size}" font-weight="700" fill="#bec7cd">Executive Demonstration Credential</text>
  <image href="{logo_uri}" x="1342" y="58" width="52" height="130" preserveAspectRatio="xMidYMid meet"/>
  <rect x="100" y="144" width="450" height="450" rx="18" fill="#ffffff"/>
  <image href="{qr_uri}" x="100" y="144" width="450" height="450" preserveAspectRatio="xMidYMid meet" clip-path="url(#qr-clip)" aria-label="QR code for {xml(redeem_url)}"/>
  <text x="650" y="192" class="serif" font-size="64" font-weight="700" fill="#ffffff">Redeem</text>
  <text x="650" y="250" class="sans" font-size="{direction_size}" fill="#d7dde1">Scan the QR Code</text>
  <text x="650" y="294" class="sans" font-size="{minor_size}" fill="#8f9ca5">or visit</text>
  <text x="650" y="335" class="sans" font-size="{url_size}" font-weight="600" fill="#ef8a4a">{xml(redeem_url)}</text>
  <line x1="650" y1="390" x2="1400" y2="390" stroke="#43515c" stroke-width="2"/>
  <circle cx="675" cy="466" r="25" fill="#ef6c1a"/>
  <text x="675" y="474" class="sans" font-size="22" font-weight="700" text-anchor="middle" fill="#ffffff">1</text>
  <text x="725" y="475" class="serif" font-size="{step_size}" fill="#ffffff">Enter the Pay Code.</text>
  <circle cx="675" cy="541" r="25" fill="#ef6c1a"/>
  <text x="675" y="549" class="sans" font-size="22" font-weight="700" text-anchor="middle" fill="#ffffff">2</text>
  <text x="725" y="550" class="serif" font-size="{step_size}" fill="#ffffff">Select Redeem.</text>
  <line x1="100" y1="660" x2="1400" y2="660" stroke="#43515c" stroke-width="2"/>
  <text x="100" y="716" class="sans caps" font-size="{prepared_size}" font-weight="700" fill="#aeb8bf">Prepared exclusively for this submission.</text>
  <text x="100" y="766" class="sans caps" font-size="{issuer_label_size}" font-weight="700" fill="#7f8c95">Issued by</text>
  <text x="100" y="805" class="serif" font-size="{issuer_size}" font-weight="700" fill="#ffffff">{xml(issuer)}</text>
  <text x="1400" y="805" class="sans caps" font-size="{footer_size}" font-weight="700" text-anchor="end" fill="#aeb8bf">Demonstration only | Version {xml(version)}</text>
</svg>
'''


def write_svg_and_png(svg: str, svg_path: Path, png_path: Path, dimensions: tuple[float, float]) -> None:
    normalized_svg = "\n".join(line.rstrip() for line in svg.splitlines()) + "\n"
    svg_path.write_text(normalized_svg, encoding="utf-8")
    magick = require_executable("magick")
    width_px = round(dimensions[0] / 25.4 * 300)
    height_px = round(dimensions[1] / 25.4 * 300)
    subprocess.run(
        [
            magick,
            "-background",
            "none",
            "-density",
            "300",
            str(svg_path),
            "-resize",
            f"{width_px}x{height_px}!",
            "-strip",
            str(png_path),
        ],
        check=True,
    )


def pdf_html(
    title: str,
    svg_paths: list[Path],
    width_mm: float,
    height_mm: float,
    description: str,
) -> str:
    pages = "\n".join(
        f'<section class="page"><img src="{path.as_uri()}" alt="{html.escape(title)}"></section>'
        for path in svg_paths
    )
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="author" content="Open Disbursement Technologies, Inc.">
  <meta name="description" content="{html.escape(description, quote=True)}">
  <meta name="document-type" content="Executive Demonstration Credential">
  <meta name="version" content="1.0">
  <title>{html.escape(title)}</title>
  <style>
    @page {{ size: {width_mm:g}mm {height_mm:g}mm; margin: 0; }}
    * {{ box-sizing: border-box; }}
    html, body {{ margin: 0; padding: 0; }}
    .page {{ width: {width_mm:g}mm; height: {height_mm:g}mm; break-after: page; overflow: hidden; }}
    .page:last-child {{ break-after: auto; }}
    img {{ display: block; width: 100%; height: 100%; }}
  </style>
</head>
<body>{pages}</body>
</html>
'''


def print_sheet_html(credentials: list[dict[str, object]], slots_per_sheet: int) -> str:
    sheets = []
    for offset in range(0, len(credentials), slots_per_sheet):
        group = credentials[offset : offset + slots_per_sheet]
        for side in ("front", "back"):
            cards = []
            for credential in group:
                path = credential[f"{side}_svg"]
                recipient = credential["recipient"]
                if not isinstance(path, Path) or not isinstance(recipient, dict):
                    raise ValueError("Print-sheet credential paths are malformed.")
                name = str(recipient.get("name", "")).strip() or "Unpersonalized recipient"
                cards.append(
                    f'<div class="slot"><img src="{path.as_uri()}" '
                    f'alt="{side.title()} of credential for {html.escape(name, quote=True)}"></div>'
                )
            cards.extend(
                '<div class="slot empty" aria-hidden="true"></div>'
                for _ in range(slots_per_sheet - len(group))
            )
            label = side.upper()
            sheets.append(
                f'<section class="sheet" aria-label="{label} print sheet">'
                f'{"".join(cards)}<span>{label} | PRINT AT 100%</span></section>'
            )
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="author" content="Open Disbursement Technologies, Inc.">
  <meta name="description" content="A4 duplex print sheet for {len(credentials)} Executive Demonstration Credentials">
  <meta name="document-type" content="Executive Demonstration Credential Print Sheet">
  <meta name="version" content="1.0">
  <title>{TITLE} - A4 Duplex Print Sheet</title>
  <style>
    @page {{ size: A4 portrait; margin: 0; }}
    * {{ box-sizing: border-box; }}
    html, body {{ margin: 0; padding: 0; }}
    .sheet {{
      position: relative;
      width: 210mm;
      height: 297mm;
      padding-top: 51mm;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 15mm;
      break-after: page;
      background: #ffffff;
    }}
    .sheet:last-child {{ break-after: auto; }}
    .slot {{ position: relative; width: 150mm; height: 90mm; outline: 0.15mm solid #aaa49b; }}
    .slot img {{ display: block; width: 150mm; height: 90mm; }}
    .slot.empty {{ outline-color: transparent; }}
    .sheet span {{
      position: absolute;
      right: 10mm;
      bottom: 8mm;
      color: #8a8f93;
      font: 6.5pt 'Avenir Next', Arial, sans-serif;
      letter-spacing: 0.12em;
    }}
  </style>
</head>
<body>{''.join(sheets)}</body>
</html>
'''


def run_weasyprint(html_path: Path, pdf_path: Path, identifier: str) -> None:
    weasyprint = require_executable("weasyprint")
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            weasyprint,
            "--pdf-tags",
            "--srgb",
            "--custom-metadata",
            "--pdf-version",
            "1.7",
            "--full-fonts",
            "--hinting",
            "--pdf-identifier",
            identifier,
            str(html_path),
            str(pdf_path),
        ],
        check=True,
    )


def pdf_pages(path: Path) -> int:
    pdfinfo = require_executable("pdfinfo")
    result = subprocess.run(
        [pdfinfo, str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    match = re.search(r"^Pages:\s+(\d+)$", result.stdout, re.MULTILINE)
    if match is None:
        raise ValueError(f"Unable to determine PDF page count: {path}")
    return int(match.group(1))


def verify_raster_qr(path: Path, expected_url: str) -> None:
    decoded = verify_qr(path, expected_url)
    if decoded != expected_url:
        raise ValueError(f"Rendered QR verification failed: {path}")


def create_contact_sheet(credentials: list[dict[str, object]], output_path: Path) -> None:
    magick = require_executable("magick")
    source_path = output_path.with_name(f".{output_path.stem}-source.png")
    images: list[str] = []
    for credential in credentials:
        front_png = credential["front_png"]
        back_png = credential["back_png"]
        if not isinstance(front_png, Path) or not isinstance(back_png, Path):
            raise ValueError("Contact-sheet credential paths are malformed.")
        images.extend((str(front_png), str(back_png)))
    subprocess.run(
        [
            magick,
            "montage",
            *images,
            "-tile",
            "2x",
            "-geometry",
            "+36+36",
            "-background",
            "white",
            str(source_path),
        ],
        check=True,
    )
    try:
        subprocess.run(
            [
                magick,
                str(source_path),
                "-resize",
                "2400x",
                "-strip",
                str(output_path),
            ],
            check=True,
        )
    finally:
        source_path.unlink(missing_ok=True)


def protect_submission_artifacts(package_directory: Path) -> dict[str, str]:
    records = {
        "cover_letter": (
            package_directory / "01-cover-letter" / "AllBank-Cover-Letter.pdf",
            EXPECTED_COVER_PDF_SHA256,
        ),
        "commercial_proposal": (
            package_directory
            / "02-commercial-proposal"
            / "AllBank-Provisional-License-and-Proof-of-Concept.pdf",
            EXPECTED_PROPOSAL_PDF_SHA256,
        ),
        "program_guide": (
            package_directory
            / "03-attachment-a"
            / "Thrift-Bank-Digital-Banking-Program-Guide-AllBank-Edition.pdf",
            EXPECTED_PROGRAM_GUIDE_PDF_SHA256,
        ),
    }
    verified: dict[str, str] = {}
    for name, (path, expected_hash) in records.items():
        if not path.is_file() or sha256(path) != expected_hash:
            raise ValueError(f"Protected submission artifact changed or missing: {path}")
        verified[name] = expected_hash
    return verified


def update_submission_package(
    package_directory: Path,
    print_sheet_pdf: Path,
    credentials: list[dict[str, object]],
) -> list[Path]:
    demonstration_directory = package_directory / "04-demonstration-pay-codes"
    demonstration_directory.mkdir(parents=True, exist_ok=True)
    package_pdf = demonstration_directory / "AllBank-Executive-Demonstration-Credentials-Print-Sheet.pdf"
    readme = demonstration_directory / "README.md"
    package_readme = package_directory / "README.md"
    shutil.copy2(print_sheet_pdf, package_pdf)
    recipient_descriptions = []
    for credential in credentials:
        recipient = credential["recipient"]
        if not isinstance(recipient, dict):
            raise ValueError("Submission-package recipient metadata is malformed.")
        name = str(recipient.get("name", "")).strip()
        title = str(recipient.get("title", "")).strip()
        organization = str(recipient.get("organization", "")).strip()
        description = ", ".join(value for value in (name, title, organization) if value)
        recipient_descriptions.append(description or "unpersonalized recipient")
    recipients_text = "; and ".join(recipient_descriptions)
    readme.write_text(
        "# Executive Demonstration Credentials\n\n"
        "First Edition - Version 1.0\n\n"
        f"This A4 duplex print sheet contains {len(credentials)} Executive Demonstration "
        f"Credentials prepared for {recipients_text}. Each credential is a "
        "Demonstration Pay Code with a blank write-in area using the canonical double bars.\n\n"
        "Print at 100% without page scaling. Each front sheet is followed by its "
        "corresponding back sheet.\n",
        encoding="utf-8",
    )
    package_readme.write_text(
        "# AllBank submission package\n\n"
        "Proposal: ODTI-2026-001, Revision 1.0\n\n"
        "Submission Date: 20 July 2026\n\n"
        "The package contains the signed-ready Cover Letter, Commercial Proposal, "
        "unchanged Program Guide attachment, and an A4 duplex print sheet containing "
        "two Executive Demonstration Credentials. The credentials are controlled "
        "demonstration instruments and are not production credentials or instruments "
        "of value.\n",
        encoding="utf-8",
    )
    return [package_pdf, readme, package_readme]


def clean_generated_outputs(output_directory: Path, pdf_directory: Path) -> None:
    for pattern in (
        f"{OUTPUT_STEM}-*.svg",
        f"{OUTPUT_STEM}-*.png",
        f"{OUTPUT_STEM}-*.html",
    ):
        for path in output_directory.glob(pattern):
            path.unlink()
    for path in pdf_directory.glob(f"{OUTPUT_STEM}*.pdf"):
        path.unlink()


def artifact_record(path: Path, kind: str, **extra: object) -> dict[str, object]:
    record: dict[str, object] = {
        "kind": kind,
        "path": str(path.relative_to(REPOSITORY_ROOT)),
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
    }
    record.update(extra)
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish the Executive Demonstration Credential.")
    parser.add_argument("source", type=Path, nargs="?", default=DEFAULT_SOURCE)
    parser.add_argument("--output-directory", type=Path, default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--pdf-directory", type=Path, default=DEFAULT_PDF_DIRECTORY)
    parser.add_argument("--package-directory", type=Path, default=DEFAULT_PACKAGE_DIRECTORY)
    args = parser.parse_args()

    source = args.source.resolve()
    output_directory = args.output_directory.resolve()
    pdf_directory = args.pdf_directory.resolve()
    package_directory = args.package_directory.resolve()
    output_directory.mkdir(parents=True, exist_ok=True)
    pdf_directory.mkdir(parents=True, exist_ok=True)

    source_hash_before = sha256(source)
    metadata, body = parse_source(source)
    validate_source(metadata, body)
    credentials = resolve_credentials(metadata)
    protected_artifacts = protect_submission_artifacts(package_directory)

    logo_path = resolve_asset(nested(metadata, "branding", "logo"))
    qr_asset_path = resolve_asset(nested(metadata, "redeem", "qr"))
    redeem_url = str(nested(metadata, "redeem", "url"))
    qr_hash_before = sha256(qr_asset_path)
    decoded_qr_url = verify_qr(qr_asset_path, redeem_url)
    logo_uri = image_data_uri(logo_path)
    qr_uri = image_data_uri(qr_asset_path)
    clean_generated_outputs(output_directory, pdf_directory)

    artifacts: list[dict[str, object]] = []
    rendered_credentials: list[dict[str, object]] = []
    for credential in credentials:
        slug = str(credential["slug"])
        recipient = credential["recipient"]
        credential_metadata = credential["metadata"]
        if not isinstance(recipient, dict) or not isinstance(credential_metadata, dict):
            raise ValueError("Resolved credential metadata is malformed.")
        recipient_name = str(recipient.get("name", "")).strip() or slug
        profile_records: dict[str, dict[str, Path]] = {}

        for profile, dimensions in PROFILE_DIMENSIONS.items():
            profile_paths: dict[str, Path] = {}
            artifact_stem = f"{OUTPUT_STEM}-{slug}-{profile}"
            for side, renderer in (("front", front_svg), ("back", back_svg)):
                svg_path = output_directory / f"{artifact_stem}-{side}.svg"
                png_path = output_directory / f"{artifact_stem}-{side}.png"
                if side == "front":
                    svg = renderer(credential_metadata, *dimensions, logo_uri)
                else:
                    svg = renderer(credential_metadata, *dimensions, logo_uri, qr_uri)
                    if f">{xml(redeem_url)}</text>" not in svg:
                        raise ValueError(
                            "The printed redemption URL does not exactly match canonical metadata."
                        )
                write_svg_and_png(svg, svg_path, png_path, dimensions)
                profile_paths[f"{side}_svg"] = svg_path
                profile_paths[f"{side}_png"] = png_path
                artifacts.append(
                    artifact_record(
                        svg_path,
                        "recipient_svg",
                        recipient=recipient_name,
                        recipient_slug=slug,
                        profile=profile,
                        side=side,
                    )
                )
                artifacts.append(
                    artifact_record(
                        png_path,
                        "recipient_png",
                        recipient=recipient_name,
                        recipient_slug=slug,
                        profile=profile,
                        side=side,
                        dpi=300,
                    )
                )
            profile_records[profile] = profile_paths

            html_path = output_directory / f"{artifact_stem}.html"
            pdf_path = pdf_directory / f"{artifact_stem}.pdf"
            html_path.write_text(
                pdf_html(
                    f"{TITLE} - {recipient_name} - {profile}",
                    [profile_paths["front_svg"], profile_paths["back_svg"]],
                    *dimensions,
                    f"Front and back of the {TITLE} for {recipient_name}, {profile} profile.",
                ),
                encoding="utf-8",
            )
            run_weasyprint(
                html_path,
                pdf_path,
                f"urn:odti:executive-demonstration-credential:1.0:{slug}:{profile}",
            )
            if pdf_pages(pdf_path) != 2:
                raise ValueError(f"Credential PDF must contain exactly two pages: {pdf_path}")
            artifacts.append(
                artifact_record(
                    html_path,
                    "recipient_html",
                    recipient=recipient_name,
                    recipient_slug=slug,
                    profile=profile,
                )
            )
            artifacts.append(
                artifact_record(
                    pdf_path,
                    "recipient_pdf",
                    recipient=recipient_name,
                    recipient_slug=slug,
                    profile=profile,
                    pages=2,
                )
            )

        recipient_publication_pdf = pdf_directory / f"{OUTPUT_STEM}-{slug}.pdf"
        shutil.copy2(
            pdf_directory / f"{OUTPUT_STEM}-{slug}-executive-card.pdf",
            recipient_publication_pdf,
        )
        artifacts.append(
            artifact_record(
                recipient_publication_pdf,
                "recipient_publication_pdf",
                recipient=recipient_name,
                recipient_slug=slug,
                profile="executive-card",
                pages=2,
            )
        )
        rendered_credentials.append(
            {
                "slug": slug,
                "recipient": recipient,
                "metadata": credential_metadata,
                "profiles": profile_records,
            }
        )

    combined_page_count = len(rendered_credentials) * 2
    for profile, dimensions in PROFILE_DIMENSIONS.items():
        combined_svg_paths: list[Path] = []
        for credential in rendered_credentials:
            profiles = credential["profiles"]
            if not isinstance(profiles, dict):
                raise ValueError("Rendered credential profile records are malformed.")
            profile_paths = profiles[profile]
            combined_svg_paths.extend(
                (profile_paths["front_svg"], profile_paths["back_svg"])
            )
        html_path = output_directory / f"{OUTPUT_STEM}-{profile}.html"
        pdf_path = pdf_directory / f"{OUTPUT_STEM}-{profile}.pdf"
        html_path.write_text(
            pdf_html(
                f"{TITLE} Set - {profile}",
                combined_svg_paths,
                *dimensions,
                f"Credential set containing {len(rendered_credentials)} personalized "
                f"{TITLE} publications, {profile} profile.",
            ),
            encoding="utf-8",
        )
        run_weasyprint(
            html_path,
            pdf_path,
            f"urn:odti:executive-demonstration-credential:1.0:set:{profile}",
        )
        if pdf_pages(pdf_path) != combined_page_count:
            raise ValueError(
                f"Credential-set PDF must contain {combined_page_count} pages: {pdf_path}"
            )
        artifacts.append(
            artifact_record(
                html_path,
                "credential_set_html",
                profile=profile,
                credentials=len(rendered_credentials),
            )
        )
        artifacts.append(
            artifact_record(
                pdf_path,
                "credential_set_pdf",
                profile=profile,
                credentials=len(rendered_credentials),
                pages=combined_page_count,
            )
        )

    validation_metadata = copy.deepcopy(credentials[0]["metadata"])
    if not isinstance(validation_metadata, dict):
        raise ValueError("Validation credential metadata is malformed.")
    validation_metadata["pay_code"]["value"] = None
    validation_metadata["demonstration_value"] = None
    validation_metadata["recipient"] = {}
    validation_directory = output_directory / "validation"
    validation_directory.mkdir(parents=True, exist_ok=True)
    validation_svg_path = validation_directory / f"{OUTPUT_STEM}-blank-optional-fields-front.svg"
    validation_png_path = validation_directory / f"{OUTPUT_STEM}-blank-optional-fields-front.png"
    validation_svg = front_svg(
        validation_metadata,
        *PROFILE_DIMENSIONS["executive-card"],
        logo_uri,
    )
    validation_failures = []
    if validation_svg.count(">||</text>") != 2:
        validation_failures.append("canonical double bars")
    if '<line x1="275"' in validation_svg or 'stroke="#b8afa1"' in validation_svg:
        validation_failures.append("blank-field divider or handwriting line")
    if ">Demonstration Value</text>" in validation_svg or ">PHP " in validation_svg:
        validation_failures.append("hidden Demonstration Value block")
    if ">Prepared for</text>" in validation_svg:
        validation_failures.append("hidden recipient block")
    if '<line x1="100" y1="602"' in validation_svg:
        validation_failures.append("reserved optional-content divider")
    if 'y="430" width="1300" height="220"' not in validation_svg:
        validation_failures.append("balanced collapsed blank-field layout")
    if validation_failures:
        raise ValueError(
            "Blank optional-field validation failed: " + ", ".join(validation_failures)
        )
    write_svg_and_png(
        validation_svg,
        validation_svg_path,
        validation_png_path,
        PROFILE_DIMENSIONS["executive-card"],
    )
    artifacts.append(
        artifact_record(
            validation_svg_path,
            "validation_svg",
            test_case="blank_pay_code_value_recipient",
            submission_package=False,
        )
    )
    artifacts.append(
        artifact_record(
            validation_png_path,
            "validation_png",
            test_case="blank_pay_code_value_recipient",
            submission_package=False,
            dpi=300,
        )
    )

    publication_pdf = pdf_directory / f"{OUTPUT_STEM}.pdf"
    shutil.copy2(pdf_directory / f"{OUTPUT_STEM}-executive-card.pdf", publication_pdf)
    artifacts.append(
        artifact_record(
            publication_pdf,
            "publication_pdf",
            profile="executive-card",
            credentials=len(rendered_credentials),
            pages=combined_page_count,
        )
    )

    print_html_path = output_directory / f"{OUTPUT_STEM}-print-sheet.html"
    print_pdf_path = pdf_directory / f"{OUTPUT_STEM}-print-sheet.pdf"
    print_sheet_credentials: list[dict[str, object]] = []
    for credential in rendered_credentials:
        profiles = credential["profiles"]
        if not isinstance(profiles, dict):
            raise ValueError("Rendered credential profile records are malformed.")
        executive_paths = profiles["executive-card"]
        print_sheet_credentials.append(
            {
                "recipient": credential["recipient"],
                "front_svg": executive_paths["front_svg"],
                "back_svg": executive_paths["back_svg"],
                "front_png": executive_paths["front_png"],
                "back_png": executive_paths["back_png"],
            }
        )
    slots_per_sheet = int(nested(metadata, "render", "credentials_per_print_sheet"))
    print_html_path.write_text(
        print_sheet_html(print_sheet_credentials, slots_per_sheet),
        encoding="utf-8",
    )
    run_weasyprint(
        print_html_path,
        print_pdf_path,
        "urn:odti:executive-demonstration-credential:1.0:a4-duplex-print-sheet",
    )
    sheet_count = (len(rendered_credentials) + slots_per_sheet - 1) // slots_per_sheet
    print_page_count = sheet_count * 2
    if pdf_pages(print_pdf_path) != print_page_count:
        raise ValueError(
            f"The duplex print sheet must contain {print_page_count} A4 pages."
        )
    artifacts.append(
        artifact_record(
            print_html_path,
            "html",
            profile="a4-duplex",
            credentials=len(rendered_credentials),
            sheets=sheet_count,
        )
    )
    artifacts.append(
        artifact_record(
            print_pdf_path,
            "print_sheet_pdf",
            profile="a4-duplex",
            pages=print_page_count,
            credentials=len(rendered_credentials),
            sheets=sheet_count,
        )
    )

    contact_sheet_path = output_directory / f"{OUTPUT_STEM}-contact-sheet.png"
    create_contact_sheet(print_sheet_credentials, contact_sheet_path)
    artifacts.append(
        artifact_record(
            contact_sheet_path,
            "contact_sheet_png",
            credentials=len(rendered_credentials),
        )
    )

    for credential in rendered_credentials:
        profiles = credential["profiles"]
        if not isinstance(profiles, dict):
            raise ValueError("Rendered credential profile records are malformed.")
        for profile in PROFILE_DIMENSIONS:
            verify_raster_qr(profiles[profile]["back_png"], redeem_url)

    package_paths = update_submission_package(
        package_directory,
        print_pdf_path,
        rendered_credentials,
    )
    for path in package_paths:
        artifacts.append(artifact_record(path, "submission_package"))

    if sha256(source) != source_hash_before:
        raise RuntimeError("Canonical Markdown changed during publication.")
    if sha256(qr_asset_path) != qr_hash_before:
        raise RuntimeError("Supplied QR artwork changed during publication.")
    verified_after = protect_submission_artifacts(package_directory)
    if verified_after != protected_artifacts:
        raise RuntimeError("A protected submission artifact changed during publication.")

    manifest_path = output_directory / "publication-manifest.json"
    checksum_path = output_directory / "SHA256SUMS.txt"
    report_path = output_directory / "render-verification-report.md"
    manifest = {
        "title": TITLE,
        "document_type": metadata["document_type"],
        "instrument_type": metadata["instrument_type"],
        "edition": metadata["edition"],
        "version": metadata["version"],
        "status": metadata["status"],
        "canonical_source": str(source.relative_to(REPOSITORY_ROOT)),
        "canonical_source_sha256": source_hash_before,
        "credential_model": {
            "mode": "collection",
            "inheritance": "shared publication metadata with per-credential deep overrides",
        },
        "credential_count": len(rendered_credentials),
        "credentials": [
            {
                "slug": credential["slug"],
                "recipient": credential["recipient"],
            }
            for credential in rendered_credentials
        ],
        "issuer": metadata["issuer"],
        "pay_code": {
            "supplied": normalized_pay_code(nested(metadata, "pay_code", "value")) is not None,
            "handwritten": nested(metadata, "pay_code", "handwritten"),
            "render_style": nested(metadata, "pay_code", "render_style"),
        },
        "demonstration_value": metadata.get("demonstration_value"),
        "currency": metadata.get("currency"),
        "redemption": {
            "url": redeem_url,
            "qr_asset": str(qr_asset_path.relative_to(REPOSITORY_ROOT)),
            "qr_asset_sha256": qr_hash_before,
            "supplied_artwork": True,
            "decoded_url": decoded_qr_url,
            "verified": True,
            "printed_url_matches_metadata": True,
        },
        "renderer": {
            "script": str(Path(__file__).resolve().relative_to(REPOSITORY_ROOT)),
            "svg_master": "Native SVG",
            "rasterizer": "ImageMagick at 300 dpi",
            "pdf_engine": "WeasyPrint",
        },
        "profiles": {
            name: {"width_mm": dimensions[0], "height_mm": dimensions[1]}
            for name, dimensions in PROFILE_DIMENSIONS.items()
        },
        "protected_submission_artifacts": protected_artifacts,
        "print_sheet_personalization": {
            "recipients": [
                credential["recipient"] for credential in rendered_credentials
            ],
            "credentials": len(rendered_credentials),
            "distinct_recipients": len(rendered_credentials),
            "credentials_per_sheet": slots_per_sheet,
            "sheet_count": sheet_count,
            "basis": "canonical Markdown credential collection",
        },
        "renderer_validation": {
            "test_case": "blank pay_code.value, demonstration_value, and recipient",
            "canonical_double_bars": True,
            "blank_field_has_no_divider_or_guide": True,
            "demonstration_value_block_hidden": True,
            "recipient_block_hidden": True,
            "optional_space_collapsed": True,
            "submission_package": False,
        },
        "artifacts": artifacts,
        "accessibility": {
            "svg_titles_and_descriptions": True,
            "html_language": "en",
            "pdf_tags_requested": True,
            "qr_text_alternative": redeem_url,
        },
    }
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    checksum_records = [source, logo_path, qr_asset_path]
    checksum_records.extend(
        REPOSITORY_ROOT / record["path"]
        for record in artifacts
        if isinstance(record.get("path"), str)
    )
    checksum_records.append(manifest_path)
    unique_checksum_records = list(dict.fromkeys(checksum_records))
    checksum_path.write_text(
        "".join(
            f"{sha256(path)}  {path.relative_to(REPOSITORY_ROOT)}\n"
            for path in unique_checksum_records
        ),
        encoding="utf-8",
    )
    report_path.write_text(
        "# Render Verification Report\n\n"
        f"- Publication: {TITLE}, {metadata['edition']}, Version {metadata['version']}\n"
        f"- Instrument type: {INSTRUMENT_TYPE}\n"
        f"- Canonical source SHA-256: `{source_hash_before}`\n"
        f"- Pay Code presentation: `|| {{PAY CODE}} ||`; blank write-in field rendered\n"
        f"- Demonstration Value: {metadata.get('currency')} {metadata.get('demonstration_value')}\n"
        f"- QR destination: `{decoded_qr_url}`\n"
        f"- Supplied QR artwork SHA-256: `{qr_hash_before}`; unchanged during publication\n"
        f"- Credential set: {len(rendered_credentials)} recipients - "
        + "; ".join(
            str(credential["recipient"].get("name", ""))
            for credential in rendered_credentials
            if isinstance(credential["recipient"], dict)
        )
        + "\n"
        f"- Supplied QR artwork and all {len(rendered_credentials) * len(PROFILE_DIMENSIONS)} "
        "rendered back PNG profiles decoded successfully: Passed\n"
        "- Printed redemption URL exactly matches canonical metadata, including scheme: Passed\n"
        "- Blank Pay Code field contains canonical double bars and no divider or guide: Passed\n"
        "- Empty Demonstration Value and recipient validation rendering collapses both blocks: Passed\n"
        "- Print-sheet personalization follows the canonical Markdown credential collection: Passed\n"
        "- Recipient-specific executive, business-card, and wallet-card front/back generation: Passed\n"
        f"- Individual recipient PDFs: 2 pages each; credential-set PDFs: {combined_page_count} pages each\n"
        f"- A4 duplex print sheet: {print_page_count} pages, {len(rendered_credentials)} credentials\n"
        "- Protected Cover Letter, Commercial Proposal, and Program Guide hashes: Unchanged\n"
        "- Canonical Markdown source freeze: Passed\n"
        "- Page-by-page visual inspection: Pending\n",
        encoding="utf-8",
    )

    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
