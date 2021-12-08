
from itertools import permutations
segments = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

def translate(permutation, elements):
    current = 0
    for element in elements:
        translated = ''.join(sorted(permutation[ord(x) - ord('a')] for x in element))
        if translated not in segments:
            return None
        current = current * 10 + segments.index(translated)
    return current

answer = 0
while True:
    try: training, data = (x.split() for x in  input().split('|'))
    except EOFError: break

    for permutation in permutations('abcdefg'):
        if translate(permutation, training) is not None:
            answer += translate(permutation, data)
            break
    
print(answer)