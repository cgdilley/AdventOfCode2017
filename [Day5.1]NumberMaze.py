

with open("inputs/[Day5]input.txt", "r") as f:
    maze = [int(x) for x in f.readlines()]


def read_value(m, pos):
    return m[pos]


def new_position(pos, val):
    return pos + val


def has_escaped(m, pos):
    return pos < 0 or pos >= len(m)


def after_jump(m, pos):
    m[pos] += 1 if read_value(m, pos) < 3 else -1


def navigate_maze(m):
    count = 0
    pos = 0

    while not has_escaped(m, pos):
        move = new_position(pos, read_value(m, pos))
        after_jump(m, pos)
        pos = move
        count += 1

    return count


jumps = navigate_maze(maze)

print("JUMPS: " + str(jumps))


