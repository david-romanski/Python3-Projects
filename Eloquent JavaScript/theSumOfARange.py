#  David Romanski
#  JavaScript Exercises
#  Updated: 04/08/2020
#  Eloquent Javascript
#  Chapter 4: The Sum Of A Range
#  Comments: Write a range function that returns an array from beginning to end inclusive. Then write a function that returns the sum of 
#  array. As a bonus add a third argument in range that performs as a stepper.

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

print("Range from 1 to 10: ", end ='')
print(rangeOfArray(1,10))

print("Range from 10 to 1: ", end ='')
print(rangeOfArrayStep(10,1,-1))

print("Range from 5 to 2 using step -1: ", end ='')
print(rangeOfArrayStep(5, 2, -1))

print("Sum from 1 to 10: " + str(sumOfArray(rangeOfArray(1,10))))

print("Sum from 1 to 100 using step 5: ", end='')
print(sumOfArray(rangeOfArrayStep(1, 100, 5)))