class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = [0], [0]
        minlr = []
        for h in height[:-1]:
            maxL = max(maxLeft[-1], h)
            maxLeft.append(maxL)
        for h in height[::-1][:-1]:
            maxR = max(maxRight[-1], h)
            maxRight.append(maxR)
        maxRight = maxRight[::-1]
        for i in range(len(maxLeft)):
            minlr.append(min(maxLeft[i], maxRight[i]))
        res = 0
        for i in range(len(height)):
            res = res + ((minlr[i] - height[i]) if (minlr[i] - height[i]) > -1 else 0)
        return res