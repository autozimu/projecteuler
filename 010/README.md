## Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.


## Solution 1

Brute-force.

A few improvements:

- check only odd numbers.
- upper limit of checking is $\sqrt(n)$.

## Solution 2

Save primes and check if existing primes are factors of n.

## Solution 3

sieve of Erotosthenes.
