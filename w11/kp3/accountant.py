#!/usr/bin/env python3

from collections import defaultdict
import ezsheets, shelve, re, sys
sys.path.append('../kp2')
from gmail_db import GmailDb
from google_sheets import GoogleSheets

class Accountant(GmailDb, GoogleSheets):
    def _get_ss(self, name):
        org_ssid = '1tHcpMC_Tj9MSkCpXAvIl4tldjxo8wPJZv7uBSigRjF4'
        with shelve.open('ssid') as d:
            try:
                ssid = d[name]
                ss = ezsheets.Spreadsheet(ssid)
            except:
                print('Duplicating from original Google sheets')
                ss = self.duplicate(org_ssid, name)
                d[name] = ss.id
                s = ss.sheets[0]
                s['A2'] = self.mail
        return ss
    
    def update_payment(self):
        print('=== update_payment ===')
        ss = self._get_ss(self.name)
        s = ss.sheets[2]
        mails = self._get_mails(s)
        periods = self._get_periods(s)
        l_timestamp_and_sender_and_line = self.search(
            subject='pp2_w11_kp3', words=['年', '月', '円', 'OK'])
        for timestamp, sender, line in l_timestamp_and_sender_and_line:
            period = re.findall(r'\b[0-9]+年[0-9]+月\b', line)[0]
            fee = int(re.findall(r'\b[0-9,]+円', line
                                 )[0].replace(',','').replace('円',''))
            s[self._col(periods, period), self._row(mails, sender)] = fee
            
    def _get_mails(self, s):
        mails = []
        row = 2; mail = s[1, row]
        while mail != '':
            mails.append(mail)
            row += 1; mail = s[1, row]
        return mails
    
    def _get_periods(self, s):
        periods = []
        col = 2; period = s[col, 1]
        while period != '':
            periods.append(period)
            col += 1; period = s[col, 1]
        return periods
    
    def _row(self, mails, mail):
        i = mails.index(mail)
        if i < 0:
            raise ValueError('Wrong mail specified!')
        else:
            return i + 2
        
    def _col(self, periods, period):
        i = periods.index(period)
        if i < 0:
            raise ValueError('Wrong period specified!')
        else:
            return i + 2
        
    def send_remind_mail(self):
        print('=== send_remind_mail ===')
        ss = self._get_ss(self.name)
        s = ss.sheets[3]
        for mail, l_period_and_fee in self._get_d_unpaid(s).items():
            subject = 'Reminder to pay membership fee'
            body = '以下の会費が未納ですので，お支払をお願いします．\n'
            body += 'お支払が済みましたら，該当する会費のそれぞれの行末に\n'
            body += 'OKと追記して返信してください．\n'
            for period, fee in l_period_and_fee:
                body += f"\n{period} {fee:,}円"
            print(f"{mail}\n{subject}\n{body}")
            self.send_mail(to=mail, subject=subject, body=body)
            
    def _get_d_unpaid(self, s):
        periods = self._get_periods(s)
        row = 2; mail = s[1, row]
        d_unpaid = defaultdict(list)
        while mail.find('@') > 1:
            for period in periods:
                fee = int(s[self._col(periods, period), row].replace(',',''))
                if fee > 0:
                    d_unpaid[mail].append([period, fee])
            row += 1; mail = s[1, row]
        return d_unpaid    

if __name__ == '__main__':
    a = Accountant('pp2_w11_kp3')
    a.update_payment()
    a.send_remind_mail()
