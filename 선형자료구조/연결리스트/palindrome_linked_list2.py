import collections
from typing import Deque


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    q: Deque = collections.deque()

    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4

print(isPalindrome(head))
