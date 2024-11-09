#!/usr/bin/env python3

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def create_place_card(guest, path_output, width=380, height=300):
    # カードの台紙を用意する
    im_base = Image.new('RGBA', (width, height), 'white')
    
    # 花の画像を貼る
    im_flower = Image.open('input/flower.png')
    im_base.paste(im_flower, (0, 0), im_flower)

    # ゲストの名前を書く
    draw = ImageDraw.Draw(im_base)
    font = ImageFont.truetype(
        '/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc', size=32)
    (_, __, tw, th) = font.getbbox(guest)
    draw.text(((width - tw) / 2, (height - th) / 2), guest, fill='black',
              font=font)

    # カードを縁どる
    draw.rectangle((0, 0, width - 1, height - 1), outline='black')

    # カードの画像を保存する
    os.makedirs(path_output.parent, exist_ok=True)
    im_base.save(path_output)

def main():
    guest_file = open('input/guests.txt', 'r', encoding='utf-8')
    for n, guest in enumerate(guest_file):
        guest = guest.strip()
        if guest == '':
            continue
        create_place_card(guest, Path(f"output/place_card{n}_{guest}.png"))
    
if __name__ == '__main__':
    main()
