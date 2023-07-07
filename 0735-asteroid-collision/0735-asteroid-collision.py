class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 1
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                temp = stack[-1] + a
                if temp < 0:
                    stack.pop()
                elif temp == 0:
                    a = 0
                    stack.pop()
                else:
                    a = 0
            if a:
                stack.append(a)
        return stack
