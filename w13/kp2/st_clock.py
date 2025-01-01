#!/usr/bin/env python3

import multiprocessing, streamlit as st, sys, threading, time

from worker import get_worker

class StClock():
    def thread_or_process(self, worker):
        if worker.method == 'threading':
            mes = f'Worker thread: {worker.name}'
        elif worker.method == 'multiprocessing':
            mes = f'Worker process: {worker.pid}'
        st.markdown(mes)
        
    def show_on_sidebar(self, worker):
        self.thread_or_process(worker)
        
    def show(self, worker):
        placeholder = st.empty()
        count = 0
        while worker.is_alive():
            count += 1
            if count > 10: break
            placeholder.markdown(worker.get_message())
            time.sleep(1)
    
    def main(self, method):
        if 'worker' not in st.session_state:
            st.session_state.worker = False
        worker = st.session_state.worker
            
        with st.sidebar:
            if st.button('Start worker', disabled=bool(worker)):
                worker = st.session_state.worker = get_worker(
                    method, report=False, daemon=True)
                worker.start()
                st.rerun()
            if st.button('Stop worker', disabled=not bool(worker)):
                worker.should_stop.set()
                worker.join()
                worker = st.session_state.worker = False
                st.rerun()
            if worker:
                self.show_on_sidebar(worker)
                
        if worker:
            self.show(worker)
        else:
            st.markdown('No worker running.')
            
if __name__ == '__main__':
    method = sys.argv[2] if len(sys.argv) == 3 else 'threading'
    StClock().main(method)
