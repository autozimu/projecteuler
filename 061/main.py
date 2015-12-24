#!/usr/bin/env python

def triangle(n):
    return n * (n + 1) / 2

def test_triangle():
    assert triangle(2) == 3
    assert triangle(3) == 6

def square(n):
    return n * n

def test_square():
    assert square(2) == 4
    assert square(3) == 9

def pentagonal(n):
    return n * (3 * n - 1) / 2

def test_pentagonal():
    assert pentagonal(2) == 5
    assert pentagonal(3) == 12

def hexagonal(n):
    return n * (2 * n - 1)

def test_hexagonal():
    assert hexagonal(2) == 6
    assert hexagonal(3) == 15

def heptagonal(n):
    return n * (5 * n - 3) / 2

def test_heptagonal():
    assert heptagonal(2) == 7
    assert heptagonal(3) == 18

def octagonal(n):
    return n * (3 * n - 2)

def test_octagonal():
    assert octagonal(2) == 8
    assert octagonal(3) == 21

def fill4digits(f):
    l = []
    i = 1
    while True:
        n = f(i)
        if n > 1000:
            break
        i += 1
    while True:
        n = f(i)
        if n > 9999:
            break
        l.append(n)
        i += 1
    return l

def test_fill4digits():
    t = fill4digits(triangle)
    assert t[0] == 1035
    assert t[-1] == 9870
    s = fill4digits(square)
    assert s[0] == 1024
    assert s[-1] == 9801

def iscyclic(l):
    d = dict()
    for n in l:
        d[n/100] = n%100
    target_value = key = d.keys()[0]
    count = 0
    while key in d:
        count += 1
        value = d[key]
        if value == target_value:
            if count == len(l):
                return True
            else:
                return False
        else:
            del d[key]
            key = value
    return False


def test_iscyclic():
    assert iscyclic([8128, 2882, 8281]) == True
    assert iscyclic([9870, 9801, 1717]) == False
    assert iscyclic([9730, 3025, 2501]) == False


if __name__ == '__main__':
    triangles4 = fill4digits(triangle)
    squares4 = fill4digits(square)
    pentagonals4 = fill4digits(pentagonal)
    hexagonals4 = fill4digits(hexagonal)
    heptagonals4 = fill4digits(heptagonal)
    octagonals4 = fill4digits(octagonal)
    for t in triangles4:
        for s in squares4:
            for p in pentagonals4:
                for hex in hexagonals4:
                    for hep in heptagonals4:
                        for o in octagonals4:
                            # print t, s, p, hex, hep, o
                            if iscyclic([t, s, p, hex, hep, o]):
                                result = [t, s, p, hex, hep, o]
                                print t, s, p, hex, hep, o

    print 'result = ', result
