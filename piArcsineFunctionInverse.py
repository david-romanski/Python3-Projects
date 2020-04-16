# Programmer: David Romanski
# Pi Arcsine Function/Inverse
# Created: 04/16/2020
# This program uses Arcsine Function/Inverse to estimate pi.
import math

while True:
	try:
		x = float(input("Please enter a number between -1 and 1: "))
	except ValueError:
		print("I'm sorry, I didn't understand that.")
		continue
	else:
		if (x>-1):
			if (x<1):
				break

answer = 2 * (math.asin(math.sqrt(1 - x**2)) + abs(math.asin(x)))

print(answer)