#!/usr/bin/env python

from numpy import sqrt

# check if an odd number is prime
def isprime(n):
    for i in range(3, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


primes = [2, 3, 5, 7]
ntruncatable = 0
n = 11
su = 0
while ntruncatable < 11:
    if isprime(n):
        print n
        primes.append(n)
        s = str(n)
        truncatable = True
        for i in range(1, len(s)):
            if not int(s[i:]) in primes:
                truncatable = False
        for i in range(1, len(s)):
            if not int(s[:-i]) in primes:
                truncatable = False
        if truncatable:
            # print n
            su += n
            ntruncatable += 1
    n += 2


print su
