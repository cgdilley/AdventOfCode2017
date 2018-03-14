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


def add_config(configs, b):
    d = configs
    config_is_new = False
    for val in b:
        if val not in d:
            d[val] = dict()
            config_is_new = True
        d = d[val]

    return config_is_new


def repeat_redistribution(b):
    configs = dict()
    count = 0
    while add_config(configs, b):
        count += 1
        pos = get_bank_to_distribute(b)
        distribute_bank(b, pos)

    return count


redists = repeat_redistribution(banks)

print("REDISTRIBUTIONS: " + str(redists))



