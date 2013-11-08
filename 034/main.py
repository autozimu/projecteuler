#!/usr/bin/env python


from numpy import zeros

factorials = zeros(10, int)
factorials[0] = 1
factorials[1] = 1
for i in range(2, 10):
    factorials[i] = i * factorials[i - 1]


s = 0
for n in range(3, 10 ** 5):
    n2 = 0
    tmp = n
    while tmp > 0:
        n2 += factorials[tmp - tmp / 10 * 10]
        tmp /= 10
    if n2 == n:
        print n
        s += n

print s
