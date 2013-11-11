#!/usr/bin/env python

import numpy as np

N = 10 ** 6
sieve = np.ones(N)
sieve[0] = sieve[1] = 0
for d in range(2, int(np.sqrt(N))+1):
    for i in range(2*d, N, d):
        sieve[i] = 0

def nfactors(n):
    """Return number of prime factors of n"""
    npf = 0  # number of prime factors
    for i in range(2, int(np.sqrt(n))+1):
        if sieve[i] == 1 and n % i == 0:
            npf += 1
            while n % i == 0:
                n /= i
    if n != 1:
        npf += 1
    return npf

def test_nfactors():
    assert nfactors(9) == 1
    assert nfactors(14) == 2
    assert nfactors(15) == 2
    assert nfactors(644) == 3
    assert nfactors(645) == 3


def consecutive(counter):
    n = 10
    c = 0
    while True:
        n += 1
        # print n
        if nfactors(n) == counter:
            c += 1
        else:
            c = 0
        if c == counter:
            return n - counter + 1

def test_consecutive():
    assert consecutive(2) == 14
    assert consecutive(3) == 644


if __name__ == '__main__':
    print consecutive(4)
