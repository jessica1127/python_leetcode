"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
"""
class Solution(object):
    def removeElement1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for item in nums[:]:
            #print "item= ",item," nums= ", nums," val= ",val, " nums[:] = ",nums[:]
            if item == val:
                nums.remove(val)
        nums = nums[:]
# two pointers solution
    def removeElement(self, nums, val):
        i = 0
        for j in range(len(nums)):
            print "nums[j] = ", nums[j], " nums = ",nums
            if nums[j] == val:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
            print "i = ",i
        print "nums[:i] = ", nums[:i]
        nums = nums[:i]

if __name__ == '__main__':
    s = Solution()
    nums = [3,3,3, 2,2,3]
    val = 3
    s.removeElement(nums, val)
