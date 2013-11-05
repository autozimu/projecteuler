#!/usr/bin/env python

import math

n = 1000000 - 1
s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ss = ""

for i in range(1, len(s) + 1):
    m = math.factorial(10 - i)
    j = n // m
    n = n % m
    ss += str(s[j])
    s.remove(s[j])

print ss
