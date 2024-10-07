#!/usr/bin/env python3

import re

# 前後にcharsの0回以上の繰り返しを持つ非貪欲マッチをする
def restrip(s, chars=r'\s'):
    return re.sub('^[' + chars + ']*(.*?)[' + chars + ']*$', r'\1', s)

def compare_restrip_and_strip(args):
    print('## compare_restrip_and_strip ##')
    for arg in args:
        rs = restrip(arg)
        ss = arg.strip()
        eq = '==' if rs == ss else '!='
        print("restrip('{}')->'{}' {} '{}'.strip()->'{}'".format(
            arg, rs, eq, arg, ss))
    
def compare_restrip_and_strip_for_EG(args):
    print('## compare_restrip_and_strip_for_EG ##')
    for arg in args:
        rs = restrip(arg, 'EG')
        ss = arg.strip('EG')
        eq = '==' if rs == ss else '!='
        left = f"restrip('{arg}', 'EG')->'{rs}'"
        right = f"'{arg}'.strip('EG')->'{ss}'"
        print(f"{left} {eq} {right}")

if __name__ == '__main__':
    args = [' spam ', '  spam  ', ' spam', 'spam ', 'spam', ' spam spam ']
    compare_restrip_and_strip(args)
    
    args = ['EspamG', 'EspamG', 'EGspamEG', ' EspamG ', 'Espam', 'spamE',
            'spam', 'EspamEspamE']
    compare_restrip_and_strip_for_EG(args)
