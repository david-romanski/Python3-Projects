# Programmer: David Romanski
# Pi Madhava Formula
# Created: 04/09/2020
# Updated: 04/12/2020
# This program uses the Madhava formula to estate Pi
# Updated to include a loop

answer = 1

x = 50000
denom = 1
while (x>0):
	denom += 2
	print(4*answer)
	answer -=1/denom
	denom += 2
	print(4*answer)
	answer +=1/denom
	x -= 1
