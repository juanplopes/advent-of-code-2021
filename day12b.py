from collections import defaultdict
from functools import cache
G = defaultdict(lambda: [])

@cache
def count(src, dst, twice, force, visited = frozenset()):
    if not force and src in visited: 
        if twice and src not in ('start', 'end'):
            return count(src, dst, False, True, visited)
        else:
            return 0

    if src == dst: return 1
    if not force and 'a' <= src[0] <= 'z': 
        visited = visited.union((src,))
    return sum(count(x, dst, twice, False, visited) for x in G[src])

while True:
    try: a, b = input().split('-')
    except EOFError: break
    G[a].append(b)
    G[b].append(a)

print(count('start', 'end', True, False))