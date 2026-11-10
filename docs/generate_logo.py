"""Compose logo_base.png + subtitle text → logo.png."""

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONT_CANDIDATES = [
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',       # Linux / CI
    '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
    '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf',
    '/System/Library/Fonts/Helvetica.ttc',                         # macOS
    'C:/Windows/Fonts/arialbd.ttf',                                # Windows
]

SUBTITLE_COLOR = (23, 24, 23)


def _find_font():
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            return path
    return None


def generate_logo(subtitle, static_dir=None):
    if static_dir is None:
        static_dir = Path(__file__).parent / 'source' / '_static'
    else:
        static_dir = Path(static_dir)

    base_path = static_dir / 'logo_base.png'
    out_path = static_dir / 'logo.png'

    base = Image.open(base_path).convert('RGBA')
    base_w, base_h = base.size

    font_path = _find_font()
    max_text_w = base_w - 40
    font_size = int(base_w * 0.17)

    if font_path:
        font = ImageFont.truetype(font_path, font_size)
        while font_size > 10:
            bbox = font.getbbox(subtitle)
            if (bbox[2] - bbox[0]) <= max_text_w:
                break
            font_size -= 2
            font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default()

    bbox = font.getbbox(subtitle)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    padding = int(text_h * 0.4)
    canvas_h = base_h + padding + text_h
    canvas = Image.new('RGBA', (base_w, canvas_h), (0, 0, 0, 0))
    canvas.paste(base, (0, 0))

    draw = ImageDraw.Draw(canvas)
    text_x = (base_w - text_w) // 2
    text_y = base_h + padding - bbox[1]
    draw.text((text_x, text_y), subtitle, fill=SUBTITLE_COLOR, font=font)

    canvas.save(out_path)


if __name__ == '__main__':
    from conf import guide_subtitle
    generate_logo(guide_subtitle)
