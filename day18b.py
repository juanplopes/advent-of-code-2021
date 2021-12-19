def L(i): return i-(i&-i)//2
def R(i): return i+(i&-i)//2
def wrap(tree, i, nodes):
    if isinstance(tree, int): 
        nodes[i] = tree
        return nodes
    return wrap(tree[0], L(i), nodes) and wrap(tree[1], R(i), nodes)

def explode(tree):
    for i in range(2, 64, 4):
        if tree[i] == None and tree[L(i)] != None and tree[R(i)] != None:    
            for j in range(L(i)-1, 0, -1):
                if tree[j] != None: tree[j] += tree[L(i)]; break
            for j in range(R(i)+1, 64):
                if tree[j] != None: tree[j] += tree[R(i)]; break
            tree[i], tree[L(i)], tree[R(i)] = 0, None, None
            return True

def split(tree):
    for i in range(2, 64, 2):
        if tree[i] != None and tree[i] >= 10:
            tree[i], tree[L(i)], tree[R(i)] = None, tree[i]//2, (tree[i]+1)//2
            return True
    
def reduce(tree):
    tree = wrap(tree, 32, [None]*64)
    while explode(tree) or split(tree): pass
    return magnitude(tree, 32)

def magnitude(tree, i):
    if tree[i] != None: return tree[i]
    return 3*magnitude(tree, L(i))+2*magnitude(tree, R(i))

T = []
while True:
    try: T.append(eval(input()))
    except EOFError: break
print(max(reduce([a, b]) for a in T for b in T))