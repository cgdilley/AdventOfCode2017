
with open("inputs/[Day9]input.txt", "r") as f:
    stream = f.read()


def process_garbage(s, pos):

    while pos < len(s):
        c = s[pos]

        if c == '>':
            return pos
        elif c == '!':
            pos += 2
        else:
            pos += 1

    return pos  # Redundant


def process_group(s, pos, depth):

    group_score = depth
    while pos < len(s):
        c = s[pos]

        if c == '}':
            return pos, group_score
        elif c == '{':
            pos, sub_score = process_group(s, pos + 1, depth + 1)
            group_score += sub_score
        elif c == '<':
            pos = process_garbage(s, pos)

        pos += 1

    return pos, group_score  # Redundant


position, score = process_group(stream, 0, 0)

print("POSITION = " + str(position) + "/" + str(len(stream)))
print("SCORE = " + str(score))



