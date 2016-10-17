#seq = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#for c in seq:
#    print(c + '\t' + str(ord(c)))

def rotate_word(word,rot):
    cipher = ''
    for c in word:
        if c.islower():
            r_ord = ((ord(c) - 97 + rot) % 26) + 97
        elif c.isupper():
            r_ord =  ((ord(c) - 65 + rot) % 26) + 65
        elif c.isspace():
            r_ord = ord(c)
        else:  # some character we can't handle
            return -1
        cipher = cipher + chr(r_ord)
    return cipher

print(rotate_word("Hello There",5))
