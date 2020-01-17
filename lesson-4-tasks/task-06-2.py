#
# Task 6.2
#

from itertools import cycle
from sys import argv


def round_lst(lst):
    for i in cycle(lst):
        yield i


if __name__ == '__main__':
    iteration = 1
    lst = argv[1:]
    for i in round_lst(lst):
        if iteration > 10:
            break
        print(i)
        iteration += 1
