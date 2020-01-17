#
# Task 7
#

from itertools import count


def fact(num):
    if num == 0:
        return 1
    return num * fact(num-1)


def gen_facts():
    for i in count(start=1):
        yield fact(i)


if __name__ == '__main__':
    iteration = 1
    for el in gen_facts():
        if iteration > 15:
            break
        print(el)
        iteration += 1
