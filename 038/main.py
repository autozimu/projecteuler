#!/usr/bin/env python

from sets import Set

def ispandigital(n):
    s = str(n)
    if len(s) == 9 and len(Set(s.replace('0', ''))) == 9:
        return True
    else:
        return False

def test_ispandigital():
    assert ispandigital(192384576) == True
    assert ispandigital(192380576) == False
    assert ispandigital(1923845761) == False
    assert ispandigital(1923845760) == False


m = 0
for k in range(1, 9999+1):
    s = ''
    n = 1
    while len(s) < 9:
        s += str(k * n)
        n += 1
    s = int(s)
    if ispandigital(s):
        print k, '\t', n, '\t', s
        if s > m:
            m = s

print m
