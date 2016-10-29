class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return '('+ str(self.x) + ', ' \
              + str(self.y) + ')'

    def __add__(self, other):
        if isinstance(other, Point):
            x = self. x + other.x
            y = self.y + other.y
            sum = Point(x, y)
            return sum
        elif isinstance(other, tuple):
            x = self. x + other[0]
            y = self.y + other[1]
            sum = Point(x, y)
            return sum
        else:
            print("Don't know how to add these!")
            return None

    def __radd__(self, other):
        return self.__add__(other)

p1 = Point(x = 10, y = 15)
p2 = Point(x = 5, y = 20)
q = (3, 7)
print(p1 + p2)
print(p1 + q)
print(p1 + 7)
print(q + p1)

def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))

print_attributes(p1)




