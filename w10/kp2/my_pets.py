#!/usr/bin/env python3

import sys
sys.path.append('../kp1')
from google_sheets import GoogleSheets

class MyPets(GoogleSheets):
    def __init__(self, name):
        GoogleSheets.__init__(self, name)

    def write_my_pets(self):
        s = self.ss.sheets[0]
        s['A1'] = 'My pets'
        s[1, 3] = 'Name';  s[2, 3] = 'Species';
        s[3, 3] = 'Color'; s[4, 3] = 'Weight'
        s.updateRow(4, ['Zophie', 'Cat', 'Gray', 10])
        s.updateRow(5, ['Poggy', 'Dog', 'Brown', 15])
    
if __name__ == '__main__':
    MyPets('pp2_w10_kp2').write_my_pets()
