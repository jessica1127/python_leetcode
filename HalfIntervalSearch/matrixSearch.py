#!/usr/bin/python env
#coding=utf-8

# There is a matrix m*n( row: m, column: n), This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
#
# Consider the following matrix:
#
# [
# [1, 3, 5, 7],
# [10, 11, 16, 20],
# [23, 30, 34, 50]
# ]
# Given target = 3, return true.   reference:
# http://www.jiuzhang.com/solution/search-a-2d-matrix#tag-highlight-lang-python
#解题思路：这道题目虽然看似矩阵问题，其实最终可以转化为一维数组，每一行按照顺序已经排好序，同事上一行末尾的元素比下一行第一个元素打，那么其实可以一次把上一行的末尾接在下一行数组前面，这样最后就把二维矩阵转化为一维的排序数组，而二维矩阵第i行第j列，在一维数组的第(i-1）*n+j-1个位置，然后由于一维排序数组已经排好序，所以用二分查找在一维排序数组里面找到对应的值就好。

class Solution:
    def matrix_search(self, matrix, target):
        m = len(matrix)    #m行，n列
        n = len(matrix[0])
        print "m={0}, n={1}".format(m, n)
        low, high = 0, m*n-1
        while low + 1 < high:
            mid = low + (high - low)//2
            print "mid={0}".format(mid)
            x = mid / n
            y = mid % n
            print "matrix[x][y]=",matrix[x][y]
            if target >= matrix[x][y]:
                low = mid
            else:
                high = mid -1
        x = low / n
        y = low % n
        if matrix[x][y] == target:
            return True
        x = high / n
        y = high % n
        if matrix[x][y] == target:
            return True
        return False

#below is official answer:
    # def searchMatrix(self, matrix, target):
    #     if len(matrix) == 0:
    #         return False
    #     n, m = len(matrix), len(matrix[0])
    #     print "search 2 m={0}, n={1}".format(m, n)
    #     start, end = 0, n * m - 1
    #     while start + 1 < end:
    #         mid = (start + end) / 2
    #         x, y = mid / m, mid % m
    #         if matrix[x][y] < target:
    #             start = mid
    #         else:
    #             end = mid
    #     x, y = start / m, start % m
    #     if matrix[x][y] == target:
    #         return True
    #
    #     x, y = end / m, end % m
    #     if matrix[x][y] == target:
    #         return True
    #
    #     return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 50]]
    s = Solution()
    ret = s.matrix_search(matrix, 11)
    # ret2 = s.searchMatrix(matrix, 7)
    print "ret =", ret
    # print "ret2=", ret2
