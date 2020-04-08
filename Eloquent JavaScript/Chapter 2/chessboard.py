# David Romanski
# JavaScript Exercises
# Created: 04/07/2020
# Updated: 04/08/2020
# Eloquent Javascript
# Chapter 2: Chessboard
# Comments: Draw a chessboard grid of size
# Updated to allow input to determine size.

while True:
	try:
		size = int(input("Please enter a positive integer for the size of the requested chessboard: "))
	except ValueError:
		print("I'm sorry, I didn't understand that.")
		continue
	else:
		if (size>0):
			break

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
