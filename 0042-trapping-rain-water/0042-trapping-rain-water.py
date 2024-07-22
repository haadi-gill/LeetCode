class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1

        maxL, maxR = height[l], height[r]

        trappedWater = 0

        while l < r:
            if (maxL < maxR):
                l += 1
                maxL = max(maxL, height[l])
                trappedWater += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                trappedWater += maxR - height[r]

        return trappedWater