# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        c = 0
        ans = None
        while s1 or s2 or c:
            v1 = s1.pop() if s1 else 0   
            v2 = s2.pop() if s2 else 0   
            c, s = divmod(v1 + v2 + c, 10)
            ans = ListNode(s, ans)            
        return ans
            
        '''tail1, tail2 = self.reverse(l1), self.reverse(l2)
        dummy = ListNode()
        add = dummy
        s, c = 0, 0
        while tail1 or tail2 or c:
            val1, val2 = tail1.val if tail1 else 0, tail2.val if tail2 else 0
            s = val1 + val2 + c
            c = s // 10
            nxtNode = ListNode(s % 10)
            add.next = nxtNode
            add = add.next
            tail1 = tail1.next if tail1 else None
            tail2 = tail2.next if tail2 else None
        return self.reverse(dummy.next)
    
    def reverse(self, head):
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev
       '''
        