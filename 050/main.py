#!/usr/bin/env python

import numpy as np

N = 1000000
sieve = np.ones(N)
sieve[0] = sieve[1] = 0
for d in range(2, int(np.sqrt(N))+1):
    for i in range(2*d, N, d):
        sieve[i] = 0
primes = np.where(sieve == 1)[0]

def test_sieve():
    assert primes[0] == 2
    assert primes[5] == 13

# number of consecutive primes
ml = 0  # max length of consecutive primes
mp = 0  # prime when max length
for i in range(0, 10):
    j = 1
    while True:
        if sum(primes[i:j]) in primes:
            print i, len(primes[i:j])
            if len(primes[i:j]) > ml:
                ml = len(primes[i:j])
                mp =  sum(primes[i:j])
        elif sum(primes[i:j]) > primes[-1]:
            break

        j += 1

print mp, ml
