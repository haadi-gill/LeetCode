class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        limit = a if a < b else b
        factorCount = 0

        for i in range(1, limit+1):
            if a%i == 0 and b%i == 0:
                factorCount += 1

        return factorCount