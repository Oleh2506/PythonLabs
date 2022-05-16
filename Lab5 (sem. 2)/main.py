# Variant 2

from ArithmeticSequence import *
from GeometricSequence import *
from functions import *

print("Enter n (n >= 2):")
n = int(input())
if n < 2:
    raise ValueError("n must be int >= 2")

a_len = n // 2
a_list = get_random_arithmetic_sequences(a_len)
g_len = n - (n // 2)
g_list = get_random_geometric_sequences(g_len)

print("Enter m:")
m = int(input())

printDate(a_list, g_list, n, m)

cond_sum = get_conditional_sum(a_list, g_list, n, m)
print("Conditional sum is : %.1f" % cond_sum)