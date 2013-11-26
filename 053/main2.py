#!/usr/bin/env python

import numpy as np

N = 101

# use float type to avoid overflow of int64
T = np.zeros([N, N], float)
counter = 0
for n in range(1, N):
    T[n, 0] = T[n, n] = 1
    for r in range(1, n):
        T[n, r] = T[n-1, r] + T[n-1, r-1]
        if T[n, r] > 1000000:
            counter += 1

print counter
