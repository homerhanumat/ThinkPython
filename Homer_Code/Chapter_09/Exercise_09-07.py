fin = open('../words.txt')

def has_doubs(word,prev,in_run,got,need):
    if len(word) < 2*(need-got)-1:
        return False
    if (got + 1 == need) and word[0] == prev and not in_run:
        return True
    if word[0] == prev and in_run:
        got = 1
    if word[0] == prev and not in_run:
        got = got +1
        in_run = True
    if word[0] != prev and not in_run:
        got = 0
    if word[0] != prev and in_run:
        in_run = False
    prev = word[0]
    word = word[1:]
    return has_doubs(word,prev,in_run,got,need)

# for word in fin:
#     if has_doubs(word,'',False,0,3):
#         print(word)

#######################################

# Here's a start on a better one.
# (Limitations:  it assumes no word has
# more than 9 of the same letter in a row, and we
# don't let triples count.)

# compute length of initial run of characters:
def init_run(word):
    if len(word) == 0:
        return 0
    if len(word) == 1:
        return 1
    first_char = word[0]
    i = 1
    while i < len(word) and word[i] == first_char:
        i = i+1
    return i

# create string of run-lengths
def run_lengths(word):
    runs = ''
    while len(word) > 0:
        run = init_run(word)
        runs = runs + str(run)
        word = word[run:]
    return runs

def has_doubs2(word,n):
    pattern = '2'*n
    rl = run_lengths(word)
    if rl.find(pattern) >= 0:
        return True
    else:
        return False

print(has_doubs2('aabaaccfaabbcct',3))


