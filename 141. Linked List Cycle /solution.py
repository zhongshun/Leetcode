# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        if not head.next: return False

        slow = head
        fast = head

        while fast and fast.next:
            if not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow2 = head
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next
            return slow.val

        return None

p1 = ListNode(3)
p2 = ListNode(2)
p3 = ListNode(0)
p4 = ListNode(-4)

p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p2

S = Solution()
print(S.hasCycle(p1))
