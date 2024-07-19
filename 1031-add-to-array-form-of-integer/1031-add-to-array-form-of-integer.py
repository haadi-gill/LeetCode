class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        index = len(num)-1
        while k > 0 and index >= 0:
            num[index] += k%10
            k = int(k/10)
            if num[index] >= 10:
                k += int(num[index]/10)
                num[index] %= 10
            index -= 1

        while k > 0:
            num.insert(0, k%10)
            k = int(k/10)
        
        return num