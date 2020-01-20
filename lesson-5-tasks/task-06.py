#
# Task 6
#


def calc_total_hours(words):
    total_hours = 0
    for word in words:
        if '(л)' in word:
            total_hours += int(word[:len(word)-3])
        elif '(пр)' in word:
            total_hours += int(word[:len(word) - 4])
        elif '(лаб).' in word:
            total_hours += int(word[:len(word) - 6])
    return total_hours


subjects = {}
with open('files/task6-input.txt') as f:
    lines = f.readlines()

for line in lines:
    words = line.split()
    subjects[words[0][:len(words[0])-1]] = calc_total_hours(words)

print(subjects)
