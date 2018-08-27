# coding: utf-8

import signal
import sigint_printstack # noqa


def factor(n):
    if not n:
        while True:
            pass
    return factor(n-1) * n


def test_normal():
    factor(10)


def test_cover():
    def sigint_handler(sig, action):
        raise Exception('My Handler')

    signal.signal(signal.SIGINT, sigint_handler)
    factor(10)


test_normal()
# test_cover()
