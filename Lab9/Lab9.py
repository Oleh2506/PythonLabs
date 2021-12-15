# Variant 2.

# Returns True if entered string contains conditional characters and False if not.
def is_string_conditional(string: str):
    words_from_string = string.split()
    string_is_conditional = True
    for word in words_from_string:
        if (not word.isdigit()):
            string_is_conditional = False
            break
    return string_is_conditional

# Returns the sum of numbers from entered string if it contains digits and spaces only and -1 if not.
def find_sum(string: str):
    nums_from_string = string.split()
    sum = 0
    if is_string_conditional(string):
        for current_num in nums_from_string:
            sum += int(current_num)
    else:
        sum = -1   
    return sum

string = str(input('Enter the string that contains digits and spaces: '))
if is_string_conditional(string):
    sum = find_sum(string)
    print('\nThe sum of numbers is: {0}\n'.format(sum))
else:
    print('\nError: input string contains unconditional characters!\n')