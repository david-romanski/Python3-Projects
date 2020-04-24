def createInputs(f) :
	# This is the original create inputs def but Python doesn't allow more than 20 nested for loops
	# and this algorithm requires 35 loops to accomplish every permitation of inputs. Also it requires
	# an array to hold all those possiblities, which is a real lot.
	##################################################################################################
	#								RETIRED DEFINITION												 #
	##################################################################################################
	allChars = [
		'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
		'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
		',', ' ', #'.', 
		'0', '1', '2' , '3', '4', '5', '6', '7', '8', '9'
		]

	inputArray = []
	input = "";

	for char1 in range(0, len(allChars)):
		for char2 in range(0, len(allChars)):
			for char3 in range(0, len(allChars)):
				for char4 in range(0, len(allChars)):
					for char5 in range(0, len(allChars)):
						for char6 in range(0, len(allChars)):
							for char7 in range(0, len(allChars)):
								for char8 in range(0, len(allChars)):
									for char9 in range(0, len(allChars)):
										for char10 in range(0, len(allChars)):
											for char11 in range(0, len(allChars)):
											#	for char12 in range(0, len(allChars)):
											#	for char13 in range(0, len(allChars)):
											#	for char14 in range(0, len(allChars)):
											#	for char15 in range(0, len(allChars)):
											#	for char16 in range(0, len(allChars)):
											#	for char17 in range(0, len(allChars)):
											#	for char18 in range(0, len(allChars)):
											#	for char19 in range(0, len(allChars)):
											#	for char21 in range(0, len(allChars)):
											#	for char22 in range(0, len(allChars)):
											#	for char23 in range(0, len(allChars)):
											#	for char24 in range(0, len(allChars)):
											#	for char25 in range(0, len(allChars)):
											#	for char26 in range(0, len(allChars)):
											#	for char27 in range(0, len(allChars)):
											#	for char28 in range(0, len(allChars)):
											#	for char29 in range(0, len(allChars)):
											#	for char30 in range(0, len(allChars)):
											#	for char31 in range(0, len(allChars)):
											#	for char32 in range(0, len(allChars)):
											#	for char33 in range(0, len(allChars)):
											#	for char34 in range(0, len(allChars)):
											#	for char35 in range(0, len(allChars)):
											#	for char36 in range(0, len(allChars)):
												input =  allChars[char1] 
												input += allChars[char2] 
												input += allChars[char3] 
												input += allChars[char4] 
												input += allChars[char5] 
												input += allChars[char6]
												input += allChars[char7]
												input += allChars[char8]
												input += allChars[char9]
												input += allChars[char10]
												input += allChars[char11]
												#	input += allChars[char12]
												#	input += allChars[char13]
												#	input += allChars[char14]
												#	input += allChars[char15]
												#	input += allChars[char16]
												#	input += allChars[char17]
												#	input += allChars[char18]
												#	input += allChars[char19]
												#	input += allChars[char20]
												#	input += allChars[char21]
												#	input += allChars[char22]
												#	input += allChars[char23]
												#	input += allChars[char24]
												#	input += allChars[char25]
												#	input += allChars[char26]
												#	input += allChars[char27]
												#	input += allChars[char28]
												#	input += allChars[char29]
												#	input += allChars[char30]
												#	input += allChars[char31]
												#	input += allChars[char32]
												#	input += allChars[char33]
												#	input += allChars[char34]
												#	input += allChars[char35]
												inputArray.append(input)
												print(input)
												f.write(input + '\n')


	print(inputArray)
	print(len(inputArray))

	for x in range (0, len(inputArray)):
#		print("Test: " + str(x))
		inputArray[x] = inputArray[x].strip();
		if (len(inputArray[x] > 1)) :
			del inputArray[x]

	inputArray = list(dict.fromkeys(inputArray))
	print(inputArray)
	print(len(inputArray))
	updateInputs(inputArray)
	return inputArray


###################################################################################################
# An older version of testing first word in the game.
###################################################################################################
# Test commands
# Using Chrome to access web
driver = webdriver.Chrome();

# Open the website
driver.get('http://www.web-adventures.org/cgi-bin/webfrotz?s=Jigsaw')

for x in range(0, len(listWT)) :
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
	if (output[len(output)-1] != "That's not a verb I recognise."):
		if (output[len(output)-1] != "You seem to want to talk to someone, but I can't see whom."):
			print("Valid input with " + listWT[x])
			# tempWT.append(walkthrough[x])
			# print(tempWT)
			#if command is valid save to new file
			newFile.write(listWT[x] + '\n')
		else :
			print(listWT[x] + " isn't valid.")
	else:
		print(listWT[x] + " isn't valid.")

		#	del remainingInputs[0]

	#walkthrough = tempWT + remainingInputs
	#print(walkthrough)

	#loop
########################################### end Testing def #######################################

###################################################################################################
# This def counts every second word in a given line and gives the largest word and what line #
###################################################################################################
# Counts the largest second word
separatedWT = walkthrough[0].split()
if (len(separatedWT) > 1) :
	print("The second word on line " + str(0) + " is " + separatedWT[1] + " and has " + str(len(separatedWT[1])) + " characters.")
	longestWord = 0
	longestWordCount = len(separatedWT[1])
print(walkthrough)
for x in range(1, len(walkthrough)) :
	separatedWT = walkthrough[x].split()
	if (len(separatedWT) > 1) :
		if ("." not in separatedWT[1]) :
			print("The first word on line " + str(x) + " is " + separatedWT[1] + " and has " + str(len(separatedWT[1])) + " characters.")
			if (len(separatedWT[1]) > longestWordCount) :
				longestWord = x
				longestWordCount = len(separatedWT[1])
print("The longest word is " + str(walkthrough[longestWord]) + " with " + str(longestWordCount) + " characters.")
##################################### end count second words ######################################

###################################################################################################
# This def counts every first word in a given line and gives the largest word and what line #
###################################################################################################
# Counts the largest first word
separatedWT = walkthrough[0].split()
if (len(separatedWT) > 0) :
	print("The first word on line " + str(0) + " is " + separatedWT[0] + " and has " + str(len(separatedWT[0])) + " characters.")
	longestWord = 0
	longestWordCount = len(separatedWT[0])
print(walkthrough)
for x in range(1, len(walkthrough)) :
	separatedWT = walkthrough[x].split()
	if ("." not in separatedWT[0]) :
		if (len(separatedWT) > 0) :
			print("The first word on line " + str(x) + " is " + separatedWT[0] + " and has " + str(len(separatedWT[0])) + " characters.")
			if (len(separatedWT[0]) > longestWordCount) :
				longestWord = x
				longestWordCount = len(separatedWT[0])
print("The longest word is " + str(walkthrough[longestWord]) + " with " + str(longestWordCount) + " characters.")
##################################### end count second words ######################################

###################################################################################################
# This def receives a list of input lines and an index and shows all the unique characters from
# that poistion. 
###################################################################################################
def countPositionAt(walkthrough, position) :
	charArray = []
	for x in range(0, len(walkthrough)) :
		word = walkthrough[x]
		if (len(word) > position) :
			charArray.append(word[position])
	charArray = list(dict.fromkeys(charArray))
	print(str(len(charArray)) + " unique " + str(position) + " chars: ", end="")
	print(charArray)

# Counts unique characters in each position of input string
for x in range(0, 55) :
	countPositionAt(walkthrough, x)
##################################### end countPositionAt #########################################
