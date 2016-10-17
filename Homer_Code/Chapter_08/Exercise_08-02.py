def char_count(s,char):
    word = s
    count = word.count(char)
    print("The number of " + char + "'s in "
          + word + ' is ' + str(count) + '.')

char_count('banana','a')
