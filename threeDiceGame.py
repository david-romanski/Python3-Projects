# Programmer: David Romanski
# Three Dice Game
# Created: unknown
# Updated: 04/09/2020, 04/19/2020
# Simple random game. Updated input/output and added verification. Also updated for Python3.
# Added starting balance and win/losing to game.
import random

def checkWinnings(die, balance):
	if (die == 1):
		print("I'm sorry, you lost.")
	if (die == 2):
		print("I'm sorry, you lost.")
	if (die == 3):
		print("You get your money back!")
		balance += 10
	if (die == 4):
		print("You get your money back!")
		balance += 10
	if (die == 5):
		print("You won $10!")
		balance += 20
	if (die == 6):
		print("You won $10!")
		balance += 20
	return balance
		
print("You have $50. To play it costs $10. You are given a 6 sided dice.  If you roll a 1 or 2 you lost. If you roll")
print("a 3 or 4 you get your money back. If you roll a 5 or 6 you win $10. After you roll once you can keep or roll")
print("again. After your second roll you can keep or roll again. After your third roll you muss keep the roll.")

balance = 50

print("Balance: $" + str(balance), end=" ")
enter = input("Hit enter to roll the first die (q to quit): ")
while (enter != 'q'):
	balance -= 10
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
			balance = checkWinnings(die, balance)
		else:
			balance = checkWinnings(die, balance)
	else:
		balance = checkWinnings(die, balance)
	if (balance <= 0):
		break
	print("Balance: $" + str(balance), end=" ")
	enter = input("Hit enter to roll the first die (q to quit): ")
