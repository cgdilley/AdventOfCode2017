CLEAN = 0
WEAKENED = 1
INFECTED = 2
FLAGGED = 3

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

START_POS = (0, 0)
START_DIR = UP


grid = dict()
with open("inputs/[Day22]input.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]

    offset = int(len(lines)/2)

    for row in range(len(lines)):
        for col in range(len(lines)):
            grid[(col - offset, row - offset)] = INFECTED if lines[row][col] == "#" else CLEAN

# I could arrange the number values of the directions to label them in a clockwise order, then simply adding -1
# (modulo 4) would give the new direction.  But I like spelling it out in this fashion.


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


def reverse(direction):
    return {
        UP: DOWN,
        DOWN: UP,
        RIGHT: LEFT,
        LEFT: RIGHT
    }[direction]


def is_infected(state):
    return state == CLEAN or state == WEAKENED


def move(pos, direction):
    x, y = pos
    return {
        UP: (x, y - 1),
        DOWN: (x, y + 1),
        LEFT: (x - 1, y),
        RIGHT: (x + 1, y)
    }[direction]


def get_pos(g: dict, pos: tuple) -> int:
    if pos not in g:
        g[pos] = CLEAN
    return g[pos]


def set_pos(g, pos, val):
    g[pos] = val


def process_node(g: dict, pos: tuple, direction: int) -> (tuple, int, int):

    state = get_pos(g, pos)

    # Turn and update state

    if state == CLEAN:
        direction = turn_left(direction)
        state = WEAKENED

    elif state == WEAKENED:
        state = INFECTED

    elif state == INFECTED:
        direction = turn_right(direction)
        state = FLAGGED

    elif state == FLAGGED:
        direction = reverse(direction)
        state = CLEAN

    set_pos(g, pos, state)

    # Move
    pos = move(pos, direction)

    return pos, direction, state


def process_bursts(g, pos, direction, iters):

    count = 0
    for _ in range(iters):
        pos, direction, state = process_node(g, pos, direction)
        if state == INFECTED:
            count += 1

    return count


infections = process_bursts(grid, START_POS, START_DIR, 10000000)

print("INFECTIONS = " + str(infections))



