class Point:
    """Represents a point on the plane.

    attributes:  x, y.
    """

class Circle:
    """Represents a circle.

    attributes:  center (a Point object), radius.
    """

c1 = Circle()
c1.center = Point()
c1.center.x = 150
c1.center.y = 100
c1.radius = 75

def point_in_circle(p, circ):

    """Determine wether a given point lies in or on
    a given cicle.

    p:  the point
    circ:  the circle

    returns:  boolean value
    """

    a = circ.center.x
    b = circ.center.y
    r = circ.radius
    return (p.x - a)^2 + (p.y - b)^2 <= r^2

p1 = Point()
p1.x = 170
p1.y = 110

print(point_in_circle(p1,c1))

class Rect:
    """Represents a rectangle.

    attributes:  width, height, corner (a Point)
    """

r1 = Rect()
r1.corner = Point()
r1.corner.x = 140
r1.corner.y = 105
r1.width = 10
r1.height = 11

def rect_in_circle(rect, circ):
    a = rect.corner.x
    b = rect.corner.y
    corners = [
        (a,b),
        (a + rect.width, b),
        (a, b + rect.height),
        (a + rect.width, b + rect.height)
    ]
    inside = True
    for corner in corners:
        p = Point()
        p.x, p.y = corner
        inside = inside and point_in_circle(p, circ)
    return inside

print(rect_in_circle(r1, c1))

def point_inside_circ(p, circ):
    a = circ.center.x
    b = circ.center.y
    r = circ.radius
    return (p.x - a)^2 + (p.y - b)^2 < r^2


def rect_circle_overlap(rect, circ):
    a = rect.corner.x
    b = rect.corner.y
    corners = [
        (a,b),
        (a + rect.width, b),
        (a, b + rect.height),
        (a+ rect.width, b + rect.height)
    ]
    overlap = False
    for corner in corners:
        p = Point()
        p.x, p.y = corner
        overlap = overlap or point_inside_circ(p, circ)
    return overlap

r2 = Rect()
r2.corner = Point()
r2.corner.x = 160
r2.corner.y = 110
r2.width = 100
r2.height = 100

print(rect_circle_overlap(r2, c1))

