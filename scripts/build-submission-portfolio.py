#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
import tempfile
import textwrap
import zipfile
from datetime import date
from pathlib import Path
from typing import Any

import yaml
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
CHECKSUM_FILENAME = "MANIFEST/SHA256SUMS.txt"


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


def load_manifest(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Submission manifest must contain a YAML mapping.")
    return data


def required(mapping: dict[str, Any], key: str) -> Any:
    if key not in mapping:
        raise ValueError(f"Required manifest field is missing: {key}")
    return mapping[key]


def pdf_page_count(path: Path) -> int:
    pdfinfo = require_executable("pdfinfo")
    result = subprocess.run(
        [pdfinfo, str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    for line in result.stdout.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise RuntimeError(f"Unable to determine PDF page count: {path}")


def decode_qr(path: Path) -> list[str]:
    zbarimg = require_executable("zbarimg")
    result = subprocess.run(
        [zbarimg, "--quiet", "--raw", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def verify_pdf_qr(
    pdf_path: Path,
    page: int,
    expected_count: int,
    expected_destination: str,
) -> None:
    pdftoppm = require_executable("pdftoppm")
    with tempfile.TemporaryDirectory(prefix="submission-qr-") as temporary:
        output_prefix = Path(temporary) / "credential-back"
        subprocess.run(
            [
                pdftoppm,
                "-f",
                str(page),
                "-l",
                str(page),
                "-singlefile",
                "-r",
                "300",
                "-png",
                str(pdf_path),
                str(output_prefix),
            ],
            check=True,
            capture_output=True,
        )
        decoded = decode_qr(output_prefix.with_suffix(".png"))
    if len(decoded) != expected_count:
        raise ValueError(
            f"Expected {expected_count} QR code(s) in {pdf_path}, decoded {len(decoded)}."
        )
    if any(value != expected_destination for value in decoded):
        raise ValueError(f"Unexpected QR destination in {pdf_path}: {decoded}")


def validate_manifest(data: dict[str, Any]) -> None:
    submission = required(data, "submission")
    if not isinstance(submission, dict):
        raise ValueError("submission must be a mapping.")
    if submission.get("document_type") != "institution_submission_portfolio":
        raise ValueError("Unsupported submission document type.")
    if str(submission.get("version")) != "1.0":
        raise ValueError("This builder invocation expects portfolio Version 1.0.")
    if submission.get("status") != "production":
        raise ValueError("Only a production submission may be packaged for delivery.")
    documents = required(data, "documents")
    if not isinstance(documents, list) or not documents:
        raise ValueError("documents must be a non-empty list.")
    recipients = required(data, "recipients")
    if not isinstance(recipients, list) or not recipients:
        raise ValueError("recipients must be a non-empty list.")


def all_profiles(data: dict[str, Any]) -> list[dict[str, Any]]:
    profiles: list[dict[str, Any]] = []
    for document in data["documents"]:
        for profile_name, profile in document["profiles"].items():
            record = dict(profile)
            record["profile"] = profile_name
            record["document_id"] = document["id"]
            record["publication_name"] = document["publication_name"]
            record["edition"] = document["edition"]
            record["version"] = str(document["version"])
            profiles.append(record)
    return profiles


def validate_sources(data: dict[str, Any]) -> None:
    verification = data["credential_verification"]
    qr_source = REPOSITORY_ROOT / verification["source"]
    if not qr_source.is_file():
        raise FileNotFoundError(f"Governed QR source is unavailable: {qr_source}")
    if sha256(qr_source) != verification["sha256"]:
        raise ValueError("Governed QR source checksum does not match the manifest.")
    decoded = decode_qr(qr_source)
    if decoded != [verification["destination"]]:
        raise ValueError(f"Governed QR destination mismatch: {decoded}")

    packaged_paths: set[str] = set()
    for profile in all_profiles(data):
        source = REPOSITORY_ROOT / profile["source"]
        if not source.is_file():
            raise FileNotFoundError(f"Source artifact is unavailable: {source}")
        actual_hash = sha256(source)
        if actual_hash != profile["sha256"]:
            raise ValueError(
                f"Source checksum mismatch for {profile['source']}: {actual_hash}"
            )
        pages = pdf_page_count(source)
        if pages != int(profile["pages"]):
            raise ValueError(
                f"Page-count mismatch for {profile['source']}: {pages}"
            )
        packaged = profile["packaged"]
        if packaged in packaged_paths:
            raise ValueError(f"Duplicate packaged path: {packaged}")
        if not packaged.lower().endswith(".pdf"):
            raise ValueError(f"Recipient-facing artifact must be a PDF: {packaged}")
        packaged_paths.add(packaged)


def readme_text(data: dict[str, Any]) -> str:
    submission = data["submission"]
    issuer = data["issuer"]
    recipients = data["recipients"]
    date_label = date.fromisoformat(submission["submission_date"]).strftime("%d %B %Y")
    date_label = date_label.lstrip("0")
    lead = recipients[0]
    attention = recipients[1]
    principal_documents = sorted(
        [document for document in data["documents"] if document["order"] <= 3],
        key=lambda document: document["order"],
    )
    contents = "\n\n".join(
        f"{document['order']}. {document['portfolio_label']}\n\n"
        f"{document['description']}"
        for document in principal_documents
    )
    credential_names = "\n".join(
        f"- {recipient['name']}" for recipient in recipients
    )
    return (
        f"{submission['title'].upper()}\n\n"
        f"Prepared by\n{issuer['organization']}\n\n"
        f"Submission Date\n{date_label}\n\n"
        "Prepared for\n\n"
        f"{lead['salutation']} {lead['name']}\n{lead['title']}\n"
        f"{lead['organization']}\n\n"
        "Attention\n\n"
        f"{attention['salutation']} {attention['name']}\n{attention['title']}\n"
        f"{attention['organization']}\n\n"
        f"CONTENTS\n\n{contents}\n\n"
        "4. Executive Demonstration Credentials\n\nPrepared for:\n\n"
        f"{credential_names}\n\n"
        "FOLDER GUIDE\n\n"
        "SCREEN\n\nUse these files for electronic reading, internal circulation, "
        "and presentation.\n\n"
        "PRINT\n\nUse these files for physical printing and submission assembly.\n\n"
        "The Demonstration Credential print sheet is arranged for duplex printing.\n"
    )


def draw_wrapped(
    pdf: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    width: float,
    font: str,
    size: float,
    leading: float,
    color: HexColor,
) -> float:
    pdf.setFont(font, size)
    pdf.setFillColor(color)
    approximate_characters = max(12, int(width / (size * 0.52)))
    lines = textwrap.wrap(text, width=approximate_characters) or [""]
    for line in lines:
        pdf.drawString(x, y, line)
        y -= leading
    return y


def render_readme_pdf(path: Path, data: dict[str, Any]) -> None:
    submission = data["submission"]
    recipients = data["recipients"]
    issuer = data["issuer"]
    width, height = A4
    ink = HexColor("#172533")
    muted = HexColor("#68747E")
    accent = HexColor("#E6691C")
    pale = HexColor("#F3F4F3")
    pdf = canvas.Canvas(
        str(path),
        pagesize=A4,
        pageCompression=1,
        invariant=1,
    )
    pdf.setTitle(submission["title"])
    pdf.setAuthor(issuer["organization"])
    pdf.setSubject("Executive submission portfolio guide")
    pdf.setCreator("x-change Submission Portfolio Builder")

    left = 48
    right = width - 48
    y = height - 48
    pdf.setFillColor(accent)
    pdf.rect(left, y - 5, 34, 3, fill=1, stroke=0)
    y -= 26
    pdf.setFillColor(ink)
    pdf.setFont("Helvetica-Bold", 17)
    pdf.drawString(left, y, "ALLBANK EXECUTIVE")
    y -= 21
    pdf.drawString(left, y, "SUBMISSION PORTFOLIO")
    pdf.setFont("Helvetica", 7.4)
    pdf.setFillColor(muted)
    pdf.drawRightString(right, y, "FIRST EDITION · VERSION 1.0")

    y -= 28
    pdf.setFillColor(pale)
    pdf.roundRect(left, y - 88, right - left, 88, 5, fill=1, stroke=0)
    pdf.setFillColor(muted)
    pdf.setFont("Helvetica-Bold", 6.8)
    pdf.drawString(left + 14, y - 16, "PREPARED BY")
    pdf.drawString(left + 214, y - 16, "SUBMISSION DATE")
    pdf.setFillColor(ink)
    pdf.setFont("Times-Roman", 9.2)
    pdf.drawString(left + 14, y - 32, issuer["organization"])
    date_label = date.fromisoformat(submission["submission_date"]).strftime("%d %B %Y").lstrip("0")
    pdf.drawString(left + 214, y - 32, date_label)
    pdf.setFillColor(muted)
    pdf.setFont("Helvetica-Bold", 6.8)
    pdf.drawString(left + 14, y - 52, "PREPARED FOR")
    pdf.drawString(left + 214, y - 52, "ATTENTION")
    pdf.setFillColor(ink)
    lead = recipients[0]
    attention = recipients[1]
    pdf.setFont("Times-Roman", 8.7)
    pdf.drawString(left + 14, y - 66, f"{lead['salutation']} {lead['name']}")
    pdf.drawString(left + 214, y - 66, f"{attention['salutation']} {attention['name']}")
    pdf.setFont("Times-Italic", 7.6)
    pdf.setFillColor(muted)
    pdf.drawString(left + 14, y - 78, f"{lead['title']} · {lead['organization']}")
    pdf.drawString(
        left + 214,
        y - 78,
        f"{attention['title']} · {attention['organization']}",
    )
    y -= 110

    pdf.setFillColor(accent)
    pdf.setFont("Helvetica-Bold", 7.1)
    pdf.drawString(left, y, "CONTENTS")
    y -= 18
    for document in sorted(data["documents"], key=lambda item: item["order"]):
        if document["id"] == "credential-duplex-sheet":
            continue
        if document["id"].startswith("credential-"):
            continue
        pdf.setFillColor(accent)
        pdf.setFont("Helvetica-Bold", 8.4)
        pdf.drawString(left, y, str(document["order"]))
        pdf.setFillColor(ink)
        pdf.setFont("Times-Bold", 9.7)
        pdf.drawString(left + 22, y, document["portfolio_label"])
        y -= 13
        y = draw_wrapped(
            pdf,
            document["description"],
            left + 22,
            y,
            right - left - 22,
            "Times-Roman",
            8.5,
            10.5,
            muted,
        ) - 8

    pdf.setFillColor(accent)
    pdf.setFont("Helvetica-Bold", 8.4)
    pdf.drawString(left, y, "4")
    pdf.setFillColor(ink)
    pdf.setFont("Times-Bold", 9.7)
    pdf.drawString(left + 22, y, "Executive Demonstration Credentials")
    y -= 14
    pdf.setFont("Times-Roman", 8.5)
    pdf.setFillColor(muted)
    pdf.drawString(left + 22, y, "Prepared for Jesus Vicente Garcia and Digna Samonte.")
    y -= 28

    pdf.setFillColor(accent)
    pdf.setFont("Helvetica-Bold", 7.1)
    pdf.drawString(left, y, "FOLDER GUIDE")
    y -= 17
    column_width = (right - left - 14) / 2
    for index, (label, description) in enumerate(
        (
            (
                "SCREEN",
                "Use these files for electronic reading, internal circulation, and presentation.",
            ),
            (
                "PRINT",
                "Use these files for physical printing and submission assembly. The credential sheet is arranged for duplex printing.",
            ),
        )
    ):
        x = left + index * (column_width + 14)
        pdf.setFillColor(pale)
        pdf.roundRect(x, y - 61, column_width, 61, 4, fill=1, stroke=0)
        pdf.setFillColor(ink)
        pdf.setFont("Helvetica-Bold", 7.6)
        pdf.drawString(x + 12, y - 17, label)
        draw_wrapped(
            pdf,
            description,
            x + 12,
            y - 32,
            column_width - 24,
            "Times-Roman",
            8.0,
            9.5,
            muted,
        )

    pdf.setStrokeColor(HexColor("#D4D9DC"))
    pdf.line(left, 38, right, 38)
    pdf.setFillColor(muted)
    pdf.setFont("Helvetica", 6.5)
    pdf.drawString(left, 26, "OPEN DISBURSEMENT TECHNOLOGIES, INC.")
    pdf.drawRightString(right, 26, "ALLBANK · 20 JULY 2026")
    pdf.showPage()
    pdf.save()
    if pdf_page_count(path) != 1:
        raise RuntimeError("Portfolio README must render as exactly one page.")


def write_status(path: Path, data: dict[str, Any], archive_name: str) -> None:
    submission = data["submission"]
    recipients = "\n".join(
        f"- {recipient['name']}, {recipient['title']}, {recipient['organization']}"
        for recipient in data["recipients"]
    )
    publications = "\n".join(
        f"- {document['publication_name']} — {document['edition']}, Version {document['version']}"
        for document in data["documents"]
        if document["id"] != "credential-duplex-sheet"
    )
    path.write_text(
        "# Submission Status\n\n"
        f"**Submission:** {submission['title']}  \n"
        f"**Institution:** {submission['institution']}  \n"
        f"**Status:** {submission['status_label']}  \n"
        f"**State:** {submission['state']}  \n"
        f"**Edition:** {submission['edition']}  \n"
        f"**Version:** {submission['version']}  \n"
        f"**Submission date:** {submission['submission_date']}  \n"
        f"**Build date:** {submission['build_date']}  \n"
        f"**Archive:** `{archive_name}`  \n"
        "**Checksum manifest:** `MANIFEST/SHA256SUMS.txt`  \n"
        f"**Build command:** `{data['build']['command']}`  \n"
        "**QA status:** Passed\n\n"
        "## Recipients\n\n"
        f"{recipients}\n\n"
        "## Included publications\n\n"
        f"{publications}\n\n"
        "## Governance boundary\n\n"
        "This record applies only to the assembled Submission Portfolio. It does not "
        "alter the edition, version, approval, doctrine, or frozen state of any included "
        "publication. Existing PDFs were copied byte-for-byte.\n\n"
        "The checksum manifest covers every portfolio file except itself, because a "
        "checksum file cannot contain its own final SHA-256 without becoming self-referential. "
        "The complete archive is independently covered by the external `.zip.sha256` file.\n",
        encoding="utf-8",
    )


def write_source_artifacts(
    path: Path,
    data: dict[str, Any],
    canonical_manifest: Path,
    staged_root: Path,
) -> None:
    manifest_hash = sha256(canonical_manifest)
    rows = [
        (
            "README.pdf",
            canonical_manifest.relative_to(REPOSITORY_ROOT).as_posix(),
            "Submission Portfolio Guide",
            str(data["submission"]["version"]),
            "Packaging derivative",
            manifest_hash,
            sha256(staged_root / "README.pdf"),
        ),
        (
            "README.txt",
            canonical_manifest.relative_to(REPOSITORY_ROOT).as_posix(),
            "Submission Portfolio Guide",
            str(data["submission"]["version"]),
            "Packaging derivative",
            manifest_hash,
            sha256(staged_root / "README.txt"),
        ),
    ]
    for profile in all_profiles(data):
        source = REPOSITORY_ROOT / profile["source"]
        packaged = staged_root / profile["packaged"]
        rows.append(
            (
                profile["packaged"],
                profile["source"],
                profile["publication_name"],
                profile["version"],
                "Byte-for-byte copy",
                sha256(source),
                sha256(packaged),
            )
        )
    table_rows = "\n".join(
        "| " + " | ".join(value.replace("|", "\\|") for value in row) + " |"
        for row in rows
    )
    path.write_text(
        "# Source Artifacts\n\n"
        "This record maps every recipient-facing portfolio file to its governed source. "
        "Approved publication PDFs were copied byte-for-byte. README files are packaging "
        "derivatives generated from the canonical institution submission manifest.\n\n"
        "| Packaged filename | Original repository path | Publication | Version | Treatment | Source SHA-256 | Packaged SHA-256 |\n"
        "| --- | --- | --- | --- | --- | --- | --- |\n"
        f"{table_rows}\n\n"
        "## Packaging records\n\n"
        f"- `MANIFEST/manifest.yaml` is a byte-for-byte copy of `{canonical_manifest.relative_to(REPOSITORY_ROOT).as_posix()}` with SHA-256 `{manifest_hash}`.\n"
        "- `MANIFEST/SUBMISSION_STATUS.md` is generated from the canonical manifest.\n"
        "- `MANIFEST/SOURCE_ARTIFACTS.md` is this self-describing generated record.\n"
        "- `MANIFEST/SHA256SUMS.txt` is generated last and therefore is not a Source Artifact. It checks every other file in the portfolio.\n"
        "- The ZIP archive and its external checksum are delivery containers outside the portfolio root.\n",
        encoding="utf-8",
    )


def write_checksums(staged_root: Path) -> None:
    checksum_path = staged_root / CHECKSUM_FILENAME
    files = sorted(
        path
        for path in staged_root.rglob("*")
        if path.is_file() and path != checksum_path
    )
    lines = [
        "# SHA-256 checksums for every portfolio file except this self-referential checksum manifest."
    ]
    lines.extend(
        f"{sha256(path)}  {path.relative_to(staged_root).as_posix()}" for path in files
    )
    checksum_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def verify_checksums(staged_root: Path) -> None:
    checksum_path = staged_root / CHECKSUM_FILENAME
    for line in checksum_path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        expected, relative = line.split("  ", 1)
        actual = sha256(staged_root / relative)
        if actual != expected:
            raise ValueError(f"Packaged checksum mismatch: {relative}")


def expected_relative_files(data: dict[str, Any]) -> set[str]:
    expected = {
        "README.pdf",
        "README.txt",
        "MANIFEST/manifest.yaml",
        "MANIFEST/SHA256SUMS.txt",
        "MANIFEST/SUBMISSION_STATUS.md",
        "MANIFEST/SOURCE_ARTIFACTS.md",
    }
    expected.update(profile["packaged"] for profile in all_profiles(data))
    return expected


def verify_staged_portfolio(staged_root: Path, data: dict[str, Any]) -> None:
    actual = {
        path.relative_to(staged_root).as_posix()
        for path in staged_root.rglob("*")
        if path.is_file()
    }
    expected = expected_relative_files(data)
    if actual != expected:
        raise ValueError(
            f"Portfolio contents differ from the governed manifest. Missing: {sorted(expected - actual)}; unexpected: {sorted(actual - expected)}"
        )
    prohibited_suffixes = {".md~", ".tmp", ".html", ".png", ".svg"}
    for relative in actual:
        if Path(relative).suffix.lower() in prohibited_suffixes:
            raise ValueError(f"Prohibited recipient package artifact: {relative}")
        if relative.startswith(("SCREEN/", "PRINT/")) and not relative.endswith(".pdf"):
            raise ValueError(f"Non-PDF recipient artifact: {relative}")
    for profile in all_profiles(data):
        packaged = staged_root / profile["packaged"]
        if sha256(packaged) != profile["sha256"]:
            raise ValueError(f"Packaged PDF is not a byte-identical copy: {profile['packaged']}")
        if pdf_page_count(packaged) != int(profile["pages"]):
            raise ValueError(f"Packaged PDF page count changed: {profile['packaged']}")
    if pdf_page_count(staged_root / "README.pdf") != 1:
        raise ValueError("README.pdf must contain one page.")
    verify_checksums(staged_root)

    destination = data["credential_verification"]["destination"]
    for profile in all_profiles(data):
        if "qr_page" in profile:
            verify_pdf_qr(
                staged_root / profile["packaged"],
                int(profile["qr_page"]),
                int(profile["qr_count"]),
                destination,
            )


def write_deterministic_zip(
    staged_root: Path,
    archive_path: Path,
    archive_timestamp: str,
) -> None:
    parsed = date.fromisoformat(archive_timestamp[:10])
    timestamp = (parsed.year, parsed.month, parsed.day, 0, 0, 0)
    paths = sorted(path for path in staged_root.rglob("*") if path.is_file())
    with zipfile.ZipFile(
        archive_path,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for path in paths:
            relative = path.relative_to(staged_root).as_posix()
            member = f"{staged_root.name}/{relative}"
            info = zipfile.ZipInfo(member, timestamp)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, path.read_bytes(), compresslevel=9)


def verify_archive(staged_root: Path, archive_path: Path) -> None:
    expected = {
        f"{staged_root.name}/{path.relative_to(staged_root).as_posix()}"
        for path in staged_root.rglob("*")
        if path.is_file()
    }
    with zipfile.ZipFile(archive_path, "r") as archive:
        actual = set(archive.namelist())
        if actual != expected:
            raise ValueError("ZIP contents do not match the staged portfolio.")
        for member in sorted(actual):
            relative = Path(member).relative_to(staged_root.name)
            if archive.read(member) != (staged_root / relative).read_bytes():
                raise ValueError(f"ZIP member differs from staged file: {member}")

    with tempfile.TemporaryDirectory(prefix="submission-extract-") as temporary:
        extraction_root = Path(temporary)
        with zipfile.ZipFile(archive_path, "r") as archive:
            archive.extractall(extraction_root)
        extracted = extraction_root / staged_root.name
        extracted_files = sorted(
            path.relative_to(extracted).as_posix()
            for path in extracted.rglob("*")
            if path.is_file()
        )
        staged_files = sorted(
            path.relative_to(staged_root).as_posix()
            for path in staged_root.rglob("*")
            if path.is_file()
        )
        if extracted_files != staged_files:
            raise ValueError("Extracted ZIP file set differs from staged portfolio.")
        for relative in staged_files:
            if (extracted / relative).read_bytes() != (staged_root / relative).read_bytes():
                raise ValueError(f"Extracted file differs from staged source: {relative}")


def build(manifest_path: Path) -> tuple[Path, Path, Path]:
    data = load_manifest(manifest_path)
    validate_manifest(data)
    validate_sources(data)

    submission = data["submission"]
    output_root = REPOSITORY_ROOT / data["build"]["output_root"]
    staged_root = output_root / submission["archive_stem"]
    archive_path = output_root / f"{submission['archive_stem']}.zip"
    archive_checksum_path = output_root / f"{submission['archive_stem']}.zip.sha256"

    output_root.mkdir(parents=True, exist_ok=True)
    if staged_root.exists():
        shutil.rmtree(staged_root)
    staged_root.mkdir(parents=True)
    (staged_root / "SCREEN").mkdir()
    (staged_root / "PRINT").mkdir()
    (staged_root / "MANIFEST").mkdir()

    for profile in all_profiles(data):
        source = REPOSITORY_ROOT / profile["source"]
        destination = staged_root / profile["packaged"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        if sha256(source) != sha256(destination):
            raise RuntimeError(f"Byte-for-byte copy verification failed: {destination}")

    text = readme_text(data)
    (staged_root / "README.txt").write_text(text, encoding="utf-8")
    render_readme_pdf(staged_root / "README.pdf", data)
    shutil.copyfile(manifest_path, staged_root / "MANIFEST" / "manifest.yaml")
    write_status(staged_root / "MANIFEST" / "SUBMISSION_STATUS.md", data, archive_path.name)
    write_source_artifacts(
        staged_root / "MANIFEST" / "SOURCE_ARTIFACTS.md",
        data,
        manifest_path,
        staged_root,
    )
    write_checksums(staged_root)
    verify_staged_portfolio(staged_root, data)

    write_deterministic_zip(
        staged_root,
        archive_path,
        data["build"]["deterministic_archive_timestamp"],
    )
    verify_archive(staged_root, archive_path)
    archive_checksum_path.write_text(
        f"{sha256(archive_path)}  {archive_path.name}\n",
        encoding="utf-8",
    )
    return staged_root, archive_path, archive_checksum_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build and verify an institution Submission Portfolio."
    )
    parser.add_argument(
        "manifest",
        type=Path,
        help="Canonical institution submission manifest.",
    )
    arguments = parser.parse_args()
    manifest_path = arguments.manifest
    if not manifest_path.is_absolute():
        manifest_path = REPOSITORY_ROOT / manifest_path
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Submission manifest is unavailable: {manifest_path}")
    staged_root, archive_path, archive_checksum_path = build(manifest_path)
    print("Submission Portfolio build passed.")
    print(f"Staged portfolio: {staged_root.relative_to(REPOSITORY_ROOT)}")
    print(f"Archive: {archive_path.relative_to(REPOSITORY_ROOT)}")
    print(f"Archive SHA-256: {sha256(archive_path)}")
    print(f"External checksum: {archive_checksum_path.relative_to(REPOSITORY_ROOT)}")


if __name__ == "__main__":
    main()
