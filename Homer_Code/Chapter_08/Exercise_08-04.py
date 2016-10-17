def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

# The above function only checks the first character.
# Hence it gives the wrong result
# on a word where the lower-case does not appear first.
w1 = 'Hello'
print("any_lowercase1('" + w1 + "') = "+
      str(any_lowercase1(w1)))


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

# Same problem as previous function, plus it's
# checking the (lowercase) character 'c'.

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

# This ends up being determined by the final character.
w3 = 'xxZ'
print("any_lowercase3('" + w3 + "') = "+
      str(any_lowercase3(w3)))

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# This one works!
w4 = 'XxZ'
print("any_lowercase4('" + w4 + "') = "+
      str(any_lowercase4(w4)))

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

# The above function returns False when there is at least
# one non lowercase letter:

w5 = 'xxxZxx'
print("any_lowercase5('" + w5 + "') = "+
      str(any_lowercase5(w5)))
