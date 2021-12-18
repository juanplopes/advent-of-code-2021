from dataclasses import dataclass

@dataclass
class Node:
    value: int; prev: object; next: object

def wrap(tree):
    nodes = []
    def inner(value):
        if not isinstance(value, int): return [inner(value[0]), inner(value[1])]
        node = Node(value, None, None)
        if len(nodes):
            nodes[-1].next = node
            node.prev = nodes[-1]
        nodes.append(node)
        return node
    return inner(tree)

def unwrap(tree):
    if isinstance(tree, Node): return tree.value
    return list(unwrap(x) for x in tree)

def explode(tree, level=0):
    if level >= 4 and not isinstance(tree, Node) and all(isinstance(x, Node) for x in tree):
        left, right = tree
        newtree = Node(0, left.prev, right.next)
        if left.prev: left.prev.next = newtree; left.prev.value += left.value
        if right.next: right.next.prev = newtree; right.next.value += right.value
        return True, newtree
    if isinstance(tree, Node): return False, tree
    success, tree[0] = explode(tree[0], level+1)
    if success: return success, tree
    success, tree[1] = explode(tree[1], level+1)
    return success, tree

def split(tree):
    if isinstance(tree, Node) and tree.value >= 10:
        left = Node(tree.value//2, tree.prev, None)
        right = Node((tree.value+1)//2, left, tree.next)
        left.next = right
        if tree.prev: tree.prev.next = left
        if tree.next: tree.next.prev = right
        return True, [left, right]
    if isinstance(tree, Node): return False, tree
    success, tree[0] = split(tree[0])
    if success: return success, tree
    success, tree[1] = split(tree[1])
    return success, tree

def reduce(tree):
    tree = wrap(tree)
    while True:
        some1, tree = explode(tree)
        if some1: continue
        some2, tree = split(tree)
        if some2: continue
        return unwrap(tree)

def magnitude(tree):
    if isinstance(tree, int): return tree
    return magnitude(tree[0])*3 + magnitude(tree[1])*2

T = []
while True:
    try: T.append(eval(input()))
    except EOFError: break

print(max(magnitude(reduce([a, b])) for a in T for b in T))