#coding:utf-8
#/usr/bin/python
#参考： https://www.cnblogs.com/zingp/p/6537841.html

def bubble_sort(array):
    '''
    冒泡排序，第一趟：相邻的两个数比较，大的往下沉，最后一个元素是最大的
    第二趟：相邻两个数相比，大的往下沉，最后一个元素不用比
    :param array: 时间复杂度O(n^)
    稳定性：稳定的
    :return: 
    '''
    print "Before Sort array={}".format(array)
    for i in range(len(array)-1):      #Point 1   i是全循环
        for j in range(len(array)-i-1):    #Point 2   j最后一个元素不用比
            print "i={0}, j={1}".format(i, j)
            if array[j] > array[j+1]:        #Point 3   是array[j] 和array[j+1]比较不是和array[i]比较
                array[j], array[j+1] = array[j+1], array[j]     #Point 4  python一次可以交换两个
    print "Sorted array={}".format(array)

'''
如果一趟比较没有发生位置交换，则认为排序完成。
'''

def bubble_sort2(array):
    continue_status = False
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                print "i={0}, j={1}".format(i, j)
                continue_status = True
        if not continue_status:                #如果没有发生位置交换，跳出外层循环
            break
    print "Sorted array={}".format(array)


def select_sort(array):
    '''
    直接选择排序：每一次排序从待排序的数据元素中选出最小（或最大的）存放到序列的起始位置，直到全部排完
    :param array: 时间复杂度：O(n^2)
    稳定性：不稳定
    :return: 
    '''
    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if (array[j]<array[min]):
                min = j
        array[min], array[i] = array[i], array[min]
        print "Sorted array={}".format(array)

    print "Final Sorted array={}".format(array)


def insert_sort(array):
    '''
    列表被分为有序区和无序区两个部分。最初有序区只有一个元素。
    每次从无序区选择一个元素，插入到有序区的位置，直到无序区变空。
    其实就相当于摸牌：
    :param array: 时间复杂度：O(n^2)
    稳定性：稳定
    :return: 
    Point 1: 循环的是第二个到最后（待摸的牌
    Point 2:  待插入的数（摸上来的牌）
    Point 3: 已排好序的最右边一个元素（手里的牌的最右边）
    '''
    print "Before sort={}".format(array)
    for i in range(1, len(array)):   #Point 1
        min = array[i]               #Point 2
        j = i - 1                    #Point 3
        while j >= 0 and array[j] > min:
            # 一只和排好的牌比较，排好的牌的牌的索引必须大于等于0
            #  比较过程中，如果手里的比摸上来的大，
            array[j+1] = array[j]
            j -= 1   #换完以后在和下一张比较
            print "Sorted array={}".format(array)
        #找到了手里的牌比摸上来的牌小或等于的时候，就把摸上来的放到它右边
        array[j+1] = min
        print "Final Sorted array={}".format(array)

