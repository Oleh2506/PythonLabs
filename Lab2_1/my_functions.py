import os.path

# Prints message and content of the file 
def print_file_content(file_name, message):
    print(message)
    with open(file_name, 'r') as file:
        print(file.read())

# Returns True if file contains at least one line starting with conditional character '#' and False if not
def is_source_file_conditional(file_name):
    file_is_conditional = False
    conditional_char = '#'
    if os.path.isfile(file_name):
        with open(file_name, 'r') as file:
            for current_line in file.readlines():
                if (current_line[0] == conditional_char):
                    file_is_conditional = True
                    break  
    else: 
        print('Error: can\'t open the file!')
    return file_is_conditional

# Returns the text typed by the user
def get_text():
    proceed_typing = True
    text = ''
    break_char = '\x17'
    while proceed_typing:
        current_line = input()
        if current_line.find(break_char) != -1:
            if len(current_line) != 1:
                break_pos = current_line.find(break_char)
                text += current_line[:break_pos] + '\n'
            proceed_typing = False
        else: 
            text += current_line + '\n'
    return text

# User interface for working with the source text file
def source_file_processing(file_name):
    source_file_is_conditional = False
    while not source_file_is_conditional:
        if os.path.isfile(file_name):
            print_file_content(file_name, 'Content of the source text file now:')
            mode_is_correct = False
            while not mode_is_correct:
                print('Please, choose one option (rewrite file - w | extend file - a | do nothing - n):')
                mode = input()
                if mode == 'w':
                    mode_is_correct = True
                    print('Please, enter the text of the file (enter CTRL + W to stop typing):')
                    text = get_text()
                    with open(file_name, mode) as file:
                        file.write(text)
                elif mode == 'a':
                    mode_is_correct = True
                    print('Please, enter the text to extend the existing file (enter CTRL + W to stop typing):')
                    text = get_text()
                    with open(file_name, mode) as file:
                        file.write(text)
                elif mode == 'n':
                    mode_is_correct = True
                else:
                    print('Error: entered character is not correct, enter another one.')
        else:
            print('There is no existing source file, you should type one. Enter CTRL + W to stop typing.')
            text = get_text()
            with open(file_name, 'w') as file:
                file.write(text)
        source_file_is_conditional = is_source_file_conditional(file_name)
        if not source_file_is_conditional:
            print('Source file is not conditional now. It should be changed.')

# Forms new text file based on source text file
def new_file_forming(source_file_name, new_file_name):
    conditional_char = '#'
    insert_char = '!'
    first_part = second_part = ''
    with open(source_file_name, 'r') as source_file, open(new_file_name, 'w') as new_file:
        for line in source_file.readlines():
            if line[0] == conditional_char:
                insert_line = line[1:] 
                pos = len(insert_line) // 2
                new_line = insert_line[:pos] + insert_char + insert_line[pos:]
                second_part += new_line
            else:
                first_part += line
        new_file_text = first_part + second_part
        new_file.write(new_file_text)
                

    
                    
