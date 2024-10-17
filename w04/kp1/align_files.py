#!/usr/bin/env python3

import os, re, shutil
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
    
if __name__ == '__main__':
    dir_input = 'input'
    dir_output = 'output'
    pattern = '.+\.(jpg|jpeg|png)$'
    align_files(dir_input, dir_output, pattern)
