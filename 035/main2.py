#!/usr/bin/env python

# N = 100
N = 1000000

from numpy import ones, sqrt

p = ones(N+1)
p[0] = 0
p[1] = 0
for n in range(2, int(sqrt(N)) + 1):
    for i in range(2 * n, N + 1, n):
        p[i] = 0

ncircular = 0
for i in range(N + 1):
    if p[i] == 1:
        s = str(i)
        circular = True
        for j in range(1, len(s)):
            if p[int(s[j:] + s[0:j])] == 0:
                circular = False
        if circular:
            print i
            ncircular += 1

print ncircular
