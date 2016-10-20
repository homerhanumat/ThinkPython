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

def is_met_pair(a,b):

    """Determine whether two anagram pairs a and b
    are a metathesis pair"""

    diffs = []
    count = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
            if count > 2:
                return False
            diffs.append(i)

    if len(diffs) != 2:
        return False

    first, second = diffs[0], diffs[1]
    if a[first] != b[second]:
        return False

    return True

def make_met_pairs(agrams):
    pairs = []
    for key in agrams:
        a_set = agrams[key]
        if len(a_set) ==  1:
            continue
        for i in range(len(a_set)):
            for j in range(i+1, len(a_set)):
                if is_met_pair(a_set[i], a_set[j]):
                    pairs.append((a_set[i], a_set[j]))
    return pairs

fin = open('../words.txt')

words = []
for word in fin:
    stripped = word.strip()
    words.append(stripped)

agrams = anagrams(words)

pairs = make_met_pairs(agrams)

for i in range(20):
    print(pairs[i])

print(len(pairs))
