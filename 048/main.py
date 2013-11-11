#!/usr/bin/env python

def last10digitsofpowers(n):
    ans = 0
    for i in range(1, n+1):
        ans += i ** i
        ans %= 10000000000
    return ans

def test_last10digitsofpowers():
    assert last10digitsofpowers(10) == 405071317

if __name__ == '__main__':
    print last10digitsofpowers(1000)
