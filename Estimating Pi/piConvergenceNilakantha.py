# Programmer: David Romanski
# Pi Convergence Nilakantha
# Created: 04/16/2020
# This program uses convergence method of Nilakantha to estimate pi

answer = 3
denom = 2
x = 100

while (x>0):
	answer += 4/(denom*(denom+1)*(denom+2))
	print(answer)
	denom += 2
	answer -= 4/(denom*(denom+1)*(denom+2))
	print(answer)
	denom += 2
	x -= 1