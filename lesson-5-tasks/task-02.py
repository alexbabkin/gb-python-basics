#
# Task 2
#

with open('files/task2-input.txt') as f:
    lines = f.readlines()

print(len(lines))
print(list(map(lambda l: len(l.split()), lines)))
