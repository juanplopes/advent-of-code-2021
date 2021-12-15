import heapq

def add(G, heap, best, distance, i, j):
    if i < 0 or j < 0 or i >= len(G) or j >= len(G): return
    if distance + G[i][j] >= best[(i, j)]: return
    heapq.heappush(heap, (distance + G[i][j], (i, j)))

def dijkstra(G, start_node, end_node):
    best = {(i, j): float('+Inf') 
            for i in range(len(G)) 
            for j in range(len(G))}
    
    heap = []
    heapq.heappush(heap, (0, start_node))
    while len(heap):
        distance, node = heapq.heappop(heap)
        if distance >= best[node]: continue
        if node == end_node: 
            return distance
        best[node] = distance
        
        x, y = node
        add(G, heap, best, distance, x-1, y)
        add(G, heap, best, distance, x+1, y)
        add(G, heap, best, distance, x, y-1)
        add(G, heap, best, distance, x, y+1)

G = []
while True:
    try: G.append(list(map(int, input())))
    except EOFError: break

print(dijkstra(G, (0, 0), (len(G)-1, len(G)-1)))
