class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if stack:
                    top = stack.pop()
                else:
                    return False
                if ch == ')':
                    if top != '(':
                        return False
                elif ch == ']':
                    if top != '[':
                        return False
                elif ch == '}':
                    if top != '{':
                        return False
        return True if len(stack) == 0 else False