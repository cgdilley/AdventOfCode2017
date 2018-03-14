GEN_A_FACTOR = 16807
GEN_B_FACTOR = 48271
DIVISOR = 2147483647

GEN_A_START = 116
GEN_B_START = 299

GEN_A_FILTER_FACTOR = 4
GEN_B_FILTER_FACTOR = 8


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


# Also considered just checking the trailing bits of the binary value to see if its divisible by 4 or 8, but
# decided on this more general solution (which avoids needing to generate the binary for all values, so may
# still just be quicker)
def is_divisible_by(val, factor):
    return val % factor == 0


def count_matches(iters):

    a = GEN_A_START
    b = GEN_B_START

    a_queue = []
    b_queue = []

    while True:
        a, b = calc_next_vals(a, b)

        if is_divisible_by(a, GEN_A_FILTER_FACTOR):
            a_queue.append(int_to_bin(a))
        if is_divisible_by(b, GEN_B_FILTER_FACTOR):
            b_queue.append(int_to_bin(b))

        if len(a_queue) >= iters and len(b_queue) >= iters:
            break

    count = 0
    for i in range(iters):
        if judge_vals(a_queue[i], b_queue[i], 16):
            count += 1

    return count


matches = count_matches(5000000)

print("MATCHES = " + str(matches))
