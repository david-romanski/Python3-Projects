#  David Romanski
#  JavaScript Exercises
#  04/07/2020
#  Eloquent Javascript
#  Chapter 3: Recursion
#  Comments: Using recursion determine if a number is odd or even

def isEven(num):
  if (num == 0):
      return "even"
  if (num == 1):
      return "odd"
  return isEven(num-2)

num = 75
print("The number " + str(num) + " is " + isEven(num))