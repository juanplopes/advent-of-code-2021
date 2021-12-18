import math
def wrap(tree):
    nodes = [None]*64
    def inner(tree, a, b):
        if isinstance(tree, int): nodes[(a+b)//2] = tree
        else: inner(tree[0], a, (a+b)//2); inner(tree[1], (a+b)//2, b)
    inner(tree, 0, 64)
    return nodes

def unwrap(tree, a=0, b=64):
    if tree[(a+b)//2] != None: return tree[(a+b)//2]
    return [unwrap(tree, a, (a+b)//2), unwrap(tree, (a+b)//2, b)]

def scan_and_set(tree, a, d, value):
    while 0 <= a < len(tree): 
        if tree[a] != None: tree[a] += value; break
        a += d

def explode(tree):
    for i in range(1, 64):
        level, left, right = int(math.log2(i&-i)), i - (i&-i)//2, i + (i&-i)//2
        if level == 1 and tree[i] == None and tree[left] != None and tree[right] != None:    
            scan_and_set(tree, left-1, -1, tree[left])
            scan_and_set(tree, right+1, +1, tree[right])
            tree[i], tree[left], tree[right] = 0, None, None
            return True

def split(tree):
    for i in range(1, 64):
        left, right = i - (i&-i)//2, i + (i&-i)//2
        if tree[i] != None and tree[i] >= 10:
            tree[i], tree[left], tree[right] = None, tree[i] // 2, (tree[i]+1) // 2
            return True
    
def reduce(tree):
    tree = wrap(tree)
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