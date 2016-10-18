def is_sorted(lst):
    return lst == sorted(lst)

a = [1,2,3,4]
print(a,is_sorted(a))

b = [1,3,4,2]
print(b,is_sorted(b))
