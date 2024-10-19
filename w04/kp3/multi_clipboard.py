#!/usr/bin/env python3

USAGE = '''[USAGE]
./command.sh - キーワードをクリップボードに格納
./command.sh save <keyword> - クリップボードの内容をキーワードに紐づけて保存
./command.sh load <keyword> - キーワードに紐づけた内容をクリップボードに格納
./command.sh delete <keyword> - キーワードを削除
./command.sh delete all - 全てのキーワードを削除'''

import os, pyperclip, shelve, sys
from pathlib import Path

def main(argv, path_output):
    def kwds_to_clip_borad():
        # キーワードのリストをクリップボードに格納
        pyperclip.copy(f"{list(shv.keys())}\n")
        
    os.makedirs(path_output.parent, exist_ok=True)
    with shelve.open(str(path_output)) as shv:
        if len(argv) == 1:
            kwds_to_clip_borad()
            print(USAGE)
        elif len(argv) == 3:
            cmd, kwd = argv[1:3]
            if cmd == 'save':
                # クリップボードをキーワードに紐づけて保存
                shv[kwd] = pyperclip.paste()
                kwds_to_clip_borad()
            elif cmd == 'load':
                # キーワードに紐づけられた内容をクリップボードに格納
                if kwd in shv.keys():
                    pyperclip.copy(shv[kwd])
                else:
                    kwds_to_clip_borad()
            elif cmd == 'delete':
                if kwd != 'all':
                    # キーワードに紐づけられた内容を削除
                    del shv[kwd] 
                else:
                    # 保存した内容を全て削除
                    shv.clear()
                kwds_to_clip_borad()

if __name__ == '__main__':
    path_output = Path('output', 'mcb')
    main(sys.argv, path_output)
