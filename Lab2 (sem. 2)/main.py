from my_module import *

initial_products_list = get_content()
write_to_bin(initial_file, initial_products_list)
initial_products_list = read_from_bin(initial_file)

print('\nInitial list of products:')
print_products_list(initial_products_list)

short_term_storage_products_list = get_short_term_storage_products_list(initial_products_list)
write_to_bin(short_file, short_term_storage_products_list)
short_term_storage_products_list = read_from_bin(short_file)

print('\nShort term storage products list:')
print_products_list(short_term_storage_products_list)

long_term_storage_products_list = get_long_term_storage_products_list(initial_products_list)
write_to_bin(long_file, long_term_storage_products_list)
long_term_storage_products_list = read_from_bin(long_file)

print('\nLong term storage products list:')
print_products_list(long_term_storage_products_list)

delete_expired_products(short_term_storage_products_list)
write_to_bin(short_file, short_term_storage_products_list)
print('\nShort term storage products list after deleting expired products:')
print_products_list(short_term_storage_products_list)

delete_expired_products(long_term_storage_products_list)
write_to_bin(long_file, long_term_storage_products_list)
print('\nLong term storage products list after deleting expired products:')
print_products_list(long_term_storage_products_list)
