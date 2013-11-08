#!/usr/bin/env python

from numpy import ones, sqrt

def ispandigital(n):
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


N = 9999999 + 1
p = ones(N, int)
p[0] = p[1] = 0
for n in range(2, int(sqrt(N))):
    for i in range(2 * n, N, n):
        p[i] = 0

for i in range(N - 1, 0, -1):
    if p[i] == 1:
        if ispandigital(i) == True:
            print i
            break
