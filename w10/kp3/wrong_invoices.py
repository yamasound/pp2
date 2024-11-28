#!/usr/bin/env python3

import ezsheets, re, sys
sys.path.append('../kp1')
from google_sheets import GoogleSheets

class WrongInvoices(GoogleSheets):
    def __init__(self, name):
        org_ssid = '17ac2UBtvIQSLJ468s4ag9DoLlrvZA6pcD88jgf_E19U'
        GoogleSheets.__init__(self, name, org_ssid)
        self.org_ss = ezsheets.Spreadsheet(org_ssid)
        
    def correct(self):
        for sheet_no in range(len(self.org_ss.sheets)):
            self._correct_sheet(sheet_no)
            
    def _correct_sheet(self, sheet_no):
        org_s = self.org_ss.sheets[sheet_no]
        subtotal = 0
        for row in range(17, 41):
            amount = self._int(org_s[9, row]) * self._int(org_s[11, row])
            subtotal += amount
            self._correct_cell(sheet_no, org_s, 13, row, amount)
        sales_tax = int(subtotal * 0.1); total = subtotal + sales_tax
        self._correct_cell(sheet_no, org_s, 13, 42, subtotal)
        self._correct_cell(sheet_no, org_s, 13, 43, sales_tax)
        self._correct_cell(sheet_no, org_s, 13, 44, total)
        self._correct_cell(sheet_no, org_s, 5, 11, total)
        
    def _correct_cell(self, sheet_no, org_s, col, row, truth):
        s = self.ss.sheets[sheet_no]
        value = self._int(org_s[col, row])
        if value != truth:
            s[col, row] = truth
            message = f"The value {value} in the row {row} and column {col} "
            message += f"on the sheet {sheet_no + 1} should be {truth}."
            print(message)
            
    def _int(self, value):
        try:
            if isinstance(value, str):
                value = re.sub('¥|,|\s+', '', value)
            return int(value)
        except:
            return 0
        
if __name__ == '__main__':
    WrongInvoices('pp2_w10_kp3').correct()
