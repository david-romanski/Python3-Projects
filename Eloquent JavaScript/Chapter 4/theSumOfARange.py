#  David Romanski
#  JavaScript Exercises
#  Created: 04/08/2020
#  Updated: 04/09/2020
#  Eloquent Javascript
#  Chapter 4: The Sum Of A Range
#  Comments: Write a range function that returns an array from beginning to end inclusive. Then write a function that returns the sum of 
#  array. As a bonus add a third argument in range that performs as a stepper.
#  Updated to include inputs and validation.

def rangeOfArray(start, end):
  rangeArray = []
  for x in range(start, end+1):
    rangeArray.append(x)
  return rangeArray

def rangeOfArrayStep(start, end, step):
  rangeArray = []

  if (start < end):
    for x in range(start, end+1, step):
      rangeArray.append(x)
  else:
    for x in range(start, end-1, step):
      rangeArray.append(x)
  return rangeArray

def sumOfArray(rangeArray):
  sumArray = 0
  for x in range(0,len(rangeArray)):
    sumArray += rangeArray[x]
  return sumArray

while True:
  try:
    startRange = int(input("Please enter the start of the range: "))
  except ValueError:
    print("I'm sorry, I need an integer.")
    continue
  else:
    break

while True:
  try:
    endRange   = int(input("Please enter the end of the range: "))
  except ValueError:
    print("I'm sorry, I need an integer.")
    continue
  else:
    break

while True:
  try:
    stepRange  = int(input("Please enter the step: "))
  except ValueError:
    print("I'm sorry, I need an integer.")
    continue
  else:
    if (startRange < endRange): 
      if (stepRange > 0):
        break
    if (startRange > endRange): 
      if (stepRange < 0):
        break
    print("I'm sorry, the step value doesn't make sense.")

print("The sum of the range is: ", end="");
print(sumOfArray(rangeOfArrayStep(startRange,endRange,stepRange)))
