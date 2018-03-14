
with open("inputs/[Day10]input.txt", "r") as f:
    spans = [int(x) for x in f.read().strip().split(",")]


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


def execute_spans(s):

    l = list(range(256))
    curr_skip = 0
    pos = 0

    for span in s:
        reverse_span(l, pos, span)

        pos += span + curr_skip

        curr_skip = modify_skip(curr_skip)

    return l


knotted = execute_spans(spans)

print("FIRST TWO = " + str(knotted[:2]))
print("MULT = " + str(knotted[0] * knotted[1]))



