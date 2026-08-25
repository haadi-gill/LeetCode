class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        factors = set()
        for i in nums:
            if i//k == i/k:
                factors.add(i//k)
        for i in range(1, 102):
            if not i in factors:
                return i * k