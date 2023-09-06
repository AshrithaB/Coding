# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def height(node):
            if not node:
                return [0, True]
            left = height(node.left)
            right = height(node.right)
            result = True if abs(left[0] - right[0]) < 2 else False
            return [(1 + max(left[0], right[0])), result and left[1] and right[1]]
            
        
        res = height(root)
        print(res)
        return res[1]