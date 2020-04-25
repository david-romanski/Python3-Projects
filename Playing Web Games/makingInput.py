import winsound

def createListFirstWord(firstWordFile) :
	# This def will funcation as normal createInputs def but it doesn't store an array of  
	# commands. It just saves them to a file to be accessed later.
	# This is also specialized for doing the first word, and the longest word is 'stewardess,'
	# and has 11 letters.
	# I think this creates 238,572,050,220,000,000 or over 2 quadrillion possible 'words'
	allChars = [
		'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
		'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
		',', ' ', #'.', 
		'0', '1', '2' , '3', '4', '5', '6', '7', '8', '9'
		]

#	FOR TESTING PURPOSES WE ARE ONLY DOING 3 CHARATERS OR 59,319 COMBINATIONS
	for char1 in range(0, len(allChars)):
		for char2 in range(0, len(allChars)):
			for char3 in range(0, len(allChars)):
#				for char4 in range(0, len(allChars)):
#					for char5 in range(0, len(allChars)):
#						for char6 in range(0, len(allChars)):
#							for char7 in range(0, len(allChars)):
#								for char8 in range(0, len(allChars)):
#									for char9 in range(0, len(allChars)):
#										for char10 in range(0, len(allChars)):
#											for char11 in range(0, len(allChars)):
												rawInput =  allChars[char1] 
												rawInput += allChars[char2] 
												rawInput += allChars[char3] 
#												rawInput += allChars[char4] 
#												rawInput += allChars[char5] 
#												rawInput += allChars[char6]
#												rawInput += allChars[char7]
#												rawInput += allChars[char8]
#												rawInput += allChars[char9]
#												rawInput += allChars[char10]
#												rawInput += allChars[char11]
												rawInput = rawInput.strip();
												if (len(rawInput.split()) == 1) :
													print(rawInput)
													firstWordFile.write(rawInput + '\n')
												else :
													print(rawInput + " is more than one word.")
##################################end createListFirstWord##########################################

def createListSecondWord(secondWordFile) :
	# This def will funcation as normal createInputs def but it doesn't store an array of  
	# commands. It just saves them to a file to be accessed later.
	# This is also specialized for doing the second word, and the longest word is 'suffragettes'
	# and has 12 letters.
	# I think this creates 238,572,050,220,000,000 or over 2 quadrillion possible 'words'

	# THE SECOND WORD CAN'T BE GUESSED!!! GET TICKET OR GET ERT OR GET SPARKLER WILL ALL SAY THE
	# SAME THING IF THE OBJECT ISN'T IN THE ROOM, EVEN IF THE OBJECT DOESN'T EXIST.

	allChars = [
		'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
		'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
		',', ' ', #'.', 
		'0', '1', '2' , '3', '4', '5', '6', '7', '8', '9'
		]

#	FOR TESTING PURPOSES WE ARE ONLY DOING 3 CHARATERS OR 59,319 COMBINATIONS
	for char1 in range(0, len(allChars)):
		for char2 in range(0, len(allChars)):
			for char3 in range(0, len(allChars)):
#				for char4 in range(0, len(allChars)):
#					for char5 in range(0, len(allChars)):
#						for char6 in range(0, len(allChars)):
#							for char7 in range(0, len(allChars)):
#								for char8 in range(0, len(allChars)):
#									for char9 in range(0, len(allChars)):
#										for char10 in range(0, len(allChars)):
#											for char11 in range(0, len(allChars)):
												rawInput =  allChars[char1] 
												rawInput += allChars[char2] 
												rawInput += allChars[char3] 
#												rawInput += allChars[char4] 
#												rawInput += allChars[char5] 
#												rawInput += allChars[char6]
#												rawInput += allChars[char7]
#												rawInput += allChars[char8]
#												rawInput += allChars[char9]
#												rawInput += allChars[char10]
#												rawInput += allChars[char11]
												rawInput = rawInput.strip();
												if (len(rawInput.split()) == 1) :
													print(rawInput)
													secondWordFile.write(rawInput + '\n')
												else :
													print(rawInput + " is more than one word.")

def updateInputs(walkthrough):
	# This def updates the inputList to remove invalid commands.
	f = open("inputList.txt", "w")
	for x in range(0, len(walkthrough)-1):
		f.write(walkthrough[x] + '\n')
	f.close()

###################################################
# I don't think this def is used
#####################################################
def getInputs():
	walkthrough = []
	try:
		f = open("inputList.txt", "x")
		#walkthrough = createInputs(f)
		createListFirstWord(f)
		f.close()
	except FileExistsError:
		print("File Already Exists.")
		f = open("inputList.txt", "r")
		for rawLine in f:
			line = rawLine.strip();
			walkthrough.append(line)

	print(len(walkthrough))
	return walkthrough



def loadWalkthrough(f):
###################################################################################################
# This def receives a file and loads 1000 words at a time then quickly checks for duplicates.
# It doesn't open or close the file, but just keeps loading 1000 words at a time.
###################################################################################################
	listOfWords = []
	loadMax = 1000
	index = 0
	while (index < 1000) :
		newLine = f.readline().rstrip()
		# Checks if EOF
		if (newLine == "") :
			print("End of file")
			break
		else :
			listOfWords.append(newLine)
		index += 1

	# Check current list for duplicates
	listOfWords = list(dict.fromkeys(listOfWords))
	print(listOfWords)
	print(len(listOfWords))

	frequency = 2500 # Set frequency to 2500 Hertz
	duration = 1000 # Set duration to 1000 ms = 1 second
	winsound.Beep(frequency, duration)

	# pause = input("Checking values>")
	return listOfWords
########################################### end loadWalkthrough ###################################
