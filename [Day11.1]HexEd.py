
with open("inputs/[Day11]input.txt", "r") as f:
    directions = f.read().strip().split(",")

print("INITIAL TRAVEL: " + str(len(directions)))


def build_dir_map(d):
    dir_map = {"s": 0, "n": 0, "se": 0, "ne": 0, "sw": 0, "nw": 0}

    dist_over_time = []
    dir_map["_size"] = 0
    for step in d:
        dir_map["_size"] += 1
        dir_map[step] += 1
        simplify_directions(dir_map, step)
        dist_over_time.append(get_steps_in_map(dir_map))

    return dir_map, dist_over_time


def fuse_directions(dir_map, dir1, dir2, dir_final):
    fused = min(dir_map[dir1], dir_map[dir2])

    if fused == 0:
        return False

    dir_map[dir1] -= fused
    dir_map[dir2] -= fused
    dir_map[dir_final] += fused
    dir_map["_size"] -= fused

    return True


def simplify_directions(dir_map, last_dir):

    if (last_dir == "sw" or last_dir == "se") and fuse_directions(dir_map, "sw", "se", "s"):
        return simplify_directions(dir_map, "s")
    if (last_dir == "nw" or last_dir == "ne") and fuse_directions(dir_map, "nw", "ne", "n"):
        return simplify_directions(dir_map, "n")
    if (last_dir == "n" or last_dir == "se") and fuse_directions(dir_map, "n", "se", "ne"):
        return simplify_directions(dir_map, "ne")
    if (last_dir == "n" or last_dir == "sw") and fuse_directions(dir_map, "n", "sw", "nw"):
        return simplify_directions(dir_map, "nw")
    if (last_dir == "s" or last_dir == "nw") and fuse_directions(dir_map, "s", "nw", "sw"):
        return simplify_directions(dir_map, "sw")
    if (last_dir == "s" or last_dir == "ne") and fuse_directions(dir_map, "s", "ne", "se"):
        return simplify_directions(dir_map, "se")


def get_steps_in_map(dir_map):
    if "_size" in dir_map:
        return dir_map["_size"]
    return sum(v for k, v in dir_map.items())


def find_path(d):

    dir_map, dist_over_time = build_dir_map(d)

    return dist_over_time


travel = find_path(directions)

print("STEPS: " + str(travel[-1]))
print("FURTHEST: " + str(max(travel)))

