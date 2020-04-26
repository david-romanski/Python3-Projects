# David Romanski
# Started 04/22/2020
# Playing Web Games 3
# Comments: This program creates all possible combinations and loads it into an array for
# a text  adventure/interactive fiction game. It runs though the game, removing commands
# that are invalid and will hopefully finish game to completion.
# This automaton 'sees' the responses from the website, and uses these responses to 'become
# smarter'.

import time
import selenium
from selenium import webdriver
import importlib
import winsound
import makingInput

def testWordList(listWT, newFile) :
# This def accepts a list of commands and the output file. It opens the game website and 
# checks if the commands are valid.

	# Using Chrome to access web
	driver = webdriver.Chrome();

	# Open the website
	driver.get('http://www.web-adventures.org/cgi-bin/webfrotz?s=Jigsaw')

	for x in range(0, len(listWT)) :
		if (listWT[x] == "") :
			return
		print("Checking " + listWT[x])

		# Submit command into game
		print(str(x) + "/" + (str(len(listWT))) + ": test[" + listWT[x] + "]test")
		input_box = driver.find_element_by_name('a')
		input_box.send_keys(listWT[x])
		input_box.submit()

		# Collect output and determine if command is valid
		descrip = driver.find_elements_by_tag_name('td')
		output = descrip[1].text.splitlines()
		print(str(len(output)) + " " + listWT[x] + ': ' + output[len(output)-1])

		valid = True
		if (output[len(output) - 1] == "That's not a verb I recognise."):
			print(listWT[x] + " isn't valid.")
			valid = False

		if (output[len(output) - 1] == "You seem to want to talk to someone, but I can't see whom."):
			print(listWT[x] + " isn't valid.")
			valid = False

		if (output[len(output) - 1] == "You can only do that to something animate.") :
			print(listWT[x] + " isn't valid.")
			valid = False

		if (valid) :
			print("Valid input with " + listWT[x])
			# tempWT.append(walkthrough[x])
			# print(tempWT)
			#if command is valid save to new file
			newFile.write(listWT[x] + '\n')

	# Finish up and check score!
	input_box = driver.find_element_by_name('a')
	input_box.send_keys('score')
	input_box.submit()
####################################### end Test Word List ########################################

def oneWordTest() :
# This check only the first word.
	try:
		f = open("inputList.txt", "x")
		print("No file found. Creating new input file...")
		makingInput.createListFirstWord(f)
		f.close()
	except FileExistsError:
		print("File already exists.")

	print("Loading file...")
	oldFile = open("inputList.txt", "r")
	newFile = open("inputList2.txt", "w")
	newFile.close()

	# Pull 1000 commands
	listWT = makingInput.loadWalkthrough(oldFile)



	while (len(listWT) > 0) :
		newFile = open("inputList2.txt", "a")
		testWordList(listWT, newFile)
		newFile.close()

		# Pull another 1000 commands
		listWT = makingInput.loadWalkthrough(oldFile)

	newFile.close()
	oldFile.close()

#####################################end one Word Test ############################################

###################################################################################################
# Main Menu
# Just a q&d menu to see if you want to check 1 word, 2 words... up to ?? words
###################################################################################################
#print("(1) Check first words")
#print("(2) Check first and second words")

#try:
#	selection = int(input("Enter election to begin> "))
#	if (selection == 1)
#		load file firstWordPoss
#	if (selection == 2) :
#		load file firstWordPoss
#		load file secondWordPoss




###################################################################################################
# This program will check 1000 commands at a time. That means it will load 1000 
# commands, store them in a list, and test them on the website. The reason for 
# 1000 commands is to save on resources and also because the game is time, and 
# after a number of valid commands that don't progressive the game, the game will end.
###################################################################################################

###################################################################################################
# We are currently working on getting the first point. Per the walkthrough we need to have the
# AI do the following moves:
# 	'east',
#  	'get sparkler',
#  	'south',
#  	'west',
#  	'get jigsaw piece', # Score 1 point
#
# I think we can get buy with:
# 	'e',
#  	'get all',
#  	'w',
#  	'get all', # Score 1 point
#
# I wonder what the AI will find...
###################################################################################################

oneWordTest()

# This checks first and second word
#firstWordFile = open("inputList.txt", "r")
#secondWordFile = open("secondWordList.txt", "r")
#outputFile = open("twoWordsList.txt", "w")

#firstWord = firstWordFile.readline()
#firstWord = firstWord.strip()
#secondWord = secondWordFile.readline()
#secondWord = secondWord.strip()

#commandList = []

#command = firstWord + " " + secondWord
#print(command)

#commandList.append(command)

#while (firstWord != "") :
#	while (secondWord != "") :
#		secondWord = secondWordFile.readline()
#		secondWord = secondWord.strip()

#		command = firstWord + " " + secondWord
#		print(command)
#
#		commandList.append(command)

#	print(commandList)
#	testWordList(commandList, outputFile)

#	frequency = 2500 # Set frequency to 2500 Hertz
#	duration = 1000 # Set duration to 1000 ms = 1 second
#	winsound.Beep(frequency, duration)

#	firstWord = firstWordFile.readline()
#	firstWord = firstWord.strip()

#firstWordFile.close()
#secondWordFile.close()
#outputFile.close()

# check first + second
# keep grabbing 1000 of second word
# keep checking first + second word
# grab next 1000 first words
# grab and check all second words
# keep grabing first words and second words and checking them
# close all files
#####################################
