import heapq

def dijkstra(G, start_node, end_node):
    N = len(G)
    best = [[float('+Inf')]*N*5 for _ in range(N*5)]
    heap = []

    heapq.heappush(heap, (0, start_node))
    while len(heap):
        distance, (x, y) = heapq.heappop(heap)
        if (x, y) == end_node: return distance
        for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
            if not (0 <= nx < N*5 and 0 <= ny < N*5): continue
            ndistance = distance + (G[nx%N][ny%N] + nx//N + ny//N - 1) % 9 + 1
            if ndistance >= best[nx][ny]: continue
            best[nx][ny] = ndistance
            heapq.heappush(heap, (ndistance, (nx, ny)))

G = []
while True:
    try: G.append(list(map(int, input())))
    except EOFError: break

print(dijkstra(G, (0, 0), (len(G)*5-1, len(G)*5-1)))
