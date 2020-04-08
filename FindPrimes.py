#  David Romanski
#  Created: 04/08/2020
#  Find Primes
#  Comments: This program finds all the primes of a number

number1 = 1
remainder = number1


while True:
	tempRem = remainder
	for x in range(2,remainder):
		if (remainder%x == 0):
			print (x)
			remainder = int(remainder/x)
			break
	if (tempRem == remainder):
		print(remainder)
		break

print("done!")