# David Romanski
# Started 04/26/2020
# pirateCoveAutomaton1
# Comments: Also known as Pirate Adventure. Just an automated walkthrough of game.

import time
import selenium
from selenium import webdriver

# Using Chrome to access web
driver = webdriver.Chrome();

# Open the website
driver.get('https://www.ifiction.org/games/playz.php?cat=44&game=39&mode=html')

def loadWalkthrough():
###################################################################################################
# This def loads a walkthrough file.
# The walkthrough has spaces before commands, but no spaces before comments.
# So I'm removing the comments
###################################################################################################
	walkthrough = []
	file = open("pirateCoveWT.txt", "r")
	for line in file:
		if (line[0] == ' '):
			input = line.strip();
			walkthrough.append(input)
	file.close()
	return walkthrough
####################################### end loadWalkthrough #######################################

def waitOnly(command, phrase, actualCommands) :
	input_box = driver.find_element_by_name('command')
	input_box.send_keys(command + '\n')
	actualCommands += 1
	descrip = driver.find_elements_by_tag_name('td')
	output = descrip[1].text.splitlines()
	print("-1: " + output[len(output) - 1])
	print("-2: " + output[len(output) - 2])
	print("-3: " + output[len(output) - 3])
	print("-4: " + output[len(output) - 4])
	while  ((output[len(output) - 2].find(phrase) == -1) 
		and (output[len(output) - 3].find(phrase) == -1)
		and (output[len(output) - 4].find(phrase) == -1)) :
		print('wait')
		input_box = driver.find_element_by_name('command')
		input_box.send_keys('wait\n')
		actualCommands += 1
		descrip = driver.find_elements_by_tag_name('td')
		output = descrip[1].text.splitlines()
		print("-1: " + output[len(output) - 1])
		print("-2: " + output[len(output) - 2])
		print("-3: " + output[len(output) - 3])
		print("-4: " + output[len(output) - 4])

def waitAndCommand(command, phrase, actualCommands) :
	input_box = driver.find_element_by_name('command')
	input_box.send_keys(command + '\n')
	actualCommands += 1
	descrip = driver.find_elements_by_tag_name('td')
	output = descrip[1].text.splitlines()
	print("-1: " + output[len(output) - 1])
	print("-2: " + output[len(output) - 2])
	print("-3: " + output[len(output) - 3])
	print("-4: " + output[len(output) - 4])
	while  ((output[len(output) - 2].find(phrase) == -1) 
		and (output[len(output) - 3].find(phrase) == -1)
		and (output[len(output) - 4].find(phrase) == -1)) :
		print('wait')
		input_box = driver.find_element_by_name('command')
		input_box.send_keys('wait\n')
		actualCommands += 1
		print(command)
		input_box = driver.find_element_by_name('command')
		input_box.send_keys(command + '\n')
		actualCommands += 1
		descrip = driver.find_elements_by_tag_name('td')
		output = descrip[1].text.splitlines()
		print("-1: " + output[len(output) - 1])
		print("-2: " + output[len(output) - 2])
		print("-3: " + output[len(output) - 3])
		print("-4: " + output[len(output) - 4])

walkthrough = loadWalkthrough()
totalCommands = len(walkthrough)
print(totalCommands)

actualCommands = 0

for x in range(0, len(walkthrough)) :
	if (walkthrough[x] == "Give Rum") :
		print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])
		waitOnly(walkthrough[x],"Pirate grabs rum", actualCommands)

	elif (walkthrough[x] == "Throw Fish") :
		print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])
		waitOnly(walkthrough[x], "Crocs eat fish", actualCommands)

	elif (walkthrough[x] == "Watch Tide") :
		print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])
		input_box = driver.find_element_by_name('command')
		input_box.send_keys(walkthrough[x] + '\n')
		actualCommands += 1
		descrip = driver.find_elements_by_tag_name('td')
		output = descrip[1].text.splitlines()
		print("-1: " + output[len(output) - 1])
		print("-2: " + output[len(output) - 2])
		print("-3: " + output[len(output) - 3])
		print("-4: " + output[len(output) - 4])
		while  (((output[len(output) - 2].find("tide is out") == -1) 
			and  (output[len(output) - 3].find("tide is out") == -1)
			and  (output[len(output) - 4].find("tide is out") == -1))
			or ((output[len(output) -2].find("Tides be a changing matey") != -1)
			or  (output[len(output) -3].find("Tides be a changing matey") != -1))) :
			print('wait')
			input_box = driver.find_element_by_name('command')
			input_box.send_keys('wait\n')
			actualCommands += 1
			print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])
			input_box = driver.find_element_by_name('command')
			input_box.send_keys(walkthrough[x] + '\n')
			actualCommands += 1
			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print("-1: " + output[len(output) - 1])
			print("-2: " + output[len(output) - 2])
			print("-3: " + output[len(output) - 3])
			print("-4: " + output[len(output) - 4])

	elif (walkthrough[x] == "Go Lagoon") :
		print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])
		input_box = driver.find_element_by_name('command')
		input_box.send_keys(walkthrough[x] + '\n')
		actualCommands += 1
		descrip = driver.find_elements_by_tag_name('td')
		output = descrip[1].text.splitlines()
		print("-1: " + output[len(output) - 1])
		print("-2: " + output[len(output) - 2])
		print("-3: " + output[len(output) - 3])
		print("-4: " + output[len(output) - 4])
		if    ((output[len(output) - 2].find("Tides be a changing matey") != -1)
			or (output[len(output) - 3].find("Tides be a changing matey") != -1)
			or (output[len(output) - 4].find("Tides be a changing matey") != -1)) :
			input_box = driver.find_element_by_name('command')
			input_box.send_keys('S\n')
			actualCommands += 1
			print('S')
			# Reset x back to 'Watch Tide'
			x -= 1
			print("watch tide test: " + walkthrough[x])

	elif (walkthrough[x] == "Dig Anchor") :
		print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])
		input_box = driver.find_element_by_name('command')
		input_box.send_keys(walkthrough[x] + '\n')
		actualCommands += 1
		descrip = driver.find_elements_by_tag_name('td')
		output = descrip[1].text.splitlines()
		print("-1: " + output[len(output) - 1])
		print("-2: " + output[len(output) - 2])
		print("-3: " + output[len(output) - 3])
		print("-4: " + output[len(output) - 4])
		while  ((output[len(output) - 2].find("Tides be a changing matey") != -1) 
			or (output[len(output) - 3].find("Tides be a changing matey") != -1)
			or (output[len(output) - 4].find("Tides be a changing matey") != -1)) :
			input_box = driver.find_element_by_name('command')
			input_box.send_keys('S\n')
			actualCommands += 1
			print('S')
			# Reset x back to 'Watch Tide'
			x -= 2
			print("dig anchor test: " + walkthrough[x])

	elif (walkthrough[x] == "Set Sail") :
		print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])
		waitAndCommand(walkthrough[x], "After a day at sea", actualCommands)

	elif (walkthrough[x] == "DIG") :
		print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])
		waitOnly(walkthrough[x], "Pirate grabs rum", actualCommands)

	elif (walkthrough[x] == "Drop Parrot") :
		print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])
		waitOnly(walkthrough[x], "Parrot attacks snakes", actualCommands)

	else :
		input_box = driver.find_element_by_name('command')
		input_box.send_keys(walkthrough[x] + '\n')
		actualCommands += 1
		print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])

print("Actual Commands used: " + str(actualCommands))
