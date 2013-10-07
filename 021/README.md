## Problem 21: Amicable numbers

Let $d(n)$ be defined as the sum of proper divisors of $n$ (numbers less than $n$
which divide evenly into $n$). If $d(a) = b$ and $d(b) = a$, where $a \neq b$,
then $a$ and $b$ are amicable pair and each of $a$ and $b$ are called amicable
numbers.

For example, the proper divisor of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55,
and 110; therefore $d(220) = 284$. The proper divisors of 284 are 1, 2, 4, 71,
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.


## Solution 1

Brute-force.

A few improvement related to sum of divisors:

- divisors always occur in pairs, (sometimes pair with itself). So we could
  set the upper limit of the check to $\sqrt(n)$.

## Solution 2

Assume $p$ is a prime, $\sigma$ be the sum of divisors, then there is

$$
\sigma(p^a) = (p^{a+1} - 1) / (p - 1)
$$

One step further

$$
\sigma(\prod p^a) = \prod (p^{a+1} - 1) / (p - 1)
$$
