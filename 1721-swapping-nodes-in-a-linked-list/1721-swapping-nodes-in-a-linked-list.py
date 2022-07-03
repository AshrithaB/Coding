# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head
        while k-1:
            right = right.next
            k -= 1
        start = right
        while right:
            left = left.next
            right = right.next
        end = left
        start.val, end.val = end.val, start.val
        return dummy.next
            
            