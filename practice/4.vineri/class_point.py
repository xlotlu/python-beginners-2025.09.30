import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
        
    def __str__(self):
        return str(self.as_tuple())

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
 
    def translate(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
    
    def as_tuple(self):
        return (self.x, self.y)

    @property
    def distance_from_origin(self):
        print("eu mă ruleeeeez")
        return math.sqrt(self.x ** 2 + self.y ** 2)

p1 = Point(5, 24)
p2 = Point(5, 24)

print(p1 == p2)

p = Point(3, 4)

print(repr(p))
print("my point is", p)
print(p.distance_from_origin)
