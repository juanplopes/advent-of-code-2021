algorithm = input()
input()
T = []
while True:
    try: T.append(input())
    except EOFError: break

def get(i, j, d):
    if not 0 <= i < len(T) or not 0 <= j < len(T[0]): return d
    return T[i][j] == '#'

def apply(i, j, d):
    return algorithm[sum(get(i-1+k//3, j-1+k%3, d)<<(8-k) for k in range(9))]
            
for k in range(2):
    T = [[apply(i, j, k%2 if algorithm[0] == '#' else 0) 
          for j in range(-1, len(T[0])+1)] 
          for i in range(-1, len(T)+1)]

print(sum(x == '#' for line in T for x in line))
