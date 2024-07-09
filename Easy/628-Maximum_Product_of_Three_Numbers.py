'''
628. Maximum Product of Three Numbers

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6

Example 2:

Input: nums = [1,2,3,4]
Output: 24

Example 3:

Input: nums = [-1,-2,-3]
Output: -6

 

Constraints:

    3 <= nums.length <= 104
    -1000 <= nums[i] <= 1000


'''

def maximumProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = sorted(nums, reverse = True)
    l = len(nums)
    a = n[0] * n[1] * n[2]
    b = n[0] * n[l-1] * n[l-2]
    if a > b: return a
    return b