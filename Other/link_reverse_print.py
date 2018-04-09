#coding:utf-8
#/usr/lib/python

'''
输入一个链表，从尾到头打印链表每个节点的值。
'''

class List:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_list(head):
    if head is None or head.next is None :
        return head
    pre = None
    cur = head
    h = head
    while cur:
        h = cur
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return h

def printListFromTailToHead(List):
    '''
    分析： 
    1. 用一个数组保存每个节点的值 
    2. 再倒序输出 
    在 python 里似乎很容易，如下代码，本题主要考查对链表的性质的理解。 
    '''
    a = []
    while List:
        a.append(List.value)
        List = List.next
    return a[::-1]





if __name__ == '__main__':
    head = List(1)
    p1 = List(2)
    p2 = List(3)
    p3 = List(4)

    head.next = p1
    p1.next = p2
    p2.next = p3
    p = reverse_list(head)

    while p:
        print p.value
        p = p.next

    print "second method==", printListFromTailToHead(head)



