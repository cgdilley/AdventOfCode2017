def build_spans(val):
    o = [ord(c) for c in val]
    o.extend([17, 31, 73, 47, 23])
    return o


def swap(l, p1, p2):
    t = l[p1 % len(l)]
    l[p1 % len(l)] = l[p2 % len(l)]
    l[p2 % len(l)] = t


def reverse_span(l, pos, length):

    if length >= len(l):
        return

    for i in range(int(length/2)):
        swap(l, pos + i, pos + length - i - 1)


def modify_skip(curr):
    return curr + 1


def execute_spans(s, reps):

    l = list(range(256))
    curr_skip = 0
    pos = 0

    for i in range(reps):
        for span in s:
            reverse_span(l, pos, span)

            pos += span + curr_skip

            curr_skip = modify_skip(curr_skip)

    return l


def xor_numbers(n1, n2):
    b1 = bin(n1)[2:]
    b2 = bin(n2)[2:]

    xor = ""
    for i in range(-1, -9, -1):
        c1 = abs(i) <= len(b1) and b1[i] == "1"
        c2 = abs(i) <= len(b2) and b2[i] == "1"
        xor = ("1" if (c1 or c2) and not (c1 and c2) else "0") + xor

    return int(xor, 2)


def dense_hash(l, block_size):
    d = []
    for block in range(0, len(l), block_size):
        val = l[block]
        for pos in range(1, block_size):
            val = xor_numbers(val, l[block + pos])
        d.append(val)

    return d


def dense_to_hex(d):
    h = ""
    for val in d:
        if val < 16:
            h += "0"
        h += hex(val)[2:]
    return h


def knot_hash(val):

    spans = build_spans(val)
    knotted = execute_spans(spans, 64)
    dense = dense_hash(knotted, 16)

    return dense_to_hex(dense)


