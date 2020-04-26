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
####################################### end loadWalkthrough #######################################

def placePuzzlePiece(piece, placement, output) :
# This def will take a pice (corner/edge) and put it in a position (a1...)
# It will handle any errors if the piece is placed incorrectly.

#	if (walkthrough[x] == "put the corner piece at a1") :
		if (placement == "grille") :
			input_box = driver.find_element_by_name('a')
			input_box.send_keys("put jigsaw piece in grille")
			input_box.submit()
			return

		sucessLine = "It fits at " + placement + ","
		while (output[len(output) - 3].find(sucessLine) == -1) :
			#pause = input("checking.")
			print(str(x) + '/' + str(len(walkthrough)) + ": [" + placement + "](Puzzle Piece)")
			input_box = driver.find_element_by_name('a')
			input_box.send_keys("put " + piece + " piece at " + placement)
			input_box.submit()		

			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print(output[len(output) - 1])

			if (output[len(output) - 1].find("That won't fit because of the piece on") != -1) :
				input_box = driver.find_element_by_name('a')
				input_box.send_keys("turn " + piece + " piece")
				input_box.submit()
			if (output[len(output) - 1].find("It fits in nicely at") != -1) :
				input_box = driver.find_element_by_name('a')
				input_box.send_keys("take " + placement + ". turn " + piece + " piece")
				input_box.submit()
			if (output[len(output) - 1].find("It would project into the") != -1) :
				input_box = driver.find_element_by_name('a')
				input_box.send_keys("turn " + piece + " piece")
				input_box.submit()
		return
######################################### end placePuzzlePiece ####################################

def checkCommand(walkthrough, output) :
# Parts of this game are random and need to be done multiple times. This def attempts to handle
# those situations. 

	# Follow the Parisiens until you find the absinthe
	if (walkthrough[x] == "follow the Parisiens until you find the absinthe") :
		print("-1: " + output[len(output) - 1])
		print("-2: " + output[len(output) - 2])
		print("-3: " + output[len(output) - 3])
		print("-4: " + output[len(output) - 4])
		print("-5: " + output[len(output) - 5])
		# pause = input("We need to follow the leader...")
		while(output[len(output) - 1].find("absinthe") == -1) :
			if (output[len(output) - 1].find("north.") != -1) :
					input_box = driver.find_element_by_name('a')
					input_box.send_keys("north")
					input_box.submit()
			elif (output[len(output) - 1].find("northeast") != -1) :
					input_box = driver.find_element_by_name('a')
					input_box.send_keys("northeast")
					input_box.submit()
			elif (output[len(output) - 1].find(" east") != -1) :
					input_box = driver.find_element_by_name('a')
					input_box.send_keys("east")
					input_box.submit()
			elif (output[len(output) - 1].find("southeast") != -1) :
					input_box = driver.find_element_by_name('a')
					input_box.send_keys("southeast")
					input_box.submit()
			elif (output[len(output) - 1].find("south.") != -1) :
					input_box = driver.find_element_by_name('a')
					input_box.send_keys("south")
					input_box.submit()
			elif (output[len(output) - 1].find("southwest") != -1) :
					input_box = driver.find_element_by_name('a')
					input_box.send_keys("southwest")
					input_box.submit()
			elif (output[len(output) - 1].find(" west") != -1) :
					input_box = driver.find_element_by_name('a')
					input_box.send_keys("west")
					input_box.submit()
			elif (output[len(output) - 1].find("northwest") != -1) :
					input_box = driver.find_element_by_name('a')
					input_box.send_keys("northwest")
					input_box.submit()

#		percent = (int(10000*(x/(len(walkthrough))))/100)
#		print(str(x) + '/' + str(len(walkthrough)) + " " + str(percent), end="")
#		print("%: test[" + walkthrough[x] + "]test(Main)")
#		input_box = driver.find_element_by_name('a')
#		input_box.send_keys(walkthrough[x])
#		input_box.submit()

			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print("-1: " + output[len(output) - 1])
			print("-2: " + output[len(output) - 2])
			print("-3: " + output[len(output) - 3])
			print("-4: " + output[len(output) - 4])
			print("-5: " + output[len(output) - 5])
		return

	# 1st check to make sure suitcase wasn't taken.
	if (walkthrough[x] == "push suitcase east") :
		percent = (int(10000*(x/(len(walkthrough))))/100)
		print(str(x) + '/' + str(len(walkthrough)) + " " + str(percent), end="")
		print("%: test[" + walkthrough[x] + "]test(Push Suitcase)")
		input_box = driver.find_element_by_name('a')
		input_box.send_keys(walkthrough[x])
		input_box.submit()

		descrip = driver.find_elements_by_tag_name('td')
		output = descrip[1].text.splitlines()
		print("-1: " + output[len(output) - 1])
		print("-2: " + output[len(output) - 2])
		print("-3: " + output[len(output) - 3])
		print("-4: " + output[len(output) - 4])
		print("-5: " + output[len(output) - 5])
