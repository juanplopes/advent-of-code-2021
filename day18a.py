def wrap(tree, a, b, nodes):
    if isinstance(tree, int): 
        nodes[(a+b)//2] = tree
    else: 
        wrap(tree[0], a, (a+b)//2, nodes) and wrap(tree[1], (a+b)//2, b, nodes)
    return nodes

def unwrap(tree, a=0, b=64):
    if tree[(a+b)//2] != None: return tree[(a+b)//2]
    return [unwrap(tree, a, (a+b)//2), unwrap(tree, (a+b)//2, b)]

def explode(tree):
    for i in range(2, 64, 4):
        left, right = i - (i&-i)//2, i + (i&-i)//2
        if tree[i] == None and tree[left] != None and tree[right] != None:    
            for j in range(left-1, -1, -1):
                if tree[j] != None: tree[j] += tree[left]; break
            for j in range(right+1, 64):
                if tree[j] != None: tree[j] += tree[right]; break
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

current = 0
while True:
    try: current = reduce([current, eval(input())])
    except EOFError: break

print(magnitude(current))