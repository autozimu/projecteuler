#!/usr/bin/env python


N = 1000000+1

s = '0'
n = 1
while len(s) < N:
    s += str(n)
    n += 1

ans = 1
for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    print s[i]
    ans *= int(s[i])

print ans
