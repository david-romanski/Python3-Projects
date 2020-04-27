# David Romanski
# Started 04/26/2020
# pirateCoveAutomaton1
# Comments: Also known as Pirate Adventure. Just an autmated walthrough of game.

import time
import selenium
from selenium import webdriver

# Using Chrome to access web
driver = webdriver.Chrome();

# Open the website
driver.get('https://www.ifiction.org/games/playz.php?cat=44&game=39&mode=html')

def loadWalkthrough():
	walkthrough = [	
	"S",
	"Get Crackers",
	"Get Sneakers",
	"Get Rum",
	"Go Stairs",
	"Get Book",
	"Go Passage",
	"E",
	"Get Torch",
	"Get Duffel",
	"Open Duffel",
	"Drop Duffel",
	"Get Matches",
	"W",
	"W",
	"Read Book",
	"Go Window",
	"Say Yoho",
	"Drop Sneakers",
	"Drop Book",
	"E",
	"Go Shack",
	"Give Rum",
	"W",
	"E",
	"Go Path",
	"Go Crack",
	"Light Torch",
	"Go Shed",
	"Get Hammer",
	"Get Wings",
	"N",
	"Go Crack",
	"Unlight Torch",
	"D",
	"W",
	"W",
	"Drop Wings",
	"Drop Matches",
	"Drop Sack",
	"Drop Torch",
	"Get Book",
	"Get Sneakers",
	"Say Yoho",
	"Go Window",
	"Go Passage",
	"E",
	"Get Bottle",
	"W",
	"W",
	"D",
	"Get Nails",
	"Get Rug",
	"Drop Rug",
	"Get Keys",
	"Go Stairs",
	"Go Window",
	"Say Yoho",
	"Drop Book",
	"Drop Hammer",
	"Drop Sneakers",
	"Drop Nails",
	"Get Wings",
	"Go Lagoon",
	"N",
	"get Water",
	"Get Fish",
	"S",
	"S",
	"Drop Wings",
	"Get Torch",
	"Get Matches",
	"E",
	"E",
	"Light Torch",
	"Go Cave",
	"D",
	"Throw Fish",
	"Drop Bottle",
	"Unlock Door",
	"Go Hall",
	"E",
	"Go Shed",
	"Get Shovel",
	"N",
	"Get Lumber",
	"Get Sails",
	"W",
	"Go Pit",
	"U",
	"W",
	"Unlight Torch",
	"W",
	"W",
	"Drop Lumber",
	"Drop Sails",
	"Drop Torch",
	"Drop Matches",
	"Get Sack",
	"E",
	"Go Shack",
	"Unlock Chest",
	"Look Chest",
	"Get Plans",
	"Look Chest",
	"Get Map",
	"Get Parrot",
	"W",
	"W",
	"Drop Keys",
	"Watch Tide",
	"Go Lagoon",
	"Dig Anchor",
	"Get Anchor",
	"S",
	"Drop Anchor",
	"Build Ship",
	"Drop Plans",
	"Get Sneakers",
	"Get Book",
	"Say Yoho",
	"Go Window",
	"Go Passage",
	"E",
	"Wake Pirate",
	"W",
	"W",
	"Go Window",
	"Say Yoho",
	"Drop Book",
	"Drop Sneakers",
	"Go Ship",
	"Set Sail",
	"Go Beach",
	"DIG",
	"S",
	"E",
	"Pace 30",
	"Dig",
	"Get Box",
	"Drop Shovel",
	"Go Monstery",
	"Drop Parrot",

	#*** Treasure # 1 – Dubleons ***
	"Get Dubleons",
	"W",
	"W",
	"Wake Pirate",
	"N",
	"Go Ship",
	"Set Sail",
	"Go Beach",
	"Get Hammer",
	"Open Box",

	#*** Treasure # 2 – Stamps ***
	"Get Stamps",
	"Drop Hammer",
	"Drop Box",
	"Get Book",
	"Get Sneakers",
	"Say Yoho",
	"Go Window",
	"D",
	"Drop Dubleons",
	"Drop Stamps",
	"Score"
	]
	return walkthrough

walkthrough = loadWalkthrough()
totalCommands = len(walkthrough)
print(totalCommands)

