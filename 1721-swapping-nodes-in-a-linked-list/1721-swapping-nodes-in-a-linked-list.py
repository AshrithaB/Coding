# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first, second = head, head
        while k-1:
            second = second.next
            k -= 1
        second2 = second
        while second2.next:
            first = first.next
            second2 = second2.next
        first.val, second.val = second.val, first.val
        return head