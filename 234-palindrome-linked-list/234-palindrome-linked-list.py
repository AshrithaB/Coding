# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        num = []
        while head:
            num.append(head.val)
            head = head.next
        i, j = 0, len(num)-1
        while i<j :
            if num[i] != num[j]:
                return False
            i += 1
            j -= 1
        return True
        