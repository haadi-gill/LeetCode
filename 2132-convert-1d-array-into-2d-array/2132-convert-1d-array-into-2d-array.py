class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """

        if len(original) != (n*m): return []
        twoD = []
        count = 0
        for i in range(m):
            twoD.append(original[(count*n):((count+1)*n)])
            count += 1
        return twoD
