#!/usr/bin/env python

import numpy as np

def isprime(n):
    for i in range(2, int(np.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def test_isprime():
    assert isprime(4) == False
    assert isprime(7) == True

def fill(pattern, d, n):
    # this is a famous Python pitfall
    # If the use list as function parameter, the funciton will recieve a
    # reference of the original list, any modification of the list inside the
    # funtion will apply to the original list, since they are the same one. So
    # here we make a copy of the list before we make modifications.
    pattern = list(pattern)
    for i in range(len(pattern)-1, -1, -1):
        if pattern[i] == 1:
            pattern[i] = n % 10
            n /= 10
        else:
            pattern[i] = d
    # if the number leading with 0, then we do not take it as a candidiate
    if pattern[0] == 0:
        return 4
    return sum([m*10**(len(pattern)-i-1) for (i, m) in enumerate(pattern)])

def test_fill():
    assert fill([1, 0, 0, 0, 1], 1, 23) == 21113


if __name__ == '__main__':
    # five digits number pattern. It must have 3 repeating digits.
    # 0 for repeated part, 1 for non-repeated part
    pattern5 = [[1, 0, 0, 0, 1],
                [0, 1, 0, 0, 1],
                [0, 0, 1, 0, 1],
                [0, 0, 0, 1, 1]]
    # six digits number pattern
    pattern6 = [[1, 1, 0, 0, 0, 1],
                [1, 0, 1, 0, 0, 1],
                [1, 0, 0, 1, 0, 1],
                [1, 0, 0, 0, 1, 1],
                [0, 1, 1, 0, 0, 1],
                [0, 1, 0, 1, 0, 1],
                [0, 1, 0, 0, 1, 1],
                [0, 0, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 1],
                [0, 0, 0, 1, 1, 1]]

    found = False
    for n in range(11, 1000, 2):
    # for n in [233]:
        if found:
            break
        # skip xx5, they must not be prime
        if n % 5 == 0:
            continue

        if len(str(n)) == 2:
            pattern = pattern5
        else:
            pattern = pattern6

        # fill pattern
        for pt in pattern:
            counter = 0
            for d in range(0, 10):
                l = fill(pt, d, n)
                if isprime(l):
                    counter += 1
            # print n, pt, counter
            if counter == 8:
                for d in range(1, 10):
                    l = fill(pt, d, n)
                    if isprime(l):
                        print 'the prime is', l
                        break
                found = True
                break
