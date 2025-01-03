class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)

        ways = 0
        currSum = 0

        for i in range(len(nums)-1):
            currSum += nums[i]
            total -= nums[i]

            if currSum >= total:
                ways += 1
        
        return ways