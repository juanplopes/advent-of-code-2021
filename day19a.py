import itertools, math
K = 3
R = [tuple(zip(A, B))
     for A in itertools.permutations(range(K))
     for B in itertools.product(*[(1, -1)]*K)
     if math.prod(B)*(1-2*(sum(A[i] != i for i in range(K)) == 2)) == 1]

def rotate(rot, vec):
    return tuple(vec[a]*b for a, b in rot)

def find_translation(scanner, test):
    for origin1 in test:
        for origin2 in scanner:
            translated = [tuple(a-b+c for a, b, c in zip(x, origin1, origin2)) for x in test]
            if len(set(translated).intersection(scanner)) < 12: continue
            return translated

def signature(A):
    return set(sum(abs(a-b) for a, b in zip(x, y)) for x in A for y in A if x > y)

def find_best(settled, test):
    for scanner in settled:
        if len(signature(test).intersection(signature(scanner))) < 66: continue
        for rot in R:
            rotated = [rotate(rot, x) for x in test]
            translated = find_translation(scanner, rotated)
            if translated is None: continue
            return translated

S = []
while True:
    try: input()
    except EOFError: break
    S.append([])
    while True:
        line = input()
        if line == '': break
        S[-1].append(tuple(map(int, line.split(','))))

settled = [S.pop(0)]

while len(S):
    for i in range(len(S)):
        best = find_best(settled, S[i])
        if best is None: continue
        S.pop(i)
        settled.append(best)
        break
       
print(len({x for scanner in settled for x in scanner}))



