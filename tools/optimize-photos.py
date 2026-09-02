#!/usr/bin/env python3
"""
Prepare interest photos for the web.

Drop originals into  photos-src/<section>/  (that folder is gitignored), then run:

    python3 tools/optimize-photos.py

For every source photo this writes two web-sized copies under
assets/images/interests/<section>/ -- a `thumb/` used in the justified grid and a
`full/` opened by the lightbox -- and records the dimensions in _data/interests.yml.

EXIF is stripped from both outputs. Phone photos carry GPS coordinates, so shipping
them unmodified would publish trailhead and home locations.

Existing alt/caption text in _data/interests.yml is preserved; new photos are appended
with empty alt/caption for you to fill in.
"""
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
    import yaml
except ImportError as e:
    sys.exit(f"missing dependency: {e}. Install with: pip install Pillow pyyaml")

try:                              # iPhone .HEIC support; optional
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pass

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "photos-src"
OUT = ROOT / "assets" / "images" / "interests"
DATA = ROOT / "_data" / "interests.yml"

THUMB_EDGE = 900     # long edge for the grid image (2x the ~450px it renders at)
FULL_EDGE = 1800     # long edge for the lightbox image
QUALITY = 82
EXTS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff", ".heic", ".heif"}

# Folders that are not gallery sections. They feed single site images instead.
AVATAR_PX = 520          # 4x the 130px the homepage avatar renders at
COVER_PX = 2400          # hero background, spans the full viewport width
RESERVED = {"profile": "avatar", "cover": "cover"}
CENTERING = (0.5, 0.4)   # crop slightly above centre; faces usually sit high


def encode(im, dest, long_edge):
    """Resize so the long edge is `long_edge`, flatten to RGB, save without EXIF."""
    im = ImageOps.exif_transpose(im)          # bake in rotation before dropping EXIF
    if im.mode in ("RGBA", "LA", "P"):
        bg = Image.new("RGB", im.size, (255, 255, 255))
        im = im.convert("RGBA")
        bg.paste(im, mask=im.split()[-1])
        im = bg
    elif im.mode != "RGB":
        im = im.convert("RGB")

    w, h = im.size
    if max(w, h) > long_edge:
        scale = long_edge / max(w, h)
        im = im.resize((round(w * scale), round(h * scale)), Image.LANCZOS)

    dest.parent.mkdir(parents=True, exist_ok=True)
    # rebuild from raw pixels so no metadata survives into the output
    clean = Image.frombytes(im.mode, im.size, im.tobytes())
    clean.save(dest, "JPEG", quality=QUALITY, optimize=True, progressive=True)
    return clean.size


def first_image(d):
    for f in sorted(d.iterdir()):
        if f.suffix.lower() in EXTS and not f.name.startswith("."):
            return f
    return None


def build_avatar(src, centering):
    """Square crop -- never squash. The theme pins the avatar to a square box."""
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im).convert("RGB")
        out = ImageOps.fit(im, (AVATAR_PX, AVATAR_PX), Image.LANCZOS, centering=centering)
    clean = Image.frombytes(out.mode, out.size, out.tobytes())
    dest = ROOT / "assets" / "images" / "authorimage.jpg"
    clean.save(dest, "JPEG", quality=88, optimize=True, progressive=True)
    return dest, out.size


def build_cover(src):
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im).convert("RGB")
        w, h = im.size
        if w > COVER_PX:
            im = im.resize((COVER_PX, round(h * COVER_PX / w)), Image.LANCZOS)
    clean = Image.frombytes(im.mode, im.size, im.tobytes())
    dest = ROOT / "assets" / "images" / "cover.jpg"
    clean.save(dest, "JPEG", quality=82, optimize=True, progressive=True)
    return dest, im.size


def load_data():
    if DATA.exists():
        return yaml.safe_load(DATA.read_text()) or {"sections": []}
    return {"sections": []}


def main():
    global CENTERING
    for a in sys.argv[1:]:
        if a.startswith("--face-y="):        # 0.0 = crop to top of frame, 1.0 = bottom
            CENTERING = (0.5, float(a.split("=")[1]))

    if not SRC.exists():
        SRC.mkdir(parents=True, exist_ok=True)
        for s in ("hiking", "baking", "cycling", "profile", "cover"):
            (SRC / s).mkdir(exist_ok=True)
        print(f"created {SRC.relative_to(ROOT)}/ -- drop photos in the section folders and re-run")
        return

    data = load_data()
    sections = {s["id"]: s for s in data.get("sections", [])}
    total_before = total_after = 0

    for sdir in sorted(p for p in SRC.iterdir() if p.is_dir()):
        sid = sdir.name

        if sid in RESERVED:
            src = first_image(sdir)
            if src is None:
                continue
            if sid == "profile":
                dest, size = build_avatar(src, CENTERING)
            else:
                dest, size = build_cover(src)
            print(f"  [{RESERVED[sid]:7}] {src.name:34} -> "
                  f"{dest.relative_to(ROOT)}  {size[0]}x{size[1]}")
            continue

        section = sections.get(sid)
        if section is None:
            section = {"id": sid, "title": sid.title(), "blurb": "", "photos": []}
            data.setdefault("sections", []).append(section)
            sections[sid] = section
        section.setdefault("photos", [])
        known = {p["file"]: p for p in section["photos"]}

        for src in sorted(sdir.iterdir()):
            if src.suffix.lower() not in EXTS or src.name.startswith("."):
                continue
            name = src.stem.lower().replace(" ", "-").replace("_", "-") + ".jpg"
            with Image.open(src) as im:
                tw, th = encode(im, OUT / sid / "thumb" / name, THUMB_EDGE)
            with Image.open(src) as im:
                encode(im, OUT / sid / "full" / name, FULL_EDGE)

            before = src.stat().st_size
            after = ((OUT / sid / "thumb" / name).stat().st_size
                     + (OUT / sid / "full" / name).stat().st_size)
            total_before += before
            total_after += after

            entry = known.get(name)
            if entry is None:
                entry = {"file": name, "alt": "", "caption": ""}
                section["photos"].append(entry)
                status = "new"
            else:
                status = "updated"
            entry["w"], entry["h"] = tw, th
            entry["ar"] = round(tw / th, 4)
            print(f"  [{status:7}] {sid}/{name:34} {tw}x{th}  "
                  f"{before/1024:7.0f}K -> {after/1024:6.0f}K")

    DATA.parent.mkdir(parents=True, exist_ok=True)
    DATA.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100))
    if total_before:
        print(f"\ntotal {total_before/1048576:.1f} MB -> {total_after/1048576:.1f} MB")
    print(f"wrote {DATA.relative_to(ROOT)} -- fill in alt and caption for any new photos")


if __name__ == "__main__":
    main()
