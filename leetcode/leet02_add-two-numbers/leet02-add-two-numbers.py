# -*-coding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #判断某个链表是否为None，如果是则返回另一个exit
        #
        if l1 == None: return l2
        if l2 == None: return l1
        h1 = l1
        h2 = l2 
        #只有两个链表的下一个节点数都为None，退出循环
        #
        while h1.next is not None or h2.next is not None:
            if h1.next == None: h1.next = ListNode(0)
            if h2.next == None: h2.next = ListNode(0)
            h1.val = h1.val + h2.val
            #当相加结果>=10,当前结果节点为个位数，下个节点+1
            if h1.val >= 10:
                h1.val = h1.val %10
                h1.next.val += 1
            h1=h1.next
            h2=h2.next
        
        h1.val = h1.val + h2.val
        if h1.val >= 10:
            h1.val = h1.val%10
            h1.next = ListNode(1)
        return l1  #问题： 为什么改变的是h1这里返回的还是l1？？如果返回h1就错误。 
        #原因l1是指到链表的地址的修改h1就是修改内存的一块地址，所以应该返回l1


    def printlist(self, l):
        while l.next is not None:
            print l.val,
            l = l.next
        else:
            print l.val
 
if __name__ == '__main__':
    '''
    l1: 1->2->6->7
    l2: 9->3->4->1
    return 0->6->0->9
    '''
    l1node1 = ListNode(1)
    l1node2 = ListNode(2)
    l1node3 = ListNode(6)
    l1node4 = ListNode(7)
    l1node1.next = l1node2
    l1node2.next = l1node3
    l1node3.next = l1node4
    
    l2node1 = ListNode(9)
    l2node2 = ListNode(3)
    l2node3 = ListNode(4)
    l2node4 = ListNode(1)
    l2node1.next = l2node2
    l2node2.next = l2node3
    l2node3.next = l2node4

    l1 = l1node1
    l2 = l2node1
    s = Solution()
    print "*** l1="
    s.printlist(l1)
    print "*** l2="
    s.printlist(l2)
    ret_l = s.addTwoNumbers(l1, l2)
    
    print "*** ret_l="
    s.printlist(ret_l)

