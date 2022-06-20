class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        maxL, maxR = height[0], height[-1]
        l, r = 0, len(height)-1
        water = 0
        while l<r:
            if maxL <= maxR:
                l += 1
                if min(maxL, maxR) - height[l] > 0:
                    water += min(maxL, maxR) - height[l]
                maxL = max(maxL, height[l])
            else:
                r -= 1
                if min(maxL, maxR) - height[r] > 0:
                    water += min(maxL, maxR) - height[r]
                maxR = max(maxR, height[r])
        return water
            
            