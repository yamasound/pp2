#!/usr/bin/env python3

import multiprocessing, sys, threading, time
sys.path.append('../kp1')
from clock import Clock

class Worker(Clock):
    def __init__(self, module, report):
        self.method = module.__name__
        self.should_stop = module.Event()
        self.report = report
        
    def run(self):
        while not self.should_stop.wait(0):
            time.sleep(1)
            if self.report:
                print(self.get_message())

class ThWorker(Worker, threading.Thread):
    def __init__(self, module, report, **kwargs):
        Worker.__init__(self, module, report)
        threading.Thread.__init__(self, **kwargs)
    
class MpWorker(Worker, multiprocessing.Process):
    def __init__(self, module, report, **kwargs):
        Worker.__init__(self, module, report)
        multiprocessing.Process.__init__(self, **kwargs)

def get_worker(method, report, daemon):
    if method in ['threading', 'th']:
        return ThWorker(threading, report=report, daemon=daemon)
    elif method in ['multiprocessing', 'mp']:
        return MpWorker(multiprocessing, report=report, daemon=daemon)
        
if __name__ == '__main__':
    method = sys.argv[2] if len(sys.argv) == 3 else 'threading'
    worker = get_worker(method, report=True, daemon=True)
    # daemonがTrueの場合，親が4秒後に終了すると子も終了する
    print('method: ', worker.method)
    print('Method Resolution Order: ', worker.__class__.__mro__)
    worker.start()
    time.sleep(4)
