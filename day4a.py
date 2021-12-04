N = list(map(int, input().split(',')))
O = {b: a for a, b in enumerate(N)}

best = (float('+inf'), 0)
while True:
    try: input(); 
    except EOFError: break
    
    B = [[int(s.strip()) for s in input().strip().split()] for _ in  range(5)]
    A = [[O[x] for x in line] for line in B]
    order = min(min(max(A[i][j] for i in range(5)) for j in range(5)), 
                min(max(A[j][i] for i in range(5)) for j in range(5)))
    score = N[order] * sum(B[i][j] for i in range(5) for j in range(5) if A[i][j] > order)
    best = min(best, (order, score))
print(best[1])