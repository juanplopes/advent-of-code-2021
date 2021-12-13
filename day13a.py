def fold(T, over_x, value):
    for x, y in T:
        yield (2*value - x if over_x and x > value else x, 
               2*value - y if not over_x and y > value else y)

T = set()
while True:
    line = input()
    if line == '': break
    T.add(tuple(map(int, line.split(','))))

while True:
    try: a, b = input().split(' ')[2].split('=')
    except EOFError: break
    T = set(fold(T, a == 'x', int(b)))
    break

print(len(T))