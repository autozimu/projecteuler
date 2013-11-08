#!/usr/bin/env python

from numpy import zeros, sqrt, floor

N = 1000+1

ps = zeros(N, int)

for a in range(3, N/3):
    for b in range(a + 1, N/2):
        c = floor(sqrt(a * a + b * b))
        if c * c == a * a + b * b and a + b + c < N:
            ps[a + b + c] += 1


print ps[840]
