def findFactor(number):

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



factors = findFactor(2)

# printing the list using loop

for x in range(len(factors)):
 
    print (factors[x], )


factors = findFactor(210)
# printing the list using loop
for x in range(len(factors)):
 
    print (factors[x], )

factors = findFactor(2310)
# printing the list using loop

for x in range(len(factors)):
 
    print (factors[x], )