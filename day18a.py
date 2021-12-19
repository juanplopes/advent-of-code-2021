def L(i): return i-(i&-i)//2
def R(i): return i+(i&-i)//2
def wrap(tree, i, nodes):
    if isinstance(tree, int): 
        nodes[i] = tree
        return nodes
    return wrap(tree[0], L(i), nodes) and wrap(tree[1], R(i), nodes)

def unwrap(tree, i):
    if tree[i] != None: return tree[i]
    return [unwrap(tree, L(i)), unwrap(tree, R(i))]

def explode(tree):
    for i in range(2, 64, 4):
        if tree[L(i)] == None or tree[R(i)] == None: continue
        for j in range(L(i)-1, 0, -1):
            if tree[j] != None: tree[j] += tree[L(i)]; break
        for j in range(R(i)+1, 64):
            if tree[j] != None: tree[j] += tree[R(i)]; break
        tree[i], tree[L(i)], tree[R(i)] = 0, None, None
        return True

def split(tree):
    for i in range(2, 64, 2):
        if tree[i] == None or tree[i] < 10: continue
        tree[i], tree[L(i)], tree[R(i)] = None, tree[i]//2, (tree[i]+1)//2
        return True
    
def reduce(tree):
    tree = wrap(tree, 32, [None]*64)
    while explode(tree) or split(tree): pass
    return unwrap(tree, 32)

def magnitude(tree):
    if isinstance(tree, int): return tree
    return magnitude(tree[0])*3 + magnitude(tree[1])*2

current = 0
while True:
    try: current = reduce([current, eval(input())])
    except EOFError: break

print(magnitude(current))