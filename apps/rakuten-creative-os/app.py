"""Rakuten Creative OS: local-only evidence-first employee web MVP."""
from __future__ import annotations
import io
import json
import os
import re
import zipfile
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, Response, StreamingResponse
from PIL import Image, ImageDraw, ImageFont, ImageOps, UnidentifiedImageError

ROOT = Path(__file__).resolve().parent
app = FastAPI(title="Rakuten Creative OS – Local MVP", docs_url=None, redoc_url=None)
LETTERS = "ABCDEFGHIJKLM"
MAX_UPLOAD = 12 * 1024 * 1024
Image.MAX_IMAGE_PIXELS = 26_000_000
FONT_PATHS = [
    os.environ.get("RAKUTEN_FONT", ""),
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "C:/Windows/Fonts/meiryo.ttc",
    "C:/Windows/Fonts/msgothic.ttc",
]

def font(size: int):
    for p in FONT_PATHS:
        if p and Path(p).exists():
            try:
                return ImageFont.truetype(p, size)
            except OSError:
                continue
    return ImageFont.load_default()

def valid_hex(value: str, default: str) -> str:
    return value if re.fullmatch(r"#[0-9a-fA-F]{6}", str(value)) else default

def fitted_photo(draw_image: Image.Image, original: Image.Image, rect, pad=18):
    x0, y0, x1, y1 = rect
    w, h = x1-x0-2*pad, y1-y0-2*pad
    if w < 8 or h < 8:
        return
    photo = ImageOps.contain(original.convert("RGBA"), (w, h))
    xx = x0 + (x1-x0-photo.width)//2
    yy = y0 + (y1-y0-photo.height)//2
    draw_image.paste(photo, (xx, yy), photo)

def textfit(draw, text, xy, max_width, size, fill, min_size=18):
    text = str(text or "")
    for s in range(size, min_size-1, -2):
        f = font(s)
        if draw.textbbox((0, 0), text, font=f)[2] <= max_width:
            draw.text(xy, text, font=f, fill=fill, stroke_width=0)
            return
    while text and draw.textbbox((0, 0), text + "…", font=font(min_size))[2] > max_width:
        text = text[:-1]
    draw.text(xy, text + "…", font=font(min_size), fill=fill)

def card(canvas, photo, label, subtitle, rect, palette):
    d = ImageDraw.Draw(canvas)
    x0, y0, x1, y1 = rect
    d.rounded_rectangle(rect, radius=25, fill="#FFFDF8", outline=palette["brown"], width=4)
    d.ellipse((x0+12, y0+12, x0+79, y0+79), fill=palette["pink"], outline=palette["brown"], width=3)
    d.text((x0+33, y0+22), label, font=font(36), fill=palette["brown"])
    textfit(d, subtitle, (x0+90, y0+28), x1-x0-106, 27, palette["brown"])
    fitted_photo(canvas, photo, (x0+12, y0+85, x1-12, y1-16), 5)

def paint(number: int, manifest: dict, photos: dict[str, Image.Image]) -> Image.Image:
    palette = {
        "bg": valid_hex(manifest.get("background"), "#FFF4CF"),
        "pink": valid_hex(manifest.get("pink"), "#F5A7B8"),
        "brown": valid_hex(manifest.get("brown"), "#6D3A37"),
    }
    canvas = Image.new("RGB", (1000, 1000), palette["bg"])
    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle((24, 24, 976, 976), radius=35, outline=palette["pink"], width=12)
    d.rounded_rectangle((40, 36, 960, 170), radius=32, fill=palette["pink"])
    texts = manifest["headlines"]
    textfit(d, texts[number-1], (66, 62), 875, 59, palette["brown"], 24)
    mapping = manifest["skus"]
    codes = [code for code in LETTERS if code in photos and mapping.get(code)]
    if not codes:
        raise HTTPException(422, "No mapped SKU image available")
    def subtitle(c): return str(mapping[c].get("name", c))
    hero = "I" if "I" in codes else codes[0]
    # Different compositions for genuinely distinct image purposes.
    if number in (1, 3, 4, 7, 10):
        x = (70, 195, 930, 815)
        card(canvas, photos[hero], hero, subtitle(hero), x, palette)
        foot = ["主商品 / メインビジュアル", "", "実物写真で質感を確認", "実物写真による使用イメージ",
                "", "", "外観・細部をチェック", "", "", "遊び方は商品に応じてご確認ください"][number-1]
        textfit(d, foot, (85, 858), 820, 34, palette["brown"])
    elif number in (2, 5, 6, 8, 9):
        if number == 2: selected = codes[:3]
        elif number == 5: selected = [c for c in "ABCEG" if c in photos][:3] or codes[:3]
        elif number == 6: selected = [c for c in "EGI" if c in photos] or codes[:3]
        elif number == 8: selected = [c for c in "EFGH" if c in photos] or codes[:3]
        else: selected = [c for c in "IJKL" if c in photos] or codes[:3]
        if not selected: selected = codes[:3]
        while len(selected) < 3: selected.append(selected[-1])
        positions = [(65, 202, 485, 515), (515, 202, 935, 515), (270, 540, 730, 910)]
        for c, r in zip(selected, positions):
            card(canvas, photos[c], c, subtitle(c), r, palette)
    elif number == 11:
        # Every actually supplied SKU is displayed, never fabricated.
        columns = 4
        for i, c in enumerate(codes):
            col, row = i % columns, i // columns
            left, top = 47 + col*229, 190 + row*190
            if top + 180 > 960: break
            card(canvas, photos[c], c, subtitle(c), (left, top, left+216, top+177), palette)
    else:  # 12: only mapped packs are eligible for package/contents panels.
        selected = [c for c in "DFHJM" if c in photos]
        if not selected:
            selected = codes[:2]
        positions = [(55, 195, 480, 565), (520, 195, 945, 565), (275, 585, 725, 930)]
        for c, r in zip(selected[:3], positions):
            card(canvas, photos[c], c, subtitle(c), r, palette)
    return canvas

