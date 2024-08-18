class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        pos = word.find(ch)
        if pos == -1:
            return word
        else:
            return word[:pos+1][::-1] + word[pos+1:]