ITERS = 50000000
INPUT = 386


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


def insert_node(curr, val):
    node = Node(val, curr.next)
    curr.next = node
    return node


def skip_ahead(curr, count, skip):
    for _ in range(skip if skip > count else skip % count):
        curr = curr.next
    return curr


def init_spinlock():
    curr = Node(0)
    curr.next = curr
    return curr


def insert_range(curr, num, skip):
    for i in range(1, num+1):
        curr = skip_ahead(curr, i, skip)
        curr = insert_node(curr, i)
        if i % 100000 == 0:
            print(i)

    return curr


start = init_spinlock()
final = insert_range(start, ITERS, INPUT)

print("NODE AFTER LAST INSERT = " + str(start.next.val))



