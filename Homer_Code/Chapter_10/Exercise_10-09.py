fin = open('../words.txt')

def make1(handler):
    lst = []
    for item in handler:
        item = item.strip()
        lst = lst + [item]
    return lst

#a = make1(fin)
#print(a[0:10])

def make2(handler):
    lst = []
    for item in handler:
        item = item.strip()
        lst.append(item)
    return lst

b = make2(fin)
print(b[0:10])

# make2 is much faster!
