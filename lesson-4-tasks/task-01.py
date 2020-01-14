#
# Task 1
#

from sys import argv


def calc_salary(prod_in_hours=0, rate_per_hour=0, bonus=0):
    return prod_in_hours * rate_per_hour + bonus


if __name__ == '__main__':
    try:
        prod_in_hours, rate_per_hour, bonus = argv[1:]
        pay = calc_salary(float(prod_in_hours), float(rate_per_hour), float(bonus))
        print(f'The pay is: {pay}')
    except ValueError:
        print("Incorrect input data, end of work")
