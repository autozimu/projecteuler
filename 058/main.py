#!/usr/bin/env python

import numpy as np

def spiral(n):
    dx, dy = 0, -1
    x, y = n-1, n-1
    array = np.zeros([n, n], int)
    for i in range(1, n ** 2+1)[::-1]:
        array[x][y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and array[nx][ny] == 0:
            x, y = nx, ny
        else:
            dx, dy = dy,-dx
            x, y = x + dx, y + dy
    return array

def printspiral(myarray):
    print 
    n = range(len(myarray))
    for x in n:
        for y in n:
            print "%2i" % myarray[x][y],
        print

def test_spiral():
    assert printspiral(spiral(7)) == None

def isprime(n):
    if n < 2 or n % 2 == 0:
        return False

    for d in xrange(2, int(np.sqrt(n))+1):
        if n % d == 0:
            return False
        
    return True

def test_isprime():
    assert isprime(4) == False
    assert isprime(17) == True

    
def primeratio(array):
    counter = 0
    for d in np.diag(array):
        if isprime(d):
            counter += 1
    for d in np.diag(array[:, ::-1]):
        if isprime(d):
            counter += 1
    return counter * 1.0 / (2 * np.shape(array)[0] - 1)

def test_primeratio():
    assert abs(primeratio(spiral(7)) - 0.62) < 0.01


if __name__ == '__main__':
    n = 7
    while True:
        n += 2
        r = primeratio(spiral(n))
        print n, r
        if r < 0.1:
            print n
            break
