from collections import deque
input(); input()

states = []
stacks = [deque() for _ in range(4)]
best = [10000000000]
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
        if level <= 2: print(' ' * level, i, best, len(visited))
        if s == IN and stacks[b][-1] == i and any(states[x][0] != states[x][2] for x in stacks[b]):
            for dst in range(11):
                if dst in (2, 4, 6, 8): continue
                src = b*2+2
                if any(dst <= b2 < src or src < b2 <= dst for a2, s2, b2, _ in states if s2 == OUT): 
                    continue
                stacks[b].pop()
                states[i] = (a, OUT, dst, 0)
                backtrack(cost + 10**a * (abs(src-dst) + 4-len(stacks[b])), level+1)
                states[i] = (a, s, b, q)
                stacks[b].append(i)
        elif s == OUT and len(stacks[a]) < 4 and all(states[x][0] == states[x][2] for x in stacks[a]):
            dst = a*2+2
            if not any(dst <= b2 < b or b < b2 <= dst for a2, s2, b2, _ in states if s2 == OUT): 
                stacks[a].append(i)
                states[i] = (a, IN2, a, len(stacks[a]))
                backtrack(cost + 10**a * (abs(b-dst) + 5-len(stacks[a])), level+1)
                states[i] = (a, s, b, q)
                stacks[a].pop()

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
