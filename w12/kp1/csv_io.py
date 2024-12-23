#!/usr/bin/env python3

import csv, os, unittest
from pathlib import Path

class CsvIo():
    def write_csv(self, l_vals, path, columns=False):
        os.makedirs(path.parent, exist_ok=True)
        with open(path, 'w') as f:
            writer = csv.writer(f)
            if columns:
                writer.writerow(columns)
            for vals in l_vals:
                writer.writerow(vals)
    
    def read_csv(self, path, columns=False):
        with open(path, 'r') as f:
            l_vals = []
            for vals in csv.reader(f):
                if str(vals[0]).strip()[0] == '#':
                    continue
                if not columns:
                    columns = vals
                    continue
                l_vals.append(vals)
        return columns, l_vals

    def print_csv(self, path):
        columns, l_vals = self.read_csv(path)
        length = sum([int(len(c)) for c in columns]) + len(columns) - 1
        print('#' * length)
        print(','.join(columns))
        print('#' * length)
        for vals in l_vals:
            print(','.join(vals))

class CsvIoTest(unittest.TestCase, CsvIo):
    columns = ['code', 'city']
    l_code_and_city = [
        ['050010', '秋田'],
        ['130010', '東京'],
        ['471010', '那覇'],
    ]
    path = Path('output/code_and_city.csv')
    
    def test1_columns(self):
        self.write_csv(self.l_code_and_city, self.path, self.columns)
        columns, _ = self.read_csv(self.path)
        self.assertTrue(self.columns == columns)
        
    def test2_l_vals(self):
        self.write_csv(self.l_code_and_city, self.path, self.columns)
        _, l_code_and_city = self.read_csv(self.path)
        a = self.l_code_and_city
        b = l_code_and_city
        cs = [a == b for a, b in zip(a, b)]
        self.assertTrue(len(a) == len(b) and all(cs))

    def test3_print(self):
        print('')
        self.print_csv(self.path)

if __name__ == '__main__':
    unittest.main()
