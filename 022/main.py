#!/usr/bin/env python

# readin content
with open('names.txt', 'r') as f:
    names = f.read()

# split, cleanup and sort
names = names.split(',')
for (i, name) in enumerate(names):
    names[i] = name[1:len(name) - 1]
names.sort()

# calculate score
score = 0
for (i, name) in enumerate(names):
    i += 1
    value = 0
    for c in name:
        value += ord(c) - ord('A') + 1
    score += i * value

print score
