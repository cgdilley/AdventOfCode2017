
programString = "abcdefghijklmnop"
commands = []
with open("inputs/[Day16]input.txt", "r") as f:
    splits = f.read().strip().split(",")

    for split in splits:
        com = {
            "type": split[0]
        }
        if com["type"] == "x":
            com["pos1"], com["pos2"] = [int(x) for x in split[1:].split("/")]
        elif com["type"] == "p":
            com["prog1"], com["prog2"] = split[1:].split("/")
        elif com["type"] == "s":
            com["num"] = int(split[1:])
        else:
            print("SOMETHING WENT WRONG.")

        commands.append(com)


def build_dance_group(progs):
    p = {
        "str": list(progs)
    }
    assign_prog_positions(p)
    return p


def assign_prog_positions(p):
    for i in range(len(p["str"])):
        p[p["str"][i]] = i


def swap(p, pos1, pos2, prog1, prog2):
    p["str"][pos2] = prog1
    p["str"][pos1] = prog2
    p[prog1] = pos2
    p[prog2] = pos1


def exchange(p, pos1, pos2):
    prog1 = p["str"][pos1]
    prog2 = p["str"][pos2]
    swap(p, pos1, pos2, prog1, prog2)


def partner(p, prog1, prog2):
    pos1 = p[prog1]
    pos2 = p[prog2]
    swap(p, pos1, pos2, prog1, prog2)


def spin(p, num):
    p["str"] = p["str"][-num:] + p["str"][:-num]
    assign_prog_positions(p)


def execute_command(p, command):
    if command["type"] == "x":
        exchange(p, command["pos1"], command["pos2"])
    elif command["type"] == "p":
        partner(p, command["prog1"], command["prog2"])
    elif command["type"] == "s":
        spin(p, command["num"])


def execute_all_commands(p, coms):
    for c in coms:
        execute_command(p, c)


programs = build_dance_group(programString)
execute_all_commands(programs, commands)

print("FINAL ORDER = " + "".join(programs["str"]))
