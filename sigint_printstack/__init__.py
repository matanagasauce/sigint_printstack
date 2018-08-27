# coding: utf-8

import sys
import signal
import traceback


def sigint_handler(sig, stack):
    traceback.print_stack(stack)
    sys.stdout.write(("Stop the script (%s/[%s])? ") % ('y', 'n'))
    sys.stdout.flush()
    line = sys.stdin.readline()
    if line.lower().startswith('y') and 'n' not in line.lower():
        signal.default_int_handler(sig, stack)

_signal = signal.signal


def new_signal(sig, action):
    if sig == signal.SIGINT:
        def _(sig, stack):
            traceback.print_stack(stack)
            return action(sig, stack)
        return _signal(sig, _)
    else:
        return _signal(sig, action)

signal.signal(signal.SIGINT, sigint_handler)
signal.signal = new_signal
