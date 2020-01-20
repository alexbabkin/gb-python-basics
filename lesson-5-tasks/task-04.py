#
# Task 4
#


def modify_line(line):
    return line.replace('One', 'Один')\
        .replace('Two', 'Два')\
        .replace('Three', 'Три')\
        .replace('Four', 'Четыре')


with open('files/task4-input.txt') as f:
    lines = f.readlines()

new_lines = list(map(modify_line, lines))

with open('files/task4-output.txt', 'w') as f:
    f.writelines(new_lines)