time.sleep(3)
for x in range(0, len(walkthrough)) :
	if (walkthrough[x] == 'pause') :
		pause = input("Check status.")
	else :

		if (walkthrough[x] == "Give Rum") :
			input_box = driver.find_element_by_name('command')
			input_box.send_keys(walkthrough[x] + '\n')
			print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])
			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print("-1: " + output[len(output) - 1])
			print("-2: " + output[len(output) - 2])
			print("-3: " + output[len(output) - 3])
			while ((output[len(output) - 2].find("Pirate grabs rum") == -1) and (output[len(output) - 3].find("Pirate grabs rum") == -1)):
				input_box = driver.find_element_by_name('command')
				input_box.send_keys('wait\n')
				print('wait')
				descrip = driver.find_elements_by_tag_name('td')
				output = descrip[1].text.splitlines()
				print("-1: " + output[len(output) - 1])
				print("-2: " + output[len(output) - 2])
				print("-3: " + output[len(output) - 3])				


		elif (walkthrough[x] == "Throw Fish") :
			input_box = driver.find_element_by_name('command')
			input_box.send_keys(walkthrough[x] + '\n')
			print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])
			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print("-1: " + output[len(output) - 1])
			print("-2: " + output[len(output) - 2])
			print("-3: " + output[len(output) - 3])
			print("-4: " + output[len(output) - 4])
			while (output[len(output) - 2].find("Crocs eat fish") == -1) :
				input_box = driver.find_element_by_name('command')
				input_box.send_keys('wait\n')
				print('wait')
				descrip = driver.find_elements_by_tag_name('td')
				output = descrip[1].text.splitlines()
				print("-1: " + output[len(output) - 1])
				print("-2: " + output[len(output) - 2])
				print("-3: " + output[len(output) - 3])				
				print("-4: " + output[len(output) - 4])				

		elif (walkthrough[x] == "Watch Tide") :
			input_box = driver.find_element_by_name('command')
			input_box.send_keys(walkthrough[x] + '\n')
			print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])
			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print("-1: " + output[len(output) - 1])
			print("-2: " + output[len(output) - 2])
			print("-3: " + output[len(output) - 3])
			print("-4: " + output[len(output) - 4])
			while ((output[len(output) - 2].find("tide is out") == -1) 
				and (output[len(output) - 3].find("tide is out") == -1)
				and (output[len(output) - 4].find("tide is out") == -1)) :
				input_box = driver.find_element_by_name('command')
				input_box.send_keys('wait\n')
				print('wait')
				input_box = driver.find_element_by_name('command')
				input_box.send_keys(walkthrough[x] + '\n')
				print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])
				descrip = driver.find_elements_by_tag_name('td')
				output = descrip[1].text.splitlines()
				print("-1: " + output[len(output) - 1])
				print("-2: " + output[len(output) - 2])
				print("-3: " + output[len(output) - 3])
				print("-4: " + output[len(output) - 4])

		elif (walkthrough[x] == "Set Sail") :
			input_box = driver.find_element_by_name('command')
			input_box.send_keys(walkthrough[x] + '\n')
			print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])
			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print("-1: " + output[len(output) - 1])
			print("-2: " + output[len(output) - 2])
			print("-3: " + output[len(output) - 3])
			print("-4: " + output[len(output) - 4])
			while ((output[len(output) -3].find("After a day at sea") == -1) and (output[len(output) -4].find("After a day at sea") == -1)) :
				input_box = driver.find_element_by_name('command')
				input_box.send_keys('wait\n')
				print('wait')
				input_box = driver.find_element_by_name('command')
				input_box.send_keys(walkthrough[x] + '\n')
				print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])
				descrip = driver.find_elements_by_tag_name('td')
				output = descrip[1].text.splitlines()
				print("-1: " + output[len(output) - 1])
				print("-2: " + output[len(output) - 2])
				print("-3: " + output[len(output) - 3])
				print("-4: " + output[len(output) - 4])

		elif (walkthrough[x] == "DIG") :
			input_box = driver.find_element_by_name('command')
			input_box.send_keys(walkthrough[x] + '\n')
			print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])
			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print("-1: " + output[len(output) - 1])
			print("-2: " + output[len(output) - 2])
			print("-3: " + output[len(output) - 3])
			print("-4: " + output[len(output) - 4])
			while ((output[len(output) -2].find("Pirate grabs rum") == -1) and (output[len(output) -3].find("Pirate grabs rum") == -1)) :
				input_box = driver.find_element_by_name('command')
				input_box.send_keys('wait\n')
				print('wait')
				descrip = driver.find_elements_by_tag_name('td')
				output = descrip[1].text.splitlines()
				print("-1: " + output[len(output) - 1])
				print("-2: " + output[len(output) - 2])
				print("-3: " + output[len(output) - 3])
				print("-4: " + output[len(output) - 4])

		elif (walkthrough[x] == "Drop Parrot") :
			input_box = driver.find_element_by_name('command')
			input_box.send_keys(walkthrough[x] + '\n')
			print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])
			descrip = driver.find_elements_by_tag_name('td')
			output = descrip[1].text.splitlines()
			print("-1: " + output[len(output) - 1])
			print("-2: " + output[len(output) - 2])
			print("-3: " + output[len(output) - 3])
			print("-4: " + output[len(output) - 4])
			while ((output[len(output) -2].find("Parrot attacks snakes") == -1) and (output[len(output) -3].find("Parrot attacks snakes") == -1)):
				input_box = driver.find_element_by_name('command')
				input_box.send_keys('wait\n')
				print('wait')
				descrip = driver.find_elements_by_tag_name('td')
				output = descrip[1].text.splitlines()
				print("-1: " + output[len(output) - 1])
				print("-2: " + output[len(output) - 2])
				print("-3: " + output[len(output) - 3])
				print("-4: " + output[len(output) - 4])

		else :
			input_box = driver.find_element_by_name('command')
			input_box.send_keys(walkthrough[x] + '\n')
			print(str(x) + '/' + str(totalCommands) + ": " + walkthrough[x])
			time.sleep(1)
