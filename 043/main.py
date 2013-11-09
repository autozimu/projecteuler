#!/usr/bin/env python

def nextpermut(s):
    i = len(s) - 2
    while not s[i] < s[i + 1]:
        i -= 1
    if i < 0:
        return []
    j = len(s) - 1
    while not s[i] < s[j]:
        j -= 1
    # print i, j

    s[i], s[j] = s[j], s[i]

    i = i + 1
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

    return s

def test_nextpermut():
    assert nextpermut([1, 2, 3, 4]) == [1, 2, 4, 3]
    assert nextpermut([1, 2, 4, 3]) == [1, 3, 2, 4]
    assert nextpermut([4, 3, 2, 1]) == []

def issubdivisible(s):
    if int(''.join([str(c) for c in s[1:4]])) % 2 == 0 \
            and int(''.join([str(c) for c in s[2:5]])) % 3 == 0 \
            and int(''.join([str(c) for c in s[3:6]])) % 5 == 0 \
            and int(''.join([str(c) for c in s[4:7]])) % 7 == 0 \
            and int(''.join([str(c) for c in s[5:8]])) % 11 == 0 \
            and int(''.join([str(c) for c in s[6:9]])) % 13 == 0 \
            and int(''.join([str(c) for c in s[7:10]])) % 17 == 0:
        return True
    else:
        return False


def test_issubdivisible():
    assert issubdivisible([1, 4, 0, 6, 3, 5, 7, 2, 8, 9]) == True


if __name__ == '__main__':
    sums = 0
    s = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        if issubdivisible(s):
            print s
            sums += int(''.join([str(c) for c in s]))
        s = nextpermut(s)
        if s == []:
            break
    print sums
