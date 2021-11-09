# Variant 2. Program to find and compare the areas of three triangles.

from math import sqrt

# Returns True if the number is positive and False if not
def is_positive(num):
    if num > 0:
        return True
    else:
        return False

# Returns the largest argument passed to the function
def max_num(*args):
    max = args[0]
    for temp in args:
        if temp > max:
            max = temp
    return max

# Returns True if the arguments passed to the function can be the sides of a triangle and False if not
def are_triangle_sides(side1, side2, side3):
    
    if is_positive(side1) and is_positive(side2) and is_positive(side3):
        sides_are_positive = True
    else:
        sides_are_positive = False

    if sides_are_positive and (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        return True
    else:
        return False

# Returns the area of the triangle calculated by the formula of Heron
def herons_formula(side1, side2, side3):
    sides_values_are_correct = are_triangle_sides(side1, side2, side3)
    if sides_values_are_correct:
        sper = (side1 + side2 + side3) / 2
        triangle_area = sqrt(sper * (sper - side1) * (sper - side2) * (sper - side3))
    else:
        triangle_area = 0

    return triangle_area

# Prints the numbers of triangles with largest areas and their areas in the brackets
def result_message_output(max_area, *args):
    index = 1
    for temp in args:
        if max_area == temp:
            print('The area of triangle № {0} ({1} sq. units) is the largest one.'.format(index, temp))
        index += 1

print('Please, input the sides of first triangle: ')
side11 = float(input('Side 1: '))
side12 = float(input('Side 2: '))
side13 = float(input('Side 3: '))
print('Please, input the sides of second triangle: ')
side21 = float(input('Side 1: '))
side22 = float(input('Side 2: '))
side23 = float(input('Side 3: '))
print('Please, input the sides of third triangle: ')
side31 = float(input('Side 1: '))
side32 = float(input('Side 2: '))
side33 = float(input('Side 3: '))

if are_triangle_sides(side11, side12, side13) and are_triangle_sides(side21, side22, side23) \
    and are_triangle_sides(side31, side32, side33):
    
    area1 = herons_formula(side11, side12, side13)
    area2 = herons_formula(side21, side22, side23)
    area3 = herons_formula(side31, side32, side33)
    max_area = max_num(area1, area2, area3)

    result_message_output(max_area, area1, area2, area3)
else:
    print('Error: input numbers aren\'t the sides of triangles!')
