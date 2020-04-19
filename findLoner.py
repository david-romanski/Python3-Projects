# David Romanski
# Create: 04/18/2020
# Computer Lab Project
# Find Loner
# Comments: Given a list of pairs and one number with no pair, find the loner.
# TODO: Check if the loner is POSSIBLE given the list of numbers (this isn't a sure thing)

# numbers = [4, 2, 4, 5, 5, 6, 1, 6, 7, 3, 7, 8, 3, 8, 2, 1, 9]
numbers = []
print("Please enter a list of paired numbers, one at a time, with one single \nnumber and I will try to find the lone number (s to submit list)")
rawInput = input("> ")
while (rawInput != 's') :
	if (rawInput.isdigit()) :
		numbers.append(int(rawInput))
	else: print("That is not valid.")
	rawInput = input("> ")
print(numbers)
answer = 0;
for x in range(0, len(numbers)) :
	answer = answer ^ numbers[x];
print("I think the lone number is: " + str(answer))