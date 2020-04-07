#  David Romanski
#  JavaScript Exercises
#  4/7/2020
#  Eloquent Javascript
#  Chapter 2: Looping A Triangle

for x in range (0,7):
  line = ""
  for y in range (0, x):
    line += "#"
  print(line)