async def collect(request: Request):
    form = await request.form(max_files=18, max_fields=12, max_part_size=14*1024*1024)
    try:
        manifest = json.loads(str(form["manifest"]))
    except (KeyError, ValueError, TypeError):
        raise HTTPException(422, "Invalid manifest JSON")
    if not isinstance(manifest, dict) or not isinstance(manifest.get("skus"), dict):
        raise HTTPException(422, "Missing SKU manifest")
    if len(manifest.get("headlines", [])) != 12:
        raise HTTPException(422, "Exactly 12 reviewed headlines needed for this test case")
    photos = {}
    for code, entry in manifest["skus"].items():
        if code not in LETTERS or not isinstance(entry, dict):
            raise HTTPException(422, "Invalid SKU code")
        if not str(entry.get("name", "")).strip():
            raise HTTPException(422, f"Missing name for SKU {code}")
        up = form.get("photo_" + code)
        if up is None:
            raise HTTPException(422, f"SKU {code} has a label but no real image")
        content = await up.read(MAX_UPLOAD + 1)
        if len(content) > MAX_UPLOAD:
            raise HTTPException(413, f"SKU {code} image exceeds 12MB")
        try:
            im = Image.open(io.BytesIO(content))
            im.load()
            photos[code] = ImageOps.exif_transpose(im).convert("RGBA")
        except (UnidentifiedImageError, OSError, ValueError, Image.DecompressionBombError):
            raise HTTPException(422, f"Invalid image for SKU {code}")
    if not photos:
        raise HTTPException(422, "Upload at least one real SKU photograph")
    return manifest, photos, form

@app.get("/")
async def homepage():
    return FileResponse(ROOT / "index.html", media_type="text/html")

@app.post("/api/preview")
async def preview(request: Request):
    manifest, photos, _ = await collect(request)
    # This is a review CONTACT SHEET, explicitly not 12 separate retail JPGs.
    sheet = Image.new("RGB", (1200, 900), "#FFFFFF")
    for i in range(12):
        page = paint(i+1, manifest, photos)
        thumb = page.resize((280, 280))
        sheet.paste(thumb, (10 + (i%4)*300, 10 + (i//4)*295))
    buf = io.BytesIO()
    sheet.save(buf, format="JPEG", quality=82)
    return Response(buf.getvalue(), media_type="image/jpeg",
                    headers={"Cache-Control":"no-store"})

@app.post("/api/export")
async def export(request: Request):
    manifest, photos, form = await collect(request)
    if not (manifest.get("approved_style") and manifest.get("approved_copy")
            and manifest.get("approved_source") and manifest.get("reviewed_preview")):
        raise HTTPException(422, "Style, Japanese copy, source identity and preview review must be confirmed")
    if form.get("style_reference") is None:
        raise HTTPException(422, "Attach the actual approved visual reference")
    ref = await form["style_reference"].read(MAX_UPLOAD + 1)
    if len(ref) > MAX_UPLOAD: raise HTTPException(413, "Reference exceeds 12MB")
    try:
        with Image.open(io.BytesIO(ref)) as im: im.verify()
    except (UnidentifiedImageError, OSError, Image.DecompressionBombError):
        raise HTTPException(422, "Invalid style reference image")
    if not manifest.get("approved_ref_name"):
        raise HTTPException(422, "Approved style reference label is missing")
    zbuf = io.BytesIO()
    index = {"status": "PENDING_HUMAN_FINAL_QA", "image_count": 12,
             "reference": manifest["approved_ref_name"],
             "note": "Template-composited only; not an AI visual match or verified Rakuten listing approval",
             "skus": manifest["skus"], "headlines": manifest["headlines"]}
    with zipfile.ZipFile(zbuf, "w", zipfile.ZIP_DEFLATED) as z:
        for i in range(1, 13):
            frame = paint(i, manifest, photos)
            out = io.BytesIO()
            frame.save(out, "JPEG", quality=94, subsampling=0)
            z.writestr(f"{i:02d}_Rakuten.jpg", out.getvalue())
        z.writestr("QA_MANIFEST.json", json.dumps(index, ensure_ascii=False, indent=2))
    zbuf.seek(0)
    return StreamingResponse(zbuf, media_type="application/zip",
        headers={"Content-Disposition":'attachment; filename="rakuten-12-draft.zip"',
                 "Cache-Control":"no-store"})
