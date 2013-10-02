## Problem 16: Power digit sum

$2^15 = 32768$ and the sum of its digit is 3 + 2 + & + 6 + 8 = 26.

What is the sum of the digits of the number $2^1000$?


## Solution 1

$2^1000$ is apparently exceed the capacity any built-in data types of C. Make
an array to hold every digits of the power. Then multiply by 8 (or 2, or 4,
but 8 is more efficient) under the law of algebra.


## Solution 2

It would be much easier when using modern script language like Python or Ruby,
since they support large numbers seamlessly, rather than the awkward
implementation in C.
