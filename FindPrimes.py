#  David Romanski
#  Created: 04/08/2020
#  Find Primes
#  Comments: This program finds all the primes of a number

number1 = 144
remainder = number1
factorsArray = []

print("Number is " + str(number1))

while True:
	tempRem = remainder
	for x in range(2,remainder):
		if (remainder%x == 0):
			print (x)
			factorsArray.append(x)
			remainder = int(remainder/x)
			break
	if (tempRem == remainder):
		factorsArray.append(remainder)
		print(remainder)
		break
print("Prime factors are: " + str(factorsArray))
print("done!")
