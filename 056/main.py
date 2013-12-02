#!/usr/bin/env python

def digitsum(n):
    digits = [int(d) for d in str(n)]
    return sum(digits)

def test_digitsum():
    assert digitsum(1000000) == 1
    assert digitsum(2**6) == 10

if __name__ == '__main__':
    sum_max = 0
    for a in range(100):
        for b in range(100):
            s = digitsum(a ** b)
            if s > sum_max:
                sum_max = s

    print sum_max
    
