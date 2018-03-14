ITERS = 50000000
INPUT = 386


def insert_node(l, curr, val):
    l.insert(curr + 1, val)
    return curr + 1


def skip_ahead(l, curr, skip):
    return curr + skip if curr + skip < len(l) else (curr + skip) % len(l)


def init_spinlock():
    return [0]


def insert_range(l, curr, num, skip):
    for i in range(1, num+1):
        curr = skip_ahead(l, curr, skip)
        curr = insert_node(l, curr, i)
        if i % 100000 == 0:
            print(i)

    return l, curr


nodes = init_spinlock()
nodes, final = insert_range(nodes, 0, ITERS, INPUT)

print("NODE AFTER LAST INSERT = " + str(nodes[1]))



