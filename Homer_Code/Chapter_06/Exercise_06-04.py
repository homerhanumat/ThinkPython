def is_power(a,b):
    if not (isinstance(a,int) and isinstance(b,int)):
        print('Both numbers must be integers!')
        return None
    if a == 0 or b == 0:
        return False
    if a == b:
        return True
    elif a % b == 0:
        return(is_power(int(a/b),b))
    else:
        return False

print(is_power(0,4))
