def has_duplicates(lst):
    if len(lst) == 0:
        return False
    for i in range(len(lst)):
        if lst[i] in lst[(i+1):]:
            return True
    return False

a = [1,2,1]
print(a, has_duplicates(a))
