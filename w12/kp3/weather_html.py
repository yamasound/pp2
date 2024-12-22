#!/usr/bin/env python3

USAGE = '''
[USAGE] ./command.sh city1 [city2 ...]
[SAMPLE] ./command.sh 秋田 東京 那覇
'''

import os, sys
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
sys.path.append('../kp2')
from json_io import JsonIo

class WeatherHtml(JsonIo):
    def __init__(self, cities):
        self.retrieve_weather(cities)
        self.create_html(cities)
        
    def create_html(self, cities):
        for city in cities:
            items = self.get_items(city)
            d_data = {'title': items[0]['title'], 'items': items}
            env = Environment(loader=FileSystemLoader('input'))
            html = env.get_template('template.html').render(d_data)
            path = Path(f"output/weather/{city}.html")
            self.write_html(path, html)
        
    def get_items(self, city):
        path = Path(f"output/weather/{city}.csv")
        column, l_vals = self.read_csv(path)
        return [{c: v for c, v in zip(column, vals)} for vals in l_vals]
    
    def write_html(self, path, html):
        os.makedirs(path.parent, exist_ok=True)
        with open(path, 'w') as f:
            f.write(html)
        
if __name__ == '__main__':
    if len(sys.argv) > 1:
        cities = sys.argv[1:]
        WeatherHtml(cities)
    else:
        print(USAGE.strip())
