class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        water = 0
        while l < r:
            if height[l] < height[r]:
                water = max(water, height[l]*(r-l))
                l += 1
            else:
                water = max(water, height[r]*(r-l))
                r -= 1
        return water

        