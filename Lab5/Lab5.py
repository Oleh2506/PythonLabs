# Variant 2. Program to complement the given number with two digits.
# The required number has to be divisible by another specified number.

INITIAL_NUM = 22200
DIVISOR = 15
FIRST_DIGIT_POS = 1
SECOND_DIGIT_POS = 0

# code to find and output numbers satisfying given condition

for i in range(10):     # loop to find first undefined digit of the given number
    for j in range(10): # loop to find second undefined digit of the given number
        currentNum = INITIAL_NUM + i * (10 ** FIRST_DIGIT_POS) + j * (10 ** SECOND_DIGIT_POS)
        if currentNum % DIVISOR == 0:
            print('{0} mod {1} == 0'.format(currentNum, DIVISOR))