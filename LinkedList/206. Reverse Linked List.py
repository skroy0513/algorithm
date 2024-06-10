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
        temp = answer = ListNode(0)
        for i in array:
            answer.next = ListNode(i)
            answer = answer.next
            print(answer.val)
        print(answer)
        return temp.next

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        print(prev.val)

        return prev

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
Solution().reverseList2(head)
