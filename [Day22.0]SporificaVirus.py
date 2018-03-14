
grid = dict()
with open("inputs/[Day22]input.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]

    offset = int(len(lines)/2)

    for row in range(len(lines)):
        for col in range(len(lines)):
            grid[(col - offset, row - offset)] = lines[row][col] == "#"

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


START_POS = (0, 0)
START_DIR = UP


def turn_left(direction):
    return {
        UP: LEFT,
        LEFT: DOWN,
        DOWN: RIGHT,
        RIGHT: UP
    }[direction]


def turn_right(direction):
    return {
        UP: RIGHT,
        RIGHT: DOWN,
        DOWN: LEFT,
        LEFT: UP
    }[direction]


def move(pos, direction):
    x, y = pos
    return {
        UP: (x, y - 1),
        DOWN: (x, y + 1),
        LEFT: (x - 1, y),
        RIGHT: (x + 1, y)
    }[direction]


def get_pos(g, pos):
    if pos not in g:
        g[pos] = False
    return g[pos]


def set_pos(g, pos, val):
    g[pos] = val


def process_node(g: dict, pos: tuple, direction: int) -> (tuple, int, bool):

    infected = get_pos(g, pos)
    # Turn
    direction = turn_right(direction) if infected else turn_left(direction)
    # Infect/cleanse
    set_pos(g, pos, not infected)
    # Move
    pos = move(pos, direction)

    return pos, direction, not infected


def process_bursts(g, pos, direction, iters):

    count = 0
    for _ in range(iters):
        pos, direction, infected = process_node(g, pos, direction)
        if infected:
            count += 1

    return count


infections = process_bursts(grid, START_POS, START_DIR, 10000)

print("INFECTIONS = " + str(infections))



