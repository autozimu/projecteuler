#!/usr/bin/env python

from sets import Set

s = Set()
for a in range(2, 100):
    for b in range(a + 1, 10000):
        if a * b > 10000:
            break
        p = str(a) + str(b) + str(a * b)
        if sorted(list(p)) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print a, b, a * b
            s.add(a * b)

print sum(s)
