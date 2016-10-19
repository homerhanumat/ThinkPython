def read_dict(file):
    fin = open(file)
    d = dict()
    i = 0
    for line in fin:
        line = line.strip()
        d[line]=i
        i += 1
    return d

d = read_dict('../words.txt')

print(d.get('elephant',-1))
