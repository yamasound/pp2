#!/usr/bin/env python3

USAGE = '[USAGE] ./command.sh keyword1 [keyword2 ...]'

import bs4, os, requests, sys

def get_soup(keywords):
    res = requests.get(f"https://www.flickr.com/search/?text={keywords}")
    res.raise_for_status() # アクセスに失敗したら例外を起こす
    return bs4.BeautifulSoup(res.text, 'html.parser') # 標準のパーサーを使用

def get_images(url, fname):
    res = requests.get(url)
    res.raise_for_status() # アクセスに失敗したら例外を起こす
    with open(fname, 'wb') as f:
        for chunk in res.iter_content(100000): # 100kByteずつファイルへ書き込む
            f.write(chunk)

def main(argv, dir_output='output', limit_images=5):
    soup = get_soup(keywords=' '.join(argv[1:]))
    imgs = soup.select('.photo-list-photo-view img')
    # ドットはCSSクラス属性を表し，たとえば，.photo-list-photo-viewは
    # <div class="photo-list-photo-view">などのタグにマッチする．
    # imgは<img ...>を検索する．
    os.makedirs(dir_output, exist_ok=True)
    for i in range(min(limit_images, len(imgs))):
        part_of_url = imgs[i].get('src')
        url = f"https:{part_of_url}"
        fname = os.path.join(dir_output, os.path.basename(part_of_url))
        print(url, fname)
        get_images(url, fname)
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv)
    else:
        print(USAGE)
