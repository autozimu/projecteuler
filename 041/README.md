## Problem 41: Pandigital prime

We shall say that an n-digit number is pandigital if it make use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?


## Solution 1

Use the sieve method to generate all primes under 999999999. Then check one by
one if they are pandigital.

Nine numbers and eight numbers cannot be the target, since 1 + 2 + 3 + 4 + 5 +
6 + 7 + 8 (+ 9) % 3 == 0.


## Solution 2

Check from the largest number. Since we only need the largest pandigital
prime, the sieve method may not be most efficient.


## Solution 3

Check all the permutations of 7 digits.
