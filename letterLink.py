import random

letters =  ['a', 'b','c','d','e', 
            'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
letterMap = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


while 1:
    userWord = input('Please enter a four letter word (enter q to quit): ')

    if (userWord == 'q'):
        break

    if (len(userWord) == 4):

        letterMap[ord(userWord[0]) - 97][ord(userWord[1]) - 97] +=1
        letterMap[ord(userWord[1]) - 97][ord(userWord[2]) - 97] +=1
        letterMap[ord(userWord[2]) - 97][ord(userWord[3]) - 97] +=1

        rndLetter = random.randint(0,25)
        #rndLetter = 3
        empty = True
        nextLetter = -1
        linkValue = 0
        for i in range(len(letterMap)):
            if letterMap[rndLetter][i] != 0:
                empty = False
                if letterMap[rndLetter][i] > linkValue:
                    nextLetter = i
                    linkValue = letterMap[rndLetter][i]
        if empty:
            print('No words start with ', chr(rndLetter+97))
        else:            
            print(chr(rndLetter+97), end='')
            print(chr(nextLetter+97), end='')

            rndLetter = nextLetter
            empty = True
            nextLetter = -1
            linkValue = 0
            for i in range(len(letterMap)):
                if letterMap[rndLetter][i] != 0:
                    empty = False
                    if letterMap[rndLetter][i] > linkValue:
                        nextLetter = i
                        linkValue = letterMap[rndLetter][i]
                        #print("i: ", i)

            print(chr(nextLetter+97), end='')

            rndLetter = nextLetter
            empty = True
            nextLetter = -1
            linkValue = 0
            for i in range(len(letterMap)):
                if letterMap[rndLetter][i] != 0:
                    empty = False
                    if letterMap[rndLetter][i] > linkValue:
                        nextLetter = i
                        linkValue = letterMap[rndLetter][i]
                        #print("i: ", i)

            print(chr(nextLetter+97))
        
    else:
        print('Invalid word length!')

        #userWord = input('Please enter a four letter word (enter q to quit)')

for i in range(len(letterMap)):
    for j in range(len(letterMap[i])):
        print(letterMap[i][j], end=' ')
    print()
