import string

def word_list(fh, begin_line):
    translator = str.maketrans({key: None for key in string.punctuation})
    lst = []
    count = 0
    for line in fh:
        count += 1
        if count >= begin_line:
            # a hyphenated word should count as two separate words:
            line = line.replace('-', ' ')
            words = line.split()
            for word in words:
                lst.append(word.translate(translator). lower())
    return lst

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

fin = open('../sense_and_sensibility.txt')
words = word_list(fin, 45)

print('Total words = ',len(words), '\n')

h = histogram(words)

lst = []
for key, value in h.items():
    lst.append((key, value))
# You need not re-order the key and value, you can
# use the key paramater in sort, along with an anonymous
# function defined by lambda:
lst.sort(reverse = True, key = lambda word : word[1])
for i in range(100):
    print(lst[i])

print('\nThe number of distinct words is', len(list(h.keys())))

# let's find the words in the book that aren't in our Scrabble list:
fin2 = open('../words.txt')
words = histogram(word_list(fin2, 0))


def subtract(d1, d2):
    return set(d1) - set(d2)  # set is great!

diff = subtract(h, words)
print('Words in the book that are not in the word list:')
for word in diff:
    print(word)
