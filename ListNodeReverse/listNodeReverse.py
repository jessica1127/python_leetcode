#coding:utf-8
#/usr/lib/python
#http://blog.csdn.net/u011608357/article/details/36933337

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def nonerecurse(head):
    '''
    非递归实现单链表反转
    :param head: 
    :return: 
    '''
    if head is None or head.next is None:
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



def recurse(head, newhead):
    '''
    递归方式
    :param head: 
    :param newhead: 
    :return: 
    '''
    if head is None:
        return
    if head.next is None:
        newhead = head

    else:
        newhead = recurse(head.next, newhead)
        head.next.next = head
        head.next = None
    return newhead








if __name__ == '__main__':
    # head = ListNode(1)
    # p1 = ListNode(2)
    # p2 = ListNode(3)
    # p3 = ListNode(4)
    # head.next = p1
    # p1.next = p2
    # p2.next = p3
    #
    #
    # p = nonerecurse(head)
    # print '===1111==',p
    # while p:
    #     print p.value
    #     p = p.next

    head = ListNode(1)
    p1 = ListNode(2)
    p2 = ListNode(3)
    p3 = ListNode(4)

    head.next = p1
    p1.next = p2
    p2.next =p3
    newhead = None

    p = recurse(head, newhead)
    while p :
        print p.value
        p = p.next
