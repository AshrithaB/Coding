class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                temp = stack[-1] + a
                if temp < 0:
                    stack.pop()
                elif temp == 0:
                    stack.pop()
                    a = 0
                else:
                    a = 0
            if a:
                stack.append(a)
        return stack
