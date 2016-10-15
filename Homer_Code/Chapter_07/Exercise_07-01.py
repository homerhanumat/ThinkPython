import math

def mysqrt(a, x, tol):
    if a < 0:
        print("a cannot be negative")
    while True:
        y = (x + a/x)/2
        if abs(y-x) < tol:
            break
        x = y
    return x


tolerance = 0.000001
first_guess = 5

print('{:7}{:15}{:15}{:15}'
    .format('a','mysqrt(a)','math.sqrt(a)','diff'))
print('{:7}{:15}{:15}{:15}'
    .format('---','---------','------------','----'))

for a in range(9):
    mine = mysqrt(a,first_guess,tolerance)
    pythons = math.sqrt(a)
    diff = abs(mine-pythons)
    print('{:<7.1f}{:<15.8f}{:<15.8f}{:<15.8f}'
          .format(a,mine,pythons,diff))


