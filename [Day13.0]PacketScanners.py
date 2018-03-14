
layers = dict()
with open("inputs/[Day13]input.txt", "r") as f:
    for line in f.readlines():
        splits = line.strip().split(":")

        lay = int(splits[0].strip())
        dep = int(splits[1].strip())

        layers[lay] = dep


def get_scan_depth(l, layer, picosecond):
    if layer not in l:
        return -1

    depth = l[layer]
    steps = ((depth - 2) * 2) + 2 if depth > 2 else depth
    pos = picosecond % steps

    if pos < depth:
        return pos
    else:
        return depth - (pos - depth) - 2


def calc_security_cost(l, layer):
    return layer * l[layer]


def traverse_layers(l):

    cost = 0
    for layer in l.keys():
        scan = get_scan_depth(l, layer, layer)

        if scan == 0:
            cost += calc_security_cost(l, layer)

    return cost


travel_cost = traverse_layers(layers)

print("COST = " + str(travel_cost))

