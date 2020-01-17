#
# Task 2
#

from sys import argv
# assume that it is a list of ints
initial_list = list(map(int, argv[1:]))


def generator():
    idx = 1
    while idx < len(initial_list):
        if initial_list[idx] > initial_list[idx - 1]:
            yield initial_list[idx]
        idx += 1


result = [r for r in generator()]
print(result)