#		pause = input("That tricky devil!")
		while (output[len(output) -1].find("Fleming comes along") != -1) :
			input_box = driver.find_element_by_name('a')
			input_box.send_keys("west. " + walkthrough[x])
			input_box.submit()
			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print("-1: " + output[len(output) - 1])
			print("-2: " + output[len(output) - 2])
			print("-3: " + output[len(output) - 3])
			print("-4: " + output[len(output) - 4])
			print("-5: " + output[len(output) - 5])
#			pause = input("That tricky devil!")
		return

	# 2nd wait until Fleming finds the mouldy dish
	if (walkthrough[x] == "wait until Fleming finds the mouldy dish") :
#		pause = input("Problem with Fleming...")
		descrip = driver.find_elements_by_tag_name('td')
		output = descrip[1].text.splitlines()
		print("-1: " + output[len(output) - 1])
		print("-2: " + output[len(output) - 2])
		print("-3: " + output[len(output) - 3])
		print("-4: " + output[len(output) - 4])
		print("-5: " + output[len(output) - 5])
		print("-6: " + output[len(output) - 6])
		percent = (int(10000*(x/(len(walkthrough))))/100)
		print(str(x) + '/' + str(len(walkthrough)) + " " + str(percent), end="")
		print("%: test[" + walkthrough[x] + "]test(Mouldy Dish)")
		while ((output[len(output) - 4].find("mouldy dish") == -1) and (output[len(output) - 4].find("mouldy dish") == -1) and (output[len(output) - 6].find("mouldy dish") == -1)) :
#			print(str(x) + '/' + str(len(walkthrough)) + ": test[wait](Mouldy dish...)")
			input_box = driver.find_element_by_name('a')
			input_box.send_keys("wait")
			input_box.submit()		

			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print("-1: " + output[len(output) - 1])
			print("-2: " + output[len(output) - 2])
			print("-3: " + output[len(output) - 3])
			print("-4: " + output[len(output) - 4])
			print("-5: " + output[len(output) - 5])
			print("-6: " + output[len(output) - 6])
		return

	# 3rd wait until the disturbed air appears
	if (walkthrough[x] == "wait until the disturbed air appears") :
#		pause = input("Problem with disturbed air...")
		percent = (int(10000*(x/(len(walkthrough))))/100)
		print(str(x) + '/' + str(len(walkthrough)) + " " + str(percent), end="")
		print("%: test[" + walkthrough[x] + "]test(Disturbed Air)")
		while ((output[len(output) - 2].find("disturbed") == -1) and (output[len(output) - 4].find("disturbed") == -1)):
#			print(str(x) + '/' + str(len(walkthrough)) + ": test[wait](Disturbed air...)")
			input_box = driver.find_element_by_name('a')
			input_box.send_keys("wait")
			input_box.submit()		

			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print("-1: " + output[len(output) - 1])
			print("-2: " + output[len(output) - 2])
			print("-3: " + output[len(output) - 3])
			print("-4: " + output[len(output) - 4])
			print("-5: " + output[len(output) - 5])
		return

	if (walkthrough[x].find("put") != -1):
		if (walkthrough[x].find("piece") != -1):
			cutupLine = walkthrough[x].split()
