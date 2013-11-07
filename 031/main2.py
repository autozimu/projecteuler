#!/usr/bin/env python


def nchange (n, d):
    if n < 0:
        return 0;
    elif n == 0:
        return 1;
    else:
        s = 0;  # number of ways of change
        if d >= 200:
            s += nchange(n - 200, 200)
        if d >= 100:
            s += nchange(n - 100, 100)
        if d >= 50:
            s += nchange(n - 50, 50)
        if d >= 20:
            s += nchange(n - 20, 20)
        if d >= 10:
            s += nchange(n - 10, 10)
        if d >= 5:
            s += nchange(n - 5, 5)
        if d >= 2:
            s += nchange(n - 2, 2)
        if d >= 1:
            s += 1
        return s


target = 200
print nchange(target, 200)
