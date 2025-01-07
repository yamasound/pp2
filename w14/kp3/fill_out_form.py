#!/usr/bin/env python3
#
USAGE='[USAGE] ./command.sh (u1 / u2)'

import pyautogui, pyperclip, sys, time

class FillOutForm():
    def __init__(self, d):
        self.d = d
        self.name()
        self.gender()
        self.food()
        self.hair()
        self.comments()
        self.submit()
        
    def jp_write(self, s):
        saved_clipboard = pyperclip.paste()
        pyperclip.copy(s)
        pyautogui.hotkey('ctrl', 'v') # macOSの場合は 'command'
        pyperclip.copy(saved_clipboard)
        
    def name(self):
        tab_name = self.d['tab_name']
        pyautogui.hotkey('ctrl', f"{self.d['tab_name']}")
        pyautogui.press('\t')
        self.jp_write(self.d['name'])
        pyautogui.press('\t')

    def gender(self):
        r = [i for i, t in enumerate(self.d['gender']) if t[1] == 1][0]
        pyautogui.press('down', presses=r)
        pyautogui.press('space')
        pyautogui.press('\t')

    def food(self):
        for t in self.d['food']:
            if t[1] == 1: pyautogui.press('space')
            pyautogui.press('\t')
            
    def hair(self):
        r = [i for i, t in enumerate(self.d['hair']) if t[1] == 1][0]
        pyautogui.press('\r')
        pyautogui.press('down', presses=r)
        pyautogui.press('\t')
        time.sleep(0.5)
        pyautogui.press('\t')

    def comments(self):
        self.jp_write(self.d['comments'])
        pyautogui.write('\t')
        
    def submit(self):
        time.sleep(1)
        pyautogui.write('\r')
        
if __name__ == '__main__':
    pyautogui.PAUSE = 1
    d1 = {
        'tab_name': 'webscrapingfordatascience.com/postform2/',
        'name': '秋田太郎',
        'gender': [('Male', 1), ('Female', 0), ('Other', 0)],
        'food': [('Pizza', 1), ('Fries', 1), ('Salad', 0)],
        'hair': [('Black', 0), ('Brown', 1), ('Blonde', 0), ('Other', 0)],
        'comments': 'I like bacon pizza.'}
    d2 = {
        'tab_name': 'webscrapingfordatascience.com/postform2/',
        'name': '本荘つばさ',
        'gender': [('Male', 0), ('Female', 0), ('Other', 1)],
        'food': [('Pizza', 1), ('Fries', 0), ('Salad', 1)],
        'hair': [('Black', 0), ('Brown', 0), ('Blonde', 1), ('Other', 0)],
        'comments': 'I like seafood pizza.'}
    
    if len(sys.argv) == 2:
        if sys.argv[1] == 'u1':
            d = d1
        elif sys.argv[1] == 'u2':
            d = d2
        else:
            print(USAGE)
            exit(0)
        FillOutForm(d)
    else:
        print(USAGE)
