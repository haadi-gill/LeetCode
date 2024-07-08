'''
500. Keyboard Row

Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

    the first row consists of the characters "qwertyuiop",
    the second row consists of the characters "asdfghjkl", and
    the third row consists of the characters "zxcvbnm".

 

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:

Input: words = ["omk"]
Output: []

Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]

'''


def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    rows = []
    rows.append(set("qwertyuiop"))
    rows.append(set("asdfghjkl"))
    rows.append(set("zxcvbnm"))
    
    good_words = []

    for word in words:
        for row in rows:
            if set(word.lower()).issubset(row):
                good_words.append(word)
                break
    
    return good_words