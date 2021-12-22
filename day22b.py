from dataclasses import dataclass

@dataclass(frozen=True)
class Cuboid:
    x1: int; x2: int; y1: int; y2: int; z1: int; z2: int

    def count(self):
        if self.x1 >= self.x2 or self.y1 >= self.y2 or self.z1 >= self.z2: return 0
        return (self.x2 - self.x1) * (self.y2 - self.y1) * (self.z2 - self.z1)

    def subtract(a, b):
        if not (a.x1 < b.x2 and a.x2 > b.x1
            and a.y1 < b.y2 and a.y2 > b.y1
            and a.z1 < b.z2 and a.z2 > b.z1):
            yield a
        else:
            b = Cuboid(min(max(b.x1, a.x1), a.x2), min(max(b.x2, a.x1), a.x2),
                    min(max(b.y1, a.y1), a.y2), min(max(b.y2, a.y1), a.y2),
                    min(max(b.z1, a.z1), a.z2), min(max(b.z2, a.z1), a.z2))

            yield Cuboid(a.x1, b.x1, a.y1, a.y2, a.z1, a.z2)
            yield Cuboid(b.x2, a.x2, a.y1, a.y2, a.z1, a.z2)
            yield Cuboid(b.x1, b.x2, a.y1, b.y1, a.z1, a.z2)
            yield Cuboid(b.x1, b.x2, b.y2, a.y2, a.z1, a.z2)
            yield Cuboid(b.x1, b.x2, b.y1, b.y2, a.z1, b.z1)
            yield Cuboid(b.x1, b.x2, b.y1, b.y2, b.z2, a.z2)
      
T = []
for step in range(1, 100000):
    try: cmd, line = input().split(' ')
    except EOFError: break
    x1, x2, y1, y2, z1, z2 = (int(b) 
        for a in line.split(',') 
        for b in a.split('=')[1].split('..'))
    
    cuboid = Cuboid(x1, x2+1, y1, y2+1, z1, z2+1)
    T = [child for other in T
         for child in other.subtract(cuboid) 
         if child.count() > 0]
    if cmd == 'on':
        T.append(cuboid)

print(sum(x.count() for x in T))