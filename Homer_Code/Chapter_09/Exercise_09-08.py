def is_palindrome(word):
    return word == word[::-1]

def int2odo(n):
    strn = str(n)
    return '0'*(6-len(strn))+strn

def is_special(odo):
    if not is_palindrome(odo[2:]):
        return False
    odo1 = int2odo(int(odo) + 1)
    if not is_palindrome(odo1[1:]):
        return False
    odo2 = int2odo(int(odo) + 2)
    if not is_palindrome(odo2[1:5]):
        return False
    odo3 = int2odo(int(odo) + 3)
    if not is_palindrome(odo3):
        return False
    return True

for i in range(999998):
    odo = int2odo(i)
    if is_special(odo):
        print(odo)
