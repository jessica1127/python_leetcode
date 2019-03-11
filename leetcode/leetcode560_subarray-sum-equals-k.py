'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
'''
import collections

class Solution(object):
    def subarraySum(self, A, K):
        count = collections.Counter()
        print "count = ", count
        count[0] = 1
        ans = su = 0
        for x in A:
            su += x
            ans += count[su-K]
            count[su] += 1
            print " x = ", x, " su = ", su, " ans = ", ans, " count = ", count
        return ans

    def subarraySum2(self, A, K):
        '''
        A[j] - A[i]
        find out number of A[j] - A[i] == K
        '''
        n = len(A)
        num = 0
        for i in range(n):
            preSum = 0
            for j in range(i, n):
                preSum += A[j]
                if preSum == K:
                    num += 1
        return num

    def subarraySum3(self, A, K):
        '''
        i can be 0, so we need preFixSum['0'] = 1
        preFixSum(i, j) = preFexSum(j) - preFixSum(i-1)
        find where i<j: preFixSum(j) - preFixSum(i) == K
        that is: 
        preFixSum(i) = preFIxSum(j) - K
        key -: prefixSum value
        value -: of occurrence of the prefixSum value
        '''

        count =collections.Counter()
        count[0] = 1
        sum = 0
        ans = 0
        for a in A:
            print "a = ", a
            sum += a
            print "sum = ", sum
            print "sum - K=", sum-K
            ans = ans + count[sum - K]
            print "count[",sum - K,"] = ", count[sum - K]
            print "ans = ", ans
            count[sum] += 1  
            print "count[",sum,"] = ", count[sum], "sum = ", sum
            print "-------"
        return ans
      

s = Solution()
A = [1,1,1]
K = 2
print s.subarraySum3(A, K)