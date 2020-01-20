#
# Task 7
#

import json


def get_firms_dict(line):
    d = {}
    words = line.split()
    d[words[0]] = float(words[2]) - float(words[3])
    return d


with open('files/task7-input.txt') as f:
    lines = f.readlines()

firm_profits = list(map(get_firms_dict, lines))
positive_profits = [list(r.values())[0] for r in firm_profits if list(r.values())[0] > 0]
firm_profits.append({'average_profit': sum(positive_profits) / len(positive_profits)})

with open("files/task7-output.json", "w") as f:
    json.dump(firm_profits, f)
