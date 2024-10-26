#!/usr/bin/env python3

from copy import copy

def switch_signal(signal):
    for key in signal.keys():
        if signal[key] == 'green':
            signal[key] = 'yellow'
        elif signal[key] == 'yellow':
            signal[key] = 'red'
        elif signal[key] == 'red':
            signal[key] = 'green'
    if list(signal.values()).count('red') == 2:
        signal = switch_signal(signal)
    assert 'red' in signal.values(), f"赤信号がない！{signal}"
    return signal

def main():
    signal = {'NS': 'green', 'EW': 'red'}
    for i in range(5):
        signal_org = copy(signal)
        signal = switch_signal(signal)
        print(f"{signal_org} -> {signal}")

if __name__ == '__main__':
    main()
