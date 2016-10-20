import string

def word_list(fh, begin_line):
    translator = str.maketrans({key: None for key in string.punctuation})
    lst = []
    count = 0
    for line in fh:
        count += 1
        if count >= begin_line:
            words = line.split()
            for word in words:
                lst.append(word.translate(translator).lower())
    return lst

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

fin = open('../sense_and_sensibility.txt')
words = word_list(fin, 45)

print('Total words = ',len(words),'\n')

h = histogram(words)

lst = []
for key in h:
    lst.append((h[key], key))
lst.sort(reverse = True)
for i in range(100):
    print(lst[i])

print('\nThe number of distinct words is', len(list(h.keys())))
