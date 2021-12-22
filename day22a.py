from collections import Counter
T = Counter()

while True:
    try: cmd, line = input().split(' ')
    except EOFError: break
    x1, x2, y1, y2, z1, z2 = (int(b) 
        for a in line.split(',') 
        for b in a.split('=')[1].split('..'))
    if not -50 <= x1 <= 50 or not -50 <= x2 <= 50: continue
    if not -50 <= y1 <= 50 or not -50 <= y2 <= 50: continue
    if not -50 <= z1 <= 50 or not -50 <= z2 <= 50: continue

    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1,z2+1):
                T[(x, y, z)] = cmd == 'on'

print(sum(T.values()))