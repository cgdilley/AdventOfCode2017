import re

tubes = dict()
with open("inputs/[Day19]input.txt", "r") as f:
    row = 0
    for line in f.readlines():
        line = line[:-1]

        if "_width" not in tubes:
            tubes["_width"] = len(line)

        for col in range(len(line)):
            c = line[col]
            if c != " ":
                tubes[(col, row)] = c
                if row == 0:
                    tubes["_start"] = (col, row)
        row += 1
    tubes["_height"] = row

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


def move(pos, direction):
    x, y = pos
    return {
        UP: (x, y - 1),
        DOWN: (x, y + 1),
        LEFT: (x - 1, y),
        RIGHT: (x + 1, y)
    }[direction]


def is_in_bounds(t, pos):
    x, y = pos
    return 0 <= x < t["_width"] and 0 <= y < t["_height"]


def get_direction(t, pos, direction):
    if t[pos] != "+":
        return direction

    if direction == UP or direction == DOWN:
        return LEFT if move(pos, LEFT) in t else RIGHT
    else:
        return UP if move(pos, UP) in t else DOWN


def get_letter(t, pos):
    if re.match(r'[A-Z]', t[pos]):
        return t[pos]
    else:
        return ""


def traverse(t):
    pos = t["_start"]
    direction = DOWN
    message = ""
    count = 0

    while is_in_bounds(t, pos) and pos in t:
        direction = get_direction(t, pos, direction)
        message += get_letter(t, pos)
        pos = move(pos, direction)
        count += 1

    return message, pos, count


answer, finalPos, steps = traverse(tubes)

print("ANSWER = " + answer)
print("FINAL POS = " + str(finalPos))
print("STEPS TAKEN = " + str(steps))
