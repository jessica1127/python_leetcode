'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permute = [[]]
        if nums is None or len(nums) == 0:
            return permute
        for n in nums:
            tmp_perm = []
            for per in permute:
                for i in xrange(len(per) + 1):
                    tmp_perm.append(per[:i] + [n] + per[i:])
            permute = tmp_perm
            print "permute = ", permute

        return permute
s = Solution()
nums = [1,2,3]
print s.permute(nums)