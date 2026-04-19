#!/usr/bin/env python3

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, "/tmp/pillow")

from PIL import Image, ImageOps

SOURCE_DIR = ROOT / "new"

OUTPUTS = {
    "thumb-mobile-opt": {
        "width": 720,
        "jpg_quality": 86,
        "webp_quality": 80,
    },
    "thumb-desktop-opt": {
        "width": 1000,
        "jpg_quality": 86,
        "webp_quality": 80,
    },
    "detail-mobile-opt": {
        "width": 1440,
        "jpg_quality": 88,
        "webp_quality": 84,
    },
    "detail-desktop-opt": {
        "width": 1800,
        "jpg_quality": 88,
        "webp_quality": 84,
    },
}


def iter_sources():
    for path in sorted(SOURCE_DIR.glob("*.jpg")):
        if path.name.startswith("."):
            continue
        yield path


def render_variant(source_path: Path, width: int):
    with Image.open(source_path) as image:
        image = ImageOps.exif_transpose(image)
        if image.mode != "RGB":
            image = image.convert("RGB")

        icc_profile = image.info.get("icc_profile")
        exif = image.info.get("exif")
        rendered = image.copy()
        rendered.thumbnail((width, width), Image.Resampling.LANCZOS)
        return rendered, icc_profile, exif


def save_variant(source_path: Path, folder_name: str, config: dict):
    output_dir = ROOT / "new" / folder_name
    output_dir.mkdir(parents=True, exist_ok=True)

    rendered, icc_profile, exif = render_variant(source_path, config["width"])

    jpg_path = output_dir / source_path.name
    jpg_options = {
        "format": "JPEG",
        "quality": config["jpg_quality"],
        "optimize": True,
        "progressive": True,
    }
    if icc_profile:
        jpg_options["icc_profile"] = icc_profile
    if exif:
        jpg_options["exif"] = exif
    rendered.save(jpg_path, **jpg_options)

    webp_path = output_dir / source_path.with_suffix(".webp").name
    webp_options = {
        "format": "WEBP",
        "quality": config["webp_quality"],
        "method": 6,
    }
    if icc_profile:
        webp_options["icc_profile"] = icc_profile
    rendered.save(webp_path, **webp_options)

    print(f"{source_path.name} -> {folder_name}: {rendered.width}x{rendered.height}")


def main():
    for source_path in iter_sources():
        for folder_name, config in OUTPUTS.items():
            save_variant(source_path, folder_name, config)


if __name__ == "__main__":
    main()
