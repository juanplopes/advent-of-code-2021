from collections import Counter
D = [1, 3, 6, 7, 6, 3, 1]
T = Counter([(int(input().split(' ')[-1]),int(input().split(' ')[-1]),0,0)])
A = [0, 0]
for i in range(42):
    T, U = Counter(), T
    for (p1, p2, s1, s2), value in U.items():
        if s1 >= 21 or s2 >= 21: A[s2 >= 21] += value
        elif i%2 == 0:
            for dice, freq in enumerate(D, 3):
                np1 = (p1+dice-1)%10+1
                T[(np1,p2,s1+np1,s2)] += freq*value
        else:
            for dice, freq in enumerate(D, 3):
                np2 = (p2+dice-1)%10+1
                T[(p1,np2,s1,s2+np2)] += freq*value

print(max(A))
