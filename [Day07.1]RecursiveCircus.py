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


def get_weight(d, name):
    if "totalWeight" in d[name]:
        return d[name]["totalWeight"]

    weight = d[name]["weight"]
    if "children" in d[name]:
        for child in d[name]["children"]:
            weight += get_weight(d, child)
    return weight


def assign_all_parents(d):
    for name, obj in d.items():
        if "children" in obj:
            for child in obj["children"]:
                assign_parent(d, name, child)
        obj["totalWeight"] = get_weight(d, name)


def find_root(d):
    for name, obj in d.items():
        if "parent" not in obj:
            return name


def build_tree(d, root):
    node = dict(d[root])

    if "children" in d[root]:
        node["children"] = []
        for child in d[root]["children"]:
            node["children"].append(build_tree(d, child))

    return node


def find_correct_child_weight(node, parent_consensus):
    if "children" not in node:
        return node, parent_consensus

    options = set()
    consensus = -1
    for child in node["children"]:
        w = child["totalWeight"]
        consensus = w
        if w not in options:
            options.add(w)
        else:
            break

    for child in node["children"]:
        if child["totalWeight"] != consensus:
            return find_correct_child_weight(child, consensus)

    return node, node["weight"] + (parent_consensus - node["totalWeight"])


assign_all_parents(discs)

tree = build_tree(discs, find_root(discs))

badNode, newWeight = find_correct_child_weight(tree, 0)

print("BAD NODE = " + str(badNode))
print("NEW WEIGHT = " + str(newWeight))




