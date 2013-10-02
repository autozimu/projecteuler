## Problem 15: Lattice paths

Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?


## Solution 1

For a nxn grid, the number of routes shall be

$$
C_{2n}^n = \frac{\prod_{n+1}^{2n} i}{n!}
$$


## Solution 2

Brute-force. I did not realize there is still a brute-force solution for this
problem until I saw the discussion on StackOverflow. The process is like this:
reduce the grid size one by one, until we have 1x1 or 2x2 like simple grids.
