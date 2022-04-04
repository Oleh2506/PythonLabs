# Variant 2

import my_functions

source_file_name = 'source_text.txt'
new_file_name = 'new_text.txt'
my_functions.source_file_processing(source_file_name)
my_functions.new_file_forming(source_file_name, new_file_name)
my_functions.print_file_content(source_file_name, '\nSource file:')
my_functions.print_file_content(new_file_name, 'New file:')
