#coding:utf-8
#/usr/lib/python
'''
# Time:  O(n * 2^n)
# Space: O(1)

# Given a set of distinct integers, S, return all possible subsets.
# 
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,3], a solution is:
# 
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
'''
class Solution(object):
    def subset(self, nums):
        '''
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        print "before sort nums===", nums
        nums.sort()
        print "nums===",nums
        result = [[]]
        for i in xrange(len(nums)):
            print "i==",i
            size = len(result)
            print "size=",size
            for j in xrange(size):
                print "j=",j
                result.append(list(result[j]))
                print "result1=",result
                result[-1].append(nums[i])
                print "result2=", result
        return result




if __name__ == "__main__":
    print Solution().subset([1,2,3])
