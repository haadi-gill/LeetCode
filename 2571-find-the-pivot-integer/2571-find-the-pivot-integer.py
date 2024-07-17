class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1: return n
        for i in range(int(n/2), round(7*n/8)):
            if sum(range(i+1)) == sum(range(i,n+1)):
                return i
        
        return -1