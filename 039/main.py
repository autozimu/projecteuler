#!/usr/bin/env python


def nsolutions(p):
    n = 0
    for a in range(1, p/3):
        for b in range(a + 1, p/2):
            if a * a + b * b == (p - a - b) * (p - a - b):
                n += 1
    return n

def test_nsolutions():
    assert nsolutions(120) == 3

m = 0
mp = 0
for p in range(12, 1000+1):
    n = nsolutions(p)
    # print p, n
    if n > m:
        m = n
        mp = p

print mp, m
