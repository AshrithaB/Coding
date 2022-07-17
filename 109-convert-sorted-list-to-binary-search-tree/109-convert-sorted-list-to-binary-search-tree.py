# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        m = self.mid(head)
        root = TreeNode(m.val)
        if head == m:
            return root
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(m.next)
        return root
        
    def mid(self, head):
        slow = fast = prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        return slow
            