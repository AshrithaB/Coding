class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxcontainer = 0
        l = 0
        r = len(height)-1
        while l <= r:
            if height[l] >= height[r]:
                maxcontainer = max(maxcontainer, height[r] * (r-l))
                r -= 1
            else:
                maxcontainer = max(maxcontainer, height[l] * (r-l))
                l += 1
        return maxcontainer
