a = int(input('Enter length of side a\n'))
b = int(input('Enter length of side b\n'))
c = int(input('Enter length of side c\n'))

def is_triangle(a,b,c):
    a_less = a < b+c
    b_less = b < a+c
    c_less = c < a+b
    if a_less and b_less and c_less:
        print("Yes, it's a triangle!")
    else:
        print("No, it's not a triangle.")

is_triangle(a,b,c)
