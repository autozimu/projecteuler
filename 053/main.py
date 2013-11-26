#!/usr/bin/env python


def factorial(n):
    if n == 0:
        return 1
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def test_factorial():
    assert factorial(3) == 6
    assert factorial(5) == 120

def combinatoric(n, r):
    return factorial(n) / factorial(r) / factorial(n - r)

def test_combinatoric():
    assert combinatoric(5, 2) == 10
    assert combinatoric(5, 5) == 1

if __name__ == '__main__':
    counter = 0
    for n in range(23, 101):
        for r in range(1, n):
            if combinatoric(n, r) > 1000000:
                counter += 1
    print counter
