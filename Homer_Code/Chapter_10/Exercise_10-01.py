def flatten(lst):
    for i in range(len(lst)):
        if isinstance(lst[i],list):
            list_elem = lst.pop(i)
            lst.extend(list_elem)
            return flatten(lst)
    return lst

def nested_sum(lst):
    return sum(flatten(lst))


a = [1,2,[3,4],[5,[[6]]]]
print(nested_sum(a))

