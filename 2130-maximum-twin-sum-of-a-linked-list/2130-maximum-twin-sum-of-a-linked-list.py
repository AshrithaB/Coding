# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        first, cur = head, slow.next
        prev = slow.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        second = prev
        maxTwinSum = 0
        while second:
            maxTwinSum = max(maxTwinSum, first.val + second.val)
            first, second = first.next, second.next
        return maxTwinSum
        