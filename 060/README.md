## Problem 60: Prime pair sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be
prime. For example, taking 7 and 109, both 7109 and 1097 are
prime. The sum of these four primes, 792, represents the lowest sum
for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.



## Solution 1

Generate list of primes that can be used to generate primes using
concatenation for a prime, e.g. 3. Find the smallest primes in the
list, e.g. 7, then generate list for 7. Keep only the common parts of
the two lists. Then keep going until the list is none or get the
result.
