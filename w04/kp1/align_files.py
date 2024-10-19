#!/usr/bin/env python3

USAGE = '[USAGE] ./command png,jpg,jpeg'

import os, re, shutil, sys
from pathlib import Path

def align_files(dir_input, dir_output, pattern):
    os.makedirs(dir_output)
    for path, dirs, files in sorted(os.walk(dir_input)):
        print('---')
        print(f"path: {path}")
        print(f"dirs: {sorted(dirs)}")
        for file in sorted(files):
            if re.match(pattern, file):
                pi = Path(path, file)
                po = Path(dir_output, file)
                print(f"file: {pi}, {pi.name}, {pi.stem}, {pi.suffix}")
                shutil.copy(pi, po)

def main(dir_input, dir_output, argv):
    if len(argv) != 2:
        print(USAGE)
    else:
        pattern = f".+\.({argv[1].replace(',','|')})$"
        align_files(dir_input, dir_output, pattern)
    
if __name__ == '__main__':
    dir_input = 'input'
    dir_output = 'output'
    main(dir_input, dir_output, sys.argv)
