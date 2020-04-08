#  David Romanski
#  JavaScript Exercises
#  Created: 04/07/2020
#  Eloquent Javascript
#  Chapter 3: Bean Counting
#  Comments: Write a function that counts the numbers of Bs in a string
#       Then write a function that counts the number of any character in a string

def countChar(word, char):
  count = 0
  for x in range (0, len(word)):
    if (word[x] == char):
      count += 1
  return count

def countBs(word):
  return countChar(word, "B")

test1 = "BBbbBB"
test2 = "WWwwWW"
key2 = "w"

print("Testing countBs with " + test1 + ". Count is: ", end ='')
print(countBs(test1))
print("Testing countChar with " + test2 + " using " + key2 + ". Count is: ", end = '')
print(countChar(test2, key2))