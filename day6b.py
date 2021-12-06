from collections import Counter
C = Counter(list(map(int, input().split(','))))
for day in range(256):
    C = (Counter({i-1: C.get(i, 0) for i in range(1, 9)}) 
        + Counter({6: C.get(0, 0), 8: C.get(0, 0)})) 
print(sum(C.values()))