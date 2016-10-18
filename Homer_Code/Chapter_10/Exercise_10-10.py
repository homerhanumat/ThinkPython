def make2(handler):
    lst = []
    for item in handler:
        item = item.strip()
        lst.append(item)
    return lst

def bsearch(item, lst, begin, end):
    if begin == end:
        if lst[begin] == item:
            return begin
        else:
            return None
    between = (end+begin) // 2
    if lst[between] == item:
        return between
    if item < lst[between]:
        return bsearch(item, lst, begin, between)
    else:
        return bsearch(item, lst, between+1, end)

def in_bisect(item, lst):
    if len(lst) == 0:
        return None
    begin = 0
    end = len(lst)-1
    return bsearch(item, lst, begin, end)

a = range(0,1000,2)
print(in_bisect(514, a))

b = []
print(in_bisect(2,b))

fin = open('../words.txt')
word_list = make2(fin)
print(in_bisect('elephant',word_list))
print(in_bisect('aardvark',word_list))



