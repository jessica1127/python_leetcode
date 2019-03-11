'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #find the middle
        #reverse the slow to end
        #compare first part and seconde(reversed part)
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        pre = None
        while slow:
            tmp = slow.next
            slow.next = pre
            pre = slow
            slow = tmp
        first , second = head, pre
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True

s = Solution()
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(1)
head.next.next.next = ListNode(1)
print s.isPalindrome(head)        
                
