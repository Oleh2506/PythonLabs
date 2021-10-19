# variant 2

# Program to find natural logarithm using mathematical series

import math

varA = float(input('Input variable \"a\" in the range (0;2]: ')) #initializing a variable, the natural logarithm of which will be calculated

# checking the correctness of input data
# inputDataIsCorrect -- boolean variable that describes the correctness of input data
if varA >= 0 and varA <= 2: 
    inputDataAreCorrect = True 
else:
    inputDataAreCorrect = False


if inputDataAreCorrect:
    CALCULATION_ACCURACY = 0.000001 # accuracy of calculation
    currentElem = varA - 1 # current element of the series
    lnA = 0 # natural log of a
    i = 0 # counter
    nextIteration = True # boolean variable for the do-while loop emulating   

    print('\nElements of the series: ')

    # finding the natural logarithm value
    while nextIteration:
        print('{1} [{0}]'.format(i, currentElem), end = '; ') # element of the series output
        lnA += currentElem
        i += 1
        currentElem *= ((-1) * (varA - 1) * i) / (i + 1)
        if abs(currentElem) <= CALCULATION_ACCURACY: # Exit condition
            nextIteration = False

    # percent error calculation
    if varA != 1:
        percentError = abs(lnA - math.log1p(varA - 1)) / math.log1p(varA - 1) * 100;
    else:
        percentError = 0

    print('\n\nLn(a): {0}\nPercent error: {1} %\n'.format(lnA, percentError)) # result message output
else:
    print('Error: input data aren\'t correct!') # error message output