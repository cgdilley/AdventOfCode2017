
instructions = []
with open("inputs/[Day8]input.txt", "r") as f:
    for line in f.readlines():
        segs = line.strip().split(" ")

        instruction = {
            "reg": segs[0],
            "inc": segs[1] == "inc",
            "amt": int(segs[2]),
            # segs[3] = IF
            "cond": {
                "reg": segs[4],
                "op": segs[5],
                "val": int(segs[6])
            }
        }

        instructions.append(instruction)


def get_reg_val(regs, reg):
    if reg not in regs:
        regs[reg] = 0
    return regs[reg]


def test_condition(regs, cond):
    reg = get_reg_val(regs, cond["reg"])

    return {
        ">": reg > cond["val"],
        "<": reg < cond["val"],
        "==": reg == cond["val"],
        ">=": reg >= cond["val"],
        "<=": reg <= cond["val"],
        "!=": reg != cond["val"]
    }[cond["op"]]


def execute_instruction(regs, inst):
    get_reg_val(regs, inst["reg"])

    if test_condition(regs, inst["cond"]):
        regs[inst["reg"]] += inst["amt"] * (1 if inst["inc"] else -1)


def build_registers(insts):
    regs = dict()
    for inst in insts:
        execute_instruction(regs, inst)

    return regs


def get_maximum_value(regs):
    return max(regs.items(), key=lambda k: k[1])

registers = build_registers(instructions)

maxReg = get_maximum_value(registers)

print("MAXIMUM REGISTER = " + str(maxReg))
