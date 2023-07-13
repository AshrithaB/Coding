"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        """

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':   
        if not node:
            return None
        oldtocopy = {}
        def dfs(curr):
            if curr in oldtocopy:
                return oldtocopy[curr]
            copy = Node(curr.val)
            oldtocopy[curr] = copy
            for n in curr.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        return dfs(node)

        
