#!/usr/bin/env python3

import os
from pathlib import Path
from PIL import Image

def add_logo_to_image(logo, image, output_path, ratio=0.3):
    # ロゴのサイズを変更する
    width, height = image.size
    logo_image, logo_width, logo_height = logo.get_logo(int(width * ratio))
    # ロゴを追加する
    image.paste(logo_image, (width - logo_width, height - logo_height),
                logo_image)
    # ロゴ付きの画像を保存する
    os.makedirs(output_path.parent, exist_ok=True)
    image.save(output_path)

class Logo():
    def __init__(self, path):
        self.path = path
        self.image = Image.open(path)

    def get_logo(self, size):
        image = self.image.resize((size, size))
        width, height = image.size
        return image, width, height
    
def main():
    dir_input = 'input'
    file_logo = 'catlogo.png'
    dir_output = 'output'
    
    logo = Logo(os.path.join(dir_input, file_logo))
    for filename in os.listdir(dir_input):
        input_path = Path(os.path.join(dir_input, filename))
        if str(input_path) == str(logo.path):
            continue
        if input_path.suffix.lower() in ['.bmp', '.gif', '.jpg', '.png']:
            image = Image.open(input_path)
            output_path = Path(os.path.join(dir_output, filename))
            add_logo_to_image(logo, image, output_path)
        
if __name__ == '__main__':
    main()
