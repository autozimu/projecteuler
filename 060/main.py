#!/usr/bin/env python

import numpy as np

N = 10 ** 6  # size of sieve
M = 10000  # upper limit of candidates

sieve = np.ones(N, int)
sieve[0] = sieve[1] = 0
for d in xrange(2, int(np.sqrt(N))+1):
    for i in xrange(2 * d, N, d):
        sieve[i] = 0


def isprime(n):
    if n < N:
        if sieve[n] == 1:
            return True
        else:
            return False
    else:
        for d in xrange(2, int(np.sqrt(n))+1):
            if n % d == 0:
                return False
        return True


def test_isprime():
    assert isprime(3) == True
    assert isprime(17) == True
    assert isprime(9) == False
    assert isprime(123456789) == False

def conprime(n1, n2):
    if isprime(int(str(n1) + str(n2))) and isprime(int(str(n2) + str(n1))):
        return True
    else:
        return False

def test_conprime():
    assert conprime(3, 7) == True
    assert conprime(7, 109) == True


if __name__ == '__main__':
    for n1 in np.where(sieve)[0]:
        l1 = [p for p in np.where(sieve[:M])[0] if conprime(n1, p)]
        # print n1, l1
        for n2 in l1:
            l2 = [p for p in np.where(sieve[:M])[0] if conprime(n2, p)]
            l12 = np.intersect1d(l1, l2, assume_unique=True)
            # print n1, n2, l12
            for n3 in l12:
                l3 = [p for p in np.where(sieve[:M])[0] if conprime(n3, p)]
                l123 = np.intersect1d(l12, l3, assume_unique=True)
                # print n1, n2, n3, l123
                for n4 in l123:
                    l4 = [p for p in np.where(sieve[:M])[0] if conprime(n4, p)]
                    l1234 = np.intersect1d(l123, l4, assume_unique=True)
                    # print n1, n2, n3, n4, l1234
                    if len(l1234) != 0:
                        print 'found'
                        print n1, n2, n3, n4, l1234,
                        print 'SUM: ', n1 + n2 + n3 + n4 + l1234[0]
                        
