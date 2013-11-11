#!/usr/bin/env python

P = lambda n: n * (3 * n - 1) / 2
H = lambda n: n * (2 * n - 1)


p = 165
h = 143
while True:
    h += 1
    while P(p) < H(h):
        p += 1
    print p, h, P(p), H(h)
    if P(p) == H(h):
        print p, h, P(p), H(h)
        break
