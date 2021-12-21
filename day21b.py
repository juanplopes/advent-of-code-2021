from collections import Counter
from itertools import product

T = Counter([(int(input().split(' ')[-1]),int(input().split(' ')[-1]),0,0)])
A = [0, 0]
for i in range(42):
    T, U = Counter(), T
    for (p1, p2, s1, s2), value in U.items():
        if s1 == 21 or s2 == 21: A[s2 == 21] += value
        elif i%2 == 0:
            for a, b, c in product((1,2,3), repeat=3):
                np1 = (p1+a+b+c-1)%10+1
                T[(np1,p2,min(s1+np1, 21),s2)] += value
        else:
            for a, b, c in product((1,2,3), repeat=3):
                np2 = (p2+a+b+c-1)%10+1
                T[(p1,np2,s1,min(s2+np2, 21))] += value

print(max(A))
