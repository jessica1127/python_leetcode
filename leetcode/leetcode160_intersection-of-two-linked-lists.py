"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 

Example 2:


Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 

Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
       
        listA, listB = headA, headB
        numA, numB = 0, 0
        while listA is not None:
            numA += 1
            listA = listA.next
        while listB is not None:
            numB += 1
            listB = listB.next
        listA, listB = headA, headB
        print "000 listA.val = ", listA.val 
        print "000 listB.val = ", listB.val
        if numA > numB:
            for i in range(numA - numB):
                listA = listA.next
        elif numB > numA:
            for i in range(numB - numA):
                listB = listB.next
        print "listA.val = ", listA.val 
        print "listB.val = ", listB.val
        while listA != listB:
            print "111 listA.val = ", listA.val 
            print "111 listB.val = ", listB.val
            listA = listA.next
            listB = listB.next
        # print "222 listA.val = ", listA.val 
        # print "222 listB.val = ", listB.val
        return listA




headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = ListNode(8)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)
headB = ListNode(5)
headB.next = ListNode(0)
headB.next.next = ListNode(1)
headB.next.next.next = ListNode(8)
headB.next.next.next.next = ListNode(4)
headB.next.next.next.next.next = ListNode(5)
s = Solution()
ret =  s.getIntersectionNode(headA, headB)
if not ret:
    print ret
else:
    print ret.val


















