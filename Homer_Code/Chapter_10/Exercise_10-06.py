def is_anagram(a,b):
    return sorted(a) == sorted(b)

a = 'carb'
b = 'bard'
print(a,b,is_anagram(a,b))
