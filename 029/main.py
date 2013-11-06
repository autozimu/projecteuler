#!/usr/bin/env python

from sets import Set

N = 100

s = Set()

for a in range(2, N+1):
    for b in range(2, N+1):
        s.add(a ** b)


print len(s)
