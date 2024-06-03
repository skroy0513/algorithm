from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if not list1 and not list2:
        #     return None
        # elif not list1 or not list2:
        #     return list2 or list1
        # else:
            answer = temp = ListNode(0)
            while list1 and list2:
                if list1.val < list2.val:
                    temp.next = list1
                    list1 = list1.next
                else:
                    temp.next = list2
                    list2 = list2.next
                temp = temp.next

            if list1:
                temp.next = list1
            else:
                temp.next = list2

            return answer.next

list1 = ListNode(1, 3)
list2 = ListNode(1, 2)
Solution().mergeTwoLists(list1, list2)