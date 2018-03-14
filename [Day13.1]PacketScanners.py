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
    steps = (depth - 1) * 2
    pos = picosecond % steps

    if pos < depth:
        return pos
    else:
        return depth - (pos - depth) - 2


def calc_security_cost(l, layer):
    return layer * l[layer]


def traverse_layers(l):
    caught_layers = []
    delay = 0
    while True:
        caught = False
        for layer in l.keys():
            scan = get_scan_depth(l, layer, layer + delay)

            if scan == 0:
                caught_layers.append(layer)
                caught = True
                break

        if not caught:
            return caught_layers

        delay += 1


travel_attempts = traverse_layers(layers)

print("LAST ATTEMPTS = " + str(travel_attempts[-30:]))
print("DELAY = " + str(len(travel_attempts)))

