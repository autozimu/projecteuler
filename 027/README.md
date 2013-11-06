## Problem 27: Quadratic primes

Euler discovered the remarkable quadratic formula:

$$
n^2 + n + 41
$$

It turns out the formula will produce 40 primes for the consecutive values $n
= 0$ to $39$. However, when $n = 40$, $40^2 + 40 + 41 = 40(40 + 1) + 41$ is
divisible by 41, and certainly when $n = 41$, $41^2 + 41 + 41$ is clearly
divisible by 41.

The incredible formula $n^2 - 79n + 1061$ was discovered, which produces 80
primes for the consecutive values $n = 0$ to 79. The product of the
coefficients, $-79$ and $1601$, is $-126479$.

Considering quadratics of the form:

$$
n^2 + an + b, \text{where} |a| < 1000, \text{and} |b| < 1000
$$

where $|n|$ is the modulus/absolute value of $n$. e.g. $|11| = 11$ and $|-4| =
4$.

Find the product of the coefficients, $a$ and $b$, for the quadratic
expression that produces the maximum number of primes for consecutive values
of $n$, starting with $n = 0$.


## Solution 1

Brute-force. Notice $b$ should be a prime (for $n = 0$), and $a$ shall be an
odd number.