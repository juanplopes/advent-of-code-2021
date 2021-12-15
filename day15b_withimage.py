import heapq, PIL.Image

def dijkstra(G, start_node, end_node):
    N = len(G)
    best = [[float('+Inf')]*N*5 for _ in range(N*5)]
    prev = [[None]*N*5 for _ in range(N*5)]
    heap = []

    heapq.heappush(heap, (0, start_node))
    while len(heap):
        distance, (x, y) = heapq.heappop(heap)
        if (x, y) == end_node: break
        for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
            if not (0 <= nx < N*5 and 0 <= ny < N*5): continue
            ndistance = distance + (G[nx%N][ny%N] + nx//N + ny//N - 1) % 9 + 1
            if ndistance >= best[nx][ny]: continue
            best[nx][ny] = ndistance
            prev[nx][ny] = (x, y)
            heapq.heappush(heap, (ndistance, (nx, ny)))

    img = PIL.Image.new('RGB', (N*5, N*5))
    for x in range(N*5):
        for y in range(N*5):
            img.putpixel((x, y), (0, 0, ((G[x%N][y%N] + x//N + y//N - 1) % 9)*256//9))
    while end_node != start_node:
        img.putpixel(end_node, (255, 255, 0))
        end_node = prev[end_node[0]][end_node[1]]

    img.save('day15.png')
   

G = []
while True:
    try: G.append(list(map(int, input())))
    except EOFError: break

dijkstra(G, (0, 0), (len(G)*5-1, len(G)*5-1))
