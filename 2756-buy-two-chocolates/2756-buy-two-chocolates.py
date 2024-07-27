class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        minMon = -1

        n = len(prices)

        for i in range(n-1):
            for j in range(i+1, n):
                diff = money - (prices[i] + prices[j])
                if diff >= 0 and diff > minMon:
                    minMon = diff
        
        return minMon if minMon > -1 else money