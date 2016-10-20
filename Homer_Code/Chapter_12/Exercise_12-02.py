import os
# Dunno why I have to do this all of a sudden;
# I'm making sure the parent directory is the working directory.
os.chdir(os.path.dirname(__file__))
# print(os.getcwd())


def anagrams(word_lst):
    a = dict()
    for word in word_lst:
        t = tuple(word)
        abc_word = tuple(sorted(t))
        a.setdefault(abc_word, []).append(word)
    return a

fin = open('../words.txt')

words = []
for word in fin:
    stripped = word.strip()
    words.append(stripped)

agrams = anagrams(words)

print('The anagram-sets of size 10 or more:\n')
for key in agrams:
    if len(agrams[key]) > 9:
        print(agrams[key])

# now let's sort from longest to shortest anagram-list:
def print_sets_by_size(agrams, n):
    d = []
    for key in agrams:
        a_set = agrams[key]
        if len(a_set) > 1:
            d.append((len(a_set), a_set))
    d.sort(reverse=True)
    print('\nThe',n, 'largest anagram sets:\n')
    for i in range(n):
        length, set = d[i]
        print(set)

print_sets_by_size(agrams,20)

# Now the bingos

a8 = {}
for key in agrams:
    if len(key) == 8:
        a8[key] = agrams[key]

print_sets_by_size(a8, 10)

# "angriest" wins!
