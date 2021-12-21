P = [int(input().split(' ')[-1]), int(input().split(' ')[-1])]
S = [0, 0]
for i in range(10000):
    P[i%2] = ((P[i%2] - 1 + 9*i+6) % 10) + 1
    S[i%2] += P[i%2]
    if S[i%2] >= 1000:
        print(S[1-i%2] * (i*3+3))
        break
