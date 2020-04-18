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

print("1. Multiply A and C")
aTimesC = A * C
print(str(A) + " times " + str(C) + " = " + str(aTimesC))

print("2. Find the factors of " + str(aTimesC))
factorsATimesC = findFactors(aTimesC)
print(factorsATimesC)

answer = ""

print("3. Now find B (" + str(B) + ")")
for x in range(0, len(factorsATimesC), 2) :
	possibleB = factorsATimesC[x] + factorsATimesC[x+1]
	print("Checking... " + str(factorsATimesC[x]) + " + " + str(factorsATimesC[x+1]) + " = " + str(possibleB))
	if (possibleB == B):
		print("We have a winner!")
		unfinishedA = factorsATimesC[x]
		unfinishedC = factorsATimesC[x+1]
		print("4. So we have (x + " + str(unfinishedA) + ")(x + " + str(unfinishedC) + ")")
		firstTerm  = "(x + " + str(unfinishedA) + ")"
		secondTerm = "(x + " + str(unfinishedC) + ")"

		if (A != 1):
			print("5. But we can't forget that we multipied by " + str(A))
			finishedA = unfinishedA / A
			finishedC = unfinishedC / A
			print("6. So we have (x + " + str(finishedA) + ")(x + " + str(finishedC) + ")")
			print("7. That didn't work...")
			print("8. Lets try: (" + str(A) + "x + " + str(unfinishedA) + ")(" + str(C) + "x + " + str(unfinishedC) + ")")
			print("9. But we can simplify this...")
			firstGCF = twoGCF(A, unfinishedA)
			print("10. " + str(A) + " & " + str(unfinishedA) + " have a greatest common factor of " + str(firstGCF))
			firstTerm = "("
			if (int(A/firstGCF) != 1): 
				firstTerm += str(int(A/firstGCF))
			firstTerm += "x + " + str(int(unfinishedA/firstGCF)) + ")"
			print("11 Therefore the first term should be " + firstTerm)
			print("12. Now to simpify the second part...")
			secondGCF = twoGCF(C, unfinishedC)
			print("13. " + str(C) + " & " + str(unfinishedC) + " have a greatest common factor of " + str(secondGCF))
			secondTerm = "(" + str(int(C/secondGCF)) + "x + " + str(int(unfinishedC/secondGCF)) + ")"
			print("14 Therefore the second term should be " + secondTerm)
		answer += firstTerm + secondTerm

print("My final answer is: " + answer)