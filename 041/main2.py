#!/usr/bin/env python

from numpy import ones, sqrt

def ispandigital(n):
    """check if a number is pandigital"""
    s = str(n)
    l = len(s)
    s = s.replace('0', '')  # remove 0
    s = ''.join(sorted(set(s))) # remove duplicates
    if len(s) == l and int(s[-1]) == l:
        return True
    else:
        return False


def test_ispandigital():
    assert ispandigital(12304) == False
    assert ispandigital(1245) == False
    assert ispandigital(12245) == False
    assert ispandigital(123) == True

def isprime(n):
    """check if an odd number is prime"""
    for d in range(3, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

def test_isprime():
    assert isprime(3) == True
    assert isprime(2143) == True
    assert isprime(9) == False


n = 9999999
while True:
    if isprime(n) and ispandigital(n):
        print n
        break
    n -= 2
