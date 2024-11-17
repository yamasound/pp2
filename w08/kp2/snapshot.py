#!/usr/bin/env python3

import os, zipfile
from pathlib import Path

class Snapshot():
    def __init__(self, dir_output='output'):
        self.dir_snapshot = f"{dir_output}/snapshot"
        self.dir_data = f"{dir_output}/data"
        
    def save(self, path_snapshot):
        print(path_snapshot)
        os.makedirs(path_snapshot.parent, exist_ok=True)
        with zipfile.ZipFile(path_snapshot, 'w') as f:
            for dir_name, _, file_names in os.walk(self.dir_data):
                f.write(dir_name)
                for file_name in file_names:
                    f.write(os.path.join(dir_name, file_name))
        
if __name__ == '__main__':
    s = Snapshot()
    s.save(Path(f"{s.dir_snapshot}/1.zip"))
