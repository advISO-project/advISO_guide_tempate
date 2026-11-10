"""Generate button images from button_base.png, guide_subtitle, and sidebar_color."""

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SUBTITLE_COLOR = (23, 24, 23)

FONT_BOLD_CANDIDATES = [
    ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 0),
    ('/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf', 0),
    ('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 0),
    ('/System/Library/Fonts/Helvetica.ttc', 1),                     # macOS Bold
    ('C:/Windows/Fonts/arialbd.ttf', 0),                            # Windows
]

FONT_BOLD_ITALIC_CANDIDATES = [
    ('/usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf', 0),
    ('/usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf', 0),
    ('/usr/share/fonts/truetype/freefont/FreeSansBoldOblique.ttf', 0),
    ('/System/Library/Fonts/Helvetica.ttc', 3),                     # macOS Bold Oblique
    ('C:/Windows/Fonts/arialbi.ttf', 0),                            # Windows
]


def _find_font(italic=False):
    candidates = FONT_BOLD_ITALIC_CANDIDATES if italic else FONT_BOLD_CANDIDATES
    for path, index in candidates:
        if os.path.exists(path):
            return path, index
    return None, 0


def _hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def _rounded_rect(size, radius, fill):
    """Create an RGBA image with a rounded rectangle."""
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([(0, 0), (size[0]-1, size[1]-1)], radius=radius, fill=fill)
    return img


def _fit_font(font_path, text, max_width, start_size, index=0):
    """Find the largest font size that fits text within max_width."""
    font_size = start_size
    font = ImageFont.truetype(font_path, font_size, index=index)
    while font_size > 10:
        bbox = font.getbbox(text)
        if (bbox[2] - bbox[0]) <= max_width:
            return font
        font_size -= 2
        font = ImageFont.truetype(font_path, font_size, index=index)
    return font


def generate_button(subtitle, bg_color, static_dir=None):
    """Generate a 1800x300 horizontal button image."""
    if static_dir is None:
        static_dir = Path(__file__).parent / 'source' / '_static'
    else:
        static_dir = Path(static_dir)

    base_path = static_dir / 'button_base.png'
    out_path = static_dir / 'button_horizontal.png'

    bg_rgb = _hex_to_rgb(bg_color) if isinstance(bg_color, str) else bg_color

    width, height = 1800, 300
    padding_x = 15
    padding_y = 10
    corner_radius = 30

    canvas = _rounded_rect((width, height), corner_radius, (*bg_rgb, 255))

    base = Image.open(base_path).convert('RGBA')
    base_w, base_h = base.size
    logo_h = height - (padding_y * 2)
    logo_scale = logo_h / base_h
    logo_w = int(base_w * logo_scale)
    logo = base.resize((logo_w, logo_h), Image.LANCZOS)
    logo_y = (height - logo_h) // 2
    canvas.paste(logo, (padding_x, logo_y), logo)

    draw = ImageDraw.Draw(canvas)

    font_path, font_index = _find_font(italic=True)
    text_left = padding_x + logo_w + 25
    text_area_w = width - text_left - padding_x
    if font_path:
        font = _fit_font(font_path, subtitle, text_area_w, int(height * 0.55), index=font_index)
    else:
        font = ImageFont.load_default()

    bbox = font.getbbox(subtitle)
    text_h = bbox[3] - bbox[1]
    text_y = (height - text_h) // 2 - bbox[1]
    draw.text((text_left, text_y), subtitle, fill=SUBTITLE_COLOR, font=font)

    canvas.save(out_path)
    return out_path


def generate_website_banner(subtitle, bg_color, static_dir=None):
    """Generate a 16:9 website banner image."""
    if static_dir is None:
        static_dir = Path(__file__).parent / 'source' / '_static'
    else:
        static_dir = Path(static_dir)

    base_path = static_dir / 'logo_base_16x9.png'
    out_path = static_dir / 'button_website.png'

    bg_rgb = _hex_to_rgb(bg_color) if isinstance(bg_color, str) else bg_color

    base = Image.open(base_path).convert('RGBA')
    base_w, base_h = base.size

    width = base_w
    height = base_h
    corner_radius = 40

    canvas = _rounded_rect((width, height), corner_radius, (*bg_rgb, 255))
    canvas.paste(base, (0, 0), base)

    # Find where the 'advISO' text starts and ends vertically (pure Pillow)
    alpha = base.split()[3]
    pixels = alpha.load()

    # Column sums for x > 1000 to find where advISO text starts
    col_sums = []
    for x in range(1000, width):
        s = sum(pixels[x, y] for y in range(height))
        col_sums.append(s)
    max_col = max(col_sums)
    threshold = max_col * 0.02
    text_x_start = next(i for i, s in enumerate(col_sums) if s > threshold) + 1000

    # Row sums in the text region to find bottom of advISO
    row_sums = []
    for y in range(height):
        s = sum(pixels[x, y] for x in range(1000, width))
        row_sums.append(s)
    max_row = max(row_sums)
    threshold_r = max_row * 0.02
    text_y_bottom = max(y for y, s in enumerate(row_sums) if s > threshold_r)

    font_path, font_index = _find_font()
    max_text_w = width - text_x_start - 40
    if font_path:
        font = _fit_font(font_path, subtitle, max_text_w, int(height * 0.10), index=font_index)
    else:
        font = ImageFont.load_default()

    bbox = font.getbbox(subtitle)
    draw = ImageDraw.Draw(canvas)
    gap = int(height * 0.08)
    text_y = text_y_bottom + gap - bbox[1]
    draw.text((text_x_start, text_y), subtitle, fill=SUBTITLE_COLOR, font=font)

    canvas.save(out_path)
    return out_path


def generate_buttons(subtitle, bg_color, static_dir=None):
    """Generate all button variants."""
    generate_button(subtitle, bg_color, static_dir)
    generate_website_banner(subtitle, bg_color, static_dir)


if __name__ == '__main__':
    from conf import guide_subtitle, sidebar_color
    generate_buttons(guide_subtitle, sidebar_color)
