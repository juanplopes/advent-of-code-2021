import heapq

def add(G, heap, best, distance, x, y):
    if x < 0 or y < 0 or x >= len(G) or y >= len(G): return
    if distance + G[x][y] >= best[x][y]: return
    heapq.heappush(heap, (distance + G[x][y], (x, y)))

def dijkstra(G, start_node, end_node):
    best = [[float('+Inf')]*len(G) for _ in range(len(G))]
    
    heap = []
    heapq.heappush(heap, (0, start_node))
    while len(heap):
        distance, (x, y) = heapq.heappop(heap)
        if distance >= best[x][y]: continue
        if (x, y) == end_node: return distance
        best[x][y] = distance
        
        add(G, heap, best, distance, x-1, y)
        add(G, heap, best, distance, x+1, y)
        add(G, heap, best, distance, x, y-1)
        add(G, heap, best, distance, x, y+1)

G = []
while True:
    try: G.append(list(map(int, input())))
    except EOFError: break

print(dijkstra(G, (0, 0), (len(G)-1, len(G)-1)))
