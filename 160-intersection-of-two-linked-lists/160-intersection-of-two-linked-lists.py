# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tailA, tailB = headA, headB
        while tailA != tailB:
            tailA = tailA.next if tailA else headB
            tailB = tailB.next if tailB else headA
        return tailA