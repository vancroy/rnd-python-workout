#!/usr/bin/env python3

# spinner_thread.py

# credits: Adapted from Michele Simionato's
# multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/538048.html

import threading
import itertools
import time
import sys


class Signal:
    go = True


def spin(msg, signal):  # <1>
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        # time.sleep(0.1)
        if not signal.go:  # <2>
            break  # <3>
    write(' ' * len(status) + '\x08' * len(status))


def slow_function():  # <4>
    # pretend waiting a long time for I/O
    time.sleep(3)  # <5>
    return 42


def supervisor():  # <6>
    # done = threading.Event()  # <7>
    signal = Signal()
    spinner = threading.Thread(
        target=spin, args=('thinking!', signal))  # <8>
    print('spinner object:', spinner)  # <9>
    spinner.start()  # <10>
    result = slow_function()  # <11>
    signal.go = False  # <12>
    spinner.join()  # <13>
    return result


def main():
    result = supervisor()  # <14>
    print('Answer:', result)


if __name__ == '__main__':
    main()
