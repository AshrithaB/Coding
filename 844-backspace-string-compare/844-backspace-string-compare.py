class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sStack, tStack = [], []
        for ch in s:
            if ch == '#':
                if sStack:
                    sStack.pop()
            else:
                sStack.append(ch)
        for ch in t:
            if ch == '#':
                if tStack:
                    tStack.pop()
            else:
                tStack.append(ch)
        return sStack == tStack
        
        