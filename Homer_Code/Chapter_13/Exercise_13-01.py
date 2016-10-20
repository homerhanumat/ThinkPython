import string

def word_list(fh):
    translator = str.maketrans({key: None for key in string.punctuation})
    lst = []
    for line in fh:
        words = line.split()
        for word in words:
            lst.append(word.translate(translator).lower())
    return lst

fin = open('../sense_and_sensibility.txt')
words = word_list(fin)


