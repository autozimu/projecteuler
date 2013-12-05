#!/usr/bin/env python

import numpy as np
from collections import Counter

keylength = 3

with open('cipher1.txt') as f:
    message = f.readline().strip('\n').split(',')
    
message = [int(c) for c in message]

message_piles = np.zeros([keylength, len(message)/3+1], int)
for (i, c) in enumerate(message):
    message_piles[i%3, i/3] = c

key = [Counter(message_piles[i]).most_common(1)[0][0] ^ ord(' ') for i in range(keylength)]

# print ''.join([chr(c) for c in key])

for (i, c) in enumerate(message):
    message[i] = c ^ key[i%3]

# print ''.join([chr(c) for c in message])

print sum(message)
