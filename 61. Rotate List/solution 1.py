# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int-
        :rtype: ListNode
        """
        if not head:
            return []
        p = head
        l = 1
        while p.next:
            p = p.next
            l = l + 1
        p.next = head

        p1 = head
        p2 = head.next
        k1 = k%l
        for i in range(l - k - 1):
            p1 = p1.next
            p2 = p2.next
        p1.next = None
        return p2

P1 = ListNode(1)
P2 = ListNode(2)
P3 = ListNode(3)
P4 = ListNode(4)
P5 = ListNode(5)

P1.next = P2
P2.next = P3
P3.next = P4
P4.next = P5

k = 2


p = Solution()
H = p.rotateRight(P1,k)
while H:
    print(H.val)
    H = H.next
