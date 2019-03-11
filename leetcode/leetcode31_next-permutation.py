#-*- coding: utf-8
'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        #corner case:
        print "entered nextPermutation... ..."
        if len(nums) < 2:
            print "if len(nums) == 0"
            return 
        #from right-2 to left,find the first num[i] < num[i+1], mark its place to firstsmall
        firstsmall = -1
        #Decreasing cycle
        for i in range(len(nums)-2, -1, -1):
            print "i = ", i
            if nums[i] < nums[i+1]:
                firstsmall = i
                break

        print "firstsmall = ", firstsmall


        #if the given permutation is the largest string
        if firstsmall == -1:
            self.reverse(nums, 0, len(nums)-1)
            return
        #from right to left, find the first num[i] > firstsmall, -> firstlarge
        firstLarge = -1
        for i in range(len(nums)-1, 0, -1):
            print "Second i = ", i
            if nums[i] > nums[firstsmall]:
                firstLarge = i
                break
        print "firstLarge = ", firstLarge
        #swap (firstsmall, firstlarge)
        self.swap(nums, firstsmall, firstLarge)
        print "After swap nums = ", nums
        #reverse(firstsmall+1, len(nums)-1)
        self.reverse(nums, firstsmall+1, len(nums)-1)
        print "nums = ", nums
        

    def swap(self, nums, i, j):
        print "nums = ", nums
        print "i = ", i
        print "j = ", j
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        i += 1
        j -= 1

    def reverse(self, nums, start, end):
        print "entered reverse:  nums = ", nums, "start = ", start, "  end = ", end
        while  start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1
            

s = Solution()
nums = [1,2,3]
s.nextPermutation(nums)
print "final nums = ", nums
