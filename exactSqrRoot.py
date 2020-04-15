def findFactors(number):
    factors = [1]
    possFactor = 2
    while (possFactor <= (number/2)):
        if ((number % possFactor) == 0):
            number = number / possFactor
            factors.append(possFactor)
            possFactor = 2
        else:
            possFactor += 1
    factors.append(int(number))
    return factors

def findPairs(factorArray):
    wholeNum = 1
    radicalNum = 1
    pointer = 0
    while (pointer < (len(factorArray) - 1)):
        prevNum = factorArray[pointer]
        curNum = factorArray[pointer + 1]
        if prevNum == curNum:
            wholeNum = wholeNum * curNum
            pointer += 2
        else:
            radicalNum = radicalNum * prevNum
            pointer += 1

    if pointer < len(factorArray):
        radicalNum = radicalNum * factorArray[pointer]

    print ('Answer:', end = " ")
    if wholeNum != 1:
        print(wholeNum, end = " ")
    if radicalNum != 1:
        print ('v', radicalNum)

number = input('Please enter the number under the radical: ')
factorArray = findFactors(int(number))
findPairs(factorArray)
