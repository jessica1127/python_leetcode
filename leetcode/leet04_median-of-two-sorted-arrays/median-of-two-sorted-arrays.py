#-*-coding:utf-8

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num = nums1 + nums2
        num = sorted(num)
        if len(num) == 0:
            return None
        elif len(num) != 0 and len(num) % 2 == 0: #偶数个元素
            return (num[len(num)//2-1] + num[len(num)//2])/2.0
        else:
            return num[len(num)//2]

if __name__ == '__main__':
    num1 = [1, 3]
    num2 = [2]
    s = Solution()
    median = s.findMedianSortedArrays(num1, num2)
    print "the median is: ", median