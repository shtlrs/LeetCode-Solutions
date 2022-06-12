# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        n1 = head
        n2 = head
        
        while n2 and n2.next:
            
            n1 = n1.next
            n2 = n2.next.next
            if n1 == n2:
                return True
            
        return False