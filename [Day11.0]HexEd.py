
with open("inputs/[Day11]input.txt", "r") as f:
    directions = f.read().strip().split(",")

print("INITIAL TRAVEL: " + str(len(directions)))


def build_dir_map(d):
    dir_map = dict()

    for step in d:
        if step in dir_map:
            dir_map[step] += 1
        else:
            dir_map[step] = 1

    dir_map["_size"] = get_steps_in_map(dir_map)

    return dir_map


def fuse_directions(dir_map, dir1, dir2, dir_final):
    fused = min(dir_map[dir1], dir_map[dir2])
    dir_map[dir1] -= fused
    dir_map[dir2] -= fused
    dir_map[dir_final] += fused
    dir_map["_size"] -= fused


def simplify_directions(dir_map):

    steps = get_steps_in_map(dir_map)

    while True:
        old_steps = steps

        fuse_directions(dir_map, "sw", "se", "s")
        fuse_directions(dir_map, "nw", "ne", "n")
        fuse_directions(dir_map, "n", "se", "ne")
        fuse_directions(dir_map, "n", "sw", "nw")
        fuse_directions(dir_map, "s", "nw", "sw")
        fuse_directions(dir_map, "s", "ne", "se")

        steps = get_steps_in_map(dir_map)

        if steps == old_steps:
            break


def get_steps_in_map(dir_map):
    if "_size" in dir_map:
        return dir_map["_size"]
    return sum(v for k, v in dir_map.items())


def find_path(d):

    dir_map = build_dir_map(d)
    simplify_directions(dir_map)

    return get_steps_in_map(dir_map)


travel = find_path(directions)

print("STEPS: " + str(travel))
