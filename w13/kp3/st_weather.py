#!/usr/bin/env python3

import streamlit as st, sys, time
sys.path.extend(['../kp1', '../kp2'])
from clock import Clock
from st_clock import StClock
from weather_data import WeatherData

class StWeather(StClock, WeatherData, Clock):
    def __init__(self, interval_in_sec):
        self.interval_in_sec = interval_in_sec
        self.wd = WeatherData(interval_in_sec=3600) # 提供元に迷惑をかけない
        self.city = '秋田'

    def show_on_sidebar(self, worker):
        self.thread_or_process(worker)
        self.city = st.radio('City:', ('秋田', '東京', '那覇'))
        
    def html_for_one_day(self, d_data, day):
        i = d_data['items'][day]
        html = f"""
          <div style="background-color:#FAFAFA; border:5px solid #CCC;">
            <b><font size=4>{i['dateLabel']}</font> - {i['date']}</b>
            <br>
              {i['telop']}<br>
              <img src="{i['image_url']}">
            <br>
                気温
                <font color="red">{i['temperature_max_celsius']}℃</font>
                <font color="blue">{i['temperature_min_celsius']}℃</font>
            <br>
                降水確率
                <font color="blue">
                  {i['chanceOfRain_T00_06']}
                  {i['chanceOfRain_T06_12']}
                  {i['chanceOfRain_T12_18']}
                  {i['chanceOfRain_T18_24']}
                </font>
          </div>
          <br>
        """
        return html
    
    def html_for_three_days(self, d_data):
        html = ''
        for day in range(3):
            html += self.html_for_one_day(d_data, day)
        return html
        
    def show(self, worker):
        placeholder1 = st.empty()
        placeholder2 = st.empty()
        while worker.is_alive():
            d_data = self.wd.get_d_data(self.city)
            title = f"<b><font size=5>{d_data['title']}</font>"
            title += f" - {self.str_time(self.machine_time())[:-7]} 現在</b>"
            html = self.html_for_three_days(d_data)
            placeholder1.markdown(title, unsafe_allow_html=True)
            placeholder2.markdown(html, unsafe_allow_html=True)
            time.sleep(self.interval_in_sec)
            
if __name__ == '__main__':
    method = sys.argv[2] if len(sys.argv) == 3 else 'threading'
    StWeather(interval_in_sec=1).main(method)
