# Programmer: David Romanski
# Pi First Infinate Series
# Created: 04/09/2020
# Updated: 04/12/2020
# This program uses the first infinate series to estate Pi
# Updated this to a loop. [I did it!!!]

import math

answer = 1
sqrtTwo = math.sqrt(2)
x = 40

while (x>0):
	answer *= sqrtTwo/2
	print(2/answer)
	sqrtTwo = math.sqrt(2 + sqrtTwo)
	x -= 1
