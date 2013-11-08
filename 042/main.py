#!/usr/bin/env python

from numpy import sqrt

def num(word):
    n = 0
    for w in word:
        n += ord(w) - ord('A') + 1
    return n


def test_num():
    assert num('SKY') == 55

if __name__ == '__main__':
    # readin words
    with open('words.txt') as f:
        words = f.readline().replace('"', '').split(',')

    # generate list of triangle numbers
    l = max([len(w) for w in words])
    trinums = []
    for n in range(1, int(sqrt(l * 26 * 2))):
        trinums.append(n * (n + 1) / 2)

    # count
    counter = 0
    for w in words:
        if num(w) in trinums:
            counter += 1
    print counter
