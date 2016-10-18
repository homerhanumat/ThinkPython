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

def find_revs(lst):
    pairs = []
    for item in lst:
        reversed = item[::-1]
        place = in_bisect(reversed, lst)
        if place == None:
            continue
        pairs.append([item, reversed])
        print(item,reversed)
    return pairs


fin = open('../words.txt')
word_list = make2(fin)
results = find_revs(word_list)
print(results[0:5])
