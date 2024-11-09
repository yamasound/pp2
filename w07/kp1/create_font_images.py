#!/usr/bin/env python3

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def get_fonts():
    fonts = []
    fs = ['NotoSerifCJK', 'NotoSansCJK']
    ts = ['ExtraLight', 'Light', 'Regular', 'Medium', 'SemiBold', 'Black']
    for f in fs:
        for t in ts:
            fonts.append(f"/usr/share/fonts/opentype/noto/{f}-{t}.ttc")
    return fonts
    
def main():
    text = 'Fontイメージの表示'
    font_size = 20
    im_width = 400
    path_output = Path('output/font_images.png')
    
    os.makedirs(path_output.parent, exist_ok=True)
    fonts = get_fonts()
    im = Image.new('RGBA', (im_width, (font_size + 25) * len(fonts)), 'white')
    draw = ImageDraw.Draw(im)
    y = 0
    for font in fonts:
        try:
            y += 3
            draw.text((0, y), font, fill='red')
            y += 10
            draw.text((10, y), text, fill='black',
                      font=ImageFont.truetype(font, font_size))
        except:
            pass
        y += font_size + 12
        draw.line(((0, y), (im_width, y)), fill='black')
    im.save(path_output)

if __name__ == '__main__':
    main()
