"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        if len(nums) == 0:
            return res
        #left:
        i = 0
        j = len(nums) - 1
        while i < j:
            m = (i + j)//2
            if nums[m] < target:
                i = m + 1
            else:
                j = m
        if nums[i] != target:
            return res
        res[0] = i


        #right:
        i = 0
        j = len(nums) - 1
        while i < j:
            m = (i + j)//2 + 1
            if nums[m] <= target:
                i = m
            else:
                j = m -1
        res[1] = i
        print "res = ", res
        return res

        
s = Solution()
nums = [5,7,7,8,8,10]
target = 8
s.searchRange(nums, target)