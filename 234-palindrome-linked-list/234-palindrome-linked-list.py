# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        prev = slow.next = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        while prev and head:
            if prev.val != head.val:
                return False
            prev, head = prev.next, head.next
        return True