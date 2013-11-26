## Problem 51: Prime digit replacements

By replacing the 1st digit of the 2-digit number \*3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56\*\*3 with the same digit, this
5-digit number is the first example having seven primes among the ten
generated numbers, yielding the family: 56003, 56333, 56443, 56663, 56773, and
56993. Consequently, 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight prime
value family.

## Solution 1

- Since we are looking for an 8 member family, it could be assumed that the
  smallest member of the family has the repeated digit to be 0, 1, or 2.
- A number can be divided by 3 if the sum of the digit sum is divisible by 3.
  The following table describe the count of failed possible digits due to the
  above rule.

| repeated digit | 1  | 2  | 3  | 4  | 5  |
| --             | -- | -- | -- | -- | -- |
| 0              | 4  | 4  | 10 | 4  | 4  |
| 1              | 3  | 3  | 0  | 3  | 3  |
| 2              | 3  | 3  | 0  | 3  | 3  |

So the repeated number must have 3 repeated digits and the digit sum must not
be divisible by 3.

- The number must be ended with 1, 3, 7 or 9.
- Assume the number is 5 or 6 digit. The non-repeating part will be from
  11--1000.


Stolen from <http://www.mathblog.dk/project-euler-51-eight-prime-family/>
