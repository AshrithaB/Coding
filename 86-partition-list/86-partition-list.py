# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()
        right = ListNode()
        first, second = left, right
        h = head
        while h:
            if h.val < x:
                left.next = h
                left = left.next
            else:
                right.next = h
                right = right.next
            h = h.next
        left.next = second.next
        right.next = None
        return first.next
        