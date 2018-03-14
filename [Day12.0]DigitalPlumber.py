
programs = dict()
with open("inputs/[Day12]input.txt", "r") as f:
    for line in f.readlines():
        splits = line.strip().split("<->")
        name = splits[0].strip()

        program = {
            "name": name,
            "pipes": [x.strip() for x in splits[1].strip().split(",")]
        }
        programs[name] = program


def assign_group(p, node, groups, num):
    groups[num].add(node)

    p[node]["group"] = num

    for pipe in p[node]["pipes"]:
        if pipe not in groups[num]:
            assign_group(p, pipe, groups, num)


def group_programs(p):

    num = 0
    groups = dict()
    for node in p:
        if "group" in node:
            continue

        groups[num] = set()
        assign_group(p, node, groups, num)

        num += 1

    return groups


g = group_programs(programs)

print("PROGRAMS IN GROUP 0: " + str(len(g[0])))