'''
接下来两个方法是对快排：
一般取最左边的数作为参照， 一次排序下来左边都是比参照数小的， 右边都是比参照数(tmp)大的
取一个元素p（通常是第一个元素，但是这是比较糟糕的选择），使元素p归位（把p右边比p小的元素都放在它左边，在把空缺位置的左边比p大的元素放在p右边）；
列表被p分成两部分，左边都比p小，右边都比p大；
python sort.py 
len(array2)==== 12
Before sort=[100, 0, 80, 2, 2, 50, 20, 19, 20, 29, 5, 0]
hi
000 [0, 0, 80, 2, 2, 50, 20, 19, 20, 29, 5, 0]
Final Sorted array=[0, 0, 80, 2, 2, 50, 20, 19, 20, 29, 5, 100]
mid = 11
Before sort=[0, 0, 80, 2, 2, 50, 20, 19, 20, 29, 5, 100]
hi
000 [0, 0, 80, 2, 2, 50, 20, 19, 20, 29, 5, 100]
Final Sorted array=[0, 0, 80, 2, 2, 50, 20, 19, 20, 29, 5, 100]
mid = 0
Before sort=[0, 0, 80, 2, 2, 50, 20, 19, 20, 29, 5, 100]
hi
000 [0, 0, 80, 2, 2, 50, 20, 19, 20, 29, 5, 100]
Final Sorted array=[0, 0, 80, 2, 2, 50, 20, 19, 20, 29, 5, 100]
mid = 1
Before sort=[0, 0, 80, 2, 2, 50, 20, 19, 20, 29, 5, 100]
hi
000 [0, 0, 5, 2, 2, 50, 20, 19, 20, 29, 5, 100]
Final Sorted array=[0, 0, 5, 2, 2, 50, 20, 19, 20, 29, 80, 100]
mid = 10
Before sort=[0, 0, 5, 2, 2, 50, 20, 19, 20, 29, 80, 100]
hi
000 [0, 0, 2, 2, 2, 50, 20, 19, 20, 29, 80, 100]
Final Sorted array=[0, 0, 2, 2, 5, 50, 20, 19, 20, 29, 80, 100]
mid = 4
Before sort=[0, 0, 2, 2, 5, 50, 20, 19, 20, 29, 80, 100]
hi
000 [0, 0, 2, 2, 5, 50, 20, 19, 20, 29, 80, 100]
Final Sorted array=[0, 0, 2, 2, 5, 50, 20, 19, 20, 29, 80, 100]
mid = 2
Before sort=[0, 0, 2, 2, 5, 50, 20, 19, 20, 29, 80, 100]
hi
000 [0, 0, 2, 2, 5, 29, 20, 19, 20, 29, 80, 100]
Final Sorted array=[0, 0, 2, 2, 5, 29, 20, 19, 20, 50, 80, 100]
mid = 9
Before sort=[0, 0, 2, 2, 5, 29, 20, 19, 20, 50, 80, 100]
hi
000 [0, 0, 2, 2, 5, 20, 20, 19, 20, 50, 80, 100]
Final Sorted array=[0, 0, 2, 2, 5, 20, 20, 19, 29, 50, 80, 100]
mid = 8
Before sort=[0, 0, 2, 2, 5, 20, 20, 19, 29, 50, 80, 100]
hi
000 [0, 0, 2, 2, 5, 19, 20, 19, 29, 50, 80, 100]
Final Sorted array=[0, 0, 2, 2, 5, 19, 20, 20, 29, 50, 80, 100]
mid = 7
Before sort=[0, 0, 2, 2, 5, 19, 20, 20, 29, 50, 80, 100]
hi
000 [0, 0, 2, 2, 5, 19, 20, 20, 29, 50, 80, 100]
Final Sorted array=[0, 0, 2, 2, 5, 19, 20, 20, 29, 50, 80, 100]
mid = 5
特点：不稳定，就是快。
'''

def quick_sort(array, left, right):
    if left < right:
        mid = partition(array, left, right)
        print "mid =", mid
        quick_sort(array, left, mid-1)
        quick_sort(array, mid+1, right)



def partition(array, left, right):
    tmp = array[left]
    print "Before sort={}".format(array)
    while left < right:
        print "hi"
        while left < right and array[right] >= tmp:
            right -= 1
        array[left] = array[right]
        print "000",array
        while left < right and array[left] <= tmp:
            left += 1
        array[right] = array[left]
    array[left] = tmp
    print "Final Sorted array={}".format(array)
    print "left====", left
    return left




if __name__=='__main__':
    array1 = [0, 100, 10, 50, 1, 2, 8, 9, 70, 20, 1]
    array2 = [100, 0, 80, 2, 2, 50, 20, 19, 20, 29, 5, 0]
    #print bubble_sort2(array2)
    #print select_sort(array2)
    #print insert_sort(array2)
    print "len(array2)====",len(array2)
    quick_sort(array2, 0, 11)

  