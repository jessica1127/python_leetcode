'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        print "num=", num
        result = num[0] + num[1] + num[2]
        print "result =", result
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            print "i = ",i, "j= ",j," k= ",k
            while j < k:
                sum = num[i] + num[j] + num[k]
                print "sum =", sum
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                print "result=",result,"sum=",sum
            
        return result
if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    s = Solution()
    result = s.threeSumClosest(nums, target)
    print "result= ", result

