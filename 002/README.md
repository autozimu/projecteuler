## Problem 2: Even Fibonacci numbers

Each new term in Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

## Solution 1

There is one even-valued term every three terms, except the first two. Anyway,
this assertion is correct since the first two items is not deferred but given
by default. So the sum process could be done every three term.

In Python or such languages, there is kind of `yield` behavior, which is quite
suitable in such a situation, if we want to make the process into a separate
function, since it avoid initialing function each time we call it.

## Solution 2

We already know that there is an even-valued term every third number. One step
further, for all the even-valued term,

    2, 8, 34, 144, ...

there is the relation

$$
F(n) = 4 * F(n - 1) + F(n - 2)
$$

or in the original sequence index

$$
F(3n) = 4 * F(3n - 3) + F(3n - 6)
$$