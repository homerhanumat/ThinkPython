import turtle
import math

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
c1.center.x = 70
c1.center.y = 50
c1.radius = 75

class Rect:
    """Represents a rectangle.

    attributes:  width, height, corner (a Point)
    """

r1 = Rect()
r1.corner = Point()
r1.corner.x = 30
r1.corner.y = 30
r1.width = 100
r1.height = 130

bob = turtle.Turtle()

def draw_rect(t, rect):
    t.penup()
    t.setx(rect.corner.x)
    t.sety(rect.corner.y)
    t.pendown()
    t.fd(rect.width)
    t.lt(90)
    t.fd(rect.height)
    t.lt(90)
    t.fd(rect.width)
    t.lt(90)
    t.fd(rect.height)
    t.lt(90)
    turtle.mainloop()

#draw_rect(bob, r1)

def polygon(t,n,length):
    side = length/n
    turn_angle = 360/n
    for i in range(n):
        t.fd(side)
        t.lt(turn_angle)

def circle(t,r):
    circumference = 2*math.pi*r
    side_number = 100
    polygon(t,side_number,circumference)

def draw_circle(t,circ):
    t.penup()
    t.setx(circ.center.x)
    t.sety(circ.center.y)
    t.pendown()
    circle(t, circ.radius)
    turtle.mainloop()

draw_circle(bob, c1)
