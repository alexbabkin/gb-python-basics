#
# Task 3
#

from functools import reduce


def get_salaries_dict(lines):
    ps_dict = {}
    for line in lines:
        ps = line.split('\t')
        # we need to remove '\n' a the end of the line
        ps_dict[ps[0]] = float(ps[1][:len(ps[1])-1])
    return ps_dict


with open('files/task3-input.txt') as f:
    person_salary = get_salaries_dict(f.readlines())

[print(f'Оклад сотрудника {k} меньше 20 000') for k, v in person_salary.items() if v < 20.0]

salaries = person_salary.values()
average_salary = sum(salaries) / len(salaries)
print(f'Срдний оклад равен: {average_salary}')
