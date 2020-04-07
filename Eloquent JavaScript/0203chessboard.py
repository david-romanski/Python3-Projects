# David Romanski
# JavaScript Exercises
# 2/24/2020
# Eloquent Javascript
# Chapter 2: Chessboard
# Comments: Draw a chessboard grid of size

size = 10;
for x in range(0,size):
  for y in range(0,size):
    if (x%2 == 1):
      if (y%2 == 0):
        print(" ", end='')
      else: print("#", end='')
    elif (y%2 == 0):
      print("#", end='')
    else: print(" ", end='')
  print()