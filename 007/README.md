## Problem 7: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?

## Solution 1

Check every number (n) to see if it is prime. Enumerate every number (k)
smaller than n, if n could evenly divided by k, then n is not a prime.

There are several improvements:

- We can check only odd numbers (except 2)
- We do not need to enumerate every number smaller than n, the upper limit
  could be $\sqrt(n)$. Since number can have at most one factor larger than
  $\sqrt(n)$.
- We do not need to enumerate every number. We can just enumerate prime
  numbers smaller than $\sqrt(n)$. Assume n could be divided by k, if k is not
  a prime number, n shall also be evenly divided by k's factors, which must be
  prime numbers.
