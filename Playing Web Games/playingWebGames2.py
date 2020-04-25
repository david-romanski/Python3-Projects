# David Romanski
# Started 04/22/2020
# Playing Web Games
# Comments: This program reads the walkthrough from a separate file for a text 
# adventure/interactive fiction game. It runs though the game, hopefully to completion.
# This automaton 'sees' the responses from the website, but is 'dumb' in that it doesn't
# act on them.

import time
import selenium
from selenium import webdriver

# Using Chrome to access web
driver = webdriver.Chrome();

# Open the website
driver.get('http://www.web-adventures.org/cgi-bin/webfrotz?s=Jigsaw')

def loadWalkthrough():
	walkthrough = []
	file = open("jigsawWalkthrough.txt", "r")
	for line in file:
		line = line.replace('[', '')
		line = line.replace(']', '')
		# The walkthrough has spaces before commands, but no spaces before comments.
		# So I'm removing the comments
		if (line[0] == ' '):
			# print(line)
			input = line.strip();
			walkthrough.append(input)
	print(len(walkthrough))
	file.close()
	return walkthrough

walkthrough = loadWalkthrough()
# print(len(walkthrough))

# for x in range(0, len(walkthrough)) :
#	print(str(x) + ': ' + walkthrough[x])

# Counts the number of words in input string
#for x in range(0, len(walkthrough)) :
#	numWords = len(walkthrough[x].split())
#	print("On line " + str(x) + " there are " + str(numWords) + " words.")

listSecondWords = []

for x in range(0, len(walkthrough)) :
	descrip = driver.find_elements_by_tag_name('td')
#	descrip = driver.find_element_by_tag_name('(text)')
#	descrip = driver.findElements(By.)
#	descrip = driver.findElement(By.id(<tr>));
#	print(len(descrip))

# I don't think we have to loop this.
#	for e in descrip:
#		print('0: ' + descrip[0].text)
#		print('1: ' + descrip[1].text)

	# This shows all the output that was scraped from the game.
	output = descrip[1].text.splitlines()

	# This is checking the -4 line to see if there is an error
	if (output[len(output) - 1] == "You can't see any such thing.") :
		print("There is an error!!!")
		break

#	for y in range(len(output), 0, -1) :
#		print("-" + str(y) + ": " + output[len(output) - y])
#		print('2: ' + descrip[2].text)

	# This finds if the second character in a string is upper case
	# This then assumes that line is the label and below is the description
#	for y in range(0, len(output)) :
#		print(str(y) + ": " + str(output[y].isupper()))

	y = len(output) - 1
	while (not output[y].isupper()) :
		if (not(output[y] == "")) :
#			print("I FOUND A BLANK AT: " + str(y))
#		else :
			rawLine = output[y].split()
			badChars = ['\"', '(', ')', '[', ']', '?', '.', ',', ':']
			for i in range(0, len(rawLine)) :
				for j in badChars :
					rawLine[i] = rawLine[i].replace(j, '')
			# print(rawLine)
			listSecondWords += rawLine
			listSecondWords = list(dict.fromkeys(listSecondWords))
#			print(str(len(listSecondWords)) + ": ", end="")
#			print(listSecondWords)
			f = open("secondWordList.txt", "w")
			for z in range(0, len(listSecondWords)) :
				f.write(listSecondWords[z] + '\n')
			f.close()
		y -= 1
	
	# Waiting for Guggenheim's letter
	if (walkthrough[x] == "repeatedly wait until Guggenheim gives you the letter") :
		print(str(x) + '/' + str(len(walkthrough)) + ": test[" + walkthrough[x] + "](Waiting...)")
		while (output[len(output) - 1].find("he pushes a letter of some kind into your hand") != -1) :
			print(str(x) + '/' + str(len(walkthrough)) + ": test[wait](Waiting...)")
			input_box = driver.find_element_by_name('a')
			input_box.send_keys("wait")
			input_box.submit()		

			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print(output[len(output) - 1])
		x += 1

	# The a4 and c2 and c1 pieces may have to be turned to work... 
	# c1
	if (walkthrough[x] == "put the edge piece at c1") :
		while (output[len(output) - 1] != "[Your score has just gone up by one point.]") :
			print(str(x) + '/' + str(len(walkthrough)) + ": test[" + walkthrough[x] + "](c1)")
			input_box = driver.find_element_by_name('a')
			input_box.send_keys(walkthrough[x])
			input_box.submit()		

			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print(output[len(output) - 1])
			if (output[len(output) - 1] == "It would project into the left-hand edge there.") :
				input_box = driver.find_element_by_name('a')
				input_box.send_keys("turn edge piece")
				input_box.submit()
			else :
				x += 1

	# a4
	if (walkthrough[x] == "put corner piece at a4") :
		while (output[len(output) - 1] != "[Your score has just gone up by one point.]") :
			print(str(x) + '/' + str(len(walkthrough)) + ": test[" + walkthrough[x] + "]test")
			input_box = driver.find_element_by_name('a')
			input_box.send_keys(walkthrough[x])
			input_box.submit()		

			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print(output[len(output) - 1])
#			if (output[len(output) - 1] == "[Your score has just gone up by one point.]") :
			if (output[len(output) - 1] == "It fits in nicely at a4.") :
				input_box = driver.find_element_by_name('a')
				input_box.send_keys("take a4. turn corner piece")
				input_box.submit()
			else :
				x += 1
				# Gotta clear out the output of getting a point...
				input_box = driver.find_element_by_name('a')
				input_box.send_keys("look")
				input_box.submit()		

				descrip = driver.find_elements_by_tag_name('td')
				output = descrip[1].text.splitlines()
				print("Resetti!: " + output[len(output) - 1])
				break

	# c2
	if (walkthrough[x] == "put centre piece at c2") :
		while (output[len(output) - 1] != "[Your score has just gone up by one point.]") :
			print(str(x) + '/' + str(len(walkthrough)) + ": test[" + walkthrough[x] + "]test")
			input_box = driver.find_element_by_name('a')
			input_box.send_keys(walkthrough[x])
			input_box.submit()		

			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print(output[len(output) - 1])
			if (output[len(output) - 1] == "It fits in nicely at c2.") :
				input_box = driver.find_element_by_name('a')
				input_box.send_keys("take c2. turn centre piece")
				input_box.submit()
			else :
				x += 1

	# Sends walkthrough command to game
	print(str(x) + '/' + str(len(walkthrough)) + ": test[" + walkthrough[x] + "]test(Main)")
	input_box = driver.find_element_by_name('a')
	input_box.send_keys(walkthrough[x])
	input_box.submit()
	time.sleep(1)

input_box = driver.find_element_by_name('a')
input_box.send_keys('score')
input_box.submit()
