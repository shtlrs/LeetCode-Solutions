from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        head = head
        if not head:
            return None

        while head.val == val:
            head = head.next
            if not head:
                return None

        node = head

        while node:
            if node.next and node.next.val == val:
                node.next = node.next.next
                continue
            node = node.next
        return head