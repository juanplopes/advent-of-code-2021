from collections import Counter
C = Counter(map(int, input().split(',')))
for day in range(256):
    C = {i: C.get(i+1, 0) + C.get(0, 0) * (i in (6, 8)) for i in range(9)}
print(sum(C.values()))