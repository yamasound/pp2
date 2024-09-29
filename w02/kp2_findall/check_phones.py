#!/usr/bin/env python3

import re

# 日本の電話番号の正規表現を作る
phone_regex = re.compile(r'''(
    (0\d{0,3}|\(\d{0,3}\))           # 市外局番
    (\s|-)                           # 区切り
    (\d{1,4})                        # 市内局番
    (\s|-)                           # 区切り
    (\d{3,4})                        # 加入者番号
    (\s*(ext|x|ext.)\s*(\d{2,5}))?   # 内線番号
    )''', re.VERBOSE)

# テキストから電話番号を抽出する
with open('input/juroku.txt', 'r', encoding='utf-8') as fi:
    for groups in phone_regex.findall(str(fi.readlines())):
        print(groups[0])
