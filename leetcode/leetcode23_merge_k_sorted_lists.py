#-*-coding: utf-8
'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''
import heapq


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        print "000 lists=",lists
        current = sentinel = ListNode(-1)
        lists = [(i.val, i) for i in lists if i] 
        heapq.heapify(lists)  #调整成最小堆
        while lists:
            current.next = heapq.heappop(lists)[1]   #弹出最小值
            print "current.next==", current.next
            current = current.next
            if current.next:
                heapq.heappush(lists, (current.next.val, current.next))
        return sentinel.next

          

if __name__ == '__main__':
    list1_node1 = ListNode(1)
    list1_node2 = ListNode(4)
    list1_node3 = ListNode(5)
    list1_node1.next = list1_node2
    list1_node2.next = list1_node3
    list2_node1 = ListNode(1)
    list2_node2 = ListNode(3)
    list2_node3 = ListNode(4)
    list2_node1.next = list2_node2
    list2_node2.next = list2_node3
    list3_node1 = ListNode(2)
    list3_node2 = ListNode(6)
    list3_node1.next = list3_node2
    input = []
    input.append(list1_node1)
    input.append(list2_node1)
    input.append(list3_node1)
    for item in input:
        while  item:
            print item.val,
            item = item.next
        print ""
    s = Solution()
    res = s.mergeKLists(input)
    while res:
        print "res.val= ", res.val
        res = res.next
