#!/usr/bin/env python

from numpy import sqrt

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

def nextpermut(s):
    """return next permutation, a smaller one"""
    i = len(s) - 2
    while not s[i] > s[i + 1]:
        i -= 1
    j = len(s) - 1
    while not s[j] < s[i]:
        j -= 1
    s[i], s[j] = s[j], s[i]
    i += 1
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s

def test_nextpermut():
    assert nextpermut([4, 3, 2, 1]) == [4, 3, 1, 2]


if __name__ == '__main__':
    s = [7, 6, 5, 4, 3, 2, 1]
    while True:
        n = int(''.join([str(c) for c in s]))
        if isprime(n):
            print n
            break
        s = nextpermut(s)
