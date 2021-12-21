from collections import Counter
from itertools import product

p1, p2 = int(input().split(' ')[-1]), int(input().split(' ')[-1])
S = [Counter() for turn in range(43)]
S[0][(p1,p2,0,0)] = 1

answer1, answer2 = 0, 0
for i in range(42):
    for (p1, p2, s1, s2), value in S[i].items():
        if s1 == 21: answer1 += value
        elif s2 == 21: answer2 += value
        elif i%2 == 0:
            for a, b, c in product((1,2,3), repeat=3):
                np1 = (p1+a+b+c-1)%10+1
                S[i+1][(np1,p2,min(s1+np1, 21),s2)] += value
        else:
            for a, b, c in product((1,2,3), repeat=3):
                np2 = (p2+a+b+c-1)%10+1
                S[i+1][(p1,np2,s1,min(s2+np2, 21))] += value

print(max(answer1, answer2))
