
with open("inputs/[Day9]input.txt", "r") as f:
    stream = f.read()


def process_garbage(s, pos):

    garbage_count = 0
    while pos < len(s):
        c = s[pos]

        if c == '>':
            return pos, garbage_count
        elif c == '!':
            pos += 2
        else:
            garbage_count += 1
            pos += 1

    return pos, garbage_count  # Redundant


def process_group(s, pos, depth):

    garbage_count = 0
    group_score = depth
    while pos < len(s):
        c = s[pos]

        if c == '}':
            return pos, group_score, garbage_count
        elif c == '{':
            pos, sub_score, sub_garbage = process_group(s, pos + 1, depth + 1)
            group_score += sub_score
            garbage_count += sub_garbage
        elif c == '<':
            pos, sub_garbage = process_garbage(s, pos + 1)
            garbage_count += sub_garbage

        pos += 1

    return pos, group_score, garbage_count  # Redundant


position, score, garbage = process_group(stream, 0, 0)

print("POSITION = " + str(position) + "/" + str(len(stream)))
print("SCORE = " + str(score))
print("GARBAGE CHARS = " + str(garbage))



