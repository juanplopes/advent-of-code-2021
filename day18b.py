def wrap(tree, a, b, nodes):
    if isinstance(tree, int): 
        nodes[(a+b)//2] = tree
    else: 
        wrap(tree[0], a, (a+b)//2, nodes) and wrap(tree[1], (a+b)//2, b, nodes)
    return nodes

def unwrap(tree, a=0, b=64):
    if tree[(a+b)//2] != None: return tree[(a+b)//2]
    return [unwrap(tree, a, (a+b)//2), unwrap(tree, (a+b)//2, b)]

def scan_and_set(tree, indices, value):
    for i in indices:
        if tree[i] != None: tree[i] += value; break

def explode(tree):
    for i in range(2, 64, 4):
        left, right = i - (i&-i)//2, i + (i&-i)//2
        if tree[i] == None and tree[left] != None and tree[right] != None:    
            scan_and_set(tree, range(left-1, -1, -1), tree[left])
            scan_and_set(tree, range(right+1, 64), tree[right])
            tree[i], tree[left], tree[right] = 0, None, None
            return True

def split(tree):
    for i in range(2, 64, 2):
        if tree[i] != None and tree[i] >= 10:
            left, right = i - (i&-i)//2, i + (i&-i)//2
            tree[i], tree[left], tree[right] = None, tree[i] // 2, (tree[i]+1) // 2
            return True
    
def reduce(tree):
    tree = wrap(tree, 0, 64, [None]*64)
    while explode(tree) or split(tree): pass
    return unwrap(tree)

def magnitude(tree):
    if isinstance(tree, int): return tree
    return magnitude(tree[0])*3 + magnitude(tree[1])*2

T = []
while True:
    try: T.append(eval(input()))
    except EOFError: break

print(max(magnitude(reduce([a, b])) for a in T for b in T))