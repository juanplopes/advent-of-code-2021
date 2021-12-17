(x1, x2), (y1, y2) = (map(int, x.split('=')[1].split('..')) 
                      for x in input().split(', '))

answer = 0
for dy in range(-500, 500):
    Y = [dy*t - (t*t-t)//2 for t in range(500)]
    if not any(filter(lambda y: y1 <= y <= y2, Y)): continue
    answer = max(answer, max(Y))
print(answer)