(x1, x2), (y1, y2) = (map(int, x.split('=')[1].split('..')) 
                      for x in input().split(', '))

S = set()
for dy in range(-500, 500):
    for t in range(500):
        if not y1 <= dy*t - (t*t-t)//2 <= y2: continue
        for dx in range(500):
            if not x1 <= min(dx*t, dx*dx)-min((t*t-t)//2, (dx*dx-dx)/2) <= x2: continue
            S.add((dx, dy))

print(len(S))
