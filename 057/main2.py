#!/usr/bin/env python

(n, d) = (3, 2)

def expansion():
    global n, d
    (n, d) = (2 * d + n, d + n)

def test_expansion():
    expansion()
    assert (n, d) == (7, 5)
    expansion()
    assert (n, d) == (17, 12)
    expansion()
    assert (n, d) == (41, 29)


if __name__ == '__main__':
    counter = 0
    for i in range(1000):
        expansion()
        if len(str(n)) > len(str(d)):
            counter += 1
    print counter
            
