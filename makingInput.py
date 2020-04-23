def updateInputs(walkthrough):
	f = open("inputList2.txt", "w")
	for x in range(0, len(walkthrough)-1):
		f.write(walkthrough[x] + '\n')
	f.close()

def createInputs(f):
	allChars = [
		'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
		'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
		'.', ',', ' ', 
		'0', '1', '2' , '3', '4', '5', '6', '7', '8', '9'
		]

	inputArray = []
	input = "";

	for char1 in range(0, len(allChars)):
		for char2 in range(0, len(allChars)):
#		for char3 in range(0, len(allChars)):
#		for char4 in range(0, len(allChars)):
#		for char5 in range(0, len(allChars)):
#		for char6 in range(0, len(allChars)):
#		for char7 in range(0, len(allChars)):
#		for char8 in range(0, len(allChars)):
#		for char9 in range(0, len(allChars)):
#		for char10 in range(0, len(allChars)):
#		for char11 in range(0, len(allChars)):
#		for char12 in range(0, len(allChars)):
#		for char13 in range(0, len(allChars)):
#		for char14 in range(0, len(allChars)):
#		for char15 in range(0, len(allChars)):
#		for char16 in range(0, len(allChars)):
#		for char17 in range(0, len(allChars)):
#		for char18 in range(0, len(allChars)):
#		for char19 in range(0, len(allChars)):
#		for char20 in range(0, len(allChars)):
			input =  allChars[char1] 
			input += allChars[char2] 
#			input += allChars[char3] 
#			input += allChars[char4] 
#			input += allChars[char5] 
#			input += allChars[char6]
#			input += allChars[char7]
#			input += allChars[char8]
#			input += allChars[char9]
#			input += allChars[char10]
#			input += allChars[char11]
#			input += allChars[char12]
#			input += allChars[char13]
#			input += allChars[char14]
#			input += allChars[char15]
#			input += allChars[char16]
#			input += allChars[char17]
#			input += allChars[char18]
#			input += allChars[char19]
#			input += allChars[char20]
			inputArray.append(input)
			print(input)
			f.write(input + '\n')


	print(inputArray)
	print(len(inputArray))

	for x in range (0, len(inputArray)):
#		print("Test: " + str(x))
		inputArray[x] = inputArray[x].strip();

	inputArray = list(dict.fromkeys(inputArray))
	print(inputArray)
	print(len(inputArray))
	updateInputs(inputArray)
	return inputArray

def getInputs():
	walkthrough = []
	try:
		f = open("inputList.txt", "x")
		walkthrough = createInputs(f)
		f.close()
	except FileExistsError:
		print("File Already Exists.")
		f = open("inputList.txt", "r")
		for rawLine in f:
			line = rawLine.strip();
			print(line)
			walkthrough.append(line)

	return walkthrough

