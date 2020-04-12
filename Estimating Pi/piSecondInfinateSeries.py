# Programmer: David Romanski
# Pi Second Infinate Series
# Created: 04/09/2020
# Updated: 04/12/2020
# This program uses the second infinate series to estate Pi
# Added looping to program

answer = 1
numer = 0
denom = 1
x = 50000
while (x>0):
	numer += 2
	answer *= ((numer/denom) * (numer/(denom+2)))
	print(2*answer)
	denom += 2
	x -= 1
