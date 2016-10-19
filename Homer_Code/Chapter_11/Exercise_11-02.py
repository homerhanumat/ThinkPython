def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        #print(key,inverse.setdefault(val,[]))
        inverse.setdefault(val,[]).append(key)
    return inverse


d = {'a': 1, 'b': 1, 'c': 3, 'd': 2 }
print(invert_dict(d))
