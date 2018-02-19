#/usr/lib/python
#coding:utf-8

#给定字符串source，希望在source中查找到第一次出现target字符串的位置。
#以下实现的strStr是O(n2)级的， 另外有o(m+n)的时间复杂度，KMP算法，比较复杂， 参考：
#http://blog.csdn.net/handsomekang/article/details/40978213


def strStr(source, target):
    # write your code here
    s_len = len(source)
    t_len = len(target)
    for i in range(s_len - t_len + 1):
        print "i=",i
        if source[i:i+t_len] == target:
            print "find i=",i
            return True
    return False


    # print source.find(target)

if __name__ == '__main__':
    print strStr('abcddddddddddd', 'dddd')
    print strStr('123snffffffff' ,'sf')