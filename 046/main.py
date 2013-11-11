#!/usr/bin/env python

from numpy import sqrt

def isprime(n):
    """Check if an odd number is a prime"""
    if n <= 1:
        return False
    for d in range(3, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

def test_isprime():
    assert isprime(9) == False
    assert isprime(11) == True


def isGoldbach(n):
    for s in range(1, int(sqrt(n/2)) + 1):
        if isprime(n - 2 * s * s):
            return True
    return False

def test_isGoldbach():
    assert isGoldbach(9) == True
    assert isGoldbach(33) == True

if __name__ == '__main__':
    n = 9
    while isprime(n) or isGoldbach(n):
        n += 2
    print n
