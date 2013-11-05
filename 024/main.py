#!/usr/bin/env python

s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

n = 1

while True:
    # find largest index $k$ such that s[k] < s[k + 1]
    k = len(s) - 2
    while not s[k] < s[k + 1]:
        k -= 1
    if k == -1:
        break

    # find largest index $l$ such that s[k] < s[l]
    l = len(s) - 1
    while not s[k] < s[l]:
        l -= 1

    # swap s[k] and s[l]
    s[k], s[l] = s[l], s[k]

    # reverse the sequence from s[k + 1] up to and including the final element
    k += 1
    l = len(s) - 1
    while k < l:
        s[k], s[l] = s[l], s[k]
        k += 1
        l -= 1

    n += 1
    if (n == 1000000):
        ss = ''
        for i in s:
            ss += str(i)
        print ss
        break
