# Programmer: David Romanski
# Pi First Infinate Series
# Created: 04/09/2020
# This program uses the first infinate series to estate Pi

import math

one   = 2 + math.sqrt(2)
two   = 2 + math.sqrt(one)
three = 2 + math.sqrt(two)
four  = 2 + math.sqrt(three)
five  = 2 + math.sqrt(four)
six   = 2 + math.sqrt(five)

answer2 = math.sqrt(2)/2

print(2/answer2)

answer2 *= math.sqrt(one) / 2

print(2/answer2)

answer2 *= math.sqrt(two) / 2

print(2/answer2)

answer2 *= (math.sqrt(three)) / 2

print(2/answer2)

answer2 *= (math.sqrt(four)) / 2

print(2/answer2)

answer2 *= (math.sqrt(five)) / 2

print(2/answer2)

answer2 *= (math.sqrt(six)) / 2

print(2/answer2)