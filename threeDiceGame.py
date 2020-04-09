# Programmer: David Romanski
# Three Dice Game
# Created: unknown
# Updated: 04/09/2020
# Simple random game. Updated input/output and added verification. Also updated for Python3.

import random

print("You are given a 6 sided dice.  After you roll you get the amount back in dollars (1 = $1, 2 = $2,...).")
print("After you roll once you can keep or roll again. After your second roll you can keep")
print("or roll again. After your third roll you muss keep the roll.  Hit enter to roll the first die:")

enter = input("Hit enter to roll the first die: ")
die = random.randint(1,6)
print("You rolled a " + str(die) + ".")
while True:
		enter = input("Do you want to keep?(y/n): ")
		if (enter == 'y'): 
			break
		if (enter == 'n'):
			break
		print("I'm sorry, I didn't understand that.")

if (enter != 'y'):
	print("Rolling again!!!")
	die = random.randint(1,6)
	print("You rolled a " + str(die) + ".")

	while True:
			enter = input("Do you want to keep?(y/n): ")
			if (enter == 'y'):
				break 
			if (enter == 'n'):
				break
			print("I'm sorry, I didn't understand that.")
			continue

	if enter != 'y':
		print("Rolling again!!!")
		die = random.randint(1,6)
		print("You rolled a " + str(die) + ".")
		print("You won $" + str(die) + "!!!")
	else:
		print("You won $" + str(die) + "!!!")
else:
	print("You won $" + str(die) + "!!!")