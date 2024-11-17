#!/usr/bin/env python3

import sys
from glob import glob
from pathlib import Path
sys.path.append('../kp2')
from snapshot import Snapshot

class GenerationalSnapshot(Snapshot):
    def next_path_snapshot(self):
        try:
            fs = glob(f"{self.dir_snapshot}/*.zip")
            i = sorted([int(Path(f).stem) for f in fs])[-1] + 1
        except:
            i = 1
        return Path(f"{self.dir_snapshot}/{i}.zip")
        
if __name__ == '__main__':
    gs = GenerationalSnapshot()
    gs.save(gs.next_path_snapshot())
