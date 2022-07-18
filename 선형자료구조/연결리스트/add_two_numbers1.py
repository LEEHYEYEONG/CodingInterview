class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 연결 리스트 뒤집기
def reverseList(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev


# 연결 리스트를 파이썬 리스트로 변환
def toList(node: ListNode) -> list:
    list1: list = []
    while node:
        list1.append(node.val)
        node = node.next
    return list1


# 파이썬 리스트를 연결 리스트로 변환
def toReverseLinkdedList(result: str) -> ListNode:
    prev: ListNode = None
    for r in result:
        node = ListNode(r)
        node.next = prev
        prev = node

    return node


# 두 연결 리스트의 덧셈
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    a = toList(reverseList(l1))
    b = toList(reverseList(l2))


    resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

    # 최종 계산 결과 연결 리스트 변환
    return toReverseLinkdedList(str(resultStr))


node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)

node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

head1 = node1
head2 = node4
node = addTwoNumbers(head1, head2)

while node:
    print(node.val)
    node = node.next
