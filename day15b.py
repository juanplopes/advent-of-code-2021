import heapq

def add(G, heap, best, distance, x, y):
    N = len(G)
    if x < 0 or y < 0 or x >= N*5 or y >= N*5: return
    cost = (G[x%N][y%N] + x//N + y//N - 1) % 9 + 1
    if distance + cost >= best[x][y]: return
    heapq.heappush(heap, (distance + cost, (x, y)))

def dijkstra(G, start_node, end_node):
    best = [[float('+Inf')]*len(G)*5 for _ in range(len(G)*5)]
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

print(dijkstra(G, (0, 0), (len(G)*5-1, len(G)*5-1)))
