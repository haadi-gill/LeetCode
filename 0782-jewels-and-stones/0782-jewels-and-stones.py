class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        j = set(jewels)
        count = 0
        for s in stones:
            if s in j:
                count += 1
        return count 