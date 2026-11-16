#!/usr/bin/env python3
#
# Googleのスクレイピングが禁止されたので
# DuckDuckGoのAPIで情報を集める

USAGE = '[USAGE] ./command.sh keyword1 [keyword2 ...]'

from ddgs import DDGS
import json, sys, webbrowser, time

def search(keywords, limit_pages):
    return list(DDGS().text(
        keywords,
        region='wt-wt',         # リージョン 日本に限定する場合は"jp-jp"
        safesearch='moderate',  # セーフサーチ on, off, moderate
        timelimit=None,         # 期間指定 None: 指定なし, d: 過去1日,
                                #   w: 過去1週間, m: 過去1か月, y: 過去1年
        max_results=limit_pages # 取得件数
    ))

def main(argv, limit_pages=3):
    keywords = ' '.join(argv[1:])
    urls = [s['href'] for s in search(keywords, limit_pages)]
    browser = webbrowser.get()
    for url in urls:
        browser.open(url)
        time.sleep(1)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv)
    else:
        print(USAGE)
