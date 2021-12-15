import heapq

def dijkstra(G, start_node, end_node):
    best = [[float('+Inf')]*len(G) for _ in range(len(G))]
    heap = []

    heapq.heappush(heap, (0, start_node))
    while len(heap):
        distance, (x, y) = heapq.heappop(heap)
        if (x, y) == end_node: return distance
        for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
            if not (0 <= nx < len(G) and 0 <= ny < len(G)): continue
            ndistance = distance + G[nx][ny]
            if ndistance >= best[nx][ny]: continue
            best[nx][ny] = ndistance
            heapq.heappush(heap, (ndistance, (nx,ny)))

G = []
while True:
    try: G.append(list(map(int, input())))
    except EOFError: break

print(dijkstra(G, (0, 0), (len(G)-1, len(G)-1)))
