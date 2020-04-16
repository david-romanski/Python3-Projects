# David Romanski
# Create: 04/16/20
# Introduction to Java Programming
# Y Daniel Liang
# Programming Exercise 11.9
# Comments: Determine the area of a polygon.
# Added validation

import math

while True:
	try:
		numSides = int(input("Please enter the NUMBER of sides: "))
	except ValueError:
		print("I'm sorry, I need a positive integer.")
		continue
	else:
		if (numSides>0):
			break

while True:
	try:
		lenSides = float(input("Please enter the LENGTH of sides: "))
	except ValueError:
		print("I'm sorry, I need a positive number.")
		continue
	else:
		if (lenSides>0):
			break
		
area = ((numSides * (lenSides ** 2))/(4*math.tan(math.pi/numSides)));
		
area = round(area*100);
area = area/100;

print("The area of the polygon is: " + str(area))