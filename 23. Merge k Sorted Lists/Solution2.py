class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    def MergeTwo(list_1,list_2):
        L_current = ListNode(0)
        Head = L_current
        while list_1 or list_2:
            if list_1 and not list_2:
                L_current.next = list_1
                return Head.next
            elif not list_1 and list_2:
                L_current.next = list_2
                return Head.next
            else:
                if list_1.val <= list_2.val:
                    L_current.next = list_1
                    L_current = L_current.next
                    list_1 = list_1.next
                else:
                    L_current.next = list_2
                    L_current = L_current.next
                    list_2 = list_2.next

        return Head.next

    length = len(lists)
    interval = 1
    while interval < length:
        for i in range(0, length - interval, 2*interval):
            lists[i] = MergeTwo(lists[i], lists[i+interval] )
        interval = 2*interval
    return lists[0]


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

L = mergeKLists(lists)
for i in range(8):
    print(L.val,L.next)
    L = L.next

