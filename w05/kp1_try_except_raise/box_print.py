#!/usr/bin/env python3

def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('symbolは1文字の文字列でなければならない．')
    if width <= 2:
        raise Exception('widthは2より大きくなければならない．')
    if height <= 2:
        raise Exception('heightは2より大きくなければならない．')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for symbol, width, height in (
        ('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(symbol, width, height)
    except Exception as err:
        print('例外が起こりました: ' + str(err))
