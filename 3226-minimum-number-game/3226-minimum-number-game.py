class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        o = sorted(nums)
        for i in range(0, len(o), 2):
            t = o[i] 
            o[i] = o[i+1]
            o[i+1] = t
        return o