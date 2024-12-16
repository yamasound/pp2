#!/usr/bin/env python3

import datetime, ezgmail, os

class Gmail():
    def __init__(self, name=''):
        os.chdir('../output')
        self.name = name
        self.mail = self._get_mail()
        self.dt = str(datetime.datetime.now())[:19]

    def _get_mail(self):
        try:
            return ezgmail.init()
        except:
            os.remove('token.json')
            return ezgmail.init()

    def send_mail(self, to=False, subject='', body=''):
        ezgmail.send(f"{to if to else self.mail}",
                     f"[{self.name}] {subject}",
                     f"{self.dt}時点のご連絡です．\n\n{body}")

if __name__ == '__main__':
    Gmail('pp2_w11_kp1').send_mail(subject='Test mail')
