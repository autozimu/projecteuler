#!/usr/bin/env python


N = 1000000

s = 0
for n in range(N):
    if n == int(str(n)[::-1]) and bin(n) == '0b' + bin(n)[:1:-1]:
        print n
        s += n

print s
