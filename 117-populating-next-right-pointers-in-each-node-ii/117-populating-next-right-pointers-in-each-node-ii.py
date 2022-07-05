"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        q = deque()
        q.append(root)
        while len(q):
            size = len(q)
            dummy = Node()
            while size > 0:
                node = q.popleft()
                dummy.next = node
                dummy = dummy.next
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                size = size - 1
        return root
                
        