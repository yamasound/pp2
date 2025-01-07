#!/usr/bin/env python3

import pyautogui
from time import sleep

def repeat(key, n):
    for _ in range(n):
        print(f"press - {key}")
        pyautogui.press(key)
        sleep(0.1)

def main():
    sleep(1)
    print('Begin - autopilot')
    
    print('keyDown - right')
    pyautogui.keyDown('right')

    for _ in range(5):
        repeat('space', 3)
        sleep(0.7)
    
    print('keyUp - right')
    pyautogui.keyUp('right')
    
    print('End - autopilot')
    
if __name__ == '__main__':
    pyautogui.PAUSE = 0.1
    main()
