#  David Romanski
#  JavaScript Exercises
#  Created: 04/07/2020
#  Updated: 04/09/2020
#  Eloquent Javascript
#  Chapter 3: Minimum
#  Comments: Give 2 numbers displays the minimum number.
#  Updated to include input. Decided to not validate input because it gives neat results when you put in other things.

def min(num1, num2):
  if (num1 == num2):
    return "neither."
  elif (num1 > num2):
    return num2
  else: return num1

num1 = input("Please enter first value: ")
num2 = input("Please enter second value: ")

print("The minimum between " + str(num1) + " and " + str(num2) + " is ", end='')
print(min(num1, num2))
