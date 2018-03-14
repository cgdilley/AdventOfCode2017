import re


discs = dict()

with open("inputs/[Day7]input.txt", "r") as f:
    for line in f.readlines():
        lineObj = dict()

        arrowSplit = line.strip().split("->")

        firstSplit = arrowSplit[0].strip().split(" ")
        lineObj["name"] = firstSplit[0]
        lineObj["weight"] = int(re.sub(r'[()]', "", firstSplit[1]).strip())

        if len(arrowSplit) > 1:
            lineObj["children"] = [x.strip() for x in arrowSplit[1].split(",")]

        discs[lineObj["name"]] = lineObj


def assign_parent(d, parent, child):
    d[child]["parent"] = parent


def assign_all_parents(d):
    for name, obj in d.items():
        if "children" in obj:
            for child in obj["children"]:
                assign_parent(d, name, child)


def find_root(d):
    for name, obj in d.items():
        if "parent" not in obj:
            return name


assign_all_parents(discs)
root = find_root(discs)

print("ROOT = " + root)





