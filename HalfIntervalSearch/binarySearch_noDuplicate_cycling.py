#/usr/bin/python
#coding:utf-8
'''
二分查找
Point 1: 不能用(low+high)//2
Point 2:  边界判断无等号
Point 3:  如果key> arr[mid], low = mid +1, 如果key<arr[mid], low = mid -1
'''
def binary_search_solution1(arr, key):
    high = len(arr) - 1
    low = 0

    while(low <= high):
        mid = low + (high - low)//2  #//在python里是向下取整   #Point 1
        if key > arr[mid]:                                     #Point 2
            low = mid +1                                      #Point 3
        elif key < arr[mid]:                                     #Point 4
            high = mid -1
        else:
            print "find your target:{0}, location is mid=arr[{1}] ".format(key, mid)
            return mid
    return -1


if __name__== '__main__':
    arr1 = [1,3,4,5,10,2,20,8,7]
    arr2 = [1,2,4,2,20,2,4,4,4,4,4,4]
    arr3 = [4,8,10,5]
    print "this is a test!"
    arr1.sort()
    arr2.sort()
    arr3.sort()
    print "arr1={0}, arr2={1}".format(arr1, arr2)
    print binary_search_solution1(arr1, 6)
    print binary_search_solution1(arr2, 4)
    print binary_search_solution1(arr3, 6)



