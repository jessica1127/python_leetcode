#coding:utf-8
#/usr/lib/python


'''
已知第一次后的桌面牌顺序ACEBFD， 求原来手中牌顺序ABCDEF。
手中一副扑克牌，假设顺序为ABCDEF，把第一张放到桌面上，第二张挪到最后，第三张放到桌面，第四章放到最后，一直到所有牌都在桌面

BCDEF    A
CDEFB
DEFB     AC
EFBD
...
http://blog.csdn.net/leorx01/article/details/64440492
排序牌面：ACEBFD

桌面扑克牌	原始扑克牌	说明
ACEBF	    D	拿出末尾最后一个D
ACEB	    FD	拿出末尾最后一个F，放到D前面得到新牌面
ACE	        BDF	原始扑克牌重新排序(最后一个牌放到第一位)，拿出末尾最后一个B，放到新排序牌面之前
AC	        EFBD	原始扑克牌重新排序(最后一个牌放到第一位)，拿出末尾最后一个E，放到新排序牌面之前
A	        CDEFB	原始扑克牌重新排序(最后一个牌放到第一位)，拿出末尾最后一个C，放到新排序牌面之前
ABCDEF	            获得原始牌面
'''


def end_to_start2(list=[]):
    if len(list) <= 1:
        pass
    else:
        list.insert(0, list[-1])
        list.pop()
    return list




#把列表的最后一个元素放到第一位：

def end_to_start(list=[]):
    if len(list)<=1:
        pass
    else:
        list.insert(0, list[-1])
        list.pop()    ## pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。
    return list


aim_list = ['A', 'C', 'E', 'B', 'F', 'D']
result = [] #起始牌面





for i in range(len(aim_list), 0, -1):  #range(start, stop, step),从start开始，stop结束，step为步长stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5， 所以这i应该取6，5，4，3，2，1
    print "i=", i
    end_to_start(result)
    print "11 result =", result
    result.insert(0, aim_list[i-1])
    print "22 result =", result

print result



