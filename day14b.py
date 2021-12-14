from collections import Counter

start = input()
input()
rules = {}
while True:
    try: a, b = input().split(' -> ')
    except EOFError: break
    rules[tuple(a)] = b

state = Counter(zip(start, start[1:]))
for i in range(40):
    new_state = Counter()
    for (a, b), value in state.items():
        c = rules[(a, b)]
        new_state[(a, c)] += value
        new_state[(c, b)] += value
    state = new_state

answer = Counter((start[0], start[-1]))
for (a, b), value in state.items():
    answer[a] += value
    answer[b] += value

print(max(answer.values())//2 - min(answer.values())//2)
