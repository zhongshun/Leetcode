class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    if not lists  or lists == len(lists)*[None]:
        return []
    L_current = ListNode(0)
    p = L_current
    for test_None in range(len(lists)-1,-1,-1):
        if not lists[test_None]:
            lists = lists[0:test_None] + lists[test_None+1:]

    while lists:
        value = [l.val for l in lists]
        k = value.index(min(value))
        p.next = lists[k]
        if lists[k].next:
            lists[k] = lists[k].next
        else:
            lists = lists[0:k] + lists[k+1:]
        p = p.next
    return L_current.next

L1 = ListNode(1)
L2 = ListNode(4)
L3 = ListNode(5)
L1.next = L2
L2.next = L3

B1 = ListNode(1)
B2 = ListNode(3)
B3 = ListNode(4)
B1.next = B2
B2.next = B3

C1 = ListNode(2)
C2 = ListNode(6)
C1.next = C2

lists = [L1,B1,C1]
#value = [l.val for l in lists]
#k = value.index(min(value))
#print(lists[k].val)
#lists[k] = lists[k].next
#print(lists[k].val)
L = mergeKLists(lists)
for i in range(8):
    print(L.val,L.next)
    L = L.next

