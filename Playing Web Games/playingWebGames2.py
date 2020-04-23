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
			print(line)
			input = line.strip();
			walkthrough.append(input)
	print(len(walkthrough))
	file.close()
	return walkthrough

# def createCommands():
#	allChars = [
#		'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
#		'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
#		'.', ',', ' ', 
#		'0', '1', '2' , '3', '4', '5', '6', '7', '8', '9']
#	walkthrough = []

#	input = "";
#	for char1 in range(0, len(allChars)):
#		for char2 in range(0, len(allChars)):
#			for char3 in range(0, len(allChars)):
#				for char4 in range(0, len(allChars)):
#					input = allChars[char1] + allChars[char2] + allChars[char3] + allChars[char4]
#					walkthrough.append(input)
#					print(input)
#	return walkthrough

walkthrough = loadWalkthrough()
# print(len(walkthrough))

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
	output = descrip[1].text.splitlines()
#		print(len(output))
#		print('2: ' + descrip[2].text)

	print(str(x) + '/' + str(len(walkthrough)) + ": test[" + walkthrough[x] + "]test")
	input_box = driver.find_element_by_name('a')
	input_box.send_keys(walkthrough[x])
	input_box.submit()
	time.sleep(1)

input_box = driver.find_element_by_name('a')
input_box.send_keys('score')
input_box.submit()
