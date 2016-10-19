def read_dict(file):
    fin = open(file)
    d = dict()
    i = 0
    for line in fin:
        line = line.strip()
        d[line]=i
        i += 1
    return d

def rotate_word(wd,i):
    i = i % len(wd)
    return wd[i:]+wd[0:i]

d = read_dict('../words.txt')

d2 = dict()
for word in d:
    d2[word] = [word]
    for i in range(1,len(word)):
        rot = rotate_word(word,i)
        if rot in d:
            d2[word].append(rot)

for word in d2:
    if len(d2[word]) >= 3:
        print(d2[word])




