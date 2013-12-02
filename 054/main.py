#!/usr/bin/env python

import numpy as np

valueL = np.array(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'])
colorL = np.array(['C', 'D', 'H', 'S'])

def cards(cs):
    """Parse cards"""
    cs = cs.split(' ')
    result = np.zeros([len(valueL), len(colorL)], int)
    for c in cs:
        result[np.where(valueL == c[0])[0][0], np.where(colorL == c[1])[0][0]] = 1

    return result

def select_by_value(cs, v):
    vidx = np.where(valueL == v)[0][0]
    return colorL[np.where(cs[vidx, :])]


def select_by_color(cs, c):
    cidx = np.where(colorL == c)[0][0]
    return valueL[np.where(cs[:, cidx])]


def test_cards():
    cs = cards('5H 5C 6S 7S KD')
    assert np.array_equal(select_by_value(cs, '5'), np.array(['C', 'H']))
    assert np.array_equal(select_by_color(cs, 'S'), np.array(['6', '7']))

def royal_flush(cs):
    for color in colorL:
        if np.array_equal(select_by_color(cs, color), valueL[-5:]):
            return 1
    return 0

def def_royal_flush():
    cs = cards('TD JD QD KD AD')
    assert royal_flush(cs) == 1
    cs = cards('9D JD QD KD AD')
    assert royal_flush(cs) == 0

def straight_flush(cs):
    for color in colorL:
        idx = [np.where(valueL == c)[0][0] for c in select_by_color(cs, color)]
        idx.sort()
        if len(idx) > 0 and np.array_equal(idx - idx[0], [0, 1, 2, 3, 4]):
            return idx[0] + 2
    return 0

def def_straight_flush():
    cs = cards('3D 4D 5D 6D 7D')
    assert straight_flush(cs) == 3

def four_of_a_king(cs):
    for value in valueL:
        colors = select_by_value(cs, value)
        if np.array_equal(colors, colorL):
            return np.where(valueL == value)[0][0] + 2
    return 0

def test_four_of_a_king():
    cs = cards('7C 7D 7H 7S 8D')
    assert four_of_a_king(cs) == 7

def full_house(cs):
    counts = [len(select_by_value(cs, value)) for value in valueL]
    if sorted(counts, reverse=True)[0:2] == [3, 2]:
        return counts.index(3) + 2
    else:
        return 0

def test_full_house():
    cs = cards('3C 3D 3S 9S 9D')
    assert full_house(cs) == 3

def flush(cs):
    values, colors = np.where(cs)
    if len(set(colors)) == 1:
        return 1
    else:
        return 0

def test_flush():
    cs = cards('3D 6D 7D TD QD')
    assert flush(cs) == 1

def straight(cs):
    values, colors = np.where(cs)
    values = np.array(list(set(values)))
    if np.array_equal(values - values[0], np.array([0, 1, 2, 3, 4])):
        return values[0] + 2
    else:
        return 0

def test_straight():
    cs = cards('5C 6D 7S 8H 9D')
    assert straight(cs) == 5
    
def three_of_a_kind(cs):
    counts = [len(select_by_value(cs, value)) for value in valueL]
    if sorted(counts, reverse=True)[0] == 3:
        vidx = counts.index(3)
        cs[vidx] = 0
        return vidx + 2
    else:
        return 0

def test_three_of_a_kind():
    cs = cards('3C 3D 3S 9S TD')
    assert three_of_a_kind(cs) == 3

def two_pairs(cs):
    counts = [len(select_by_value(cs, value)) for value in valueL]
    if sorted(counts, reverse=True)[0:2] == [2, 2]:
        vidx = len(valueL) - 1 - counts[::-1].index(2)
        cs[vidx] = 0
        return vidx + 2
    else:
        return 0

def test_two_pairs():
    cs = cards('3C 3D 5H 8D 8S')
    assert two_pairs(cs) == 8

def one_pair(cs):
    counts = [len(select_by_value(cs, value)) for value in valueL]
    if sorted(counts, reverse=True)[0] == 2:
        vidx = counts.index(2)
        cs[vidx] = 0
        return vidx + 2
    else:
        return 0

def test_one_pair():
    cs = cards('3C 4H 5D 5H 6S')
    assert one_pair(cs) == 5

def high_card(cs):
    values, colors = np.where(cs)
    vidx = values[-1]
    cs[vidx] = 0
    return vidx + 2

def test_high_card():
    cs = cards('3C 4H 5H 7D 9S')
    assert high_card(cs) == 9
    
def deal(player1, player2):
    r1 = royal_flush(player1)
    r2 = royal_flush(player2)
    if r1 > r2:
        return 1
    elif r1 < r2:
        return 2

    r1 = straight_flush(player1)
    r2 = straight_flush(player2)
    if r1 > r2:
        return 1
    elif r1 < r2:
        return 2

    r1 = four_of_a_king(player1)
    r2 = four_of_a_king(player2)
    if r1 > r2:
        return 1
    elif r1 < r2:
        return 2

    r1 = full_house(player1)
    r2 = full_house(player2)
    if r1 > r2:
        return 1
    elif r1 < r2:
        return 2
    
    r1 = flush(player1)
    r2 = flush(player2)
    if r1 > r2:
        return 1
    elif r1 < r2:
        return 2

    r1 = straight(player1)
    r2 = straight(player2)
    if r1 > r2:
        return 1
    elif r1 < r2:
        return 2

    r1 = three_of_a_kind(player1)
    r2 = three_of_a_kind(player2)
    if r1 > r2:
        return 1
    elif r1 < r2:
        return 2

    r1 = two_pairs(player1)
    r2 = two_pairs(player2)
    if r1 > r2:
        return 1
    elif r1 < r2:
        return 2

    r1 = one_pair(player1)
    r2 = one_pair(player2)
    if r1 > r2:
        return 1
    elif r1 < r2:
        return 2

    r1 = high_card(player1)
    r2 = high_card(player2)
    if r1 > r2:
        return 1
    elif r1 < r2:
        return 2

def test_deal():
    player1 = cards('5H 5C 6S 7S KD')
    player2 = cards('2C 3S 8S 8D TD')
    assert deal(player1, player2) == 2
        
    player1 = cards('5D 8C 9S JS AC')
    player2 = cards('2C 5C 7D 8S QH')
    assert deal(player1, player2) == 1

    player1 = cards('2D 9C AS AH AC')
    player2 = cards('3D 6D 7D TD QD')
    assert deal(player1, player2) == 2

    player1 = cards('4D 6S 9H QH QC')
    player2 = cards('3D 6D 7H QD QS')
    assert deal(player1, player2) == 1

    player1 = cards('2H 2D 4C 4D 4S')
    player2 = cards('3C 3D 3S 9S 9D')
    assert deal(player1, player2) == 1


if __name__ == '__main__':
    with open('poker.txt') as f:
        lines = f.readlines()

    counter = 0
    for line in lines:
        player1 = cards(line[0:14])
        player2 = cards(line[15:29])
        if deal(player1, player2) == 1:
            counter += 1

    print counter
        
