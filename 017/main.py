#!/usr/bin/env python
# Author: Junfeng Li <li424@mcmaster.ca>

digits = {}
digits[0] = ''
digits[1] = 'one'
digits[2] = 'two'
digits[3] = 'three'
digits[4] = 'four'
digits[5] = 'five'
digits[6] = 'six'
digits[7] = 'seven'
digits[8] = 'eight'
digits[9] = 'nine'
digits[10] = 'ten'
digits[11] = 'eleven'
digits[12] = 'twelve'
digits[13] = 'thirteen'
digits[14] = 'fourteen'
digits[15] = 'fifteen'
digits[16] = 'sixteen'
digits[17] = 'seventeen'
digits[18] = 'eighteen'
digits[19] = 'nineteen'

tens = {}
tens[2] = 'twenty'
tens[3] = 'thirty'
tens[4] = 'forty'
tens[5] = 'fifty'
tens[6] = 'sixty'
tens[7] = 'seventy'
tens[8] = 'eighty'
tens[9] = 'ninety'

def countletters(number):
    letters = ''

    if number >= 100:
        letters += digits[number/100]
        letters += 'hundred'
        number %= 100
        if number != 0:
            letters += 'and'

    if number >= 20:
        letters += tens[number/10]
        number %= 10
        letters += digits[number]
    else:
        letters += digits[number]

    return len(letters)


n = 0
for number in range(1, 1000):
    n += countletters(number)

n += len('onethousand')

print n
