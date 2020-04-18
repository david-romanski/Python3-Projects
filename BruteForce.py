# Programmer: David Romanski
# Written: 04/18/2020
# Program: Brute Force
# Comments: This way is just called 'Starting Out' and seems like a brute force method to solve.

import math

def findPrimes(remainder):
	# This method finds all the prime numbers for a number
	factors = []

	print("Primes for " + str(remainder) + ": ", end="")
	while True :
		tempRem = remainder
		for x in range(2,remainder):
			if (remainder%x == 0) :
				print(str(x), end=" ")
				factors.append(x)
				remainder = int(remainder/x)
				break
		if (tempRem == remainder) :
			print(remainder)
			factors.append(remainder)
			break
	# print(factors)
	return factors

def GCF(num1, num2, num3) :
	number1 = num1
	number2 = num2
	number3 = num3
	commonFactors = []

	num1Array = findPrimes(number1)
	num2Array = findPrimes(number2)
	num3Array = findPrimes(number3)

	startX = 0
	startY = 0
	startZ = 0

	for x in range(startX, len(num1Array)) :
		for y in range(startY, len(num2Array)) :
			for z in range(startZ, len(num3Array)) :
				if (num1Array[x] == num2Array[y]) :
					if (num1Array[x] == num3Array[z]) :
						if (num2Array[y] == num3Array[z]) :
							commonFactors.append(num1Array[x])
							print(str(x) + " " + str(num1Array[x]))
							print(str(y) + " " + str(num2Array[y]))
							print(str(z) + " " + str(num3Array[z]))
							x += 1
							y += 1
							z += 1
							startX += 1
							startY += 1
							startZ += 1
							print("Hello!")

	final = 1
	for x in range(0, len(commonFactors)): 
		final *= commonFactors[x]
	print("GCF: " + str(final))
	return final

def findFactors(term) :
	listFactors = []
	# print("test " + (str(int(math.ceil((math.sqrt(term)))))))
	max = int(math.ceil(math.sqrt(term)))
	if (abs(term) == 1):
		max += 1
	if (term>0) :
		for x in range(1, max) :
			if ((term % x) == 0) :
				listFactors.append(int(term/x))
				listFactors.append(x)
				# print("(" + str(int(term / x)) + " * " + str(x) + ") ")
				listFactors.append(int(-term/x))
				listFactors.append(-x)
				# print("(" + str(int(-term / x)) + " * " + str(-x) + ") ") 
	if (term<0) :
		absTerm = math.abs(term)
		for x in range(1, max+1) :
			if ((absTerm % x) == 0) :
				listFactors.append(int(-absTerm/x))
				listFactors.append(x)
				# print("(" + str(int(-term / x)) + " * " + str(x) + ") ")
				listFactors.append(int(absTerm/x))
				listFactors.append(-x)
				# print("(" + str(int(term / x)) + " * " + str(-x) + ") ")
	return listFactors

while True:
	try:
		A = int(input("Please enter a nonzero integer for the first term: "))
	except ValueError:
		print("I'm sorry, I didn't understand that.")
		continue
	else:
		if (A != 0):
			break

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

factor = GCF(A, B, C)
A = int(A/factor)
B = int(B/factor)
C = int(C/factor)

# Showing factors of A
print("A(" + str(A) + ") can be ", end="")
factorsA = findFactors(A)
print(factorsA)

# Showing factors of C
print("C(" + str(C) + ") can be ", end="")
factorsC = findFactors(C)
print(factorsC)

answer = ""

print("That means that B(" + str(B) + ") can be ")

for x in range(0, len(factorsA)-1, 2) :
	for y in range(0, len(factorsC)-1, 2) :
		print("(" + str(factorsA[x]) + " * " + str(factorsC[y]) + ") + (" + str(factorsA[x+1]) + " * " + str(factorsC[y+1]) + ") = ", end="")
		possibleB = factorsA[x] * factorsC[y] + factorsA[x+1] * factorsC[y+1] 
		print(possibleB)
		if (possibleB == B) :
			if (factor != 1):
				answer += str(factor)
			answer += "("
			if (abs(factorsA[x]) == 1) :
				if (factorsA[x] == -1) :
					answer += '-'
			else: answer += str(factorsA[x])

			answer += "x"

			if (factorsC[y+1] < 0) :
				answer += ' - '
			else: answer += ' + '
			answer += str(abs(factorsC[y+1]))

			answer += ")("

			if (abs(factorsA[x+1]) == 1) :
				if (factorsA[x+1] == -1) :
					answer += '-'
			else: answer += str(factorsA[x+1])

			answer += "x"
 
			if (factorsC[y] < 0) :
				answer += ' - '					
			else: answer += ' + '
			answer += str(abs(factorsC[y]))

			answer += ')\n'
			print(answer)

		print("(" + str(factorsA[x+1]) + " * " + str(factorsC[y]) + ") + (" + str(factorsA[x]) + " * " + str(factorsC[y+1]) + ") = ", end="")
		possibleB = factorsA[x+1] * factorsC[y] + factorsA[x] * factorsC[y+1]
		print(possibleB)
		if (possibleB == B) :
			if (factor != 1) :
				answer += str(factor)
			answer += "("
			if (abs(factorsA[x+1]) == 1) :
				if (factorsA[x+1] == -1) :
					answer += '-'
			else: answer += str(factorsA[x+1])

			answer += "x"

			if (factorsC[y+1] < 0) :
				answer += ' - '
			else: answer += ' + '
			answer += str(abs(factorsC[y+1]))

			answer += ")("

			if (abs(factorsA[x]) == 1) :
				if (factorsA[x] == -1) :
					answer += '-'
			else: answer += str(factorsA[x])

			answer += "x"
 
			if (factorsC[y] < 0) :
				answer += ' - '					
			else: answer += ' + '
			answer += str(abs(factorsC[y]))

			answer += ')\n'
			print(answer)

print("My answer(s) are: ")
print(answer)