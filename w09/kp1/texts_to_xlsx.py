#!/usr/bin/env python3

from glob import glob
import openpyxl
from pathlib import Path

def main():
    path_output = Path('output/texts.xlsx')
    book = openpyxl.Workbook()
    for col, path_name in enumerate(sorted(glob(
            f"{path_output.parent}/txt/*.txt")), 1):
        with open(Path(path_name), 'r') as f:
            for row, line in enumerate(f.readlines(), 1):
                book.active.cell(row=row, column=col).value = line.strip()
    book.save(path_output)
    
if __name__ == '__main__':
    main()
