class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        c = Counter(word).most_common()
        position = 0
        count = 0
        for a in c:
            count += ((position // 8)+1) * a[1]
            position += 1
        return count