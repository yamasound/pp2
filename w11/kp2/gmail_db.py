#!/usr/bin/env python3

import ezgmail, re, sys, unicodedata
sys.path.append('../kp1')
from gmail import Gmail

class GmailDb(Gmail):
    def _extract_mail_address(self, text):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.findall(pattern, text)[0]
    
    def search(self, subject, words):
        threads = ezgmail.search(f"subject:{subject}")
        print(f"{len(threads)}本のスレッドが件名に{subject}を含んでいます．")
        l_timestamp_and_sender_and_line = []
        for thread in threads:
            for message in thread.messages:
                for line in message.body.strip().split('\n'):
                    if all([word.lower() in unicodedata.normalize(
                            'NFKC', line).lower() for word in words]):
                        sender = self._extract_mail_address(message.sender)
                        l_ = [str(message.timestamp), sender, line]
                        l_timestamp_and_sender_and_line.append(l_)
                        print(', '.join(l_))
        return l_timestamp_and_sender_and_line

if __name__ == '__main__':
    gd = GmailDb()
    gd.search(subject='pp2_w11_kp1', words=['時点'])
