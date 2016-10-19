def has_dups(lst):
    d = dict()
    for item in lst:
        d[item] = d.get(item,0) + 1
        if d[item] > 1:
            return True
    return False

s = [1,2,3,4,5,6]
print(has_dups(s))
