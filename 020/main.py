#!/usr/bin/env python
# Author: Junfeng Li <li424@mcmaster.ca>

# N = 10
N = 100

factorial = 1
for i in range(2, N + 1):
    factorial *= i

sum = 0
while factorial != 0:
    sum += factorial % 10
    factorial /= 10

print sum
