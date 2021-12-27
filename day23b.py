from collections import deque
input(); input()

B = [[sum(1 << j for j in range(a, b))+sum(1 << j for j in range(b+1, a+1)) 
        for b in range(20)] 
        for a in range(20)]

states = []
stacks = [deque() for _ in range(4)]
best = [10000000000]
out = [0]
visited = {}
IN, OUT, IN2 = 0, 1, 2

def backtrack(cost, level=0):
    frozen = tuple(states)
    if visited.get(frozen, float('+inf')) <= cost: return
    visited[frozen] = cost

    if cost >= best[0]: return
    if all(a == b and s in (IN, IN2) for a, s, b, _ in states):
        best[0] = cost
        return

    for i, (a, s, b, q) in enumerate(states):
        if level < 2: print(' ' * level, i, best, len(visited))
        if s == IN and stacks[b][-1] == i and any(states[x][0] != states[x][2] for x in stacks[b]):
            for dst in range(11):
                if dst in (2, 4, 6, 8): continue
                src = b*2+2
                if B[dst][src] & out[0]: 
                    continue
                stacks[b].pop()
                states[i] = (a, OUT, dst, 0)
                out[0] |= 1 << dst
                backtrack(cost + 10**a * (abs(src-dst) + 4-len(stacks[b])), level+1)
                states[i] = (a, s, b, q)
                stacks[b].append(i)
                out[0] &= ~(1 << dst)
        elif s == OUT and len(stacks[a]) < 4 and all(states[x][0] == states[x][2] for x in stacks[a]):
            dst = a*2+2
            if not (B[dst][b] & out[0]):
                stacks[a].append(i)
                states[i] = (a, IN2, a, len(stacks[a]))
                out[0] &= ~(1 << b)
                backtrack(cost + 10**a * (abs(b-dst) + 5-len(stacks[a])), level+1)
                states[i] = (a, s, b, q)
                stacks[a].pop()
                out[0] |= 1 << b

for i, x in enumerate(input().replace('###', '').split('#')):
    stacks[i].appendleft(len(states))
    states.append((ord(x) - ord('A'), IN, i, 4))
    
for i, x in enumerate('D#C#B#A'.split('#')):
    stacks[i].appendleft(len(states))
    states.append((ord(x) - ord('A'), IN, i, 3))

for i, x in enumerate('D#B#A#C'.split('#')):
    stacks[i].appendleft(len(states))
    states.append((ord(x) - ord('A'), IN, i, 2))

for i, x in enumerate(input().replace('  #', '').replace('#  ', '').split('#')):
    stacks[i].appendleft(len(states))
    states.append((ord(x) - ord('A'), IN, i, 1))
    
backtrack(0)
print(best[0])
