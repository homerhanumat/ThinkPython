import turtle

def clock(t,radius, hours, color):
    t.color(color)
    mark_start = 0.75*radius
    mark_len = 0.1*radius
    final_step = radius - (mark_start+mark_len)
    t.stamp()
    t.penup()
    for i in range(hours):
        t.fd(mark_start)
        t.pendown()
        t.fd(mark_len)
        t.penup()
        t.fd(final_step)
        t.stamp()
        t.backward(radius)
        t.lt(360/hours)

bob = turtle.Turtle()
bob.shape('turtle')
clock(bob,100,6,'blue')
turtle.mainloop()

