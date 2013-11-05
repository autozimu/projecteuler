#!/usr/bin/env python


# nd = 3
nd = 1000

F1 = 1
F2 = 1
n = 2

while True:
    F3 = F1 + F2
    n += 1
    if F3 > 10 ** (nd - 1):
        print n
        break
    else:
        F1 = F2
        F2 = F3
