#!/usr/bin/env python3

USAGE = '[USAGE] ./command.sh keyword1 [keyword2 ...]'

import bs4, requests, sys, webbrowser

def get_soup(keywords):
    res = requests.get(f"https://google.com/search?q={keywords}")
    res.raise_for_status() # アクセスに失敗したら例外を起こす
    return bs4.BeautifulSoup(res.text, 'lxml') # 高速なlxmlパーサーを使用

def main(argv, limit_pages=5):
    soup = get_soup(keywords=' '.join(argv[1:]))
    pages = soup.select('div#main > div > div > div > a')
    for i in range(min(limit_pages, len(pages))):
        part_of_url = pages[i].get('href')
        url = f"https://google.com{part_of_url}"
        print(url)
        webbrowser.open(url)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv)
    else:
        print(USAGE)
