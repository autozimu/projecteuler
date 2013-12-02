#!/usr/bin/env python

def ispalindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False

def test_ispalindrome():
    assert ispalindrome(121) == True
    assert ispalindrome(122) == False

def isLychrel(n):
    niterations = 0
    while niterations <= 50:
        n = n + int(str(n)[::-1])
        if ispalindrome(n):
            return False
        niterations += 1
    return True

def test_isLychrel():
    assert isLychrel(196) == True
    assert isLychrel(4994) == True
    assert isLychrel(349) == False
    assert isLychrel(10677) == True

if __name__ == '__main__':
    counter = 0
    for n in range(10000):
        if isLychrel(n):
            counter += 1
    print counter
