#coding:utf-8
#/usr/lib/python

class Solution:
	def twoSum(self, num, target):
		dict = {}
		for i in xrange(len(num)):
			x = num[i]
			print "111 i = ",i, "x=",x
			if target-x in dict:
				print "222 target-x= ",target-x, "dict= ",dict
				return (dict[target-x], i)
			dict[x] = i
			print "333 dict=",dict

if __name__ == '__main__':
	num = [1,5,2,4]
	target = 6
	s = Solution()
	ret = s.twoSum(num, target)
	print "final ret = ", ret