# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def height(head):
            if not head:
                return 0
            return 1 + max(height(head.left), height(head.right))
        
        level = height(root)
        if level == 1:
            return True
        q = deque()
        q.append(root)
        l = 0
        end = 0
        res = []
        while q and l < level:
            inside = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    inside.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)  
                else:
                    inside.append("N")
            l += 1
            res.append(inside)
            flag = 0
            if "N" in inside:
                if l < level:
                    return False
                for i in range(len(inside)-1):
                    if inside[i] == "N":
                        flag = 1
                    if flag == 1 and str(inside[i+1]).isdigit():
                        return False
        return True
        