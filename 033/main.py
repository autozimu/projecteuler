#!/usr/bin/env python

# Euclid's algorithm to determine greatest common divisor
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


numer = []
denom = []

for a in range(11, 100):
    for b in range(a + 1, 100):
        sa = str(a)
        sb = str(b)
        for i in sa:
            if i in sb and i != '0':
                a2 = int(sa.replace(i, '', 1))
                b2 = int(sb.replace(i, '', 1))
                g2 = gcd(a2, b2)
                g = gcd(a, b)
                if (a2/g2, b2/g2) == (a/g, b/g):
                    numer.append(a)
                    denom.append(b)

nn = 1
for n in numer:
    nn *= n
dd = 1
for d in denom:
    dd *= d
print dd / gcd(nn, dd)
