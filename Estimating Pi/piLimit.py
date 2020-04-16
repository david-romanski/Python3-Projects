# Programmer: David Romanski
# Pi Convergence Gregory-Leibniz
# Created: 04/16/2020
# This program uses convergence method of Gregory-Leibniz series to estimate pi.
import math

while True:
	try:
		x = float(input("Please enter a number, the larger the better: "))
	except ValueError:
		print("I'm sorry, I didn't understand that.")
		continue
	else:
		if (x>0):
			break


answer = math.radians(x * math.sin(180/x))

print(answer)