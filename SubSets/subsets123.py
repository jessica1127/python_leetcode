#coding=utf-8
class Solution(object):
    def subSet(self, nums):
        nums.sort()
        result = [[]]
        for i in xrange(len(nums)):
            print "i=",i
            size = len(result)
            for j in xrange(size):
                print "j=",j
                result.append(list(result[j]))
 		result[-1].append(list(num[i]))
	return result

if __name__ == '__main__':
    print Solution().subset([1,2,3])
    

