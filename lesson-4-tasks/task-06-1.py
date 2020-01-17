#
# Task 6.1
#

from itertools import count
from sys import argv


def ints(start=0):
    for i in count(start=start, step=1):
        yield i


if __name__ == '__main__':
    try:
        start = int(argv[1])
        for i in ints(start=start):
            if i > 10 + start:
                break
            print(i)
    except ValueError:
        print('Incorrect input')
