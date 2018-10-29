# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        New_head = ListNode(0)
        New_head.next = head
        pre = New_head
        while head and head.next:
            L1 = head
            L2 = head.next

            pre.next = L2
            L1.next = L2.next
            L2.next = L1

            head = L1.next
            pre = L1
        return New_head.next

L1 = ListNode(1)
L2 = ListNode(2)
L3 = ListNode(3)
L4 = ListNode(4)
L5 = ListNode(5)
L6 = ListNode(6)
L1.next = L2
L2.next = L3
L3.next = L4
L4.next = L5

Head = L1

p = Solution()
h = p.swapPairs(Head)
for i in range(5):
    print(h.val)
    h=h.next
