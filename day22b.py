from dataclasses import dataclass

@dataclass(frozen=True)
class Cuboid:
    x1: int; x2: int
    y1: int; y2: int
    z1: int; z2: int

    def count(self):
        if self.x1 >= self.x2 or self.y1 >= self.y2 or self.z1 >= self.z2: return 0
        return (self.x2 - self.x1) * (self.y2 - self.y1) * (self.z2 - self.z1)

    def subtract(self, other):
        other = Cuboid(
            min(max(other.x1, self.x1), self.x2),
            min(max(other.x2, self.x1), self.x2),
            min(max(other.y1, self.y1), self.y2),
            min(max(other.y2, self.y1), self.y2),
            min(max(other.z1, self.z1), self.z2),
            min(max(other.z2, self.z1), self.z2))

        yield Cuboid(self.x1, other.x1, self.y1, self.y2, self.z1, self.z2)
        yield Cuboid(other.x2, self.x2, self.y1, self.y2, self.z1, self.z2)

        yield Cuboid(other.x1, other.x2, self.y1, other.y1, self.z1, self.z2)
        yield Cuboid(other.x1, other.x2, other.y2, self.y2, self.z1, self.z2)

        yield Cuboid(other.x1, other.x2, other.y1, other.y2, self.z1, other.z1)
        yield Cuboid(other.x1, other.x2, other.y1, other.y2, other.z2, self.z2)
      
T = set()
for step in range(1, 100000):
    try: cmd, line = input().split(' ')
    except EOFError: break
    x1, x2, y1, y2, z1, z2 = (int(b) 
        for a in line.split(',') 
        for b in a.split('=')[1].split('..'))
    
    cuboid = Cuboid(x1, x2+1, y1, y2+1, z1, z2+1)
    print(step, len(T), cuboid)
    T = {child for other in T
         for child in other.subtract(cuboid) 
         if child.count() > 0}
    if cmd == 'on':
        T.add(cuboid)

print(sum(x.count() for x in T))