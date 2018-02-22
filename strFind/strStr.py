#coding:utf-8
#/usr/bin/python

def strStr(source, target):
    s_length = len(source)
    t_length = len(target)
    for item in range(s_length-t_length+1):
        if source[item:item+t_length] == target:
            print "Find your target {},index is {}".format(target,item)
            return item
    print "can't find your target"
    return -1


if __name__ == '__main__':
    source1 = '1abc123456'
    source2 = '12333445555566abc123334455555661233344555556612333445555566'
    target1 = '12333445555566'
    strStr(source1, target1)
    strStr(source2, target1)
