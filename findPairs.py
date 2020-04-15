def findPairs(factorArray):

    wholeNum = 1

    radicalNum = 1

    pointer = 0

    #for x in range(len(factorArray)-1):

    while (pointer < (len(factorArray) - 1)):

        prevNum = factorArray[pointer]

        print (prevNum)

        curNum = factorArray[pointer + 1]

        print (curNum)

        if prevNum == curNum:

            wholeNum = wholeNum * curNum

            pointer += 2

        else:

            radicalNum = radicalNum * prevNum

            pointer += 1


    if pointer < len(factorArray):

        radicalNum = radicalNum * factorArray[pointer]


    print('Pointer:', pointer)

    print ('Number outside the radical: ', wholeNum)

    print ('Number under the radical: ', radicalNum)


findPairs([1, 2, 3])

findPairs([1, 2, 2, 2])

findPairs([2, 2, 3, 3])

findPairs([1, 3, 3, 7, 7, 19])