# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = head
        while head and head.next:
            Next = head.next
            if head.val == Next.val:
                head.next = Next.next
            else:
                head = head.next
        return h
L1 = ListNode(1)
L2 = ListNode(1)
L3 = ListNode(2)
L4 = ListNode(3)
L5 = ListNode(3)
L1.next = L2
L2.next = L3
L3.next = L4
L4.next = L5

p = Solution()
h = p.deleteDuplicates(L1)

while h:
    print(h.val)
    h = h.next
