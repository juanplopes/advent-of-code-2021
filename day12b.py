from collections import defaultdict
G = defaultdict(lambda: [])

def count(src, dst, twice, force, visited):
    if not force and src in visited: 
        return (0 if not twice or src in ('start', 'end') else count(src, dst, False, True, visited))
    if src == dst: return 1

    if not force and 'a' <= src[0] <= 'z': visited.add(src)
    answer = 0
    for neighbor in G[src]:
        answer += count(neighbor, dst, twice, False, visited)

    if not force and 'a' <= src[0] <= 'z': visited.remove(src)
    return answer

while True:
    try: a, b = input().split('-')
    except EOFError: break
    G[a].append(b)
    G[b].append(a)

print(count('start', 'end', True, False, set()))