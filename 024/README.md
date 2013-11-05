## Problem 24: Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

    012 021 102 120 201 210

What is the millionth lexicographic permutations of the digits 0, 1, 2, 3, 4,
5, 6, 7, 8, 9?


## Solution 1

Brute-force / classical

<http://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order>

## Solution 2

counting of sub-factorials

The total number of 0xxxxxxxxx like permutations is 9!. And then 1xxxxxxxxx.
Thus, the first digit would be (1000000 - 1) / 9!. Then remove the used digit.
Repeat the previous steps until there is no more digits.

Looks like how to divided a certain amount of cents to least number of coins.
