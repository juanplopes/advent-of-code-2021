from dataclasses import dataclass

@dataclass(frozen=True)
class Cuboid:
    x1: int; x2: int
    y1: int; y2: int
    z1: int; z2: int

    def intersects(self, other):
        return (self.x1 < other.x2 and self.x2 > other.x1
            and self.y1 < other.y2 and self.y2 > other.y1
            and self.z1 < other.z2 and self.z2 > other.z1)

    def contains(self, other):
        return (self.x1 <= other.x1 and self.x2 >= other.x2
            and self.y1 <= other.y1 and self.y2 >= other.y2
            and self.z1 <= other.z1 and self.z2 >= other.z2)

    def count(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1) * (self.z2 - self.z1)


    def children(self):
        if self.count() > 1:
            mx, my, mz = (self.x2+self.x1)//2, (self.y2+self.y1)//2, (self.z2+self.z1)//2
            yield Cuboid(self.x1, mx     , self.y1, my     , self.z1, mz     )
            yield Cuboid(self.x1, mx     , self.y1, my     , mz      , self.z2)
            yield Cuboid(self.x1, mx     , my     , self.y2, self.z1, mz     )
            yield Cuboid(self.x1, mx     , my     , self.y2, mz     , self.z2)
            yield Cuboid(mx     , self.x2, self.y1, my     , self.z1, mz     )
            yield Cuboid(mx     , self.x2, self.y1, my     , mz     , self.z2)
            yield Cuboid(mx     , self.x2, my     , self.y2, self.z1, mz     )
            yield Cuboid(mx     , self.x2, my     , self.y2, mz     , self.z2)
        
class SegTree3D:
    def __init__(self):
        self.root = Cuboid(-2**17, 2**17, -2**17, 2**17, -2**17, 2**17)
        self.data = {self.root: 0}
        self.lazy = {self.root: None}

    def answer(self):
        return self.data[self.root]

    def update_lazy(self, node):
        value = self.lazy.pop(node, None)
        if value is None: return
        self.data[node] = node.count() * value
        for child in node.children():
            self.lazy[child] = value

    def update(self, cuboid, value):
        return self.update_at(self.root, cuboid, value)

    def update_at(self, node, cuboid, value):
        self.update_lazy(node)
        if not cuboid.intersects(node):
            return self.data.get(node, 0)
        elif cuboid.contains(node):
            self.data[node] = node.count() * value
            for child in node.children():
                self.lazy[child] = value
            return self.data[node]    
        
        self.data[node] = sum(self.update_at(child, cuboid, value) for child in node.children())
        return self.data[node]

T = SegTree3D()
while True:
    try: cmd, line = input().split(' ')
    except EOFError: break
    x1, x2, y1, y2, z1, z2 = (int(b) 
        for a in line.split(',') 
        for b in a.split('=')[1].split('..'))
    #if not -50 <= x1 <= 50 or not -50 <= x2 <= 50: continue
    #if not -50 <= y1 <= 50 or not -50 <= y2 <= 50: continue
    #if not -50 <= z1 <= 50 or not -50 <= z2 <= 50: continue
    T.update(Cuboid(x1, x2+1, y1, y2+1, z1, z2+1), cmd == 'on')
    print(T.answer())
print(T.answer())