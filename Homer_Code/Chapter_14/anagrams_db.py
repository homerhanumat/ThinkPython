import anagram_sets
import shelve, inspect

#print(os.getcwd())

def store_anagrams(filename, ad):
    """Stores the anagrams in ad in a shelf.

    filename: string file name of shelf
    ad: dictionary that maps strings to list of anagrams
    """
    shelf = shelve.open(filename)

    for word, word_list in ad.items():
        shelf[word] =  word_list

    shelf.close()

def read_anagrams(filename, word):

    shelf = shelve.open(filename, 'c')
    sig = inspect.signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []


if __name__ == '__main__':
    d = anagram_sets.all_anagrams('words.txt')
    store_anagrams('anagram_dict.db', d)
    print(read_anagrams('anagram_dict.db','post'))

# the last line gives error:  db,.error:  db type could not be determined
