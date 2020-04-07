#  David Romanski
#  JavaScript Exercises
#  4/07/2020
#  Eloquent Javascript
#  Chapter 3: Minimum
#  Comments: Give 2 numbers displays the minimum number

def min(num1, num2):
  if (num1 == num2):
    return "both are equal."
  elif (num1 > num2):
    return num2
  else: return num1

num1 = 100;
num2 = 100;
print("Between " + str(num1) + " and " + str(num2) + " the minimum is ", end='')
print(min(num1, num2))