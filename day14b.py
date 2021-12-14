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

answer = Counter(start[0])
for (a, b), value in state.items():
    answer[b] += value

print(max(answer.values()) - min(answer.values()))
