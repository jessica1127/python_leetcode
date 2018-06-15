#!/usr/lib/python
#*coding=utf-8

'''
快速排序
本代码已经测试通过， 注意 quick_sort #POINT1： 应该是key >= A[low]  一定要带等号 否则遇到有重复的，就会死循环
这个测试好像有问题。。。。。 带看
'''

def partition(A):
    start = 0
    end = len(A) - 1
    if start < end:
        p = quick_sort(A, start, end)
        quick_sort(A, start, p-1)
        quick_sort(A, p+1, end)
    return A


def quick_sort(A, start, end):
    low, high = start, end
    key = A[low]   #POINT2 key 取A[low]
    while low < high:
        while low < high and key >= A[low]:  #POINT1
            low += 1
        A[high] = A[low]
        while low < high and key <= A[high]:  #POINT1
            high -= 1
        A[low] = A[high]
        A[low] = key  #POINT 3 别忘了最后把key赋值给A【low】
    return low


s = [6, 8, 1, 4, 3, 9, 5, 4, 11, 2, 2, 15, 6]
print "Before sort: s= ", s

a = partition(s)
print "After sort: s=", a
