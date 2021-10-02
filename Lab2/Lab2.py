#variant 2

edge1 = float(input('Input first edge of the brick: '))
edge2 = float(input('Input second edge of the brick: '))
edge3 = float(input('Input third edge of the brick: '))
side1 = float(input('Input first side of the hole: '))
side2 = float(input('Input second side of the hole: '))

data_is_correct = 1

if (edge1 < 0) or (edge2 < 0) or (edge3 < 0) or (side1 < 0) or (side2 < 0):
    print('Error: inputted data aren\'t correct')
    data_is_correct = 0

if data_is_correct:
    if ((side1 >= edge1) and (side2 >= edge2)) or ((side1 >= edge1) and (side2 >= edge3)) \
    or ((side1 >= edge2) and (side2 >= edge3)) or ((side1 >= edge2) and (side2 >= edge1)) \
    or ((side1 >= edge3) and (side2 >= edge1)) or ((side1 >= edge3) and (side2 >= edge2)):
        print('The brick can be pushed through the hole')
    else:
        print('The brick can\'t be pushed through the hole')
    
    


