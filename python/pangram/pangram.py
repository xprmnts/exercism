import re
def is_pangram(phrase):
    # lowercase everything
    # remove everything but alphabets
    # check length of set
    if(len(set(re.sub(r'[^a-z]',"", phrase.lower()))) != 26):
        return False
    return True