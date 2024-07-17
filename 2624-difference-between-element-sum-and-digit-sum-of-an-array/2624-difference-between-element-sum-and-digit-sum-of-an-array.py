class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:


        DS = []

        ES = sum(nums)

        for n in nums:
            while n > 0:
                DS.append(n%10)
                n = int(n/10)

        return abs(ES - sum(DS))