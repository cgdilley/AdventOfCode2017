import math

code = 289326


def calc_value(spiral, pos, dist):
    """
    Finds all existing spiral coordinates within the given distance (including diagonal) of the given
    position in the given spiral, and returns the sum of the values at those coordinates.

    :param spiral: The spiral to search
    :param pos: The coordinates in the spiral to center the search on
    :param dist: The distance to search around the given coordinate
    :return: The sum of all existing values within the given distance of the given coordinate in the given spiral.
    """
    val = 0
    for x_offset in range(-dist, dist + 1):
        for y_offset in range(-dist, dist + 1):
            x = pos[0] + x_offset
            y = pos[1] + y_offset
            if (x, y) in spiral:
                val += spiral[(x, y)]
    return val


def add_to_spiral(spiral, pos, stop):
    """
    Calculates the value for a new addition to the given spiral at the given position, and adds it to the spiral
    (in-place).  If the calculated value is greater than the given stop value, returns true; otherwise, returns false.

    :param spiral: The spiral to add to
    :param pos: The position to calculate values for and insert the value at
    :param stop: The threshold at which the spiral construction should halt
    :return:
    """
    spiral[pos] = calc_value(spiral, pos, 1)
    return spiral[pos] > stop


def build_spiral(stop):
    """
    Constructs the spiral object as a dictionary that uses (x, y) tuples as keys, with the values being the values
    that the coordinate specified by the tuple contains.  Continues building up the spiral until a value is generated
    that is greater than the given stop value.

    :param stop: The threshold at which the spiral construction should halt
    :return: A tuple containing the constructed spiral object, as well as the coordinates of the last-added value.
    """

    # Seed the initial spiral with a value of 1 at the center (0, 0)
    spiral = {(0, 0): 1}
    layer = 0

    # Repeat infinitely (until stop value is reached)
    while True:
        # Increment layer counter
        layer += 1

        # Build up right side of spiral layer
        for y in range(layer - 1, -layer, -1):
            pos = (layer, y)
            if add_to_spiral(spiral, pos, stop):
                return spiral, pos
        # Build up top side of the spiral layer
        for x in range(layer, -layer, -1):
            pos = (x, -layer)
            if add_to_spiral(spiral, pos, stop):
                return spiral, pos
        # Build up left side of the spiral layer
        for y in range(-layer, layer):
            pos = (-layer, y)
            if add_to_spiral(spiral, pos, stop):
                return spiral, pos
        # Build up bottom side of the spiral layer
        for x in range(-layer, layer + 1):
            pos = (x, layer)
            if add_to_spiral(spiral, pos, stop):
                return spiral, pos

# Construct the spiral and get the final coordinates
_spiral, _pos = build_spiral(code)

# Extract the value of the last coordinate added to the spiral
largest = _spiral[_pos]

print("STOP VALUE = " + str(largest))
print("SPIRAL:\n")


# For funsies, render the spiral


digitLength = math.log10(largest) + 2
lay = max(abs(_pos[0]), abs(_pos[1]))


def normalize(val, length):
    s = str(val)
    while len(s) < length:
        s = " " + s
    return s


for _y in range(-lay, lay + 1):
    line = ""
    for _x in range(-lay, lay + 1):
        if (_x, _y) in _spiral:
            line += normalize(_spiral[(_x, _y)], digitLength)
        else:
            line += normalize(" ", digitLength)
    print(line)
