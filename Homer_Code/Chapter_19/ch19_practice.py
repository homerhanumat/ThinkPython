from collections import Counter, defaultdict, namedtuple
from math import pow

c = Counter('supercalifragilisticexpialadocious')
print(c)

for key, value in c.most_common(3):
    print(key, value)

s = int(sum(pow(x,2) for x in range(101) if x % 10 == 0))
print(s)

print([ int(pow(x,2)) for x in range(101) if x % 10 == 0 ])

numbers = [ 4,5,7,3,1,8]
doubled_odds = map(lambda n: n * 2, filter(lambda n: n % 2 == 1, numbers))
print(numbers)
for number in doubled_odds:
    print(number)

# dictionary comprehension:
words = [ 'hello', 'there', 'python', 'enthusiast' ]
dict = { word: len(word) for word in words }
print(dict)

# set comprehension:
first_letters = { word[0] for word in words }
print(first_letters)
