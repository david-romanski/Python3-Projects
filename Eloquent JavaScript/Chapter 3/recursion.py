#  David Romanski
#  JavaScript Exercises
#  Created: 04/07/2020
#  Updated: 04/09/2020
#  Eloquent Javascript
#  Chapter 3: Recursion
#  Comments: Using recursion determine if a number is odd or even
#  Updated to include input.

def isEven(num):
  if (abs(num) == 0):
      return "even"
  if (abs(num) == 1):
      return "odd"
  return isEven(abs(num)-2)

while (True):
	try:
		num = int(input("Please enter an integer to determing if it is odd or even: "))
	except ValueError:
		print("I'm sorry, I need an integer.")
		continue
	else: break

print("The number " + str(num) + " is " + isEven(num))
