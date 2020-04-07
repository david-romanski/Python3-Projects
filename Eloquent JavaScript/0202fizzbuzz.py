# David Romanski
# JavaScript Exercises
# 04/07/2020
# Eloquent Javascript
# Chapter 2: FizzBuzz
# Comments: From 1 to 100
# If a number is divisible by 3 it prints Fizz
# If a number is divisible by 5 it prints Buzz
# If a number is both it prints FizzBuzz
for i in range(1,100):
  if (i%3 == 0):
    if (i%5 == 0):
      print("FizzBuzz")
    print("Fizz")  
  elif (i%5 == 0):
    print("Buzz")
  else: print(i)