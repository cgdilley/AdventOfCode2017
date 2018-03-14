import numpy as np


with open("inputs/[Day6]input.txt", "r") as f:
    banks = [int(x) for x in f.read().strip().split("\t")]


def get_bank_to_distribute(b):
    return np.argmax(b)


def distribute_bank(b, pos):
    val = b[pos]
    b[pos] = 0
    for i in range(pos + 1, pos + 1 + val):
        b[i % len(b)] += 1


def add_config(configs, b, count):
    d = configs
    for i in range(len(b) - 1):
        val = b[i]

        if val not in d:
            d[val] = dict()
        d = d[val]

    if b[-1] in d:
        return count - d[b[-1]]
    else:
        d[b[-1]] = count
        return -1


def repeat_redistribution(b):
    configs = dict()
    count = 0
    while True:
        since_seen = add_config(configs, b, count)
        if since_seen >= 0:
            return count, since_seen

        count += 1
        pos = get_bank_to_distribute(b)
        distribute_bank(b, pos)


redists, cycle = repeat_redistribution(banks)

print("REDISTRIBUTIONS: " + str(redists))
print("CYCLE LENGTH: " + str(cycle))



