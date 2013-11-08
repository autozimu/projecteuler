## Problem 39: Integer right triangles

If $p$ is the perimeter of a right angle triangle with integral length sides,
${a, b, c}$, there are exactly three solutions for $p = 120$.

$$
{20, 48, 52}, {24, 45, 51}, {30, 40, 50}
$$

For which value of $p \le 1000$, is the number of solutions maximised?


## Solution 1

Brute force. For every number, find the number of solutions. Note there is a
simple relation about the range of a and b, $3 < a < p/3, a < b < p/2$


## Solution 2

Loop a and b, then decide if there is a c to satisfy the right triangle
regulation. If so, increase counter of corresponding p. This approach is about
10x faster than the first one.
