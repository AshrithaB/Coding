"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        newnodedict = {}
        def dfs(curr):
            if curr in newnodedict:
                return newnodedict[curr]
            newnode = Node(curr.val)
            newnodedict[curr] = newnode
            for nei in curr.neighbors:
                newnode.neighbors.append(dfs(nei))
            return newnode
        dfs(node)
        return newnodedict[node]
        