import collections
from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        list = []
        sample = head
        while sample:
            list.append(sample.val)
            sample = sample.next

        while len(list) > 1:
            if list.pop(0) != list.pop():
                return False

        return True

    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        deque = collections.deque()
        sample = head
        while sample:
            deque.append(sample.val)
            sample = sample.next

        while len(deque) > 1:
            if deque.popleft() != deque.pop():
                return False

        return True

    def isPalindrome3(self, head: Optional[ListNode]) -> bool:
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