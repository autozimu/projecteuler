#!/usr/bin/env python

N = 1001
s = 1
for n in range(3, N+1, 2):
    s += 4 * n * n - 6 * (n - 1)

print s
