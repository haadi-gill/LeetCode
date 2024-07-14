class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        d = {}
        for i, c in enumerate(alphabet):
            d[c] = i
        
        val1 = 0
        val2 = 0
        val3 = 0

        for x in firstWord:
            val1 = (val1*10) + d[x]
        
        for y in secondWord:
            val2 = (val2*10) + d[y]

        for z in targetWord:
            val3 = (val3*10) + d[z]

        return val3 == (val1 + val2)