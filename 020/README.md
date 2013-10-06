## Problem 20: Factorial digit sum

n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800, and the sum of the
digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!


## Solution 1

Brute-force.

The solution itself is quite strait forward, but there is a small catch. The
factorial of 100! would be exceed `long long` data type in C, which is the
largest integers available in C. We can use an array of integers to mimic the
behavior of multiply of big integer. Or we can use modern language like
Python, Ruby to implement it, let those languages will take care of the
big-int problem.
