# Programmer: David Romanski
# Written: 04/18/2020
# Program: Trunk Method
# Comments: This way solves quadratic equations using the Trunk method.

import math

def findPrimes(remainder):
	# This method finds all the prime numbers for a number
	factors = []
	absRemainder = abs(remainder)

	print("Primes for " + str(remainder) + ": ", end="")
	if (absRemainder != remainder):
		factors.append(-1)
	while True :
		tempRem = absRemainder
		for x in range(2,absRemainder):
			if (absRemainder%x == 0) :
				factors.append(x)
				absRemainder = int(absRemainder/x)
				break
		if (tempRem == absRemainder) :
			factors.append(absRemainder)
			break
	print(factors)
	return factors

def twoGCF(num1, num2) :
	number1 = num1
	number2 = num2
	commonFactors = []

	num1Array = findPrimes(number1)
	num2Array = findPrimes(number2)

	startX = 0
	startY = 0

	i = 0
	while (i < len(num1Array)) :
		for y in range(startY, len(num2Array)) :
			if (num1Array[i] == num2Array[y]) :
				commonFactors.append(num1Array[i])
				i += 1
				y += 1
				startY = y
				if (i >= len(num1Array)) :
					break
		i += 1

	final = 1
	for x in range(0, len(commonFactors)): 
		final *= commonFactors[x]
	print("GCF: " + str(final))
	return final

def findFactors(term) :
	listFactors = []
	max = int(math.ceil(math.sqrt(term)))
	if (abs(term) == 1):
		max += 1
	if (term>0) :
		for x in range(1, max) :
			if ((term % x) == 0) :
				listFactors.append(int(term/x))
				listFactors.append(x)
				listFactors.append(int(-term/x))
				listFactors.append(-x)
	if (term<0) :
		absTerm = math.abs(term)
		for x in range(1, max+1) :
			if ((absTerm % x) == 0) :
				listFactors.append(int(-absTerm/x))
				listFactors.append(x)
				listFactors.append(int(absTerm/x))
				listFactors.append(-x)
	return listFactors

# Get and validate input
while True:
	try:
		A = int(input("Please enter a nonzero integer for the first term: "))
	except ValueError:
		print("I'm sorry, I didn't understand that.")
		continue
	else:
		if (A != 0):
			break

# B should be allowed to be zero
while True:
	try:
		B = int(input("Please enter a nonzero integer for the second term: "))
	except ValueError:
		print("I'm sorry, I didn't understand that.")
		continue
	else:
		if (B != 0):
			break

while True:
	try:
		C = int(input("please enter a nonzero integer for the third term: "))
	except ValueError:
		print("I'm sorry, I didn't understand that.")
		continue
	else:
		if (C != 0):
			break

# Just Making sure that the values loaded.
print(str(A) + "x^2 + " + str(B) + "x + " + str(C))

print("1. Multiply A term by the C term")
aTimesC = A * C
print(str(A) + " times " + str(C) + " = " + str(aTimesC))

print("2. Get the B term (" + str(B) + ") by factoring and testing.")
factorsATimesC = findFactors(aTimesC)
print(factorsATimesC)

answer = ""

#print("3. Now find B (" + str(B) + ")")
for x in range(0, len(factorsATimesC), 2) :
	possibleB = factorsATimesC[x] + factorsATimesC[x+1]
	print("Checking... " + str(factorsATimesC[x]) + " + " + str(factorsATimesC[x+1]) + " = " + str(possibleB))
	if (possibleB == B):
		print("We have a winner!")
		print(str(factorsATimesC[x])+ " * " + str(factorsATimesC[x+1]) + " = " + str(aTimesC))
		print(str(factorsATimesC[x])+ " + " + str(factorsATimesC[x+1]) + " = " + str(possibleB))
		print("3. Substitute the two numbers you get into your equation as the sum of the B term")
		print(str(A) + "x^2 + " + str(factorsATimesC[x]) + "x + " + str(factorsATimesC[x+1]) + "x + " + str(C))
		print("4. Factor the polnomial by grouping.")
		print("(" + str(A) + "x^2 + " + str(factorsATimesC[x]) + "x) + (" + str(factorsATimesC[x+1]) + "x + " + str(C) + ")")
		firstGCF  = twoGCF(A, factorsATimesC[x])
		firstTermA = str(firstGCF)  + "x"
		secondGCF = twoGCF(factorsATimesC[x+1], C)
		firstTermB = str(secondGCF)
		secondTermA = "(" + str(int(A/firstGCF)) + "x + " + str(int(factorsATimesC[x]/firstGCF)) + ")"
		secondTermB = "(" + str(int(factorsATimesC[x+1]/secondGCF)) + "x + " + str(int(C/secondGCF)) + ")"
		print(firstTermA + secondTermA + " + " + firstTermB + secondTermB)
		if (secondTermA != secondTermB):
			print("ERROR!!! ERROR!!!")
		firstTerm = "(" + firstTermA + " + " + firstTermB + ")"
		group = firstTerm + " + " + secondTermA
		print(group)
		answer = group
		


print("My final answer is: " + answer)