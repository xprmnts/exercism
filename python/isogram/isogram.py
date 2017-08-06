import re


def is_isogram(word):
    # convert word to lowercase
    word = word.lower()

    # Remove anything other than alphabets
    word = re.sub(r'[^a-z]', "", word)

    len_word = len(word)

    # if input is not a word return true
    if(len_word < 1):
        return True

    # for each letter iterate from position of current letter to end
    # if the current letter finds itself in rest of the string
    # return false, else after loop ends return true
    for letter in range(0, len_word):
        if(word[letter] in word[letter + 1: len_word]):
            return False
    return True
