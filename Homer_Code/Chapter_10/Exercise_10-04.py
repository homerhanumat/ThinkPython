def chop(lst):
    if len(lst) < 2:
        return -1
    del lst[0]
    del lst[-1]
    return None

a = [1,2,3,4,5]
print(chop(a),a)

b = [1,2]
print(chop(b),b)
