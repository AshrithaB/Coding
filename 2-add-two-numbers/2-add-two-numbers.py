# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            add = val1 + val2 + carry
            temp = ListNode(add%10)
            tail.next = temp
            tail = tail.next
            carry = add // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
        