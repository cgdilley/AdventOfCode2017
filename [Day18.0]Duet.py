import re

commands = []
with open("inputs/[Day18]input.txt") as f:
    for line in f.readlines():
        splits = line.strip().split(" ")

        com = {
            "com": splits[0],
            "src": splits[1]
        }
        if len(splits) > 2:
            com["val"] = splits[2]
        commands.append(com)


def eval_ref(regs, ref):
    if re.match(r'[\-0-9]+', ref):
        return int(ref)

    if ref not in regs:
        regs[ref] = 0

    return regs[ref]


def modify_reg(regs, command, src, val):
    e_val = eval_ref(regs, val)
    s_val = eval_ref(regs, src)
    if command == "set":
        regs[src] = e_val
    elif command == "add":
        regs[src] = s_val + e_val
    elif command == "mul":
        regs[src] = s_val * e_val
    elif command == "mod":
        regs[src] = s_val % e_val


def exec_command(regs, sounds, c, pos):
    command = c[pos]

    if command["com"] == "jgz":
        if eval_ref(regs, command["src"]) != 0:
            return pos + eval_ref(regs, command["val"]), False

    elif command["com"] == "rcv":
        if eval_ref(regs, command["src"]) != 0:
            sounds.append(sounds[-1])
            return pos + 1, True
    elif command["com"] == "snd":
        sounds.append(eval_ref(regs, command["src"]))
    else:
        modify_reg(regs, command["com"], command["src"], command["val"])

    return pos + 1, False


def perform_commands(c):

    sounds = []
    regs = {}
    pos = 0
    while True:
        pos, recovered = exec_command(regs, sounds, c, pos)
        if pos < 0 or pos >= len(c) or recovered:
            break

    return sounds


music = perform_commands(commands)

print("SOUNDS = " + str(music))
print("LAST = " + str(music[-1]))
