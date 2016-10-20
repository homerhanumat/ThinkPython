import random

def choose_from_hist(h):
    """Choose an item at random, with probability of
    selection of each item determined by its relative frequency
    in the histogram h.

    h:  A histogram dictionary.

    returns:  a random item"""
    lst = []
    for key in h:
        lst.extend([key] * h[key])
    return random.choice(lst)

hist = { 'a':3, 'b':5, 'c':2}
print(choose_from_hist(hist))
