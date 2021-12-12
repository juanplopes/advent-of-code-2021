from collections import defaultdict
G = defaultdict(lambda: [])

def count(src, dst, visited):
    if src in visited: return 0
    if src == dst: return 1

    if 'a' <= src[0] <= 'z': visited.add(src)
    answer = 0
    for neighbor in G[src]:
        answer += count(neighbor, dst, visited)

    if 'a' <= src[0] <= 'z': visited.remove(src)
    return answer


while True:
    try: a, b = input().split('-')
    except EOFError: break
    G[a].append(b)
    G[b].append(a)

print(count('start', 'end', set()))