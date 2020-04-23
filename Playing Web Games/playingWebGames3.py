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

import makingInput
#moduleName = 'makingInput'
#importlib.import_module(moduleName)

# Using Chrome to access web
driver = webdriver.Chrome();

# Open the website
driver.get('http://www.web-adventures.org/cgi-bin/webfrotz?s=Jigsaw')

# def loadWalkthrough():
#	walkthrough = []
#	file = open("jigsawWalkthrough.txt", "r")
#	for line in file:
#		line = line.replace('[', '')
#		line = line.replace(']', '')
#		# The walkthrough has spaces before commands, but no spaces before comments.
#		# So I'm removing the comments
#		if (line[0] == ' '):
#			print(line)
#			input = line.strip();
#			walkthrough.append(input)
#	print(len(walkthrough))
#	file.close()
#	return walkthrough

#def createCommands():
#	allChars = [
#		'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#		'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
#		'.', ',', ' ', 
#		'0', '1', '2' , '3', '4', '5', '6', '7', '8', '9'
#		]

#	walkthrough = []

#	input = "";
#	for char1 in range(0, len(allChars)):
#		for char2 in range(0, len(allChars)):
#			for char3 in range(0, len(allChars)):
#				for char4 in range(0, len(allChars)):
#					for char5 in range(0, len(allChars)):
#						for char6 in range(0, len(allChars)):
#							for char7 in range(0, len(allChars)):
#								for char8 in range(0, len(allChars)):
#									for char9 in range(0, len(allChars)):
#										for char10 in range(0, len(allChars)):
#											for char11 in range(0, len(allChars)):
#												for char12 in range(0, len(allChars)):
#													for char13 in range(0, len(allChars)):
#														for char14 in range(0, len(allChars)):
#															for char15 in range(0, len(allChars)):
#																for char16 in range(0, len(allChars)):
#																	for char17 in range(0, len(allChars)):
#																		for char18 in range(0, len(allChars)):
#																			for char19 in range(0, len(allChars)):
#																				for char20 in range(0, len(allChars)):
#																					input =  allChars[char1] 
#																					input += allChars[char2] 
#																					input += allChars[char3] 
#																					input += allChars[char4] 
#																					input += allChars[char5] 
#																					input += allChars[char6]
#																					input += allChars[char7]
#																					input += allChars[char8]
#																					input += allChars[char9]
#																					input += allChars[char10]
#																					input += allChars[char11]
#																					input += allChars[char12]
#																					input += allChars[char13]
#																					input += allChars[char14]
#																					input += allChars[char15]
#																					input += allChars[char16]
#																					input += allChars[char17]
#																					input += allChars[char18]
#																					input += allChars[char19]
#																					input += allChars[char20]
#																					walkthrough.append(input)
##					print(input)

#	print(walkthrough)
#	print(len(walkthrough))

#	for x in range (0, len(walkthrough)):
#		# print("Test: " + str(x))
#		walkthrough[x] = walkthrough[x].strip()

#	walkthrough = list(dict.fromkeys(walkthrough))

#	return walkthrough

walkthrough = makingInput.getInputs()
tempWT = []
# print(len(walkthrough))

for y in range(0,2):
	for x in range(0, len(walkthrough)) :
	#	descrip = driver.find_element_by_tag_name('(text)')
	#	descrip = driver.findElements(By.)
	#	descrip = driver.findElement(By.id(<tr>));
	#	print(len(descrip))
	#	for e in descrip:
	#		print('0: ' + descrip[0].text)
	#		print('1: ' + descrip[1].text)

		print(str(x) + "/" + (str(len(walkthrough))) + ": test[" + walkthrough[x] + "]test")
		input_box = driver.find_element_by_name('a')
		input_box.send_keys(walkthrough[x])
		input_box.submit()
#		time.sleep(2)

		descrip = driver.find_elements_by_tag_name('td')
#		print(descrip[0].text)
#		print(descrip[1].text)

		output = descrip[1].text.splitlines()
#		print(output)
		print(str(len(output)) + " " + walkthrough[x] + ': ' + output[len(output)-1])
		if (output[len(output)-1] != "That's not a verb I recognise."):
			if (output[len(output)-1] != "You seem to want to talk to someone, but I can't see whom."):
				print("Valid input with " + walkthrough[x])
				tempWT.append(walkthrough[x])
				print(tempWT)
	#		print(len(output))
	#		print(output[4])
	#		print('2: ' + descrip[2].text)

	#	print(str(x) + "/" + (str(len(walkthrough))) + ": test[" + walkthrough[x] + "]test")
	#	input_box = driver.find_element_by_name('a')
	#	input_box.send_keys(walkthrough[x])
	#	input_box.submit()
	walkthrough = tempWT
	tempWT = []	
	print(walkthrough)

input_box = driver.find_element_by_name('a')
input_box.send_keys('score')
input_box.submit()

updateInputs(walkthrough)
