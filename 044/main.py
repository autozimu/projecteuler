#!/usr/bin/env python

s = [n * (3 * n - 1) / 2 for n in range(0, 10000)]

found = False
i = 1900
while not found:
    i += 1
    j = 1
    while j < i:
        # actually, we cannot guarentee that j < i, the real condition would
        # be s[i] < 3 * j + 1, which is the distance of s[j] and s[j + 1]. But
        # this one is too time consuming.
        print i, j
        if (s[i] + s[j]) in s and (2 * s[j] + s[i]) in s:
            print 'found', i, j
            found = True
            break
        else:
            j += 1

print s[i]
