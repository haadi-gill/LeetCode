class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = sorted(nums)
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums = sorted(self.nums + [val])
        
        if len(self.nums) < self.k:
            return None
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)