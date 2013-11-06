#!/usr/bin/env python

from math import sqrt


def isprime(n):
    if n <= 1:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n%i == 0:
            return False

    return True


bs = []
for n in range(2, 1000):
    if isprime(n):
        bs.append(n)

maxl = 1 # max lengh of quadratic primes
maxp = 1 # product of a and b at max length

for a in range(-999, 1000, 2):
    for b in bs:
        f = lambda n: n * n + a * n + b
        l = 0
        n = 0
        while isprime(f(n)):
            l += 1
            n += 1
        if l > maxl:
            maxl = l
            maxp = a * b

print maxp, maxl
