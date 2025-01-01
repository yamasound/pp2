#!/usr/bin/env python3

import sys
sys.path.append('../kp1')
from clock import Clock
from weather_html import WeatherHtml

class Weather(WeatherHtml, Clock):
    def __init__(self, city, interval_in_sec):
        self.interval_in_sec = interval_in_sec
        self.maximum_number_of_calls = 10
        self.number_of_calls = 0
        self.city = city
        self.time = False

    def _need_for_update(self):
        if self.diff_in_sec(
                self.machine_time(), self.time) > self.interval_in_sec:
            return True
        else:
            return False
        
    def get_d_data(self):
        if not self.time or self._need_for_update():
            print(f"Retrieving weather data for {self.city}...")
            self.retrieve_weather([self.city])
            self.time = self.machine_time()
            self.number_of_calls += 1
            if self.number_of_calls > self.maximum_number_of_calls:
                print('Maximum number of calls has been exceeded!')
                exit(0)
        items = self.get_items(self.city)
        d_data = {'title': items[0]['title'], 'items': items}
        return d_data

class WeatherData():
    def __init__(self, interval_in_sec=3600):
        self.interval_in_sec = interval_in_sec
        self.d_weather = {}

    def get_d_data(self, city):
        if city not in self.d_weather.keys():
            self.d_weather[city] = Weather(city, self.interval_in_sec)
        weather = self.d_weather[city]
        return weather.get_d_data()
        
if __name__ == '__main__':
    wd = WeatherData()
    wd.get_d_data('秋田')
    wd.get_d_data('秋田') # 短時間で再実行してもデータは再取得されない
