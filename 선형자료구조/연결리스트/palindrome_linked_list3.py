class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4

print(isPalindrome(head))
