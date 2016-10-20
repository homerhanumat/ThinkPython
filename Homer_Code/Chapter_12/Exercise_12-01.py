# Mostly copying Downey's code, here.

def most_frequent(s):
    """Sorts the letters in s in reverse order of frequency.

    s: string

    Returns: list of letters
    """

    # My additonas:  pre-process the string.
    # First convert to lower-case:
    lowercase = s.lower()

    # Then remove all non alphabetic characters:
    all_alpha = []
    for char in lowercase:
        if char.isalpha():
            all_alpha.append(char)

    # Now we a have list, but make_histogram can handle it:
    hist = make_histogram(all_alpha)

    t = []
    for x, freq in hist.items():
        t.append((freq, x))
    t.sort(reverse=True)
    # We are making a table, so return t:
    return t


def make_histogram(s):
    """Make a map from letters to number of times they appear in s.

    s: list of characters

    Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist


# Test sentence:
# s = 'Hello there! This is a Small Sentence.  Do you like it?'

# Opne the text and slurp:
sense = open('../sense_and_sensibility.txt').read()

table = most_frequent(sense)

letter_sum = 0
for freq, letter in table:
    letter_sum += freq

print('{:<10}{:<10}{:<10}'.format('letter','frequency','percentage'))
for freq, letter in table:
    print('{:<10}{:<10}{:>10.2f}'.format(letter, freq, 100*freq/letter_sum))

# And for fun:  find the words that contain the letter z:

sense_words = sense.split() # will miss on some punctuation!

print('\nAnd now, the z-words:\n')
for word in sense_words:
    if word.find('z') > -1:
        print(word)
