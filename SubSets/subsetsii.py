#coding:utf-8
#/usr/lib/python
'''
# Time:  O(n * 2^n)
# Space: O(1)

# Given a collection of integers that might contain duplicates, S, return all possible subsets.
# 
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,2], a solution is:
# 
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
https://github.com/kamyu104/LeetCode/blob/master/Python/subsets-ii.py
'''
class Solution(object):
    def subSetsii(self, nums):
        nums.sort()
        result = [[]]
        previous_size = 0
        for i in xrange(len(nums)):
            print "i = {}".format(i)
            size = len(result)
            print "size = {}".format(size)
            for j in xrange(size):
                print "j = {}".format(j)
                if i == 0 or nums[i] != nums[i-1] or j >= previous_size:
                    print "result1 = {}".format(result)
                    result.append(list(result[j]))
                    print "result2 = {}".format(result)
                    result[-1].append(nums[i])
                    print "result3 = {}".format(result)
            previous_size = size
        return result
    
    
    
if __name__ == '__main__':
    print Solution().subSetsii([0,9,0,9])