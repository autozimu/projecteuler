#!/usr/bin/env python

import sys
sys.setrecursionlimit(10000)

def expansion(i):
    if i == 1:
        return (3, 2)
    else:
        n, d = expansion(i-1)
        return (2 * d + n, d + n)

def test_expansion():
    assert expansion(1) == (3, 2)
    assert expansion(2) == (7, 5)
    assert expansion(3) == (17, 12)
    assert expansion(4) == (41, 29)

if __name__ == '__main__':
    counter = 0
    for i in range(1, 1001):
        n, d = expansion(i)
        if len(str(n)) > len(str(d)):
            counter += 1

    print counter
