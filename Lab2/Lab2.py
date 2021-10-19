#variant 2

edge1 = float(input('Input first edge of the brick: '))  # variable input; edge1 -- first edge of the brick
edge2 = float(input('Input second edge of the brick: ')) # variable input; edge2 -- second edge of the brick
edge3 = float(input('Input third edge of the brick: '))  # variable input; edge3 -- third edge of the brick
side1 = float(input('Input first side of the hole: '))   # variable input; side1 -- first side of the hole
side2 = float(input('Input second side of the hole: '))  # variable input; side2 -- second side of the hole

data_are_correct = True # initializing of boolean variable that describes the correctness of input data

if (edge1 < 0) or (edge2 < 0) or (edge3 < 0) or (side1 < 0) or (side2 < 0): # checking of input data
    print('Error: input data aren\'t correct') # error message output
    data_are_correct = False # input data aren't correct

if data_are_correct: # the main part of the program will be executed in case of successful input data verification
    if ((side1 >= edge1) and (side2 >= edge2)) or ((side1 >= edge1) and (side2 >= edge3)) \
    or ((side1 >= edge2) and (side2 >= edge3)) or ((side1 >= edge2) and (side2 >= edge1)) \
    or ((side1 >= edge3) and (side2 >= edge1)) or ((side1 >= edge3) and (side2 >= edge2)): # checking the possibility of pushing the brick through the hole
        print('The brick can be pushed through the hole') # output of the result message
    else:
        print('The brick can\'t be pushed through the hole') # output of the result message
    
    


