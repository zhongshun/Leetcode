class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p_next = ListNode(0)
        P = p_next
        carry = 0
        while l1 != None or l2 != None or carry:
            if l1 != None:
                carry = l1.val + carry
                l1 = l1.next
            if l2 != None:
                carry = l2.val + carry
                l2 = l2.next
            p_next.next = ListNode(carry%10)
            carry //= 10
            p_next = p_next.next
        return P.next
