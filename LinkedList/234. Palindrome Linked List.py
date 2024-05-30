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
