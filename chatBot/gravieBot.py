import random

wordList = []
wordMap = []

## Read file

print('Please talk to gravieBot in simple sentences. (q to quit)')
line = input('>')

while line != 'q':
    
    ## PROCESS INPUT TEXT
    words = line.split() #split string into a list

    preIndex = -1
    for word in words:
        curIndex = wordList.count(word)				# Counts times a word occurs in the list
        if curIndex == 0:					# If word not found in list
             curIndex = len(wordList)				# Make current index the edge of the map
             wordList.append(word)
        else:
             curIndex = wordList.index(word)			# or make current index where the word is.
             # This needs to check for a previous word. If there is a previous word then
             if preIndex != -1:
                 wordMap[preIndex][curIndex] += 1

        found = False						# is this another way to do the same thing?
        for setWord in wordList:
            if word == setWord:
                found = True
                #wordMap[					# Idk what this did
        
        ## ADD NEW WORD TO WORDLIST AND LINK TO WORDMAP
        if not found:
#            wordList.append(word)   #append word to wordList
#            index = wordList.index(word)
#            print(wordList.index(word))
            appendArray = []
            for i in range(index+1):
                if i < index:
                    appendArray.append(0)
                else:
                    appendArray.append(0)
            wordMap.append(appendArray)

            traceBack = curIndex
            while traceBack > 0:
                traceBack -= 1
                wordMap[traceBack].append(0)

#            if preIndex != -1:
#                wordMap[preIndex][curIndex] +=1
#                print('where are we?', preIndex, ' ', curIndex)

            print("Pre: ", preIndex, " ", "Cur: ", curIndex)

            preIndex = curIndex					# Holds the column of worldMap
        
#    for word in wordList:
#        print(word)
        
    for record in wordMap:
        print (record)
        
    ## CREATE RESPONSE
    #row = random.randint(0,len(wordList)-1)
    row = 0
    #print(start)
    response = wordList[row]
    responseLength = len(response)
    #print(wordList[start])
        
    while responseLength < 144:
        nextRow = -1
        maxLinks = 0
        column = 0
        for numWordLinks in wordMap[row]:
            # print(wordList[row], ":", numWordLinks, wordList[column], ":", maxLinks)
            if numWordLinks > maxLinks:
                maxLinks = numWordLinks
                nextRow = column
            column += 1
        if maxLinks == 0:
            responseLength = 150
        else:
            response += ' ' + wordList[maxLinks]
            responseLength = len(response)
            row = nextRow
            print('row: ', row)
    print('gravieBot says: ', response)
    
    line = input('>')
    
#print('Map[1][0]', wordMap[1][0])
