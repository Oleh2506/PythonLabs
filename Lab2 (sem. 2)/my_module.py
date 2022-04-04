from typing import NamedTuple
from datetime import *
import pickle

initial_file, long_file, short_file = 'initial.txt', 'long.txt', 'short.txt'

class Product(NamedTuple):
    name: str
    manufacture_date: date
    expiration_date: date

def get_content() -> list:
    num_of_items = int(input('Please, enter the number of products in the store: '))
    products_list = []
    i = 0
    print('\nPlease, enter the list of products. Each line should contain name, date of manufacture and expiration date')
    print('(date format is DD-MM-YYYY):')
    while i < num_of_items:
        name, date_entry1, date_entry2 = input().split()
        day, month, year = map(int, date_entry1.split('-'))
        manufacture_date = date(year, month, day)
        day, month, year = map(int, date_entry2.split('-'))
        expiration_date = date(year, month, day)
        if expiration_date >= manufacture_date and manufacture_date <= date.today():
            curr_product = Product(name, manufacture_date, expiration_date)
            products_list.append(curr_product)
            i += 1
        else:
            print('Error: entered dates are impossible! Enter another line.')

    return products_list

def print_products_list(products_list: list) -> None:
    for curr_product in products_list:
        print(curr_product.name, curr_product.manufacture_date.strftime('%d-%m-%Y'), curr_product.expiration_date.strftime('%d-%m-%Y'), sep = '\t')

def delete_expired_products(products_list: list) -> None:
    i = 0

    while i < len(products_list):
        if products_list[i].expiration_date < date.today(): 
            products_list.pop(i)
        else:
            i += 1

def get_long_term_storage_products_list(products_list: list) -> list:
    long_term_storage_products_list = []
    conditional_num = 5
    for i in range(len(products_list)):
        if (products_list[i].expiration_date - products_list[i].manufacture_date).days > conditional_num:
            long_term_storage_products_list.append(products_list[i])

    return long_term_storage_products_list

def get_short_term_storage_products_list(products_list: list) -> list:
    short_term_storage_products_list = []
    conditional_num = 5

    for i in range(len(products_list)):
        if (products_list[i].expiration_date - products_list[i].manufacture_date).days < conditional_num:
            short_term_storage_products_list.append(products_list[i])

    return short_term_storage_products_list

def write_to_bin(file_name: str, products_list: list) -> None:
    pickle.dump(products_list, open(file_name, 'wb'))

def read_from_bin(file_name: str) -> list:
    products_list = pickle.load(open(file_name, 'rb'))

    return products_list
