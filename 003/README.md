## Problem 3: Largest prime factor

The prime factor of 13195 are 5, 7, 13 and 29.

What is the largest factor of the number 600851475143 ?


## Solution 1

It seems that we have to start from bigger numbers if we want to get the
largest prime factor. But this is a pitfall. Since we will have to check if a
factor is a prime.

Actually, we can start from the smallest number (actually from 2, and one by
one, the upper limit shall be $\sqrt(n)$). For every number, we check if it is
a factor. If it is, then we divide by the number. In the end, the largest
prime number is remained.
