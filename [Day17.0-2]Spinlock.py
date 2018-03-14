ITERS = 2017
INPUT = 386


class Node:
    def __init__(self, val, next_node=None, prev_node=None, skip_backward=None, skip_forward=None):
        self.val = val
        self.next = next_node
        self.prev = prev_node
        self.skip_forward = skip_forward
        self.skip_backward = skip_backward


def insert_node(curr, val, count, skip):
    node = Node(val, curr.next, curr)
    curr.next = node
    node.next.prev = node

    if skip < count:
        node.skip_forward = curr.skip_forward
        node.skip_forward.skip_backward = node

        node.skip_backward = node.next.skip_backward
        node.skip_backward.skip_forward = node

        node.next.skip_backward = node.skip_backward.next
        node.next.skip_backward.skip_forward = node.next

        curr.skip_forward = curr.skip_forward.prev
        curr.skip_forward.skip_backward = curr

        init = curr
        x = curr.next
        while init is not x:
            if x.skip_forward.skip_backward is not x:
                print("ERROR")
            x = x.next

    return node


def skip_ahead(curr, count, skip):
    if curr.skip_forward is not None:
        return curr.skip_forward
    for _ in range(skip if skip > count else skip % count):
        curr = curr.next
    return curr


def init_spinlock():
    curr = Node(0)
    curr.next = curr
    return curr


def assign_skips(curr, skip):
    init = curr
    l = [curr]
    curr = curr.next
    while init is not curr:
        l.append(curr)
        curr = curr.next

    for i in range(len(l)):
        l[i].skip_forward = l[(i + skip) % len(l)]
        l[i].skip_backward = l[(i - skip) % len(l)]

    print("ASSIGNED SKIPS.")


def insert_range(curr, num, skip):
    for i in range(1, num + 1):
        curr = skip_ahead(curr, i, skip)
        curr = insert_node(curr, i, i, skip)
        if i == skip:
            assign_skips(curr, skip)

    return curr


final = insert_range(init_spinlock(), ITERS, INPUT)

print("NODE AFTER LAST INSERT = " + str(final.next.val))



