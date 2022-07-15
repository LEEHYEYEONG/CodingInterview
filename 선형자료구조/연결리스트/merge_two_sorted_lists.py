class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = mergeTwoLists(l1.next, l2)
    return l1


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

l1 = node1
l2 = node4

mergeTwoLists(l1, l2)

while l1:
    print(l1.val)
    l1 = l1.next
