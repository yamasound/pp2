#!/usr/bin/env python3
#
#[USAGE] ./command.sh [city1 city2 ...]
#[SAMPLE] ./command.sh 秋田 東京 那覇

import json, os, pprint, requests, sys, time
from copy import copy
from pathlib import Path
sys.path.append('../kp1')
from csv_io import CsvIo

class JsonIo(CsvIo):
    def read_json(self, path):
        with open(path, 'r') as f:
            d_data = json.load(f)
        return d_data
    
    def write_json(self, d_data, path):
        os.makedirs(path.parent, exist_ok=True)
        with open(path, 'w') as f:
            json.dump(d_data, f)
            
    def print_json(self, path):
        d_data = self.read_json(path)
        pprint.pprint(d_data)
        
    def conv_dict_to_list(self, d_data):
        def get_val(fc, ts):
            data = copy(fc)
            for t in ts:
                data = data[t]
            return data
        
        l_vals = []
        for fc in d_data['forecasts']:
            tree = [['date'],
                    ['dateLabel'],
                    ['telop'],
                    ['image', 'url'],
                    ['temperature', 'max', 'celsius'],
                    ['temperature', 'min', 'celsius'],
                    ['chanceOfRain', 'T00_06'],
                    ['chanceOfRain', 'T06_12'],
                    ['chanceOfRain', 'T12_18'],
                    ['chanceOfRain', 'T18_24'],
                    ]
            columns = ['title']
            columns.extend(['_'.join(ts) for ts in tree])
            vals = [d_data['title']]
            vals.extend([get_val(fc, ts) for ts in tree])
            l_vals.append(vals)
        return columns, l_vals
    
    def retrieve_weather(self, cities):
        for city in cities:
            path = Path(f"output/weather/{city}.json")
            d_data = self.get_d_weather(city)
            self.write_json(d_data, path)
            #
            path = Path(f"output/weather/{city}.csv")
            columns, l_vals = self.conv_dict_to_list(d_data)
            self.write_csv(l_vals, path, columns)
            
    def get_d_weather(self, city):
        d_city_to_code = {'秋田': '050010', '東京': '130010', '那覇': '471010'}
        code = d_city_to_code[city]
        url = f"https://weather.tsukumijima.net/api/forecast?city={code}"
        response = requests.get(url)
        response.raise_for_status()
        time.sleep(1)
        return response.json() # json.loads(response.text)と同じ
            
class JsonIoDemo(JsonIo, CsvIo):
    def __init__(self):
        self.demo1_read_and_write_json()
        self.demo2_read_json_and_convert_to_csv_and_write_it()
        
    def demo1_read_and_write_json(self):
        path = Path('input/sample.json')
        d_data = self.read_json(path)
        #
        path = Path('output/sample.json')
        self.write_json(d_data, path)
        self.print_json(path)
        
    def demo2_read_json_and_convert_to_csv_and_write_it(self):
        path = Path('input/sample.json')
        d_data = self.read_json(path)
        #
        path = Path('output/sample.csv')
        columns, l_vals = self.conv_dict_to_list(d_data)
        self.write_csv(l_vals, path, columns)
        self.print_csv(path)
        
if __name__ == '__main__':
    if len(sys.argv) == 1:
        JsonIoDemo()
    elif len(sys.argv) > 1:
        cities = sys.argv[1:]
        JsonIo().retrieve_weather(cities)
