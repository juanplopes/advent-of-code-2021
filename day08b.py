def common(a, b): 
    return len(set(a).intersection(b));

A = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
S = {tuple(common(A[x], A[y]) for y in (1, 4, 7, 8)): x for x in range(10)}

answer = 0
while True:
    try: training, data = (x.split() for x in  input().split('|'))
    except EOFError: break

    sample = {len(x): x for x in training}
    value = 0
    for digit in data:
        signature = tuple(common(digit, sample[x]) for x in (2, 4, 3, 7))
        value = value * 10 + S[signature]
    answer += value
print(answer)