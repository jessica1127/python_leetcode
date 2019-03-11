'''
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
'''
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i, res = 0, []
        if len(nums) == 0:
            return res
        if len(nums) == 1:
            res.append(str(nums[0]))
        #for len(nums) >= 2
        while i < len(nums):
            start = i
            while i+1 < len(nums) and nums[i+1] - nums[i] == 1:
                i += 1
            if len(nums[start:i+1]) == 1:
                tmp_str = str(nums[start:i+1][0])
            else:
                tmp_str = str(nums[start:i+1][0]) + "->" + str(nums[start:i+1][-1])
            res.append(tmp_str)
            i += 1
        return res
        
s = Solution()
nums = [0,1,2,4,5,7]
print s.summaryRanges(nums)