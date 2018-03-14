GEN_A_FACTOR = 16807
GEN_B_FACTOR = 48271
DIVISOR = 2147483647

GEN_A_START = 116
GEN_B_START = 299


def gen_val(prev, factor):
    return (prev * factor) % DIVISOR


def calc_next_vals(prev_a, prev_b):
    return gen_val(prev_a, GEN_A_FACTOR), gen_val(prev_b, GEN_B_FACTOR)


def int_to_bin(val):
    return bin(val)[2:]


def judge_vals(val_a, val_b, bits):
    if len(val_a) < bits:
        val_a.zfill(bits)
    if len(val_b) < bits:
        val_b.zfill(bits)
    return val_a[-bits:] == val_b[-bits:]


def count_matches(iters):

    a = GEN_A_START
    b = GEN_B_START

    count = 0

    for i in range(iters):
        a, b = calc_next_vals(a, b)

        if judge_vals(int_to_bin(a), int_to_bin(b), 16):
            count += 1

    return count


matches = count_matches(40000000)

print("MATCHES = " + str(matches))
