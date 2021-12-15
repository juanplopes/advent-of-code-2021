import heapq

def add(G, heap, best, distance, i, j):
    N = len(G)
    if i < 0 or j < 0 or i >= N*5 or j >= N*5: return
    cost = (G[i%N][j%N] + i//N + j//N - 1) % 9 + 1
    if distance + cost >= best[(i, j)]: return
    heapq.heappush(heap, (distance + cost, (i, j)))

def dijkstra(G, start_node, end_node):
    best = {(i, j): float('+Inf') 
            for i in range(len(G)*5) 
            for j in range(len(G)*5)}
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

print(dijkstra(G, (0, 0), (len(G)*5-1, len(G)*5-1)))
