#!/usr/bin/env python3

USAGE = '''
[USAGE]
  ./command.sh file_ext max_size_kilobyte

[SAMPLE]
  ./command.sh txt 1
  ./command.sh jpg 1000
'''

import os, shutil, sys

def main(ext, max_size):
    dir_input = 'input'
    dir_output = f"output/{ext}"
    os.makedirs(dir_output, exist_ok=True)
    for dir_name, _, file_names in os.walk(dir_input):
        for file_name in file_names:
            if file_name.lower().endswith(f".{ext}".lower()):
                path_name = os.path.join(dir_name, file_name)
                size = int(os.path.getsize(path_name) / pow(10, 3))
                if size <= max_size:
                    print(f".. Copy:   {path_name} -> {dir_output}")
                    shutil.copy(path_name, dir_output)
                else:
                    print(f".. Ignore: {path_name} ({size}[kByte])" )

if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1], int(sys.argv[2]))
    else:
        print(USAGE)
