class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        index = 0
        combined = ''

        if len(word1) > len(word2):
            index = len(word2)
            for i in range(index):
                combined += word1[i] + word2[i]
            combined += word1[index:]
        else:
            index = len(word1)
            for i in range(index):
                combined += word1[i] + word2[i]
            combined += word2[index:]

        return combined
