#!/usr/bin/env python

import  numpy as np

def diags():
    diags.n = diags.n + 2 * diags.d
    if diags.i == 3:
        diags.d += 1
        diags.i = 0
    else:
        diags.i += 1
    return diags.n
diags.n = 1
diags.d = 1
diags.i = 0


def test_diags():
    ds = [diags() for idx in xrange(12)]
    assert ds == [3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49]

def isprime(n):
    """Check if an odd number (>=3) is a prime"""
    for d in xrange(2, int(np.sqrt(n))+1):
        if n % d == 0:
            return False
    return True


def test_isprime():
    assert isprime(9) == False
    assert isprime(17) == True

if __name__ == '__main__':
    nprimes = 0
    ndiags = 1
    while True:
        for i in range(4):
            n = diags()
            ndiags += 1
            if isprime(n):
                nprimes += 1
        ratio = nprimes * 1.0 / ndiags
        # print (ndiags + 1) / 2, ratio
        if ratio < 0.1:
            break

    print (ndiags + 1) / 2
