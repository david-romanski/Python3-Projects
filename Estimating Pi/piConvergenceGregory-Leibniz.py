# Programmer: David Romanski
# Pi Convergence Gregory-Leibniz
# Created: 04/16/2020
# This program uses convergence method of Gregory-Leibniz series to estimate pi.

denom = 1
x = 10000
answer = 0

while (x>0):
	answer += 4/denom
	print(answer)
	denom += 2
	answer -= 4/denom
	print(answer)
	denom += 2
	x -= 1