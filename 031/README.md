## Problem 31: Coin sums

In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

$$
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p)
$$

It is possible to make £2 in the following way:

$$
1 \times £1 + 1 \times 50p + 2 \times 20p + 1 \times 5p + 1 \times 2p + 3
\times 1p
$$

How many different ways can £2 be made using any number of coins?


## Solution 1

Brute-force using nested loops.

## Solution 2

Using recursion. Also belongs to dynamic programming, but from top to bottom.

## Solution 3

Dynamic Programming. From bottom to top.
