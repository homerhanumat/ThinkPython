def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if not isinstance(word,str):
        print('Expected a string!')
        return None
    wlen = len(word)
    if wlen <= 1:
        return True
    elif first(word) != last(word):
        return False
    else:
        word = middle(word)
        return is_palindrome(word)

print(is_palindrome('abba'))
