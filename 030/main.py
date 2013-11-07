#!/usr/bin/env python


# N = 4
# limit = 5 * 9 ** 4  # upper limit for fourth powers
N = 5
limit = 6 * 9 ** 5  # upper limit for fifth powers


s = 0
for n in range(2, limit):
    if n == sum([int(d) ** N for d in str(n)]):
        s += n
print s
