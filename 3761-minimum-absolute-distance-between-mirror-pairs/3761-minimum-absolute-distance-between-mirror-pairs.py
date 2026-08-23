class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        distance = {}
        minDistance = len(nums)

        for a in range(len(nums)):
            if nums[a] in distance:
                b = distance[nums[a]]
                if (a - b < minDistance):
                    minDistance = a-b
                
            flipped = flip(nums[a])
            distance[flipped] = a
            
        if minDistance == len(nums):
            return -1
        return minDistance
        
def flip(num: int) -> int:
    newNum = 0
    while(num > 0):
        newNum *= 10
        newNum += num % 10
        num //= 10
    return newNum