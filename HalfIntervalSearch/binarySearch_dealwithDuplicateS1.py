#/usr/bin/python
#coding:utf-8

'''
Point 1: 带有重复的数组循环结束的条件是： low+1 < high也就是low和high不能重合, 否则会出现死循环
Point 2: 不能用(low+high)//2极端情况，low+high会越界溢出
Point 3: 如果找最大index，则判断key>= arr[mid] 否则判断key<=arr[mid]
point 4: key所在的一边，移动的边界=mid
'''
def binary_search_duplicate(arr, key):
    #如果有重复的返回最后一次出现的位置（最大值的位置）：
    low = 0
    high = len(arr) - 1
    while (low+1 < high):                  #POINT 1
        mid = low + (high - low)//2        #POINT 2
        if key >= arr[mid]:                 #POINT 3
            low = mid                        #POINT 4
        else:
            high = mid -1
    if arr[low] == key:
        return low
    elif arr[high] ==key:
        return high
    else:
        return -1

def binary_search_with_duplicate_minindex(arr, key):
    low = 0
    high = len(arr)-1
    while(low + 1 < high):
        mid = low + (high - low)//2
        if (key <= arr[mid]):
            high = mid
        else:
            low = mid + 1
    if arr[low] == key:
        return low
    elif arr[high] ==key:
        return high
    else:
        return -1


if __name__ == '__main__':
    arr1 = [1, 3, 4, 5, 10, 2, 20, 8, 7]
    arr2 = [1, 2, 4, 2, 20, 2, 4, 4, 4, 4, 4, 4]
    arr3 = [4, 8, 10, 5]
    arr4 = [1, 2, 0, 8, 10, 20, 1, 3, 4, 2, 1, 1, 1, 1, 0, 1]
    print "this is a test!"
    arr1.sort()
    arr2.sort()
    arr3.sort()
    arr4.sort()
    print "arr1={0}, arr2={1}, arr3={2}, arr4={3}".format(arr1, arr2, arr3, arr4)
    print binary_search_duplicate(arr1, 6)
    print binary_search_duplicate(arr2, 4)
    print binary_search_duplicate(arr3, 6)
    print binary_search_duplicate(arr4, 1)
    print "below is binary_search_with_duplicate_minindex"
    print binary_search_with_duplicate_minindex(arr1, 6)
    print binary_search_with_duplicate_minindex(arr2, 4)
    print binary_search_with_duplicate_minindex(arr3, 6)
    print binary_search_with_duplicate_minindex(arr4, 1)



