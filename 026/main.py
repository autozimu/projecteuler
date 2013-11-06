#!/usr/bin/env python

ln = 2  # longest recuring number
ll = 1  # longest recuring

for d in range(2, 1000):
    n = 1
    l = []

    while n != 0:
        if n in l:
            lr = len(l) - l.index(n) # recuring length
            if lr > ll:
                ll = lr
                ln = d
            break
        else:
            l.append(n)

        while n < d:
            n *= 10
        n %= d

print ln
