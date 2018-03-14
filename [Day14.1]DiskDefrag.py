import knothash as knot

keystring = "uugsqrei"


def generate_hex_grid(key, rows):
    return [knot.knot_hash(key + "-" + str(x)) for x in range(rows)]


def hex_to_bin(h):
    return bin(int(h, 16))[2:].zfill(len(h) * 4)


def hex_grid_to_bin_grid(g):
    return [hex_to_bin(x) for x in g]


def add_to_group(g, groups, row, col, group_num):
    if (row, col) in groups["_seen"] or \
                    row < 0 or row >= len(g) or \
                    col < 0 or col >= len(g[row]) or \
                    g[row][col] == "0":
        return

    groups[group_num].add((row, col))
    groups["_seen"].add((row, col))

    add_to_group(g, groups, row-1, col, group_num)
    add_to_group(g, groups, row+1, col, group_num)
    add_to_group(g, groups, row, col-1, group_num)
    add_to_group(g, groups, row, col+1, group_num)


def build_groups(g):
    groups = {
        "_seen": set()
    }

    curr_group = 0
    for row in range(len(g)):
        for col in range(len(g[row])):
            if (row, col) in groups["_seen"] or g[row][col] == "0":
                continue

            groups[curr_group] = set()

            add_to_group(g, groups, row, col, curr_group)

            curr_group += 1

    groups["_count"] = curr_group
    return groups


hex_grid = generate_hex_grid(keystring, 128)
bin_grid = hex_grid_to_bin_grid(hex_grid)
groupings = build_groups(bin_grid)

print("NUMBER OF GROUPS = " + str(groupings["_count"]))
