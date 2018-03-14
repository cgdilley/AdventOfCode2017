def generate_orientations(chunk):
    return [
        chunk,
        chunk[::-1],  # Flip (vertical)
        ["".join([chunk[y][x] for y in reversed(range(len(chunk)))]) for x in range(len(chunk))],  # Rotate 90°
        [x[::-1] for x in chunk[::-1]],  # Rotate 180°
        ["".join([chunk[y][x] for y in range(len(chunk))]) for x in reversed(range(len(chunk)))],  # Rotate 270°
        ["".join([chunk[y][x] for y in range(len(chunk))]) for x in range(len(chunk))],  # Rotate 90° + Flip
        [x[::-1] for x in chunk],  # Rotate 180° + Flip
        ["".join([chunk[y][x] for y in reversed(range(len(chunk)))]) for x in reversed(range(len(chunk)))]
        # Rotate 270° + Flip
    ]

rules = dict()
with open("inputs/[Day21]input.txt", "r") as f:
    for line in f.readlines():
        splits = [x.strip() for x in line.strip().split("=>")]

        rule = splits[0].split("/")
        result = splits[1].split("/")

        for o in generate_orientations(rule):
            rules[tuple(o)] = result


START = [".#.", "..#", "###"]


def match_rule(r, chunk):
    chunk = tuple(chunk)
    if chunk in r:
        return r[chunk]

    print("NO PATTERN MATCH FOUND")
    return None


def print_drawing(drawing):
    print("\n".join(drawing) + "\n")


def iterate(r, drawing, iters):

    # print_drawing(drawing)

    for _ in range(iters):

        print("ITER: " + str(_ + 1))

        step = 2 if len(drawing) % 2 == 0 else 3
        size = len(drawing)

        extra_rows = 0
        for row in range(0, size, step):
            results = []
            for col in range(0, size, step):
                chunk = [drawing[row + extra_rows + x][col:col+step] for x in range(step)]
                results.append(match_rule(r, chunk))
            for i in range(step):
                drawing[row + extra_rows + i] = "".join([results[x][i] for x in range(len(results))])
            drawing.insert(row + extra_rows + step, "".join([results[x][step] for x in range(len(results))]))
            extra_rows += 1

        # print_drawing(drawing)

    return drawing

final = iterate(rules, START, 18)

totalOn = sum(sum(1 if c == "#" else 0 for c in r) for r in final)

print("PIXELS ON = " + str(totalOn))
