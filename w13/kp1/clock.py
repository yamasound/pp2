#!/usr/bin/env python3

import ntplib, requests
from datetime import datetime, timedelta, timezone

class Clock():
    ntp_client = ntplib.NTPClient()
    JST = timezone(timedelta(hours=+9)) # 日本標準時は協定世界時より9時間早い
    
    def get_message(self):
        machine_time = self.str_time(self.machine_time())
        ntp_time = self.str_time(self.ntp_time())
        diff_in_sec = self.diff_in_sec(self.machine_time(), self.ntp_time())
        message = f"使用中の計算機の時刻: {machine_time[:-4]}  \n"
        message += f"NTPで取得した時刻: {ntp_time[:-4]}  \n"
        message += f"誤差（秒）: {diff_in_sec}"
        return message
    
    def str_time(self, t):
        return f"{t.strftime('%Y-%m-%d %H:%M:%S.%f')}"
    
    def machine_time(self):
        return datetime.now(self.JST)
        
    def ntp_time(self):
        ntp_server = '192.168.10.30' # 提供元(ntp.nict.jp)に迷惑をかけない
        response = self.ntp_client.request(ntp_server, version=3)
        unix_time = response.tx_time # 1970年1月1日からの秒数を取得
        return datetime.fromtimestamp(unix_time, tz=self.JST)
    
    def diff_in_sec(self, t1, t2):
        return (t1 - t2).total_seconds()
    
if __name__ == '__main__':
    print(Clock().get_message())
