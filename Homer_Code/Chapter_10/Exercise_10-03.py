def copy_of(lst):
    new = []
    new.extend(lst)
    return new

def middle(lst):
    new = copy_of(lst)
    if len(new) < 2:
        return -1
    del new[0]
    del new[-1]
    return new

a = [1,2,3,4,5]
print(a,middle(a))

b = [1,2]
print(b,middle(b))

