#!/usr/bin/env python3

import os, shutil
from pathlib import Path

def write(path, i):
    os.makedirs(path.parent, exist_ok=True)
    with open(path, 'w') as f:
        for j in range(1, i + 1):
            f.write(f'{j}\n')
        f.write('最終行')  

def reset_dir(dname):
    try:
        shutil.rmtree(dname)
    except:
        pass
    
def main():
    dname = 'output/txt'
    ext = 'txt'
    reset_dir(dname)
    for i in range(1, 6):
        write(Path(dname, f"d{i:02d}.{ext}"), i)
        
if __name__ == '__main__':
    main()
