#!/usr/bin/env python3

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, "/tmp/pillow")

from PIL import Image, ImageOps

SOURCE_DIR = ROOT / "new"
OUTPUTS = {
    "thumb-mobile": 800,
    "thumb-desktop": 1200,
    "large-mobile": 1400,
    "large-desktop": 2000,
}

JPEG_OPTIONS_BY_VARIANT = {
    "default": {
        "format": "JPEG",
        "quality": 88,
        "optimize": True,
        "progressive": True,
    },
    "thumb-mobile": {
        "format": "JPEG",
        "quality": 78,
        "optimize": True,
        "progressive": True,
    },
}

WEBP_OPTIONS_BY_VARIANT = {
    "default": {
        "format": "WEBP",
        "quality": 84,
        "method": 6,
    },
    "thumb-mobile": {
        "format": "WEBP",
        "quality": 74,
        "method": 6,
    },
}


def iter_source_images():
    for path in sorted(SOURCE_DIR.glob("*.jpg")):
        if path.name.startswith("."):
            continue
        yield path


def resize_image(source_path: Path, target_width: int):
    with Image.open(source_path) as image:
        image = ImageOps.exif_transpose(image)
        if image.mode not in ("RGB", "L"):
            image = image.convert("RGB")
        elif image.mode == "L":
            image = image.convert("RGB")

        icc_profile = image.info.get("icc_profile")
        resized = image.copy()
        resized.thumbnail((target_width, target_width), Image.Resampling.LANCZOS)
        return resized, icc_profile


def save_variants(source_path: Path):
    for folder_name, target_width in OUTPUTS.items():
        output_dir = ROOT / "images" / folder_name
        output_dir.mkdir(parents=True, exist_ok=True)

        resized, icc_profile = resize_image(source_path, target_width)
        jpg_path = output_dir / source_path.name
        webp_path = output_dir / source_path.with_suffix(".webp").name

        jpg_options = JPEG_OPTIONS_BY_VARIANT.get(folder_name, JPEG_OPTIONS_BY_VARIANT["default"]).copy()
        if icc_profile:
            jpg_options["icc_profile"] = icc_profile
        resized.save(jpg_path, **jpg_options)

        webp_options = WEBP_OPTIONS_BY_VARIANT.get(folder_name, WEBP_OPTIONS_BY_VARIANT["default"]).copy()
        if icc_profile:
            webp_options["icc_profile"] = icc_profile
        resized.save(webp_path, **webp_options)

        print(f"{source_path.name} -> {folder_name}: {resized.width}x{resized.height}")


def main():
    for source_path in iter_source_images():
        save_variants(source_path)


if __name__ == "__main__":
    main()
