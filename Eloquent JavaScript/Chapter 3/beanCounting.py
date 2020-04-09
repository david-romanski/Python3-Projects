#  David Romanski
#  JavaScript Exercises
#  Created: 04/07/2020
#  Updated: 04/09/2020
#  Eloquent Javascript
#  Chapter 3: Bean Counting
#  Comments: Write a function that counts the numbers of Bs in a string
#       Then write a function that counts the number of any character in a string
#  Updated to include inputs and validation.

def countChar(word, char):
  count = 0
  for x in range (0, len(word)):
    if (word[x] == char):
      count += 1
  return count

# Legacy code from the original problem. Not used.
def countBs(word):
  return countChar(word, "B")

while True:
	test = input("Please enter string to be searched: ")
	if (len(test)>0):
		break;

while True:
	key = input("Please enter key (chr) to search for: ")
	if (len(key) == 1):
		break;

print(countChar(test,key))
