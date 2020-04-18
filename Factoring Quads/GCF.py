#  David Romanski
#  Created: 04/08/2020
#  Greatest Common Factor
#  Comments: This program finds the greatest common factor from two numbers

import math

def findPrimes(num):
	factors = []
	remainder = num
	while True:
		tempRem = remainder
		for x in range(2,remainder):
			if (remainder%x == 0):
#				print (x)
				factors.append(x)
				remainder = int(remainder/x)
				break
		if (tempRem == remainder):
#			print(remainder)
			factors.append(remainder)
			break
	return factors

number1 = 100
num1Array = []
number2 = 25
num2Array = []
commonFactors = []

num1Array = findPrimes(100)
num2Array = findPrimes(25)

for x in range(1, len(num1Array)):
	for y in range(1, len(num2Array)):
		if (num1Array[x] == num2Array[y]):
			commonFactors.append(num1Array[x])
			break

print("For number " + str(number1) + " prime numbers are: " + str(num1Array))
print("For number " + str(number2) + " prime numbers are: " + str(num2Array))
print("Common factors are: " + str(commonFactors))

final = 1
for x in range(0,len(commonFactors)):
	final *= commonFactors[x]

print("Or: " + str(final))