#			pause = input(cutupLine[-4] + " " + cutupLine[-1])
			placePuzzlePiece(cutupLine[-4], cutupLine[-1], output)
			return

	# Waiting for Guggenheim's letter
	if (walkthrough[x] == "repeatedly wait until Guggenheim gives you the letter") :
		percent = (int(10000*(x/(len(walkthrough))))/100)
		print(str(x) + '/' + str(len(walkthrough)) + " " + str(percent), end="")
		print("%: test[" + walkthrough[x] + "]test(Letter)")
		while ((output[len(output) - 2].find("letter") == -1) and (output[len(output) - 4].find("letter") == -1)) :
			#print(str(x) + '/' + str(len(walkthrough)) + ": test[wait](Waiting...)")
			input_box = driver.find_element_by_name('a')
			input_box.send_keys("wait")
			input_box.submit()		

			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print("-1: " + output[len(output) - 1])
			print("-2: " + output[len(output) - 2])
			print("-3: " + output[len(output) - 3])
			print("-4: " + output[len(output) - 4])
			print("-5: " + output[len(output) - 5])
		return

	# Finding the snow leopard.
	if (walkthrough[x] == "find the snow leopard") :
#		pause = input("Finding the snow leopard.")
		descrip = driver.find_elements_by_tag_name('td')
		output = descrip[1].text.splitlines()
		print("-1: " + output[len(output) - 1])
		print("-2: " + output[len(output) - 2])
		print("-3: " + output[len(output) - 3])
		print("-4: " + output[len(output) - 4])
		print("-5: " + output[len(output) - 5])


		while (output[len(output)- 1].find("leopard") == -1) :
			input_box = driver.find_element_by_name('a')
			input_box.send_keys("east")
			input_box.submit()

			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print("-1: " + output[len(output) - 1])
			print("-2: " + output[len(output) - 2])
			print("-3: " + output[len(output) - 3])
			print("-4: " + output[len(output) - 4])
			print("-5: " + output[len(output) - 5])
		return

	# find the Tundra again
	if (walkthrough[x] == "find the Tundra again") :
#		pause = input("Finding the Tundra.")
		descrip = driver.find_elements_by_tag_name('td')
		output = descrip[1].text.splitlines()
		print("-1: " + output[len(output) - 1])
		print("-2: " + output[len(output) - 2])
		print("-3: " + output[len(output) - 3])
		print("-4: " + output[len(output) - 4])
		print("-5: " + output[len(output) - 5])

		while (output[len(output)- 3].find("TUNDRA") == -1) :
			input_box = driver.find_element_by_name('a')
			input_box.send_keys("east")
			input_box.submit()

			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print("-1: " + output[len(output) - 1])
			print("-2: " + output[len(output) - 2])
			print("-3: " + output[len(output) - 3])
			print("-4: " + output[len(output) - 4])
			print("-5: " + output[len(output) - 5])
		return

#	if (walkthrough[x] == "play mandolin") :
#		pause = input("Checking on mandolin")

	# wait until the mouse pauses, inspecting the trap
	if (walkthrough[x] == "wait until the mouse pauses, inspecting the trap") :
#		pause = input("Waiting for the mouse.")
		descrip = driver.find_elements_by_tag_name('td')
		output = descrip[1].text.splitlines()
		print("-1: " + output[len(output) - 1])
		print("-2: " + output[len(output) - 2])
		print("-3: " + output[len(output) - 3])
		print("-4: " + output[len(output) - 4])
		print("-5: " + output[len(output) - 5])
#		while (output[len(output)- 1].find("A mouse rushes in and then pauses, inspecting the mousetrap.") == -1) :
		while (output[len(output)- 1].find("inspecting the mousetrap") == -1) :
			input_box = driver.find_element_by_name('a')
			input_box.send_keys("wait")
			input_box.submit()

			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print("-1: " + output[len(output) - 1])
			print("-2: " + output[len(output) - 2])
			print("-3: " + output[len(output) - 3])
			print("-4: " + output[len(output) - 4])
			print("-5: " + output[len(output) - 5])
#			pause = input("Waiting for the mouse.")
		return

	# Sends walkthrough command to game
	percent = (int(10000*(x/(len(walkthrough))))/100)
	print(str(x) + '/' + str(len(walkthrough)) + " " + str(percent), end="")
	print("%: test[" + walkthrough[x] + "]test(Main)")
	input_box = driver.find_element_by_name('a')
	input_box.send_keys(walkthrough[x])
	input_box.submit()
	#time.sleep(1)


#################################### end checkCommands ############################################

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
	
	checkCommand(walkthrough, output)

input_box = driver.find_element_by_name('a')
input_box.send_keys('score')
input_box.submit()
