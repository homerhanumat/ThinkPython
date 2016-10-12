import turtle
import math

# square function
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

def square2(t,length):
    for i in range(4):
        t.fd(length/4)
        t.lt(90)

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

def arc(t,r,angle):
    """Draws line segments to make an the arc
    of a circle of radius r, over the
    given angle.  t is a turtle."""
    n = 50 #divide up angle
    turn_angle = angle/n
    total_arc_length = angle*math.pi/180*r
    for i in range(n):
        t.fd(total_arc_length/n)
        t.lt(turn_angle)

bob = turtle.Turtle()
arc(bob,100,360)
turtle.mainloop()
