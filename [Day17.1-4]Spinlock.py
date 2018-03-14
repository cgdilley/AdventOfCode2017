ITERS = 50000000
INPUT = 386


def get_pos(num, skip):
    pos = 0
    final = 0
    for i in range(1, num + 1):
        pos = ((pos + skip) % i + 1)
        if pos == 1:
            final = i

    return final

pos_one = get_pos(ITERS, INPUT)

print("VAL = " + str(pos_one))


