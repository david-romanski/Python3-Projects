# David Romanski
# JavaScript Exercises
# 04/12/2020
# Eloquent Javascript
# Chapter 4: Reversing An Array
#Comments: Given an array return a new array with everything reversed, then reverse array without using a new array.

def reverseArray(arrayIn):
  arrayOut = []
  for x in range(0,len(arrayIn)):
    arrayOut.append(arrayIn[(len(arrayIn)-1)-x])
  return arrayOut

def reverseArrayInPlace(arrayIn):
  temp = arrayIn[0]
  for x in range(0,len(arrayIn)):
    arrayIn[x] = arrayIn[(len(arrayIn)-1)-x];
  arrayIn[(len(arrayIn)-1)] = temp
  return arrayIn

test = ["A","B","C"];
print("Reversing array " + str(test))
print(reverseArray(test))

print("Reversing array in place " + str(test))
print(reverseArrayInPlace(test))

test = [1, 2, 3, 4, 5];
print("Reversing array " + str(test))
print(reverseArray(test))

print("Reversing array in place " + str(test))
print(reverseArrayInPlace(test))