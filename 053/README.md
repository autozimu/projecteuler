## Problem 53: Combinatoric selections

There are exactly ten ways of selecting three from five, 12345:

    123, 123, 125, 134, 135, 145, 234, 235, and 345

In combinatorics, we use the notation, $C_5^3 = 10$.

In general,

$$
C_n^r = \frac{n!}{r!(n - r)!}
$$

where $r \le n, n! = n \times (n - 1) \times ... \times 3 \times 2 \times 1$,
and $0! = 1$

It is not until $n = 23$, that a value exceeds one-million: $C_{23}^{10} =
1144066$.

How many, not necessarily distinct, values of $C_n^r$, for $1 \le n \le 100$,
are greater than one-million?

## Solution 1

Brute force. Normally, it is almost impossible in compiled language in C/C++,
since 100! is an extraordinarily large. While this is a breeze in Python/Ruby,
thanks to their support of infinity integers.

## Solution 2

$$
C_n^r = C_{n-1}^{r} + C{n-1}^{r-1}
$$

for $0 < k < n$

Kind of dynamic programming.
