#coding:utf-8
#/usr/lib/python
'''
http://blog.csdn.net/leorx01/article/details/64440492
求ABCDEF到第一次poker后的顺序,即桌面牌的顺序。
'''
def start_to_end(list=[]):
    if len(list) <= 1:
        pass
    else:
        list.append(list[0])
        list.pop(0)

    return list



aim_list = ['A','B','C','D','E','F']
result = []


for i in range(len(aim_list)):
    print "i=",i
    result.append(aim_list[0])
    aim_list.pop(0)
    start_to_end(aim_list)

print result




