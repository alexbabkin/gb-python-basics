#
# Task 4
#

from sys import argv
# assume that it is a list of ints
initial_list = list(map(int, argv[1:]))
result = [num for num in initial_list if initial_list.count(num) == 1]
print(result)
