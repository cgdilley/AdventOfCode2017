code = 289326


def s_to_l(s):
    """
    Finds the layer that contains the square of the given corner square value
    :param s: The corner square value to find the layer of
    :return: The layer of the given corner square
    """
    return (s - 1) / 2


def l_to_s(l):
    """
    Finds the value whose square is the corner value of the given layer.
    :param l: The layer to find the corner square of
    :return: The corner square value
    """

    return (l * 2) + 1


def find_layer(val):
    sqrt_ceil = int(val ** 0.5) + 1
    if sqrt_ceil % 2 == 0:
        sqrt_ceil += 1
    return s_to_l(sqrt_ceil)


def find_val_in_layer(val, lay):
    size = l_to_s(lay)
    root_corner = size ** 2
    x = lay
    y = lay

    for side in range(4):
        corner = root_corner - ((size - 1) * side)
        if val >= corner:
            return {
                0: (-x + (val - corner), y),
                1: (-x, -y + (val - corner)),
                2: (-x + (val - corner), -y),
                3: (x, -y + (val - corner))
            }[side]

    return None


def manhattan_dist(coord):
    return abs(coord[0]) + abs(coord[1])

layer = find_layer(code)
pos = find_val_in_layer(code, layer)
dist = manhattan_dist(pos)

print(layer)
print(pos)
print(dist)
