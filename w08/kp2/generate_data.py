#!/usr/bin/env python3

import os, shutil
from pathlib import Path

def write(path, i):
    os.makedirs(path.parent, exist_ok=True)
    with open(path, 'w') as f:
        f.write(str(i))

def reset_dir(dname):
    try:
        shutil.rmtree(dname)
    except:
        pass
    
def main():
    dname = 'output/data'
    reset_dir(dname)
    for i in range(1, 13):
        d = f"{dname}/sub" if i % 3 == 0 else dname
        ext = 'txt' if i % 2 == 0 else 'csv'
        write(Path(d, f"d{i:02d}.{ext}"), i)
        
if __name__ == '__main__':
    main()
