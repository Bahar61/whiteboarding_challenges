"""A pangram is a sentence that contains all the letters of the English alphabet at least once, for example
Write a function that returns True if given string is a pangram.

    >>> is_pangram('The quick brown fox jumps over the lazy dog.')
    True
"""

import string 
  
def is_pangram(string): 

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = set(string.lower())
    
    for char in alphabet: 
        if char not in letters: 
            return False
  
    return True







def is_pangram(s):

    # Make a set of unique characters in `s`
    letters = set([c for c in s.lower() if c.isalpha()])

    # `s` is a pangram if there are 26 unique characters present
    return len(letters) == 26



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE TERRIFIC AT THIS!\n")
