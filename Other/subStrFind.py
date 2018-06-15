#coding=utf-8
#/usr/lib/python

#给定字符串， 求出其中连续是数字的子串和最大的首字符的坐标
#eg:   abc123M1234Ida78906   返回14 即：7的位置



##2.  输出字符串中最长的数字字符串和它的长度。如果有相同长度的串，则要一块儿输出，但是长度还是一串的长度   解析：简单的遍历字符串，并设置length，当连续数字串大于len时，进行交换，否则清空

def solve(arry_given):
    count = 0
    temp = []
    for i in range(0, len(arry_given)):
        if str(arry_given[i]) >= '0' and str(arry_given[i]) <= '9':
            count += 1
            temp.append(str(arry_given[i]))
        else:
            if