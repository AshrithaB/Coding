class Solution:
    def trap(self, height: List[int]) -> int:
        maxl, maxr = height[0], height[-1]
        l, r = 0, len(height)-1
        water = 0
        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                water += maxl - height[l] if maxl - height[l] > 0 else 0
            else:
                r -= 1
                maxr = max(maxr, height[r])
                water += maxr - height[r] if maxr - height[r] > 0 else 0
        return water