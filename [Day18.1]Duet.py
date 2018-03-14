import re
import queue

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
    if re.match(r'[\-0-9]+', str(ref)):
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


def exec_command(p, send, c, pos):
    command = c[pos]
    regs = p["regs"]

    if command["com"] == "jgz":
        if eval_ref(regs, command["src"]) > 0:
            return pos + eval_ref(regs, command["val"]), False

    elif command["com"] == "rcv":
        if p["queue"].empty():
            return pos, True
        else:
            modify_reg(regs, "set", command["src"], p["queue"].get())
    elif command["com"] == "snd":
        send.put(eval_ref(regs, command["src"]))
        p["sent"] += 1
    else:
        modify_reg(regs, command["com"], command["src"], command["val"])

    return pos + 1, False


def build_program(num):
    return {
        "regs": {
            "p": num
        },
        "pos": 0,
        "queue": queue.Queue(),
        "sent": 0
    }


def perform_commands(c):

    p0 = build_program(0)
    p1 = build_program(1)
    
    while True:
        p0["pos"], locked1 = exec_command(p0, p1["queue"], c, p0["pos"])
        p1["pos"], locked2 = exec_command(p1, p0["queue"], c, p1["pos"])

        if not (0 <= p0["pos"] < len(c)) or not (0 <= p1["pos"] < len(c)) or (locked1 and locked2):
            break

    return p0, p1


program0, program1 = perform_commands(commands)

print("SENT VALUES = " + str(program1["sent"]))
