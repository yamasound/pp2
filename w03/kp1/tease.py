#!/usr/bin/env python3

import pyinputplus as pyip

while True:
    prompt = '人を何時間も忙しくさせておく方法を知りたいですか？\n'

    response = pyip.inputYesNo(prompt, yesVal='はい', noVal='いいえ')
    if response == 'いいえ':
        break

print('ありがとう，ごきげんよう．')

