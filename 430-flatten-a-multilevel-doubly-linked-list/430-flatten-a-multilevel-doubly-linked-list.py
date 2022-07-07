"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head:
            self.flat(head)
        return head
    
    def flat(self, head):
        cur = tail = head
        while cur:
            child = cur.child
            nxt = cur.next
            if cur.child:
                tail = self.flat(child)
                tail.next = nxt
                if nxt:
                    nxt.prev = tail
                cur.next = child
                child.prev = cur
                cur.child = None
                cur = tail
            else:
                cur = nxt
            if cur:
                tail = cur
        return tail
            