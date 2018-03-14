import knothash as knot

keystring = "uugsqrei"


def generate_hex_grid(key, rows):
    return [knot.knot_hash(key + "-" + str(x)) for x in range(rows)]


def hex_to_bin(h):
    return bin(int(h, 16))[2:].zfill(len(h) * 4)


def hex_grid_to_bin_grid(g):
    return [hex_to_bin(x) for x in g]


def count_ones(bin_string):
    return bin_string.count("1")


def count_ones_in_grid(g):
    count = 0
    for row in g:
        count += count_ones(row)

    return count


hex_grid = generate_hex_grid(keystring, 128)
bin_grid = hex_grid_to_bin_grid(hex_grid)
ones_count = count_ones_in_grid(bin_grid)

print("ONES = " + str(ones_count))
