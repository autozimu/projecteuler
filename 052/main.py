#!/usr/bin/env python

def ispermuted(n, m):
    """Check if a multiple of n, n * m, is a permutation of n"""
    if set(list(str(n))) == set(list(str(n * m))):
        return True
    else:
        return False

def test_ispermuted():
    assert ispermuted(125874, 2) == True


if __name__ == '__main__':
    n = 123 - 1
    while True:
        n += 1
        if ispermuted(n, 2) and ispermuted(n, 3) and ispermuted(n, 4) \
                and ispermuted(n, 5) and ispermuted(n, 6):
            print n
            break
