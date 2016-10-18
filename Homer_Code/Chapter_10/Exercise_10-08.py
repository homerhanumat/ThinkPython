import random as rnd

def has_duplicates(lst):
    if len(lst) == 0:
        return False
    for i in range(len(lst)):
        if lst[i] in lst[(i+1):]:
            return True
    return False

def birthday(n,days,sims):
    counter = 0
    for m in range(sims):
        bdays = [0] * n
        for i in range(n):
            bdays[i] = rnd.randint(1,days)
        if has_duplicates(bdays):
            counter += 1
    print("Proabablity of a match is:  ",
          str(counter/sims),sep = '')

birthday(23,365,20000)
