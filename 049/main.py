#!/usr/bin/env python

import numpy as np
from collections import Counter

N = 10000

# create prime sieve
sieve = np.ones(N)
sieve[0] = sieve[1] = 0
for d in range(2, int(np.sqrt(N))+1):
    for i in range(2 * d, N, d):
        sieve[i] = 0
# ignore prime numbers smaller than 1000
for i in range(2, 1000):
    sieve[i] = 0

primes = [p for p in np.where(sieve == 1)[0]]
for (i, p) in enumerate(primes):
    pp = [q for q in primes[i:] if set(str(q)) == set(str(p))]
    if len(pp) >= 3:
        for m in range(len(pp)):
            for n in range(m+1, len(pp)):
                if (2 * pp[n] - pp[m]) in pp:
                    print pp[m], pp[n], 2 * pp[n] - pp[m]
