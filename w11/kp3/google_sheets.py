#!/usr/bin/env python3
#
# [USAGE] ./command.sh [original_google_spread_sheet_id]

import ezsheets, os, shelve, sys

class GoogleSheets():
    def __init__(self, name, org_ssid=False):
        os.chdir('../output')
        self.ss = self.get_ss(name, org_ssid)
        
    def get_ss(self, name, org_ssid):
        with shelve.open('ssid') as d:
            try:
                if org_ssid:
                    ss = self.duplicate(org_ssid, name)
                    d[name] = ss.id
                else:
                    ssid = d[name]
                    ss = ezsheets.Spreadsheet(ssid)
            except:
                ss = ezsheets.createSpreadsheet(title=name)
                d[name] = ss.id
        return ss

    def duplicate(self, org_ssid, new_name):
        org_ss = ezsheets.Spreadsheet(org_ssid)
        org_fname = f"{org_ss.title}.xlsx"
        new_fname = f"{new_name}.xlsx"
        org_ss.downloadAsExcel()
        os.rename(org_fname, new_fname)
        new_ss = ezsheets.upload(new_fname)
        os.remove(new_fname)
        return new_ss

if __name__ == '__main__':
    if len(sys.argv) == 2:
        GoogleSheets('pp2_w10_kp1', sys.argv[1])
    else:
        GoogleSheets('pp2_w10_kp1')
