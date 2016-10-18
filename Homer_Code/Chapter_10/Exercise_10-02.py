def cumsum(lst):
    cum = [lst[0]]
    for elem in lst[1:]:
        new_sum = cum[-1]+elem
        cum.append(new_sum)
    return cum

a = [1,2,3,4,5]
print(cumsum(a))
