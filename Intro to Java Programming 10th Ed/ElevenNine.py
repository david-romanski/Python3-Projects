# David Romanski
# Created: 04/11/2020
# Introduction to Java Programming
# Y Daniel Liang
# Programming Exercise 11.9
# Comments: Fill a variable sized matrix with 1s and 0s 
# then find the rows and columns with the most 1s.

import random

while True:
	try:
		n = int(input("Please enter size of matrix: "))
	except ValueError:
		print("I'm sorry, I need a positive integer.")
		continue
	else:
		if (n>0):
			break
		
randomMatrix = [[0 for x in range(n)] for y in range(n)]

for x in range(0, n):
	for y in range(0,n):
		num = round(random.random()) 
		randomMatrix[x][y] = num

print("The random array is:")
for x in range(0, n):
	for y in range(0, n):
		print(randomMatrix[x][y], end="")
	print()

largestRow = [0]*n
				
largeRow = 0
for x in range(0, n):
	ones = 0
	for y in range(0, n):
		ones += randomMatrix[x][y]
		if (ones > largeRow):
			largeRow = ones
			largestRow = []
			largestRow.append(x)
		elif (largeRow == ones):
			if (largestRow[len(largestRow)-1] != x):
				largestRow.append(x)
			
print("The largest row index: " + str(largestRow))

largestColumn = [0]*n
				
largeColumn = 0;
for y in range(0, n):
	ones = 0;
	for x in range(0, n):
		if (randomMatrix[x][y] == 1):
			ones +=1
			if (ones > largeColumn):
				largeColumn = ones
				largestColumn = []
				largestColumn.append(y)
			elif (largeColumn == ones):
				if (largestColumn[len(largestColumn)-1] != y):
					largestColumn.append(y);

print("The largest column index: " + str(largestColumn))