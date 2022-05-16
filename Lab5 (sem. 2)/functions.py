from random import *
from GeometricSequence import *
from ArithmeticSequence import *

def get_random_geometric_sequences(n: int) -> list:
    g_list = []
    i = 0
    
    while i < n:
        curr = GeometricSequence()
        curr.first_term = uniform(-5.0, 5.0)
        curr_rand = uniform(-5.0, 5.0)
        while curr_rand == 0:
            curr_rand = uniform(-5.0, 5.0)

        curr.common_ratio = curr_rand
        g_list.append(curr)
        i += 1

    return g_list

def get_random_arithmetic_sequences(n: int) -> list:
    a_list = []
    i = 0
    
    while i < n:
        curr = ArithmeticSequence()
        curr.first_term = uniform(-5.0, 5.0)
        curr.common_difference = uniform(-5.0, 5.0)
        a_list.append(curr)
        i += 1

    return a_list

def get_conditional_sum(a_list: list, g_list: list, n: int, m: int) -> float:
    max_index_g = 0
    max_index_a = 0
    i = 1
    while i < len(a_list):
        if a_list[i].get_nth_term(n) > a_list[max_index_a].get_nth_term(n):
            max_index_a = i
        i += 1
    i = 1
    while i < len(g_list):
        if g_list[i].get_nth_term(n) > g_list[max_index_g].get_nth_term(n):
            max_index_g = i
        i += 1

    if g_list[max_index_g].get_nth_term(n) > a_list[max_index_a].get_nth_term(n):
        cond_sum = g_list[max_index_g].get_sum_of_n_terms(m)
    else: 
        cond_sum = a_list[max_index_a].get_sum_of_n_terms(m)

    return cond_sum

def printDate(a_list: list, g_list: list, n: int, m: int) -> None:
    i = 0
    while i < len(a_list):
        print("AS: sum[%i] = %.1f; common difference = %.1f; term[1] = %.1f; term[%i] = %.1f\n" % 
              (m, a_list[i].get_sum_of_n_terms(m), a_list[i].common_difference, a_list[i].first_term,
               n, a_list[i].get_nth_term(n))) 
        i += 1

    i = 0
    while i < len(g_list):
        print("GS: sum[%i] = %.1f; common ratio = %.1f; term[1] = %.1f; term[%i] = %.1f\n" % 
              (m, g_list[i].get_sum_of_n_terms(m), g_list[i].common_ratio, g_list[i].first_term,
               n, g_list[i].get_nth_term(n)))
        i += 1