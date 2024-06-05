from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        array = []
        while head.next:
            array.append(head.val)
            head = head.next
        array.append(head.val)
        array.reverse()
        answer = ListNode()
        answer.next = array
        return answer.next

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
Solution().reverseList2(head)
