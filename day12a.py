from collections import defaultdict
from functools import cache
G = defaultdict(lambda: [])

@cache
def count(src, dst, visited = frozenset()):
    if src in visited: return 0
    if src == dst: return 1

    if 'a' <= src[0] <= 'z': visited |= {src}
    return sum(count(x, dst, visited) for x in G[src])


while True:
    try: a, b = input().split('-')
    except EOFError: break
    G[a].append(b)
    G[b].append(a)

print(count('start', 'end'))