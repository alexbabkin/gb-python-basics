#
# Task 5
#

from functools import reduce


def mult(p1, p2):
    return p1 * p2


initial_list = [num for num in range(100, 1001) if num % 2 == 0]
print(initial_list)
result = reduce(mult, initial_list)
print(result)
