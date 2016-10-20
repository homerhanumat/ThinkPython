def anagrams(word_lst):
    a = dict()
    for word in word_lst:
        t = tuple(word)
        abc_word = tuple(sorted(t))
        a.setdefault(abc_word, []).append(word)
    return a


fin = open('Homer_Code/words.txt')
words = []
for word in fin:
    stripped = word.strip()
    words.append(stripped)

agrams = anagrams(words)

for key in agrams:
    if len(agrams[key]) > 9:
        print(agrams[key])
