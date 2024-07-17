class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        inc = True

        if nums[0] > nums[-1]:
            inc = False

        for i in range(1, len(nums)):
            if inc:
                if nums[i] < nums[i-1]:
                    # print("expecting increment, found", str(nums[i]), "less than", str(nums[i-1]))
                    return False
            else:
                if nums[i] > nums [i-1]:
                    # print("expecting decrement, found", str(nums[i]), "greater than", str(nums[i-1]))
                    return False

        return True