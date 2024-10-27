#!/usr/bin/env python3

USAGE = '[USAGE] ./command.sh n [DEBUG | INFO | WARNING | ERROR | CRITICAL]'

import logging, os, sys, time
from pathlib import Path

def factorial(n):
    logging.debug(f"factorial({n})開始")
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug(f"i = {i}, total = {total}")
        time.sleep(0.1)
    logging.debug(f"factorial({n})終了")
    return total

def main(n, log_level):
    path_log = Path('output/log.txt')
    os.makedirs(path_log.parent)
    logging.basicConfig(
        filename=str(path_log), level=getattr(logging, log_level),
        format='%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')
    logging.info('プログラム開始')
    print(factorial(n))
    logging.info('プログラム終了')

if __name__ == '__main__':
    if 1 < len(sys.argv) and len(sys.argv) < 4:
        n = int(sys.argv[1])
        if len(sys.argv) == 2:
            log_level = 'INFO'
            main(n, log_level)
        elif sys.argv[2] in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
            log_level = sys.argv[2]
            main(n, log_level)
        else:
            print(USAGE)
    else:        
        print(USAGE)
